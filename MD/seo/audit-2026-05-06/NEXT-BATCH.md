# Next Batch — SparkCore SEO Roadmap

**Date:** 2026-05-06 (post-execution roadmap)
**Audit reference:** `FULL-AUDIT-REPORT.md` (66/100 baseline) · `ACTION-PLAN.md`
**State after today's deploy:** 7 PRs merged (#94–#100), score projected 66 → ~85/100

This document organises everything that **remains** on the SEO backlog. Per the user's `propose-then-implement` rule for SCI, this MD lists the items, estimates each, and waits for the user's "go" on the ones that should ship.

---

## Quick decision matrix

| # | Item | Effort | SEO impact | Gate |
|---|---|---|---|---|
| **B1** | Cluster pillar page `/resources/regulated-crypto-fund-estonia/` (~3,000 words) | 4-6 h | **HIGH** (cluster 45 → ~70) | **`/blog-write` skill** — orchestrated draft, user reviews |
| **B2** | Article "AIF vs AIFM" (~800-1,000 words) | 1-2 h | HIGH (closes P0 cluster gap) | **`/blog-write` skill** — orchestrated draft, user reviews |
| **B3** | Quick Answer callouts on 14 remaining indexable articles | 2-3 h | MEDIUM (compounds GEO) | Autonomous (mechanical insertion, no new prose) |
| **B4** | FR home FAQPage (translate 6 EN questions) | 30 min | LOW-MEDIUM (parity) | Autonomous (FR translation OK) |
| **B5** | CSP cleanup (remove `fonts.googleapis.com` / `fonts.gstatic.com`) | 5 min API call | NONE (security hygiene) | Needs write-scoped CF API token (or manual UI) |
| **B6** | Beta branch re-sync with main | 2 min | NONE (ops cleanup) | Needs explicit force-push authorisation |
| **B7** | Noindex articles decision (3 articles) | Strategic 5-min decision | HIGH (3 indexable articles unlocked) | **NEEDS USER CALL** |
| **B8** | Bilingual content policy decision | Strategic 10-min decision | MEDIUM | **NEEDS USER CALL** |
| **B9** | Trust strip move into hero | 1-2 h CSS | LOW direct SEO, UX gain | Autonomous, but visual — eyes-on review preferred |
| **B10** | White-label dedicated landing `/services/white-label-aifm/` | 6-8 h | HIGH SXO (51→62) | **NEEDS YOUR MARKETING COPY** |
| ~~**B11**~~ | ~~3 fund landing pages~~ | — | — | **DEFERRED — user direction 2026-05-06: no per-fund pages for now** |
| **B12** | Static performance data table on home | 30 min | LOW direct SEO, MEDIUM AI citation | **NEEDS KPMG-AUDITED NAV FIGURES** |
| **B13** | 30-day checkpoint re-audit | 2 h orchestration | Validates everything done today | Schedule for 2026-06-05 |
| **B14** | Drift compare baseline | 5 min | Detect regressions | Already captured today; auto-compare next audit |

**Total autonomous backlog:** ~3-4 h (B3+B4+B9 — content tasks B1+B2 use `/blog-write`)
**Total `/blog-write` orchestrated backlog:** B1+B2 (~6-8 h orchestration with Claude in the loop)
**Total user-gated backlog:** B7+B8+B10+B12 — needs decisions or content
**Total ops backlog:** B5+B6 — needs token / authorisation
**Removed from backlog:** B11 (per-fund landings — deferred indefinitely per user direction)

---

## Recommended sequencing

### Sprint 1 — Content + GEO batch (mixed: `/blog-write` for prose + autonomous for mechanical)

**Why this batch first:** Highest combined SEO impact remaining. Pillar page is the single biggest cluster lever; Quick Answer rollout compounds GEO. Each step is shippable independently.

| Step | Item | Workflow | Output |
|---|---|---|---|
| 1.a | **B1 pillar page** | `/blog-write` skill (orchestrated, user-in-the-loop) | New page `/resources/regulated-crypto-fund-estonia/` + 11 inbound links from spokes + nav card |
| 1.b | **B2 AIF vs AIFM article** | `/blog-write` skill | New page `/blog/aif-vs-aifm-crypto-explained` (or chosen slug) + 4 inbound links from cluster |
| 1.c | **B3 Quick Answer rollout** | Autonomous — 1 mechanical PR | 14 articles get the same callout pattern as #99 |
| 1.d | **B4 FR home FAQPage** | Autonomous — 1 small PR | 6 Q&A translated, JSON-LD inserted in `fr/index.html` |

**`/blog-write` invocation pattern (proposed for B1 + B2):**
```
/blog-write "Launching a Regulated Crypto Fund in Estonia: The Complete Guide" \
  --type pillar \
  --target-words 3000 \
  --location MD/seo/audit-2026-05-06/drafts/ \
  --cluster-context "regulated-crypto-fund-manager-estonia, sub-threshold-aifm-crypto-estonia, how-to-launch-a-crypto-fund-estonia, do-crypto-fund-managers-need-mica-casp-license, what-is-a-crypto-aifm, white-label-crypto-fund-manager-services, crypto-fund-for-qualified-investors, crypto-fund-fees-2026, estonia-luxembourg-malta-crypto-fund, what-an-alternative-investment-fund-platform-does"
```

The skill will produce a draft MD file in `MD/` (gitignored from web). I then convert it to HTML using the `md-to-html` workflow already documented in `MD/CLAUDE.md`, add internal-link injections, schema, sitemap entry, and ship as a PR.

For B2 (AIF vs AIFM), same pattern with `--target-words 800-1000` and `--type explainer`.

Expected score lift after Sprint 1: **~85 → ~90/100 (A-)**.

**Sequencing note:** B3 + B4 can ship before B1 + B2 since they don't depend on the new content. If you want incremental wins, run B3+B4 as a single small PR first while we scope B1+B2 with `/blog-write`.

### Sprint 2 — User-gated decisions (no PR, just decisions)

**Why this is short:** Two decisions unblock several downstream items.

1. **B7 — Noindex articles decision.** Pick one:
   - **(a) Flip to index** — `cost-to-launch-regulated-crypto-fund-europe`, `crypto-fund-fees-2026`, `estonia-eresidency-crypto-fund-eu` go from `noindex` → `index`. Adds 3 indexable articles, unlocks the 8 internal-link recommendations skipped in #98, fixes the cluster's link equity flow.
   - **(b) Keep noindex (status quo)** — these articles stay as redirect-target shells; cluster keeps the 8-link gap.
   - **(c) Delete** — remove the files entirely if they're truly deprecated. Cleanest if no incoming links matter.
   
   Decision is mostly editorial: do you want this content to rank, or is it deliberately archived?

2. **B8 — Bilingual policy.** Currently 22 EN articles + 4 FR-original (different topics) + 0 bilingual pairs. Pick one:
   - **(a) EN-first, no FR blog** — kill the 4 FR articles, adhere to the documented policy in `MD/CLAUDE.md`
   - **(b) Mirror cluster** — translate the 11 main regulation articles to FR (substantial work)
   - **(c) Two clusters** — EN regulatory cluster + FR markets/strategy cluster (de facto current state). Update `MD/CLAUDE.md` to formalise.
   
   Recommendation: **(c)**, formalised. Update CLAUDE.md to document the dual-cluster strategy. No content work needed.

### Sprint 3 — User-content sprint (parallel work, you provide copy)

These need YOUR marketing/legal/financial copy. I can scaffold the HTML, schema, nav, internal links — but the substantive text must come from you.

1. **B10 — White-label landing page**
   - **What I need from you:**
     - 1 hero headline + 2-sentence value prop
     - 3-5 differentiators (e.g., "EFSA-supervised AIFM shell", "30-day onboarding", "MiCA-compatible structure")
     - Target audience copy block (who this is for: emerging managers, family offices, etc.)
     - Process steps (what happens after a discovery call)
     - 1 testimonial OR 1 case study (anonymised if needed)
   - **What I'll deliver:** Page scaffold, FinancialProduct schema, nav integration, internal links from blog cluster, FAQPage with 4 white-label-specific Q&A.

2. ~~**B11 — Fund landing pages × 3**~~ — **DEFERRED (user direction 2026-05-06).** No per-fund landing pages for now. The fund pitch stays consolidated on the homepage. Trade-off accepted: SparkCore won't rank for fund-specific queries (e.g., "delta neutral crypto fund"), but the gated factsheet-by-email model is preserved as the primary distribution channel for fund-level data. Re-evaluate in 6+ months if non-brand discovery becomes a priority.

3. **B12 — Performance data table on home**
   - **What I need from you:** Same KPMG-audited NAV data as B11 — 1 row per active fund (Dynamic Trends, CryptoVision; Equinoxe shown as "planned").
   - **What I'll deliver:** Static `<table>` below the chart on `/` and `/fr/`, with caption "Source: KPMG-audited NAV", AI-extractable.

### Sprint 4 — Ops cleanup

1. **B5 — CSP cleanup.** Remove unused `fonts.googleapis.com` / `fonts.gstatic.com` from the Cloudflare Transform Rule. Two options:
   - **(a) Manual UI** (5 min) — go to dash.cloudflare.com → sparkcore.fund → Rules → Transform Rules → "Add Content-Security-Policy" → edit the value to remove the two domains
   - **(b) Create a write-scoped CF API token** — can then automate this AND any future zone-config changes (e.g., for dsungkur). Token: `Zone:Zone Settings:Edit` + `Zone:Transform Rules:Edit`, IP-restrict to VPS, save under `cloudflare_api_token_write` in `~/.config/claude-seo/projects/sci.json`

2. **B6 — Beta branch re-sync.** `git push origin main:beta --force-with-lease` after explicit authorisation. Beta is currently 9 commits behind main with content-divergent versions of `index.html` + `fr/index.html`. No prod impact, but if you want to use beta for previewing future PRs, sync it now.

3. **B9 — Trust strip move into hero (optional, defer if no design appetite).** Risk: small layout regression. Approach options:
   - **(a) Move existing trust-strip into hero** (modifies hero CSS — risky)
   - **(b) Add a discreet credentials text bar inside hero** (1-line addition between H1 and tagline — safer, recommended)
   - **(c) Keep below the fold** (status quo — institutional users will scroll)
   
   Recommendation: **(b)**, with a single-line text strip like *"EFSA-supervised · KPMG-audited · LEI 8945003BBN0RVNNB0S84"*.

### Sprint 5 — Validation & monitoring (mostly automatic)

1. **B13 — 30-day checkpoint re-audit (2026-06-05).** Re-run `/seo audit https://sparkcore.fund/`, compare to today's baseline. Should show: blog now indexed, CrUX field data starting to populate, non-brand impressions > 50.

2. **B14 — Drift baseline compare.** A baseline was captured today by `drift_baseline.py`. Run `drift_compare.py https://sparkcore.fund/` next time to detect regressions.

---

## Detailed item specs (Sprint 1)

### B1 — Pillar page `/resources/regulated-crypto-fund-estonia/`

**Workflow:** `/blog-write` skill. The skill orchestrates research, outline, sourced statistics, and answer-first prose; I keep responsibility for site integration (HTML conversion, schema, sitemap, internal-link injection from the spokes back to the pillar).

**Goal:** Become the topical hub for the cluster. Re-pool link equity from the 11 indexable articles. Currently link equity has accidentally pooled in 2 commercial pages (white-label + regulated-crypto-fund-manager-estonia) — wrong for YMYL ranking signals.

**Brief to pass into `/blog-write`:**
- **Title (proposed):** "Launching a Regulated Crypto Fund in Estonia: The Complete Guide"
- **Type:** pillar / cornerstone
- **Target length:** 3,000 words
- **Audience:** institutional investors, family offices, prospective fund managers (B2B + B2C-institutional)
- **Tone:** YMYL-rigorous, evidence-cited, regulator-credible
- **Cluster context:** the 11 indexable spoke articles already on `/blog/` (regulated-crypto-fund-manager-estonia, sub-threshold-aifm-crypto-estonia, how-to-launch-a-crypto-fund-estonia, do-crypto-fund-managers-need-mica-casp-license, what-is-a-crypto-aifm, white-label-crypto-fund-manager-services, crypto-fund-for-qualified-investors, estonia-luxembourg-malta-crypto-fund, what-an-alternative-investment-fund-platform-does, what-an-institutional-crypto-fund-manager-does, crypto-fund-vs-etf)
- **Required schema:** BlogPosting (or `@type: WebPage` if we want to differentiate it from blog), BreadcrumbList (Home → Resources → page), FAQPage (6 Q&A), Person (Alexandre VINAL author)
- **Required structural elements:** TL;DR / Quick Answer at top, Key Takeaways block (5 bullets), each H2 section linking to 1-2 cluster spokes, citation capsules with EFSA + EUR-Lex + AIFMD legal sources

**Outline (the skill will refine):**
1. What "regulated crypto fund" means in the EU (AIFMD framework)
2. Why Estonia for crypto fund managers (jurisdiction comparison)
3. Sub-threshold vs full AIFM: which regime fits you (links to → sub-threshold + how-to-launch)
4. Registration steps with Finantsinspektsioon (links to → how-to-launch)
5. Capital requirements + fund vehicle structure (usaldusfond) (links to → estonia-luxembourg-malta)
6. MiCA + AIFMD interaction (links to → mica-casp-license + what-is-a-crypto-aifm)
7. White-label vs in-house AIFM (links to → white-label-crypto-fund-manager-services)
8. Investor eligibility + minimum subscription (links to → qualified-investors)
9. Fund strategies available (links to → market-neutral, arbitrage, delta-neutral, what-an-institutional-crypto-fund-manager-does)
10. Operational reality: timelines, costs, ongoing compliance (links to → regulated-crypto-fund-manager-estonia)
11. FAQ (6 questions covering the most common queries)

**Deliverable (post `/blog-write`):**
- Draft MD in `MD/seo/audit-2026-05-06/drafts/regulated-crypto-fund-estonia-pillar.md` (user reviews)
- Once approved: HTML conversion via the `md-to-html` workflow in `MD/CLAUDE.md` (template: `blog/do-crypto-fund-managers-need-mica-casp-license.html`, but at `/resources/<slug>/index.html` to enable the `/resources/` URL pattern)
- 1 PR with: new page + nav card on `/blog/` + footer "Resources" link + sitemap entry with self-canonical + 11 contextual back-links from spokes

### B2 — Article "AIF vs AIFM"

**Workflow:** `/blog-write` skill, same as B1 but smaller scope.

**Goal:** Close the most common reader confusion in the cluster (AIF = the *fund*, AIFM = the *manager*).

**Brief to pass into `/blog-write`:**
- **Title (proposed):** "AIF vs AIFM: What's the Difference and Why It Matters for Crypto Funds"
- **Type:** explainer / definitional
- **Target length:** 800-1,000 words
- **Audience:** prospective fund managers + institutional investors evaluating regulated structures
- **Tone:** clear definitional, with one concrete worked example (SparkCore as illustration)
- **Cluster context:** sub-threshold, do-crypto-fund-managers-need-mica-casp-license, how-to-launch-a-crypto-fund-estonia, what-is-a-crypto-aifm
- **Required schema:** BlogPosting, BreadcrumbList, FAQPage (3 Q&A), Person
- **Required structural elements:** Quick Answer at top, Key Takeaways (3-4 bullets), H2 sections in question format

**Outline (the skill will refine):**
1. What is an AIF? (definition + scope)
2. What is an AIFM? (manager vs fund, AIFMD framework)
3. Who can be an AIFM? (sub-threshold, full authorisation tiers)
4. Why the distinction matters (legal, operational, fundraising)
5. AIF vs AIFM in the crypto context
6. How SparkCore is structured (concrete example)

**Deliverable (post `/blog-write`):**
- Draft MD in `MD/seo/audit-2026-05-06/drafts/aif-vs-aifm.md` (user reviews)
- HTML conversion at `/blog/aif-vs-aifm-crypto-explained.html` (or chosen slug)
- 1 PR with: new article + 4 inbound link edits (from sub-threshold, mica-casp, how-to-launch, what-is-a-crypto-aifm) + sitemap entry

### B3 — Quick Answer rollout on 14 remaining articles

**Articles needing the callout (indexable, missing it after #99):**

| Article | Suggested Quick Answer focus |
|---|---|
| bitcoin-outperformance-strategy-fund | What is a Bitcoin outperformance strategy and when does it work? |
| crypto-arbitrage-investment-fund | What is a crypto arbitrage fund and how does it manage risk? |
| crypto-fund-compliance-guide | Compliance checklist for crypto AIFs in 2026 |
| crypto-fund-for-qualified-investors | What makes a fund "qualified-investor only" in EU |
| crypto-fund-vs-etf | Crypto fund vs spot ETF: 4 key differences |
| delta-neutral-crypto-strategies-explained | What is delta-neutral and why fund managers use it |
| estonia-luxembourg-malta-crypto-fund | EU jurisdiction comparison for crypto AIFs |
| how-to-launch-a-crypto-fund-estonia | 7-step Estonia launch summary |
| regulated-crypto-investment-fund | What "regulated" means in the crypto fund context |
| what-a-market-neutral-crypto-fund-does | Market-neutral crypto fund mechanics |
| what-an-alternative-investment-fund-platform-does | What an AIF platform does for emerging managers |
| what-an-institutional-crypto-fund-manager-does | Institutional crypto fund manager: scope of services |
| white-label-crypto-fund-manager-services | The white-label setup in 50 words |
| white-label-crypto-fund-platform | White-label fund platform: how it differs from a single AIFM |

Pattern same as #99 (emerald border, "Quick answer" label, 30-50 words). Single mechanical PR.

### B4 — FR home FAQPage

Translate the 6 EN home FAQ entries into French. The translations need to use SparkCore's existing French terminology (already established in `/fr/index.html` body copy):

1. *Qu'est-ce que SparkCore Fund Management ?*
2. *Quel est l'investissement minimum dans les fonds SparkCore ?*
3. *SparkCore Fund Management est-il réglementé ?*
4. *Quels fonds SparkCore gère-t-il ?*
5. *Qui a fondé SparkCore ?*
6. *Quels sont les frais de SparkCore ?*

**Deliverable:** Insert the FR FAQPage JSON-LD block into `fr/index.html` after the @graph block. Same 6 Q&A as EN home, translated.

---

## What I'd recommend you do next

1. **Today (5 min):** Read this document, give a "go" on Sprint 1.
   - **Fast path:** start with B3 + B4 (autonomous, ~3 h, immediate ship). Then B1 + B2 via `/blog-write` once you're ready to review drafts.
   - **Big move first:** start with B1 via `/blog-write` (highest single SEO impact remaining).
2. **This week (15 min):** Make the two decisions in Sprint 2 (B7 noindex + B8 bilingual). They unblock follow-up work and clean up the cluster's link-equity flow.
3. **This week (UI, 5 min):** Do B5 (CSP cleanup) manually via the CF dashboard, OR create the write-scoped CF token if you want me to script it (and any future zone-config work).
4. **When you have 1 hour:** Send me the marketing copy for B10 (white-label landing) and the KPMG NAV data for B12 (perf table). I scaffold the rest. (B11 fund landings are deferred per your direction.)
5. **Schedule (2026-06-05):** 30-day checkpoint re-audit. I'll re-run `/seo audit` and produce a drift compare against today's baseline.

---

## Files modified today (audit + execution)

For reference, today's deploy touched these files (now on `main`):

```
assets/css/fonts.css                                   (new)
assets/css/style.css                                   (1 line)
assets/fonts/{12 woff2 files}                          (new)
assets/images/blog/mica-casp-hero.webp                 (new)
assets/images/blog/mica-casp-hero-768.webp             (new)
assets/js/analytics.js                                 (gtag defer)
fr/index.html                                          (preloads + alts + JSON-LD founders)
fr/blog/{4 FR articles}.html                           (hreflang removal)
fr/blog/le-vrai-cout-du-market-timing.html             (WebP swap)
index.html                                             (preloads + JSON-LD founders + 2 FAQ)
sitemap.xml                                            (hreflang on 20 URLs)
llms.txt                                               (LEI + dateModified)
blog/{6 articles}                                      (hero fetchpriority)
blog/regulated-crypto-fund-manager-estonia.html        (FAQPage + Quick Answer + CTA)
blog/sub-threshold-aifm-crypto-estonia.html            (Quick Answer + disambiguation + CTA)
blog/how-to-launch-a-crypto-fund-estonia.html          (disambiguation + CTA)
blog/what-is-a-crypto-aifm.html                        (Quick Answer + CTA)
blog/why-invest-in-crypto-funds-2026.html              (Quick Answer)
blog/do-crypto-fund-managers-need-mica-casp-license.html (Quick Answer + CTA + WebP hero)
blog/crypto-fund-for-qualified-investors.html          (Related reading callout)
blog/{6 other B2B articles}                            (mid-article CTA)
MD/seo/audit-2026-05-06/                               (full audit reports)
MD/CLAUDE.md                                           (CF state + APIs table)
MD/seo/audit-2026-05-06/NEXT-BATCH.md                  (this file)
49 HTML files                                          (style.css cache-bust v=1.4/1.5 → v=1.6)
```

---

**Status of this document:** Awaiting user approval on which Sprint 1 items to ship + Sprint 2 decisions.
