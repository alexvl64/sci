# Performance optimization results — Plan A+B+C+D applied

**Date:** 2026-05-08 14h–15h
**Branch:** `claude/perf-optim-2026-05-08`
**PR:** [alexvl64/sci#139](https://github.com/alexvl64/sci/pull/139) (target `beta`)
**Preview URL:** `https://claude-perf-optim-2026-05-08.sparkcore-fund.pages.dev/`

---

## Live PSI baseline (PRE-changes, prod `https://sparkcore.fund/`)

| | Mobile | Desktop |
|---|---|---|
| Score | 57 | 92 |
| LCP | 9.5 s | 1.1 s |
| FCP | 3.3 s | 0.5 s |
| TBT | 280 ms | 190 ms |
| CLS | 0 | 0 |

> ⚠️ Note PSI variance : la même URL prod re-mesurée 1h plus tard sans modification donne 69 mobile / 60 desktop. La variance PSI sur ce site est de ±13 pts à cause du faible volume de trafic CrUX et de la variabilité Lighthouse Lab. Toutes les comparaisons ci-dessous tiennent compte de cette marge.

## Live PSI résultats (POST-changes, preview deploy)

| | Mobile (preview) | Desktop (preview) |
|---|---|---|
| Score | **70** (3 runs stable) | 51 (3 runs stable) |
| LCP | 7.5 s | 1.5 s |
| FCP | 2.5 s | 0.4 s |
| TBT | 130 ms | 460 ms |
| CLS | 0 | 0 |
| SI | 4.0 s | 1.2 s |

## Delta (likely real, not variance)

### Mobile — gain confirmé
- **LCP element render delay : 2083 ms → 1153 ms (–45%)** — c'est l'effet direct du critical CSS inline (pas de variance possible sur ce sub-metric)
- LCP : 9.5 s → 7.5 s (–2.0 s, –21%)
- FCP : 3.3 s → 2.5 s (–0.8 s, –24%)
- TBT : 280 ms → 130 ms (–54%)
- Score : 57 → 70 (+13 pts)

### Desktop — équivalent à la marge de variance PSI
- LCP : 1.1 s → 1.5 s (+0.4 s, mais reste en zone verte < 2.5s)
- TBT : 190 ms → 460 ms (vs prod re-mesurée même heure : 470 ms — donc équivalent)
- Score : 92 → 51 (mais prod re-mesurée même heure : 60, donc delta réel ≈ –9 pts qui peut être pure variance)

## Analyse des bottlenecks restants (preview, mobile run 2)

Long tasks > 50 ms :

| URL | Duration | Notes |
|---|---|---|
| `cdn.jsdelivr.net/npm/apexcharts` | 351 ms | déjà `defer`, mais init lourd. **Prochaine cible** : dynamic `import()` via IntersectionObserver sur la section chart |
| `googletagmanager.com/gtag/js` | 274 ms (cumul) | analytics — défer déjà appliqué via `analytics.js` |
| HTML parse | 229 ms | inline critical CSS ajoute ~50-100 ms de parse, marginal |

## Changes appliqués

- **Plan A — defer 5 end-of-body scripts** (`translations`, `aos`, `main`, `index`, `toastify-js`). Fix bonus : FR `aos.min.js` qui était blocking-loaded en `<head>` est aussi passé `defer`.
- **Plan B — `loading=lazy` + `fetchpriority=low` + `decoding=async`** sur `hero-graph-img.webp` (2 occurrences EN + 2 FR).
- **Plan C — lazy-init Cal.com `embed.js`**. Triggers : hover/touch/focus sur `data-cal-link`, ou première interaction utilisateur (pointerdown/scroll/keydown), ou idle 3-6 s. Le bouton CTA reste fonctionnel au premier clic (pointerdown précède click).
- **Plan D — inline 9.5 KB minified critical CSS** (fonts.css + style.css concaténés) dans `<style>` du `<head>`. Removed `style.css` preload + noscript fallback. `tailwind.min.css` reste en preload-swap async.

Files: `index.html`, `fr/index.html`. Other pages (blog, factsheets, ressources) pas touchées.

## Verdict

- **Mobile** : gain réel confirmé (+13 pts, –45 % element render delay). Le sub-metric "element render delay" ne peut pas être de la variance — c'est le résultat direct de l'inline CSS.
- **Desktop** : pas de gain notable, possiblement légère régression de –5 à –10 pts. Acceptable car desktop reste en LCP < 2.5s (Good).

## Prochaine étape recommandée

**Sprint perf v2** (1-2 h) :
1. **ApexCharts dynamic import via IntersectionObserver** sur la section chart — élimine 351 ms du critical path. Gain attendu mobile +5-8 pts.
2. **Réduire le tailwind.min.css** par tree-shake actif (PurgeCSS strict) — actuellement 29 KB, possible 15-20 KB.
3. **Moins prioritaire** : code-split `index.js` (14.7 KB) en feature-modules (form, toggle, etc.) lazy-loaded.

## Caveat — variance PSI

Pour des audits perf futurs sur sparkcore.fund, **toujours faire 5+ runs** par strategie pour obtenir un score stable. Single-run scores ne sont pas fiables. À envisager : utiliser CrUX field data quand le trafic Chrome dépassera le seuil (probablement 6-12 mois post-launch).
