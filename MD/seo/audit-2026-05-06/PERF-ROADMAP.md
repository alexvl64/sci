# Performance Sprint Roadmap — Mobile LCP (P1-A)

**Source :** `FULL-AUDIT-REPORT.md` Section 5 + `raw/seo-google.md`
**Cible globale :** Mobile Lighthouse perf ≥ 80 sur `/`, `/fr/`, `/blog/<slug>` · Mobile LCP ≤ 2,500 ms
**État baseline 2026-05-06 :**

| Page | Score | LCP | TBT | Diagnostic dominant |
|---|---|---|---|---|
| `/` | 68 / 100 | **5.6 s** 🔴 | 247 ms | Render-blocking fonts + Tailwind + gtag |
| `/fr/` | **62** / 100 | **9.8 s** 🔴 | 208 ms | + missing srcset/sizes hero (audit images) |
| `/blog/` | 86 / 100 | 3.2 s 🟡 | 97 ms | Fonts + Tailwind |
| `/blog/<slug>` | 73 / 100 | 4.5 s 🔴 | 169 ms | + lazy-loaded hero (delays LCP) + 3 oversized JPGs |
| `/privacy-policy` | 91 / 100 | 2.7 s 🟡 | 105 ms | OK |

Desktop est **86–100 partout** — c'est un problème mobile uniquement.
CrUX field data **indisponible** (trafic Chrome insuffisant) — donc seul le lab compte aujourd'hui pour Google.

---

## Hypothèse de fond : 4 leviers, ROI décroissant

| # | Levier | Gain LCP estimé (mobile) | Effort | Risque | Ordre |
|---|---|---|---|---|---|
| **1** | Self-host les 4 fonts (Gotham × 2 + ProximaNova × 2) — éliminer round-trip `fonts.googleapis.com` + `fonts.gstatic.com` | **−700 à −900 ms** | 1 h | Faible (woff2 déjà supporté par tous les navigateurs cibles) | 1er |
| **2** | Image fixes : srcset/sizes sur FR hero (parité EN) + WebP-twin sur 3 JPGs (mica/iran/panic) + `fetchpriority="high"` sur les 11 hero blog (au lieu de `loading="lazy"`) + alts descriptifs | **−1,500 à −2,500 ms sur FR home** + 200-400 ms blog articles | 1-2 h | Très faible (assets WebP existent déjà sur disque) | 2e |
| **3** | Defer gtag.js jusqu'au premier intent ou idle 3s — pattern `gtm-lazy.js` éprouvé sur dsungkur (CAPI-side captures conversions, donc pas de perte de tracking) | **−250 à −400 ms TBT** + libère le main thread | 2 h | Faible si on garde le `dataLayer` shim (pattern dsungkur prouvé) | 3e |
| **4** | Critical CSS inline + Tailwind defer (lightningcss-cli, pattern dsungkur) | **−300 à −450 ms** | 3-4 h | Modéré (FOUC possible si mal extrait — à valider sur beta) | 4e |

**Pourquoi cet ordre :** chaque levier est **indépendant**, mesurable isolément (PSI re-run après chaque PR). Levier 2 a le plus gros gain absolu (FR home gap mobile = principalement images). Levier 1 est universel (toutes les pages bénéficient). Levier 3 améliore TBT/INP plus que LCP. Levier 4 est le plus risqué donc en dernier.

---

## Décisions techniques à figer avant de coder

### Décision 1 — Variant fonts à self-héberger

Les 4 weights utilisés au-dessus du fold (vérifié sur dsungkur, à confirmer sur sci) :
- `Gotham_Book` (400)
- `Gotham_Medium` (500)
- `ProximaNova_Regular` (400)
- `ProximaNova_Bold` (700)

**À valider :** est-ce que sci utilise les mêmes families que dsungkur, ou des variants Google Fonts différents (Inter, Funnel-Display selon `MD/CLAUDE.md` blog conventions) ? Si Inter + Funnel-Display sont vraiment utilisés, il faut self-héberger ces deux-là (woff2 disponibles publiquement).

> **Action user :** confirme la liste des fonts critiques (ou je grep `font-family` dans `style.css` pour trancher).

### Décision 2 — Provenance des fichiers .woff2

Trois options pour récupérer les .woff2 self-host-ready :

- **(a) google-webfonts-helper.herokuapp.com** — outil web, copy-paste, 5 min
- **(b) `fontsource` npm package** — versionné, automatisable, ajoute une dep build-time
- **(c) télécharger directement depuis `fonts.gstatic.com` URL captée dans devtools** — manuel mais déterministe

Recommandation **(a)** : un seul shot, fonts mis en `/assets/fonts/`, pas de dep ajoutée.

### Décision 3 — `font-display`

Standard pour LCP : `font-display: swap` (texte affiché immédiatement avec fallback, swap quand la font custom charge).

### Décision 4 — Préload

Préloader **uniquement les 2 fonts above-the-fold** (typiquement Regular 400 + le H1 weight). Préloader les 4 → critical path overhead. À mesurer.

### Décision 5 — Defer gtag — quel trigger

Pattern dsungkur (`gtm-lazy.js`) déclenche sur :
- `pointerdown` / `touchstart` / `scroll` / `keydown` / `focusin` (premier intent)
- ou `requestIdleCallback` après 3s

`dataLayer` array initialisé en synchrone → tous les `gtag('event', ...)` queue avant le défer et rejouent après. Aucune perte d'event.

> **À valider :** le `MD/CLAUDE.md` sci insiste sur "tracking minimaliste, pas de GTM". Le pattern lazy-load conserve cette philosophie (pas de container GTM ajouté, juste gtag.js déféré). Compatible.

### Décision 6 — Critical CSS — méthode

**Pattern dsungkur** (déjà prouvé) :
```bash
npm install --save-dev lightningcss-cli
npx lightningcss --minify --bundle assets/css/style.css -o assets/css/style.min.css
```
Plus extraction critical via outil tiers (e.g. `critical` npm) ou manuel (sélecteurs above-the-fold listés à la main — plus stable).

### Décision 7 — Tester sur `beta` avant `main`

Workflow par `MD/CLAUDE.md` :
- branche `claude/perf-sprint-fonts` → PR vers `beta`
- preview auto sur `beta.sparkcore.fund`
- PSI sur `beta.sparkcore.fund` pour mesurer le gain réel
- merge `main` seulement après validation visuelle + perf confirmée

---

## Plan d'exécution

### Phase 1 — Fonts self-host (1 PR)

**Branche :** `claude/perf-fonts-selfhost`
**Fichiers touchés :**
- `assets/fonts/*.woff2` (nouveaux fichiers — 4 fonts × ~30 KB = ~120 KB ajoutés)
- `assets/css/fonts.css` (nouveau, `@font-face` declarations)
- `index.html`, `fr/index.html`, `blog/*.html`, `fr/blog/*.html` : retirer `<link href="https://fonts.googleapis.com/...">`, ajouter `<link rel="preload" as="font" type="font/woff2" crossorigin>` pour les 2 fonts critiques
- CSP Transform Rule : retirer `https://fonts.googleapis.com` du `style-src` et `https://fonts.gstatic.com` du `font-src` (cleanup, pas obligatoire pour la perf)

**Test sur beta :**
1. PSI mobile sur `https://beta.sparkcore.fund/` → score attendu **68 → 75-78**
2. Visual diff vs prod : aucun changement de typo (woff2 self-host = même rendu que Google CDN)
3. `curl -I https://beta.sparkcore.fund/assets/fonts/<file>.woff2` → cache-control 1 year (déjà set par `_headers`)

**Rollback :** revert PR — fonts self-host n'a aucun side-effect côté DOM/JS.

### Phase 2 — Image fixes (1 PR)

**Branche :** `claude/perf-images`
**Fichiers touchés :**
- `fr/index.html` : 4 alts vides → descriptifs (Steps to invest icons L998/1016/1034/1052) **+** ajouter srcset/sizes au hero (parité EN)
- `blog/*.html` (11 fichiers) : remplacer `loading="lazy"` par `fetchpriority="high"` sur le hero figure
- `blog/do-crypto-fund-managers-need-mica-casp-license.html` (et autres avec mica-casp-hero), `blog/<celle qui utilise iran-macro-shock>`, `blog/<celle qui utilise panic-seller-vs-hedger>` : remplacer `<img src=...jpg/jpeg>` par le `.webp` twin existant
- (optionnel cleanup) supprimer `assets/images/webp/nous-contacter.webp` (dead asset 71 KB)

**Liste exacte des 3 JPGs et leurs WebP twins** : à `find`-er sur disque avant la PR.

**Test sur beta :**
1. PSI mobile FR home → **62 → 75-80** (le srcset seul devrait fermer 60% du gap EN-FR)
2. PSI mobile blog article → **73 → 80-85**
3. Visual diff : aucun changement perçu (WebP twins ont la même résolution que les JPGs originaux)

### Phase 3 — Defer gtag.js (1 PR)

**Branche :** `claude/perf-gtag-lazy`
**Fichiers touchés :**
- `assets/js/analytics.js` : refactor en pattern lazy (basé sur `gtm-lazy.js` dsungkur)
- ou nouveau fichier `assets/js/gtag-lazy.js` + retirer `<script defer src="/assets/js/analytics.js">` des HTML, remplacer par `gtag-lazy.js`

**Test sur beta :**
1. PSI mobile : −250 à −400 ms TBT
2. **Critique** : ouvrir DevTools Network → onglet Console → vérifier qu'après 3s d'idle (ou un click), `https://www.googletagmanager.com/gtag/js?id=G-J80NVPQNVZ` se charge bien
3. GA4 Realtime → confirmer qu'un page_view fire après le defer
4. Test conversion : ouvrir le sidebar form, soumettre un test → `contact_form_submit` doit fire dans GA4 Debug View

**Risque principal :** perdre des sessions courtes (< 3s + pas d'intent) — mais ces sessions sont aussi celles qui bouncent sans valeur business. Acceptable trade-off.

### Phase 4 — Critical CSS (1 PR — **optionnelle, à décider après Phase 1-3**)

Si après Phase 1-3 le score mobile est ≥ 80 partout, **on n'ouvre pas Phase 4** — gain marginal pour effort élevé + risque FOUC. Si on est encore à 75-78, on enchaîne.

**Branche :** `claude/perf-critical-css`
**Fichiers touchés :**
- `package.json` : devDep `lightningcss-cli`
- nouveau script `npm run build:css`
- Critical CSS extrait (manuel, ~3-5 KB) inline dans `<head>` de `index.html`, `fr/index.html`
- `tailwind.min.css` chargé async (ou loaded via `<link rel="preload" ... onload="this.rel='stylesheet'">` pattern)

---

## Checkpoints & success criteria

### Après Phase 1 (fonts)
- PSI mobile `/` ≥ 75
- PSI mobile `/fr/` ≥ 70
- Visual : 0 régression

### Après Phase 2 (images)
- PSI mobile `/fr/` ≥ 78 (gros saut attendu)
- PSI mobile `/blog/<slug>` ≥ 80
- LCP mobile FR home ≤ 5 s

### Après Phase 3 (gtag)
- PSI mobile `/` ≥ 80
- PSI mobile `/fr/` ≥ 80
- TBT < 100 ms partout
- GA4 events fire correctement (vérifié manuellement)

### Final cible (toutes phases sauf 4 si pas nécessaire)
- Mobile perf ≥ 80 sur les 4 page-types
- Mobile LCP ≤ 2,500 ms sur le top of funnel (`/`, `/fr/`, blog index)
- 30 jours plus tard : CrUX commence à populer (à vérifier via `crux_history.py`)

---

## Hors-scope explicite (ne pas confondre avec backlog)

- **CDN migration** (Cloudflare Pro Image Resizing $60/yr) — décision deferred per `MD/CLAUDE.md`
- **Migration vers Workers** — pas avant qu'il y ait un cas d'usage concret (auth, paiement)
- **Lighthouse CI** — overkill pour un site statique de cette taille, on mesure ad-hoc via PSI

---

## Question pour validation user

1. **OK pour démarrer Phase 1 (fonts self-host) en ouvrant une PR sur `beta` ?**
2. Est-ce que les fonts utilisées sur sci sont **Gotham + ProximaNova** (comme dsungkur) ou bien **Inter + Funnel-Display** (mentionnés dans `MD/CLAUDE.md` blog convention `font-inter` `font-funnel-display`) ? Si tu n'es pas sûr, je grep `style.css` pour trancher avant de coder.
3. **Approche Phase 4 (Critical CSS)** : on l'évalue après Phase 1-3 ou on la planifie dès maintenant ?

Pas de code modifié à ce stade — j'attends ton go.
