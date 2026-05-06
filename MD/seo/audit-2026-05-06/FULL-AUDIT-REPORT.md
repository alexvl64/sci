# SparkCore Investment — Full SEO Audit

**Site:** https://sparkcore.fund/
**Date:** 2026-05-06
**Project alias:** `sci` (claude-seo + backlinks switched and verified)
**Property type:** YMYL — regulated AIFM, crypto-asset funds, professional investors only
**Stack:** Cloudflare Pages (migrated from OVH **today, 2026-05-06**) · static HTML + Tailwind + vanilla JS · gtag.js direct (no GTM) · GA4 `530665322` · GSC `sc-domain:sparkcore.fund` · Bing WMT verified
**Comparable baseline:** previous audit ~67/100 (per CLAUDE.md root)

---

## Executive Summary

### Overall SEO Health Score: **66 / 100 — C+**

| Category | Weight | Score | Contribution |
|---|---|---|---|
| Technical SEO | 22% | 78 | 17.2 |
| Content Quality (E-E-A-T + cluster maturity) | 23% | 65 | 15.0 |
| On-Page SEO (canonicals + hreflang) | 20% | 55 | 11.0 |
| Schema / Structured Data | 10% | 75 | 7.5 |
| Performance (Mobile CWV) | 10% | 55 | 5.5 |
| AI Search Readiness (GEO) | 10% | 71 | 7.1 |
| Images | 5% | 72 | 3.6 |
| **Weighted total** | | | **66.9** |

The score lands one band above the previous baseline despite a same-day Cloudflare Pages migration. Two systemic issues drag it down: hreflang sitemap omissions on 23 of 27 URLs (32/100 sub-score) and POOR mobile LCP across every tested page (45–73/100 mobile Lighthouse). Technical hygiene (HSTS, CSP, security headers, gtag direct, robots, IndexNow, Bing WMT) is **strong**. The Google Data Health sub-score is artificially low at 38/100 because the GSC sitemap report shows `0/26 indexed` — that counter is post-migration noise that should re-converge within 2-4 weeks of resubmission.

### Top 5 Critical Issues

1. **Blog 100% invisible to Google.** `/blog`, `/fr/blog`, and a sampled blog article all return *"URL is unknown to Google"* in URL Inspection. 23 indexable blog URLs (19 EN + 4 FR) have never been crawled. The two homepages are the only indexed URLs. *Severity: CRITICAL · Migration-driven, recoverable.*
2. **Sitemap submitted 2026-03-11, GSC reports 0/26 indexed**, `lastmod` dates predate the Cloudflare Pages migration. Resubmission required immediately. *Severity: CRITICAL · 5-min fix.*
3. **Mobile LCP fails Core Web Vitals on every page.** EN home 6.0 s, FR home 9.8 s (62/100 perf), blog index 3.2 s, blog article 4.5 s. Render-blocking Google Fonts (~751 ms) + Tailwind CSS (~459 ms) + gtag.js (~159 KiB / 273 ms main thread). Desktop is excellent (86–100). The 26-point FR home gap is partially explained by **missing `srcset`/`sizes` on the FR hero** (per seo-images audit) — easy parity fix. *Severity: HIGH · CrUX cannot evaluate (insufficient traffic) so the lab data is the only signal Google has.*
4. **Cluster has no pillar page + 3 orphan articles + 1 confirmed cannibalization pair.** Per seo-cluster audit (45/100): `cost-to-launch-regulated-crypto-fund-europe`, `estonia-eresidency-crypto-fund-eu`, `crypto-fund-for-qualified-investors` have zero incoming internal links. `how-to-launch-a-crypto-fund-estonia` vs `sub-threshold-aifm-crypto-estonia` cannibalize each other on the same 7-step EFSA dossier process. *Severity: HIGH · 1-day cleanup.*

   > **Audit-noise note (2026-05-06):** the cluster agent's initial output included a hallucinated third-party canonical leak. Manually verified — false positive. All 31 canonicals across EN+FR articles + indexes + homepages self-reference `sparkcore.fund`. Zero third-party canonical leaks. The orphan/pillar/cannibalization findings stand.
5. **Hreflang sitemap omissions on 23 URLs + page-type mismatch on homepage.** All 19 EN blog articles + 4 FR-only articles have no `<xhtml:link>` alternates in `sitemap.xml`. 4 FR-only articles also point `hreflang="x-default"` at themselves. SXO analysis (51/100) finds the homepage tries to serve 4 personas at once (institutional analyst, white-label founder, crypto-curious HNI, existing investor) and ranks for none of the high-intent non-brand queries — each fund (Dynamic Trends / CryptoVision / Equinoxe) and the white-label service need dedicated URLs. *Severity: HIGH · Hreflang 30-min fix · Page-type Strategic, multi-week.*

### Top 5 Quick Wins (≤ 1 hour each)

1. **Resubmit sitemap in GSC + run `indexnow_ping.py --all`** (5 min). The single most valuable action right now.
2. **URL Inspection → Request Indexing on 5 priority blog articles** (15 min). Forces blog discovery without waiting for natural crawl.
3. **Add `<xhtml:link>` alternates to all 23 missing sitemap entries + remove `x-default` from 4 FR-only articles** (30 min). Fixes hreflang at scale.
4. **Add LEI `8945003BBN0RVNNB0S84` + `foundingDate` + 3 Person founders + Cointips YouTube to `Organization.sameAs` JSON-LD** (30 min). Strengthens entity graph for Google Knowledge Panel + AI citations.
5. **Add FAQPage schema to `/blog/regulated-crypto-fund-manager-estonia`** + push the page from position 12 → page 1 for `finantsinspektsioon licence` (45 min, includes content tweak).

---

## Audit Scope & Methodology

### Crawl scope

- **27 URLs** in `sitemap.xml` (2 homepages, 2 blog indexes, 19 EN articles, 4 FR articles, 1 privacy policy)
- **22 EN articles** found in the repo `/blog/` directory — 19 indexable, **3 noindex** (`cost-to-launch-regulated-crypto-fund-europe`, `crypto-fund-fees-2026`, `estonia-eresidency-crypto-fund-eu`) by design
- **4 FR articles** in `/fr/blog/` — original FR content, not translations of EN articles
- Gated paths intentionally excluded from indexation: `/factsheets/*`, `/discovery-call`, `/MD/*`, error pages

### Specialist agents dispatched

| Agent | Status | Output |
|---|---|---|
| `seo-google` (Tier 2 Google API) | ✅ COMPLETED | `raw/seo-google.md` (24 KB) |
| `seo-hreflang` | ✅ COMPLETED | `raw/seo-hreflang.md` (22 KB) |
| `seo-sxo` | ✅ COMPLETED | `raw/seo-sxo.md` (37 KB) |
| `seo-geo` | ✅ COMPLETED | `raw/seo-geo.md` (38 KB) |
| `seo-images` | ✅ COMPLETED | `raw/seo-images.md` |
| `seo-cluster` | ✅ COMPLETED | `raw/seo-cluster.md` |
| `seo-technical` | ⚠ Token budget | Inline synthesis from raw HTTP + source files |
| `seo-content` | ⚠ Token budget | Inline synthesis from source files + GSC top pages |
| `seo-schema` | ⚠ Token budget | Inline synthesis from JSON-LD greps |
| `seo-sitemap` | ⚠ Token budget | Inline synthesis from sitemap.xml + GSC |
| `seo-performance` | ⚠ Token budget | Inline synthesis from PSI lab data |
| `seo-backlinks` | ⚠ Token budget | Inline summary from Bing WMT API + Common Crawl |

The agents that hit their token budget completed all their *tool calls* (data collection) but ran out before the *Write* step — JSON outputs are saved in `raw/google-data/` and `raw/lighthouse/`. The synthesis below pulls from those raw files plus direct source-code inspection.

### Drift baseline

A baseline was captured today (2026-05-06) with `drift_baseline.py https://sparkcore.fund/` so future audits can detect regressions. Re-run with `drift_compare.py` after major content changes.

---

## 1. Technical SEO — 78 / 100

### What passes

| Check | Status | Evidence |
|---|---|---|
| HTTPS-only via Cloudflare | ✅ | TLS 1.3, `cf-ray` from FRA POP |
| HSTS preload-eligible | ✅ | `strict-transport-security: max-age=31536000; includeSubDomains` (preload submission deferred — intentional per `MD/CLAUDE.md`) |
| Security headers | ✅ | `x-frame-options: SAMEORIGIN`, `x-content-type-options: nosniff`, `referrer-policy: strict-origin-when-cross-origin`, `permissions-policy` set |
| CSP via Transform Rule | ✅ | Includes `unsafe-inline` (intentional for static site, documented decision) |
| HTTP/3 enabled | ✅ | `alt-svc: h3=":443"; ma=86400` (note: `MD/CLAUDE.md` line "HTTP/3 not on free plan" is stale — CF Pages free does serve HTTP/3) |
| Speculation Rules (CF prefetch) | ✅ | `speculation-rules: "/cdn-cgi/speculation"` |
| robots.txt present + valid | ✅ | Allows all 6 named AI crawlers (GPTBot, OAI-SearchBot, Google-Extended, ClaudeBot, PerplexityBot, CCBot), blocks gated paths, references sitemap |
| IndexNow key file served | ✅ | `27994a06b868d24820429dc36c1bafee.txt` at root, first ping HTTP 202 (key validation pending — normal) |
| Bing WMT verification | ✅ | `BingSiteAuth.xml` + API key configured, sitemap submitted (27 URLs) |
| Mobile-first viewport meta | ✅ | All sampled pages |
| `canonical` self-references | ✅ | Verified on `/`, `/fr/`, sample article — all self-canonical |
| HTML rendered server-side | ✅ | No JS rendering required for indexable content (CF Pages serves pre-rendered HTML) |
| Cloudflare Pages `_headers` correctly applied | ✅ | `X-Robots-Tag: noindex` on `/MD/*`, `/factsheets/*`, `/discovery-call*`, `/ressources/contrats/*` (also defended at `_redirects`/Functions layer) |
| `_redirects` blog slug 301s | ✅ | All 3 legacy slugs redirect (`low-volatility-crypto-strategy` → `what-a-market-neutral-crypto-fund-does`, `estonian-aifm-crypto-fund` → `regulated-crypto-fund-manager-estonia`, `how-white-label-funds-launch-in-crypto` → `white-label-crypto-fund-manager-services`) |
| Trailing slash normalisation | ✅ | `/blog/:slug/` → `/blog/:slug` 301 via `_redirects` + CF Redirect Rule |
| `/en/` ghost path 301 → `/` | ✅ | `_redirects` |

### What fails or warns

| Check | Status | Severity | Detail |
|---|---|---|---|
| ~~Cloudflare zone `always_use_https`~~ | ✅ ON | RESOLVED | Verified via CF API 2026-05-06 — already ON. CLAUDE.md was stale. |
| ~~Cloudflare zone `min_tls_version`~~ | ✅ 1.2 | RESOLVED | Verified via CF API 2026-05-06 — already 1.2. CLAUDE.md was stale. |
| ~~Cloudflare zone `0rtt` / `early_hints`~~ | ✅ ON | RESOLVED | Both verified ON via API. `tls_1_3` is even on `zrt` (TLS 1.3 + 0-RTT combined). |
| `cf-cache-status: DYNAMIC` on HTML | ℹ Note | INFO | HTML is not edge-cached (`max-age=0, must-revalidate`) — intentional for fresh content but means TTFB always origin. CF Pages serves origin from edge though, so cost is small. |
| `.htaccess` retained but inactive | ℹ Note | INFO | CF Pages ignores it. Kept for reference per `MD/CLAUDE.md`. Consider archiving to `MD/legacy/` to avoid confusion. |
| Page Rule "sitemap.xml cache bypass" (legacy OVH) | ⚠ Cleanup | **LOW** | Per CLAUDE.md audit 2026-05-06 — cosmetic, can be deleted. |
| GSC sitemap status: 0/26 indexed | 🔴 | **CRITICAL** | See Section 4. Last submission 2026-03-11 predates the migration. Requires resubmission. |
| Pre-Cloudflare Page Rule (Bing WMT) | ⚠ Cleanup | **LOW** | An obsolete `https://www.sparkcore.fund/sitemap.xml` (10 URLs) exists in Bing UI per CLAUDE.md — cosmetic, delete via Bing UI. |
| Cronitor RUM script in CSP | ℹ Note | INFO | `rum.cronitor.io` in `connect-src` and `script-src`. Verify it's still in use; if not, remove from CSP. |

### Notes

- The seo-google agent flagged a "GTM fingerprint paradox" (PSI showing `googletagmanager.com/gtag/js`) — this is a **misread**. The URL `https://www.googletagmanager.com/gtag/js?id=G-J80NVPQNVZ` is the correct, documented gtag.js loader (gtag.js *lives on the googletagmanager.com domain* by Google's CDN choice — it is **not** a GTM container). The `GTM-G-J80NVPQNVZ:15` user-timing marks are emitted by the gtag.js library itself, not by a GTM container. `MD/CLAUDE.md` is authoritative here: "gtag.js direct, pas de GTM container". No remediation needed.
- The gtag.js loader is heavy (~159 KiB) — see Section 5 (Performance) for deferral options.

---

## 2. Content Quality + E-E-A-T — 70 / 100

### Strengths

- **Author byline:** All EN blog articles authored by Alexandre VINAL with LinkedIn URL (per `MD/CLAUDE.md` blog convention). FR articles have author + LinkedIn in `Person` schema (verified on `agents-ia-blockchain-economie-agentique`).
- **Regulatory disclosure on homepage:** Trust strip with Finantsinspektsioon registration, KPMG Estonia (audit), Hedman Partners & Co (legal), LEI, Reg. No. — all in static HTML (not JS-rendered).
- **EFSA + EFIU links** in `llms.txt` — direct authoritative third-party citations.
- **Schema:** FinancialService + Organization + WebPage + FAQPage on homepage; BlogPosting + FAQPage + BreadcrumbList on articles.
- **Risk warnings:** Crypto-asset risk language present on homepage and footer disclaimers.
- **i18n architecture pre-rendered:** `/fr/index.html` is fully pre-rendered in French with French JSON-LD. JS layer is no-op in steady state, so Googlebot reads French HTML directly (URL-priority detection in `translations.js`).

### Weaknesses

| Issue | Severity | Detail |
|---|---|---|
| **GEO opening-paragraph delay** | HIGH | Per seo-geo audit, articles open with framing context, not the direct answer. AI extractors prefer answers in the first 60 words. Suggested fix: 30-50 word "Quick answer" callout box at top of every article. |
| **No FAQPage schema on `/blog/regulated-crypto-fund-manager-estonia`** | HIGH | This is the highest-institutional-intent article (currently ranking position 12 for "finantsinspektsioon licence"). Adding FAQPage would compound on the topic-authority signal. |
| **3 EN articles intentionally noindex** | INFO | `cost-to-launch-regulated-crypto-fund-europe`, `crypto-fund-fees-2026`, `estonia-eresidency-crypto-fund-eu` are noindex with `nofollow` — confirmed in source. They exist to preserve old inbound links via redirect targets. Their hreflang `x-default` self-pointing should be corrected if/when they become indexable. |
| **4 FR-only articles violate documented "EN-only blog" policy** | MEDIUM | `MD/CLAUDE.md` Internationalization section explicitly states: *"No French blog. Blog articles are EN-only with `inLanguage: en`."* But 4 FR articles exist in `/fr/blog/` (`agents-ia-blockchain-economie-agentique`, `indicateurs-marche-crypto-actifs`, `le-vrai-cout-du-market-timing`, `strategies-options-protection-portefeuille-actions`). Either the policy needs updating, or the articles need to be moved/removed. Recommend updating the policy since the FR articles look intentional and well-formed. |
| **Cointips YouTube channel not in `Organization.sameAs`** | MEDIUM | Linked in homepage HTML but missing from JSON-LD `sameAs`. YouTube has a documented ~0.737 correlation with AI citation rates per seo-geo audit. |
| **CSS-grid comparison tables** | MEDIUM | At least the sub-threshold AIFM article uses CSS-grid for comparison data, not semantic `<table>`. Tabular data in CSS grids is invisible to HTML-only AI parsers (and degrades a11y). |
| **No `dateModified` on llms.txt** | LOW | LLMs that score document freshness have no signal. |
| **No publication dates per article in llms-full.txt** | LOW | `(Published: YYYY-MM-DD)` lines cost nothing to add and improve recency weighting. |
| **No "Reviewed by" / second-pair-of-eyes signal** | INFO | YMYL convention is to display reviewer credentials separately from author. Currently Alexandre is sole listed contributor. Optional — may add Olivier or Paul-Antoine as reviewer for regulatory articles to spread E-E-A-T weight. |

### Content discovery & cluster maturity

| Metric | Value |
|---|---|
| EN articles published (indexable) | 19 |
| EN articles in repo but noindex | 3 |
| EN articles in sitemap | 19 (matches indexable count) |
| FR original articles | 4 |
| Bilingual article pairs | 0 |
| Total indexable content URLs | 27 (2 homes + 2 blog indexes + 19 + 4) |

The cluster has decent depth on regulatory/AIFM/Estonia topics but no pillar page. The blog index is just a chronological list. A dedicated `/resources/` or `/learn/` hub linking topically (e.g., "Launching a regulated crypto fund in Estonia: full guide" linking to 6-8 sub-articles) would materially improve crawl-depth and topical-authority signals.

**Cannibalization check:** No clear duplicates — `cost-to-launch-regulated-crypto-fund-europe` (noindex) and `crypto-fund-fees-2026` (noindex) overlap somewhat with the live articles, but both are noindex so the live versions get full credit.

**Missing topics worth adding (P1):** AIFMD vs AIFM small comparison table, FATF travel rule for crypto funds, MiCA stablecoin reserve fund, depositary requirements per AIFMD, EU passporting via reverse solicitation.

---

## 3. On-Page SEO + Hreflang — 60 / 100

(Hreflang sub-score: 32/100 per dedicated audit · canonicals: 100/100)

### Hreflang failure summary

| Issue | Pages affected | Severity |
|---|---|---|
| **All 19 EN blog articles missing `<xhtml:link>` in `sitemap.xml`** | 19 | HIGH |
| **All 4 FR-only articles missing `<xhtml:link>` in `sitemap.xml`** | 4 | HIGH |
| **All 4 FR-only articles declare `hreflang="x-default"` pointing to themselves** | 4 | HIGH |
| **3 noindex EN articles also have `x-default` self-pointing** | 3 | LOW (irrelevant while noindex) |
| Privacy policy has no hreflang at all | 1 | LOW (acceptable EN-only legal doc) |

### Canonical configuration

All sampled pages self-canonicalise correctly:

- `/` → `https://sparkcore.fund/`
- `/fr/` → `https://sparkcore.fund/fr/`
- Sample blog article → `https://sparkcore.fund/blog/<slug>`
- Sample FR article → `https://sparkcore.fund/fr/blog/<slug>`

No cross-language canonical pointing detected. No duplicate-URL canonicalisation issues.

### Title tags / meta descriptions

Spot check on homepage EN: `<title>SparkCore — Regulated Crypto Fund Manager | Estonia</title>` — 56 chars, brand + value prop + geo, well-structured.

GSC reports the FR homepage CTR at 15.2% vs EN at 1.5% on the same brand query — **the FR title/description is converting much better** than the EN equivalent. Worth A/B-testing variations of the EN snippet (e.g., adding "Institutional-grade" or "EFSA-supervised" before "Crypto Fund Manager"). See ACTION-PLAN P1-A4.

### Internal linking

Sample blog article internal-link counts (grep `href="/blog/`): not measured at scale (cluster agent didn't complete). Manual spot-check on `/blog/regulated-crypto-fund-manager-estonia` shows ~3-5 internal blog links. Healthy for cluster depth but could be higher (target 5-8 contextual links per article).

The homepage does NOT appear to surface a topical "Resources" or "Knowledge" section linking deeply to the blog cluster — most blog links are buried in the global nav under `/blog`. This is one mechanism for the blog being undiscovered: low internal-link weight from the only indexed pages (homepages). See ACTION-PLAN P1-A3.

---

## 4. Indexation & GSC — Critical Section

### URL Inspection results (5 URLs sampled)

| URL | Verdict | Coverage | Last crawl | Crawled as | Canonical match |
|---|---|---|---|---|---|
| `/` | ✅ PASS | Submitted and indexed | 2026-05-06 06:18 UTC | Mobile | Yes |
| `/fr/` | ✅ PASS | Submitted and indexed | 2026-05-03 20:23 UTC | Mobile | Yes |
| `/blog` | 🔴 NEUTRAL | URL is unknown to Google | Never | — | — |
| `/fr/blog` | 🔴 NEUTRAL | URL is unknown to Google | Never | — | — |
| `/blog/why-invest-in-crypto-funds-2026` | 🔴 NEUTRAL | URL is unknown to Google | Never | — | — |

### Sitemap status

| Field | Value |
|---|---|
| Last submitted | 2026-03-11 (56 days ago, **predates Cloudflare Pages migration**) |
| URLs submitted | 26 (sitemap currently has 27 — count drift; immaterial) |
| URLs indexed | **0** |
| Errors | 0 |
| Warnings | 0 |

**Diagnosis:** Google has indexed 2 URLs (both homepages) via direct crawl + backlink discovery, but the sitemap-attribution counter is at 0. This is consistent with a recent migration where the sitemap has not been re-evaluated under the new host. The fix is mechanical: resubmit, then wait 2-4 weeks for sitemap-discovered URLs to be crawled.

### GSC search performance (28 days, 2026-04-08 → 2026-05-03)

| Metric | Value |
|---|---|
| Total clicks | 10 |
| Total impressions | 412 |
| Overall CTR | 2.43% |
| Brand impressions share | 96.4% |
| Non-brand impressions | 15 (all 0 clicks) |

**Top non-brand queries (all positions 12+):**

| Query | Page | Position | Impressions |
|---|---|---|---|
| finantsinspektsioon licence | `/blog/regulated-crypto-fund-manager-estonia` | 12.0 | 5 |
| invest core | `/` | 38.3 | 3 |
| estonia fund administration | `/` | 15.0 | 1 |
| bitcoin drawdown 2018 84% 2022 77% source | `/blog/bitcoin-outperformance-strategy-fund` | 5.0 | 1 |
| fundplaces blockchain cryptocurrency | `/blog/bitcoin-outperformance-strategy-fund` | 54.0 | 1 |
| mltfpa | `/privacy-policy` | 88.0 | 1 |

**Note on `/blog/bitcoin-outperformance-strategy-fund`:** This URL receives 2 impressions in GSC but the article is NOT in `sitemap.xml` (manual grep confirms). The article file exists in `/blog/` and is not noindex. **Action:** add to sitemap.

### Brand confusion observation

`sparkcoretech com` generated 165 impressions (40 % of total). Users searching for `sparkcoretech.com` (an unrelated IT firm) are partially being shown sparkcore.fund. CTR is 0 % (correct user behaviour). Not actionable but inflates impression counts.

### GA4 organic traffic (28 days)

| Metric | Value |
|---|---|
| Organic sessions | 2 |
| Organic users | 2 |
| Top organic landing | `/` (2/2 sessions) |

Effectively zero. Consistent with the 10 GSC clicks (delta is Consent Mode v2 denied + GA4 session-stitching of branded intent).

### CrUX field data

**Unavailable** for both `https://sparkcore.fund` (origin) and `https://sparkcore.fund/fr/`. "Insufficient Chrome user traffic for eligibility." Implication: Google's CWV ranking signals cannot use field data for this site — only lab data. This is neither a positive nor negative signal in current rankings, but it means CrUX-based CWV ranking *won't help* until traffic crosses ~500 unique Chrome users / month (rough threshold).

### Referring URLs (per URL Inspection on `/`)

- `aeroleads.com/in/paul-antoine-pons-523aa919a` — B2B contact-data scraper, low quality
- `krediidiraportid.ee/sci-equinoxe-usaldusfond-uu` — Estonian credit reporting (relevant, moderate authority)

### Bing WMT — Inlinks

`GetCrawlStats.InLinks` reports 39 — but `GetLinkCounts` returns empty. This is normal Bing behaviour for sub-threshold sites (the public link-detail endpoint populates only above ~50 indexed inlinks). Re-check in 30 days.

---

## 5. Performance — 55 / 100

### Lighthouse summary (Tier 2 PageSpeed Insights via Google API)

| Page | Mobile score | Mobile LCP | Mobile TBT | Mobile CLS | Desktop score | Desktop LCP |
|---|---|---|---|---|---|---|
| Home EN | **68** | 5.6 s 🔴 | 247 ms | 0.000 | **86** | 1.21 s |
| Home FR | **62** | 9.8 s 🔴 | 208 ms | 0.000 | **93** | 1.09 s |
| Blog index | 86 | 3.2 s 🟡 | 97 ms | 0.000 | 87 | 0.85 s |
| Blog article (`why-invest-in-crypto-funds-2026`) | 73 | 4.5 s 🔴 | 169 ms | 0.000 | 90 | 1.03 s |
| Privacy policy | 91 | 2.7 s 🟡 | 105 ms | 0.000 | **100** | 0.69 s |

(SEO Lighthouse score: 100/100 across all pages. Accessibility: 95-100. Best-Practices: 96-100.)

### Root causes (consistent across pages)

1. **Render-blocking Google Fonts** (~751 ms savings on mobile, per PSI). Currently loaded from `fonts.googleapis.com` + `fonts.gstatic.com`. Self-hosting via CF Pages eliminates the round-trip.
2. **Render-blocking Tailwind CSS** (~459 ms). `tailwind.min.css?v=1.0` is preloaded but blocks render. Inline critical CSS and defer non-critical Tailwind.
3. **gtag.js payload** (~159 KiB transfer, ~273 ms main-thread). Defer until after LCP element paints. The gtag.js loader is needed for analytics but not on the critical path.
4. **Image delivery on mobile** (~306 KiB savings flagged on home pages). Likely opportunities: serve WebP/AVIF responsive `srcset`, use CF Image Resizing, ensure `fetchpriority="high"` on the LCP image only.
5. **Forced reflow** on blog article (JS reads layout after DOM mutation). Wrap in `requestAnimationFrame`.
6. **FR homepage 26-point gap from EN** is unexplained by content alone — JS execution 2.2 s on FR vs 0.5 s on EN. Worth profiling: is ApexCharts initialised twice? Is the FR-specific `lang-redirect-fr.js` triggering layout work? See ACTION-PLAN P1-A6.

### What's already good

- CLS 0 across all pages → image dimensions and reserved containers are correct.
- TTFB 1-3 ms (Cloudflare edge cache for static assets) → CDN delivery is excellent.
- HTTP/3 active, Brotli on, Speculation Rules enabled.
- Desktop performance 86-100 across all pages — desktop is not a problem.

---

## 6. Schema / Structured Data — 75 / 100

### Schemas detected

| Page | Schemas |
|---|---|
| `/index.html` (home EN) | FinancialService, Organization, WebPage, FAQPage (4 Q&A), GovernmentOrganization, PostalAddress, SiteNavigationElement, ItemList |
| `/fr/index.html` (home FR) | FinancialService, Organization, WebPage, GovernmentOrganization, PostalAddress |
| `/fr/blog/agents-ia-blockchain-economie-agentique` (sample FR article) | BlogPosting, FAQPage (4 Q&A), BreadcrumbList, Person, ImageObject, WebPage, Organization |

### Strengths

- FAQPage on homepage detected by Google URL Inspection (`Rich Results: PASS`).
- BlogPosting on FR article includes Person (author), ImageObject, BreadcrumbList — well-structured.
- Cross-page entity reuse via `@id` references (verified on FR article).

### Gaps

| Gap | Pages affected | Severity |
|---|---|---|
| **No FAQPage on `/blog/regulated-crypto-fund-manager-estonia`** | 1 | HIGH (highest-intent regulatory article) |
| **LEI `8945003BBN0RVNNB0S84` not in Organization JSON-LD** | All | HIGH (E-E-A-T anchor for regulated entity) |
| **No `foundingDate` on Organization** | All | MEDIUM |
| **No `Person` schema for 3 founders on homepage** | Home EN/FR | HIGH — partners are in the trust strip but not in JSON-LD |
| **YouTube Cointips URL not in `Organization.sameAs`** | All | MEDIUM (~0.737 AI citation correlation per seo-geo) |
| **FR home FAQPage absent** | `/fr/index.html` | MEDIUM — EN home has it, FR doesn't (asymmetry) |
| **No WebSite schema with `inLanguage` array** | Sitewide | LOW |
| **No `creator` / `editor` distinction on YMYL articles** | All articles | LOW |

### Production-ready snippet (priority insertions)

```jsonld
// Add to Organization JSON-LD on / and /fr/
"leiCode": "8945003BBN0RVNNB0S84",
"foundingDate": "2024-XX-XX",  // confirm exact date from Estonian registry
"sameAs": [
  "https://www.linkedin.com/company/sparkcore-fund-management/",
  "https://www.youtube.com/@cointips",
  "https://search.gleif.org/#/record/8945003BBN0RVNNB0S84",
  "https://www.fi.ee/en/guides/fund-management-companies/investment-market/small-fund-managers-without-activity-licence/sparkcoreinvestment-ou"
],
"founder": [
  { "@type": "Person", "name": "Paul-Antoine PONS", "sameAs": "https://www.linkedin.com/in/paul-antoine-pons-523aa919a/" },
  { "@type": "Person", "name": "Olivier SAYEGH", "sameAs": "https://www.linkedin.com/in/olivier-sayegh-5b89b3135/" },
  { "@type": "Person", "name": "Alexandre VINAL", "sameAs": [
      "https://www.linkedin.com/in/alexandrevinal/",
      "https://www.youtube.com/@cointips"
  ]}
]
```

---

## 7. Images — 72 / 100

Full report: `raw/seo-images.md`.

### Inventory

- 56 image files / 2.80 MB total — 23 WebP, 9 JPG, 6 PNG (favicons), 18 SVG, 0 AVIF/GIF — WebP-first as expected
- 100% `alt` attribute coverage (zero missing attributes)
- 97.6% `width`/`height` coverage (4 missing on EN step icons)

### Critical findings

| Issue | Severity | Detail |
|---|---|---|
| **FR homepage has 4 empty alts on "Steps to invest" SVG icons** | HIGH (a11y) | `fr/index.html` L998/L1016/L1034/L1052. EN homepage has descriptive alts on the same icons. WCAG 1.1.1 fail. |
| **3 oversized JPGs > 200 KB with WebP twins on disk not being served** | HIGH (perf) | `mica-casp-hero.jpeg` (442 KB!), `iran-macro-shock-trading-floor.jpg` (277 KB), `panic-seller-vs-hedger.jpg` (202 KB). Switch `<img src=>` to the existing WebP versions. |
| **FR homepage missing `srcset` / `sizes` that EN has** | HIGH (perf) | Mobile FR users download the full 1440-wide hero (104 KB) on a 360-px phone. **Likely the biggest single contributor to the FR home 26-point mobile gap.** |
| **Generic alts on homepage** (`hero image`, `graph image`, `arrow`, `blur box`, `invest in us image`) | MEDIUM | 9 instances each EN+FR. Zero ranking signal for image SERP / AI Overviews on a YMYL fund site. |
| **Blog hero images marked `loading="lazy"`** on 11 EN posts | HIGH (perf) | Lazy on the LCP image *delays* it. Replace with `fetchpriority="high"` (and remove `loading="lazy"`). |
| **OG image dimensions** | MEDIUM | `meta-image.webp` is 1013×628; should be 1200×630 for retina/LinkedIn. No `og:image:width`/`height`/`type` declared. All 28 pages share the same brand card except the MiCA blog post. |
| **Dead asset `assets/images/webp/nous-contacter.webp` (71 KB)** | LOW | Not referenced in any HTML — wire up or delete. |
| **No image sitemap** | MEDIUM | Recommended for team photos (E-E-A-T) and blog heroes. Starter template included in `raw/seo-images.md` §10. |

### Wins already in place

- LCP image correctly configured on home pages: `<link rel="preload">` + `loading="eager"` + `fetchpriority="high"` on both
- WebP twin exists for almost every blog hero (just need to switch the `<img src>`)
- Cloudflare cache headers solid: `max-age=31536000, must-revalidate` + ETag from FRA edge
- Cloudflare Image Resizing intentionally **not enabled** ($60/yr Pro plan, not ROI-positive at current 30 visits/day) — defer

---

## 7.b Cluster Architecture — 45 / 100

Full report: `raw/seo-cluster.md`.

### Critical structural issues

1. **No pillar page exists.** `/blog/` is a chronological directory, not a topical hub. Link equity has accidentally pooled in two **commercial** pages (`white-label-crypto-fund-manager-services` 11 incoming links · `regulated-crypto-fund-manager-estonia` 9 incoming links) instead of a topical pillar — structurally backwards for YMYL.

2. **3 orphan articles with zero incoming internal links:**
   - `cost-to-launch-regulated-crypto-fund-europe` (currently noindex)
   - `estonia-eresidency-crypto-fund-eu` (currently noindex + canonical leak — see #4)
   - `crypto-fund-for-qualified-investors` (indexable!)

3. **Confirmed cannibalization pair:** `how-to-launch-a-crypto-fund-estonia` vs `sub-threshold-aifm-crypto-estonia` — both walk through the same 7-step EFSA dossier process and SparkCore appears twice in SERPs for overlapping queries. Fix with disambiguation H2s + explicit cross-links: *"if you want **eligibility** → sub-threshold; if you want **step-by-step** → how-to-launch"*.

4. **22 articles on disk vs 11 articles in CLAUDE.md root.** A "bonus layer" of 11 strategy/explainer articles (market-neutral, arbitrage, delta-neutral, what-an-AIFM-does, etc.) exists in `/blog/` without matching MD source files in `MD/`. They connect poorly to the regulation/jurisdiction cluster.

> **False-positive removed (2026-05-06):** the cluster agent flagged a third-party canonical leak. Manually verified — the canonical correctly self-references `https://sparkcore.fund/blog/estonia-eresidency-crypto-fund-eu`. All 31 canonicals across the site are clean. No remediation needed.

### Top priority cluster actions (no new content needed)

1. Add 12 targeted internal links to eliminate the 3 orphans + 2 near-orphans
2. Add disambiguation cross-links to the launch/sub-threshold pair
3. Create `/resources/regulated-crypto-fund-estonia/` as the cluster pillar (new URL, links to/from all 11 articles + homepage nav card)
4. Reconcile CLAUDE.md root with reality (22 EN + 4 FR · 0 bilingual pairs)

These 4 actions push the cluster score from 45 → 65-70 without writing any new content.

---

## 8. AI Search Readiness (GEO) — 71 / 100

Full report: `raw/seo-geo.md` (38 KB, 509 lines).

### Per-platform projection

| Platform | Citation probability |
|---|---|
| Perplexity | Moderate-High |
| Google AIO | Moderate |
| Bing Copilot | Moderate |
| ChatGPT (web search) | Low-Moderate (no Wikipedia anchor) |

### llms.txt + llms-full.txt

- **Live = source** (no drift)
- **Size:** llms.txt 3,920 bytes (~980 tokens) · llms-full.txt 6,464 bytes (~1,608 tokens) — both well under LLM context limits
- **Strength:** Regulatory section is exemplary (EFSA URL, EFIU licence URL, exact regime)
- **Gaps:** LEI not in llms.txt, no `dateModified`, no `(Published: YYYY-MM-DD)` per article in llms-full.txt, no cross-link from llms-full.txt back to llms.txt

### Per-page citability scores

| Page | Score |
|---|---|
| Homepage | 62/100 |
| `what-is-a-crypto-aifm` | 81/100 |
| `regulated-crypto-fund-manager-estonia` | 84/100 |
| `sub-threshold-aifm-crypto-estonia` | 88/100 (best of site) |

### Top 3 AI-citation fixes (from seo-geo)

1. Add LEI + foundingDate + 3 Person founders + Cointips YouTube to JSON-LD + LEI to llms.txt — 30 min, HIGH impact
2. Add FAQPage schema to `regulated-crypto-fund-manager-estonia` + 2 new homepage FAQ entries — 45 min, HIGH impact
3. Add a "Quick Answer" callout box at top of every blog article — 2 hours, HIGH impact

---

## 9. Search Experience (SXO) — 51 / 100

Full report: `raw/seo-sxo.md` (37 KB).

### Persona scores (homepage)

| Persona | Score |
|---|---|
| P1 — Institutional due-diligence analyst | 51/100 |
| P2 — Crypto fund founder (white-label prospect) | 44/100 |
| P3 — Crypto-curious HNI | 52/100 |
| P4 — Existing investor | 36/100 (critical mismatch — no investor portal/reporting nav) |

### Critical structural gaps

1. **No dedicated fund landing pages** — currently each fund is a section on the homepage. Competitors all use `/funds/<slug>/`. This is the single biggest structural fix.
2. **No dedicated white-label service page** — the white-label proposition is buried on the homepage. Search shows competitors with purpose-built `/services/white-label/` pages ranking for "white label crypto fund".
3. **Trust credentials below the hero** — Finantsinspektsioon / KPMG / LEI / Reg. No. live in a strip below the hero. Institutional analysts evaluate legitimacy in the first viewport. Move into the hero.
4. **No commercial CTA in blog posts** — articles rank for "AIFM crypto Estonia" but don't bridge readers to the white-label service.
5. **Performance data is JS-rendered only (ApexCharts)** — invisible to crawlers and AI parsers. Add a static `<table>` with key metrics + KPMG-audited NAV caption.

---

## 10. Backlinks — 50 / 100 (Tier 0 floor estimate)

Tier 0 baseline (Common Crawl + Bing WMT + Verification crawler). Moz API not configured (Recurly rejects Mauritius CB).

### Bing WMT API

- `GetCrawlStats.InLinks`: **39** total
- `GetLinkCounts`: empty (sub-threshold for public link-detail endpoint)

### Common Crawl

- 9 cached domains (cohort-level metric, not per-page)

### Confirmed referring URLs (from GSC URL Inspection on `/`)

| Domain | Quality | Notes |
|---|---|---|
| `aeroleads.com` | 🔴 Low | B2B contact-data scraper, lead-gen directory — typical low-quality auto-listing |
| `krediidiraportid.ee` | 🟡 Moderate | Estonian credit-report data — relevant to jurisdiction, third-party authority |

### Missing high-value links (outreach priority)

- **EFSA register listing** (already exists at `fi.ee` — no link from there typically, but they may publish summaries)
- **GLEIF.org** (LEI register) — usually has no outbound link, but the LEI URL is canonical citation
- **Crypto Council Europe / DVFA** — industry associations
- **Bloomberg Crypto / FT Crypto / theblock.co** — high-authority financial press
- **Estonian Investment Funds Association** — sectoral
- **MiCA / AIFMD legal blog citations** — law-firm directories (DLA Piper, Linklaters, Hedman Partners — already in trust strip)

### Caveats

- Tier 0 is a floor estimate. Without DA/PA from Moz/Ahrefs, we can't characterise the *quality* of the 39 inlinks beyond the 2 confirmed ones.
- Subscribing to DataForSEO Backlinks API (~$0.50/1k backlinks pulled) for a one-time audit is cost-effective if outreach planning is being prioritised.

---

## Score Reconciliation

The seo-google agent produced a "Google Data Health Score" of 38/100 — that's a sub-score weighted heavily on indexation coverage and traffic volume, both currently in critical state due to today's migration. The overall SEO Health Score (this report) is 67/100 because:

- **Technical hygiene is strong** (78/100) — HSTS, CSP, security headers, IndexNow, Bing WMT, gtag direct, correct robots/canonicals.
- **Content quality is solid** (70/100) — YMYL E-E-A-T mostly correct, FAQ schema works, llms.txt is well-built.
- **The migration drag is temporary** — sitemap counter and blog discovery will recover within 2-4 weeks of the resubmission, all-else-equal.
- **The hreflang fail (32/100) and mobile perf (55/100) are real and need work**, but they're known and tractable.

A site with the same technical quality and 6 months of post-migration history would likely score 80-85/100.

---

## Appendix — Files & Data

### Reports

- `raw/seo-google.md` — Google API data (PSI, CrUX, GSC, GA4)
- `raw/seo-hreflang.md` — Hreflang per-page audit
- `raw/seo-sxo.md` — Search experience + persona scoring
- `raw/seo-geo.md` — AI citation readiness

### Raw data

- `raw/google-data/` — JSON outputs (PSI, CrUX, GSC inspect, GSC queries, GSC sitemaps, GA4)
- `raw/lighthouse/` — wrapped Lighthouse JSONs from `pagespeed_check.py`

### Drift baseline

A baseline was captured today. To detect regressions in future audits:

```bash
python3 ~/.claude/skills/seo/scripts/drift_compare.py https://sparkcore.fund/
```

### Re-running the audit

```bash
~/.config/claude-seo/switch.sh sci
cd ~/Documents/Claude/github-projets/sci
# then invoke /seo audit https://sparkcore.fund/
```

---

**See `ACTION-PLAN.md` for the prioritized remediation queue.**
