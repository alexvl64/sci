# Blog Audit — SparkCore Investment (sparkcore.fund)

**Audit Date:** 2026-05-16
**Scope:** 23 EN articles in `blog/` + 6 FR articles in `fr/blog/` (hub `index.html` and `fr/blog/repurposed/` excluded by design)
**Methodology:** Parallel blog-reviewer agents, 5-category 100-point scoring (Content 30 / SEO 25 / E-E-A-T 15 / Tech 15 / AI Citation 15), file-only analysis (no web fetches)
**Site nature:** YMYL — regulated AIFM (SparkCore Investment OÜ, supervised by Finantsinspektsioon, audited by KPMG) addressed to qualified/professional investors only (min €50k)

---

## TL;DR

| KPI | EN (n=23) | FR (n=6) |
|---|---|---|
| **Average score** | **85.0/100 (B/B+)** | **87.2/100 (B+)** |
| 90+ Exceptional | 9 | 1 (strc) |
| 80-89 Strong | 5 | 5 |
| 70-79 Acceptable | 9 | 0 |
| <70 | 0 | 0 |
| YMYL bar met | 23/23 ✓ | 6/6 ✓ |
| Stale >12 mo | 0 | 0 |
| Stale >6 mo | 0 | 0 |
| Stale >3 mo | 0 | 0 |
| `dateModified` window | 100% within 8 days | 100% within 9 days |

**Headline findings**
- Corpus is **homogeneously strong** post the 2026-05-08 sweep (every article re-published that day in EN, FR cluster around May 8-11). No <70 rewrite-tier articles in either locale.
- **Sprint 1 (2026-05-07) noindex→index flips** — all 3 articles scored 93-95: cost-to-launch (95), crypto-fund-fees-2026 (93), estonia-eresidency (93). YMYL bar cleared. Safe to remain indexed.
- **EN↔FR parity is structurally zero — and that is intentional, not a gap.** The FR locale targets a different audience (crypto-curious retail / Cointips channel cross-promo) with market commentary, not fund mechanics. See "Parity" section below — recommendation is to **document the split-audience strategy explicitly** rather than build translations.
- **P0 legal/YMYL risk** in 1 FR article (strc): editorial phrasing "structurellement proche d'un schéma de Ponzi" applied to a named, SEC-listed issuer (Strategy Inc.) — defamation/market-manipulation exposure even with disclaimer. Single-paragraph edit.
- **2 unverified-claim risks** flagged for fact-check: `le-vrai-cout` (Iran war Feb 2026 macro stats sourced FXStreet/Reuters dated April 2026), `agents-ia` (Q1 2026 stablecoin volume 28T$ sourced Cryptonews.net Tier 3).
- **Largest corpus-wide gap (EN)**: 10/23 articles missing FAQPage schema, 15/23 missing SVG/figure visuals — both concentrated in the older March 2026 cohort. Direct AI-citation and dwell-time penalty.

---

## Health Overview

| Metric | Value |
|---|---|
| Total scored articles | 29 (23 EN + 6 FR) |
| Average corpus score | 85.5/100 |
| Articles flagged for **rewrite** (<60) | 0 |
| Articles flagged for **upgrade** (60-79) | 9 (all EN, all in 74-79 band) |
| Articles flagged for **legal review** | 1 (FR/strc — Ponzi language) |
| Articles flagged for **fact-check** | 2 (FR/le-vrai-cout, FR/agents-ia) |
| Cannibalization candidates | 2 EN pairs (white-label-platform vs white-label-services; what-a-market-neutral vs delta-neutral) |
| Orphan pages (heuristic — articles with ≤2 internal blog links) | 2 EN (white-label-crypto-fund-platform, what-a-market-neutral) |
| Future-dated (correctly noindex) | 0 |
| FAQPage schema present | 13/23 EN (57 %) · 6/6 FR (100 %) |
| Self-hosted hero image | ~14/23 EN (newer cohort only) · 5/6 FR (strategies-options uses Unsplash hotlink) |
| Audio narration | 0/23 EN · 2/6 FR (clarity-act, strc) |
| Author Person schema with credentials | 23/23 EN ✓ · 6/6 FR ✓ |
| Body-level YMYL disclaimer | 23/23 EN ✓ · 6/6 FR ✓ |
| Finantsinspektsioon footer attribution | 23/23 EN ✓ · 6/6 FR ✓ |

---

## EN — Per-Article Scores (23 articles)

| File | Score | C/30 | SEO/25 | EEA/15 | T/15 | AI/15 | Modified | Words | YMYL | Top Issues |
|---|---|---|---|---|---|---|---|---|---|---|
| sub-threshold-aifm-crypto-estonia | **96** | 29 | 24 | 15 | 15 | 13 | 2026-05-08 | ~5,000 | ✓ | Length (5k words) — consider pinned TL;DR at top |
| cost-to-launch-regulated-crypto-fund-europe ⭐ | **95** | 29 | 24 | 14 | 14 | 14 | 2026-05-08 | ~2,800 | ✓ | OG image generic vs article-specific |
| do-crypto-fund-managers-need-mica-casp-license | **95** | 29 | 24 | 15 | 14 | 13 | 2026-05-08 | ~3,800 | ✓ | Alt-text length on some chart SVGs |
| estonia-luxembourg-malta-crypto-fund | **94** | 28 | 24 | 14 | 14 | 14 | 2026-05-08 | ~3,050 | ✓ | Title tag 88 chars (over 60-char target) |
| crypto-fund-fees-2026 ⭐ | **93** | 28 | 24 | 14 | 14 | 13 | 2026-05-08 | ~2,600 | ✓ | Verify PwC/Galaxy fee benchmark freshness for H2 2026 |
| estonia-eresidency-crypto-fund-eu ⭐ | **93** | 28 | 24 | 14 | 14 | 13 | 2026-05-08 | ~2,850 | ✓ | One Estonia stat cited via secondary blog vs Statistikaamet primary |
| why-invest-in-crypto-funds-2026 | **93** | 28 | 24 | 14 | 14 | 13 | 2026-05-08 | ~3,600 | ✓ | "55%" stat — verify PwC/AIMA 2025 citation date |
| aif-vs-aifm-crypto-explained | **92** | 27 | 23 | 14 | 14 | 14 | 2026-05-08 | ~1,200 | ✓ | Thin word count for pillar topic; absorb more EU regulator data |
| regulated-crypto-fund-manager-estonia | **90** | 26 | 23 | 14 | 14 | 13 | 2026-05-08 | ~2,462 | ✓ | KPMG cited once — could reinforce as Tier 1 trust signal |
| how-to-launch-a-crypto-fund-estonia | **89** | 26 | 23 | 14 | 13 | 13 | 2026-05-08 | ~2,789 | ✓ | No chart visuals; OG image generic |
| delta-neutral-crypto-strategies-explained | **88** | 26 | 22 | 14 | 13 | 13 | 2026-05-08 | ~2,546 | ✓ | No payoff diagram for quant content |
| crypto-fund-vs-etf | **86** | 25 | 22 | 14 | 12 | 13 | 2026-05-08 | ~1,653 | ✓ | FAQ only 3 questions; comparison sits as prose vs table |
| what-is-a-crypto-aifm | **86** | 25 | 22 | 14 | 13 | 12 | 2026-05-08 | ~1,648 | ✓ | Entity overlap risk with aif-vs-aifm |
| white-label-crypto-fund-manager-services | **83** | 24 | 21 | 14 | 12 | 12 | 2026-05-08 | ~2,569 | ✓ | No FAQ; no visuals; few EU regulator inline cites |
| crypto-fund-compliance-guide | **80** | 23 | 21 | 14 | 11 | 12 | 2026-05-08 | ~1,647 | ✓ | No FAQ; no question-H2s; list-heavy compliance content begs for table |
| crypto-fund-for-qualified-investors | **80** | 23 | 21 | 14 | 11 | 12 | 2026-05-08 | ~1,626 | ✓ | No FAQ; no visuals; section density borderline |
| regulated-crypto-investment-fund | **79** | 22 | 20 | 13 | 11 | 13 | 2026-05-08 | ~1,591 | ✓ | No FAQ; no visuals; title weaker keyword front-loading vs URL slug |
| bitcoin-outperformance-strategy-fund | **78** | 22 | 20 | 13 | 11 | 12 | 2026-05-08 | ~1,678 | ✓ | No FAQ; only 2 ext citations (CoinGecko ×2); zero visuals |
| what-an-institutional-crypto-fund-manager-does | **77** | 22 | 20 | 13 | 11 | 12 | 2026-05-08 | ~1,560 | ✓ | No FAQ; no visuals; prose-only without differentiators |
| crypto-arbitrage-investment-fund | **76** | 22 | 19 | 13 | 11 | 11 | 2026-05-08 | ~1,630 | ✓ | No FAQ; no Quick Answer; zero EU regulator inline citations; no visuals |
| what-an-alternative-investment-fund-platform-does | **76** | 21 | 19 | 13 | 11 | 12 | 2026-05-08 | ~1,503 | ✓ | Thin at 1,503 words for "what is" pillar; weak ext citations |
| what-a-market-neutral-crypto-fund-does | **75** | 21 | 19 | 13 | 11 | 11 | 2026-05-08 | ~1,564 | ✓ | No FAQ; only 2 internal blog links; zero regulator citations; no visuals |
| white-label-crypto-fund-platform | **74** | 21 | 19 | 13 | 11 | 10 | 2026-05-08 | ~1,555 | ✓ | No FAQ; near-duplicate of white-label-manager-services; thin sourcing |

⭐ = Sprint 1 (2026-05-07) noindex→index flip.

### EN Score Distribution

| Band | Count | % | Articles |
|---|---|---|---|
| 90+ Exceptional | 9 | 39 % | sub-threshold, cost-to-launch, do-crypto-mica, estonia-lux-malta, crypto-fund-fees-2026, estonia-eresidency, why-invest, aif-vs-aifm, regulated-crypto-fund-manager-estonia |
| 80-89 Strong | 5 | 22 % | how-to-launch, delta-neutral, crypto-fund-vs-etf, what-is-crypto-aifm, white-label-manager-services |
| 70-79 Acceptable | 9 | 39 % | crypto-fund-compliance-guide, crypto-fund-for-qualified-investors, regulated-crypto-investment-fund, bitcoin-outperformance, what-an-institutional, crypto-arbitrage, what-an-AIF-platform, what-a-market-neutral, white-label-platform |
| <70 | 0 | 0 % | — |

### EN Sub-category averages

| Category | Average | Comment |
|---|---|---|
| Content / 30 | 24.6 | Older Mar-cohort thin (~1,500-1,700 words); newer flagship 2,500-5,000 |
| SEO / 25 | 21.9 | Strong meta hygiene corpus-wide; 1 title-tag overflow (estonia-lux-malta) |
| E-E-A-T / 15 | 13.7 | Author/Person schema universal; KPMG/Finantsinspektsioon footer universal; 10/23 lack inline regulator citations |
| Technical / 15 | 12.7 | 10/23 missing FAQPage schema is the main drag |
| AI Citation / 15 | 12.4 | Citation capsules + question H2s missing on most Mar cohort; 15/23 lack visuals |

---

## FR — Per-Article Scores (6 articles)

| File | Score | C/30 | SEO/25 | EEA/15 | T/15 | AI/15 | Modified | Words | YMYL | Top Issues |
|---|---|---|---|---|---|---|---|---|---|---|
| strc-strategy-yield-sous-remunere-analyse | **91** | 28 | 23 | 15 | 13 | 12 | 2026-05-11 | ~4,900 | ⚠ | "Schéma de Ponzi" applied to named SEC-listed issuer — legal risk; minor anglicisms ("ATM equity", "BB high yield") |
| clarity-act-us-impacts-investisseurs | **89** | 27 | 23 | 14 | 14 | 11 | 2026-05-09 | ~3,300 | ✓ | Heavy untranslated jargon ("Mark it up", "yield deposit-equivalent", "flight to quality", "midterms"); 1 future-dated event presented as fact |
| indicateurs-marche-crypto-actifs | **88** | 27 | 22 | 14 | 13 | 12 | 2026-05-08 | ~5,400 | ✓ | High jargon density (Open Interest, funding, skew, CVD, basis trade); CoinReporter/Amberdata Tier 3-4 for ATH stats |
| agents-ia-blockchain-economie-agentique | **86** | 25 | 22 | 14 | 13 | 12 | 2026-05-08 | ~2,200 | ✓ | Cryptonews.net/MEXC Tier 3 for headline stat (28 T$ stablecoin Q1); residual anglicisms (spending caps, whitelists, default) |
| le-vrai-cout-du-market-timing | **85** | 26 | 22 | 13 | 13 | 11 | 2026-05-08 | ~4,450 | ⚠ | Iran war Feb 2026 macro specifics (S&P -7.8%, Brent +68%) need primary fact-check; emotive framing next to formal disclaimer |
| strategies-options-protection-portefeuille-actions | **84** | 25 | 21 | 13 | 12 | 13 | 2026-05-08 | ~4,800 | ✓ | External Unsplash hotlink hero + og:image (CWV + brand consistency); FAQ schema present but not visibly rendered (extractability loss) |

### FR Score Distribution

| Band | Count | % |
|---|---|---|
| 90+ Exceptional | 1 | 17 % (strc) |
| 80-89 Strong | 5 | 83 % |
| <80 | 0 | 0 % |

### FR Sub-category averages

| Category | Average | Comment |
|---|---|---|
| Content / 30 | 26.3 | Long-form depth (3.3k-5.4k words) is a strength |
| SEO / 25 | 22.2 | Meta hygiene solid; missing `og:locale=fr_FR` and `theme-color` across the locale |
| E-E-A-T / 15 | 13.8 | Author bio + LEI universal; flagged Ponzi-phrasing on strc lowers E-E-A-T defensibility |
| Technical / 15 | 13.0 | FAQ schema 6/6 ✓; strategies-options FAQ not visibly rendered (schema-only) |
| AI Citation / 15 | 11.8 | Lowest sub-cat — heavy jargon load reduces passage citability; Tier 3 sources hurt grounding |

---

## Top 5 Articles to Rewrite (Priority Queue)

Sorted by descending priority (legal risk → YMYL fact-check → rewrite ROI).

### P0 — Legal / YMYL credibility risk (do this week)

| # | File | Locale | Score | Issue | Action | Effort |
|---|---|---|---|---|---|---|
| 1 | strc-strategy-yield-sous-remunere-analyse | FR | 91 | "Structurellement proche d'un schéma de Ponzi" applied to a named, SEC-listed issuer (Strategy Inc.). Defamation / market-manipulation exposure under EU/Estonian standards despite the article disclaimer. | Single-paragraph edit. Soften to "présente certaines caractéristiques d'un système autosustaining par émission" or similar, **citing financial-analyst frames rather than the criminal-law term**. Preserve the analytical conclusion (rendement sous-rémunère le risque 400-500 bps) — drop the loaded label. | 20 min |
| 2 | le-vrai-cout-du-market-timing | FR | 85 | Opening macro claims (S&P -7,8 %, Brent +68 %, gas +40 % suite Iran-USA Feb 2026) sourced FXStreet + Reuters April 2026. If any number is off, YMYL credibility collapses on a fact-check-by-AI scenario. | Run `/blog factcheck` on this article; if any source 404s or stat drift, add `[verified 2026-05-16]` capsule next to each macro stat with the canonical Bloomberg/Reuters terminal URL. | 1h |
| 3 | agents-ia-blockchain-economie-agentique | FR | 86 | Headline stat "28 T$ stablecoin Q1 2026, 76% bots" anchored to Cryptonews.net (Tier 3) — too thin for a flagship YMYL claim. | Re-source to Visa Onchain Analytics, Chainalysis, or Allium primary data. Add Wikipedia-style citation capsule near the stat. | 45 min |

### P1 — Rewrite / cannibalization (this month)

| # | File | Locale | Score | Issue | Action | Effort |
|---|---|---|---|---|---|---|
| 4 | white-label-crypto-fund-platform | EN | 74 | Near-duplicate intent vs `white-label-crypto-fund-manager-services` (83). Thin sourcing, no FAQ, only 2 internal links. **Cannibalization risk on "white label crypto fund" keyword cluster.** | **Decision needed**: merge into the manager-services article (301 redirect) OR differentiate platform = infrastructure/tech stack, services = operational outsourcing. If keep: full rewrite to 2,500 w + FAQ + 2 SVGs + 5 inline regulator cites. | 4h merge / 6h differentiate |
| 5 | what-a-market-neutral-crypto-fund-does | EN | 75 | Overlaps with `delta-neutral-crypto-strategies-explained` (88). No FAQ, no regulator citations, no visuals, only 2 internal blog links. | Rewrite as **strategy-specific** (market-neutral = pair-trades + cash-and-carry + arbitrage funding) and explicitly internal-link to delta-neutral as the broader umbrella. Add FAQ + 1 payoff/PnL chart. | 4h |

### Secondary upgrade tier (P2 — backlog)

| # | File | Locale | Score | Action |
|---|---|---|---|---|
| 6 | crypto-arbitrage-investment-fund | EN | 76 | Add FAQ schema, 3 inline EU regulator citations (MiCA Art 4 on market manipulation, ESMA arbitrage guidance), 1 SVG (yield-source breakdown). |
| 7 | what-an-alternative-investment-fund-platform-does | EN | 76 | Thicken to 2,000-2,500 w. Add FAQ + comparison table (platform vs standalone vs white-label). |
| 8 | what-an-institutional-crypto-fund-manager-does | EN | 77 | Add FAQ, 1 SVG (fund manager value-chain), 3 institutional-grade cites (Fidelity Digital Assets, BlackRock IBIT 13F, BNY Mellon). |
| 9 | regulated-crypto-investment-fund | EN | 79 | Add FAQ; consider title rewrite to front-load "What is a Regulated Crypto Investment Fund?" for keyword alignment with URL slug. |
| 10 | bitcoin-outperformance-strategy-fund | EN | 78 | Add FAQ + 1 chart (BTC vs SPX 10y total return); upgrade citations beyond CoinGecko (add S&P DJI BTC index, BlackRock BTC ETF flows). |

---

## Action Queue — Corpus-wide (P2-P3)

### P2 — Programmatic improvements (batch)

| ID | Action | Scope | Effort | Score Impact |
|---|---|---|---|---|
| CW-1 | Add FAQPage schema + 4-6 visible Q&A block | 10 EN articles missing FAQ (all from Mar-2026 cohort) | ~30 min/article × 10 = 5h | +1-2 pts each on AI Citation + Technical |
| CW-2 | Add 1 SVG visual minimum per article (chart, diagram, payoff) | 15 EN articles + 1 FR (strategies-options needs self-hosted hero) | ~45 min/article × 16 = 12h | +1 pt each on AI Citation + Content engagement |
| CW-3 | Replace generic `/meta-image.webp` OG with article-specific image | ~14 EN articles | ~15 min/article × 14 = 3.5h | Social CTR; no audit-score impact |
| CW-4 | Add `og:locale=fr_FR` + `meta name="theme-color"` to all FR articles | 6 FR articles | 1h batch | +0.5 pt SEO |
| CW-5 | Replace Unsplash external hotlink with self-hosted hero | strategies-options (FR) | 30 min | +1 pt Tech (CWV) |
| CW-6 | Tighten title tag length on `estonia-luxembourg-malta-crypto-fund` from 88 → 60 chars | 1 EN article | 5 min | +0.5 pt SEO |

### P3 — Strategic decisions (require user input)

| ID | Decision | Why it matters |
|---|---|---|
| SD-1 | **Document EN↔FR split-audience strategy explicitly** (CLAUDE.md + sitemap policy) — OR commit to translating top 5-9 EN flagships into FR | Currently 0 articles have a cross-locale equivalent. AI crawlers (and SEO) see this as "missing hreflang pairs". Either ship hreflang pairs OR ship a content-strategy note that explains why FR is editorially independent. |
| SD-2 | **External reviewer / co-author** for technical strategy articles (delta-neutral, market-neutral, arbitrage) | Alexandre VINAL's credentials are "operator/founder authority" — not CFA/CAIA. For YMYL technical strategy content, adding a "Reviewed by [KPMG auditor / compliance officer]" line would lift E-E-A-T defensibility from 13.7 → 14.5+. |
| SD-3 | **Audio narration rollout policy** — currently 2/6 FR have it (clarity-act, strc), 0/23 EN | Decide: ship audio on all FR new articles (+ retrofit 4 remaining), or scope down to flagship articles only? EN locale not started — same question. |
| SD-4 | **Fact-check cadence for time-sensitive articles** (le-vrai-cout, indicateurs, agents-ia, clarity-act) | These articles cite 2026-specific market events. A 90-day re-verification cron (similar to dsungkur's freshness sweep) would protect YMYL credibility from quiet stat drift. |

---

## Freshness Signals

**Reference date:** 2026-05-16.

| Bucket | EN | FR |
|---|---|---|
| Modified ≤ 30 days | 23 (100%) | 6 (100%) |
| Modified 30-90 days | 0 | 0 |
| Modified 90-180 days | 0 | 0 |
| Modified > 180 days | 0 | 0 |
| Modified > 365 days | 0 | 0 |

All articles are within the 30-day freshness window — the 2026-05-08 sweep re-published the entire EN corpus on a single day, and FR articles cluster May 8-11.

**Caveat:** `dateModified` reflecting a one-shot batch sweep can be a false-positive freshness signal. **Inline content freshness varies**: some Mar-cohort EN articles (white-label-platform, what-a-market-neutral, what-an-AIF-platform) likely had only metadata/schema touched, not body content. **Recommendation: differentiate "republish-only" from "content-refresh" with a `lastReviewed` vs `dateModified` distinction** — Google December 2025 Core Update penalizes "fake freshness" signals.

Suggested freshness sweep cadence:
- **Top 9 flagship (90+) articles**: 90-day light review (next: 2026-08-08)
- **Sprint 1 noindex→index flips**: 60-day stat verification (next: 2026-07-07)
- **FR market-commentary articles (le-vrai-cout, indicateurs, agents-ia, clarity-act)**: 60-day fact-check on time-sensitive macro claims
- **strc article**: post-legal-edit, then 90-day yield/balance sheet update cycle (the underlying Strategy Inc. position changes weekly)

---

## EN↔FR Parity Analysis

**Finding: zero direct parity. Zero shared topic.**

| EN article (sample) | FR equivalent? |
|---|---|
| cost-to-launch-regulated-crypto-fund-europe | None |
| do-crypto-fund-managers-need-mica-casp-license | None |
| sub-threshold-aifm-crypto-estonia | None |
| estonia-eresidency-crypto-fund-eu | None |
| white-label-crypto-fund-manager-services | None |
| crypto-fund-vs-etf | None |
| ... (all 23 EN) | None |

| FR article | EN equivalent? |
|---|---|
| strc-strategy-yield-sous-remunere-analyse | None |
| clarity-act-us-impacts-investisseurs | None |
| indicateurs-marche-crypto-actifs | None |
| le-vrai-cout-du-market-timing | None |
| strategies-options-protection-portefeuille-actions | None |
| agents-ia-blockchain-economie-agentique | None |

**This is intentional, not a gap.** The two locales serve **different audiences with different topics**:

- **EN locale** = regulated AIFM mechanics, fund-launch buyer journey, MiCA/AIFMD/Estonian compliance — institutional B2B
- **FR locale** = crypto market commentary, options strategies, on-chain indicators, regulatory news for retail/informed individuals — Cointips YouTube cross-promotion audience

**Hreflang implications:**
- Each article currently declares `hreflang="en"` self-referential (EN) or `hreflang="fr"` self-referential (FR) with no `alternate` cross-reference.
- Google does not penalize asymmetric hreflang per se — it just ignores the cross-link signal.
- Two viable paths:

  **Path A — Maintain split-audience strategy (recommended)**
  - Document explicitly in `CLAUDE.md` (project-level) and in `llms.txt` that EN and FR are editorially independent content tracks targeting different ICPs.
  - Add a one-line note in each blog `index.html` hub explaining the locale focus.
  - Adjust sitemap entries to declare locale without claiming `x-default` cross-reference.
  - Effort: 1h documentation + 0 content work.

  **Path B — Build hreflang pairs (heavy)**
  - Translate top 5-9 EN flagships into FR (cost-to-launch, sub-threshold, do-crypto-mica, estonia-eresidency, estonia-lux-malta, why-invest, crypto-fund-fees-2026 priority).
  - At ~3-5h per high-quality translation × 5-9 = 15-45h.
  - Brings hreflang pair coverage to 22-39% on the EN side.
  - **Tradeoff**: dilutes FR locale focus from "crypto retail commentary" to a hybrid feed.
  - Use only if Estonian/French institutional investor channel is being actively prospected.

**Recommendation: Path A.** The current split is editorially defensible (different ICPs, different topics, different channels — Cointips YouTube for FR, LinkedIn/EFAMA-tier for EN). Document the split, don't paper over it with token translations.

---

## Cannibalization

| Pair | Score gap | Recommendation |
|---|---|---|
| white-label-crypto-fund-platform (74) vs white-label-crypto-fund-manager-services (83) | 9 | **Merge or differentiate** (see P1 #4). Same primary keyword "white label crypto fund". |
| what-a-market-neutral-crypto-fund-does (75) vs delta-neutral-crypto-strategies-explained (88) | 13 | **Differentiate**: market-neutral = pair-trades + cash-and-carry; delta-neutral = options/perpetuals hedging. Cross-link explicitly. (see P1 #5) |
| aif-vs-aifm-crypto-explained (92) vs what-is-a-crypto-aifm (86) | 6 | **Light differentiation**: aif-vs-aifm is the comparison piece (entity vs entity); what-is-crypto-aifm is the explainer. Already different intents, but entity overlap risk noted in EN audit. Monitor SERP overlap; differentiate further if both rank for the same query. |

No other cannibalization detected within either locale.

---

## YMYL E-E-A-T Critical Review

YMYL bar **met across all 29 articles** on the baseline check:
- Named author with credentials + LinkedIn + Person schema: 29/29 ✓
- Visible byline: 29/29 ✓
- Body-level disclaimer ("ne constitue pas un conseil en investissement" / "not investment advice"): 29/29 ✓
- Footer-level disclaimer + Finantsinspektsioon URL + LEI: 29/29 ✓
- "Qualified/professional investors only" framing: 29/29 ✓

**Specific YMYL concerns flagged:**

| # | Article | Concern | Severity |
|---|---|---|---|
| 1 | FR/strc | "Schéma de Ponzi" on named SEC-listed issuer | **HIGH** — legal risk |
| 2 | FR/le-vrai-cout | Iran war Feb 2026 macro specifics need primary verification | MEDIUM — credibility risk if any stat drifts |
| 3 | FR/agents-ia | Headline 28 T$ stablecoin stat sourced Cryptonews.net (Tier 3) | MEDIUM — primary-source upgrade needed |
| 4 | FR/indicateurs | CME OI ATH 45 Md$ sourced CoinReporter (Tier 3-4) | MEDIUM — replace with CFTC COT report |
| 5 | FR/clarity-act | White House July 4 2026 target presented as confirmed; "Brian Armstrong a posté un laconique « Mark it up »" needs permalink fallback | LOW — fact-check apparatus needed |
| 6 | EN — multiple | Author credentials are operator/founder authority, not certified FA/CFA/CAIA | LOW — defensible given Finantsinspektsioon-supervised AIFM context; adding co-author/reviewer would lift defense (SD-2) |

---

## Implementation Effort Summary

| Tier | Items | Total effort | Score impact |
|---|---|---|---|
| **P0 — Legal/YMYL** | 3 (strc edit, le-vrai-cout fact-check, agents-ia source upgrade) | ~2h | Legal protection + +1-2 pts per article |
| **P1 — Rewrites** | 2 (white-label-platform, what-a-market-neutral) | ~8h | +5-10 pts per article; cannibalization closed |
| **P1 — Secondary upgrades** | 5 (crypto-arbitrage, what-an-AIF-platform, what-an-institutional, regulated-crypto-investment-fund, bitcoin-outperformance) | ~10h | +3-5 pts per article |
| **P2 — Corpus-wide programmatic** | 6 batches (CW-1 to CW-6) | ~22h | +1-2 pts per affected article |
| **P3 — Strategic decisions** | 4 (parity policy, co-author, audio policy, fact-check cadence) | 1h user decision + variable execution | Strategic positioning |
| **TOTAL** | — | **~43h execution + decisions** | Corpus average projected: 85.5 → 90+ |

---

## Notes on Methodology / Limitations

- **No web fetching** — scores rely on file contents only. Citation freshness (whether sources are still live at their URL, whether stats have drifted in source publications) was not verified. Use `/blog factcheck <file>` on flagged articles.
- **Word counts are byte/markup estimates**, not formal word counts. Within ±10%.
- **Hub `index.html` pages** (EN and FR) were not scored per-post but spot-checked structurally intact.
- **`fr/blog/repurposed/`** folder was excluded per scope (contains social/discord/LinkedIn repurposed content from `/blog repurpose`, not original articles).
- **No `dateModified` drift was checked vs underlying content drift** — see Freshness section caveat about the May 8 batch republish.
- **No SERP / GSC data was pulled** — for that, run `/blog google search-console <url>` against flagged articles to see if low-scoring articles are also under-performing in impressions/clicks.

---

## Suggested Next Steps

1. **This week**: Edit strc Ponzi paragraph (20 min) → eliminates highest legal exposure.
2. **This week**: Run `/blog factcheck fr/blog/le-vrai-cout-du-market-timing.html` and `/blog factcheck fr/blog/agents-ia-blockchain-economie-agentique.html` → close P0 fact-check gaps.
3. **Decision call**: SD-1 parity policy. Pick Path A (document split) or Path B (translate top flagships). Recommendation Path A.
4. **Next sprint (CW-1)**: Batch-add FAQPage schema to the 10 EN articles missing it. Can be parallelized via `/blog rewrite <file>` with a `--faq-only` style brief.
5. **Schedule**: 60-day freshness re-audit cron (next: 2026-07-16). Watchdog flag if `dateModified` drifts >90 days on any 90+ flagship.

---

## Report references

- EN audit: this file (per-article table + cross-cutting findings)
- FR audit: this file (per-article table + cross-cutting findings)
- Source articles: `/home/alex/Documents/Claude/github-projets/sci/blog/` (23 EN) + `/home/alex/Documents/Claude/github-projets/sci/fr/blog/` (6 FR)
- Related audits: `MD/seo/audit-2026-05-16/` (technical SEO, schema, GEO/AI, SXO, sitemap, google-api)
- Previous content audit: none — this is the first blog audit for sci
- Adjacent skill: `/blog factcheck <file>` for source verification on flagged YMYL articles
