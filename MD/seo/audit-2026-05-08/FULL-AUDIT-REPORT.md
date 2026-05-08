# SparkCore.fund — Full SEO Audit (2026-05-08)

**Site:** https://sparkcore.fund/
**Type:** YMYL Financial — Regulated AIFM (Crypto Fund Manager), Estonia
**Audit date:** 2026-05-08
**Audited by:** claude-seo (8 specialist agents)

---

## Executive Summary

**Overall SEO Health Score: 71 / 100 — C+ (Solid foundation, several high-leverage gaps)**

| Category | Weight | Score | Weighted |
|---|---|---|---|
| Technical SEO | 22% | 86 | 18.9 |
| Content Quality / E-E-A-T | 23% | 68 | 15.6 |
| On-Page SEO / SXO | 20% | 67 | 13.4 |
| Schema / Structured Data | 10% | 52 | 5.2 |
| Performance (CWV) | 10% | 62 | 6.2 |
| AI Search Readiness | 10% | 72 | 7.2 |
| Images | 5% | 80 | 4.0 |
| **Total** | **100%** | | **70.5 → 71** |

**Bonus observability:**
- Backlinks: 32/100 — *planning baseline only* (Common Crawl no data, Bing API endpoint mismatch). Not included in weighted score per insufficient data.
- Sitemap: 92/100 (rolled into Technical SEO).
- GSC visibility: 11 clicks / 28d — 100% brand-navigational.

### Top 5 Critical / High-Leverage Issues

1. **`dateModified` frozen at `datePublished` on every blog article** — YMYL freshness fail. Articles covering AIFMD II (transposition deadline April 2026) and the 1 July 2026 VASP licence sunset look "never reviewed" to Google + LLMs. (CRITICAL — Content / GEO)
2. **No author bio boxes on any blog article** — only a byline. For YMYL financial, QRG explicitly weighs author credentials. Pillar has the schema but visitors never see it. (CRITICAL — E-E-A-T)
3. **No `@id` on Organization / FinancialService / Person nodes** — every page declares the same entity as a disconnected anonymous node. Breaks Knowledge Graph entity merging and weakens E-E-A-T cross-page consistency. (CRITICAL — Schema)
4. **Comparison-format mismatch on `/blog/estonia-luxembourg-malta-crypto-fund`** — Google rewards a structured comparison table for that query; SparkCore ships narrative prose. 193 impressions @ p8.1, 0.5% CTR. Single highest-impact page edit on the site. (HIGH — SXO / Content)
5. **Two render-blocking CSS files in `<head>`, `tailwind.min.css?v=1.0` not Brotli-compressed at the edge** — 29.5 KB raw, would be 7-9 KB with Brotli. LCP estimate 2.2-2.8 s on borderline hardware. (HIGH — Performance)

### Top 5 Quick Wins (1-2 hour effort, high uplift)

1. **Add Speakable schema to pillar + top 3 blog articles** — 1 h, immediate AI Overviews / voice eligibility (GEO).
2. **Add author Person `sameAs` (LinkedIn, YouTube) on every blog article** — 30 min template change, fixes 19 articles at once (E-E-A-T + GEO).
3. **Add `defer` to `lang-redirect-en.js`** — 30 sec attribute change, eliminates a parser-block on every pageview (Performance, +100-200 ms LCP mobile).
4. **Add 1-line regulatory trust signal beneath H1 on homepage** — "Supervised by Finantsinspektsioon (EE) · LEI: 8945003BBN0RVNNB0S84" (SXO Skeptic persona, 30 min).
5. **Fix `_headers` rule on `/validation`** — currently targets `/validation.html` which CF Pages canonicalizes. Single-layer noindex gap (Technical, 5 min).

---

## 1. Technical SEO — 86 / 100

Source: `technical-seo.md`.

**What passes:** TLS 1.3 + 0-RTT + HTTP/3, full security header set (CSP via CF Transform Rule, HSTS 12mo, X-Frame, X-Content-Type, Referrer-Policy, Permissions-Policy), robots.txt with explicit AI crawler allowlist + archive bot block, valid sitemap with hreflang xhtml namespace, www → non-www 301, canonical/hreflang correct on `/` ↔ `/fr/`, PDF gate (CF Pages Function) returns 403 on missing hash, gated pages defense-in-depth (`/discovery-call` HTTP 200 + X-Robots-Tag noindex confirmed), JS rendering not required (static SSR), URL-path-first language detection guarantees Googlebot sees French on `/fr/`, IndexNow + Bing WMT verified.

**Findings:**

| ID | Sev | Finding | Fix |
|---|---|---|---|
| T-01 | Med | `_headers` rule for `/validation.html` but CF canonicalizes to `/validation` (no extension). Live `/validation` HTTP 200 has no `X-Robots-Tag`. | Change `_headers` and `robots.txt` entries to `/validation`. |
| T-02 | Med | HSTS preload flag absent — site not in browser preload list. | Enable preload in CF dashboard, submit to hstspreload.org. |
| T-03 | Low | FR blog returns 308 (vs EN 301) on trailing-slash redirect — inconsistent. | Add `/fr/blog/:slug/ → /fr/blog/:slug 301` to `_redirects`. |
| T-04 | Low | Robots `User-agent: Wayback Machine` is invalid token — inert. Real one (`ia_archiver`) already blocked. | Remove the stanza. |
| T-05 | Low | `.htaccess` deployed but ignored by CF Pages — risk of dev confusion. | Add legacy comment header or remove from repo. |

---

## 2. Content Quality + E-E-A-T — 68 / 100

Source: `content-eeat.md`.

**E-E-A-T weighted breakdown (YMYL):**
- Experience 14/20 — case study in blog-en-1 genuine; no author bio box.
- Expertise 18/25 — strong technical accuracy; no credentials disclosed on articles.
- Authority 14/25 — FI.ee + GLEIF in schema/footer; zero external editorial coverage.
- Trustworthiness 15/30 — disclaimers present, but `dateModified` frozen = critical freshness fail.

**Critical findings:**

| Sev | Finding | Fix |
|---|---|---|
| CRIT | `dateModified` = `datePublished` on all 4 sampled pages. AIFMD II not even mentioned in articles published March 2026 yet `dateModified` is March 2026. | Add visible "Last reviewed" line; bump `dateModified` quarterly with substantive paragraph updates. |
| CRIT | No author bio box on any article — credentials invisible to readers. | Add 3-5 line bio at article bottom: role, fund registration, years experience, LinkedIn. |
| HIGH | Author `Person` schema has only `url`, missing `sameAs` (LinkedIn, YouTube `@cointips`) and `jobTitle`. | Template change across all 19 EN + 4 FR articles. |
| HIGH | `crypto-fund-fees-2026` covers AIFMD II fee disclosure but doesn't link to the pillar. | Add pillar CTA block (same pattern as blog-en-1). |
| HIGH | Homepage body has no visible investment risk disclaimer between fund cards and CTA. | Add 1-sentence body disclaimer. Footer alone is insufficient YMYL signal. |
| HIGH | `regulated-crypto-fund-manager-estonia` (pub 2026-03-09) doesn't mention AIFMD II at all. | Add AIFMD II paragraph in Section 6; bump `dateModified`. |
| MED | FR cluster has 3 internal links per article; zero lateral links between FR articles. | Add 2 lateral links per FR article. |
| MED | No editorial reviewer signal anywhere. | Add `reviewedBy` schema or "Reviewed by SparkCore compliance" footer line. |
| MED | `blog-en-1` schema `wordCount` 17% understated. | Update to actual count. |
| LOW | Pillar typed `BlogPosting` but breadcrumb labels it "Resources". | Switch to `Article` + add `articleSection`. |
| LOW | Generic OG image on EN blog cluster (only pillar + FR uses per-article images). | Create per-article OG images. |

---

## 3. Schema / Structured Data — 52 / 100

Source: `schema.md`.

**What passes:** All JSON-LD syntactically valid. `@context` correct everywhere. YMYL fields present on `Organization` + `FinancialService` (`leiCode`, `taxID`, `sameAs` to GLEIF, `memberOf` Finantsinspektsioon, `address`, `areaServed`). FAQPage answers match visible content. BreadcrumbList present on articles.

**3 Critical issues:**

1. **No `@id` on Organization, FinancialService, Person, BlogPosting anywhere.** Every page declares the same entity as a disconnected anonymous node — Google cannot merge nodes into a single Knowledge Graph entity. The `publisher` object on BlogPosting also has trailing-slash inconsistency (`https://sparkcore.fund` vs `https://sparkcore.fund/`).
2. **Author Person on all 20+ blog articles missing `sameAs` and `jobTitle`** (only `name` + `url`). Standalone richer Person block exists on the pillar but is not referenced from any article.
3. **Pillar typed `BlogPosting` but editorially an `Article`/guide** — type contradicts breadcrumb label.

**Other notable:**
- No `WebSite` + `SearchAction` — sitelinks searchbox eligibility foregone.
- `image` is a bare string URL on articles (must be `ImageObject` with width/height for Article rich result eligibility).
- `isAccessibleForFree` missing on `crypto-fund-fees-2026` and `strategies-options`.
- `crypto-fund-fees-2026` has `datePublished: 2026-05-12` — future date as of audit.
- Nav `ItemList` only lists 3 items (Home, Blog, Privacy Policy) — incomplete (Resources/Funds pages exist).
- No `speakable` anywhere — low-effort GEO win.
- No schema on `/privacy-policy`.
- FAQPage ineligible for Google rich results on commercial sites since Aug 2023, but valuable for AI ingestion — keep.

---

## 4. Sitemap — 92 / 100

Source: `sitemap.md`.

**Pass:** XML valid, 34 URLs, gated pages absent (`/factsheets/*`, `/discovery-call`, `/MD/`), hreflang consistent with dual-cluster strategy (EN/FR independent), lastmods plausible & varied, blog articles correctly self-canonical without trailing slash.

**Findings (all Low/Info):**
- `priority` and `changefreq` tags present but ignored by Google — remove on next regeneration.
- FR blog cluster is 5 articles, not 4 (documentation discrepancy in CLAUDE.md).
- Bing WMT still has the legacy `www.sparkcore.fund/sitemap.xml` (10 URLs) submission — remove from Bing WMT UI.

---

## 5. Performance / CWV — 62 / 100

Source: `performance.md`.

**Lab estimates** (no CrUX field data — insufficient Chrome traffic, expected for new site):

| Metric | Estimate | Status |
|---|---|---|
| LCP | ~2.2-2.8 s | Needs Improvement |
| INP | ~80-140 ms | Good |
| CLS | ~0.02-0.05 | Good |

**What's pulling LCP down:**
1. Two render-blocking CSS files: `style.css?v=1.6` (4.4 KB Brotli) + `tailwind.min.css?v=1.0` (**29.5 KB raw — not Brotli-compressed at CF edge**). Brotli compression alone would cut 22+ KB.
2. `lang-redirect-en.js` is the **first script in `<body>` with no `async` or `defer`** — fully parser-blocking on every pageview, even though redirect logic only matters for FR-language browsers.
3. Hero image preload lacks `imagesrcset` / `imagesizes` — mobile (480w) preloads the full 1440w image (106 KB) instead of an appropriate variant.

**What works well:** HTTP/3, TLS 1.3 + 0-RTT, Early Hints, 1-year browser cache, ApexCharts deferred, AOS/Toastify CSS preload-swap correct, all images have explicit width/height (CLS clean), analytics + Cronitor + Turnstile all async/defer.

---

## 6. AI Search / GEO Readiness — 72 / 100

Source: `geo-ai.md`.

**Per-platform:**
| Platform | Score |
|---|---|
| Perplexity | 78 |
| ChatGPT search | 76 |
| Google AI Overviews | 74 |
| Claude | 72 |
| Gemini | 70 |
| Bing Copilot | 68 |

**Strengths:** All 6 AI crawlers explicitly allowed in robots; gated paths blocked per-bot. `llms.txt` and `llms-full.txt` present, RSL 1.0 licensed, well-structured (entity, regulators, fund inventory, team with LinkedIn, key terms, article inventory). Statistics in body text are source-attributed (bfinance, PwC/AIMA, Crypto Insights Group). FAQPage on every page. Static SSR.

**Highest-impact gaps:**
- No Wikidata entity / Wikipedia article — for YMYL, AI platforms weight independent Knowledge Graph nodes more heavily than self-declared schema. SparkCore has every prerequisite (LEI, GLEIF, dual regulator, KPMG audit, named founders) — just hasn't created the QID.
- No Speakable schema anywhere.
- Author Person schema only on pillar — absent from all 19 EN articles.
- No proprietary charts, no embedded video — despite founder running the Cointips YouTube channel which is in the Organization `sameAs`. Per GEO research, owned-video correlation with AI citations is ~0.737 (strongest single brand signal).
- No disambiguation block in `llms.txt` (other "SparkCore" entities exist: Spark Networks SE, gaming engine, Spark Energy).

---

## 7. SXO — 67 / 100

Source: `sxo.md`.

**Persona scoring (1-5):**

| Persona | Homepage | Pillar | blog: regulated-crypto-fund-manager | blog: crypto-fund-fees-2026 |
|---|---|---|---|---|
| Allocator (institutional CIO) | 4 | 3 | 3 | 4 |
| Founder (wants to launch fund) | 2 | 5 | 4 | 3 |
| Compliance (DD lawyer) | 3 | 4 | 4 | 2 |
| Skeptic (first-time visitor) | 3 | 3 | 3 | 2 |

**3 page-type mismatches found from SERP backwards analysis:**

1. **`/blog/estonia-luxembourg-malta-crypto-fund`** — narrative prose where Google rewards comparison tables (HIGH). 193 impressions, p8.1, 0.5% CTR. Single highest-leverage page edit on site.
2. **`/blog/regulated-crypto-fund-manager-estonia`** — competing law-firm guides at p4-7 use structured comparison callouts (sub-threshold vs full AIFM); SparkCore's narrative format is missing these depth markers (HIGH).
3. **All regulatory blog articles** — SparkCore owns p1-4 for "crypto AIFM estonia." Founder traffic arrives, finds no AIFM structuring CTA, exits (HIGH).

**Skeptic persona above-the-fold fail:** "Supervised by Finantsinspektsioon" is below fold on mobile — first-second trust verification gap.

---

## 8. Backlinks — 32 / 100 (planning baseline)

Source: `backlinks.md`.

**Tier 2 access available but no actionable data this pass:**
- Bing WMT API returned 404 (likely trailing-slash mismatch in `bing_verified_sites` config).
- Common Crawl 0 records — last CC batch predates site launch.
- DataForSEO not enabled.

**Known authority anchors (verified live):**
- `https://search.gleif.org/#/record/8945003BBN0RVNNB0S84` (LEI registry — HTTP 200 confirmed)
- `https://www.fi.ee/.../sparkcoreinvestment-ou` (Estonian regulator)
- `https://mtr.ttja.ee/...` (EFIU Financial Institution licence registry)
- LinkedIn company page
- YouTube `@cointips` (founder)

For a 1-month-old YMYL fund those are exceptionally strong starting credentials — they just haven't been amplified by outreach. Re-score at 2026-08-08 once CC indexes domain and Bing API config is fixed.

---

## 9. Google API Snapshot

Source: `google-api.md`.

**GSC 28-day:** 11 clicks · 368 query impressions · 3.15% CTR · all clicks brand-navigational ("sparkcore", "spark core", "alexandre vinal").

**Highest-impression non-brand:** `/blog/estonia-luxembourg-malta-crypto-fund` — 193 impressions @ p8.1, 1 click. Same page flagged by SXO as #1 SERP-format mismatch.

**Brand confusion:** "sparkcoretech com" — 125 impressions @ p7.7. SparkCore.fund appears for an unrelated brand query but converts no clicks. Worth monitoring (no immediate action).

**Sitemap GSC:** 28 URLs submitted, **0 indexed** in GSC sitemap counter — almost certainly a `sc-domain:` reporting lag. URL Inspection on 5 key pages all confirm individual indexation. Recheck checkpoint 2026-05-19.

**GA4 28-day:** 2 organic sessions / 2 users — Consent Mode v2 modeling thin at this volume; matches GSC 11 clicks within expected attribution gap.

**CrUX:** `noCruxData` — insufficient Chrome traffic. Continue monthly checks.

**PageSpeed script:** still hits known `KeyError: audit_details` bug — defer to manual PSI run if needed.

---

## Findings Tally

| Severity | Count |
|---|---|
| Critical | 3 |
| High | 11 |
| Medium | 11 |
| Low | 7 |

See `ACTION-PLAN.md` for the prioritized punch list with effort estimates.

## Specialist Reports (full detail)

- `technical-seo.md` (84/100)
- `content-eeat.md` (69/100)
- `schema.md` (52/100)
- `sitemap.md` (92/100)
- `performance.md` (62/100)
- `geo-ai.md` (72/100)
- `sxo.md` (67/100)
- `backlinks.md` (32/100, planning baseline)
- `google-api.md` (Tier 2 data)

---

## Trend vs Prior Audit

The previous baseline noted in `CLAUDE.md` was **67/100** (`sparkcore-fund-seo-audit/ACTION-PLAN.md` legacy). This audit reports **71/100** — a +4 point uplift, consistent with the post-2026-04 work: full robots.txt AI crawler block, Cloudflare migration, security headers via Transform Rule, IndexNow + Bing WMT verification, custom GA4 events, gated pages defense-in-depth, dual-cluster EN/FR strategy.

**The next 10-12 points are concentrated in three buckets:**

1. **Schema cleanup** (+8-10 pts to Schema sub-score, +1 pt overall): `@id` everywhere, author `sameAs`/`jobTitle`, pillar Article retype, WebSite SearchAction, Speakable.
2. **Content freshness** (+10-15 pts to Content/GEO sub-scores, +3 pts overall): visible "Last reviewed" + author bio boxes + AIFMD II content updates + `dateModified` cadence.
3. **Performance** (+15-20 pts to Performance sub-score, +1.5 pts overall): defer the redirect script, async-load both render-blocking CSS files, fix Tailwind Brotli, hero `imagesrcset`.

A targeted 8-12 hour sprint addressing only those three buckets would lift the overall score to ~78-80/100 (B+).
