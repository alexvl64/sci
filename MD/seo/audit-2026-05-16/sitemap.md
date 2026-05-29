# Sitemap Audit — sparkcore.fund — 2026-05-16

**Previous audit:** 2026-05-08 — Score 92/100
**Data source:** `curl https://sparkcore.fund/sitemap.xml` at audit time; local copy saved to `MD/seo/audit-2026-05-16/data/sitemap.xml`

---

## 1. Executive Summary

The sitemap is structurally valid, correctly scoped, and now reflects the 6th FR article (`strc-strategy-yield-sous-remunere-analyse`, published 2026-05-11). All 35 URLs are public, indexable content. Gated pages remain absent and are enforced by `X-Robots-Tag: noindex, nofollow, noarchive` at the edge. One new medium-severity finding compared to the 2026-05-08 audit: four sitemap entries (`/`, `/fr/`, `/blog/`, `/fr/blog/`) carry `lastmod: 2026-05-08` despite those pages receiving content or structural changes on 2026-05-11 and 2026-05-16. The `priority`/`changefreq` removal recommendation from 2026-05-08 was not actioned — still present, remains Info-level.

---

## 2. URL Inventory (35 URLs total)

| Category | Count | Notes |
|---|---|---|
| EN homepage | 1 | `/` |
| FR homepage | 1 | `/fr/` |
| EN blog index | 1 | `/blog/` |
| FR blog index | 1 | `/fr/blog/` |
| EN pillar page | 1 | `/resources/regulated-crypto-fund-estonia/` |
| EN blog articles | 23 | See full list below |
| FR blog articles | 6 | Confirmed 6 — up from 5 at 2026-05-08 |
| Privacy policy | 1 | `/privacy-policy` |
| Orphans | 0 | None detected |

**Total vs 50k limit:** 35 / 50,000 — no index sitemap required.

### EN blog articles (23)

`aif-vs-aifm-crypto-explained`, `bitcoin-outperformance-strategy-fund`, `cost-to-launch-regulated-crypto-fund-europe`, `crypto-arbitrage-investment-fund`, `crypto-fund-compliance-guide`, `crypto-fund-fees-2026`, `crypto-fund-for-qualified-investors`, `crypto-fund-vs-etf`, `delta-neutral-crypto-strategies-explained`, `do-crypto-fund-managers-need-mica-casp-license`, `estonia-eresidency-crypto-fund-eu`, `estonia-luxembourg-malta-crypto-fund`, `how-to-launch-a-crypto-fund-estonia`, `regulated-crypto-fund-manager-estonia`, `regulated-crypto-investment-fund`, `sub-threshold-aifm-crypto-estonia`, `what-a-market-neutral-crypto-fund-does`, `what-an-alternative-investment-fund-platform-does`, `what-an-institutional-crypto-fund-manager-does`, `what-is-a-crypto-aifm`, `white-label-crypto-fund-manager-services`, `white-label-crypto-fund-platform`, `why-invest-in-crypto-funds-2026`

### FR blog articles (6)

`agents-ia-blockchain-economie-agentique`, `clarity-act-us-impacts-investisseurs`, `indicateurs-marche-crypto-actifs`, `le-vrai-cout-du-market-timing`, `strategies-options-protection-portefeuille-actions`, `strc-strategy-yield-sous-remunere-analyse` (NEW — added 2026-05-11, commit `6ca9d55`)

---

## 3. XML Validity

Pass. The sitemap declares both required namespaces on `<urlset>`:

- `xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"` — base sitemap spec
- `xmlns:xhtml="http://www.w3.org/1999/xhtml"` — required for `<xhtml:link rel="alternate">` hreflang blocks

UTF-8 declaration present. No malformed tags, no encoding issues, no unclosed elements detected.

---

## 4. Hreflang Consistency

The dual-cluster strategy (EN regulatory hub / FR investor-education) means blog articles are independent — not translations — so self-referential hreflang with no cross-cluster alternate is the correct implementation.

| URL pair | hreflang declared | Assessment |
|---|---|---|
| `/` and `/fr/` | `en`, `fr`, `x-default` bidirectional | Correct |
| `/blog/` and `/fr/blog/` | `en`, `fr`, `x-default` bidirectional | Correct |
| `/resources/regulated-crypto-fund-estonia/` | `en` + `x-default` self-referential | Correct — EN-only page |
| EN blog articles (`/blog/*`) | `en` + `x-default` self-referential | Correct — dual-cluster policy |
| FR blog articles (`/fr/blog/*`) | None (no hreflang block) | Correct — dual-cluster policy; FR articles have no EN mirror |
| `/privacy-policy` | `en` + `x-default` self-referential | Correct — EN-only page |

No hreflang issues. The new STRC article (`strc-strategy-yield-sous-remunere-analyse`) correctly carries no hreflang block, consistent with all other FR articles.

---

## 5. lastmod Accuracy

| Entry | lastmod in sitemap | Last real git commit | Gap | Assessment |
|---|---|---|---|---|
| `/` | 2026-05-08 | 2026-05-11 (header fix + mobile layout) | 3d | Stale |
| `/fr/` | 2026-05-08 | 2026-05-16 (hero badge update `1ff6ff5`) | 8d | Stale |
| `/blog/` | 2026-05-08 | 2026-05-11 (header fix + mobile layout) | 3d | Stale |
| `/fr/blog/` | 2026-05-08 | 2026-05-11 (charts/layout fix) | 3d | Stale |
| `/fr/blog/strc-strategy-yield-sous-remunere-analyse` | 2026-05-11 | 2026-05-11 (`6ca9d55`) | 0 | Correct |
| `/fr/blog/agents-ia-blockchain-economie-agentique` | 2026-05-08 | 2026-05-13 (`ffdb850` bps fix) | 5d | Stale |
| EN blog articles | 2026-05-08 | 2026-05-08 (sprint 6 batch) | 0 | Correct |
| `/resources/regulated-crypto-fund-estonia/` | 2026-05-08 | 2026-05-08 (sprint 6 batch) | 0 | Correct |
| `/privacy-policy` | 2026-03-05 | 2026-03-05 (initial publish) | 0 | Correct |

**Stale entries identified:** `/`, `/fr/`, `/blog/`, `/fr/blog/`, `/fr/blog/agents-ia-blockchain-economie-agentique` — five entries. The most significant is `/fr/` which shows 2026-05-08 despite a live content change (hero badge) merged to main at `1ff6ff5` on 2026-05-16.

Note: `lastmod` staleness on structural pages (`/`, `/blog/`) from minor layout fixes (header mobile, chart sizing) is borderline — these are template changes, not content changes. Google's guidance is to use `lastmod` only for meaningful content changes. However `/fr/` has a genuine content delta (new hero badge linking to STRC article), and `/fr/blog/agents-ia-blockchain-economie-agentique` has a terminology correction (`bps` → `points de base`), both of which warrant a bump.

---

## 6. priority and changefreq Tags

Both tags remain present across all 35 entries (no change from 2026-05-08 audit). Google officially ignores both. Bing also ignores `priority`; `changefreq` has marginal effect on Bing crawl scheduling at most.

Severity: Info. No ranking impact. Removing reduces file size marginally and eliminates maintenance debt.

---

## 7. Gated Pages — Absence Confirmed

Cross-checked sitemap against all three gated paths:

| Gated path | Present in sitemap | HTTP status | X-Robots-Tag header |
|---|---|---|---|
| `/factsheets/dynamic-trends` | No | 200 (page loads) | `noindex, nofollow, noarchive` |
| `/factsheets/cryptovision` | No | 200 (page loads) | `noindex, nofollow, noarchive` |
| `/discovery-call` | No | 200 (page loads) | `noindex, nofollow, noarchive` |

All four protection layers remain intact: meta noindex in HTML, `X-Robots-Tag` via `_headers`, `robots.txt` Disallow, and sitemap exclusion. Pass.

---

## 8. HTTP Status — Sampled URLs

All sampled URLs return HTTP 200 after following redirects (`curl -L`).

| URL | Status |
|---|---|
| `https://sparkcore.fund/` | 200 |
| `https://sparkcore.fund/resources/regulated-crypto-fund-estonia/` | 200 |
| `https://sparkcore.fund/fr/blog/strc-strategy-yield-sous-remunere-analyse` | 200 |
| `https://sparkcore.fund/fr/blog/clarity-act-us-impacts-investisseurs` | 200 |
| `https://sparkcore.fund/blog/delta-neutral-crypto-strategies-explained` | 200 |
| `https://sparkcore.fund/blog/white-label-crypto-fund-manager-services` | 200 |
| `https://sparkcore.fund/privacy-policy` | 200 |

No redirected or 404 URLs found in the sitemap. Pass.

---

## 9. Trailing-Slash Policy

Cloudflare Redirect Rule strips trailing slashes on `/blog/*/` → `/blog/$1` (301). Per the 2026-05-08 audit, this rule was confirmed correct.

Blog articles in the sitemap carry no trailing slashes — consistent with the CF redirect rule. Directory-style URLs (`/`, `/fr/`, `/blog/`, `/fr/blog/`, `/resources/regulated-crypto-fund-estonia/`) correctly carry trailing slashes. The new STRC article is listed without a trailing slash (`/fr/blog/strc-strategy-yield-sous-remunere-analyse`). Pass.

**Note (from 2026-05-08):** The trailing-slash CF Redirect Rule for blog articles was removed from `_redirects` in commit `598929f` (infra cleanup), but the CF zone-level Redirect Rule remains active. No change to this check.

---

## 10. Coverage Delta — New Content Since 2026-05-08

| Page | Status |
|---|---|
| `/fr/blog/strc-strategy-yield-sous-remunere-analyse` | In sitemap — correct, `lastmod: 2026-05-11` accurate |
| FR cluster total | 6 articles (was 5) — count confirmed |
| EN cluster total | 23 articles — no change |
| Any new EN articles in repo | None — repo has exactly 23 `/blog/*.html` files (excluding `index.html`) |

The FR article count question from the 2026-05-08 brief is now settled: 6 FR articles live in both the repo and the sitemap. The CLAUDE.md dual-cluster policy doc still references 4 FR articles in the "FR cluster" section (the old count from before the recent additions) — this is a doc drift issue, not a sitemap issue.

---

## 11. Findings Table

| Severity | Check | Location | Finding | Recommended Fix |
|---|---|---|---|---|
| Medium | lastmod accuracy | `/fr/` | lastmod `2026-05-08` but page had hero badge content change on 2026-05-16 (`1ff6ff5`) | Bump to `2026-05-16` |
| Medium | lastmod accuracy | `/fr/blog/agents-ia-blockchain-economie-agentique` | lastmod `2026-05-08` but terminology correction shipped 2026-05-13 (`ffdb850`) | Bump to `2026-05-13` |
| Low | lastmod accuracy | `/`, `/blog/`, `/fr/blog/` | lastmod `2026-05-08` but structural layout changes (header/chart) shipped 2026-05-11 — minor, not content changes | Bump to `2026-05-11` if treating template edits as meaningful; acceptable to leave |
| Info | Deprecated tags | All 35 `<url>` entries | `priority` and `changefreq` present — ignored by Google | Remove from sitemap on next regeneration |
| Info | Doc drift | CLAUDE.md FR cluster section | Still references 4 FR articles; live count is 6 | Update FR cluster article count in CLAUDE.md |
| Info | Bing WMT legacy | Bing WMT UI | Legacy `www.sparkcore.fund/sitemap.xml` (10 URLs) still listed — carryover from 2026-05-08 | Delete via Bing WMT UI (cosmetic) |

No critical or high issues. No non-200 URLs. No gated pages leaking into sitemap. No hreflang violations.

---

## 12. Score

**94 / 100**

| Deduction | Reason | Points |
|---|---|---|
| -3 | Medium: two `lastmod` entries stale against real content changes (`/fr/` hero badge, `agents-ia` bps fix) | -3 |
| -2 | Info: `priority`/`changefreq` still present (carried from 2026-05-08, second audit cycle without action) | -2 |
| -1 | Info: CLAUDE.md FR article count doc drift | -1 |

Up from 92/100 at 2026-05-08: +2 gained by correctly adding STRC article with accurate `lastmod: 2026-05-11`; -2 offset by `priority`/`changefreq` escalating from first-instance to repeated finding.

---

## 13. Top 3 Actions

1. **Bump stale `lastmod` for `/fr/` and `/fr/blog/agents-ia-blockchain-economie-agentique`** — `/fr/` should move to `2026-05-16` (hero badge content delta); `agents-ia` should move to `2026-05-13` (terminology correction). Optionally bump `/`, `/blog/`, `/fr/blog/` to `2026-05-11` for the layout/header fixes. These are the two entries where the gap is clearly content-driven, not purely structural.

2. **Remove `priority` and `changefreq` tags** — both have now appeared in two consecutive audits without being actioned. Strip them from the sitemap template. This is the lowest-effort change and eliminates the recurring Info finding.

3. **Delete the legacy Bing WMT submission** (`www.sparkcore.fund/sitemap.xml`, 10 URLs) from the Bing Webmaster Tools UI — cosmetic cleanup, prevents Bing from treating the two submissions as conflicting signals.
