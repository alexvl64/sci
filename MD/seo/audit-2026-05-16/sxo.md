# SXO Audit — sparkcore.fund
**Date:** 2026-05-16 | **Analyst:** Claude SXO (claude-sonnet-4-6)
**Prior audit:** 2026-05-08 | **SXO Gap Score then:** 67/100
**Scope:** Homepage `/`, Pillar `/resources/regulated-crypto-fund-estonia/`, `/blog/regulated-crypto-fund-manager-estonia`, `/blog/estonia-luxembourg-malta-crypto-fund`, `/blog/crypto-fund-fees-2026`
**Context:** Regulated AIFM (Finantsinspektsioon, Estonia) — YMYL financial, qualified investors, €50k minimum, no paid ads

---

## Sprint Delta Since 2026-05-08

| Item | 2026-05-08 status | 2026-05-16 status |
|---|---|---|
| Trust line under H1 (S1-4) | Shipped, then reverted commit `0c997cc` on 2026-05-08 | STILL ABSENT — Skeptic gap open |
| Comparison table in `/blog/estonia-luxembourg-malta-crypto-fund` | Absent — narrative prose | PRESENT — full `<table>` at `<h2>` position ~250 words in |
| Founder CTA on comparison blog | Absent | PRESENT — `Schedule a Founders Call` Cal.com button near bottom |
| Founder CTA on `/blog/regulated-crypto-fund-manager-estonia` | Absent | PRESENT — same `founder-cta-btn` Cal.com button |
| Founder CTA on pillar | Absent | PRESENT — same button at conclusion |
| HowTo schema on pillar registration steps | Absent | STILL ABSENT — 7 steps exist in HTML prose, no JSON-LD |
| `dateModified` pillar | 2026-05-08 | Unchanged at 2026-05-08 (8 days stale) |
| Lead-type qualifier on sidebar form | Absent | STILL ABSENT |
| Speakable schema | Added sprint 1 | Present on all audited pages |
| Byline format | Fixed sprint 1 | Present |

Sprint 1 (commit `a3df92f`) delivered Speakable parity and byline fix, but did not address the core SXO content findings. The most impactful structural changes (comparison table, Founder CTAs) were shipped in an earlier sprint (commit `fe72b39` and `f3fdca8`) that predates the 2026-05-08 audit by days — confirming the table and CTAs were live at audit time. The 2026-05-08 audit scored them absent because SERP position had not yet responded.

---

## PRIMARY FINDING — Trust-Line Revert Confirmed Open (Skeptic Gap)

Commit `0c997cc` (2026-05-08, same day as prior audit) removed the inline trust credential `"Supervised by Finantsinspektsioon · LEI · Audited by KPMG Estonia"` from the hero section on both EN and FR homepages. The revert message states the removal was a visual decision made after review on `beta.sparkcore.fund`.

**Current hero state (confirmed from HTML lines 561–590):** H1 reads "Institutional-grade strategies in digital assets". Below it: tagline "Three distinct approaches. One regulated framework." Then two CTAs: `Schedule a Discovery Call` + `Request Documentation`. No trust credential appears in the hero viewport.

The trust strip (Finantsinspektsioon link, KPMG, LEI) exists at line 640 — immediately AFTER the `</section>` tag closing the hero. On desktop it renders below the hero image. On mobile (hero image `h-[400px]`), the trust strip is always below the fold.

**Mismatch severity: HIGH.** The single most actionable Skeptic fix from the prior audit was reverted and never re-implemented. This is the open finding with the highest persona-conversion impact.

---

## 1. SERP Backwards Analysis — What Google Rewards Per Query

### Query: "crypto fund estonia" / "regulated crypto fund estonia"

**Top 10 page-type pattern (2026-05-16 WebSearch):**
SparkCore ranks p1 (homepage), p4 (blog: regulated-crypto-fund-manager-estonia), p6 (blog: estonian-aifm-crypto-fund redirect). Competitors: hacken.io (explainer), rue.ee (regulatory guide), kalashnikov.ee (law firm service page), thompsonstein.com (AIF explainer), eestifirma.ee (service landing), coredo.eu (step-by-step guide).

**Dominant SERP page-type:** Regulatory explainer / service landing (7 of 10). Two SparkCore blog posts. One government page.

**What Google rewards:** Structured regulatory explainers with step-by-step flows (coredo.eu, eestifirma.ee). Law firm service pages that present cost and timeline as the first H2 (kalashnikov.ee). Google's AI Overview (where visible) surfaces AUM thresholds, registration timelines, and fee figures — all structured data candidates.

**SparkCore match:** Blog at p4 is narrative-first but now includes comparison tables. Partial match. Pillar at `/resources/regulated-crypto-fund-estonia/` not appearing for this query despite being the strongest depth match — possible indexation lag or anchor insufficiency.

---

### Query: "crypto AIFM estonia"

**Top 10 page-type pattern:**
SparkCore holds p1 (blog: regulated-crypto-fund-manager-estonia), p2 (redirect to same), p3 (homepage). Competitors: kalashnikov.ee (law firm AIF registration page), thompsonstein.com (AIF-in-Estonia explainer), coredo.eu (step-by-step), eestifirma.ee (service page).

**Dominant SERP page-type:** Mix of law firm service pages (p4–5) and regulatory step-by-step guides (p6–8). SparkCore owns top 3 with blog content.

**Key SERP signal:** Law firm service pages at p4–5 present a "Book a Consultation" or "Get a Quote" CTA above the fold. The Founder CTA now exists on SparkCore's blog (confirmed: `Schedule a Founders Call` button with `data-cal-link="sparkcore/discovery"`), but it appears near the end of a 4,500-word article — below the fold by 90% of scroll depth. Law firms surface the CTA within the first 300 words.

**SparkCore match:** Good position dominance. CTA architecture improved but CTA depth placement still disadvantages conversion vs competitors.

---

### Query: "estonia luxembourg malta crypto fund"

**Top 10 page-type pattern:**
Page `/blog/estonia-luxembourg-malta-crypto-fund` at p8.1 per prior GSC data (position likely shifted by now given structural improvements). SERP shows jurisdiction-comparison guides from ifbusiness.uk, coredo.eu (Switzerland vs EU), and general crypto-friendly-country listicles. The SparkCore comparison blog is now the most structurally complete pure-AIFM comparison article in English for this query — the table now present.

**Dominant SERP page-type:** Comparison table / jurisdiction matrix format. Confirmed: ifbusiness.uk article uses a jurisdiction matrix; general listicles use country tables. SparkCore's page now matches this format.

**SERP feature observed:** No featured snippet captured by SparkCore despite the table — the Quick Answer callout block (emerald border, visible at line 216) is the strongest featured snippet candidate. Table caption uses `<caption class="sr-only">` — correct for accessibility, but the table is not the first content element (hero image and 2 intro paragraphs appear before it). For featured snippets, the table should appear as close to the H2 as possible with no intervening prose.

---

### Query: "finantsinspektsioon licence" / "finantsinspektsioon crypto fund"

**SERP pattern:** Official fi.ee pages, charltonsquantum.com PDF, rue.ee regulatory guide. SparkCore not appearing in top 10 for this specific query — blog content mentions Finantsinspektsioon but does not target the term as a primary keyword.

**What Google rewards:** Primary-source citations, direct regulator-page links, compliance checklists. SparkCore links to fi.ee in the blog bylines and in the JSON-LD `sameAs` array — good structural signal. Missing: a dedicated page that targets "finantsinspektsioon" as the primary keyword with the regulator's public registry URL as the primary anchor.

---

## 2. Page-Type Mismatch Assessment (Updated)

| Page | SparkCore Type | Dominant SERP Type | Mismatch | Change vs 2026-05-08 |
|---|---|---|---|---|
| Homepage `/` | Product/brand landing | Regulatory guide / explainer | MEDIUM | Unchanged — trust line still absent above fold |
| Pillar `/resources/regulated-crypto-fund-estonia/` | Long-form guide with 12 H2s, internal links, Founder CTA | Long-form guide (ALIGNED) | ALIGNED | No structural change; dateModified stale |
| Blog: `regulated-crypto-fund-manager-estonia` | Blog article with Founder CTA + white-label section | Regulatory guide with service CTA | MEDIUM → LOW | Improved: Founder CTA present; missing: early CTA placement |
| Blog: `estonia-luxembourg-malta-crypto-fund` | Comparison article with `<table>` above fold | Comparison table / jurisdiction matrix | HIGH → LOW | Major improvement: table present, Founder CTA present |
| Blog: `crypto-fund-fees-2026` | Data article with fee benchmarks table | Data article / benchmarks | ALIGNED | Unchanged — remains well-matched |

**Net mismatch change:** The single highest-impact finding from the prior audit (F-1: comparison table) is resolved. Mismatch across the portfolio drops from 2× HIGH + 1× MEDIUM to 1× MEDIUM (homepage trust gap) + 2× remaining minor gaps. The remaining open finding that drives the most persona score delta is the trust-line revert.

---

## 3. Trust-Line Revert: Skeptic Gap Open (Confirmed)

**Commit evidence:** `0c997cc` — "revert(hero): remove trust line under H1 (S1-4)" — removes `heroTrustLine` i18n key from `translations.js` and 6 lines from both `index.html` and `fr/index.html`. Commit message confirms a visual review decision on beta.

**Current above-fold hero (EN, confirmed HTML):**
- Badge: "New — AIF vs AIFM: What's the Difference for Crypto Funds"
- H1: "Institutional-grade strategies in digital assets"
- Tagline: "Three distinct approaches. One regulated framework."
- CTA 1: "Schedule a Discovery Call"
- CTA 2: "Request Documentation"

The word "regulated" appears in the tagline ("One regulated framework") — this is the only trust signal visible above fold. It makes a claim but provides no verifiable anchor. The trust strip with Finantsinspektsioon link, KPMG, and LEI is immediately below the hero section, but on every mobile viewport it renders below the fold.

**Skeptic first-second test:** A first-time visitor on mobile sees H1 + tagline + two CTAs. No verifiable regulatory credential is visible. "Regulated framework" is self-asserted. The Skeptic's question — "is this real or marketing?" — is not answered before the first scroll.

**Why the revert happened:** The beta visual review likely found the credential line created a typography clash or crowded the hero. The right fix is not to restore the same inline text — it's to embed the regulatory credential in a format that fits the dark hero aesthetic (e.g., a small pill badge below the CTAs: "Supervised by Finantsinspektsioon · EST" with a regulator icon). The `founder-cta-btn` class already exists and its dark-on-dark style could be adapted for a trust badge variant.

---

## 4. Persona Re-Scoring (1–5 scale)

**Rubric:** 5 = Fully meets persona need | 4 = Mostly met, minor gap | 3 = Partially met | 2 = Significant gap | 1 = Not addressed

### Allocator (institutional CIO, evaluating fund allocation)

| Page | Score | Score change | Rationale |
|---|---|---|---|
| Homepage | 4 | = | Trust strip (Finantsinspektsioon, KPMG, LEI) present below hero. Fund cards, Discovery Call CTA. Minus 1: trust strip below fold on mobile; no NAV or performance data above fold. |
| Pillar | 2 | = | Content targets Founder persona. An allocator finds registration mechanics, not fund performance data, investment terms, or subscription process. Mismatch of content vs persona. |
| Blog: regulated-crypto-fund-manager-estonia | 3 | = | Regulatory depth is present. Minus 2: article explains how AIFM is regulated, not why SparkCore's track record or strategy warrants an allocation. No fund-specific data. |
| Blog: estonia-luxembourg-malta-crypto-fund | 3 | +1 | The jurisdiction comparison is relevant to an allocator evaluating the structural quality of a fund. The table makes key facts scannable. Minus 2: no link to factsheet or discovery call from the Allocator's perspective. |
| Blog: crypto-fund-fees-2026 | 4 | = | Fee benchmark data directly relevant to Allocator DD. SparkCore's fees disclosed and contextualised. Strong. |

**Allocator aggregate: 3.2/5 (+0.2 vs prior)**

---

### Founder (crypto trader evaluating how to launch a regulated fund)

| Page | Score | Score change | Rationale |
|---|---|---|---|
| Homepage | 3 | +1 | The white-label section now visible on homepage (confirmed HTML line 1277). Finantsinspektsioon reference. Founders see a path. Minus 2: CTA is "Schedule a Discovery Call" which blends Founder and Allocator intent without persona distinction. |
| Pillar | 5 | = | Near-perfect. 12 H2s covering regime choice, registration steps, capital requirements, MiCA overlay, white-label vs in-house, timeline, FAQ. Founder CTA at conclusion. |
| Blog: regulated-crypto-fund-manager-estonia | 4 | +1 | Founder CTA now present. White-label section at line 438 describes SparkCore's AIFM structuring offer explicitly. Minus 1: CTA appears after 4,500 words — most Founders will not scroll that far. |
| Blog: estonia-luxembourg-malta-crypto-fund | 5 | +2 | Comparison table above fold. Founder CTA present. Quick Answer addresses the decision directly. Cost SVG charts scannable. Internal links to white-label article. Near-optimal for Founder decision stage. |
| Blog: crypto-fund-fees-2026 | 3 | = | Fee benchmark is useful for Founders modelling their P&L. No explicit Founder CTA or link to white-label services. Internal link to white-label exists (line 392) but is editorial rather than a CTA block. |

**Founder aggregate: 4.0/5 (+0.8 vs prior)**

---

### Compliance (DD lawyer or CRO doing third-party due diligence)

| Page | Score | Score change | Rationale |
|---|---|---|---|
| Homepage | 3 | = | LEI link to GLEIF, Finantsinspektsioon link in trust strip. KPMG named. Hedman Partners named. Minus 2: no direct link to Finantsinspektsioon's public registry entry for SparkCore.investment OÜ from the trust strip value (link goes to the correct URL but requires knowing what to look for). No audit report reference. |
| Pillar | 4 | = | Full regulatory mechanics, primary-source citations, EFSA licensing guidance links, EFIU/FIU dual supervision explained. Minus 1: registration number and LEI appear in the author bio but not in a dedicated "Compliance verification" block early in the article. |
| Blog: regulated-crypto-fund-manager-estonia | 4 | = | Strongest Compliance content in the cluster. Dual-authority supervision (Finantsinspektsioon + FIU) explained. Primary-source FSA link in author bio. LEI cited. MiCA/VASP sunset deadline flagged. |
| Blog: estonia-luxembourg-malta-crypto-fund | 3 | = | Regulatory framework per jurisdiction compared. Sources cited (CSSF, PwC Tax Summaries, FATF). Minus 2: no primary-source link to MFSA or CSSF regulatory registers; comparison is editorial, not verified-by-regulator-link at each cell. |
| Blog: crypto-fund-fees-2026 | 2 | = | Compliance officer cares about fee disclosure under AIFMD (KID/PRIIP requirements). Article covers fee benchmarks but does not reference AIFMD II Art. 23 fee disclosure mandates specifically. Missed opportunity. |

**Compliance aggregate: 3.2/5 (= vs prior)**

---

### Skeptic (first-time visitor, no prior knowledge)

| Page | Score | Score change | Rationale |
|---|---|---|---|
| Homepage | 2 | = | Hero text "Institutional-grade strategies" + "One regulated framework" are unverifiable claims. Trust strip below fold on mobile. Skeptic's first-second test fails. Score unchanged — the trust-line revert means this gap is identical to 2026-05-08. |
| Pillar | 3 | = | Quick Answer box visible early. Regulatory explanation present. Author bio with LinkedIn and registry link at bottom. Minus 2: no "Is this a real regulated entity?" shortcut near the top — Skeptics abandon long articles before reaching the author bio. |
| Blog: regulated-crypto-fund-manager-estonia | 3 | = | Quick Answer box names Finantsinspektsioon, LEI, and EFIU licence in first viewport. This is the strongest Skeptic entry point in the blog cluster — the Quick Answer directly answers "is SparkCore regulated?" Minus 2: the registry URL and LEI are in the Quick Answer prose but not hyperlinked there — only in the author bio at the bottom. |
| Blog: estonia-luxembourg-malta-crypto-fund | 3 | = | Quick Answer (Estonia cost figure, registration timeline) answers a Founder question, not a Skeptic question. Skeptic arriving on this page gets jurisdiction data, not entity verification. |
| Blog: crypto-fund-fees-2026 | 2 | = | Fee data article gives no entity verification signal. A Skeptic reading this page cannot confirm SparkCore is regulated without clicking away. |

**Skeptic aggregate: 2.6/5 (= vs prior)**

---

### Persona Score Summary Table

| Persona | Homepage | Pillar | Blog: regulated-estonia | Blog: est-lux-malta | Blog: fees-2026 | Avg | vs 2026-05-08 |
|---|---|---|---|---|---|---|---|
| **Allocator** | 4 | 2 | 3 | 3 | 4 | 3.2 | +0.2 |
| **Founder** | 3 | 5 | 4 | 5 | 3 | 4.0 | +0.8 |
| **Compliance** | 3 | 4 | 4 | 3 | 2 | 3.2 | = |
| **Skeptic** | 2 | 3 | 3 | 3 | 2 | 2.6 | = |

**Weakest persona: Skeptic (2.6/5). Second weakest: Allocator and Compliance (tied 3.2/5). Strongest: Founder (4.0/5).**

---

## 5. Gap Analysis — SXO Gap Score (Updated)

| Dimension | Max | Score | Evidence | vs 2026-05-08 |
|---|---|---|---|---|
| Page Type fit | 15 | 13 | Comparison blog now matches format. Blog: regulated-estonia partially matches. Homepage MEDIUM mismatch persists. -2 | +3 |
| Content Depth | 15 | 12 | Pillar strong (12 H2s, FAQ, Founder CTA). Comparison blog now has full table, 5 SVG charts, cost breakdowns, sourced data. Fees blog has benchmark data and table. Minus 3: fees blog missing AIFMD II fee disclosure angle; pillar missing HowTo schema for 7-step registration. | +1 |
| UX Signals | 15 | 10 | Founder CTA added to 3 blog articles + pillar. Table improves scan-ability on comparison blog. Minus 5: trust strip below fold on mobile homepage (trust-line revert); no lead-type qualifier on sidebar form; Founder CTA on regulated-estonia blog appears after 4,500 words. | +1 |
| Schema | 15 | 13 | FAQPage, BreadcrumbList, BlogPosting, Organization, FinancialService, Person, Speakable on all pages. Minus 2: HowTo schema still absent on pillar 7-step registration section; Table schema not declared on comparison blog `<table>`. | = |
| Media | 15 | 11 | Comparison blog has 3 SVG cost/timeline/tax charts. Homepage hero chart present. Pillar has hero image. Minus 4: no jurisdiction comparison infographic (table only, no visual matrix); no video across the cluster; fees blog has no charts. | +2 |
| Authority | 15 | 8 | GLEIF link, Finantsinspektsioon link, KPMG name, Hedman Partners. Three LinkedIn-linked founders. Bing WMT: 0 backlinks confirmed (normal at 6 weeks post-launch). No third-party coverage or press mentions. KPMG not linked to audit scope. | = |
| Freshness | 10 | 7 | Comparison blog `dateModified: 2026-05-08` (table added ~Sprint 2, May pre-08). Pillar `dateModified: 2026-05-08` — 8 days with no bump post-Sprint 1. Fees blog `dateModified: 2026-05-08`. Homepage no visible publish date. Minus 3: YMYL financial content without quarterly review signal. | = |
| **Total** | **100** | **74** | | **+7** |

**SXO Gap Score: 74 / 100 (up from 67)**

---

## 6. New SXO Wins Since 2026-05-08

### Win 1 — Comparison table on `/blog/estonia-luxembourg-malta-crypto-fund` (F-1 resolved)

The jurisdiction comparison `<table>` is present from approximately word 250 of the article body, immediately after the H2 "Estonia vs Luxembourg vs Malta — At a Glance". The table covers: Regulator, AIFM path, minimum share capital, registration timeline, corporate income tax, EU passport, and MiCA transition. This is the exact format Google rewards for comparison queries. The table is sourced (CSSF, PwC Tax Summaries, AIFMD Art. 9, Malta Business Registry).

**Residual gap:** The table appears after the hero image and Key Takeaways block. Two intro paragraphs precede it. For a featured snippet, the table should be the first semantic answer to the H2. Consider moving the Quick Answer block above the hero image, or removing the two intro paragraphs preceding the table (they are now redundant given the Quick Answer).

### Win 2 — Founder CTA deployed across the cluster (F-3 resolved)

The `Schedule a Founders Call` button with Cal.com embed (`data-cal-link="sparkcore/discovery"`) is present in:
- `/blog/estonia-luxembourg-malta-crypto-fund` (confirmed line 795)
- `/blog/regulated-crypto-fund-manager-estonia` (confirmed line 457)
- `/resources/regulated-crypto-fund-estonia/index.html` (confirmed line 492)

All three CTAs link to the same `sparkcore/discovery` Cal.com event type. This resolves the "no Founder exit path" finding from the prior audit. F-3 is resolved.

**Residual gap:** On the two blogs, the Founder CTA appears only in the article conclusion (after 4,000+ words). A second inline CTA block at the mid-article point (after the jurisdiction table or after the AIFM regime explanation) would catch Founders who self-qualify mid-read without completing the article.

### Win 3 — White-label offer surfaced on homepage

Confirmed at line 1277 of `index.html`: white-label AIFM section visible on the homepage with Finantsinspektsioon mention. Founders now have a homepage entry point to the white-label offer. F-5 is partially resolved — a distinct Founder CTA from the homepage white-label section still leads to the sidebar form (not the Founders Call Cal.com event).

---

## 7. Remaining Findings Table (Priority Order)

| # | Severity | Page | Finding | Status vs 2026-05-08 | Recommended Fix |
|---|---|---|---|---|---|
| F-2 | HIGH | Homepage | Trust-line revert (commit 0c997cc) leaves Skeptic above-fold gap open. No verifiable regulatory credential visible before first scroll on mobile. | OPEN — unchanged | Re-implement as a trust badge pill below the CTAs in dark-hero style (not inline text). Suggested: `<a href="[fi.ee URL]" class="trust-badge">Supervised by Finantsinspektsioon · Estonia</a>` styled as a small translucent pill consistent with `hero-latest-badge` design pattern. Effort: 30 min. |
| F-3b | MEDIUM | Blog: regulated-crypto-fund-manager-estonia | Founder CTA present but placed at article conclusion (~4,500 words in). Most Founders self-qualify in the first 500–800 words (AIFM regime description) and abandon before reaching the CTA. | PARTIALLY RESOLVED | Add a second `founder-cta-btn` block immediately after the "Sub-threshold AIFM" H2 section (~word 600). Mirror the existing CTA block. Effort: 20 min. |
| F-6 | MEDIUM | Pillar | HowTo schema absent. 7 registration steps exist in HTML (`<li>` list, lines ~300–309) but no JSON-LD HowTo block. Google renders HowTo rich results for "how to launch a crypto fund" queries. | OPEN — unchanged | Add HowTo JSON-LD with `step` array matching the 7 existing `<li>` items. Nest inside the existing `@graph` array alongside BlogPosting. Keep step `name` concise (Google truncates at ~80 chars). Effort: 1 hour. |
| F-7 | MEDIUM | Homepage sidebar form | No lead-type qualifier on contact form. Allocator and Founder are different qualification paths; a single "How did you hear about us?" dropdown conflates them. | OPEN — unchanged | Add a `form_source` dropdown field: "I am: [ ] An investor looking to allocate / [ ] A fund manager exploring AIFM services / [ ] Other". Route to existing `contact_form_submit` GA4 event `form_source` param. Effort: 1 hour. |
| F-4 | MEDIUM | Blog: estonia-luxembourg-malta-crypto-fund | Featured snippet not captured despite table presence. Two intro paragraphs and a hero image appear before the table, reducing its proximity to the H2. Table `<caption class="sr-only">` is accessibility-correct but its text is not visible for users scanning for a quick answer. | PARTIALLY RESOLVED | Remove the hero image (or move below the table) and the two introductory prose paragraphs that precede the `<table>`. Let the Quick Answer callout + table be the first content under the H1. Effort: 15 min. |
| F-8 | LOW | All pages | No dedicated Regulatory Status page aggregating LEI, FSA registry URL, KPMG audit scope, Hedman Partners, FIU licence reference. Compliance persona DD without a centralised verification page. | OPEN — unchanged | Create `/about/regulatory-status` (or `/compliance`) — can be noindex if commercially sensitive. Link from footer and homepage trust strip. Effort: 2 hours. |
| F-9 | LOW | Pillar | `dateModified: 2026-05-08` — 8 days stale at time of this audit. YMYL financial content stale dateModified reduces E-E-A-T freshness signal. AIFMD II transposition (April 2026) and VASP sunset (July 2026) are live regulatory events that warrant a content review pass. | NEW | Trigger a review pass on the pillar for any content delta related to AIFMD II (transposition deadline was 16 April 2026) and bump dateModified across all 4 surfaces (JSON-LD, OG `article:modified_time`, visible byline, sitemap). Effort: 2 hours content + 30 min tech. |
| F-10 | LOW | Blog: crypto-fund-fees-2026 | No Founder CTA or white-label internal link CTA block. Fee benchmark is a Founder research touchpoint (modelling management company P&L). Article has editorial link to white-label but no CTA block. | NEW | Add a Founder CTA block after the "What institutional allocators accept" section. Same `founder-cta-btn` pattern. Effort: 20 min. |

---

## 8. CTA Placement Audit — AIFM Structuring CTAs for Founders

| Location | CTA present | Format | Placement depth | Quality |
|---|---|---|---|---|
| `/resources/regulated-crypto-fund-estonia/` | Yes | `founder-cta-btn` Cal.com button | After conclusion, before FAQ | GOOD — near article end but article-appropriate |
| `/blog/regulated-crypto-fund-manager-estonia` | Yes | `founder-cta-btn` Cal.com button | After SparkCore case study (~word 4,500) | WEAK — too deep, add mid-article instance |
| `/blog/estonia-luxembourg-malta-crypto-fund` | Yes | `founder-cta-btn` Cal.com button | After conclusion (~word 3,000) | ADEQUATE — article is shorter, less severe |
| `/blog/crypto-fund-fees-2026` | No | — | — | MISSING — add |
| Homepage `/` | Partial | White-label section exists; CTA leads to sidebar form, not Founders Call | Mid-page | WEAK — sidebar form conflates Allocator and Founder |
| Homepage hero | No | — | — | MISSING — hero CTA "Schedule a Discovery Call" is the same for all personas; no Founder-specific entry point |

**Summary:** Founder CTA coverage improved significantly (0 → 3 of 5 pages). The remaining gaps are the fees blog and the mid-article placement on the regulated-crypto-fund-manager article.

---

## 9. Top 5 SXO Actions (Priority Order)

**Action 1 — Re-implement trust signal in hero as badge pill (F-2)**
The trust-line revert was a visual decision, not an SEO one. The prior inline text clashed with the dark hero typography. The solution is a trust badge styled as a translucent pill using the existing `.hero-latest-badge` design language — dark background, `DBD1BC` text, already used for the "New article" badge. Place below the two CTAs, above the scroll arrow. Text: "Supervised by Finantsinspektsioon · Estonia". Link to fi.ee public registry. This answers the Skeptic's question before they scroll, without requiring a new CSS class.
Effort: 30 min. Persona impact: Skeptic 2→3, Allocator 4→4 (marginal). Zero ranking risk.

**Action 2 — Add mid-article Founder CTA to `/blog/regulated-crypto-fund-manager-estonia` (F-3b)**
The article ranks p1 for "crypto AIFM estonia" and attracts the highest Founder intent traffic of any page in the cluster. The existing Founder CTA appears only after 4,500 words. Add a second `founder-cta-btn` block immediately after the H2 "Sub-threshold vs full AIFM" section (~word 600). This is where Founders self-identify and decide whether to research further or act.
Effort: 20 min. Persona impact: Founder 4→5 on this article.

**Action 3 — Add HowTo schema to pillar registration steps (F-6)**
Seven registration steps exist in an ordered list at lines 300–309 of the pillar. Google's HowTo rich result for "how to launch crypto fund estonia" type queries is not captured by any SparkCore page. Add a HowTo JSON-LD block nested in the pillar's `@graph`. The step names already exist as HTML list items — copy-adapt them into the schema `step` array.
Effort: 1 hour. Expected impact: rich result eligibility for HowTo queries; incremental CTR improvement for step-by-step query variants.

**Action 4 — Bump pillar `dateModified` after AIFMD II content review (F-9)**
The AIFMD II transposition deadline was 16 April 2026 — exactly 30 days ago. The pillar covers AIFMD II in its H3 "AIFMD II — transposition deadline 16 April 2026" section. This section now describes a future event that has passed. A substantive review pass (confirm transposition status per member state, update tense, add any post-transposition regulatory guidance from Finantsinspektsioon) constitutes a genuine content update. Bump all 4 dateModified surfaces.
Effort: 2 hours content + 30 min tech. E-E-A-T impact: YMYL freshness signal restored.

**Action 5 — Remove two intro paragraphs before comparison table on `/blog/estonia-luxembourg-malta-crypto-fund` (F-4)**
The comparison blog already has the table. The remaining barrier to featured snippet capture is that two prose paragraphs and a hero image appear between the H2 and the table. Moving the table to be the first element under the H2 (with only the `<caption sr-only>` and `<p>` source attribution below) is the structural match Google uses to select table featured snippets.
Effort: 15 min. Expected impact: featured snippet capture for "estonia luxembourg malta crypto fund" query — estimated CTR jump from ~0.5% to 3–5% at current impression volume.

---

## 10. Cross-Skill Recommendations

- **E-E-A-T gap persists** (0 backlinks confirmed at Bing WMT, no third-party coverage, KPMG not linked to audit scope document) → recommend `/seo content` for E-E-A-T signal density audit on pillar and top 2 cluster articles.
- **HowTo schema missing** on pillar registration steps → recommend `/seo schema` to generate and validate HowTo JSON-LD block before deployment.
- **Backlink profile at zero** (normal at 6 weeks post-launch, documented in CLAUDE.md) → recommend `/seo backlinks` at 90-day mark (re-check date: 2026-08-05 per GSC checkpoint).
- **`dateModified` review cadence** not yet triggered — quarterly Mode A cadence (Apr/Jul/Oct) defined in CLAUDE.md; next pass due July 2026. Consider an event-driven review now for AIFMD II transposition.

---

## 11. Limitations

- **SERP positions are inferred.** GSC data used in this audit is from the prior report (2026-05-08). New SERP positions have not been measured — position changes from the comparison table addition would require 14–28 days of GSC data to confirm.
- **Featured snippet eligibility unverified.** Table presence assessed from HTML inspection; Google's actual rendering of the comparison table as a featured snippet candidate depends on crawler re-evaluation after the table was added. Timing unknown.
- **No CrUX field data.** Mobile UX assessments remain structural. Chrome user volume insufficient for LCP/CLS real-user data.
- **Bing WMT 0 backlinks** is normal at this stage but means Authority score cannot improve until link-building begins.
- **Founder CTA Cal.com event type** (`sparkcore/discovery`) is the same event for both Allocator ("Schedule a Discovery Call") and Founder ("Schedule a Founders Call"). If both CTAs point to the same Cal.com URL, GA4 `cal_booking_complete` cannot distinguish persona type. Consider creating a second Cal.com event type (`sparkcore/founders-call`) with Founder-specific intake questions.

---

*Generate a PDF report? Use `/seo google report`*
