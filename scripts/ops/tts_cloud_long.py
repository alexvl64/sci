#!/usr/bin/env python3
"""SparkCore -- Generate long-form audio via Google Cloud TTS Neural2 (or Studio).

Splits text by paragraph (max ~4500 chars/chunk to stay under 5000 bytes API limit),
calls Cloud TTS per chunk, concatenates with ffmpeg.

Why Cloud TTS Neural2 over Gemini TTS Flash :
- No undocumented audio-duration cap (Gemini Flash compresses long texts to fit ~10 min)
- Uniform prosody across the whole article
- ~$0.48 per 30k chars at Neural2 rate (vs $3.67 Gemini Flash)
- 1M chars / month free Neural2 tier

Usage:
    GOOGLE_APPLICATION_CREDENTIALS=path/to/sa.json \\
    python3 scripts/ops/tts_cloud_long.py \\
      --input text.txt \\
      --output assets/audio/post.mp3 \\
      --voice fr-FR-Neural2-D
"""
from __future__ import annotations
import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# Cloud TTS hard limit per request: 5000 bytes
MAX_CHARS_PER_CHUNK = 4500
INTER_CHUNK_SILENCE_SEC = 0.4


def split_text(text: str, max_chars: int) -> list[str]:
    """Split text on paragraph boundaries first, then sentences if needed."""
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks: list[str] = []
    buf = ""
    for p in paragraphs:
        if len(p) > max_chars:
            # Paragraph itself too long: split by sentence
            for s in _sentence_split(p):
                if len(buf) + len(s) + 1 > max_chars:
                    if buf: chunks.append(buf.strip())
                    buf = s
                else:
                    buf = (buf + " " + s) if buf else s
            continue
        if len(buf) + len(p) + 2 > max_chars:
            chunks.append(buf.strip())
            buf = p
        else:
            buf = (buf + "\n\n" + p) if buf else p
    if buf:
        chunks.append(buf.strip())
    return chunks


def _sentence_split(text: str) -> list[str]:
    import re
    parts = re.split(r"(?<=[.!?])\s+", text)
    out = []
    for p in parts:
        if not p: continue
        # Ultra-long sentence (rare): hard split on commas
        while len(p) > MAX_CHARS_PER_CHUNK:
            cut = p.rfind(",", 0, MAX_CHARS_PER_CHUNK)
            if cut < MAX_CHARS_PER_CHUNK // 2: cut = MAX_CHARS_PER_CHUNK
            out.append(p[:cut].strip())
            p = p[cut:].strip()
        out.append(p)
    return out


def synth_chunk(client, text: str, voice_name: str, language_code: str, sample_rate_hz: int = 24000) -> bytes:
    from google.cloud import texttospeech as tts
    input_ = tts.SynthesisInput(text=text)
    voice = tts.VoiceSelectionParams(language_code=language_code, name=voice_name)
    audio_cfg = tts.AudioConfig(
        audio_encoding=tts.AudioEncoding.MP3,
        sample_rate_hertz=sample_rate_hz,
        speaking_rate=1.0,
        pitch=0.0,
    )
    resp = client.synthesize_speech(input=input_, voice=voice, audio_config=audio_cfg)
    return resp.audio_content


def concat_mp3s(chunk_paths: list[Path], output: Path, silence_sec: float, sample_rate: int):
    """Concat MP3 chunks via ffmpeg with inter-chunk silence."""
    if not shutil.which("ffmpeg"):
        raise SystemExit("ffmpeg required")
    silence_path = output.parent / ".silence.mp3"
    subprocess.run(
        ["ffmpeg", "-y", "-f", "lavfi", "-i", f"anullsrc=r={sample_rate}:cl=mono",
         "-t", str(silence_sec), "-b:a", "96k", str(silence_path)],
        check=True, capture_output=True,
    )
    list_file = output.parent / ".concat_list.txt"
    with list_file.open("w") as f:
        for i, c in enumerate(chunk_paths):
            f.write(f"file '{c.resolve()}'\n")
            if i < len(chunk_paths) - 1:
                f.write(f"file '{silence_path.resolve()}'\n")
    subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(list_file),
         "-c:a", "libmp3lame", "-b:a", "96k", "-ac", "1", "-ar", str(sample_rate),
         str(output)],
        check=True, capture_output=True,
    )
    list_file.unlink()
    silence_path.unlink()


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True, help="Path to plain text file")
    p.add_argument("--output", required=True, help="Output MP3 path")
    p.add_argument("--voice", default="fr-FR-Neural2-D",
                   help="Voice name (default: fr-FR-Neural2-D, male informative)")
    p.add_argument("--language", default="fr-FR")
    p.add_argument("--sample-rate", type=int, default=24000)
    p.add_argument("--silence-sec", type=float, default=INTER_CHUNK_SILENCE_SEC)
    args = p.parse_args()

    if not os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"):
        raise SystemExit("GOOGLE_APPLICATION_CREDENTIALS env var required")

    text = Path(args.input).read_text(encoding="utf-8").strip()
    chunks = split_text(text, MAX_CHARS_PER_CHUNK)
    print(f"Text length: {len(text)} chars / {len(text.split())} words")
    print(f"Chunks: {len(chunks)} (max {MAX_CHARS_PER_CHUNK} chars each)")
    for i, c in enumerate(chunks):
        print(f"  chunk {i+1}: {len(c)} chars / {len(c.split())} words")

    from google.cloud import texttospeech as tts
    client = tts.TextToSpeechClient()
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp:
        chunk_paths = []
        for i, chunk in enumerate(chunks, start=1):
            print(f"  [chunk {i}/{len(chunks)}] synthesizing {len(chunk)} chars... ", end="", flush=True)
            audio = synth_chunk(client, chunk, args.voice, args.language, args.sample_rate)
            cp = Path(tmp) / f"chunk_{i:03d}.mp3"
            cp.write_bytes(audio)
            chunk_paths.append(cp)
            print(f"{len(audio)//1024} KB")
        print(f"Concatenating {len(chunk_paths)} chunks with {args.silence_sec}s silence between...")
        concat_mp3s(chunk_paths, out_path, args.silence_sec, args.sample_rate)

    size_mb = out_path.stat().st_size / (1024 * 1024)
    # Get duration via ffprobe
    dur_proc = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(out_path)],
        capture_output=True, text=True,
    )
    dur_sec = float(dur_proc.stdout.strip()) if dur_proc.returncode == 0 else 0
    dur_h = f"{int(dur_sec // 60)}:{int(dur_sec % 60):02d}"
    wpm = (len(text.split()) / (dur_sec / 60)) if dur_sec > 0 else 0

    # Cost: Neural2 = $16/1M chars (https://cloud.google.com/text-to-speech/pricing)
    # Free tier: 1M chars/month Neural2
    cost = (len(text) / 1_000_000) * 16
    print()
    print(f"OK -> {out_path}")
    print(f"  size: {size_mb:.2f} MB | duration: {dur_h} | wpm: {wpm:.0f}")
    print(f"  cost (paid tier): ${cost:.4f} | free tier: 1M chars/month Neural2")


if __name__ == "__main__":
    main()
