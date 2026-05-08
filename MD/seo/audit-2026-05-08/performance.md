# Core Web Vitals & Performance Audit — sparkcore.fund
**Date:** 2026-05-08 | **Lab data only — CrUX N/A** (insufficient Chrome traffic, expected for new institutional site)

---

## Lab CWV Estimates

| Metric | Estimate | Status | Rationale |
|--------|----------|--------|-----------|
| **LCP** | ~2.2–2.8 s | Needs Improvement (borderline) | 2 render-blocking CSS files (~34 KB compressed) must fully parse before paint; hero image preloaded + `fetchpriority=high` but blocked by CSS chain. Cloudflare edge reduces TTFB to ~80–120 ms. |
| **INP** | ~80–140 ms | Good | Vanilla JS only; no heavy frameworks; main JS bundle totals ~66 KB compressed. No synchronous XHR. ApexCharts (529 KB uncompressed) is `defer`'d so it cannot block interaction on load. |
| **CLS** | ~0.02–0.05 | Good | Hero `width`/`height` set (1440×1600). Logo, sidebar images, all below-fold images carry explicit dimensions. Fonts are preloaded. AOS and Toastify CSS load async (preload swap pattern). No injected banners or ads. |

---

## Resource Breakdown

| Resource | Transfer size | Notes |
|----------|--------------|-------|
| `style.css?v=1.6` | 4.4 KB (Brotli) | Render-blocking — `<link rel="stylesheet">` in `<head>` |
| `tailwind.min.css?v=1.0` | 29.5 KB (already minified, single line) | Render-blocking — `<link rel="stylesheet">` in `<head>`. Not Brotli-encoded at edge (served as-is). Purged? Appears purged (29 KB is reasonable for a real-world Tailwind build). |
| `aos.min.css` | CDN async | Correctly async via preload swap |
| `toastify.min.css` | CDN async | Correctly async via preload swap |
| `hero-image.webp` | 106 KB | Preloaded + `fetchpriority=high` + `loading="eager"` + srcset (480/768/1440w) ✅ |
| `hero-graph-img.webp` | 112 KB (desktop) / 48 KB (768w) | No `loading="lazy"` — above-fold on desktop, partially above-fold on mobile. Missing `fetchpriority` or `lazy`. |
| `hero-image.webp` (preload target) | 106 KB | Preload declared for 1440w; no `imagesizes`/`imagesrcset` on the `<link rel="preload">` — browser may preload wrong size on mobile |
| `funnel-display-400-latin.woff2` | 17.7 KB | Preloaded ✅ |
| `inter-400-latin.woff2` | 48.3 KB | Preloaded ✅ |
| `lang-redirect-en.js` | 1.5 KB | **Blocking — first `<script>` in `<body>`, no `defer`/`async`** — causes parser block on every page load |
| `translations.js` | 26 KB | End-of-body, no `defer` — parser-blocking at `</body>` |
| `aos.min.js` | 14 KB | End-of-body, no `defer` |
| `main.js` | 3.7 KB | End-of-body, no `defer` |
| `index.js?v=2.6` | 14.7 KB | End-of-body, no `defer` |
| `toastify-js` (jsdelivr) | 6.8 KB | End-of-body, no `defer` — CDN round-trip adds latency |
| `apexcharts` (jsdelivr) | 529 KB uncompressed | `defer` ✅ — does not block first paint |
| `analytics.js` | 7.5 KB | `defer` ✅ |
| Cronitor RUM script | 187 B | `async` ✅ |
| Turnstile (Cloudflare) | CDN | `async defer` ✅ |
| Cal.com inline init | ~350 B inline | Inline `<script>` at bottom — no `defer`, triggers `app.cal.eu/embed/embed.js` download |

**Total estimated render-blocking CSS (compressed):** ~34 KB  
**Total body JS without defer (end-of-body):** ~66 KB (5 scripts parsed sequentially before `DOMContentLoaded`)

---

## Cloudflare Infrastructure — Confirmed Good

| Setting | Value | Impact |
|---------|-------|--------|
| HTTP/2 | On | Multiplexed requests |
| Brotli | On | Compression on text assets |
| TLS 1.3 + 0-RTT | On (`zrt`) | Reduced handshake latency |
| Browser Cache TTL | 31 536 000 s (1 year) | Versioned assets (`?v=`) cached long-term |
| Early Hints | On | Preconnect/preload pushed before full response |
| HSTS | 12 months + subdomains | No HTTP redirect overhead for returning visitors |
| HTML Cache-Control | `max-age=0, must-revalidate` | HTML always revalidated — correct for a CF Pages site |

Note: CF free plan shows `cf-cache-status: DYNAMIC` for HTML — this is expected. Static assets (CSS/JS/images) served from CF edge with 1-year TTL.

---

## Findings Table

| Severity | Location | Finding | Fix |
|----------|----------|---------|-----|
| HIGH | `<head>` lines 48–49 | `style.css` + `tailwind.min.css` are both `rel="stylesheet"` — render-blocking. ~34 KB CSS blocks first paint. Preload tags on lines 43–44 help download speed but the blocking `<link rel="stylesheet">` still holds the render tree. | Extract ~5–8 KB of above-fold critical CSS inline; load both files async (preload swap pattern already used for AOS/Toastify — apply same pattern here). |
| HIGH | `<body>` line 229 | `lang-redirect-en.js` loaded as first `<script>` in `<body>` with no `async` or `defer` — **fully parser-blocking** on every pageview. Only needed for FR-browser users (~20–30% of audience). | Add `defer` (redirect logic runs after DOM parse; `sessionStorage` guard means it fires once). |
| MEDIUM | `<head>` line 47 | Hero image preload `<link rel="preload" as="image" href="/assets/images/webp/hero-image.webp">` lacks `imagesrcset` and `imagesizes` attributes. Browser always preloads the 1440w version even on mobile, wasting ~60–70 KB on 480w screens. | Add `imagesrcset` and `imagesizes` matching the `<img srcset>` below: `imagesrcset="/assets/images/webp/hero-image-480.webp 480w, /assets/images/webp/hero-image-768.webp 768w, /assets/images/webp/hero-image.webp 1440w" imagesizes="(max-width: 480px) 480px, (max-width: 768px) 768px, 1440px"` |
| MEDIUM | `<body>` lines 504–509 | `hero-graph-img.webp` (112 KB desktop) is in the hero section with no `loading="lazy"` — browser fetches it eagerly even though it is a decorative background element. No `fetchpriority="low"` either. | Add `loading="lazy"` or `fetchpriority="low"` since `hero-image.webp` (the actual LCP element) already has `fetchpriority="high"`. |
| MEDIUM | `<body>` lines 1471–1475 | `translations.js` (26 KB), `aos.min.js` (14 KB), `main.js` (3.7 KB), `index.js` (14.7 KB), `toastify-js` (6.8 KB) — 5 scripts at end of `<body>` with no `defer`. While end-of-body position means HTML is already parsed, these scripts still block `DOMContentLoaded` and delay interactivity. The CDN round-trip for `toastify-js` adds extra latency. | Add `defer` to all 5. `DOMContentLoaded` will fire sooner, improving TTI. Bundle local scripts (`translations.js` + `main.js` + `index.js`) into one file to eliminate 2 HTTP round-trips. |
| MEDIUM | `<body>` line 47 | Only 2 font weights preloaded (`funnel-display-400` + `inter-400`). If bold/medium variants are used in above-fold text (e.g. hero `<h1>` or nav button), the missing weight triggers FOUT. | Audit which font weights render in the first viewport. Add preload for any additional weight used above fold. |
| LOW | `tailwind.min.css` | Not Brotli-compressed at the Cloudflare edge layer (no `content-encoding: br` header seen on this file). Delivered as 29.5 KB raw; Brotli would reduce to ~7–9 KB. | Verify CF Brotli setting applies to `.css` files served from CF Pages. CF Brotli should auto-compress; if not firing, check if the file is already pre-compressed (`.br` extension) or served with wrong `Content-Type`. |
| LOW | `<body>` line 1477 | Cal.com inline `<script>` at bottom injects `app.cal.eu/embed/embed.js` immediately — no lazy-loading condition. If the discovery-call CTA is below-fold (it is), the embed download could be deferred until user scrolls near the CTA. | Wrap the Cal init in an Intersection Observer or scroll-intent trigger, similar to the GTM lazy pattern used on dsungkur. |
| INFO | CSP header | `font-src 'self'` — correct since fonts are self-hosted. However `style-src` includes `'unsafe-inline'`; noted as accepted trade-off for a static site without Workers. | No action required (documented decision). |

---

## Performance Sub-score

**62 / 100**

Breakdown:
- Cloudflare infra: excellent (HTTP/2, Brotli, 0-RTT, 1-year cache) — no points lost here
- LCP path: render-blocking CSS is the primary bottleneck; hero image itself is well-optimised
- INP: good — vanilla JS, no heavy synchronous work
- CLS: good — explicit dimensions throughout, async non-critical CSS
- JS loading discipline: 5 body scripts missing `defer`, 1 blocking in-body script

---

## Top 3 Quick Wins

**1. Add `defer` to `lang-redirect-en.js` (30 min, HIGH impact)**
This single-file change eliminates a parser block on every pageview. The redirect logic uses `sessionStorage` + `navigator.language` — both available post-parse. Expected LCP improvement: 100–200 ms on mobile.

**2. Load render-blocking CSS async using the preload swap pattern (2–4 h, HIGH impact)**
`style.css` and `tailwind.min.css` already have `<link rel="preload">` — add `onload="this.onload=null;this.rel='stylesheet'"` and a `<noscript>` fallback (same pattern as AOS/Toastify, already in place). Extract ~5–8 KB of above-fold critical CSS inline. Expected LCP improvement: 300–600 ms. Caveat: requires careful above-fold CSS extraction to avoid FOUC.

**3. Fix hero image preload to include `imagesrcset`/`imagesizes` (15 min, MEDIUM impact)**
Replace `<link rel="preload" as="image" href="/assets/images/webp/hero-image.webp" fetchpriority="high">` with:
```html
<link rel="preload" as="image"
  href="/assets/images/webp/hero-image.webp"
  imagesrcset="/assets/images/webp/hero-image-480.webp 480w,
               /assets/images/webp/hero-image-768.webp 768w,
               /assets/images/webp/hero-image.webp 1440w"
  imagesizes="(max-width: 480px) 480px, (max-width: 768px) 768px, 1440px"
  fetchpriority="high">
```
Saves 60–70 KB on mobile (480w) and ensures the correct image is preloaded per viewport width.

---

## Notes

- **CrUX field data unavailable** — sparkcore.fund has insufficient Chrome user traffic. Lab estimates above are directional; validate with Lighthouse CLI once stable traffic accumulates.
- **ApexCharts (529 KB uncompressed, `defer`)** — correctly loaded but large. If charts are only used on one page section, consider dynamic `import()` triggered on IntersectionObserver instead of site-wide `defer`.
- **Cloudflare Brotli on `tailwind.min.css`** — the asset is served without `content-encoding: br`. Worth verifying; if CF Pages is not compressing it on the fly, re-saving the file or adding a `.br` pre-compressed variant could cut 20+ KB from the render-blocking payload.
