# SparkCore.fund — SEO Action Plan (2026-05-08)

**Companion to:** `FULL-AUDIT-REPORT.md`
**Current SEO Health Score:** 71 / 100 — C+
**Target after Sprint 1 (8-12 h work):** ~78-80 / 100 — B+

Tasks are ordered by **expected ROI per hour of effort**. Severity: Critical → High → Medium → Low. Effort: S = ≤30 min, M = 30-90 min, L = 2-4 h, XL = full day+.

---

## SPRINT 1 — Quick Wins (~6 hours total, +8 score points)

These are small edits with disproportionate impact. Ship in one PR each.

### S1-1 · Defer `lang-redirect-en.js` and `lang-redirect-fr.js`
**Sev:** High · **Effort:** S (5 min) · **Source:** Performance #1
**File:** `index.html`, `fr/index.html`
**Change:** Add `defer` attribute to both script tags. The bot-skip + URL-priority logic does not need to run before `<body>` parsing.
**Impact:** -100 to -200 ms LCP on every pageview, mobile especially.

### S1-2 · Fix `_headers` rule + robots.txt for `/validation`
**Sev:** Medium · **Effort:** S (5 min) · **Source:** Technical T-01
**Files:** `_headers`, `robots.txt`
**Change:** Replace `/validation.html` with `/validation` in both files (CF Pages canonicalizes the URL).
**Impact:** Closes a single-layer noindex gap on a gated page.

### S1-3 · Add `imagesrcset` + `imagesizes` to hero preload
**Sev:** High · **Effort:** S (15 min) · **Source:** Performance #3
**File:** `index.html`, `fr/index.html`
**Change:** Replace bare hero preload link with responsive variant:
```html
<link rel="preload" as="image"
      href="/assets/images/webp/hero-image.webp"
      imagesrcset="/assets/images/webp/hero-image-480.webp 480w,
                   /assets/images/webp/hero-image-1024.webp 1024w,
                   /assets/images/webp/hero-image.webp 1440w"
      imagesizes="(max-width: 600px) 480px, (max-width: 1100px) 1024px, 1440px"
      fetchpriority="high">
```
(generate the 480w + 1024w variants with `sharp` if not present)
**Impact:** Saves 60-70 KB on mobile + correctly prefetches the right variant. -150 to -300 ms LCP mobile.

### S1-4 · Add 1-line trust signal beneath homepage H1
**Sev:** High · **Effort:** S (30 min) · **Source:** SXO F-2
**Files:** `index.html`, `fr/index.html`
**Change:** Add inline trust line in hero section, below the H1, above the CTA:
```html
<p class="text-sm text-mediumGray mt-2">
  Supervised by Finantsinspektsioon (EE) ·
  LEI <a href="https://search.gleif.org/#/record/8945003BBN0RVNNB0S84">8945003BBN0RVNNB0S84</a> ·
  Audited by KPMG Estonia
</p>
```
French equivalent on `/fr/`.
**Impact:** First-second Skeptic-persona conversion. Above-the-fold trust answer the homepage currently fails to deliver.

### S1-5 · Add `defer` `lang-redirect-fr.js` AND remove invalid robots stanza
**Sev:** Low · **Effort:** S (10 min) · **Sources:** Technical T-04 + Performance #1 (FR)
**File:** `robots.txt`
**Change:** Remove `User-agent: Wayback Machine` (invalid token, inert). `ia_archiver` already blocks Wayback.

### S1-6 · Enable HSTS Preload
**Sev:** Medium · **Effort:** S (10 min — manual, dashboard) · **Source:** Technical T-02
**Where:** Cloudflare dashboard → SSL/TLS → Edge Certificates → HSTS → Enable preload + submit to https://hstspreload.org/?domain=sparkcore.fund
**Prereq:** HSTS already at `max-age=31536000; includeSubDomains` ✅. Zone has been stable since 2026-05-06 ✅.
**Impact:** Closes first-visit HTTPS upgrade window across all browsers (6-12 weeks for Chromium pickup).

### S1-7 · Add `Speakable` schema to pillar + top 3 articles + homepage
**Sev:** Medium · **Effort:** M (1 h) · **Source:** GEO #2
**Files:** `resources/regulated-crypto-fund-estonia/index.html`, top 3 EN blog articles, `index.html`
**Change:** Add to existing JSON-LD blocks:
```json
"speakable": {
  "@type": "SpeakableSpecification",
  "cssSelector": [".quick-answer", "h2", ".key-takeaways"]
}
```
**Impact:** Direct AI Overviews + voice-search citation eligibility.

### S1-8 · Author Person `sameAs` + `jobTitle` on all blog articles
**Sev:** High · **Effort:** M (1 h, templated) · **Sources:** Schema #2 + Content E-E-A-T HIGH + GEO #3
**Files:** All 19 EN blog articles + 4 FR blog articles
**Change:** Replace minimal `author` Person block with the standalone Person schema already proven on the pillar:
```json
"author": {
  "@type": "Person",
  "@id": "https://sparkcore.fund/#person-alexandre-vinal",
  "name": "Alexandre VINAL",
  "url": "https://www.linkedin.com/in/alexandrevinal/",
  "jobTitle": "Founder & Managing Partner, SparkCore Fund Management",
  "sameAs": [
    "https://www.linkedin.com/in/alexandrevinal/",
    "https://www.youtube.com/@cointips"
  ]
}
```
Use a build-time include or the existing template helper rather than copy-paste.
**Impact:** YMYL E-E-A-T author trust on every article + AI entity disambiguation.

### S1-9 · Fix `crypto-fund-fees-2026` future date
**Sev:** Medium · **Effort:** S (5 min) · **Source:** Schema
**File:** `blog/crypto-fund-fees-2026.html`
**Change:** `datePublished` is `2026-05-12` — future. Set to actual publish date.

### S1-10 · `Article` retype on pillar
**Sev:** Medium · **Effort:** S (10 min) · **Source:** Schema #3
**File:** `resources/regulated-crypto-fund-estonia/index.html`
**Change:** `"@type": "BlogPosting"` → `"@type": "Article"`. Add `"articleSection": "Regulatory Guide"`.
**Impact:** Aligns with breadcrumb label, opens Article rich result eligibility.

---

## SPRINT 2 — High-Impact Content (8-10 h, +6-8 score points)

### S2-1 · Comparison table on `/blog/estonia-luxembourg-malta-crypto-fund`
**Sev:** HIGH · **Effort:** L (2-3 h) · **Source:** SXO F-1 + GSC top non-brand impression
**File:** `blog/estonia-luxembourg-malta-crypto-fund.html`
**Change:** Add a structured HTML table above-the-fold (within first 500 words) comparing the three jurisdictions across at least: minimum capital, AIFM threshold, registration timeline, total launch cost, EU passport rights, MiCA scope. Keep prose body below.
**Impact:** Highest-leverage content edit on the entire site. Currently 193 imp @ p8.1, 0.5% CTR. Comparison-format SERP signal — expected CTR lift to 3-5%, position lift to p4-6.

### S2-2 · Add author bio box to all blog article templates
**Sev:** CRITICAL · **Effort:** L (2 h template + apply) · **Source:** Content E-E-A-T CRITICAL
**Files:** All blog article templates
**Change:** Add a standardized 3-5 line bio block at the article foot:
```html
<aside class="article-bio mt-12 border-t border-paleBlue pt-8">
  <img src="/assets/images/webp/alexandre-vinal.webp"
       alt="Alexandre VINAL" class="w-16 h-16 rounded-full" />
  <h3>About the author</h3>
  <p>Alexandre VINAL is Managing Partner of SparkCore Fund Management
  (SparkCore.investment OÜ), a Finantsinspektsioon-supervised AIFM
  in Estonia. Reg. 16265864 · LEI 8945003BBN0RVNNB0S84.
  <a href="https://www.linkedin.com/in/alexandrevinal/">LinkedIn</a> ·
  <a href="https://www.youtube.com/@cointips">YouTube</a></p>
</aside>
```
Visible to readers; not just schema.
**Impact:** Closes the largest YMYL Trustworthiness gap. Single highest E-E-A-T uplift in the audit.

### S2-3 · Visible "Last reviewed" line + `dateModified` cadence
**Sev:** CRITICAL · **Effort:** M (1 h ops + recurring) · **Source:** Content E-E-A-T CRITICAL + GEO #5
**Files:** All blog article templates
**Change:** Add visible line beneath the byline: "Last reviewed: 2026-05-08" — drive from a single canonical metadata source. Establish quarterly review cadence: any time you re-touch an article, bump `dateModified` AND add at least one substantive paragraph (not a typo fix).
**Impact:** Currency signal to Google + LLMs. Frozen `dateModified` on YMYL = "this content has never been reviewed."

### S2-4 · AIFMD II content patches on regulatory articles
**Sev:** HIGH · **Effort:** L (2-3 h) · **Source:** Content E-E-A-T HIGH
**Files:** `blog/regulated-crypto-fund-manager-estonia`, `blog/sub-threshold-aifm-crypto-estonia`, `blog/do-crypto-fund-managers-need-mica-casp-license`, pillar
**Change:** Each article should explicitly mention the AIFMD II transposition deadline (April 2026) and the 1 July 2026 VASP licence sunset where relevant. `regulated-crypto-fund-manager-estonia` (pub March 2026) currently doesn't mention AIFMD II at all.
**Impact:** Expertise + freshness simultaneously.

### S2-5 · Pillar CTA on `crypto-fund-fees-2026`
**Sev:** HIGH · **Effort:** S (15 min) · **Source:** Content E-E-A-T HIGH
**File:** `blog/crypto-fund-fees-2026.html`
**Change:** Add the same pillar-CTA block already used in `regulated-crypto-fund-manager-estonia`, pointing to `/resources/regulated-crypto-fund-estonia/`.

### S2-6 · Founder-persona CTA on regulatory articles
**Sev:** HIGH · **Effort:** L (2 h) · **Source:** SXO F-3
**Files:** Top 4-6 regulatory blog articles
**Change:** Add inline CTA block:
```html
<aside class="cta-founder">
  <h3>Looking to launch your own regulated fund?</h3>
  <p>SparkCore offers white-label AIFM structuring services in Estonia.</p>
  <a href="/discovery-call?source=blog-founder">Schedule a Founders Call →</a>
</aside>
```
SparkCore already ranks p1-4 for "crypto AIFM estonia" — Founder traffic arrives but has no entry point.
**Impact:** Activates a conversion path that already exists in latent demand.

---

## SPRINT 3 — Schema + Architecture (4-6 h, +3-5 score points)

### S3-1 · Add `@id` to Organization, FinancialService, Person nodes
**Sev:** CRITICAL · **Effort:** M (1 h) · **Source:** Schema #1
**Files:** All HTML pages
**Change:** Add `@id` to every entity reused across pages so Google can merge the nodes:
- Organization: `"@id": "https://sparkcore.fund/#organization"`
- FinancialService: `"@id": "https://sparkcore.fund/#financialservice"`
- Person Alexandre VINAL: `"@id": "https://sparkcore.fund/#person-alexandre-vinal"`
- Person Paul-Antoine Pons / Olivier Sayegh similarly
- WebPage: `"@id": "<page-url>#webpage"`
On BlogPosting `publisher`, replace nested Organization with `{"@id": "https://sparkcore.fund/#organization"}` reference (and unify trailing slash to `https://sparkcore.fund/`).
**Impact:** Single Knowledge Graph entity across all pages, instead of N anonymous re-declarations.

### S3-2 · Add `WebSite` + `potentialAction SearchAction`
**Sev:** Medium · **Effort:** S (15 min) · **Source:** Schema
**File:** `index.html`
**Change:** Add to `@graph`:
```json
{
  "@type": "WebSite",
  "@id": "https://sparkcore.fund/#website",
  "url": "https://sparkcore.fund/",
  "name": "SparkCore Fund Management",
  "publisher": {"@id": "https://sparkcore.fund/#organization"},
  "inLanguage": ["en", "fr"]
}
```
(SearchAction only if site search exists — currently no internal search; skip.)
**Impact:** WebSite entity in graph, sitelinks searchbox eligibility if site search is added later.

### S3-3 · Convert `image` strings to `ImageObject` on articles
**Sev:** Medium · **Effort:** M (1 h, templated) · **Source:** Schema
**Change:** Replace `"image": "https://..."` with `"image": {"@type": "ImageObject", "url": "...", "width": 1260, "height": 750}` on all BlogPosting / Article schemas.
**Impact:** Article rich-result eligibility on Google.

### S3-4 · Standalone founder profiles + founder pages
**Sev:** Medium · **Effort:** L (2-3 h) · **Source:** Schema + GEO
**Files:** Optional new `/about/team` page or 3 founder pages
**Change:** Create publicly visible bio pages for the 3 Managing Partners (Alexandre VINAL, Paul-Antoine PONS, Olivier SAYEGH). Each carries full Person schema with `sameAs`, `jobTitle`, education/credentials, role at SparkCore. Link from homepage Organization `founder` URLs.
**Impact:** YMYL author entity resolution; AI platforms can verify founder claims.

### S3-5 · BlogPosting `about` regulatory linking
**Sev:** Low · **Effort:** M (1 h, templated) · **Source:** GEO
**Change:** On regulatory articles, add `"about": [{"@type": "Thing", "name": "AIFMD", "sameAs": "https://eur-lex.europa.eu/eli/dir/2011/61/oj"}]`.

---

## SPRINT 4 — Performance Polish (3-4 h, +5-8 sub-score points)

### S4-1 · Async-load both render-blocking CSS files
**Sev:** HIGH · **Effort:** L (2-3 h) · **Source:** Performance #2
**Files:** `index.html`, `fr/index.html`, all blog/article templates
**Change:** Use the same preload-swap pattern already proven for AOS and Toastify:
```html
<link rel="preload" href="./assets/css/style.css?v=1.6" as="style"
      onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="./assets/css/style.css?v=1.6"></noscript>
<link rel="preload" href="./assets/css/tailwind.min.css?v=1.0" as="style"
      onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="./assets/css/tailwind.min.css?v=1.0"></noscript>
```
Then extract ~5-8 KB of above-fold critical CSS (logo + hero typography + first paint colors) and inline in `<head>`.
**Impact:** -300 to -600 ms LCP. Biggest performance gain available.

### S4-2 · Investigate why `tailwind.min.css?v=1.0` is not Brotli-compressed at CF edge
**Sev:** Medium · **Effort:** M (30 min — debug) · **Source:** Performance
**Where:** Cloudflare dashboard → Speed → Optimization → Brotli (verify ON globally) → check origin headers; possibly file is being served pre-compressed or excluded by URL pattern.
**Impact:** ~22 KB savings on every first pageview if root-caused.

---

## SPRINT 5 — Authority + Backlinks (Multi-week)

### S5-1 · Wikidata entity + QID
**Sev:** HIGH · **Effort:** L (3-5 h create, +2-4 weeks pickup) · **Source:** GEO #1
**Where:** wikidata.org
**Change:** Create Wikidata item for SparkCore.investment OÜ with: P31 (instance of) → Alternative Investment Fund Manager, P17 (country) → Estonia, P1278 (LEI), P3548 (Estonian registry), P361 (regulator → Finantsinspektsioon), P159 (HQ → Pudisoo), P749 (auditor → KPMG). Founders: P112. Sister Wikidata item for Alexandre VINAL linking Cointips YouTube. Add the QID to homepage Organization `sameAs` and to `llms.txt`.
**Impact:** Strongest entity-disambiguation signal AI platforms can recognize.

### S5-2 · Disambiguation block in `llms.txt`
**Sev:** Medium · **Effort:** S (10 min) · **Source:** GEO #5
**File:** `llms.txt`
**Change:** Add `## Disambiguation` section: "SparkCore Fund Management (SparkCore.investment OÜ, LEI 8945003BBN0RVNNB0S84) is not affiliated with Spark Networks SE, the SparkCore game engine, or Spark Energy."

### S5-3 · Launch press release on a regulated finance wire
**Sev:** HIGH · **Effort:** L (4-6 h once + agency support) · **Source:** Backlinks #1
**Where:** CityWire, Hedge Week, Investment Europe, Funds Society
**Impact:** Single press release on a Tier-1 wire typically generates 10-20 syndicated referring domains in 30 days. For a regulated fund, this is the standard first-mover.

### S5-4 · Industry directory submissions
**Sev:** Medium · **Effort:** L (3-4 h) · **Source:** Backlinks
**Where:** AIMA (Alternative Investment Management Association), FinanceEstonia, ESMA professional contacts list, ALFI Estonia chapter, EU crypto fund directories.
**Impact:** Slow but durable authority signals from finance-vertical .org and registry-style domains.

### S5-5 · Embed founder YouTube videos on regulatory articles
**Sev:** HIGH · **Effort:** M (1-2 h) · **Source:** GEO multi-modal
**Where:** Top 3 EN regulatory articles
**Change:** Embed 1-2 thematically relevant Cointips videos. The YouTube channel is already in `sameAs` and the founder hosts it — owned-media authority is strongest video signal in GEO research (~0.737 correlation with AI citations).

---

## SPRINT 6 — Misc maintenance

### S6-1 · Fix Bing WMT API endpoint
**Sev:** Medium · **Effort:** S (15 min) · **Source:** Backlinks
**File:** `~/.config/claude-seo/backlinks-projects/sci.json`
**Check:** `bing_verified_sites` value matches exactly what is registered in Bing Webmaster Tools (likely a trailing slash or http/https mismatch).
**Impact:** Re-enables Bing backlinks data path for next audit.

### S6-2 · Remove legacy `www.sparkcore.fund/sitemap.xml` from Bing WMT
**Sev:** Low · **Effort:** S (5 min, dashboard) · **Source:** Sitemap
**Where:** Bing WMT UI → Sitemaps → remove the `www.` prefixed entry (10 URLs, obsolete since CF migration).

### S6-3 · `_redirects` 308→301 consistency for FR blog
**Sev:** Low · **Effort:** S (5 min) · **Source:** Technical T-03
**File:** `_redirects`
**Change:** Add `/fr/blog/:slug/ → /fr/blog/:slug 301`.

### S6-4 · Remove `priority` and `changefreq` from sitemap
**Sev:** Low · **Effort:** S (10 min) · **Source:** Sitemap
**File:** `sitemap.xml` (or build script if generated)
**Change:** Both fields ignored by Google. Strip on next regeneration.

### S6-5 · Annotate or remove legacy `.htaccess`
**Sev:** Low · **Effort:** S (5 min) · **Source:** Technical T-05
**File:** `.htaccess`
**Change:** Add comment header `# LEGACY — sparkcore.fund migrated to Cloudflare Pages on 2026-05-06. CF Pages does not execute Apache config. Kept for reference only.`

---

## Recommended Sequencing

**Week 1** — Sprint 1 quick wins (S1-1 → S1-10) + S6-1 (Bing API fix). Single dev session, ~6 h. Deploy via PR to `beta` branch, test on `beta.sparkcore.fund`, then merge to `main`.

**Week 2** — Sprint 2 content work (S2-1 → S2-6). 8-10 h. The comparison table on `/blog/estonia-luxembourg-malta-crypto-fund` is the single highest-impact item — ship that first.

**Week 3** — Sprint 3 schema + Sprint 4 performance polish. 4-6 + 3-4 h.

**Week 4-8** — Sprint 5 authority work in parallel with editorial calendar. The Wikidata item is high-leverage but needs review time; press release needs PR vendor coordination.

**Re-audit** — Run `/seo audit` again at 2026-08-08. Expected target: **80-83 / 100 (B+)** assuming Sprints 1-4 ship clean.

---

## Out of Scope / Decisions Already Made

The following were considered and confirmed *not* to be addressed (consistent with `MD/CLAUDE.md` decisions):

- **CSP `'unsafe-inline'`** — conscious tradeoff for static site without Workers. Keep.
- **SRI on jsDelivr scripts** — maintenance cost > benefit. Skip until handling payments/auth.
- **EN ↔ FR cross-cluster hreflang** — by design dual-cluster, no cross-translations.
- **Microsoft Clarity** — declined per traffic volume and DPA cost.
- **Moz API** — abandoned project-wide (CB Maurice rejected).
- **DataForSEO** — defer; activate ad-hoc only for backlinks deep-dive at ~$0.50/1k.

---

## Score Trajectory Outlook

| Milestone | Target Score | Required Effort |
|---|---|---|
| Today (2026-05-08) | 71 / 100 | — (baseline) |
| After Sprint 1 (Week 1) | ~75 / 100 | 6 h |
| After Sprint 2 (Week 2) | ~78 / 100 | +8-10 h |
| After Sprints 3+4 (Week 3) | ~80-82 / 100 | +7-10 h |
| After Sprint 5 (Month 2-3) | ~84-87 / 100 | +10-15 h spread |
| Steady state (with cadence) | ~88-90 / 100 | quarterly review + content work |

The remaining gap to 100 is structural — backlinks (32 → ?, scoring impossible without data + organic age), and editorial coverage (Wikipedia/Tier-1 press), both of which take 6-12 months to materialize for a regulated YMYL fund.
