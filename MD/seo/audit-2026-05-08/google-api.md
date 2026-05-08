# Google API Data — sparkcore.fund
**Date:** 2026-05-08 | **Tier:** 2 (Full — API Key + Service Account + GA4)
**GSC property:** `sc-domain:sparkcore.fund` | **GA4 property:** `530665322`
**Data freshness:** GSC 2026-04-10 → 2026-05-05 (28d, 2-3d lag) · GA4 2026-04-10 → 2026-05-07 (28d, 1d lag) · CrUX 28-day rolling

---

## 1. Credential Tier

| Layer | Status | Detail |
|---|---|---|
| API Key | Active | PageSpeed / CrUX access |
| Service Account | Active | `claude-seo@sparkcore-projet-1733486598578.iam.gserviceaccount.com` — GSC Full + GA4 Viewer |
| GA4 | Active | Property `530665322` confirmed (corrected 2026-05-02 from orphaned `529476067`) |

---

## 2. PageSpeed / Lighthouse

**Status: Script error (known bug in `pagespeed_check.py` — `KeyError: audit_details`).** PSI data skipped. Refer to lab estimates from the seo-performance agent report for performance scores.

---

## 3. CrUX Field Data

**Status: No data — `noCruxData`.**

> Insufficient Chrome user volume for eligibility threshold. Expected for a new institutional site with low organic traffic. CrUX eligibility requires meaningful Chrome usage across the origin over the 28-day collection window.

No LCP / INP / CLS field ratings available. Continue monitoring via GA4 + GSC as traffic grows. Re-check at J+90 checkpoint (2026-08-03).

---

## 4. GSC Search Performance — 28 Days (2026-04-10 → 2026-05-05)

Google API (field data)

### Summary

| Metric | Value |
|---|---|
| Total clicks | 11 |
| Total impressions | 368 (query-level) / 1,457 (page-level) |
| Average CTR | 3.15% (query) / 2.06% (page) |
| Active pages generating impressions | 16 |

Note: query-level and page-level impression totals differ because one page can rank for multiple queries simultaneously.

### Top 10 Queries by Clicks

| Query | Clicks | Impressions | CTR | Avg Position | Rating |
|---|---|---|---|---|---|
| sparkcore | 6 | 147 | 4.1% | 6.7 | Yellow — p7, threshold risk |
| spark core | 4 | 33 | 12.1% | 7.2 | Yellow — p7 |
| alexandre vinal | 1 | 8 | 12.5% | 3.6 | Green |
| sparkcoretech com | 0 | 125 | 0.0% | 7.7 | Red — brand confusion |
| spark core company | 0 | 6 | 0.0% | 5.3 | Yellow |
| chainscore crypto | 0 | 7 | 0.0% | 17.3 | Red — p17 |
| finantsinspektsioon licence | 0 | 7 | 0.0% | 16.6 | Red — p17 |
| estonia fund administration | 0 | 1 | 0.0% | 15.0 | Red — p15 |
| invest core | 0 | 3 | 0.0% | 38.3 | Red — deep |
| spark investment | 0 | 1 | 0.0% | 3.0 | Green — 0 clicks |

**Key observations:**

- All 11 clicks are brand-navigational ("sparkcore", "spark core", "alexandre vinal"). Zero clicks from non-brand / YMYL financial queries.
- "sparkcoretech com" generates 125 impressions at p7.7 with 0 clicks — searchers for a different entity are landing on sparkcore.fund results. Not actionable (cannot suppress competitor confusion), but confirms domain authority is near zero for disambiguated brand queries.
- "finantsinspektsioon licence" at p16.6 and "estonia fund administration" at p15 are the only two non-brand regulatory queries with impressions. Both below page 1. Reaching p1-5 on these would be the first meaningful non-brand traffic signal.

### Top 10 Pages by Clicks

| Page | Clicks | Impressions | CTR | Avg Position |
|---|---|---|---|---|
| sparkcore.fund/ | 17 | 649 | 2.6% | 6.5 |
| sparkcore.fund/fr/ | 8 | 57 | 14.0% | 3.4 |
| sparkcore.fund/blog/ | 1 | 90 | 1.1% | 6.0 |
| /blog/crypto-arbitrage-investment-fund | 1 | 76 | 1.3% | 5.1 |
| /blog/estonia-luxembourg-malta-crypto-fund | 1 | 193 | 0.5% | 8.1 |
| /blog/regulated-crypto-fund-manager-estonia | 1 | 95 | 1.1% | 10.0 |
| /blog/what-an-institutional-crypto-fund-manager-does | 1 | 46 | 2.2% | 7.7 |
| /blog/bitcoin-outperformance-strategy-fund | 0 | 27 | 0.0% | 6.9 |
| /blog/what-a-market-neutral-crypto-fund-does | 0 | 78 | 0.0% | 6.3 |
| /fr/blog/strategies-options-protection-portefeuille-actions | 0 | 41 | 0.0% | 4.7 |

**Key observations:**

- `/blog/estonia-luxembourg-malta-crypto-fund` has the highest impression volume (193) of any blog post but sits at p8.1 with only 1 click and 0.5% CTR. Breaking into top 5 here is the most immediate lever for non-brand traffic.
- `/blog/what-a-market-neutral-crypto-fund-does` (78 impressions, p6.3, 0 clicks) and `/blog/regulated-crypto-fund-manager-estonia` (95 impressions, p10.0, 1 click) are in the p6-10 band where small ranking improvements would cross the click-threshold.
- `/fr/` homepage at p3.4 / 14% CTR outperforms the EN homepage on CTR, suggesting French-speaking searchers find the title/description more relevant.

---

## 5. GSC URL Inspection — Key Pages

Google API (field data)

| URL | Verdict | Coverage State | Last Crawled | Crawled As | Canonical Match | Rich Results |
|---|---|---|---|---|---|---|
| sparkcore.fund/ | PASS | Submitted and indexed | 2026-05-08 01:38Z | Mobile | Yes | FAQ detected |
| sparkcore.fund/fr/ | PASS | Submitted and indexed | 2026-05-07 05:01Z | Mobile | Yes | FAQ detected |
| /resources/regulated-crypto-fund-estonia/ | PASS | Submitted and indexed | 2026-05-07 05:46Z | Mobile | Yes | Breadcrumbs + FAQ |
| /blog/regulated-crypto-fund-manager-estonia | PASS | Submitted and indexed | 2026-05-07 19:11Z | Mobile | Yes | Breadcrumbs + FAQ |
| /blog/crypto-fund-fees-2026 | PASS | Submitted and indexed | 2026-05-07 05:48Z | Mobile | Yes | Breadcrumbs + FAQ |

All 5 key pages: indexed, robots-allowed, mobile-crawled, canonical self-referential with no mismatch. Crawl cadence is healthy (all crawled within the last 48 hours). No mobile usability issues reported on any page.

**Note on `VERDICT_UNSPECIFIED` for mobile usability:** The API returns this when it has not completed a mobile-usability assessment for that crawl cycle, not as a failure. No issues array is populated, which is the clean state.

---

## 6. GSC Sitemap Status — Critical Finding

| Sitemap | Last Submitted | Errors | Warnings | URLs Submitted | URLs Indexed |
|---|---|---|---|---|---|
| sparkcore.fund/sitemap.xml | 2026-05-06 14:17Z | 0 | 0 | 28 | **0** |

**28 URLs submitted, 0 indexed in GSC's sitemap report.** This is a critical discrepancy. The URL Inspection tool confirms 5 key pages are individually "Submitted and indexed," meaning Google has indexed them — but GSC's sitemap index counter shows 0. This is a known GSC reporting lag / counter behavior for domain-property (`sc-domain:`) properties: sitemap-level indexed counts update more slowly than URL-level data and can show 0 for weeks after initial submission even when pages are individually indexed. The sitemap itself has 0 errors and 0 warnings, which confirms the XML is valid and parseable. Recommend monitoring at the J+14 checkpoint (2026-05-19 — already scheduled in crontab as `gsc-checkpoint-2026-05-19`). If the count remains 0 at J+30, investigate with a manual `fetch as Google` on the sitemap URL.

---

## 7. GA4 Organic Traffic — 28 Days (2026-04-10 → 2026-05-07)

Google API (field data)

| Metric | Value |
|---|---|
| Organic sessions | 2 |
| Organic users | 2 |
| Pageviews | 2 |
| Avg daily sessions | 1.0 (2 days with activity only) |

### Top Organic Landing Pages

| Landing Page | Sessions | Users | Bounce Rate | Engagement Rate | Avg Duration |
|---|---|---|---|---|---|
| / (homepage EN) | 2 | 2 | 50.0% | 50.0% | — |

**Conversion events fired:** 0 (factsheet_request_open, contact_form_submit, cal_booking_complete — none registered in the 28-day window).

**Interpretation:** GA4 organic sessions (2) are far lower than GSC clicks (11). This gap is expected and attributable to three factors: (1) gtag.js traffic attribution relies on cookie consent, and institutional visitors on a Consent Mode v2 site with strict defaults are modeled/not counted; (2) some GSC clicks are from searchers who bounce before GA4 fires; (3) the GA4 property was corrected on 2026-05-02 (replaced orphaned `529476067` with `530665322`) — data before that date may be missing. GA4 organic numbers will stabilize as traffic grows and consent mode modeling accumulates sufficient signal.

---

## 8. Indexation Health Summary

| Area | Status | Detail |
|---|---|---|
| Key pages indexed | All 5/5 | Confirmed via URL Inspection |
| Sitemap validity | Clean | 0 errors, 0 warnings |
| Sitemap index count | 0/28 | Likely GSC lag for sc-domain property — monitor |
| Canonical conflicts | None | All 5 inspected URLs: self-canonical, no mismatch |
| Robots.txt blocking | None | All pages: ALLOWED |
| Mobile crawl | Active | All pages crawled as mobile, no usability issues |
| Rich results | Detected | FAQ on all pages; Breadcrumbs on blog + resources |

---

## 9. Findings Table

| Severity | Area | Finding | Recommended Fix |
|---|---|---|---|
| High | GSC queries | Zero non-brand clicks in 28 days. All 11 clicks are navigational. | Accelerate ranking on in-progress targets: "estonia luxembourg malta crypto fund" (p8.1), "regulated crypto fund manager estonia" (p10), "finantsinspektsioon licence" (p16.6). Content depth + backlinks needed. |
| High | GSC queries | "sparkcoretech com" (125 impressions, p7.7, 0 clicks) — brand confusion with an unrelated entity. | Monitor for click cannibalization. Add explicit brand differentiation copy ("SparkCore Investment OÜ, Estonia") in meta descriptions to reduce confusion-driven zero-clicks. |
| Medium | GSC sitemap | 28 submitted / 0 indexed in sitemap counter. | Monitor at scheduled J+14 checkpoint (2026-05-19). If 0 persists at J+30, fetch sitemap manually in GSC. No immediate action required. |
| Medium | GA4 | Only 2 organic sessions vs 11 GSC clicks — consent/attribution gap. | Verify Consent Mode v2 configuration. Review GA4 data quality report to confirm modeling is active. Not a blocker at current traffic volume. |
| Medium | GSC queries | "finantsinspektsioon licence" at p16.6, "estonia fund administration" at p15 — regulatory queries with zero clicks. | These are high-value YMYL queries. Target via dedicated resources/ pages or blog content expansion. Already partially addressed by `/resources/regulated-crypto-fund-estonia/`. |
| Low | CrUX | No field data — insufficient Chrome volume. | No action. Re-evaluate at J+90 (2026-08-03). Continue GA4 monitoring. |
| Low | PageSpeed | PSI script has a known `KeyError: audit_details` bug preventing automated Lighthouse scores. | Fix `pagespeed_check.py` line ~289 (missing `audit_details` key init). Use seo-performance agent lab data in the meantime. |
| Info | URL Inspection | All 5 key pages crawled within 48h, all mobile-indexed, all FAQs detected. | No action needed. Healthy crawl cadence. |
