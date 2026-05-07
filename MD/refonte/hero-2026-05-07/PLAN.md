# Hero Refonte — Roadmap

**Date :** 2026-05-07
**Branche de travail :** `beta` (deploy auto sur `beta.sparkcore.fund`)
**Source du brief :** B9 du `MD/seo/audit-2026-05-06/NEXT-BATCH.md` — option A (refonte complète)
**Mode :** propose-then-implement (per CLAUDE.md root rule SCI). Aucun code écrit avant validation user.

---

## 1. État actuel — analyse

### Composition (`index.html` lignes 498-592)

```
┌──────────────────────────────────────────────────────────────────┐
│ HERO — bg-darkGray (#0E1117) — h-[calc(100vh-88px)] @ 2xl        │
│                                                                  │
│ ┌──────────────────────┐  ┌─────────────────────────────────┐  │
│ │ LEFT 50% (text)      │  │ RIGHT 50% (image)               │  │
│ │                      │  │                                 │  │
│ │ H1 (50px white):     │  │ ┌─────────────────────────────┐ │  │
│ │ Institutional-grade  │  │ │                             │ │  │
│ │ strategies in        │  │ │     hero-image.webp         │ │  │
│ │ digital assets       │  │ │     (1440×1600 portrait)    │ │  │
│ │                      │  │ │                             │ │  │
│ │ Tagline (lightBlue)  │  │ │                             │ │  │
│ │ Three distinct       │  │ │                             │ │  │
│ │ approaches. One      │  │ │                             │ │  │
│ │ regulated framework. │  │ │                             │ │  │
│ │                      │  │ └─────────────────────────────┘ │  │
│ │ [Schedule Call →]    │  │   ↑ vector overlay top-right    │  │
│ │ [Request Doc]        │  │                                 │  │
│ │                      │  │                                 │  │
│ │ ↓ scroll arrow       │  │                                 │  │
│ └──────────────────────┘  └─────────────────────────────────┘  │
│                                                                  │
│  ↓ background graph image (full-width, alpha overlay 2xl)        │
└──────────────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────────────┐
│ TRUST STRIP — bg #F3F5F7, separate section below hero            │
│ Regulator │ Accounting │ Legal Counsel │ LEI                     │
│ Finantsinspektsioon (EE) │ KPMG Estonia │ Hedman Partners │ 894...│
└──────────────────────────────────────────────────────────────────┘
```

### Forces

- ✅ **Above-the-fold complet** : H1 + tagline + 2 CTAs sont visibles sans scroll (sur desktop)
- ✅ **Brand cohérente** : darkGray + cream + lightBlue forment une palette financière premium
- ✅ **CTAs clairs** : primary (Cal.com) + secondary (sidebar form) — funnel propre
- ✅ **Performance** : `fetchpriority="high"` + `loading="eager"` sur hero-image, preload dans `<head>`
- ✅ **Accessibilité** : alt text présent, ARIA labels OK

### Faiblesses (à fixer dans la refonte)

- ❌ **Trust strip below the fold** sur desktop standard — les visiteurs institutionnels ratent les 4 signaux clés (EFSA, KPMG, Hedman, LEI) avant de quitter
- ❌ **Image droite générique** : `hero-image.webp` ne véhicule pas le message "regulated AIFM Estonia". Aucun signal de différenciation visuelle
- ❌ **Pas de preuve/data** : le hero promet "institutional-grade" mais n'en montre rien (pas de NAV, pas de chart, pas de track record visible)
- ❌ **CTAs verticaux** : "Schedule a Discovery Call" + "Request Documentation" empilés mangent de la verticale, alors qu'horizontaux gagneraient en compacité
- ❌ **Background graph (`hero-graph-img.webp`)** est purement décoratif, ne dit rien
- ❌ **Mobile** : hero-image ~400px de hauteur passe avant les CTAs (scroll inversé non-naturel)

### KPIs à améliorer (mesurables post-refonte)

| KPI | Source | Baseline | Cible post-refonte |
|---|---|---|---|
| Bounce rate `/` | GA4 | TBD (à mesurer) | -10% |
| Scroll past hero (90%) | GA4 enhanced measurement | TBD | +15% |
| `cal_booking_complete` from origin=hero | GA4 custom event | ~0 (volume bas) | volume mesurable |
| `factsheet_request_open` from origin=hero | GA4 custom event | ~0 | +qualified leads |
| Time-to-first-engagement | GA4 | TBD | -20% |

---

## 2. Trois directions design — décision attendue

Chaque direction est **shippable indépendamment**. Estimations effort pour passer du roadmap à la prod (HTML + CSS + assets + QA).

---

### Direction A — "Institutional Authority" (recommandée par défaut)

**Philosophie :** densité d'information + autorité réglementaire visible. Inspiré de KPMG / BlackRock institutional pages. Trust comme premier signal, pas comme footer.

**Composition :**

```
┌──────────────────────────────────────────────────────────────────┐
│ TOP BAR — bg-cream (#DBD1BC), full-bleed, ~40px height           │
│ EFSA-supervised · KPMG-audited · Hedman counsel · LEI 894...     │
└──────────────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────────────┐
│ HERO — bg-darkGray (#0E1117) — h-[calc(100vh-128px)]             │
│                                                                  │
│  Centered single column, max-w-[960px]                           │
│                                                                  │
│            REGULATED CRYPTO ASSET MANAGER                        │
│            (eyebrow, 12px uppercase tracking-wider, cream)       │
│                                                                  │
│            Institutional-grade strategies                        │
│            in digital assets.                                    │
│            (H1 — font-funnel-display, 64-80px, white)            │
│                                                                  │
│            Three distinct approaches. One regulated              │
│            framework. Managed for investors who                  │
│            demand precision.                                     │
│            (subtitle — 18-20px, lightBlue, max-w-[640px])        │
│                                                                  │
│            [Schedule Discovery Call →]   [Request Documentation] │
│            (CTAs horizontaux, gap-4)                             │
│                                                                  │
│                          ↓                                       │
│                      (scroll arrow)                              │
└──────────────────────────────────────────────────────────────────┘
```

**Changements :**
- Trust strip **devient TOP BAR** au-dessus du hero (above the H1) en bg-cream — premier signal visible
- **Image droite supprimée** — full hero centré, plus institutionnel/sobre
- **CTAs horizontaux** (gap-4) au lieu de verticaux empilés
- Eyebrow ajouté au-dessus du H1 ("REGULATED CRYPTO ASSET MANAGER" en cream uppercase)
- H1 légèrement plus grand (64-80px vs 50px actuel) avec vrai retour à la ligne contrôlé
- Background graph `hero-graph-img.webp` supprimé (ne dit rien)
- Animation subtle : pas d'AOS (data-aos="fade-right" supprimé), juste fade-in CSS @ load

**Trade-offs :**
- ✅ Above-the-fold ultra clair, dense, autoritaire
- ✅ Aucune image hero à charger → meilleur LCP
- ✅ Compatible `prefers-reduced-motion`
- ⚠️ Plus austère, perd l'image de la femme professionnelle (qui peut humaniser)
- ⚠️ Demande typo précise (font-weight, line-height) pour ne pas sembler vide

**Effort estimé :** 3-4h (HTML + CSS + responsive QA + FR parity)

**Risque régression layout :** 🟢 LOW — moins d'éléments = moins de breakpoints à gérer.

---

### Direction B — "Editorial / Premium Publication"

**Philosophie :** feel "Financial Times / Economist long-read". Beige / cream BG inversé du dark actuel. Typographie éditoriale. Crédibilité par le ton.

**Composition :**

```
┌──────────────────────────────────────────────────────────────────┐
│ HERO — bg-cream (#DBD1BC) — min-h-[680px]                        │
│                                                                  │
│ ┌────────────────────────┐  ┌───────────────────────────────┐  │
│ │ LEFT 60% (editorial)   │  │ RIGHT 40% (fund cards stack)  │  │
│ │                        │  │                               │  │
│ │ Quatre · LEI 894...    │  │ ┌─────────────────────────┐   │  │
│ │ (eyebrow 10px upper)   │  │ │ DYNAMIC TRENDS          │   │  │
│ │                        │  │ │ Live since Aug 2025     │   │  │
│ │ Institutional-grade    │  │ │ ▲ +XX% YTD             │   │  │
│ │ strategies in          │  │ └─────────────────────────┘   │  │
│ │ digital assets.        │  │ ┌─────────────────────────┐   │  │
│ │ (H1 80-96px serif-ish, │  │ │ CRYPTOVISION            │   │  │
│ │  font-funnel-display,  │  │ │ Live since 2021         │   │  │
│ │  text-darkGray)        │  │ │ ▲ +XX% YTD             │   │  │
│ │                        │  │ └─────────────────────────┘   │  │
│ │ Three distinct         │  │ ┌─────────────────────────┐   │  │
│ │ approaches. One        │  │ │ EQUINOXE                │   │  │
│ │ regulated framework... │  │ │ Planned 2026            │   │  │
│ │ (italics serif accent) │  │ │ Market-neutral          │   │  │
│ │                        │  │ └─────────────────────────┘   │  │
│ │ [Schedule Call →]      │  │                               │  │
│ │ [Request Doc]          │  │                               │  │
│ └────────────────────────┘  └───────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────────────┐
│ TRUST STRIP — kept below, bg-white                               │
│ EFSA · KPMG · Hedman · LEI                                       │
└──────────────────────────────────────────────────────────────────┘
```

**Changements :**
- BG inversé : **bg-cream** au lieu de bg-darkGray — feel beaucoup plus "premium publication"
- Image droite remplacée par **3 fund cards** (Dynamic Trends, CryptoVision, Equinoxe) — montre l'offre directement
- Texte left agrandi 60% (split 60/40)
- H1 **80-96px** sur desktop avec line-height très resserré (110%) — feel éditorial
- Une phrase italique en accent (peut-être issu d'une citation client / KPMG quote)
- Trust strip reste below mais avec bg-white au lieu de bg-#F3F5F7 (contraste avec cream du hero)

**Trade-offs :**
- ✅ Différenciation forte vs concurrents crypto fund (qui sont tous dark-bg)
- ✅ Montre l'OFFRE (3 funds) directement above the fold
- ✅ Crédibilité éditoriale → cible HNW investors qui valorisent le ton
- ⚠️ Demande **données NAV à afficher** sur les fund cards (B12 deferred — soit on met "+XX%" placeholder, soit on attend les NAV KPMG, soit on omet les % et on ne montre que statut/style)
- ⚠️ Cassure visuelle complète vs reste du site (qui reste dark) — peut sentir incohérent
- ⚠️ Compatible avec la nouvelle pillar card cream → renforce la cohérence cream comme color signature

**Effort estimé :** 5-7h (HTML + CSS + 3 fund card components + responsive)

**Risque régression :** 🟡 MEDIUM — refonte fond clair = test contraste + accessibilité (WCAG AA) sur darkGray sur cream. Demande validation sur Lighthouse.

**Bloquant :** décision sur les data fund cards — afficher quoi (NAV ? statut ? Strategy short label ?). Si pas de NAV publique, je propose un design "statut + style" sans chiffres.

---

### Direction C — "Data-led / Quant Aesthetic"

**Philosophie :** institutional credibility par les **données visibles**. Inspiré de Bloomberg terminal / Two Sigma / DE Shaw. Chart en hero = preuve, pas image.

**Composition :**

```
┌──────────────────────────────────────────────────────────────────┐
│ TOP BAR — bg-#1a1d24 (slightly lighter than darkGray)            │
│ EFSA-supervised · KPMG-audited · Hedman · LEI 894...             │
└──────────────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────────────┐
│ HERO — bg-darkGray (#0E1117) — h-[calc(100vh-128px)]             │
│                                                                  │
│ ┌────────────────────────┐  ┌───────────────────────────────┐  │
│ │ LEFT 45% (text)        │  │ RIGHT 55% (chart, full-bleed) │  │
│ │                        │  │                               │  │
│ │ Eyebrow cream 11px:    │  │ DYNAMIC TRENDS · NAV Series   │  │
│ │ AIFM · ESTONIA · LEI   │  │ AS OF 2026-04-30              │  │
│ │                        │  │ (corner labels, 10px gray)    │  │
│ │ Institutional-grade    │  │                               │  │
│ │ strategies in          │  │     ╱╲    ╱╲                  │  │
│ │ digital assets.        │  │    ╱  ╲  ╱  ╲     ╱╲          │  │
│ │ (H1 56-64px white)     │  │   ╱    ╲╱    ╲   ╱  ╲         │  │
│ │                        │  │  ╱            ╲ ╱    ╲        │  │
│ │ Three distinct         │  │ ╱              v      ╲       │  │
│ │ approaches...          │  │                                │  │
│ │ (subtitle 18px)        │  │  Apr  Jun  Aug  Oct  Dec  Feb │  │
│ │                        │  │                               │  │
│ │ [Schedule Call →]      │  │ +XX% YTD · max DD -X%         │  │
│ │ [Request Doc]          │  │ (small footer caption)        │  │
│ └────────────────────────┘  └───────────────────────────────┘  │
│                                                                  │
│                          ↓                                       │
└──────────────────────────────────────────────────────────────────┘
```

**Changements :**
- Trust strip → **TOP BAR au-dessus du hero**, en bg-#1a1d24 (slightly lighter dark)
- **Image droite remplacée par un chart inline ApexCharts** showing real Dynamic Trends NAV series
- Chart : line chart minimaliste, palette darkGray + cream, axis labels 10-11px gray
- Eyebrow + corner labels comme Bloomberg ("AS OF 2026-04-30", "DYNAMIC TRENDS · NAV Series")
- Subtitle plus court, plus dense
- Footer caption sous le chart : "+XX% YTD · max DD -X%" (factual)
- Aucune image décorative — toute la verticale est utilisable

**Trade-offs :**
- ✅ Crédibilité immédiate (preuve par les chiffres)
- ✅ Différenciation maximale vs concurrents (la plupart utilisent images stock)
- ✅ Chart déjà supporté par le stack (ApexCharts via jsdelivr CDN)
- ⚠️ **Bloquant : NAV data publique requise** (B12 deferred). Sans NAV propre, on doit soit (a) attendre le go KPMG audit data, (b) afficher un chart "indicative" avec disclaimer, (c) afficher une projection / strategy thesis chart au lieu d'une track record
- ⚠️ Compliance MiFID II : montrer du performance data sur la home publique = potentiellement marketing material à archiver et soumettre à l'EFSA. À valider.
- ⚠️ Risque de feel trop "trading desk" alors que cible = institutional allocator (pas day-trader)

**Effort estimé :** 6-8h (HTML + CSS + ApexCharts integration + data source décision + responsive)

**Risque régression / compliance :** 🟠 MEDIUM-HIGH — la compliance Finantsinspektsioon doit valider tout affichage de performance data sur le site public.

**Bloquant fort :** décision data + compliance avant d'écrire la moindre ligne de code.

---

## 3. Décisions à prendre par toi

Avant que j'écrive du code, je dois savoir :

### Q1. Quelle direction (A / B / C / autre) ?

| Direction | Effort | Risque | Compliance |
|---|---|---|---|
| A — Institutional Authority | 3-4h | 🟢 LOW | aucun |
| B — Editorial Premium | 5-7h | 🟡 MEDIUM | aucun (sans NAV) |
| C — Data-led Quant | 6-8h | 🟠 MED-HIGH | EFSA review du chart |

Tu peux aussi mixer : ex. "**A** mais avec les fund cards de **B** à la place de l'arrow scroll", ou "**A** avec un mini-chart inline plus discret que C".

### Q2. Que faire de la trust strip ?

- **(a)** TOP BAR au-dessus du hero (bg-cream ou darker) — recommandé direction A et C
- **(b)** Eyebrow inline dans le hero (single-line ABOVE H1) — plus discret
- **(c)** Garder below the fold (status quo) — pas vraiment "above the fold"

### Q3. Image humaine (woman portrait actuelle)

- **Garder** dans une autre section du site (about / team) ?
- **Remplacer** par 3 fund cards (B) ou chart (C) ?
- **Supprimer entièrement** (A) ?

### Q4. Copy H1 — faut-il le modifier ?

Actuel : *"Institutional-grade strategies in digital assets"*

Possibles updates :
- *"Regulated crypto fund management. Estonia."* (plus direct, moins corporate)
- *"For investors who demand precision."* (plus client-facing)
- *"Three regulated AIFs. One Estonian AIFM."* (factuel, dense)
- garder l'actuel

### Q5. CTA primary/secondary copy

Actuels : "Schedule a Discovery Call →" + "Request Documentation"

Tu veux modifier ? Souvent ça gagne à être :
- Primary : "Book a Call" / "Schedule a Call" / "Talk to us"
- Secondary : "Get the factsheets" / "View our funds" / "Read the framework"

---

## 4. Workflow proposé après ta réponse

1. **Aujourd'hui** : tu choisis direction + réponds aux Q2/Q3/Q4/Q5
2. **Branche `claude/hero-refonte-implementation`** créée à partir de `beta` actualisée
3. **Je code** : EN homepage hero (`index.html` lignes ~498-614) + parité FR (`fr/index.html` lignes ~498-580 environ) + `style.css` rules adapt
4. **Push beta** → preview live sur **`beta.sparkcore.fund`**
5. **QA mobile + desktop + i18n** (toi sur le preview)
6. **Itérations design** sur la branche
7. **Une fois validé** : PR `beta → main` pour ship sur prod

## 5. Out of scope (à ne PAS faire dans cette refonte)

- ❌ Toucher au form sidebar, au footer, à la nav
- ❌ Migration Cloudflare config, CSP, _redirects
- ❌ Modifier les autres sections (Our Approach, Team, etc.)
- ❌ Refonte typographique sitewide (stay on Funnel Display + Inter, déjà self-hosted depuis #97)
- ❌ Ajouter un preconnect cal.eu statique (déjà décidé qu'il est lazy via `cal-lazy.js`)

---

## 6. Réponse attendue de toi

Format minimal :

```
Direction: A | B | C | mix(A+B fund cards) | autre
Q2 trust strip: a | b | c
Q3 image: garder ailleurs | remplacer | supprimer
Q4 H1: garder | nouveau texte: "..."
Q5 CTAs: garder | nouveau primary: "..." | nouveau secondary: "..."
```

Une fois ça reçu, je crée la branche d'implémentation et je code. Estimation préliminaire : **branche prête en 4-8h** selon direction, preview beta dès le premier push.
