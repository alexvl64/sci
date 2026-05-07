/* SparkCore article audio player
 * - Main player en haut de l'article
 * - Mini-player sticky bottom, apparait quand le main sort du viewport (IntersectionObserver)
 * - Les 2 UI partagent le meme element <audio> (sync play/pause/seek/speed)
 *
 * Usage HTML :
 *   <aside class="article-audio-player" data-src="/path.mp3" data-label="Ecouter l'article"></aside>
 *   (le mini-player est cree automatiquement et injecte avant </body>)
 */
(function () {
  "use strict";

  const SVG_PLAY =
    '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 2.5v11l11-5.5z"/></svg>';
  const SVG_PAUSE =
    '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 2h3.5v12H3zm6.5 0H13v12H9.5z"/></svg>';
  const SVG_CLOSE =
    '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M12.7 4.7l-1.4-1.4L8 6.6 4.7 3.3 3.3 4.7 6.6 8l-3.3 3.3 1.4 1.4L8 9.4l3.3 3.3 1.4-1.4L9.4 8z"/></svg>';
  const SPEEDS = [1, 1.25, 1.5, 1.75, 2];

  function fmt(seconds) {
    if (!isFinite(seconds) || seconds < 0) return "--:--";
    const m = Math.floor(seconds / 60);
    const s = Math.floor(seconds % 60);
    return m + ":" + (s < 10 ? "0" + s : s);
  }

  function buildMainUI() {
    return (
      '<button type="button" class="aap-play" aria-label="Lire">' + SVG_PLAY + "</button>" +
      '<div class="aap-meta">' +
      '<span class="aap-label"></span>' +
      '<span class="aap-times" aria-hidden="true"><span class="aap-current">0:00</span><span class="aap-sep">/</span><span class="aap-total">--:--</span></span>' +
      "</div>" +
      '<button type="button" class="aap-speed" aria-label="Vitesse de lecture">1x</button>' +
      '<div class="aap-progress" role="progressbar" aria-label="Progression" tabindex="0"><div class="aap-progress-fill"></div></div>'
    );
  }

  function buildMiniUI() {
    return (
      '<div class="article-audio-player-mini-inner">' +
      '<div class="aap-progress" role="progressbar" aria-label="Progression"><div class="aap-progress-fill"></div></div>' +
      '<button type="button" class="aap-play" aria-label="Lire">' + SVG_PLAY + "</button>" +
      '<div class="aap-meta">' +
      '<span class="aap-label"></span>' +
      '<span class="aap-times" aria-hidden="true"><span class="aap-current">0:00</span><span class="aap-sep">/</span><span class="aap-total">--:--</span></span>' +
      "</div>" +
      '<button type="button" class="aap-speed" aria-label="Vitesse de lecture">1x</button>' +
      '<button type="button" class="aap-mini-close" aria-label="Fermer le lecteur sticky">' + SVG_CLOSE + "</button>" +
      "</div>"
    );
  }

  function init(mainEl) {
    const src = mainEl.dataset.src;
    if (!src) return;
    const labelText = mainEl.dataset.label || "Écouter l'article";

    /* --- Render main UI --- */
    mainEl.innerHTML = buildMainUI();

    /* --- Create mini UI (injected at end of <body>) --- */
    const miniEl = document.createElement("aside");
    miniEl.className = "article-audio-player-mini";
    miniEl.setAttribute("aria-label", "Lecteur audio compact");
    miniEl.innerHTML = buildMiniUI();
    document.body.appendChild(miniEl);

    /* --- Single shared <audio> element --- */
    const audio = new Audio();
    audio.preload = "metadata";
    audio.src = src;

    /* --- Cache view bindings (queries scoped to each view) --- */
    const views = [
      bindView(mainEl, audio, labelText),
      bindView(miniEl, audio, labelText),
    ];

    let speedIdx = 0;

    function setSpeed(newIdx) {
      speedIdx = newIdx;
      audio.playbackRate = SPEEDS[speedIdx];
      views.forEach(function (v) { v.speedBtn.textContent = SPEEDS[speedIdx] + "x"; });
    }

    audio.addEventListener("loadedmetadata", function () {
      views.forEach(function (v) {
        v.el.classList.remove("is-loading");
        v.totalEl.textContent = fmt(audio.duration);
        v.progressEl.setAttribute("aria-valuemin", "0");
        v.progressEl.setAttribute("aria-valuemax", String(Math.round(audio.duration)));
      });
    });

    audio.addEventListener("error", function () {
      views.forEach(function (v) {
        v.el.classList.remove("is-loading");
        v.el.classList.add("is-error");
        v.labelEl.textContent = "Audio indisponible";
        v.totalEl.textContent = "";
      });
    });

    audio.addEventListener("timeupdate", function () {
      const pct = isFinite(audio.duration) ? (audio.currentTime / audio.duration) * 100 : 0;
      views.forEach(function (v) {
        v.currentEl.textContent = fmt(audio.currentTime);
        v.progressFill.style.width = pct + "%";
        v.progressEl.setAttribute("aria-valuenow", String(Math.round(audio.currentTime)));
      });
    });

    audio.addEventListener("play", function () {
      views.forEach(function (v) {
        v.playBtn.innerHTML = SVG_PAUSE;
        v.playBtn.setAttribute("aria-label", "Pause");
      });
    });
    audio.addEventListener("pause", function () {
      views.forEach(function (v) {
        v.playBtn.innerHTML = SVG_PLAY;
        v.playBtn.setAttribute("aria-label", "Lire");
      });
    });
    audio.addEventListener("ended", function () {
      audio.currentTime = 0;
    });

    views.forEach(function (v) {
      v.el.classList.add("is-loading");
      v.labelEl.textContent = labelText;

      v.playBtn.addEventListener("click", function () {
        if (audio.paused) audio.play();
        else audio.pause();
      });

      v.speedBtn.addEventListener("click", function () {
        setSpeed((speedIdx + 1) % SPEEDS.length);
      });

      v.progressEl.addEventListener("click", function (e) {
        if (!isFinite(audio.duration)) return;
        const rect = v.progressEl.getBoundingClientRect();
        const x = (e.clientX || 0) - rect.left;
        const pct = Math.max(0, Math.min(1, x / rect.width));
        audio.currentTime = pct * audio.duration;
      });
      v.progressEl.addEventListener("keydown", function (e) {
        if (!isFinite(audio.duration)) return;
        const step = audio.duration / 20;
        if (e.key === "ArrowRight") { audio.currentTime = Math.min(audio.duration, audio.currentTime + step); e.preventDefault(); }
        else if (e.key === "ArrowLeft") { audio.currentTime = Math.max(0, audio.currentTime - step); e.preventDefault(); }
      });
    });

    /* --- Mini close button --- */
    const closeBtn = miniEl.querySelector(".aap-mini-close");
    if (closeBtn) {
      closeBtn.addEventListener("click", function () {
        miniEl.classList.remove("is-pinned");
        miniEl.classList.add("is-dismissed");
      });
    }

    /* --- IntersectionObserver: show mini when main is offscreen --- */
    if ("IntersectionObserver" in window) {
      const observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (miniEl.classList.contains("is-dismissed")) return;
          if (!entry.isIntersecting) {
            /* main est hors viewport ET audio en cours de lecture (ou deja consulte) */
            if (audio.currentTime > 0 || !audio.paused) {
              miniEl.classList.add("is-pinned");
            }
          } else {
            miniEl.classList.remove("is-pinned");
          }
        });
      }, { threshold: 0, rootMargin: "0px 0px -20px 0px" });
      observer.observe(mainEl);

      /* Si l'utilisateur lance le play en haut puis scroll, on veut le mini visible immediatement
         meme si le main n'a pas encore quitte le viewport. On declenche un re-evaluation quand audio.play */
      audio.addEventListener("play", function () {
        const rect = mainEl.getBoundingClientRect();
        if (rect.bottom < 0 || rect.top > window.innerHeight) {
          if (!miniEl.classList.contains("is-dismissed")) miniEl.classList.add("is-pinned");
        }
      });
    }
  }

  function bindView(el, audio, labelText) {
    return {
      el: el,
      playBtn: el.querySelector(".aap-play"),
      labelEl: el.querySelector(".aap-label"),
      currentEl: el.querySelector(".aap-current"),
      totalEl: el.querySelector(".aap-total"),
      speedBtn: el.querySelector(".aap-speed"),
      progressEl: el.querySelector(".aap-progress"),
      progressFill: el.querySelector(".aap-progress-fill"),
    };
  }

  function boot() {
    document.querySelectorAll(".article-audio-player").forEach(init);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
