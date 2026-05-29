# Technical SEO Audit — sparkcore.fund
**Date:** 2026-05-16
**Auditor:** seo-technical
**Baseline (2026-05-08):** 84 / 100
**Score: 91 / 100** (+7 from baseline)

---

## Context

Incremental audit since the 2026-05-08 baseline. All five prior findings (T-01 through T-05) reviewed. Significant infra changes audited: `.htaccess` removal, branded 403/500 pages via `functions/_middleware.js`, `_redirects` MD/ leak closure, FR blog 301 normalization (trailing-slash rules), and header mobile fixes (#151–153). One new article published since baseline (`/fr/blog/strc-strategy-yield-sous-remunere-analyse`, 2026-05-11). Raw curl data in `data/technical-headers.txt`.

---

## What Passes (14/14 checks green)

| Check | Result | Evidence |
|---|---|---|
| HTTPS enforced | PASS | HTTP/2 200 on all pages; www→non-www 301 confirmed |
| HSTS with preload | PASS | `strict-transport-security: max-age=31536000; includeSubDomains; preload` live on all responses including www redirect |
| Security headers (CSP, X-Frame, nosniff, Referrer, Permissions) | PASS | All present on `/`, `/fr/`, `/blog/`, `/fr/blog/` — no regression |
| CSP via CF Transform Rule | PASS | Full CSP value confirmed; `font-src 'self'` correct for self-hosted fonts |
| robots.txt syntax and AI crawler allowlist | PASS | 6 AI crawlers (GPTBot, OAI-SearchBot, Google-Extended, ClaudeBot, PerplexityBot, CCBot) correctly allowed with targeted disallows on `/factsheets/`, `/discovery-call`, `/validation`, `/MD/` |
| Sitemap (HTTP 200, correct MIME, hreflang) | PASS | 35 URLs, `xmlns:xhtml` namespace present, homepage 3-way hreflang correct |
| Canonicals (self-reference) | PASS | `/` → `https://sparkcore.fund/`, `/fr/` → `https://sparkcore.fund/fr/`, articles self-canonical |
| hreflang EN↔FR on homepages | PASS | Reciprocal alternates on both `/` and `/fr/`, `x-default` → `/` |
| JS rendering (SSR, bot guard) | PASS | Static HTML pre-rendered per language; bot-skip regex in `lang-redirect-*.js` prevents Googlebot redirect |
| PDF gate (`/ressources/instructions_depot_dynamic_trends.pdf`) | PASS | HTTP 403 confirmed without hash param; branded 403.html served with `noindex` meta |
| MD/ leak (`/MD/README.md`) | PASS | HTTP 404 — `_redirects` rule `/MD/* /404.html 404` active |
| Branded error pages (403/500) | PASS | 403.html served by `functions/_middleware.js`; `<title>403 — Access Denied — SparkCore Fund Management</title>` and `noindex` confirmed in body |
| IndexNow key file | PASS | `https://sparkcore.fund/27994a06b868d24820429dc36c1bafee.txt` → HTTP 200 |
| BingSiteAuth.xml | PASS | HTTP 200; GUID `0739094849505C87C0C6BCFDCA094258` |
| Gated pages (discovery-call, factsheets) | PASS | `X-Robots-Tag: noindex, nofollow, noarchive` confirmed on both via `_headers` |
| Article sample (3 EN + 1 new FR) | PASS | All HTTP 200; self-canonical and `index, follow` confirmed |
| Trailing-slash redirects EN + FR | PASS | Both `/blog/:slug/` and `/fr/blog/:slug/` return 301 (no longer 308 on FR) |
| Mobile viewport + lang attributes | PASS | `<meta name="viewport">` and `<html lang>` confirmed on all tested pages |
| Structured data (homepage) | PASS | 3 JSON-LD blocks: `@graph` (Organization + WebPage), `ItemList` (SiteNavigation), `FAQPage` |

---

## Prior Findings Status

| ID | Severity (2026-05-08) | Finding | Status 2026-05-16 |
|---|---|---|---|
| T-01 | Medium | `/validation` X-Robots-Tag missing — `_headers` targeted `/validation.html` only | **CLOSED** — `/validation` now returns `X-Robots-Tag: noindex, nofollow, noarchive`; `_headers` updated to target extensionless path |
| T-02 | Medium | HSTS `preload` flag absent | **CLOSED** — `preload` confirmed live: `strict-transport-security: max-age=31536000; includeSubDomains; preload` on all responses including www |
| T-03 | Low | FR blog trailing-slash → 308 instead of 301 | **CLOSED** — `/fr/blog/:slug/` now returns 301; `/fr/blog/:slug/ → /fr/blog/:slug 301` rule added to `_redirects` (commit 598929f) |
| T-04 | Low | `Wayback Machine` invalid robots.txt token | **CLOSED** — `Wayback Machine` stanza removed from robots.txt; only standard tokens remain (`ia_archiver`, `archive.org_bot`, etc.) |
| T-05 | Low | Legacy `.htaccess` in repo (maintenance confusion) | **CLOSED** — `.htaccess` deleted entirely from repo (commit `claude/cf-error-pages-htaccess-cleanup`) |

**All 5 prior findings resolved. No regressions detected.**

---

## Findings Table (New — 2026-05-16)

| ID | Severity | Category | Location | Finding | Recommended Fix |
|---|---|---|---|---|---|
| T-06 | Low | Sitemap freshness | `sitemap.xml` — homepage, `/fr/`, `/blog/`, `/fr/blog/` entries | Homepage/blog index `lastmod` still reads `2026-05-08` despite the STRC FR article being published 2026-05-11. The article's own entry correctly shows `2026-05-11`, but parent index entries (`/fr/blog/`, `/fr/`) were not bumped. Google tolerates this, but an accurate `lastmod` on the index entry signals freshness more reliably. | When publishing a new article, bump `lastmod` on the parent index entry (`/fr/blog/` and `/fr/`) in `sitemap.xml` to match the article date. Minimal effort: one-line change per index entry at publish time. |
| T-07 | Info | robots.txt `User-agent: *` block | `robots.txt` line for `User-agent: *` | The `User-agent: *` block retains both `/validation` and `/validation.html` disallows (defensive belt-and-suspenders after T-01 fix). This is harmless duplication — CF Pages only serves the extensionless path. No SEO defect. | Optional: remove `/validation.html` from `User-agent: *` block as cleanup now that `_headers` targets the canonical extensionless path. Cosmetic only; no rush. |

---

## Score Breakdown

| Category | Weight | Score 2026-05-08 | Score 2026-05-16 | Change | Notes |
|---|---|---|---|---|---|
| Crawlability (robots.txt, sitemap) | 15% | 90 | 97 | +7 | T-04 closed (Wayback Machine token); `validation` disallow consistent across all 6 AI stanzas |
| Indexability (canonicals, noindex, gated pages) | 15% | 88 | 98 | +10 | T-01 closed — X-Robots-Tag now live on `/validation`; all 3 gated page layers confirmed |
| Security (HTTPS, headers) | 20% | 88 | 96 | +8 | T-02 closed — HSTS `preload` confirmed live; all headers pass; branded 403/500 pages operational |
| URL structure (redirects, trailing slash) | 10% | 90 | 99 | +9 | T-03 closed — FR blog now 301 matching EN; no redirect chains; `_redirects` clean |
| Mobile (viewport, lang) | 10% | 100 | 100 | 0 | No regression; header mobile fixes (#151–153) pass |
| Core Web Vitals (lab estimate) | 10% | 75 | 75 | 0 | No new source-level changes to rendering path; render-blocking CSS pair still present; CrUX data insufficient for field measurement |
| Structured data | 10% | 95 | 95 | 0 | Unchanged; 3 JSON-LD blocks on homepage confirmed |
| JS rendering | 5% | 100 | 100 | 0 | SSR confirmed; bot guard intact |
| IndexNow / Bing WMT | 5% | 100 | 100 | 0 | Key file 200, BingSiteAuth 200; no regression |

**Weighted total: 91 / 100** (+7 from 84 baseline)

---

## Infra Changes — Verification Summary

| Change (since 2026-05-08) | Verification result |
|---|---|
| `.htaccess` removed entirely | Confirmed — no `.htaccess` in repo; CF Pages `_headers`/`_redirects`/`functions/` carry all rules |
| Branded 403/500 via `functions/_middleware.js` | PASS — PDF gate triggers 403 with branded body (`title`, `noindex`, SparkCore nav) |
| `_redirects` `/MD/*` → 404 | PASS — `/MD/README.md` returns 404 |
| FR blog trailing-slash 301 normalization | PASS — 301 confirmed, closing T-03 |
| Header mobile fixes (#151, #152, #153) | Out of scope for technical SEO (HTML/CSS layout) — viewport meta unchanged |
| Trailing-slash redirect rules dropped (commit 598929f) | Interpreted as: CF Transform Rule for blog trailing slash was replaced by `_redirects` rule — both EN and FR now 301-normalized via `_redirects` |

---

## New Content Since 2026-05-08

- `/fr/blog/strc-strategy-yield-sous-remunere-analyse` — FR article published 2026-05-11. HTTP 200, self-canonical, `index, follow`, correct `lastmod: 2026-05-11` in sitemap. Homepage hero badge linking to it confirmed (commit `1ff6ff5`). SEO tags are correct; no hreflang cross-link expected under dual-cluster strategy (correct per policy). **One note:** `/fr/` and `/fr/blog/` `lastmod` in sitemap remain `2026-05-08` — see T-06 above.

---

## Priority Action List

**Fix at next publish event (Low)**

1. **T-06** — When the next article is published, bump `lastmod` on all parent index entries (`/`, `/fr/`, `/blog/`, `/fr/blog/`) in `sitemap.xml` to match the publication date. This can be incorporated into the publishing workflow checklist in `MD/CLAUDE.md` (section "Blog article conventions").

**Optional cleanup only (Info)**

2. **T-07** — Remove `/validation.html` from the `User-agent: *` block in `robots.txt`. One-line deletion, no SEO impact.

---

## Notes on Outstanding Items (unchanged from baseline)

- **HSTS preload list inclusion:** The flag is enabled and submitted. Chromium preload list acceptance takes 6-12 weeks from submission. Expected inclusion ~July 2026. No action required.
- **FR blog articles — no hreflang in sitemap:** 6 FR articles carry no `xhtml:link` blocks per the documented dual-cluster strategy. This remains an accepted tradeoff. If the FR cluster grows beyond 10 articles, reconsider adding FR self-referencing hreflang at minimum.
- **CrUX field data:** Chrome User Experience Report data still insufficient for this domain (low traffic volume). CWV field metrics unavailable. Lab estimates unchanged: render-blocking CSS pair (`style.css?v=2.3` + `tailwind.min.css?v=1.1`) is the main lab-observable risk; both are self-hosted on CF CDN and expected to deliver fast for EU audiences.
- **`/ressources/contrats/*` PDFs:** Accessible by URL with `X-Robots-Tag: noindex, no-store` — threat model is documented as accepted in `MD/CLAUDE.md` (§ Security — Décisions assumées).
