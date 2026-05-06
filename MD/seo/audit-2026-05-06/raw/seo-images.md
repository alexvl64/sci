# Image SEO Audit — sparkcore.fund

**Audit date:** 2026-05-06
**Scope:** Static assets in `/home/alex/Documents/Claude/github-projets/sci/assets/images/` + 28 HTML pages (index EN/FR, blog ×23 EN, blog ×4 FR, blog/index EN+FR, privacy-policy, validation, discovery-call, 403/404/500)
**Method:** Direct file reads, Pillow dimension probe, Python regex `<img>` parser, live HTTP HEAD on Cloudflare Pages
**Hosting:** Cloudflare Pages (CF Image Resizing **not** enabled — confirmed `/cdn-cgi/image/...` returns HTTP 404)

---

## 1. Score

**Image SEO Score: 72 / 100 — B-**

| Category | Weight | Sub-score | Weighted |
|---|---:|---:|---:|
| Alt text completeness & quality | 25 | 75/100 | 18.75 |
| File sizes (perf budget) | 15 | 70/100 | 10.50 |
| Format optimization (WebP/AVIF) | 15 | 95/100 | 14.25 |
| Responsive images (`srcset`/`sizes`) | 15 | 35/100 | 5.25 |
| `width`/`height` (CLS prevention) | 10 | 95/100 | 9.50 |
| Lazy-loading + LCP `fetchpriority` | 10 | 80/100 | 8.00 |
| OG / social card metadata | 5 | 50/100 | 2.50 |
| Image sitemap + CDN delivery | 5 | 60/100 | 3.00 |
| **TOTAL** | **100** | — | **71.75 → 72** |

Net assessment: solid foundation (modern formats dominate, dimensions present everywhere, headers correctly cached for 1 year), but **alt text quality on the homepage is a recurring weakness** (`hero image`, `arrow`, `blur box`, `graph image`, `invest in us image`) and **the FR homepage lost its `srcset`/`sizes`** that the EN version has. The single biggest one-shot win is replacing `mica-casp-hero.jpeg` (442 KB) with a WebP — that one file alone is 15 % of the entire image library.

---

## 2. Asset inventory

### 2.1 Counts by format

| Format | Files | Total bytes | Average |
|---|---:|---:|---:|
| WebP | 23 | 1,239 KB | 53.9 KB |
| JPG/JPEG | 9 | 1,496 KB | 166.2 KB |
| PNG | 6 | 36 KB | 6.0 KB (favicons) |
| SVG | 18 | 28 KB | 1.6 KB |
| AVIF | 0 | 0 | n/a |
| GIF | 0 | 0 | n/a |
| **TOTAL** | **56** | **2.80 MB** | — |

WebP is the dominant format (41 % of files, 43 % of bytes). The 9 remaining JPGs are blog hero images (8 of which already have a paired WebP — only `mica-casp-hero.jpeg` is JPG-only and is the largest file in the entire repo). PNG is reserved for favicons (legitimate use). SVG is used for logos, flags, icons, and step illustrations (legitimate use).

### 2.2 Library breakdown by directory

```
assets/images/
├── blog/        16 files  1,654 KB   — 8 JPG + 8 WebP pairs (blog hero/inline)
├── jpeg/         1 file     442 KB   — mica-casp-hero.jpeg (only JPG without WebP pair)
├── png/          6 files     36 KB   — favicons (16, 32, 48, 64, 192, 512)
├── svg/         18 files     28 KB   — logos, flags, icons, step diagrams
└── webp/        15 files     739 KB   — homepage hero, team, decorative, vectors
```

### 2.3 Asset → page mapping

- **Hero (homepage):** `hero-image.webp` (1440×1600, 104 KB) + responsive 480/768 variants — used on `/` and `/fr/`
- **Hero graph:** `hero-graph-img.webp` (1440×852, 110 KB) + 768 variant — homepage
- **Team photos (3):** `team-member-{first,second,third}.webp` (832×800 each) — homepage `#team`
- **Blog hero (8 paired JPG/WebP):** cvd-funding, etf-flows, hero-agents-ia, hero-indicateurs, hero-market-timing, iran-macro-shock, options-volatility, panic-seller-vs-hedger
- **Blog hero (1 JPG only):** `mica-casp-hero.jpeg` — used on `/blog/do-crypto-fund-managers-need-mica-casp-license.html` AND as that page's `og:image`
- **OG image:** `meta-image.webp` (1013×628, 75 KB) at root — used by all 28 pages except the MiCA blog post
- **Decorative:** `blur-box.webp`, `hero-sec-vector.webp`, `contact-us-img.webp`, `nous-contacter.webp`, `invest-in-us.webp`, `crypto-vision.webp`, `tick-circle.webp`

Note: `nous-contacter.webp` (2100×2238, 71 KB) is a French-targeted decorative asset — **not currently referenced** in any HTML file (potential dead asset, see §10).

---

## 3. Alt-text audit (166 `<img>` tags scanned across 28 pages)

### 3.1 Headline numbers

| Check | Count | Status |
|---|---:|---|
| Total `<img>` tags scanned | 166 | — |
| Missing `alt` attribute entirely | **0** | PASS |
| Empty `alt=""` without `aria-hidden`/`role="presentation"` | **4** | FAIL |
| Decorative images with `alt=""` + `aria-hidden`/`role` | 0 | n/a |
| `alt` present and non-empty | 162 | PASS |

### 3.2 The 4 empty-alt offenders (FR homepage)

`/home/alex/Documents/Claude/github-projets/sci/fr/index.html`
- L998 — `invest-svg-1.svg` `alt=""` (should mirror EN `alt="Étape 1 : Demandez les informations"`)
- L1016 — `invest-svg-2.svg` `alt=""` (EN: "Step 2: We will contact you with further details")
- L1034 — `invest-svg-3.svg` `alt=""` (EN: "Step 3: Sign the required documents")
- L1052 — `invest-svg-4.svg` `alt=""` (EN: "Step 4: Become an investor")

The English homepage has descriptive alts on these same four step illustrations (`alt="Step 1: Request information"` etc.). The FR version was published with empty alts. If they were meant to be decorative they would need `aria-hidden="true"`, but since the EN equivalent is informative, treat these as **content alts to translate**.

**Fix (copy-paste):**

```html
<!-- L1077 fr/index.html -->
<img src="../assets/images/svg/invest-svg-1.svg" alt="Étape 1 : Demandez les informations" class="w-full h-full" />
<!-- L1096 -->
<img src="../assets/images/svg/invest-svg-2.svg" alt="Étape 2 : Nous vous recontactons avec les détails" class="w-full h-full" />
<!-- L1115 -->
<img src="../assets/images/svg/invest-svg-3.svg" alt="Étape 3 : Signez les documents requis" class="w-full h-full" />
<!-- L1134 -->
<img src="../assets/images/svg/invest-svg-4.svg" alt="Étape 4 : Devenez investisseur" class="w-full h-full" />
```

### 3.3 Alt-text quality issues (homepage EN+FR)

The technical check passed (no missing alts), but **9 alts on the homepage are generic/non-descriptive**. These should be improved for image SERP visibility — a YMYL fund site benefits from keyword-rich, contextual alts. Both EN and FR have the same issue:

| File | Line (EN) | Current alt | Recommended |
|---|---:|---|---|
| `webp/hero-graph-img.webp` | L458, L507 | `hero graph image` | `Performance chart of SparkCore Dynamic Trends fund — net asset value growth since launch` |
| `svg/hero-arrow.svg` | L520 | `arrow` | `""` + `aria-hidden="true"` (purely decorative) |
| `webp/hero-sec-vector.webp` | L533 | `hero section vector` | `""` + `aria-hidden="true"` (purely decorative) |
| `webp/hero-image.webp` | L538 | `hero image` | `Institutional crypto investment fund management — SparkCore Investment OÜ team office` |
| `webp/blur-box.webp` | L973 | `blur box` | `""` + `aria-hidden="true"` (purely decorative) |
| `webp/contact-us-img.webp` | L978 | `graph image` | `""` + `aria-hidden="true"` (decorative panel behind contact form) |
| `webp/invest-in-us.webp` | L1043 | `invest in us image` | `Steps to invest in SparkCore Investment OÜ regulated crypto fund — process diagram` |
| `svg/dropdown-arrow.svg` | L362 | `arrow` | `""` + `aria-hidden="true"` |
| `svg/back-to-top.svg` | L1416 | `back-top` | `Back to top` (button-like, keep informative) |

The pattern is the dev kept placeholder alts from the design template instead of writing brand-aware copy. For a YMYL fund site this matters: Google Image Search and AI Overviews both consume alt text as a primary signal, and **`hero image` ranks for nothing**.

### 3.4 Alt-text quality wins (already correct)

These are already excellent and should be preserved:
- Team photos: `Photo of Paul-Antoine PONS`, `Photo of Olivier SAYEGH`, `Photo of Alexandre VINAL` — names present, but **could be enriched with role**: e.g. `Photo of Paul-Antoine PONS, Founder & Fund Manager, SparkCore Investment OÜ`. The CLAUDE.md / llms.txt does not appear to publish team roles, so this fix may need a copy decision first.
- Logo `alt="SparkCore Fund Management"` (consistent across 28 pages, in nav and footer)
- Step icons EN home: `Step 1: Request information` etc.
- All FR blog hero alts (e.g. `Salle des marchés institutionnelle pendant la crise iranienne : traders analysant...`) — keyword-rich, descriptive, follows AI-citation best practice
- All EN blog Unsplash hero alts (`Laptop with digital ID card representing Estonia e-Residency for crypto fund management...`) — descriptive

---

## 4. Oversized images (>200 KB)

3 files exceed the 200 KB threshold. All are blog hero JPGs.

| File | Pixel size | File size | Quick win |
|---|---|---:|---|
| `assets/images/jpeg/mica-casp-hero.jpeg` | 2250×1500 | **442 KB** | Convert to WebP @ q=80 → ~80–100 KB (-78 %). This is the only JPG-only blog hero — the page also lists it as `og:image`, so update both. |
| `assets/images/blog/iran-macro-shock-trading-floor.jpg` | 1600×893 | 277 KB | A WebP twin already exists (173 KB) but is unused. Either swap the `<img src>` to point at the WebP, or wrap in `<picture>` with `<source type="image/webp">`. JPG can stay as fallback (<2 % of users). |
| `assets/images/blog/panic-seller-vs-hedger.jpg` | 1600×893 | 202 KB | Same — WebP twin (106 KB) exists, just need to wire it up in `fr/blog/le-vrai-cout-du-market-timing.html` L4. |

**Pattern:** the 2 `iran-macro-shock` and `panic-seller-vs-hedger` JPGs are referenced directly from `fr/blog/le-vrai-cout-du-market-timing.html` (`src="...iran-macro-shock-trading-floor.jpg"`) — but a WebP twin already exists in the same folder. Either the dev forgot to flip the src after generating WebP, or `<picture>` was never wrapped. Same situation for `hero-market-timing-regret.jpg` (185 KB, just under 200 KB threshold).

**The three FR blog posts (`agents-ia-blockchain`, `indicateurs-marche-crypto-actifs`, `le-vrai-cout-du-market-timing`) all use `.jpg` directly when `.webp` twins exist on disk.** Same for `do-crypto-fund-managers-need-mica-casp-license` which uses `.jpeg`. **Estimated saving by switching all 8 paired JPGs to their WebP twins via `<picture>`: ~700 KB → ~315 KB on those pages, a 55 % reduction.**

### 4.1 Recommended `<picture>` wrapper pattern

```html
<picture>
  <source srcset="/assets/images/blog/iran-macro-shock-trading-floor.webp" type="image/webp">
  <img src="/assets/images/blog/iran-macro-shock-trading-floor.jpg"
       alt="Salle des marchés institutionnelle..."
       width="1600" height="893" loading="lazy">
</picture>
```

WebP browser support is now 96 %+ globally (caniuse, May 2026), so the `<source>` will be picked by virtually every visitor.

### 4.2 Future-proof: AVIF

There are zero AVIF assets. AVIF would shave another 25–35 % off the WebP files (the `iran-macro-shock-trading-floor.webp` at 173 KB would become ~115 KB AVIF). With Cloudflare Pages there's no automatic AVIF generation unless you enable Image Resizing (paid Pro plan or Workers Paid plan, ~$5/mo). For a YMYL fund site with 30 visits/day this is **not ROI-positive yet** — defer.

---

## 5. Responsive images (`srcset` + `sizes`)

3 of 166 `<img>` tags use `srcset` — all on the **EN homepage** only.

| Page | `<img>` count | `srcset` count | `sizes` count |
|---|---:|---:|---:|
| `index.html` | 26 | **3** | **3** |
| `fr/index.html` | 26 | 0 | 0 |
| All blog posts (combined) | 90 | 0 | 0 |
| Other pages | 24 | 0 | 0 |

### 5.1 EN homepage — currently OK (3 srcset)
- L458 hero-graph-img: `srcset="...-768.webp 768w, ...img.webp 1440w" sizes="(max-width: 768px) 768px, 1440px"` ✅
- L507 hero-graph-img (duplicate, second viewport block): same srcset ✅
- L538 hero-image: `srcset="...-480.webp 480w, ...-768.webp 768w, ...image.webp 1440w" sizes="(max-width: 480px) 480px, (max-width: 768px) 768px, 1440px"` ✅

### 5.2 FR homepage — REGRESSION
The FR `<img>` for hero-image (L461) has **no `srcset` and no `sizes`**, despite the 480/768 WebP variants existing on disk. Mobile users in France/Mauritius/Quebec are downloading the full 1440-wide 104 KB hero on a 360-px-wide phone.

**Fix (`fr/index.html` L461 + L385/L432 hero-graph):**

```html
<!-- L461 -->
<img src="/assets/images/webp/hero-image.webp"
     srcset="/assets/images/webp/hero-image-480.webp 480w,
             /assets/images/webp/hero-image-768.webp 768w,
             /assets/images/webp/hero-image.webp 1440w"
     sizes="(max-width: 480px) 480px, (max-width: 768px) 768px, 1440px"
     alt="Gestion de fonds crypto institutionnels..." width="1440" height="1600"
     fetchpriority="high" loading="eager">

<!-- L385 + L432 hero-graph -->
<img src="../assets/images/webp/hero-graph-img.webp"
     srcset="../assets/images/webp/hero-graph-img-768.webp 768w,
             ../assets/images/webp/hero-graph-img.webp 1440w"
     sizes="(max-width: 768px) 768px, 1440px"
     alt="..." width="1440" height="852">
```

This recovers ~80 KB on mobile for the FR home — the same Lighthouse "Properly size images" pass that EN already has.

### 5.3 Blog hero responsive variants
None of the 24 blog posts use `srcset`. Blog hero JPGs are 1200×800 or 1600×893 served as-is to mobile. For a 360-px viewport, browsers are downloading 4× more pixels than they paint. **Recommendation:** generate 768w variants for all blog heroes (8 EN local + 4 FR local + the MiCA hero = 13 images) and wrap in `<picture>` with `srcset`. Estimated saving: ~40–60 % per blog hero on mobile (~500 KB across the 4 most-trafficked blog posts).

---

## 6. `width` / `height` attributes (CLS prevention)

162 of 166 `<img>` tags have explicit `width` and `height` (97.6 %). The 4 missing are the EN homepage step icons:

| File | Lines |
|---|---|
| `index.html` | L1077, L1096, L1115, L1134 (invest-svg-1/2/3/4) |

These are 32×32 SVG icons inside flex containers — CLS risk is low (the parent `<span class="size-8">` reserves space), but adding `width="32" height="32"` is a 30-second fix and brings 100 % coverage. The FR equivalents already have these dims.

---

## 7. Lazy-loading + LCP `fetchpriority`

| Status | Count |
|---|---:|
| `loading="lazy"` | 19 |
| `loading="eager"` | 2 |
| No `loading` attribute | 145 |

### 7.1 LCP image — correctly configured

- EN homepage L538: `loading="eager"` + `fetchpriority="high"` + `<link rel="preload" as="image">` at L46 ✅
- FR homepage L461: `loading="eager"` + `fetchpriority="high"` + `<link rel="preload">` at L45 ✅

### 7.2 Below-the-fold lazy-load gap

145 `<img>` tags without any `loading` attribute. The browser default is `eager`, which forces them all to load on first paint. The biggest impact is on **homepage decorative images** (team photos, contact-us, invest-in-us, blur-box) which are deep below the fold but currently load eagerly on every visit.

**Quick win (homepage EN+FR, 16 images each):** add `loading="lazy"` to all `<img>` below row 800. Skip only the LCP candidate (already eager) and the logo (above-the-fold).

```html
<!-- L827 -->
<img src="./assets/images/webp/team-member-first.webp"
     alt="Photo of Paul-Antoine PONS" width="832" height="800" loading="lazy">
```

Estimated mobile saving: ~250 KB deferred from initial load to scroll trigger on the homepage.

### 7.3 Blog hero — should NOT be lazy
Blog hero images are above the fold and are the LCP candidate on each blog page, but currently they're tagged `loading="lazy"` (e.g. `blog/cost-to-launch-regulated-crypto-fund-europe.html` L2). On slower connections, lazy-loading the LCP image **delays LCP** instead of helping. **Fix:** change blog hero `loading="lazy"` → remove the attr (defaults to eager) and add `fetchpriority="high"`. The 11 blog posts with hero images need this, plus the 4 FR blog posts.

---

## 8. OG / social card metadata

### 8.1 OG image asset

- `meta-image.webp` — 1013×628, 75 KB
- Used by 26 of 28 pages as `og:image` and `twitter:image`
- Exception: `do-crypto-fund-managers-need-mica-casp-license.html` uses its `mica-casp-hero.jpeg` (442 KB) as og:image — works but heavy for SMS preview / Facebook bot

### 8.2 Issues

**A. Dimensions slightly off** — 1013×628 instead of the recommended 1200×630. Facebook minimum is 600×315; recommended is 1200×630 for retina displays. LinkedIn requires ≥1200×627 for proper rendering. The current size **will display, but will be downsampled** by some platforms and may appear soft on retina.

**B. No `og:image:width` / `og:image:height` / `og:image:type` declared.** Facebook's bot crawls the page even when the image isn't in cache, but explicit dims accelerate the first share.

**Recommended fix:**

1. Re-export `meta-image` at exactly 1200×630 (resize source artwork or upscale slightly). Keep WebP — Facebook, LinkedIn, Twitter all support WebP og:image as of 2025.
2. Add to `<head>` of every page that has `og:image`:

```html
<meta property="og:image" content="https://sparkcore.fund/meta-image.webp">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:type" content="image/webp">
<meta property="og:image:alt" content="SparkCore Investment OÜ — regulated crypto investment fund (Estonia, AIFM)">
<meta name="twitter:image" content="https://sparkcore.fund/meta-image.webp">
<meta name="twitter:image:alt" content="SparkCore Investment OÜ — regulated crypto investment fund">
```

**C. Single OG image for entire site** — every blog post shares the same `meta-image.webp`. For YMYL ranking this is suboptimal: each blog post should have a topic-specific OG card so social shares look distinct. The 11 EN posts that use Unsplash heroes could re-use those Unsplash URLs as `og:image` (but with `?w=1200&h=630&fit=crop&q=85` to control crop). The 4 FR posts already have local heroes that could double as OG images. The MiCA post already does this correctly. **Effort:** 30 min for all 28 pages.

---

## 9. Image sitemap

**Currently:** none. `sitemap.xml` declares URL/hreflang/lastmod/priority for 28 pages but no `<image:image>` entries.

**For a YMYL fund site this is a missed opportunity.** Image sitemaps help Google discover:
- Team photos (E-E-A-T trust signal — Google can connect Person schema to face)
- Blog hero images (so they qualify for image SERP / AI-Overview thumbnails)
- The `meta-image.webp` brand asset

**Caveat:** factsheets/PDFs are gated and the `_headers` file already sets `X-Robots-Tag: noindex` on `/factsheets/*` and `/ressources/contrats/*`. Do **NOT** include those in an image sitemap. Discovery-call, validation, 403/404/500 pages are likewise excluded.

**Suggested image sitemap** (`/sitemap-images.xml`) covering ~14 indexable assets:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
  <url>
    <loc>https://sparkcore.fund/</loc>
    <image:image>
      <image:loc>https://sparkcore.fund/assets/images/webp/hero-image.webp</image:loc>
      <image:title>SparkCore Investment — institutional crypto fund management</image:title>
    </image:image>
    <image:image>
      <image:loc>https://sparkcore.fund/assets/images/webp/team-member-first.webp</image:loc>
      <image:title>Paul-Antoine PONS — SparkCore Investment OÜ</image:title>
    </image:image>
    <image:image>
      <image:loc>https://sparkcore.fund/assets/images/webp/team-member-second.webp</image:loc>
      <image:title>Olivier SAYEGH — SparkCore Investment OÜ</image:title>
    </image:image>
    <image:image>
      <image:loc>https://sparkcore.fund/assets/images/webp/team-member-third.webp</image:loc>
      <image:title>Alexandre VINAL — SparkCore Investment OÜ</image:title>
    </image:image>
    <image:image>
      <image:loc>https://sparkcore.fund/meta-image.webp</image:loc>
      <image:title>SparkCore Investment — brand identity card</image:title>
    </image:image>
  </url>
  <!-- ... blog hero images per blog post ... -->
</urlset>
```

Then reference it in `robots.txt`:

```
Sitemap: https://sparkcore.fund/sitemap.xml
Sitemap: https://sparkcore.fund/sitemap-images.xml
```

---

## 10. Cloudflare CDN delivery

### 10.1 Headers (verified live)

```
HTTP/2 200
content-type: image/webp
content-length: 106232
cache-control: public, max-age=31536000, must-revalidate
etag: "6f2859007e7b2b875abc52db824ad62e"
server: cloudflare
cf-ray: 9f77f4f5efc59762-FRA  (Frankfurt edge — close to Estonia)
```

`max-age=31536000` (1 year) + `must-revalidate` is the right setting for content-hashed assets, **but the asset URLs are not content-hashed** (`hero-image.webp` not `hero-image.abc123.webp`). On cache-bust the user will revalidate against ETag — slow path. **Mitigation:** introduce content hashing in the build (Cloudflare Pages doesn't do this automatically for HTML-referenced assets) or accept that hero swaps need manual cache purge via dashboard.

### 10.2 Cloudflare Image Resizing

**Status: NOT enabled.** Test query `/cdn-cgi/image/width=300,quality=80/assets/images/webp/hero-image.webp` returns HTTP 404.

**Recommendation:** **defer**. Image Resizing requires Pro plan ($25/mo) or Workers Paid bundle ($5/mo). For a 30-visit/day YMYL fund site the savings (one hero asset, ~80 KB on mobile if AVIF + auto-resize) don't justify $60/year. Re-evaluate if traffic 10×.

### 10.3 Polish (lossless)

Cloudflare Polish would auto-convert images to WebP/AVIF at the edge with no URL changes — but it also requires Pro plan. Current site has WebP for almost everything anyway, so the marginal gain is the AVIF conversion of the 9 JPGs. **Defer for the same reason.**

### 10.4 Dead asset

`assets/images/webp/nous-contacter.webp` (2100×2238, 71 KB) appears not to be referenced in any HTML file (grepped all 28 pages). Either schedule to use it (FR contact section was redesigned and forgot to wire it back, or it's a French equivalent of `contact-us-img.webp`) or delete it from the build to save 71 KB at deploy time.

---

## 11. Decorative vs informative classification

YMYL/E-E-A-T standard: decorative images get `alt=""` + `aria-hidden="true"`; informative images get descriptive alts. Current state mixes the two. The 4 FR step icons (§3.2) are **informative misclassified as decorative**. The reverse problem exists too — these are **decorative misclassified as informative**:

| File | Current alt | Should be |
|---|---|---|
| `svg/hero-arrow.svg` | `arrow` | `aria-hidden="true"` + `alt=""` |
| `svg/dropdown-arrow.svg` | `arrow` | `aria-hidden="true"` + `alt=""` |
| `webp/blur-box.webp` | `blur box` | `aria-hidden="true"` + `alt=""` |
| `webp/hero-sec-vector.webp` | `hero section vector` | `aria-hidden="true"` + `alt=""` |
| `webp/contact-us-img.webp` | `graph image` | `aria-hidden="true"` + `alt=""` |

Screen readers currently announce "arrow" / "blur box" / "graph image" — confusing for assistive tech users.

### 11.1 Charts & diagrams

`hero-graph-img.webp` (homepage L458/L507) and `invest-in-us.webp` (L1043) are **informative** chart-style images. Currently `alt="hero graph image"` and `alt="invest in us image"`. They need:

1. Descriptive alt with the data conveyed (`Performance chart of SparkCore Dynamic Trends fund — net asset value indexed at 100 since launch August 2025`)
2. A nearby `<figcaption>` or visible caption text that matches (current site has no `<figure>` wrapper).

This is the highest-impact alt fix for YMYL — Google's E-E-A-T raters explicitly look at chart accessibility.

---

## 12. Prioritized action queue

### Critical (do this week)

1. **Fix 4 empty alts on `fr/index.html`** (§3.2) — 5 min, prevents WCAG 2.1 SC 1.1.1 fail
2. **Switch FR blog post images to WebP via `<picture>`** (§4.1) — 4 files, ~30 min, saves ~700 KB total
3. **Convert `mica-casp-hero.jpeg` to WebP** (§4) — 5 min, saves 350 KB. Update both `<img src>` and `og:image` reference
4. **Improve generic alts on homepage** (§3.3) — 9 alts EN, 9 alts FR, 30 min total. The "hero image" / "graph image" / "blur box" ones lose ranking signal

### High (do this month)

5. **Add `srcset`/`sizes` to FR homepage hero + hero-graph** (§5.2) — 15 min, mobile perf parity with EN
6. **Generate 768w blog hero variants + wire them up** (§5.3) — 13 images, ~1 h with sharp/squoosh CLI
7. **Lazy-load below-the-fold homepage images** (§7.2) — 16 images × 2 locales, 15 min
8. **Remove `loading="lazy"` from blog hero images** (§7.3) — 15 files, 15 min — fixes LCP
9. **Add OG image dimension metadata + per-post OG images** (§8.2) — 28 pages, 30 min for global meta + 1 h for per-post images

### Medium (next quarter)

10. **Generate image sitemap** (§9) — covers homepage hero, team photos, blog heroes, brand card. 1 h to write generator
11. **Reclassify 5 decorative images as `aria-hidden`** (§11) — accessibility win, 10 min
12. **Add chart `<figcaption>` + descriptive alt to hero-graph and invest-in-us** (§11.1) — 30 min, E-E-A-T win

### Low / defer

13. **Cloudflare Image Resizing** — defer until 10× traffic
14. **AVIF generation pipeline** — defer
15. **Delete or wire up `nous-contacter.webp`** (§10.4) — 5 min cleanup

---

## 13. Summary metrics

- Total `<img>` tags audited: **166** across 28 pages
- Pages audited: **28** (2 home + 23 blog EN + 4 blog FR + 2 blog index + privacy + discovery + validation + 3 errors — note: 5 of the 28 served as "blog index/error" don't carry hero content)
- Asset count: **56** files, **2.80 MB** total
- WebP coverage of bitmap heroes: **89 %** (16 of 18 raster heroes have a WebP version on disk; 4 are still served as JPG in HTML despite WebP twin existing)
- Alt attribute coverage: **100 %** (no missing `alt`)
- Alt non-empty rate: **97.6 %** (4 empty on FR home that should be informative)
- Width/height coverage: **97.6 %** (4 missing on EN home step icons)
- LCP image properly hinted (`fetchpriority=high` + preload + eager): **YES** on both home pages
- Cloudflare cache headers: **OK** (`max-age=31536000, must-revalidate`, ETag, served from FRA edge for EU/Estonia audience)
- Cloudflare Image Resizing: **OFF** (recommendation: keep off until traffic justifies $60/yr)
- Image sitemap: **NONE** (recommendation: create)
