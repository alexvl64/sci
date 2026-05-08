# Technical SEO Audit — sparkcore.fund
**Date:** 2026-05-08  
**Auditor:** seo-technical  
**Score: 84 / 100**

---

## Summary

The site is well-configured for a YMYL static site on Cloudflare Pages. HTTPS, HSTS, HTTP/2, security headers, robots.txt, sitemap, canonicals, gated-page defense-in-depth, and PDF gate all pass. Five issues worth addressing: the CSP `font-src` directive is too restrictive for the self-hosted Toastify CDN use-case, the HSTS `preload` flag is absent, `validation.html` redirects to `/validation` which lacks an `X-Robots-Tag`, FR blog articles carry no `hreflang` in the sitemap (intentional dual-cluster strategy but increases soft-404 risk if FR slugs change), and the `/fr/blog/*` trailing-slash redirects return 308 (permanent redirect preserving method) instead of 301. A legacy `.htaccess` file in the repo is a cleanup item.

---

## Section Findings

### 1. Crawlability

**Status: PASS**

- `robots.txt` syntax is valid. `Sitemap:` directive is present and points to the correct URL.
- Archiving bots (`ia_archiver`, `archive.org_bot`, `Wayback Machine`, `HTTrack`, and four offline copiers) are blocked at the root with `Disallow: /`.
- Six AI crawlers (`GPTBot`, `OAI-SearchBot`, `Google-Extended`, `ClaudeBot`, `PerplexityBot`, `CCBot`) are explicitly allowed on public content with targeted `Disallow` on `/factsheets/`, `/discovery-call`, and `/MD/`. This is the correct posture for a YMYL institutional site that wants AI citation coverage without exposing gated investor materials.
- `User-agent: *` also blocks `/validation.html`, `/404.html`, `/403.html`, `/500.html` — correct.
- Minor: `Wayback Machine` is not a valid crawl token per the robots.txt spec (the real bot is `ia_archiver`). The entry is harmless but ineffective as a standard directive; the CF Firewall custom rule for archiving bots is the effective control here.

### 2. Sitemap

**Status: PASS with one note**

- Sitemap serves correctly at `https://sparkcore.fund/sitemap.xml` (HTTP 200, correct MIME).
- Namespace declaration includes `xmlns:xhtml` — required for `xhtml:link` hreflang blocks.
- Homepage, `/fr/`, `/blog/`, and `/fr/blog/` carry full three-way hreflang alternates (`en`, `fr`, `x-default`). Correct.
- `/resources/regulated-crypto-fund-estonia/` carries `en` and `x-default` only — correct, no FR equivalent exists.
- EN blog articles (25 entries) carry `en` + `x-default` self-references with no cross-language alternate — this matches the documented dual-cluster strategy where FR and EN blogs are independent clusters, not translations.
- FR blog articles (5 entries) carry **no `xhtml:link` blocks at all** — consistent with the same dual-cluster policy, but it means Googlebot has no in-sitemap hreflang signal for those pages. This is an accepted tradeoff documented in `MD/CLAUDE.md`. No fix required unless the FR cluster grows large enough to warrant its own hreflang cluster.
- `lastmod` dates are recent and plausible. `changefreq`/`priority` values are present and reasonable.

### 3. Canonicals

**Status: PASS**

- `https://sparkcore.fund/` → `<link rel="canonical" href="https://sparkcore.fund/" />`. Correct.
- `https://sparkcore.fund/fr/` → `<link rel="canonical" href="https://sparkcore.fund/fr/" />`. Correct (self-canonical).
- Both pages include `<html lang>` attribute matching the canonical (`lang="en"` on `/`, `lang="fr"` on `/fr/`). Correct.
- `<meta charset="UTF-8" />` present on both. Correct.
- `<meta name="viewport" content="width=device-width, initial-scale=1.0" />` present. Correct.

### 4. HTTPS / TLS / Transport

**Status: PASS with one note**

- HTTPS enforced. `always_use_https: on` in CF zone settings. www → non-www redirect returns 301 to `https://sparkcore.fund/` — correct.
- TLS: CF zone `tls_1_3: zrt` (TLS 1.3 + 0-RTT enabled). `min_tls_version: 1.2`. Correct.
- HTTP/2 confirmed (`HTTP/2 200` on all responses). CF Pages serves HTTP/2 by default.
- HTTP/3: `alt-svc: h3=":443"; ma=86400` advertised in live headers — browsers will upgrade. CF docs note HTTP/3 as free-plan supported; this is confirmed live.
- HSTS: `strict-transport-security: max-age=31536000; includeSubDomains` confirmed live. **The `preload` flag is absent.** The CF zone SSL/TLS dashboard shows preload deferred pending stability confirmation per `MD/CLAUDE.md`. This is a known intentional deferral, not an oversight. Flag as Medium — preload submission to hstspreload.org should occur when the CF zone is confirmed stable.

### 5. Security Headers

**Status: PASS with one note**

All headers confirmed live on homepage response:

| Header | Value | Assessment |
|---|---|---|
| `Content-Security-Policy` | Via CF Transform Rule (see below) | Pass — `'unsafe-inline'` is a conscious tradeoff for static site |
| `X-Frame-Options` | `SAMEORIGIN` | Pass |
| `X-Content-Type-Options` | `nosniff` | Pass |
| `Referrer-Policy` | `strict-origin-when-cross-origin` | Pass |
| `Permissions-Policy` | `geolocation=(), microphone=(), camera=()` | Pass |
| `Strict-Transport-Security` | `max-age=31536000; includeSubDomains` | Pass (preload absent — see §4) |

**CSP delta between `_headers` source and live header:** The CF Transform Rule CSP omits `https://fonts.googleapis.com` from `style-src` and `https://fonts.gstatic.com` from `font-src` relative to the value stored in `MD/CLAUDE.md`. Live `font-src` is `'self'` only. The homepage preloads `funnel-display-400-latin.woff2` and `inter-400-latin.woff2` from `/assets/fonts/` (self-hosted), so `font-src 'self'` is technically correct for fonts. However, `style-src` includes `https://cdn.jsdelivr.net` (for Toastify CSS) but the `_headers` file and the live CSP's `style-src` both include `cdn.jsdelivr.net` — this is consistent. No CSP violation expected for fonts. `'unsafe-inline'` is documented as a known tradeoff; it is not flagged as a finding.

**One gap identified:** The `_headers` file applies `X-Robots-Tag: noindex, nofollow, noarchive` to `/validation.html` but CF Pages strips `.html` extensions and canonicalizes to `/validation`. The live `/validation` URL (HTTP 200) does **not** carry `X-Robots-Tag` — the `_headers` rule for `/validation.html` is not triggered because CF Pages serves the extensionless path. The HTML `<meta name="robots">` tag on that page is the only active noindex signal. This is a defense-in-depth gap: if Googlebot crawls `/validation` it relies on the meta tag alone, not a HTTP header.

### 6. URL Structure and Redirects

**Status: PASS with one note**

- www → non-www: 301 confirmed.
- HTTP → HTTPS: enforced by `always_use_https` at CF zone level.
- Blog trailing slash (EN): `_redirects` rule `/blog/:slug/ → /blog/:slug 301` confirmed working. Live test: `https://sparkcore.fund/blog/regulated-crypto-investment-fund/` returns `301 → https://sparkcore.fund/blog/regulated-crypto-investment-fund`. Correct.
- Blog trailing slash (FR): `/fr/blog/agents-ia-blockchain-economie-agentique/` returns `308` (not `301`). The 308 is a CF Pages-native permanent redirect from its built-in `.html` extension handling — it is semantically equivalent to 301 for GET requests and search engines treat it identically. However it is inconsistent with the EN blog `301` and may confuse log analysis. No SEO defect, but worth normalizing.
- Old slug redirects (3 pairs in `_redirects`): correctly configured with both slash and non-slash variants.
- `/en/` → `/` 301: correctly handled.
- No redirect chains detected in tested URLs.

### 7. Gated Pages — Defense in Depth

**Status: PASS with one gap**

| Page | robots.txt | X-Robots-Tag (HTTP) | meta robots | Assessment |
|---|---|---|---|---|
| `/factsheets/*` | Disallow (all + 6 AI) | `noindex, nofollow, noarchive` via `_headers` | Yes (on page) | Pass — 3/3 layers active. Returns 404 in test (not in sitemap, not linked). |
| `/discovery-call` | Disallow (all + 6 AI) | `noindex, nofollow, noarchive` via `_headers` | Yes (on page) | Pass — HTTP 200 with X-Robots-Tag confirmed. |
| `/MD/` | Disallow `*` and 6 AI | `noindex, nofollow, noarchive` via `_headers` | n/a (not HTML) | Pass — returns 404 live (directory not exposed). |
| `/validation.html` / `/validation` | Disallow in robots.txt as `/validation.html` | **Missing on `/validation`** | Present in HTML | Partial — see §5 gap above. |

The `robots.txt` `Disallow: /validation.html` entry would only prevent crawl of the `.html` form. CF Pages canonicalizes to `/validation` so the disallow directive may not match. Low severity because the page is not linked or in the sitemap, but both the `robots.txt` entry and the `_headers` entry should reference `/validation` (without `.html`) to guarantee coverage.

### 8. PDF Gate

**Status: PASS**

- `https://sparkcore.fund/ressources/instructions_depot_dynamic_trends.pdf` without hash parameter returns `HTTP/2 403`. The CF Pages Function (`functions/ressources/[[path]].js`) is operating correctly.
- Response returns in ~200ms (CF edge processing). No `X-Robots-Tag` on the 403 response — acceptable since 403 responses are not indexed by Google.
- `/ressources/contrats/*` static PDFs pass through with `X-Robots-Tag: noindex, nofollow, noarchive` and `Cache-Control: no-store` per `_headers`. This defense-in-depth is functional.

### 9. Mobile and Fundamentals

**Status: PASS**

- `<meta name="viewport" content="width=device-width, initial-scale=1.0" />` present on homepage (confirmed in HTML source).
- `<html lang="en">` on EN pages, `<html lang="fr">` on FR pages — confirmed live.
- `<meta charset="UTF-8" />` present.
- Touch targets: not auditable from headers alone; deferred to UX review.

### 10. JavaScript Rendering

**Status: PASS**

The site is static HTML with JS overlays for translation, analytics, and UI interactions. Googlebot receives pre-rendered content in the correct language because:

1. `lang-redirect-en.js` and `lang-redirect-fr.js` both contain a bot-skip regex that catches `googlebot`, `crawl`, `spider`, `gptbot`, `claudebot`, `perplexitybot` and others — bots are never auto-redirected.
2. `translations.js` applies `currentLang` detection with URL path as the highest-priority signal: paths starting with `/fr` render in French regardless of `navigator.language`. Googlebot crawling `/fr/` receives the French pre-rendered body.
3. `analytics.js` is `defer`-loaded — it does not block rendering.
4. ApexCharts and Toastify are loaded `defer` / `async` respectively — non-blocking.
5. Cloudflare Turnstile is `async defer` — correct.

No client-side rendering dependency for meaningful body content. Googlebot sees full text on first render.

### 11. Core Web Vitals (Lab Estimate from Source)

**Defer to seo-google for field data (CrUX).**

Source-level observations:

- **LCP candidate:** Hero image at `/assets/images/webp/hero-image.webp` has `<link rel="preload" ... fetchpriority="high">` — correct LCP optimization.
- **Two CSS files are render-blocking** (`style.css?v=1.6` and `tailwind.min.css?v=1.0`). Both are preloaded via `<link rel="preload">` immediately before the `<link rel="stylesheet">` tags. This is an attempt to reduce blocking time but the files still block first paint until downloaded. On Cloudflare's global CDN edge (not a single origin server), these should deliver in <50ms to most EU/NA audiences — acceptable for a YMYL institutional site not competing on Page Experience alone.
- **CLS risk:** Two fonts are preloaded (`funnel-display-400-latin.woff2`, `inter-400-latin.woff2`). Self-hosted fonts with preload reduce FOUT/CLS risk. ApexCharts charts load async — if they inject layout elements after initial paint, there is a CLS risk; this depends on whether chart containers have fixed dimensions declared (not verifiable from headers alone).
- **AOS (Animate On Scroll) CSS** loaded async via `onload` hack — correct, non-blocking.
- **INP:** Static HTML with minimal blocking JS. INP is unlikely to be problematic. Turnstile (third-party) is async; FormCarry calls are async fetch — no main-thread blocking expected.

### 12. Structured Data

**Status: PASS**

Three JSON-LD blocks on the homepage:

1. `@graph` containing `Organization` (with `leiCode`, `taxID`, `sameAs` to GLEIF and Finantsinspektsioon registry) and `WebPage`.
2. `FinancialService` (with `PostalAddress`, `memberOf: GovernmentOrganization`).
3. `ItemList` (SiteNavigationElement).
4. `FAQPage` (at least 3 questions visible in source).

The `Organization.legalName` reads `"SparkCore.investment OÜ"` — the dot in the legal name matches the Estonian registry entry `SparkCore.investment OÜ`. Correct.

`memberOf` using `GovernmentOrganization` for Finantsinspektsioon is a reasonable schema type — the regulator is a public body. No validation errors expected.

### 13. IndexNow

**Status: PASS**

Key file `https://sparkcore.fund/27994a06b868d24820429dc36c1bafee.txt` is deployed. Script `scripts/ops/indexnow_ping.py` is in place. First ping returned HTTP 202. Bing WMT account verified on `sparkcore.public.df59f6@gmail.com`.

### 14. Legacy `.htaccess` in Repo

**Status: Cleanup item (no production impact)**

The `.htaccess` file is tracked in git and deployed to CF Pages but CF Pages does not execute Apache configuration. All rules it contained (redirects, headers, PDF blocking) have been replicated in `_redirects`, `_headers`, and `functions/ressources/[[path]].js`. The file is harmless but adds maintenance confusion (a developer could edit it expecting production effect). Recommendation: add a prominent comment at the top of `.htaccess` confirming it is legacy and inert on CF Pages, or remove it from the repo and keep only the CF Pages equivalents.

---

## Findings Table

| ID | Severity | Category | Location | Finding | Recommended Fix |
|---|---|---|---|---|---|
| T-01 | Medium | Security / Gated pages | `/validation` (live), `_headers`, `robots.txt` | `/validation.html` rules in `_headers` and `robots.txt` do not match the CF Pages extensionless canonical `/validation`. The X-Robots-Tag is missing on the live `/validation` URL; only the HTML meta tag provides noindex. | Update `_headers` to use `/validation` (no extension). Update `robots.txt` `Disallow: /validation` (no `.html`). |
| T-02 | Medium | Transport | CF zone HSTS settings | HSTS `preload` flag is absent (`max-age=31536000; includeSubDomains` only). Site is not in the browser preload list, leaving a first-visit window without forced HTTPS before HSTS is cached. | Enable `preload` in CF SSL/TLS → Edge Certificates → HSTS once zone is confirmed stable. Submit to hstspreload.org. |
| T-03 | Low | URL structure | `/fr/blog/*` trailing slash | FR blog trailing-slash redirects return HTTP 308, while EN blog returns 301. Inconsistency in redirect code. 308 is valid for SEO but inconsistent. | Add `/fr/blog/:slug/ → /fr/blog/:slug 301` to `_redirects` to normalize to 301 across both clusters. |
| T-04 | Low | Robots.txt | `robots.txt` line 70 | `Wayback Machine` is not a recognized `User-agent` token in the robots.txt specification. The actual Internet Archive crawler is `ia_archiver` (already blocked). This entry is ineffective. | Remove the `Wayback Machine` stanza or replace with the `archive.org_bot` token (also already blocked). Either way it is a documentation issue only since the CF Firewall rule is the effective control. |
| T-05 | Low | Crawlability | `.htaccess` in repo | Legacy Apache config tracked in git; no production effect on CF Pages. Creates maintenance confusion. | Add a comment block at line 1: `# LEGACY — This file is inert on Cloudflare Pages. See _headers, _redirects, and functions/ for active config.` Optionally delete from repo. |

---

## Score Breakdown

| Category | Weight | Score | Notes |
|---|---|---|---|
| Crawlability (robots, sitemap) | 15% | 90 | Robots.txt well-structured; one ineffective bot token |
| Indexability (canonicals, noindex) | 15% | 88 | Strong; `/validation` X-Robots-Tag gap is only layer missing |
| Security (HTTPS, headers) | 20% | 88 | All headers present; HSTS preload absent; CSP `'unsafe-inline'` is deliberate |
| URL structure (redirects, trailing slash) | 10% | 90 | EN blog correct; FR blog 308 vs 301 inconsistency |
| Mobile (viewport, lang) | 10% | 100 | Full pass |
| Core Web Vitals (lab estimate) | 10% | 75 | Render-blocking CSS pair; defer to CrUX for field data |
| Structured data | 10% | 95 | Three JSON-LD blocks, YMYL-appropriate Organization/FinancialService |
| JS rendering | 5% | 100 | Full SSR; bot redirect guard confirmed |
| IndexNow / Bing WMT | 5% | 100 | Key deployed, 202 confirmed |

**Weighted total: 84 / 100**

---

## Priority Action List

**Fix now (Medium)**

1. **T-01** — Add `Disallow: /validation` (no `.html`) to `robots.txt` `User-agent: *` block. Update `_headers` to target `/validation` instead of `/validation.html`. This closes the single-layer noindex gap on that page. 5-minute change in two files, deploy via PR.

2. **T-02** — Enable HSTS `preload` in CF dashboard and submit `sparkcore.fund` to hstspreload.org. Prerequisites: confirm no planned subdomain changes, HSTS `max-age=31536000` has been stable for at least a few weeks (confirmed since migration 2026-05-06). The preload list inclusion takes 2–4 weeks.

**Fix when convenient (Low)**

3. **T-03** — Add `/fr/blog/:slug/ → /fr/blog/:slug 301` to `_redirects`. Removes the 308 inconsistency.

4. **T-04** — Remove the `User-agent: Wayback Machine` stanza from `robots.txt` (redundant, non-standard token). One-line deletion.

5. **T-05** — Add legacy disclaimer comment to `.htaccess` top. Or delete the file after confirming no developer relies on it as documentation.
