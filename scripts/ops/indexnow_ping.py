#!/usr/bin/env python3
"""
Ping IndexNow (Bing, Yandex, Seznam, Yep, Naver) to notify about new or
updated URLs on sparkcore.fund. Stdlib only - no external dependencies.

IndexNow spec: https://www.indexnow.org/documentation

Usage:
    # Ping all URLs listed in sitemap.xml
    python3 scripts/ops/indexnow_ping.py --all

    # Ping specific URLs (e.g. after publishing an article)
    python3 scripts/ops/indexnow_ping.py https://sparkcore.fund/blog/new-slug \
                                         https://sparkcore.fund/fr/blog/new-slug

    # Dry-run: print the payload without sending
    python3 scripts/ops/indexnow_ping.py --all --dry-run

Log file: logs/indexnow.log (entries older than 30 days are auto-purged)
"""

import argparse
import json
import sys
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SITEMAP_PATH = ROOT / "sitemap.xml"
LOG_PATH = ROOT / "logs" / "indexnow.log"
LOG_RETENTION_DAYS = 30
ENTRY_SEP = "---\n"

HOST = "sparkcore.fund"
KEY = "27994a06b868d24820429dc36c1bafee"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"
ENDPOINT = "https://api.indexnow.org/indexnow"

SITEMAP_NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}


def read_sitemap_urls() -> list[str]:
    """Extract <loc> URLs from the sitemap."""
    if not SITEMAP_PATH.exists():
        sys.exit(f"Sitemap not found: {SITEMAP_PATH}")
    tree = ET.parse(SITEMAP_PATH)
    root = tree.getroot()
    urls = [loc.text.strip() for loc in root.findall("sm:url/sm:loc", SITEMAP_NS) if loc.text]
    return urls


def validate_urls(urls: list[str]) -> list[str]:
    """Only keep URLs on the declared host - IndexNow rejects cross-host batches."""
    valid = [u for u in urls if u.startswith(f"https://{HOST}/")]
    rejected = set(urls) - set(valid)
    for u in rejected:
        print(f"  [skip] {u} (not on https://{HOST}/)", file=sys.stderr)
    return valid


def _parse_entry_ts(entry: str) -> datetime | None:
    """Return the timestamp of a log entry, or None if unparseable."""
    first_line = entry.strip().splitlines()[0] if entry.strip() else ""
    try:
        ts_str = first_line.split(" | ")[0].strip()
        ts = datetime.fromisoformat(ts_str)
        if ts.tzinfo is None:
            ts = ts.replace(tzinfo=timezone.utc)
        return ts
    except (ValueError, IndexError):
        return None


def purge_old_logs() -> None:
    """Remove log entries older than LOG_RETENTION_DAYS days."""
    if not LOG_PATH.exists():
        return
    cutoff = datetime.now(timezone.utc) - timedelta(days=LOG_RETENTION_DAYS)
    raw = LOG_PATH.read_text(encoding="utf-8")
    entries = [e for e in raw.split(ENTRY_SEP) if e.strip()]
    kept, purged = [], 0
    for entry in entries:
        ts = _parse_entry_ts(entry)
        if ts is not None and ts < cutoff:
            purged += 1
        else:
            kept.append(entry)
    if purged:
        LOG_PATH.write_text(ENTRY_SEP.join(kept) + (ENTRY_SEP if kept else ""), encoding="utf-8")
        print(f"  [log] {purged} entr{'y' if purged == 1 else 'ies'} older than {LOG_RETENTION_DAYS} days purged.")


def write_log(urls: list[str], code: int, message: str) -> None:
    """Append a log entry then purge old entries."""
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines = [f"{now} | {code} | {message}", f"  urls ({len(urls)}):"]
    lines += [f"    - {u}" for u in urls]
    entry = "\n".join(lines) + "\n"
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(entry)
        f.write(ENTRY_SEP)
    purge_old_logs()
    print(f"  [log] {LOG_PATH}")


def ping(urls: list[str], dry_run: bool = False) -> int:
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }
    body = json.dumps(payload, indent=2)

    if dry_run:
        print("[dry-run] POST", ENDPOINT)
        print(body)
        return 0

    req = urllib.request.Request(
        ENDPOINT,
        data=body.encode("utf-8"),
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Host": "api.indexnow.org",
            "User-Agent": "sparkcore-indexnow/1.0 (+https://sparkcore.fund)",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            code = resp.status
            body_resp = resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        code = e.code
        body_resp = e.read().decode("utf-8", errors="replace")
    except urllib.error.URLError as e:
        msg = f"Network error: {e.reason}"
        print(msg, file=sys.stderr)
        write_log(urls, 0, msg)
        return 2

    interpret = {
        200: "OK - URLs received and validated",
        202: "Accepted - URLs received, key validation pending",
        400: "Bad Request - invalid payload",
        403: "Forbidden - key file not found or does not match",
        422: "Unprocessable Entity - invalid URLs or host mismatch",
        429: "Too Many Requests - rate limit exceeded",
    }
    tag = interpret.get(code, f"HTTP {code}")
    print(f"[{code}] {tag}")
    if body_resp.strip():
        print(body_resp)
    write_log(urls, code, tag)
    return 0 if code in (200, 202) else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Ping IndexNow for sparkcore.fund")
    parser.add_argument("urls", nargs="*", help="URLs to ping (optional)")
    parser.add_argument("--all", action="store_true",
                        help="Ping all URLs found in sitemap.xml")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print payload without sending")
    args = parser.parse_args()

    if args.all and args.urls:
        parser.error("--all and explicit URLs are mutually exclusive")
    if not args.all and not args.urls:
        parser.error("Provide URLs or use --all")

    urls = read_sitemap_urls() if args.all else args.urls
    urls = validate_urls(urls)
    if not urls:
        sys.exit("No valid URLs to submit.")

    print(f"Submitting {len(urls)} URL(s) to {ENDPOINT}:")
    for u in urls:
        print(f"  - {u}")
    return ping(urls, dry_run=args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
