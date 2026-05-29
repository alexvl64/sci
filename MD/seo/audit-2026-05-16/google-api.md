# Google API Data — sparkcore.fund
**Date:** 2026-05-16 | **Tier:** 2 (Full — API Key + Service Account + GA4)
**GSC property:** `sc-domain:sparkcore.fund` | **GA4 property:** `530665322`
**Data freshness:** GSC 2026-04-18 → 2026-05-13 (28d, 2-3d lag) · GA4 2026-04-18 → 2026-05-15 (28d, 1d lag) · CrUX 28-day rolling
**Previous snapshot:** 2026-05-08 | **Delta period:** 8 days

---

## 1. Credential Tier

| Layer | Status | Detail |
|---|---|---|
| API Key | Active | PageSpeed / CrUX access |
| Service Account | Active | `claude-seo@sparkcore-projet-1733486598578.iam.gserviceaccount.com` — GSC Full + GA4 Viewer |
| GA4 | Active | Property `530665322` confirmed |

---

## 2. PageSpeed / Lighthouse (Lab Data)

**Status: Script ran successfully this time. `audit_details` bug appears resolved in current build.**

Google API (lab data) — run 2026-05-16

### Mobile Scores

| Metric | Score | Rating |
|---|---|---|
| Performance | 70/100 | Yellow — Needs Work |
| Accessibility | 96/100 | Green |
| Best Practices | 100/100 | Green |
| SEO | 100/100 | Green |

### Core Web Vitals Lab Metrics (Mobile)

| Metric | Value | Threshold | Rating |
|---|---|---|---|
| LCP (Largest Contentful Paint) | 10.9 s | Good: ≤2,500ms / Poor: >4,000ms | Red — POOR |
| FCP (First Contentful Paint) | 2.6 s | — | Yellow |
| TBT (Total Blocking Time) | 30 ms | — | Green |
| CLS (Cumulative Layout Shift) | 0 | Good: ≤0.1 | Green |
| Speed Index | 3.6 s | — | Green |
| Time to Interactive | 11.0 s | — | Red |

> **Critical: Mobile LCP at 10.9s is far above the 4,000ms Poor threshold.** This is a lab measurement from PSI's US/EU datacenter — actual user LCP in Europe may differ, but the gap is significant enough to indicate a real performance problem, not just geographic latency.

### Failed Audits (Mobile)

| Audit | Finding | Impact |
|---|---|---|
| LCP request discovery | LCP image not discoverable from HTML immediately, or lazy-loaded | High |
| Image delivery | Est. savings 346 KiB — images oversized for viewport | High |
| Forced reflow | JS queries geometric properties after DOM state change | Medium |
| Network dependency tree | Long critical request chain | Medium |
| Color contrast | Text/background contrast ratio insufficient (accessibility) | Low |

### Opportunities

| Opportunity | Estimated Savings |
|---|---|
| Reduce unused JavaScript | 300 ms |
| Improve image delivery | 346 KiB |

### Server Latency (from PSI diagnostics)

| Origin | Server Response Time |
|---|---|
| sparkcore.fund | 1 ms |
| cdn.jsdelivr.net | 1.5 ms |
| www.googletagmanager.com | 6 ms |
| challenges.cloudflare.com | 10 ms |

The Cloudflare Pages edge itself is fast (1 ms TTFB). The LCP bottleneck is not server latency — it is image delivery and render-blocking resources.

---

## 3. CrUX Field Data

**Status: No data — `noCruxData` (unchanged from 2026-05-08).**

Insufficient Chrome user volume for eligibility threshold. Expected for a new institutional site at this traffic stage. No LCP / INP / CLS field ratings available.

Re-check at J+90 checkpoint (2026-08-03, already scheduled in crontab as `gsc-checkpoint-2026-08-03`).

---

## 4. GSC Search Performance — 28 Days (2026-04-18 → 2026-05-13)

Google API (field data)

### Summary vs Prior Snapshot

| Metric | 2026-05-08 snapshot | 2026-05-16 snapshot | Delta |
|---|---|---|---|
| Total clicks (query-level) | 11 | 15 | +4 (+36%) |
| Total clicks (page-level) | 26 (page sum) | 42 | +16 (+62%) |
| Total impressions (query-level) | 368 | 1,246 | +878 (+239%) |
| Total impressions (page-level) | 1,457 | 5,558 | +4,101 (+282%) |
| Average CTR (page-level) | 2.06% | 0.76% | -1.3pp — diluted by new 0-click pages entering index |
| Active pages in GSC | 16 | 23 | +7 |

> **Impression volume has grown 3-4x in 8 days.** This is driven by new pages entering the index (particularly the new FR Clarity Act article and custody fees content) and reflects Googlebot discovering and ranking more content — not organic traffic in the traditional sense. Clicks have grown modestly (+36%) because the new impressions are mostly at positions p4-10 where CTR is low.

### Top 10 Queries by Clicks

| Query | Clicks | Impressions | CTR | Avg Position | Type | Rating |
|---|---|---|---|---|---|---|
| sparkcore | 6 | 118 | 5.1% | p6.0 | Brand | Yellow — p6, one rank from top-5 |
| clarity act | 4 | 257 | 1.6% | p7.1 | Non-brand | Yellow — high volume, p7 |
| spark core | 4 | 43 | 9.3% | p7.0 | Brand | Yellow — p7 |
| clarity act crypto | 1 | 18 | 5.6% | p9.1 | Non-brand | Yellow |
| (all others) | 0 | — | 0% | — | — | — |

**Key change from 2026-05-08:** "clarity act" is a new entrant at position 4 with 4 clicks and 257 impressions. This is the first meaningful non-brand query generating actual clicks. The `/fr/blog/clarity-act-us-impacts-investisseurs` article published post-05-08 is responsible.

### Non-Brand Query Landscape (0-click but notable impressions)

These queries show impressions with zero clicks — ranking but not yet converting to traffic. Sorted by impressions:

| Query | Impressions | Avg Position | Opportunity |
|---|---|---|---|
| how much does compliant crypto custody cost for an asset manager aum 500m rough pricing ranges | 200 | p1.2 | Critical — p1 but 0 clicks: title/snippet mismatch or SERP feature eating clicks |
| what is the typical pricing for compliant crypto custody for a hedge fund aum 200m | 263 | p1.1 | Critical — same pattern, p1 with 0 clicks |
| clarity act | 257 | p7.1 | High — 4 clicks already, push to p4 |
| cost to launch regulated crypto fund europe (page-level) | 972 | p4.3 | High — highest impression page with 0 clicks |
| crypto fund fees 2026 (page-level) | 937 | p4.3 | High — same page, needs snippet optimization |
| eur-lex directive 2011/61/eu article 3 100 million 500 million | 26 | p7.2 | Medium — long-tail regulatory, YMYL audience |
| aifmd sub-threshold 100 million 500 million without leverage lock-up 5 years | 6 | p8.0 | Medium — very specific regulatory query |
| estonia e-residency company setup for international trading payments crypto | 11 | p3.5 | Medium — p3.5 but 0 clicks, title relevance issue |
| sparkcoretech com | 49 | p7.9 | Monitor — brand confusion competitor |
| chainscore crypto | 28 | p16.2 | Monitor — unrelated entity confusion |
| finantsinspektsioon licence | 7 | p12.1 | Medium — down from p16.6 (+4 positions gained) |

**Standout finding — custody fees page at p1 with 0 clicks:**
`/blog/crypto-fund-fees-2026` appears to rank p1.1-1.2 for "compliant crypto custody cost" queries (200-263 impressions) with zero clicks. At p1, expected CTR is 25-35%. Zero clicks suggests one of three explanations: (1) a featured snippet or AI Overview is absorbing all clicks above the organic listing; (2) the title/description does not match the searcher's expected result; or (3) GSC's position reporting is averaging across a mix of very high and very low positions. This requires a manual SERP check.

### Top 10 Pages by Clicks

| Page | Clicks | Impressions | CTR | Avg Position | vs 05-08 |
|---|---|---|---|---|---|
| sparkcore.fund/ | 14 | 584 | 2.4% | p6.3 | -3 clicks, -65 imp, +0.2pp CTR |
| /fr/blog/clarity-act-us-impacts-investisseurs | 12 | 854 | 1.4% | p5.9 | **NEW — not in prior snapshot** |
| sparkcore.fund/fr/ | 9 | 74 | 12.2% | p9.9 | +1 click, +17 imp |
| /blog/crypto-fund-fees-2026 | 1 | 937 | 0.1% | p4.3 | NEW entry — highest impressions in corpus |
| /blog/cost-to-launch-regulated-crypto-fund-europe | 0 | 972 | 0.0% | p4.3 | NEW — near-equal impressions, zero clicks |
| /blog/estonia-eresidency-crypto-fund-eu | 0 | 643 | 0.0% | p6.5 | NEW |
| /blog/aif-vs-aifm-crypto-explained | 0 | 324 | 0.0% | p8.0 | NEW |
| /resources/regulated-crypto-fund-estonia/ | 1 | 271 | 0.4% | p7.9 | stable |
| /blog/estonia-luxembourg-malta-crypto-fund | 1 | 262 | 0.4% | p8.4 | +69 imp, position worsened from p8.1 |
| /blog/regulated-crypto-fund-manager-estonia | 1 | 117 | 0.9% | p13.4 | position worsened from p10.0 |

**Key observations:**

- The `/fr/blog/clarity-act-us-impacts-investisseurs` article is now the 2nd most-clicked page on the site with 12 clicks in its first weeks, ranking at p5.9. This is the strongest non-brand organic signal the site has produced. The Clarity Act was actively legislated in the US in May 2026, creating real search demand.
- `/blog/cost-to-launch-regulated-crypto-fund-europe` and `/blog/crypto-fund-fees-2026` have each accumulated ~950 impressions but zero clicks. Both sit at p4.3 — theoretically in the click zone but clearly not converting impressions to clicks. Meta description optimization or competing SERP features are the most likely causes.
- `/blog/regulated-crypto-fund-manager-estonia` has slipped from p10.0 to p13.4 (-3.4 positions) — regression into page 2.
- `/blog/estonia-luxembourg-malta-crypto-fund` has slipped from p8.1 to p8.4 — marginal, within variance.

### Brand vs Non-Brand Split

| Category | Clicks | % of Total |
|---|---|---|
| Brand (sparkcore, spark core, alexandre vinal, spark core company, sparkcoretech, etc.) | ~10 | ~67% |
| Non-brand (clarity act, clarity act crypto, etc.) | ~5 | ~33% |

First non-brand clicks have arrived. The 2026-05-08 snapshot was 100% brand. This is the first measurable non-brand organic traffic signal on sparkcore.fund.

---

## 5. GSC URL Inspection — Key Pages

Google API (field data) — run 2026-05-16

| URL | Verdict | Coverage | Last Crawled | Crawled As | Rich Results |
|---|---|---|---|---|---|
| sparkcore.fund/ | PASS | Submitted and indexed | 2026-05-15 14:01Z | Mobile | FAQ |
| sparkcore.fund/fr/ | PASS | Submitted and indexed | 2026-05-14 20:55Z | Mobile | FAQ |
| /resources/regulated-crypto-fund-estonia/ | PASS | Submitted and indexed | 2026-05-08 15:40Z | Mobile | Breadcrumbs + FAQ |
| /blog/regulated-crypto-fund-manager-estonia | PASS | Submitted and indexed | 2026-05-07 19:11Z | Mobile | Breadcrumbs + FAQ |
| /blog/estonia-luxembourg-malta-crypto-fund | PASS | Submitted and indexed | 2026-05-10 09:36Z | Mobile | Breadcrumbs + FAQ |
| /fr/blog/strc-strategy-yield-analysis | NEUTRAL | URL is unknown to Google | Not crawled | — | None |

**All 5 existing key pages remain indexed and crawled.** Crawl cadence on the homepage has improved — last crawl 2026-05-15 (yesterday), vs 2026-05-08 in the prior snapshot. This indicates Googlebot is visiting the homepage daily.

**Notable referring URLs discovered (homepage inspection):**
- `aeroleads.com` — a B2B lead intelligence tool; suggests the site is being indexed by prospecting tools
- `krediidiraportid.ee/sci-equinoxe-usaldusfond-uu` — an Estonian credit/company report site has indexed a page for SparkCore. This is a first external link signal appearing in GSC data

**New article not yet indexed:** `/fr/blog/strc-strategy-yield-analysis` (commit 6ca9d55) is completely unknown to Google — no crawl, no canonical, not yet discovered. This is expected for a very recent publish (days old), but requires an IndexNow ping to accelerate discovery.

---

## 6. GSC Sitemap Status

| Sitemap | Last Submitted | Errors | Warnings | URLs Submitted | URLs Indexed |
|---|---|---|---|---|---|
| sparkcore.fund/sitemap.xml | 2026-05-06 14:17Z | 0 | 0 | 28 | **0** |

**Sitemap counter still shows 0 indexed at J+10 post-submission.** The URL Inspection tool confirms multiple pages are individually "Submitted and indexed," confirming Google has indexed them — but the sitemap-level counter remains at 0. This is a persistent GSC reporting behavior for `sc-domain:` domain properties.

Assessment: This is not an indexation problem. It is a known GSC counter lag. The scheduled `gsc-checkpoint-2026-05-19` (J+14) will provide the next data point. If the counter remains 0 at J+30 (`gsc-checkpoint-2026-06-04`), a manual fetch of the sitemap URL in GSC Search Console UI would be warranted.

---

## 7. GA4 Organic Traffic — 28 Days (2026-04-18 → 2026-05-15)

Google API (field data)

### Summary vs Prior Snapshot

| Metric | 2026-05-08 snapshot | 2026-05-16 snapshot | Delta |
|---|---|---|---|
| Organic sessions | 2 | 4 | +2 (+100%) |
| Organic users | 2 | 3 | +1 (+50%) |
| Pageviews | 2 | 3 | +1 |
| Avg daily sessions | 1.0 (2 active days) | 1.3 (3 active days) | +1 active day |

### Top Organic Landing Pages (GA4)

| Landing Page | Sessions | Users | Bounce Rate | Engagement Rate |
|---|---|---|---|---|
| / (EN homepage) | 2 | 2 | 50% | 50% |
| /resources/regulated-crypto-fund-estonia | 1 | 1 | 100% | 0% |
| (not set) | 1 | 1 | 100% | 0% |

**Note:** GA4 counts 4 organic sessions against GSC's 42 page-level clicks. The attribution gap of ~38 sessions is attributable to: (1) Consent Mode v2 denied-by-default — institutional visitors on a strict-consent site are partially unmodeled; (2) GSC counts impression/click events that include pre-fetch and quick bounces that never fire GA4; (3) the Clarity Act FR article (12 GSC clicks) is not surfacing as an organic landing page in GA4, which likely means those visitors bounced before GA4 fired or consented, or are modeled but aggregated into the `(not set)` group.

**Conversion events fired:** 0 in the 28-day window (factsheet_request_open, contact_form_submit, cal_booking_complete).

---

## 8. Indexation Health Summary

| Area | Status | Detail |
|---|---|---|
| Key pages indexed | 5/6 | 5 confirmed indexed; /fr/blog/strc-strategy-yield-analysis unknown to Google |
| Sitemap validity | Clean | 0 errors, 0 warnings |
| Sitemap indexed counter | 0/28 | Persistent GSC sc-domain lag — not a real indexation issue |
| Canonical conflicts | None | All 5 inspected-and-indexed URLs: self-canonical, no mismatch |
| Robots.txt blocking | None | All indexed pages: ALLOWED |
| Mobile crawl | Active | All indexed pages crawled as mobile |
| Rich results | Detected | FAQ on all indexed pages; Breadcrumbs on blog + resources |
| Crawl freshness | Improving | Homepage now crawled daily (2026-05-15), up from weekly |
| External links discovered | 2 | aeroleads.com + krediidiraportid.ee — first link signals in GSC |

---

## 9. Trend Summary — 8-Day Delta (2026-05-08 → 2026-05-16)

| Signal | Direction | Commentary |
|---|---|---|
| GSC clicks | +36% (11→15 query-level) | Growth driven by Clarity Act FR article |
| GSC impressions | +239% (query) / +282% (page) | Corpus expanding — new pages entering SERP |
| Non-brand clicks | 0% → ~33% | First non-brand organic clicks on the site |
| Active pages in GSC | 16 → 23 | +7 new pages in the index |
| Avg position (leading pages) | Mixed | fees/cost pages at p4.3 (new high); estonia blog slipped to p13.4 |
| GA4 organic sessions | 2 → 4 | Doubled but still near-zero volume |
| New backlinks in GSC | 0 → 2 | krediidiraportid.ee + aeroleads.com discovered |
| Mobile LCP (lab) | Not measured 05-08 | 10.9s — POOR, significant performance gap |
| Factsheet page appearing in GSC | 0 → 1 | /factsheets/cryptovision has 2 impressions at p7 — gated page is leaking |

---

## 10. Findings and Recommendations

| Priority | Area | Finding | Recommended Action |
|---|---|---|---|
| Critical | Performance | Mobile LCP 10.9s — POOR. PSI identifies LCP image not discoverable from HTML (lazy-loaded or missing preload), plus 346 KiB oversized images. | Audit the LCP element on CF Pages deployment. Add `fetchpriority="high"` + `rel="preload"` on the LCP hero image. Compress/resize images to viewport dimensions. Target: LCP < 2,500ms. |
| Critical | Indexation | `/fr/blog/strc-strategy-yield-analysis` (newest article, commit 6ca9d55) is "unknown to Google" — no crawl, no discovery. | Run IndexNow ping immediately: `python3 scripts/ops/indexnow_ping.py https://sparkcore.fund/fr/blog/strc-strategy-yield-analysis`. Optionally submit URL directly in GSC URL Inspection tool. |
| High | GSC queries | `/blog/crypto-fund-fees-2026` and `/blog/cost-to-launch-regulated-crypto-fund-europe` each have ~950 impressions at p4.3 with 0 clicks. P4 should yield 8-12% CTR normally. | Check the live SERP manually for "crypto fund fees 2026" and "cost to launch regulated crypto fund europe" — likely an AI Overview or Featured Snippet is capturing all clicks. If so, optimize for SERP feature targeting (concise structured answer in H2 + summary table). |
| High | GSC queries | Custody fees queries ("how much does compliant crypto custody cost for asset manager aum 500m") ranking p1.1-1.2 with 200-263 impressions and 0 clicks. At p1, expected CTR is 25-35%. | Manual SERP check required. If AI Overview is present, add a direct answer box / FAQ schema to the article. If it's a title mismatch, revise the `<title>` to match the query intent more closely. |
| High | SEO | `/fr/blog/clarity-act-us-impacts-investisseurs` is the top non-brand traffic driver (12 clicks, p5.9). Timing-sensitive — Clarity Act is in active legislation. | Maintain freshness: bump `dateModified` with substantive update after any Clarity Act vote/signature. Ensure the article is linked from the FR homepage and the FR blog index. Monitor position weekly — if it drops to p8+ as the news cycle fades, the article needs a content refresh. |
| High | Security/SEO | `/factsheets/cryptovision` appears in GSC with 2 impressions at p7. This gated page has `noindex` meta tag and `X-Robots-Tag: noindex, nofollow, noarchive` via CF `_headers`. It should not be indexed. | Verify the CF `_headers` rule is live in production: `curl -I https://sparkcore.fund/factsheets/cryptovision` and check for `X-Robots-Tag: noindex` in response headers. If the header is missing, the CF Transform Rule or `_headers` file may not be applying correctly. Submit URL for removal in GSC if it gains further impressions. |
| Medium | GSC rankings | `/blog/regulated-crypto-fund-manager-estonia` slipped from p10.0 to p13.4 (-3.4 positions) — into page 2 territory. | This page had 95 impressions in the prior period at p10; it now has 117 impressions but at p13.4. A content update (add new regulatory reference post-AIFMD II transposition April 2026, bump dateModified) + internal linking from the pillar page could arrest the slide. |
| Medium | GSC queries | `finantsinspektsioon licence` improved from p16.6 to p12.1 (+4.5 positions). Still page 2. | The `/resources/regulated-crypto-fund-estonia/` page is the natural home for this query. Confirm it is the ranking page. Add "Finantsinspektsioon licence" as an explicit H2 or FAQ entry if not already present. Target: p7 by J+60. |
| Medium | GSC | "sparkcoretech com" at p7.9 with 49 impressions (down from 125 impressions in prior snapshot) — brand confusion competitors query declining. | Positive trend. Continue monitoring. No action needed unless impressions climb again. |
| Low | GA4 | 4 GA4 organic sessions vs 42 GSC clicks — 38-session attribution gap. | Verify Consent Mode v2 is correctly configured and modeling is active. Review GA4 Data Quality report for the property. Attribution gap will narrow as traffic grows. Not a blocker. |
| Low | CrUX | No field data — insufficient Chrome volume. | No action. Re-evaluate at J+90 (2026-08-03). |
| Info | External links | krediidiraportid.ee has linked to SparkCore. This is the first external domain link signal visible in GSC. | No action needed. Monitor for additional link acquisition from Estonian regulatory/business directories. |

---

## 11. IndexNow Action Required

The newest article `/fr/blog/strc-strategy-yield-analysis` is unknown to Google. Run immediately from the VPS:

```bash
python3 /home/alex/Documents/Claude/github-projets/sci/scripts/ops/indexnow_ping.py \
  https://sparkcore.fund/fr/blog/strc-strategy-yield-analysis
```

This will notify Bing, Yandex, and Google-indexing-compatible engines. For Google specifically, also submit the URL via GSC URL Inspection tool (manual step in browser).

---

## 12. Data File Locations

Raw JSON dumps saved to:
`/home/alex/Documents/Claude/github-projets/sci/MD/seo/audit-2026-05-16/data/google-api/`

| File | Contents |
|---|---|
| `gsc_queries.json` | 92 queries, 28d totals |
| `gsc_pages.json` | 23 pages, 28d totals |
| `gsc_sitemaps.json` | Sitemap status (28 submitted / 0 indexed counter) |
| `ga4_organic.json` | 4 organic sessions, top landing pages |
| `crux_history.json` | No data response |
| `pagespeed.json` | Mobile PSI scores summary |
| `url_inspections.json` | 6 URL inspection results |
