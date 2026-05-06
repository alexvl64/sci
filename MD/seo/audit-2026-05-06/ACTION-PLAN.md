# SparkCore — SEO Action Plan (2026-05-06)

**Source audit:** `FULL-AUDIT-REPORT.md` (66 / 100 — C+)
**Sequence priority:** P0 (this week) → P1 (this month) → P2 (next quarter)
**Working assumption:** per user feedback in memory, **major refactors deliver roadmap MD + PR first**, wait for go before coding. Items below marked 🛠 *propose-then-implement* should be turned into discrete PRs against `beta` (preview on `beta.sparkcore.fund`) and merged to `main` only after sign-off.

> **Migration context:** Cloudflare Pages migration completed 2026-05-06 (today). The single most valuable action is to resubmit the sitemap so Google can re-discover the site under the new host. That + `IndexNow` ping covers Google + Bing + Yandex + Seznam in one pass.

---

## P0 — Do this week (≤ 30 min each, high leverage)

### P0-1 · Resubmit sitemap to GSC + IndexNow ping

**Effort:** 5 min
**Impact:** Forces Google to re-evaluate sitemap post-migration. Currently 0/26 indexed despite 2 homepages confirmed indexed.

**Steps:**
1. GSC → Sitemaps → resubmit `https://sparkcore.fund/sitemap.xml`
2. From repo root:
   ```bash
   ~/.config/claude-seo/switch.sh sci
   cd ~/Documents/Claude/github-projets/sci
   python3 scripts/ops/indexnow_ping.py --all
   ```
3. Verify Bing WMT shows the sitemap as "successful" (already submitted, just confirm).

**Success metric:** GSC sitemap status moves from `0 indexed / 26 submitted` to ≥ 5 indexed within 14 days.

---

### P0-2 · URL Inspection → Request Indexing on 5 priority blog articles

**Effort:** 15 min
**Impact:** Bypasses crawl-budget delay for the most commercially valuable articles.

**Pages to request:**
1. `https://sparkcore.fund/blog/regulated-crypto-fund-manager-estonia` (currently P12 for `finantsinspektsioon licence` — quickest path to first non-brand click)
2. `https://sparkcore.fund/blog/sub-threshold-aifm-crypto-estonia` (highest GEO citability score, 88/100)
3. `https://sparkcore.fund/blog/why-invest-in-crypto-funds-2026` (top-of-funnel, broad query intent)
4. `https://sparkcore.fund/blog/white-label-crypto-fund-manager-services` (commercial — internal link hub)
5. `https://sparkcore.fund/blog/` (the blog index itself)

**Success metric:** All 5 transition from `URL is unknown to Google` to `Submitted and indexed` within 14 days.

---

### ~~P0-3 · Fix canonical leak on `estonia-eresidency-crypto-fund-eu`~~ — **CANCELLED (false positive)**

The seo-cluster agent reported a third-party canonical leak on this article. **Manually verified 2026-05-06: false positive.** All 31 canonicals across the site (22 EN articles + 5 FR + 2 indexes + 2 homepages) self-reference `sparkcore.fund` correctly. No remediation needed.

The remaining noindex articles (`cost-to-launch-regulated-crypto-fund-europe`, `crypto-fund-fees-2026`, `estonia-eresidency-crypto-fund-eu`) all self-canonicalise — verified with:

```bash
grep -EH 'rel="canonical"' ~/Documents/Claude/github-projets/sci/blog/*.html | grep -v "sparkcore.fund"
# (empty result = no leak)
```

---

### P0-4 · Fix 4 empty `alt` attributes on FR homepage Steps-to-invest icons

**Effort:** 5 min
**Impact:** WCAG 1.1.1 compliance + parity with EN page. Both legal (EU Accessibility Act, EN 301 549) and brand-trust signal for institutional investors.

**File:** `/home/alex/Documents/Claude/github-projets/sci/fr/index.html`
**Lines:** 998, 1016, 1034, 1052
**Action:** Copy the 4 alt strings from the matching EN icons in `/home/alex/Documents/Claude/github-projets/sci/index.html` and translate to FR (or use FR equivalents already in `translations.js`).

---

### P0-5 · Add hreflang `<xhtml:link>` to 23 missing sitemap entries + remove FR-only `x-default`

**Effort:** 30 min (mostly mechanical sitemap edit)
**Impact:** Hreflang sub-score 32 → 75. Reduces Google's effort to validate language relationships.

**File:** `/home/alex/Documents/Claude/github-projets/sci/sitemap.xml`

**Two distinct fixes:**

**Fix A — EN articles (19 URLs):** Add 2 self-referencing alternates per `<url>` block:
```xml
<xhtml:link rel="alternate" hreflang="en" href="https://sparkcore.fund/blog/<slug>"/>
<xhtml:link rel="alternate" hreflang="x-default" href="https://sparkcore.fund/blog/<slug>"/>
```

**Fix B — FR-only articles (4 URLs):** Choose one approach. **Recommended (Option B from `seo-hreflang.md`):** remove all `hreflang` declarations from the 4 FR-only HTML files entirely, and rely on `lang="fr"` HTML attribute. No sitemap alternates needed.

**Affected FR HTML files** (remove `hreflang` block from `<head>`):
- `/fr/blog/agents-ia-blockchain-economie-agentique.html`
- `/fr/blog/indicateurs-marche-crypto-actifs.html`
- `/fr/blog/le-vrai-cout-du-market-timing.html`
- `/fr/blog/strategies-options-protection-portefeuille-actions.html`

**Success metric:** `grep -c "x-default" sitemap.xml` returns the right count (matched pairs only). `seo-hreflang` re-run shows score ≥ 75.

---

### P0-6 · Add LEI + foundingDate + Person founders + YouTube to JSON-LD

**Effort:** 30 min
**Impact:** Knowledge Panel eligibility + AI citation strength + GEO 71→78. The LEI is the machine-verifiable entity anchor for YMYL financial — its absence from JSON-LD is a notable gap.

**Files:** `/home/alex/Documents/Claude/github-projets/sci/index.html` and `/home/alex/Documents/Claude/github-projets/sci/fr/index.html`

**Patch the `Organization` (or `FinancialService`) JSON-LD block to include:**
```json
"leiCode": "8945003BBN0RVNNB0S84",
"foundingDate": "2024-XX-XX",
"sameAs": [
  "https://www.linkedin.com/company/sparkcore-fund-management/",
  "https://www.youtube.com/@cointips",
  "https://search.gleif.org/#/record/8945003BBN0RVNNB0S84",
  "https://www.fi.ee/en/guides/fund-management-companies/investment-market/small-fund-managers-without-activity-licence/sparkcoreinvestment-ou"
],
"founder": [
  { "@type": "Person", "name": "Paul-Antoine PONS", "jobTitle": "Managing Partner", "sameAs": "https://www.linkedin.com/in/paul-antoine-pons-523aa919a/" },
  { "@type": "Person", "name": "Olivier SAYEGH", "jobTitle": "Managing Partner", "sameAs": "https://www.linkedin.com/in/olivier-sayegh-5b89b3135/" },
  { "@type": "Person", "name": "Alexandre VINAL", "jobTitle": "Managing Partner", "sameAs": ["https://www.linkedin.com/in/alexandrevinal/", "https://www.youtube.com/@cointips"] }
]
```

Confirm exact `foundingDate` from Estonian registry (16265864 — likely 2019 per CLAUDE.md root mention "founded 2019").

---

### P0-7 · Add LEI + dateModified to llms.txt

**Effort:** 5 min
**Impact:** AI citation strength. LEI is the machine-verifiable entity anchor.

**File:** `/home/alex/Documents/Claude/github-projets/sci/llms.txt`
**Action:**
- In the "Regulatory Structure" section, add a line: `- LEI: 8945003BBN0RVNNB0S84 — https://search.gleif.org/#/record/8945003BBN0RVNNB0S84`
- Add a `> Last updated: 2026-05-06` line near the H1
- (Optional) Add `(Published: YYYY-MM-DD)` per article in `llms-full.txt`

---

### ~~P0-8 · Configure Cloudflare zone settings~~ — **ALREADY APPLIED (verified via API 2026-05-06)**

`MD/CLAUDE.md` was stale — the 4 toggles flagged as needing change are already ON in production.

API check (read via `cloudflare_api_token` in `~/.config/claude-seo/projects/sci.json`, force IPv4 due to IP restriction):

| Setting | CLAUDE.md doc | Live state | Note |
|---|---|---|---|
| `always_use_https` | OFF ⚠ | **on** | Done |
| `min_tls_version` | 1.0 ⚠ | **1.2** | Done |
| `0rtt` | OFF | **on** | Done |
| `early_hints` | OFF | **on** | Done |
| `tls_1_3` | on | **zrt** | "zrt" = TLS 1.3 + 0-RTT (better than plain `on`) |
| `ssl` | strict | strict | Already optimal |
| `http3`, `brotli`, `browser_cache_ttl` | on | on | Already optimal |

The CLAUDE.md zone-settings section has been updated in the same PR to reflect live state.

Optional cleanup still standing: delete the legacy "sitemap.xml cache bypass" Page Rule (cosmetic, no impact). Requires a write-scoped CF API token or manual action via the dashboard.

---

## P1 — Do this month (≤ 1 day each)

### P1-A · Performance Sprint (target: mobile LCP < 2,500 ms on home)

**Effort:** 2-4 days (dev work)
**Impact:** Mobile perf 55 → 80+. Pushes site closer to CrUX eligibility threshold.

**🛠 Propose-then-implement** — open as PR against `beta` first, validate on `beta.sparkcore.fund`.

#### A-1: Self-host Google Fonts (eliminate 751 ms render-block)
Move `Gotham_Book` / `Gotham_Medium` / `ProximaNova_Regular` / `ProximaNova_Bold` from `fonts.googleapis.com` to `/assets/fonts/` with `<link rel="preload" as="font" type="font/woff2" crossorigin>` for the critical 2 fonts. Update `fonts.googleapis.com` references in `<head>` of `index.html`, `fr/index.html`, all blog templates.

#### A-2: Inline critical CSS, defer non-critical Tailwind (459 ms)
Use `lightningcss-cli` (already devDep on dsungkur sister project — pattern-replicable) to extract above-the-fold CSS, inline in `<head>`, async-load remainder.

#### A-3: Defer gtag.js until after LCP element (~273 ms main-thread reduction)
Currently `analytics.js` is `<script defer>` — but `defer` still parses in the critical path. Use a `requestIdleCallback` pattern (e.g., the `gtm-lazy.js` pattern proven on dsungkur) — wait for first user intent or 3s idle, then load gtag.js. Keep `dataLayer` shim active.

#### A-4: Image fixes (per `raw/seo-images.md`)
- Switch 3 oversized JPGs to existing WebP twins on disk (mica-casp-hero, iran-macro-shock, panic-seller — combined ~700 KB savings)
- Add `srcset`/`sizes` to FR homepage hero (parity with EN — likely the biggest single win on the FR mobile gap)
- Replace `loading="lazy"` with `fetchpriority="high"` on the 11 EN blog hero images
- Replace generic alts (`hero image`, `graph image`, etc.) with descriptive content-aware alts

#### A-5: Wrap `onScroll`/forced-reflow JS in `requestAnimationFrame`
Per PSI diagnostic on blog article. Find the JS reading layout after DOM mutation (likely in `index.js` or `analytics.js`), wrap in `rAF`.

#### A-6: Investigate FR home 26-pt mobile gap
Beyond image srcset, profile the FR-specific JS execution (2.2 s vs 0.5 s on EN). Likely culprit: ApexCharts initialised with FR data, or `lang-redirect-fr.js` triggering layout work. Add `console.time` markers and rerun PSI.

**Success metric:** Mobile Lighthouse perf score on `/` ≥ 80, `/fr/` ≥ 80, `/blog/<article>` ≥ 80. CrUX eligibility check at 30 days.

---

### P1-B · Cluster Architecture Sprint

**Effort:** 1-2 days
**Impact:** Cluster maturity 45 → 65. Concentrates link equity on a topical pillar.

**🛠 Propose-then-implement.**

#### B-1: Build the topical pillar
Create `/resources/regulated-crypto-fund-estonia/` (and FR mirror once content is ready). Hub-and-spoke design:
- Pillar links to all 11 regulation/jurisdiction/structure articles
- Each spoke gets 1-2 contextual back-links to the pillar
- Add a homepage nav card linking to `/resources/...`

#### B-2: Eliminate 3 orphans + 2 near-orphans
Add ~12 contextual internal links across the cluster so no article has zero incoming links. Per `raw/seo-cluster.md` recommendations:
- `crypto-fund-for-qualified-investors` ← link from `regulated-crypto-fund-manager-estonia`, `sub-threshold-aifm-crypto-estonia`, `what-is-a-crypto-aifm`
- `cost-to-launch-regulated-crypto-fund-europe` (noindex) — leave isolated unless content is repurposed
- `estonia-eresidency-crypto-fund-eu` (noindex + canonical leak) — see P0-3

#### B-3: Resolve cannibalization
On `how-to-launch-a-crypto-fund-estonia` and `sub-threshold-aifm-crypto-estonia`, add disambiguation H2s + cross-links:

> *In `how-to-launch-a-crypto-fund-estonia`:*
> "**Looking for the eligibility criteria?** Read [Sub-threshold AIFM for crypto in Estonia](/blog/sub-threshold-aifm-crypto-estonia) first. This article is the step-by-step *how* once you've confirmed the *whether*."

> *In `sub-threshold-aifm-crypto-estonia`:*
> "**Already confirmed eligibility?** The step-by-step EFSA dossier walkthrough lives at [How to launch a crypto fund in Estonia](/blog/how-to-launch-a-crypto-fund-estonia)."

#### B-4: Reconcile CLAUDE.md root with reality
The root `CLAUDE.md` references "11 EN articles + 11 FR translations". Reality is **22 EN articles + 4 FR original articles + 0 bilingual pairs**. Update CLAUDE.md root + `MD/CLAUDE.md` to match (and decide: keep the 11 "bonus layer" articles or migrate them into the cluster proper?).

---

### P1-C · GEO / AI Citation Sprint

**Effort:** 1-2 days
**Impact:** GEO 71 → 82. Citation rate on ChatGPT, Perplexity, AI Overviews.

#### C-1: Add FAQPage schema to `regulated-crypto-fund-manager-estonia`
Highest-institutional-intent article + currently P12 for `finantsinspektsioon licence`. Adding FAQPage compounds topic-authority.

Suggested 4 questions:
1. *"Is SparkCore regulated by Finantsinspektsioon?"*
2. *"What is the EFSA Small Fund Manager regime?"*
3. *"What is the LEI of SparkCore Investment OÜ?"* (`8945003BBN0RVNNB0S84`)
4. *"What is the AUM threshold for sub-threshold AIFMs in Estonia?"*

#### C-2: Add 2 new homepage FAQ entries
- *"Who founded SparkCore?"* — names + LinkedIn URLs
- *"What are SparkCore's fees?"* — 2 % management, 20 % performance HWM, 0 % entry/exit, 4 % early break

#### C-3: Add a "Quick Answer" callout box to all blog articles
30-50 word direct answer at the top of each article, before any framing context. Becomes the primary AI snippet extraction target.

Pattern to replicate (similar to the existing "Key takeaways" block per `MD/CLAUDE.md` blog conventions):
```html
<div class="border-l-4 border-emerald-500 bg-[#F9FAFB] pl-5 py-4 pr-4 mb-8 rounded-r-lg">
  <p class="font-inter text-sm font-semibold text-darkGray mb-2">Quick answer</p>
  <p class="font-inter text-base text-mediumGray leading-160">[30-50 word direct answer]</p>
</div>
```

#### C-4: Convert CSS-grid comparison tables to semantic `<table>`
At least the sub-threshold AIFM article. Tabular data in CSS grids is invisible to HTML-only AI parsers.

#### C-5: Cross-link `llms-full.txt` → `llms.txt`
One-line addition. Add author per article (`— By Alexandre VINAL`) for entity reinforcement.

---

### P1-D · SXO / Page-type Sprint

**Effort:** 3-5 days
**Impact:** SXO 51 → 70. Captures non-brand intent currently exiting the site.

**🛠 Propose-then-implement.** Big enough to warrant a separate roadmap MD before coding.

#### D-1: Move trust credentials into the hero (LOW effort, HIGH impact)
Finantsinspektsioon badge + KPMG + LEI + Reg. No. currently below hero. Move into hero or a credentials bar immediately following the H1. Mirror on `/fr/`.

#### D-2: Add commercial CTA mid-blog post
On the 11 articles ranking for B2B intent (`AIFM crypto Estonia`, `regulated crypto fund Estonia`, `white label crypto fund`, etc.), insert a mid-article callout: *"Launching your own regulated crypto fund? Learn about our white-label solution."* with link to `/services/white-label-aifm/` (created in D-4).

#### D-3: Add static performance data table
ApexCharts is JS-only — invisible to crawlers and AI. Add a static `<table>` below the chart with inception date, ITD return, YTD return, max drawdown per fund + caption "Source: KPMG-audited NAV". This is YMYL-credibility *and* AI-citability.

#### D-4: Create dedicated white-label service page
`/services/white-label-aifm/` (and FR mirror later). Most content already exists in the homepage section — needs isolation, expansion, dedicated meta tags, FinancialProduct schema.

#### D-5: Create per-fund landing pages (longer-term)
`/funds/dynamic-trends/`, `/funds/cryptovision/`, `/funds/equinoxe/` (last marked "planned 2026" prominently). Each with its own InvestmentFund/FinancialProduct schema, factsheet CTA, fund-specific SEO. **This is multi-week.**

---

### P1-E · Title/Description A/B for EN homepage

**Effort:** 30 min + 30-day measurement window
**Impact:** EN home CTR 1.5% → 5-8% target (FR is at 15.2% — proves the snippet can convert).

**Variants to test in `<title>` + `<meta name="description">`:**
- Current: `SparkCore — Regulated Crypto Fund Manager | Estonia`
- B: `SparkCore — Institutional-Grade Crypto Funds | EFSA Estonia`
- C: `EFSA-Supervised Crypto Fund Manager — SparkCore Investment Estonia`

Roll one variant, wait 30 days, compare CTR on `sparkcore` query.

---

## P2 — Next quarter (strategic, multi-week)

### P2-1 · Dedicated fund landing pages
See P1-D-5. `/funds/dynamic-trends/`, `/funds/cryptovision/`, `/funds/equinoxe/`. Each with FinancialProduct schema, performance table, fund-specific factsheet gate, dedicated meta tags. Equinoxe page can launch immediately as a "coming 2026" announcement page (acceptable per `MD/CLAUDE.md`).

### P2-2 · Bilingual content strategy decision
Currently FR has 4 original articles (no EN translation) + EN has 19 indexable articles (no FR translation). Decide one of:
- (a) **EN-first** — kill the 4 FR articles, adhere to documented "no French blog" policy
- (b) **Mirror cluster** — translate the 11 regulation/Estonia articles to FR
- (c) **Two clusters** — EN regulatory cluster + FR markets/strategy cluster (current de facto)

Recommendation: (c), formalised. Update `MD/CLAUDE.md` to document the new policy. Add hreflang reciprocal pairs only if/when actual translations happen.

### P2-3 · Image sitemap
Generate `image-sitemap.xml` with team photos (E-E-A-T) and blog hero images. Submit via GSC. Template in `raw/seo-images.md` §10.

### P2-4 · Link-building outreach
Targeted outreach to:
- Crypto Council Europe / DVFA / Estonian Investment Funds Association (sectoral)
- DLA Piper / Linklaters / Hedman Partners blog citations (legal)
- Bloomberg Crypto / FT Crypto / theblock.co (press)
- Author appearances on YouTube channels in the crypto-fund space (Alexandre's existing Cointips audience is a launchpad)

Subscribe to DataForSEO Backlinks one-off (~$10) for a quality-graded inlink audit before deciding outreach targets.

### P2-5 · HSTS preload submission
After 4-6 weeks of confirmed stability, submit at https://hstspreload.org. Currently intentionally deferred per `MD/CLAUDE.md`.

### P2-6 · Microsoft Clarity revisit
Per `MD/CLAUDE.md`, Clarity decision deferred until traffic > 100 sessions/month for 3 months consecutive. Re-evaluate at the 90-day checkpoint if the perf + cluster work has lifted traffic.

### P2-7 · Wikipedia / Wikidata entry (optional, very long-term)
The largest remaining brand-authority gap. Requires editorial press coverage first to satisfy Wikipedia notability guidelines — coupled with P2-4.

---

## Sequencing & dependencies

```
Today (P0):
  P0-1 sitemap   ┐
  P0-2 indexing  ├─→ unlocks blog discovery (compounds for 2-4 weeks)
  P0-3 canonical │
  P0-4 alts FR   │
  P0-5 hreflang  │   (independent, all parallelisable today)
  P0-6 JSON-LD   │
  P0-7 llms.txt  │
  P0-8 CF zone   ┘  ← already done (verified via API 2026-05-06)

This month (P1):
  P1-A perf      ─→ depends on B for content stability (or run beta-only first)
  P1-B cluster   ─→ unlocks D-2 (commercial CTAs need stable cluster)
  P1-C GEO       ─→ partially depends on B (FAQPage on cluster pages)
  P1-D SXO       ─→ depends on B (cluster) + A (perf) — biggest sprint, do last
  P1-E A/B title  (parallel, no deps)

Next quarter (P2):
  P2-1 funds pages   ─→ depends on D-4 (white-label page first)
  P2-2 bilingual policy  (decision before any translation work)
  P2-4 outreach          (depends on perf + cluster being stable so links land on solid pages)
```

---

## Success metrics & checkpoints

### 30-day checkpoint (2026-06-05)
- GSC sitemap status: ≥ 15 indexed of 27 submitted
- ≥ 5 blog URLs indexed (URL Inspection PASS on the 5 priority articles)
- Hreflang sub-score: ≥ 75 (re-run `seo-hreflang`)
- Mobile Lighthouse perf on `/`: ≥ 75 (target 80)
- GSC non-brand impressions: ≥ 50 (vs baseline 15)
- ≥ 1 non-brand click (likely on `finantsinspektsioon licence` after P0-2 + P1-C)

### 60-day checkpoint (2026-07-05)
- Cluster maturity score: ≥ 65
- GEO score: ≥ 80
- Mobile LCP on FR home: ≤ 4 s (down from 9.8 s)
- White-label landing page live (P1-D-4)
- ≥ 3 non-brand queries with > 5 impressions each

### 90-day checkpoint (2026-08-05)
- Overall SEO Health Score: ≥ 80 (B / B+)
- CrUX eligibility: field data starts populating
- ≥ 1 fund landing page live (Dynamic Trends or CryptoVision)
- HSTS preload submitted
- 5+ blog articles ranking on page 1 for non-brand queries

---

## Items NOT to do (assumed decisions per `MD/CLAUDE.md`)

These are flagged in audits but **already decided against** with reasoning:

| Item | Decision | Why |
|---|---|---|
| SRI on CDN scripts (ApexCharts, Toastify) | ❌ Skipped | Maintenance cost > benefit; jsdelivr never compromised in 10 years. |
| CSP without `'unsafe-inline'` | ❌ Kept | Static site without Workers needs it. |
| Microsoft Clarity install | ❌ Deferred | Volume < 100 sessions/month; YMYL DPA cost. |
| Cloudflare Image Resizing ($60/yr Pro) | ❌ Deferred | Not ROI-positive at current 30 visits/day. |
| Move from CF Pages to Workers | ❌ Not now | Pages is fine for static + Functions. |
| Add JS framework (React/Next) | ❌ Not now | Static HTML is correct for SEO + perf. |
| Translate privacy-policy.html to FR | ❌ Not required | GDPR Art 12 doesn't mandate translation; legal in EN is acceptable. |

---

## Re-run instructions

```bash
# Switch project context
~/.config/claude-seo/switch.sh sci
cd ~/Documents/Claude/github-projets/sci

# Re-run a specific specialist after changes
# (in Claude Code session)
/seo geo               # AI citation re-check after C-3 / C-5
/seo hreflang          # after P0-5
/seo schema            # after P0-6
/seo performance       # after P1-A

# Drift compare (against today's baseline)
python3 ~/.claude/skills/seo/scripts/drift_compare.py https://sparkcore.fund/

# Force-index after content changes
python3 scripts/ops/indexnow_ping.py https://sparkcore.fund/blog/<slug>

# Full re-audit (this skill)
/seo audit https://sparkcore.fund/
```

---

**Total P0 effort:** ~2 hours of focused work · **Total P1 effort:** ~2 weeks of dev/content time · **P2:** ~1 quarter

Open the FULL-AUDIT-REPORT.md alongside this plan for the full evidence trail, raw data references, and per-area scoring detail.
