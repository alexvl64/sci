# SparkCore.fund — Content Cluster Analysis
**Audit date:** 2026-05-06
**Scope:** sparkcore.fund/blog — 22 live EN articles (+ 11 FR translations)
**Analyst:** Semantic Topic Clustering — claude-sonnet-4-6

---

## 1. Blog Inventory — Full Article Map

The blog contains 22 articles beyond the index, not the 11 initially scoped. The user's 11 MD-tracked articles map onto 2 thematic layers, plus an additional 11 "bonus" strategy/explainer articles with no MD source files. Two of the 11 tracked articles have slug mismatches between their MD filename and live HTML path.

### Slug mismatch register

| MD filename | Live HTML slug |
|---|---|
| `how-to-launch-small-aif-estonia-crypto-funds.md` | `how-to-launch-a-crypto-fund-estonia` |
| `white-label-aifm-crypto-funds.md` | `white-label-crypto-fund-manager-services` |

All link counts and matrix data below use the live HTML slugs.

---

## 2. Topic Map — The 11 MD-tracked Articles

```
sparkcore.fund/blog/ (navigation index — 19 internal blog links)
│
├── [CLUSTER A: REGULATION & LICENSING]
│   ├── sub-threshold-aifm-crypto-estonia
│   │   Primary KW: "sub-threshold AIFM crypto Estonia"
│   │   Intent: Informational (procedural)
│   │   Outbound blog links: 11 (HIGHEST)
│   │
│   ├── do-crypto-fund-managers-need-mica-casp-license
│   │   Primary KW: "do crypto fund managers need MiCA CASP license"
│   │   Intent: Informational (regulatory Q&A)
│   │   Outbound blog links: 9
│   │
│   └── how-to-launch-a-crypto-fund-estonia [MD: how-to-launch-small-aif]
│       Primary KW: "how to launch small AIF Estonia crypto fund"
│       Intent: Informational (procedural / step-by-step)
│       Outbound blog links: 5
│
├── [CLUSTER B: JURISDICTION SELECTION]
│   ├── estonia-luxembourg-malta-crypto-fund
│   │   Primary KW: "Estonia vs Luxembourg vs Malta crypto fund"
│   │   Intent: Commercial/Informational (comparison/decision)
│   │   Outbound blog links: 7
│   │
│   ├── estonia-eresidency-crypto-fund-eu
│   │   Primary KW: "Estonia e-residency crypto fund"
│   │   Intent: Informational
│   │   Outbound blog links: 7
│   │
│   └── cost-to-launch-regulated-crypto-fund-europe
│       Primary KW: "cost to launch regulated crypto fund Europe"
│       Intent: Commercial/Informational (cost comparison)
│       Outbound blog links: 6
│
├── [CLUSTER C: FUND STRUCTURE & SERVICES]
│   ├── white-label-crypto-fund-manager-services [MD: white-label-aifm-crypto-funds]
│   │   Primary KW: "white label AIFM crypto funds"
│   │   Intent: Commercial/Informational (service evaluation)
│   │   Outbound blog links: 4
│   │
│   └── regulated-crypto-fund-manager-estonia
│       Primary KW: "regulated crypto fund manager Estonia"
│       Intent: Commercial (service/provider)
│       Outbound blog links: 4
│       Note: No MD source file found in /sci/MD/
│
└── [CLUSTER D: INVESTOR PERSPECTIVE]
    ├── why-invest-in-crypto-funds-2026
    │   Primary KW: "why invest in crypto funds 2026"
    │   Intent: Informational (investor rationale)
    │   Outbound blog links: 5
    │
    ├── crypto-fund-fees-2026
    │   Primary KW: "crypto fund fees 2026"
    │   Intent: Informational (investor research)
    │   Outbound blog links: 3
    │
    └── crypto-fund-for-qualified-investors
        Primary KW: "crypto fund for qualified investors"
        Intent: Informational (investor eligibility)
        Outbound blog links: 1 (NEAR-ORPHAN)
        Note: No MD source file found in /sci/MD/
```

### The 11 additional live articles (no MD source — Strategies & Explainer layer)

| Slug | Inferred Primary KW | Intent | Links out |
|---|---|---|---|
| `what-is-a-crypto-aifm` | what is a crypto AIFM | Informational | 4 |
| `regulated-crypto-investment-fund` | regulated crypto investment fund | Informational | 3 |
| `crypto-fund-vs-etf` | crypto fund vs ETF | Informational | 3 |
| `what-a-market-neutral-crypto-fund-does` | market neutral crypto fund | Informational | 3 |
| `delta-neutral-crypto-strategies-explained` | delta neutral crypto strategies | Informational | 4 |
| `bitcoin-outperformance-strategy-fund` | bitcoin outperformance strategy fund | Informational | 4 |
| `crypto-arbitrage-investment-fund` | crypto arbitrage investment fund | Informational | 4 |
| `crypto-fund-compliance-guide` | crypto fund compliance guide | Informational | 4 |
| `what-an-alternative-investment-fund-platform-does` | alternative investment fund platform | Informational | 4 |
| `what-an-institutional-crypto-fund-manager-does` | institutional crypto fund manager | Informational | 4 |
| `white-label-crypto-fund-platform` | white label crypto fund platform | Commercial | 4 |

---

## 3. Cannibalization Risk Table

Intent classification used: I = Informational, C = Commercial/Informational.

| Pair | Primary KW A | Primary KW B | Overlap Signal | Risk Level | Verdict |
|---|---|---|---|---|---|
| `how-to-launch-a-crypto-fund-estonia` vs `sub-threshold-aifm-crypto-estonia` | "how to launch small AIF Estonia" | "sub-threshold AIFM crypto Estonia" | HIGH — SparkCore appears twice in SERP for combined intent queries; both target same searcher persona (manager starting an Estonia fund) with near-identical procedural content (step-by-step FSA dossier, LPF, FIU) | CRITICAL | Merge or differentiate. `how-to-launch` covers process steps; `sub-threshold` covers threshold/eligibility. These overlap in the 7-step setup section of sub-threshold. Recommend: sub-threshold becomes definitional/eligibility hub; how-to-launch retains the procedural step-by-step and adds firm prerequisites from sub-threshold. Add explicit differentiation nav at top of each. |
| `cost-to-launch-regulated-crypto-fund-europe` vs `crypto-fund-fees-2026` | "cost to launch regulated crypto fund Europe" | "crypto fund fees 2026" | LOW — SERP intent diverges strongly. `cost-to-launch` returns setup/launch cost results (legal, regulatory, one-time); `crypto-fund-fees-2026` returns investor-facing management/performance fee benchmarks. Different audiences (fund launcher vs. fund investor). | LOW | No action needed. These serve orthogonal intents. Note in link strategy: `cost-to-launch` should link to `fees-2026` as supplementary investor context. |
| `white-label-crypto-fund-manager-services` vs `regulated-crypto-fund-manager-estonia` | "white label AIFM crypto funds" | "regulated crypto fund manager Estonia" | MEDIUM — Both are Commercial/Informational targeting a fund manager seeking a provider in Estonia. `white-label-aifm` is structure-agnostic (also covers Luxembourg/Ireland/Liechtenstein); `regulated-crypto-fund-manager-estonia` is Estonia-specific. Partial SERP overlap likely on "white label crypto fund manager Estonia" queries. | MEDIUM | Differentiate by scope: white-label = pan-EU service model explanation; Estonia = SparkCore-specific local expertise page. Ensure each targets distinct head terms. Add explicit cross-link with clear "vs" framing. |
| `estonia-eresidency-crypto-fund-eu` vs `estonia-luxembourg-malta-crypto-fund` | "Estonia e-residency crypto fund" | "Estonia vs Luxembourg vs Malta crypto fund" | LOW-MEDIUM — Shared Estonia angle but distinct intent. e-residency targets searchers starting from the e-residency program; jurisdiction comparison targets searchers deciding between jurisdictions. SERP signals diverge (e-residency = practical setup; comparison = decision guide). | LOW-MEDIUM | Low urgency. Ensure e-residency article links TO the jurisdiction comparison as "next step" when searcher needs cost/tax context. |
| `white-label-crypto-fund-manager-services` vs `white-label-crypto-fund-platform` | "white label AIFM crypto funds" | "white label crypto fund platform" | MEDIUM — Both target "white label" modifiers in crypto fund context. Platform article may compete on "white label crypto fund" head term. | MEDIUM | Differentiate: `manager-services` = AIFM/ManCo service model (regulatory); `platform` = technology platform layer. Ensure `platform` links to `manager-services` as the regulatory wrapper. No MD source for `platform` — flag for content review. |

---

## 4. Internal Link Matrix — 11 Tracked Articles

Rows = source article (links OUT). Columns = target article (receives link).
Notation: 1 = link exists, 0 = no link. Diagonal = self (excluded).

Short codes:
- **COST** = cost-to-launch-regulated-crypto-fund-europe
- **FEES** = crypto-fund-fees-2026
- **MICA** = do-crypto-fund-managers-need-mica-casp-license
- **ERES** = estonia-eresidency-crypto-fund-eu
- **JURI** = estonia-luxembourg-malta-crypto-fund
- **LAUN** = how-to-launch-a-crypto-fund-estonia
- **RCME** = regulated-crypto-fund-manager-estonia
- **SUBT** = sub-threshold-aifm-crypto-estonia
- **WLAB** = white-label-crypto-fund-manager-services
- **INVE** = why-invest-in-crypto-funds-2026
- **QUAL** = crypto-fund-for-qualified-investors

```
SRC \ TGT  COST FEES MICA ERES JURI LAUN RCME SUBT WLAB INVE QUAL
COST        —    0    1    0    1    0    0    1    1    0    0    = 4 out
FEES        0    —    0    0    0    0    0    1    1    1    0    = 3 out
MICA        0    0    —    0    0    1    1    0    0    0    0    = 2 out (+ crypto-fund-compliance-guide, what-is-a-crypto-aifm outside tracked set)
ERES        0    0    1    —    1    0    1    1    0    0    0    = 4 out (+ what-is-a-crypto-aifm)
JURI        0    0    1    0    —    0    1    0    1    0    0    = 3 out (+ what-is-a-crypto-aifm)
LAUN        0    0    0    0    0    —    1    0    1    0    0    = 2 out (+ delta-neutral)
RCME        0    0    0    0    0    1    —    0    1    0    0    = 2 out (+ delta-neutral)
SUBT        0    0    1    0    0    1    1    —    0    0    0    = 3 out (+ crypto-fund-compliance, crypto-fund-vs-etf, what-is-a-crypto-aifm)
WLAB        0    0    0    0    0    1    1    0    —    0    0    = 2 out (+ delta-neutral)
INVE        0    0    1    0    0    1    0    0    1    —    0    = 3 out
QUAL        0    0    0    0    0    0    0    0    0    0    —    = 0 out (ORPHAN)

Incoming:
COST        —    0    0    0    0    0    0    0    0    0    0    = 0 IN (ORPHAN)
FEES        0    —    0    0    0    0    0    0    0    1    0    = 1 IN (near-orphan)
MICA        1    0    —    1    1    0    0    1    0    1    0    = 5 IN
ERES        0    0    0    —    0    0    0    0    0    0    0    = 0 IN (ORPHAN)
JURI        1    0    0    1    —    0    0    0    0    0    0    = 2 IN
LAUN        0    0    1    0    0    —    1    1    1    1    0    = 7 IN (de facto hub)
RCME        0    0    1    1    1    1    —    1    1    0    0    = 9 IN (highest in-degree)
SUBT        1    1    0    1    0    0    0    —    0    0    0    = 3 IN
WLAB        1    1    0    0    1    1    1    0    —    1    0    = 11 IN (highest overall)
INVE        0    1    0    0    0    0    0    0    0    —    0    = 1 IN (near-orphan)
QUAL        0    0    0    0    0    0    0    0    0    0    —    = 0 IN (ORPHAN — no article links to it from tracked set; 6 from bonus layer)
```

### Critical link gaps (tracked articles only)

| Missing Link | Direction | Priority | Rationale |
|---|---|---|---|
| Any article → COST | → `cost-to-launch` | P0 | 0 incoming links from tracked set. Critical commercial article is invisible from within cluster. |
| Any article → ERES | → `estonia-eresidency` | P0 | 0 incoming links from tracked set. Entry-level article for "start from e-residency" persona. |
| Any article → FEES | → `crypto-fund-fees-2026` | P1 | 1 incoming link only. Investor-facing content isolated from rest of cluster. |
| Any article → INVE | → `why-invest-in-crypto-funds-2026` | P1 | 1 incoming link only. Top-of-funnel investor rationale content is near-orphan. |
| COST → LAUN | `cost-to-launch` → `how-to-launch` | P0 | Cost article has no "how to proceed" next step for reader who's decided. |
| COST → ERES | `cost-to-launch` → `estonia-eresidency` | P1 | Cost article compares jurisdictions but doesn't connect to Estonia entry path. |
| LAUN → SUBT | `how-to-launch` → `sub-threshold` | P1 | Procedural article doesn't reference eligibility/threshold article. |
| WLAB → SUBT | `white-label` → `sub-threshold` | P1 | White-label decision depends on threshold status; no link. |
| WLAB → COST | `white-label` → `cost-to-launch` | P1 | White-label cost comparison needs direct link to cost benchmark article. |
| FEES → INVE | `fees` → `why-invest` | P1 | Natural continuation for investor researching costs → rationale. |
| INVE → COST | `why-invest` → `cost-to-launch` | P1 | Investor convinced → next question is cost. |
| QUAL → any | `crypto-fund-for-qualified-investors` | P0 | Article has 0 outbound links to tracked set. Complete internal linking dead-end. |

---

## 5. Missing Topics — Priority List

### P0 — Cluster blockers (no equivalent article exists)

| Missing Topic | Target KW | Rationale |
|---|---|---|
| **Dedicated pillar page** — "Regulated Crypto Fund Estonia: Complete Guide 2026" | "regulated crypto fund Estonia" / "Estonia crypto fund setup" | No true pillar exists. Blog index is navigation, not content. This would be the hub article linking all 11 spokes. Without it, the cluster cannot rank topically for broad head terms. |
| **AIF vs. AIFM explainer** | "what is the difference between AIF and AIFM" | Multiple articles use both terms; no dedicated definitional post clarifies the distinction for non-expert searchers. `what-is-a-crypto-aifm` exists in bonus layer but is not linked from regulation cluster. |
| **Investor onboarding / KYC/AML for crypto funds** | "crypto fund investor onboarding Estonia" / "AIF KYC requirements" | 8-step `how-to-launch` mentions Step 8 (investor onboarding) but no dedicated article exists. High searcher intent for compliance professionals. |

### P1 — Gap fills (topic exists but coverage is thin or misdirected)

| Missing Topic | Target KW | Rationale |
|---|---|---|
| **LPF (Limited Partnership Fund) Estonia deep-dive** | "Estonia limited partnership fund LPF setup" | The LPF structure is mentioned in `how-to-launch` and `sub-threshold` but no standalone article exists. FSA registration, LPF deed, LPF vs. FCP vs. SICAV comparison. |
| **AIFMD II impact on small AIFMs** | "AIFMD II sub-threshold AIFM changes 2025" | `white-label-aifm` mentions AIFMD II briefly; `sub-threshold` does not address the revised Article 3(2) threshold discussions and new ESMA supervisory convergence requirements. |
| **Custody and prime brokerage for crypto funds** | "crypto fund custody solutions EU" | `how-to-launch` mentions custody as Step 7 but no standalone article covers custodian selection, segregated wallet requirements, or AIFMD depositary rules for crypto assets. |
| **Cryptocurrency as AIF asset class** | "can an AIF invest in crypto assets" | Assumed by every article but never explicitly addressed. Needed for searchers questioning legality of crypto-as-AIF-asset before reading the setup guides. |

### P2 — Differentiation enhancements (nice-to-have)

| Missing Topic | Target KW | Rationale |
|---|---|---|
| **Finantsinspektsioon (FSA Estonia) application process** | "Estonia FSA AIFM application 2026" | Detailed walkthrough of actual FSA dossier requirements, timelines, typical rejection reasons. Would differentiate from generic "launch guide" content. |
| **DeFi protocol funds under AIFMD** | "DeFi fund AIFMD compliant" | Emerging query cluster. DeFi-native fund structures using on-chain smart contracts as depositary. Niche but growing. |
| **Tax treatment of crypto fund income Estonia** | "Estonia crypto fund tax 0% CIT" | Estonia's 0% CIT on retained profits is mentioned in `estonia-luxembourg-malta` but warrants a standalone explainer for CFO-persona searchers. |
| **NAV calculation for crypto AIF** | "crypto fund NAV methodology" | Valuation methodology for illiquid/volatile crypto assets under AIFMD is a specialist compliance topic with high YMYL credibility value. |

---

## 6. Hub-and-Spoke Architecture Recommendation

### Current state

There is no hub. The cluster has 22 spokes pointing at each other with no central gravitational page. The blog index (`/blog/`) functions as a directory but contains no topical content, no schema, and no crawl-signal concentration. The homepage is a commercial landing page, not a content hub.

Link authority concentration:
- `white-label-crypto-fund-manager-services` receives 11 incoming links — the de facto hub by link topology, but its content serves a Commercial/Informational intent (white-label service evaluation), not a broad topic pillar role
- `regulated-crypto-fund-manager-estonia` receives 9 incoming links — provider/service page, same issue
- `how-to-launch-a-crypto-fund-estonia` receives 7 incoming links — closest to a procedural pillar

This means link equity is flowing toward service/commercial pages rather than toward a topically broad, authoritative cluster pillar. For YMYL/SERP trust, this is backwards.

### Recommended architecture

**Option A (recommended): Dedicated `/resources/` pillar page**

Create `/resources/regulated-crypto-fund-estonia/` as a 3,500-word pillar article targeting "regulated crypto fund Estonia" (estimated search volume: medium, high commercial intent, low competition from non-AIFMD-specific content).

The pillar should:
- Summarize each of the 5 regulatory tracks (sub-threshold AIFM, full AIFM, white-label AIFM, MiCA CASP, e-residency path)
- Contain a 400-word section per cluster (Regulation, Jurisdiction, Structure, Investor)
- Link to every tracked spoke article with descriptive anchor text
- Be linked from the homepage navigation ("Resources" or "Knowledge Center")
- Receive links FROM every spoke article in the "Read the complete guide" CTA pattern

This creates a true hub-and-spoke topology:

```
/resources/regulated-crypto-fund-estonia/ [PILLAR]
     |
     ├── [REGULATION CLUSTER]
     │   ├── /blog/sub-threshold-aifm-crypto-estonia
     │   ├── /blog/do-crypto-fund-managers-need-mica-casp-license
     │   └── /blog/how-to-launch-a-crypto-fund-estonia
     │
     ├── [JURISDICTION CLUSTER]
     │   ├── /blog/estonia-luxembourg-malta-crypto-fund
     │   ├── /blog/estonia-eresidency-crypto-fund-eu
     │   └── /blog/cost-to-launch-regulated-crypto-fund-europe
     │
     ├── [STRUCTURE CLUSTER]
     │   ├── /blog/white-label-crypto-fund-manager-services
     │   └── /blog/regulated-crypto-fund-manager-estonia
     │
     └── [INVESTOR CLUSTER]
         ├── /blog/why-invest-in-crypto-funds-2026
         ├── /blog/crypto-fund-fees-2026
         └── /blog/crypto-fund-for-qualified-investors
```

**Option B: Elevate `how-to-launch-a-crypto-fund-estonia` to pillar**

Expand the existing launch guide to 3,500+ words, add a "complete overview" section with links to all other articles, and promote it via homepage navigation. Faster to implement (no new URL), but the "how to launch" primary KW is narrower than the broader "regulated crypto fund Estonia" head term. The pillar would rank for procedural queries but miss broader commercial intent.

**Recommendation: Option A.** The `/resources/` URL pattern also creates a crawlable, permanent home for future non-blog assets (factsheets, investor deck PDFs). It aligns with the SCI memory note about "beta.sparkcore.fund dev subdomain in prep" — the pillar can be built on prod without disrupting blog URLs.

### Homepage "Resources" section

Add a "Knowledge Center" or "Resources" section to the homepage with 4 cards (one per cluster) linking to:
1. The pillar page
2. The highest-traffic/most-linked spoke per cluster as a secondary entry

This is separate from the existing homepage services nav and should sit between the "About our funds" section and the footer.

---

## 7. Cluster Maturity Score

### Scoring rubric (100 points)

| Dimension | Max pts | Score | Notes |
|---|---|---|---|
| **Pillar page exists** | 15 | 0 | No true topical pillar. Blog index is navigation only. |
| **Spoke coverage breadth** | 15 | 9 | 4 distinct intent clusters covered; 3 P0 topic gaps; 4 P1 gaps. ~60% of essential topic space covered. |
| **Internal link density** | 20 | 7 | 3 tracked articles have 0 incoming links (COST, ERES, QUAL). Average incoming link count = 3.5 from tracked set. Isolated nodes represent 27% of tracked articles. |
| **Cannibalization hygiene** | 10 | 5 | 1 CRITICAL pair (launch vs. sub-threshold), 2 MEDIUM pairs. 50% of high-risk pairs unresolved. |
| **Intent differentiation** | 10 | 7 | Most articles serve distinct intents. Some Commercial vs. Informational boundary blurring in structure cluster. |
| **Anchor text diversity** | 5 | 2 | Not audited at word level, but link topology shows most links concentrate on 2 commercial targets (white-label, regulated-manager-estonia) suggesting anchor text may be repetitive. |
| **Content depth per article** | 10 | 8 | MD-sourced articles are substantive (1500-3000+ words, data-backed). Bonus-layer articles estimated shorter based on link counts. |
| **Orphan prevention** | 10 | 4 | 2 of 11 tracked articles have 0 incoming links from tracked set. QUAL has 0 outbound links. |
| **Slug / URL hygiene** | 5 | 3 | 2 slug mismatches (MD vs. live HTML). `estonia-eresidency` has wrong canonical pointing to third-party domain. |

**Total: 45 / 100**

### Score interpretation

**45/100 — Immature cluster (D grade).** The content assets individually are high-quality (YMYL-compliant, data-rich), but they operate as disconnected posts rather than a linked cluster. The cluster's primary weaknesses are structural (no pillar, orphaned commercial articles) rather than content-quality (the writing quality is solid). A pillar page + 12 targeted internal link additions would bring this to 65-70/100 without writing a single new article.

---

## 8. Immediate Action Plan

### Sprint 1 (0-1 week, no new content)

1. **Fix 3 orphaned incoming-link articles:**
   - Add link to `cost-to-launch` from: `how-to-launch`, `sub-threshold`, `estonia-luxembourg-malta`
   - Add link to `estonia-eresidency` from: `how-to-launch`, `sub-threshold`, `cost-to-launch`
   - Fix `crypto-fund-for-qualified-investors` to add 3+ outbound links to cluster

2. **Fix near-orphan incoming articles:**
   - Add 2 links pointing to `crypto-fund-fees-2026` from: `cost-to-launch`, `why-invest`
   - Add 2 links pointing to `why-invest-in-crypto-funds-2026` from: `sub-threshold`, `how-to-launch`

3. **~~Fix canonical on `estonia-eresidency-crypto-fund-eu`~~** — *false positive (2026-05-06): canonical correctly self-references `https://sparkcore.fund/blog/estonia-eresidency-crypto-fund-eu` per direct grep verification. Discount this finding.*

4. **Differentiate `how-to-launch` vs `sub-threshold`:** Add a 2-sentence disambiguation header on each article explaining the scope difference and cross-linking with explicit "If you want X, read Y" framing.

### Sprint 2 (1-4 weeks)

5. **Create `/resources/regulated-crypto-fund-estonia/` pillar page** (3,000-3,500 words). Link to/from all 11 tracked articles. Add to homepage nav.

6. **Write P0 missing article:** AIF vs. AIFM explainer — short definitional post (800-1,000 words), link from `sub-threshold`, `do-crypto-fund-managers`, `how-to-launch`.

### Sprint 3 (1-3 months)

7. Write P1 gap articles: LPF deep-dive, AIFMD II changes, custody for crypto funds.
8. Add Homepage "Knowledge Center" section with 4 cluster cards.
9. Resolve `white-label-crypto-fund-platform` vs. `white-label-crypto-fund-manager-services` cannibalization (content differentiation or merge with 301 to services page).

---

*File generated by Semantic Topic Clustering skill — claude-sonnet-4-6 — 2026-05-06*
*Source data: `/home/alex/Documents/Claude/github-projets/sci/blog/*.html` (grep-based link matrix) + MD source files + live SERP overlap verification*
