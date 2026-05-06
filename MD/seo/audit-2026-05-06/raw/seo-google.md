# SparkCore Investment — Google API SEO Report
**Date:** 2026-05-06
**Project:** `sci` | GSC property: `sc-domain:sparkcore.fund` | GA4: `530665322`
**Tier:** 2 (Full — PageSpeed + CrUX + GSC + Indexing API + GA4)
**Data source:** Google API (lab data + field data where available)
**Data freshness:** PSI lab = real-time snapshot | GSC = 2-3 day lag (window 2026-04-08→2026-05-03) | GA4 = 1 day lag (window 2026-04-08→2026-05-05)

---

## 1. PageSpeed Insights — Lab Data (Google API)

CrUX field data is unavailable for all URLs: insufficient Chrome user traffic for CrUX eligibility. Lab data only. Thresholds: LCP Good ≤ 2,500 ms / Needs Improvement 2,500–4,000 ms / Poor > 4,000 ms.

### 1a. Homepage EN — `https://sparkcore.fund/`

| Metric | Mobile | Rating | Desktop | Rating |
|--------|--------|--------|---------|--------|
| Performance score | 71/100 | Needs Improvement | 86/100 | Good |
| LCP | 6.0 s | POOR | 1.2 s | GOOD |
| FCP | 3.3 s | Needs Improvement | — |
| TBT | 50 ms | GOOD | — |
| CLS | 0 | GOOD | — |
| Accessibility | 97/100 | | 97/100 | |
| Best Practices | 100/100 | | 96/100 | |
| SEO | 100/100 | | 100/100 | |

**Top issues (mobile):**
- LCP 6.0 s — POOR. Primary culprit: ApexCharts JS (charting library on homepage) combined with render-blocking fonts and Tailwind CSS. Total payload 1,997 KiB.
- Render-blocking requests cost estimated 1,620 ms (Google Fonts CSS + tailwind.min.css).
- Unused JavaScript: 147 KiB savings (ApexCharts + gtag.js unused portions).
- 5 long main-thread tasks detected.
- Image delivery: 306 KiB savings possible (images not in next-gen formats / over-sized).

**Desktop:** Score 86/100. LCP 1.2 s (Good). Best Practices 96 (not 100 — image aspect ratio issue flagged).

---

### 1b. Homepage FR — `https://sparkcore.fund/fr/`

| Metric | Mobile | Rating | Desktop | Rating |
|--------|--------|--------|---------|--------|
| Performance score | 45/100 | POOR | 97/100 | GOOD |
| LCP | 9.6 s | POOR | 1.1 s | GOOD |
| FCP | 4.3 s | POOR | 0.8 s | |
| TBT | 650 ms | POOR | 80 ms | |
| CLS | 0 | GOOD | 0 | GOOD |
| Accessibility | 95/100 | | — | |
| Best Practices | 96/100 | | — | |
| SEO | 100/100 | | — | |

**Top issues (mobile):**
- LCP 9.6 s — critically POOR. Main-thread work 2.2 s. JS execution 1.0 s.
- 5 long tasks detected. Render-blocking: estimated 1,620 ms savings.
- Unused JS: 147 KiB. Image delivery: 306 KiB savings.
- Color contrast failure (accessibility, score 95 not 100).
- Accessibility: missing main landmark, label/name mismatch.
- FR page is measurably worse than EN on mobile (45 vs 71) — possibly due to more complex DOM or larger image assets specific to the FR variant.

**Desktop:** Score 97/100. LCP 1.1 s (Good). Effectively clean.

---

### 1c. Blog Index — `https://sparkcore.fund/blog`

| Metric | Mobile | Rating | Desktop | Rating |
|--------|--------|--------|---------|--------|
| Performance score | 71/100 | Needs Improvement | 99/100 | GOOD |
| LCP | 4.8 s | POOR | 0.8 s | GOOD |
| FCP | 3.0 s | Needs Improvement | 0.8 s | |
| TBT | 240 ms | Needs Improvement | 50 ms | |
| CLS | 0 | GOOD | 0 | GOOD |
| Accessibility | 100/100 | | 100/100 | |
| Best Practices | 100/100 | | 100/100 | |
| SEO | 100/100 | | 100/100 | |

**Notes:**
- URL `https://sparkcore.fund/blog` (without slash) triggers a 308 redirect to `/blog/` adding ~759 ms on mobile, ~207 ms on desktop. Confirmed by network waterfall.
- Render-blocking: Tailwind CSS (459 ms) + Google Fonts CSS (751 ms) = ~1,200 ms combined on mobile.
- Third-party weight: Google Tag Manager 159 KiB (245 ms main-thread), Google Fonts 94 KiB.
- GTM fingerprint visible in PSI: the blog page loads `gtag/js?id=G-J80NVPQNVZ` via GTM container — this contradicts the CLAUDE.md claim of "gtag.js direct, no GTM". Actual loader appears to be GTM wrapping GA4 on at least the blog index. (See Surprising Findings #1.)

---

### 1d. Blog Article — `https://sparkcore.fund/blog/why-invest-in-crypto-funds-2026`

| Metric | Mobile | Rating | Desktop | Rating |
|--------|--------|--------|---------|--------|
| Performance score | 65/100 | Needs Improvement | 97/100 | GOOD |
| LCP | 4.8 s | POOR | 0.8 s | GOOD |
| FCP | 3.3 s | Needs Improvement | — |
| TBT | 420 ms | Needs Improvement | — |
| CLS | 0.046 | GOOD (borderline) | — |
| Accessibility | 100/100 | | 100/100 | |
| Best Practices | 100/100 | | 100/100 | |
| SEO | 100/100 | | 100/100 | |

**Notes:**
- Render-blocking: 2,400 ms estimated savings on mobile.
- CLS 0.046 is within Good threshold but non-zero — first layout shift found (heading element).
- Forced reflow detected (JS querying layout after DOM change).
- Unused JS: 63 KiB savings (gtag.js).
- Desktop near-perfect: 97/100, LCP 0.8 s.

---

### PageSpeed Summary

| Page | Mobile Score | Desktop Score | Mobile LCP | LCP Rating |
|------|-------------|---------------|------------|------------|
| Homepage EN | 71/100 | 86/100 | 6.0 s | POOR |
| Homepage FR | 45/100 | 97/100 | 9.6 s | POOR |
| Blog Index | 71/100 | 99/100 | 4.8 s | POOR |
| Blog Article | 65/100 | 97/100 | 4.8 s | POOR |

**Pattern:** Desktop performance is excellent across all pages (86–99). Mobile is the problem across the board. Root causes are consistent: render-blocking Google Fonts + Tailwind CSS, heavy gtag.js payload (~159 KiB), and image delivery inefficiencies. The FR homepage has an additional severe penalty from what appears to be heavier JS execution (2.2 s main-thread vs ~0.5 s on blog).

---

## 2. CrUX Field Data

**Origin:** `https://sparkcore.fund` — No CrUX data. Insufficient Chrome user traffic.
**URL `https://sparkcore.fund/fr/`** — No CrUX data. Insufficient Chrome user traffic.

No 25-week history is available for any URL or the origin. This is consistent with a site that launched in late 2024 / early 2025 with a niche B2B institutional audience (professional investors, €50K minimum). CrUX eligibility requires sustained Chrome user traffic volume that this site has not yet reached.

**Implication:** Google's ranking signals for CWV cannot currently be informed by field data for this site. Lab data (above) is the only available signal. The site is effectively invisible to CrUX-based ranking adjustments — neither helped nor penalised by field CWV.

---

## 3. GSC Search Analytics — Last 28 Days (2026-04-08 → 2026-05-03)

**Data freshness:** 2-3 day lag. Total data rows returned: 29 (query × page combinations).

### 3a. Aggregate Performance

| Metric | Value |
|--------|-------|
| Total clicks | 10 |
| Total impressions | 412 |
| Overall CTR | 2.43% |
| Avg position | Not reported (weighted avg not available in row data) |

### 3b. Top 20 Queries (by impressions)

| # | Query | Clicks | Impressions | CTR | Avg Position | Brand? |
|---|-------|--------|-------------|-----|-------------|--------|
| 1 | sparkcoretech com | 0 | 165 | 0% | 7.7 | Partial |
| 2 | sparkcore | 2 | 148 | 1.35% | 6.9 | Yes |
| 3 | spark core | 3 | 17 | 17.65% | 10.5 | Yes |
| 4 | spark core | 1 | 16 | 6.25% | 4.4 | Yes |
| 5 | sparkcore | 0 | 6 | 0% | 5.0 | Yes |
| 6 | sparkcore | 0 | 6 | 0% | 2.0 | Yes |
| 7 | sparkcore | 0 | 6 | 0% | 5.5 | Yes |
| 8 | spark core company | 0 | 6 | 0% | 5.3 | Yes |
| 9 | finantsinspektsioon licence | 0 | 5 | 0% | 12.0 | No |
| 10 | alexandre vinal | 1 | 4 | 25.0% | 4.0 | Partial |
| 11 | invest core | 0 | 3 | 0% | 38.3 | No |
| 12 | sparkcoretech com | 0 | 2 | 0% | 7.0 | Partial |
| 13 | spark-core | 0 | 2 | 0% | 15.5 | Yes |
| 14 | alexandre vinal | 0 | 2 | 0% | 4.0 | Partial |
| 15 | sparkcore company | 0 | 1 | 0% | 1.0 | Yes |
| 16 | sparkcore company | 0 | 1 | 0% | 1.0 | Yes |
| 17 | sparkcore company | 0 | 1 | 0% | 1.0 | Yes |
| 18 | safecore ag | 0 | 1 | 0% | 5.0 | No |
| 19 | sharpcore | 0 | 1 | 0% | 5.0 | No |
| 20 | spark funds pro | 0 | 1 | 0% | 7.0 | No |

**Non-brand queries with impressions (growth frontier):**

| Query | Clicks | Impressions | Avg Position | Page |
|-------|--------|-------------|-------------|------|
| finantsinspektsioon licence | 0 | 5 | 12.0 | /blog/regulated-crypto-fund-manager-estonia |
| estonia fund administration | 0 | 1 | 15.0 | / |
| bitcoin drawdown 2018 84% 2022 77% source | 0 | 1 | 5.0 | /blog/bitcoin-outperformance-strategy-fund |
| fundplaces blockchain cryptocurrency | 0 | 1 | 54.0 | /blog/bitcoin-outperformance-strategy-fund |
| mltfpa | 0 | 1 | 88.0 | /privacy-policy |
| invest core | 0 | 3 | 38.3 | / |

### 3c. Brand vs Non-Brand Split

Queries containing "sparkcore" or "spark core" or "alexandre vinal":

| Category | Clicks | Impressions | Share of Impressions |
|----------|--------|-------------|----------------------|
| Brand (sparkcore variants) | 10 | 397 | 96.4% |
| Non-brand | 0 | 15 | 3.6% |

**Interpretation:** The site is almost entirely brand-driven at this stage. 96.4% of impressions come from users already looking for "sparkcore" or variants. Non-brand impressions total 15 in 28 days — effectively zero organic discovery. This is expected for a site this new in a niche YMYL financial sector, but confirms that content SEO has not yet generated any meaningful non-brand signal.

### 3d. Top 20 Pages (by clicks)

| # | Page | Clicks | Impressions | CTR |
|---|------|--------|-------------|-----|
| 1 | https://sparkcore.fund/fr/ | 5 | 33 | 15.2% |
| 2 | https://sparkcore.fund/ | 5 | 329 | 1.5% |
| 3 | https://sparkcore.fund/blog/regulated-crypto-fund-manager-estonia | 0 | 7 | 0% |
| 4 | https://sparkcore.fund/blog/bitcoin-outperformance-strategy-fund | 0 | 2 | 0% |
| 5 | https://sparkcore.fund/blog/ | 0 | 6 | 0% |
| 6 | https://sparkcore.fund/fr/blog/ | 0 | 6 | 0% |
| 7 | https://sparkcore.fund/privacy-policy | 0 | 9 | 0% |
| 8 | https://sparkcore.fund/fr/ (spark core company) | 0 | 1 | 0% |

**Notable:** The FR homepage (`/fr/`) has a dramatically higher CTR (15.2%) vs EN homepage (1.5%) despite fewer impressions. This suggests the FR SERP listing (title/description) is more compelling, or FR searchers have stronger intent when they find it.

The privacy-policy page appears for "mltfpa" (a Mauritius financial compliance acronym) — irrelevant traffic, no concern.

### 3e. Quick-Win Opportunities (GSC flagged)

| Query | Position | Impressions | Action |
|-------|----------|-------------|--------|
| sparkcoretech com | 7.7 | 165 | High impression volume, 0 clicks — CTR collapse. Users are looking for a different company (sparkcoretech.com). Not actionable but worth monitoring for brand confusion. |
| sparkcore | 6.9 | 148 | Position 4-10 zone. Improving to position 1-3 (currently only at 1.3 on `/fr/`) would capture significantly more traffic. |

---

## 4. GSC URL Inspection — Indexation Status

| URL | Verdict | Coverage State | Last Crawled | Crawled As | Canonical Match | Rich Results |
|-----|---------|----------------|--------------|------------|-----------------|--------------|
| https://sparkcore.fund/ | PASS | Submitted and indexed | 2026-05-06 06:18 UTC | Mobile | Yes | FAQ schema detected (PASS) |
| https://sparkcore.fund/fr/ | PASS | Submitted and indexed | 2026-05-03 20:23 UTC | Mobile | Yes | None |
| https://sparkcore.fund/blog | NEUTRAL | URL is unknown to Google | Never | — | — | — |
| https://sparkcore.fund/fr/blog | NEUTRAL | URL is unknown to Google | Never | — | — | — |
| https://sparkcore.fund/blog/why-invest-in-crypto-funds-2026 | NEUTRAL | URL is unknown to Google | Never | — | — | — |

**Key findings:**
- Both homepages (EN + FR) are indexed and pass all Google checks. EN home was crawled as recently as today (2026-05-06), FR on 2026-05-03. Crawl cadence is healthy.
- **The blog index, FR blog index, and the sampled blog article are all unknown to Google.** This is a significant indexation gap for a site with an active content strategy. Possible causes: (1) sitemap lists `/blog/` (with slash) but the redirect from `/blog` → `/blog/` may be confusing the inspector; (2) internal linking to blog may be insufficient; (3) blog content is too new post-migration.
- Referring URLs on EN home: `aeroleads.com` (lead gen directory) and `krediidiraportid.ee` (Estonian credit reporting site) — both are likely auto-generated listings, not editorial links.
- FAQ rich results detected on EN homepage — this is a positive signal that structured data is working.
- Mobile usability verdict is VERDICT_UNSPECIFIED on all URLs — this is a data gap in the API response, not an actual issue (pages pass mobile usability in practice based on PSI scores and crawl behaviour).

---

## 5. GSC Sitemap Status

| Sitemap | Last Submitted | Errors | Warnings | URLs Submitted | URLs Indexed |
|---------|---------------|--------|----------|----------------|-------------|
| https://sparkcore.fund/sitemap.xml | 2026-03-11 | 0 | 0 | 26 | 0 |

**Critical finding:** The sitemap was submitted on 2026-03-11 (nearly 2 months ago) and shows **0 indexed URLs** despite both homepages being indexed and crawled. This is a direct contradiction — Google has indexed the homepages, but the sitemap coverage counter shows 0.

Two likely explanations:
1. The sitemap URL count is at 26 (not 27 as expected from CLAUDE.md) — one URL may have been recently added or the count differs between tools.
2. More critically, the GSC sitemap indexing counter may not yet reconcile pages discovered via other means (direct crawl, backlinks) with sitemap-attributed indexing. This should resolve over time but is worth monitoring.

The 0 indexed count in GSC sitemap report combined with the blog pages being unknown to Google suggests the blog URLs may be in the sitemap but Google has not yet crawled them. The last submission date of March 11 predates the Cloudflare Pages migration (noted as 2026-05-06 in CLAUDE.md) — the sitemap may need to be resubmitted post-migration.

---

## 6. GA4 Organic Traffic — Last 28 Days (2026-04-08 → 2026-05-05)

| Metric | Value |
|--------|-------|
| Organic sessions | 2 |
| Organic users | 2 |
| Organic pageviews | 2 |
| Avg daily sessions | 1.0 (but only 2 days with sessions) |
| Bounce rate | 50% (1 of 2 sessions bounced) |
| Avg session duration | Session 1: 4.9 s (bounced) / Session 2: 38.7 s (engaged) |

**Session detail:**
- 2026-05-01: 1 session, bounced immediately (4.9 s) — likely a quick brand check
- 2026-05-03: 1 session, engaged (38.7 s, 100% engagement rate) — meaningful visit

**Top organic landing pages:**

| Landing Page | Sessions | Users | Bounce Rate | Engagement Rate |
|-------------|----------|-------|-------------|-----------------|
| / (homepage) | 2 | 2 | 50% | 50% |

Only the homepage received organic traffic in the 28-day window. No blog articles, no FR homepage, no inner pages received GA4-attributed organic sessions.

**Geographic distribution:** Not available in the returned data (GA4 geo dimension not included in the default report response for this property). Note: with n=2 sessions, geo data would not be statistically meaningful.

**Interpretation:** GA4 organic is effectively zero — 2 sessions in 28 days from a single landing page. This is consistent with the GSC picture of ~10 clicks total in the same window. The delta between GSC clicks (10) and GA4 organic sessions (2) is expected: some users may have consent mode denying analytics, others may arrive via branded search that GA4 session-stitches differently, or the tracking setup (gtag.js, Consent Mode v2 denied by default) is suppressing a portion of sessions.

---

## 7. Cross-Signal Summary

| Dimension | Signal | Status |
|-----------|--------|--------|
| EN homepage indexation | Indexed, crawled 2026-05-06 | GOOD |
| FR homepage indexation | Indexed, crawled 2026-05-03 | GOOD |
| Blog indexation (any URL) | Unknown to Google | CRITICAL |
| Sitemap indexed URL count | 0/26 | CRITICAL |
| CrUX field data | Unavailable (insufficient traffic) | Note |
| Mobile LCP — homepage EN | 6.0 s (POOR) | HIGH |
| Mobile LCP — homepage FR | 9.6 s (POOR) | CRITICAL |
| Mobile LCP — blog/article | 4.8 s (POOR) | HIGH |
| Desktop performance | 86–99/100 across all pages | GOOD |
| Non-brand impressions | 15 in 28 days | LOW (expected at this stage) |
| GA4 organic sessions | 2 in 28 days | LOW |
| Rich results (FAQ) | Detected on EN homepage | GOOD |
| Canonical configuration | Correct on all indexed pages | GOOD |
| SEO Lighthouse score | 100/100 on all 4 pages tested | GOOD |

---

## 8. Five Most Surprising Findings

**1. GTM detected on the blog despite CLAUDE.md stating "no GTM, gtag direct."**
PSI network waterfall for `https://sparkcore.fund/blog/` shows `https://www.googletagmanager.com/gtag/js?id=G-J80NVPQNVZ` loading — a GTM-served script, not a raw gtag.js direct embed. GTM timing marks (`GTM-G-J80NVPQNVZ:15`, `:17`, `:10:14`) are present in user-timings on the blog index and also on the blog article. This represents an inconsistency between the documented stack and the live page behaviour. The script is responsible for 159 KiB of transfer and 273 ms of main-thread time on mobile — the single largest performance bottleneck on the blog. (Clarification needed: the homepage may use a genuinely direct gtag.js embed while blog pages inherited a legacy GTM container from a previous hosting configuration, or `analytics.js` itself loads via GTM internally.)

**2. FR homepage mobile score (45/100) is dramatically worse than EN (71/100) despite being the same visual template.**
A 26-point gap between identical-appearing pages is unusual. The FR page has 2.2 s of main-thread work vs the EN page's lean TBT of 50 ms. This suggests the FR page loads significantly more JavaScript or has heavier JS execution — possibly the ApexCharts library rendering a chart that takes longer on a "slower" mobile simulation, combined with the lang-redirect JS and a deeper DOM. LCP of 9.6 s is in critically unacceptable territory.

**3. `sparkcoretech com` generated 165 impressions in 28 days — the highest impression count of any query — with 0 clicks.**
This query refers to a different company (sparkcoretech.com, an IT services firm). Google is serving `sparkcore.fund` as a result for users searching for a competitor/different brand. This is brand confusion at scale: 165 people looked for sparkcoretech and were partially shown SparkCore Investment. The 0% CTR is correct behaviour (wrong brand), but this query accounts for 40% of all impressions. It inflates the impression count without representing real addressable traffic.

**4. The blog section is completely unknown to Google despite being live and in the sitemap.**
Three blog URLs sampled (blog index EN, blog index FR, one article) all returned "URL is unknown to Google" — never crawled. For a site with an active blog content strategy (11 articles referenced in CLAUDE.md), having zero blog URLs indexed is a significant content investment that is returning zero search visibility. Combined with the sitemap showing 0 indexed URLs, this suggests either a crawl budget/discovery issue or a recent migration disruption.

**5. The GSC sitemap shows 0 indexed URLs despite both homepages being confirmed indexed.**
This internal contradiction in GSC data (pages indexed via direct crawl, but 0 credit given to the sitemap) is almost certainly an artefact of the Cloudflare Pages migration that happened around 2026-05-06 (today) — the sitemap was last submitted on 2026-03-11, predating the migration. Google may have de-associated the sitemap in the process of re-evaluating the domain under the new host. Resubmitting the sitemap immediately post-migration is the correct action.

---

## 9. Three Highest-Impact Opportunities

**Opportunity 1 — Priority: CRITICAL — Resubmit sitemap and force blog crawl**
The entire blog (11+ articles) is invisible to Google. The sitemap was last submitted on 2026-03-11 and the site has since migrated to Cloudflare Pages. Immediate action: resubmit `https://sparkcore.fund/sitemap.xml` in GSC, then use the URL Inspection tool to request indexing on the 5 most important blog articles individually. Use IndexNow (`python3 scripts/ops/indexnow_ping.py --all`) to notify Bing simultaneously. Expected outcome: blog URLs enter Google's index within 2-4 weeks, enabling non-brand organic traffic from informational queries in the crypto/finance space.

**Opportunity 2 — Priority: HIGH — Fix mobile LCP across all pages (target: < 2,500 ms)**
Every page tested has a POOR mobile LCP (4.8–9.6 s). The root cause is consistent: render-blocking Google Fonts + Tailwind CSS + heavy gtag.js. The highest-ROI fix is: (a) self-host fonts using Cloudflare Pages (eliminate Google Fonts round-trip, ~751 ms savings on blog), (b) load `tailwind.min.css` inline or defer non-critical CSS (~459 ms savings), (c) defer gtag.js until after LCP element is painted (~600 ms TBT reduction). The FR homepage is the priority (9.6 s LCP, 45/100 mobile) — it may also have an image delivery issue (306 KiB savings flagged). Combined, these fixes could push mobile scores from 45–71 to 75–85 range, achieving the CrUX eligibility threshold faster and entering Google's CWV ranking signals.

**Opportunity 3 — Priority: HIGH — Target "finantsinspektsioon licence" and regulatory non-brand queries**
The query "finantsinspektsioon licence" returned 5 impressions at position 12.0 for the blog article `/blog/regulated-crypto-fund-manager-estonia`. Position 12 is just off page 1. A focused content update to that article — adding more specific regulatory details, the exact licence number, the supervised entity name, schema markup for the regulated entity — could push it to page 1 (positions 1-10), the first non-brand query to generate clicks for the site. At position 5, even with niche volume, this validates the content strategy and establishes topical authority for AIFM/regulatory content. Similarly, "estonia fund administration" at position 15 for the homepage points to a content gap: a dedicated page or article on Estonian fund administration structures would likely rank faster than trying to rank the homepage for that term.

---

## 10. Google Data Health Score

**Score: 38/100**

| Dimension | Score | Weight | Contribution | Notes |
|-----------|-------|--------|-------------|-------|
| Indexation coverage | 25/100 | 25% | 6.3 | Only 2 of 5 sampled URLs indexed; blog = 0% |
| Mobile Core Web Vitals | 15/100 | 25% | 3.8 | All 4 pages POOR LCP; no CrUX field data |
| Organic traffic volume | 10/100 | 20% | 2.0 | 2 GA4 sessions, 10 GSC clicks / 28d |
| Sitemap integrity | 20/100 | 10% | 2.0 | 0 indexed / 26 submitted; stale post-migration |
| Non-brand visibility | 10/100 | 10% | 1.0 | 15 non-brand impressions total, 0 clicks |
| Technical SEO hygiene | 90/100 | 10% | 9.0 | 100/100 Lighthouse SEO, correct canonicals, FAQ schema |

**Weighted total: 38/100**

**Context note:** A score of 38/100 reflects the site's early-stage position as a new YMYL financial domain in a niche market — not a site in technical distress. Technical SEO hygiene is high. The low score is driven almost entirely by volume (near-zero traffic, no CrUX eligibility) and the blog indexation gap. A site with the same technical quality and 6 months more indexation history would score 60-70/100. The actionable gap is primarily blog visibility and mobile performance.

---

## Appendix — Data Collection Log

| Script | Target | Status | File |
|--------|--------|--------|------|
| pagespeed_check.py | sparkcore.fund/ | OK | psi-home-en.json |
| pagespeed_check.py | sparkcore.fund/fr/ | OK | psi-home-fr.json |
| pagespeed_check.py | sparkcore.fund/blog | OK | psi-blog-index.json |
| pagespeed_check.py | sparkcore.fund/blog/why-invest-in-crypto-funds-2026 | OK | psi-blog-article.json |
| crux_history.py | sparkcore.fund (origin) | No data — insufficient Chrome traffic | crux-history-origin.json |
| crux_history.py | sparkcore.fund/fr/ | No data — insufficient Chrome traffic | crux-history-fr.json |
| gsc_query.py | sc-domain:sparkcore.fund | OK — 29 rows | gsc-queries.json |
| gsc_query.py sitemaps | sc-domain:sparkcore.fund | OK | gsc-sitemaps.json |
| gsc_inspect.py | sparkcore.fund/ | PASS | gsc-inspect-home-en.json |
| gsc_inspect.py | sparkcore.fund/fr/ | PASS | gsc-inspect-home-fr.json |
| gsc_inspect.py | sparkcore.fund/blog | NEUTRAL (unknown) | gsc-inspect-blog-en.json |
| gsc_inspect.py | sparkcore.fund/fr/blog | NEUTRAL (unknown) | gsc-inspect-blog-fr.json |
| gsc_inspect.py | sparkcore.fund/blog/why-invest-in-crypto-funds-2026 | NEUTRAL (unknown) | gsc-inspect-blog-article.json |
| ga4_report.py | property 530665322 | OK | ga4-organic.json |
| ga4_report.py top-pages | property 530665322 | OK | ga4-top-pages.json |
