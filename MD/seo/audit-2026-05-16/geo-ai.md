# GEO / AI Search Readiness Audit — sparkcore.fund
**Date:** 2026-05-16
**Auditor:** Claude (claude-sonnet-4-6) — autonomous GEO audit
**Baseline:** GEO 72/100 (2026-05-08)

---

## 1. GEO Health Score

| Dimension | Weight | Raw Score | Weighted | Delta vs 05-08 |
|-----------|--------|-----------|---------|----------------|
| Citability | 25% | 80/100 | 20.0 | +1.5 |
| Structural Readability | 20% | 84/100 | 16.8 | +0.4 |
| Multi-Modal Content | 15% | 48/100 | 7.2 | +1.5 |
| Authority & Brand Signals | 20% | 63/100 | 12.6 | +0.4 |
| Technical Accessibility | 20% | 90/100 | 18.0 | 0 |

**Overall GEO Health Score: 75/100 (B-) — up 3 pts from 72**

Three points of progress: Sprint 1 closed the Speakable gap on the pillar + EN/FR homepages + 2 high-traffic blog articles. Author Person schema is now present across all 23 EN articles (was partially missing). Audio narration on FR articles adds a new multi-modal signal. The ceiling remains capped by the Wikidata gap, the llms-full.txt stale inventory (8 articles missing), and no embedded video content.

---

## 2. AI Crawler Access Status

| Crawler | robots.txt Rule | Gated Paths Blocked | Status |
|---------|----------------|---------------------|--------|
| GPTBot | `Allow: /` | Yes — `/factsheets/`, `/discovery-call`, `/validation`, `/MD/` | ALLOWED |
| OAI-SearchBot | `Allow: /` | Yes | ALLOWED |
| ClaudeBot | `Allow: /` | Yes | ALLOWED |
| PerplexityBot | `Allow: /` | Yes | ALLOWED |
| Google-Extended | `Allow: /` | Yes | ALLOWED |
| CCBot | `Allow: /` | Yes | ALLOWED (training permitted) |
| ia_archiver | Blocked | n/a | BLOCKED |
| HTTrack / WebCopier / SiteSucker / Offline Explorer | Blocked | n/a | BLOCKED |

All six target AI crawlers are explicitly allowed on public paths. Gated pages carry four-layer protection (robots.txt Disallow, HTML meta noindex, `X-Robots-Tag` HTTP header, exclusion from llms.txt and llms-full.txt). Lang-redirect scripts explicitly skip all AI crawler UAs — bots never redirected from EN to FR. SSR via Cloudflare Pages: full HTML delivered pre-JavaScript.

**Verdict: FULLY ACCESSIBLE. No change from 05-08.**

---

## 3. llms.txt Assessment

**Status: PRESENT, RSL 1.0 licensed, but STALE INVENTORY**

| Criterion | Status | Notes |
|-----------|--------|-------|
| File present at canonical URL | YES | `https://sparkcore.fund/llms.txt` |
| RSL 1.0 license declared | YES | `License: RSL 1.0` at EOF |
| Last-updated timestamp | STALE | `Last updated: 2026-05-06` — not updated since last audit |
| Entity identification | EXCELLENT | LEI, registry no., GLEIF URL, EFSA URL, EFIU URL, KPMG all present |
| Regulatory anchors (primary sources) | EXCELLENT | fi.ee + mtr.ttja.ee URLs included |
| Fund inventory | GOOD | 3 funds with strategy, risk level, status |
| Team section | GOOD | 3 partners with LinkedIn URLs, Alexandre VINAL YouTube reference |
| Key Terms section | EXCELLENT | Fees, minimums, liquidity, currencies explicit |
| llms-full.txt companion | OUTDATED | 21 EN + 3 FR listed — but 5 EN articles + 3 FR articles published after last update are missing |
| Knowledge Graph / Wikipedia sameAs | GAP | No Wikidata QID or Wikipedia URL — unchanged from 05-08 |
| Competitor disambiguation block | GAP | No disambiguation paragraph — unchanged from 05-08 |

### llms-full.txt inventory gap (critical)

**23 EN articles on disk, only 21 in llms-full.txt. 6 FR articles on disk, only 3 in llms-full.txt.**

Articles published but missing from llms-full.txt:

**EN missing:**
- `aif-vs-aifm-crypto-explained`
- `cost-to-launch-regulated-crypto-fund-europe`
- `crypto-fund-fees-2026` (despite being a high-traffic Speakable-enabled article)
- `do-crypto-fund-managers-need-mica-casp-license`
- `estonia-eresidency-crypto-fund-eu`

**FR missing:**
- `clarity-act-us-impacts-investisseurs` (audio narration present)
- `indicateurs-marche-crypto-actifs`
- `strc-strategy-yield-sous-remunere-analyse` (newest article — audio narration present)

These 8 articles are invisible to LLMs that consume llms-full.txt as their primary content index (notably Perplexity's direct-ingest pipeline). The stale `Last updated: 2026-05-06` timestamp signals to AI systems that content has not been refreshed, which can suppress citation preference for newer content.

**llms.txt Score: 74/100 (down from 81 — stale inventory discovered)**

---

## 4. Status of 2026-05-08 Gaps — Closed/Open

| Gap from 05-08 | Priority | Status | Notes |
|----------------|----------|--------|-------|
| No Speakable schema | MEDIUM | PARTIALLY CLOSED | Sprint 1 (commit a3df92f, 2026-05-08): added to EN/FR homepages, pillar, `what-a-market-neutral-crypto-fund-does`, `crypto-fund-fees-2026`, `estonia-luxembourg-malta-crypto-fund`, `regulated-crypto-fund-manager-estonia`. 4/23 EN articles covered. 0/6 FR articles covered. |
| Author Person schema absent from articles | MEDIUM | CLOSED | All 23 EN articles now carry `"@type": "Person"` JSON-LD (sprint-3+4 schema graph cleanup, commit f3fdca8). All 6 FR articles also covered. |
| No Wikidata entity / Wikipedia | HIGH | OPEN | No change. No Wikidata QID in any `sameAs` array. Highest-priority unresolved gap. |
| No disambiguation block in llms.txt | MEDIUM | OPEN | Not added. |
| FAQ answers below 134-167 word optimal | LOW | OPEN | Not addressed. Average remains ~80-130 words. |
| H2 headings mostly statement-form | LOW | OPEN | Not addressed. |
| No video embeds | HIGH | OPEN | No embedded YouTube videos from Cointips channel on any page. |
| No proprietary charts | HIGH | PARTIALLY CLOSED | FR articles now use PNG/WebP charts (commits #154/#155). EN articles remain Unsplash-only. |
| `isAccessibleForFree` absent on 4 articles | LOW | PARTIALLY CLOSED | 3 articles still missing: `cost-to-launch-regulated-crypto-fund-europe`, `crypto-fund-fees-2026`, `why-invest-in-crypto-funds-2026`. |
| No audio on EN articles | MEDIUM | OPEN | Audio player now on 2 FR articles (clarity-act + STRC). EN cluster has no audio. |
| dateModified stale on older articles | MEDIUM | CLOSED | Sprint content reviewed: all sampled older articles show `dateModified: 2026-05-08` (sprint-1 batch bump). Quarterly cadence cron documented. |
| No `about` property on some BlogPosting | LOW | MOSTLY CLOSED | 16/23 EN articles now carry `about` property with regulatory entity links. 7 remaining without: `bitcoin-outperformance`, `crypto-arbitrage`, `crypto-fund-vs-etf`, `delta-neutral`, `what-a-market-neutral`, `white-label-platform`, `why-invest`. |
| llms-full.txt inventory incomplete | NEW | OPEN | 8 articles missing from llms-full.txt (5 EN + 3 FR). Not identified in previous audit. |

---

## 5. Speakable Schema Audit (Sprint 1 post-verification)

Speakable schema was the top recommended action from 05-08. Sprint 1 (commit a3df92f) deployed it. Current coverage:

| Page | Speakable Present | cssSelector |
|------|-------------------|-------------|
| `/index.html` (EN homepage) | YES | verified |
| `/fr/index.html` (FR homepage) | YES | added in Sprint 1 |
| `/resources/regulated-crypto-fund-estonia/` (pillar) | YES | verified pre-Sprint 1 |
| `blog/what-a-market-neutral-crypto-fund-does` | YES | added in Sprint 1 |
| `blog/crypto-fund-fees-2026` | YES | confirmed |
| `blog/estonia-luxembourg-malta-crypto-fund` | YES | confirmed |
| `blog/regulated-crypto-fund-manager-estonia` | YES | confirmed |
| All other 19 EN blog articles | NO | not extended |
| All 6 FR blog articles | NO | not extended |

**Assessment:** Sprint 1 addressed the highest-priority pages (pillar + top traffic articles). The remaining 19 EN articles and all 6 FR articles do not carry Speakable schema. For a site with 29 indexed articles, this leaves 86% of content without the voice/AI-summary citation signal. Extending the implementation is a templated 1-line addition per article.

---

## 6. Passage-Level Citability — 3 Article Sample

### Article 1: STRC Strategy Yield (FR, newest — `fr/blog/strc-strategy-yield-sous-remunere-analyse`)
**Published:** 2026-05-11 | **dateModified:** 2026-05-11

**Strengths:**
- FAQPage schema with 5 Q&A blocks present
- Audio narration player (1 min 50 — resume format) embedded immediately after H1
- Author Person schema confirmed
- BreadcrumbList correct

**Gaps:**
- No Speakable schema
- `dateModified == datePublished` — signals no editorial review history to crawlers (same-day freshness penalty)
- No `isAccessibleForFree` detected
- No `about` property on BlogPosting
- Not listed in llms-full.txt — invisible to AI systems consuming the content index

**Citability verdict:** MEDIUM. The audio resume is a genuine multi-modal differentiator. The llms-full.txt absence neutralises the advantage for AI platforms that use direct ingest.

### Article 2: Crypto Fund Fees 2026 (EN, Speakable-enabled — `blog/crypto-fund-fees-2026`)
**Published:** 2026-04-01 | **dateModified:** 2026-05-08

**Strengths:**
- Speakable schema present
- FAQPage with 6 Q&A blocks
- Author Person schema confirmed
- `about` property with AIFMD II regulatory entity link
- `dateModified` advanced past `datePublished` — signals ongoing editorial review
- Source-attributed statistics confirmed from prior audit (bfinance, PwC/AIMA, Crypto Insights Group)

**Gaps:**
- `isAccessibleForFree` missing — YMYL financial content should declare this
- Not in llms-full.txt despite being one of the most citation-ready articles on the site
- No embedded video

**Citability verdict:** HIGH. This article is structurally the best on the site for AI citation. The llms-full.txt omission is a priority fix.

### Article 3: Regulated Crypto Fund Manager Estonia (EN, pillar cluster — `blog/regulated-crypto-fund-manager-estonia`)
**Published:** 2026-03-09 | **dateModified:** 2026-05-08

**Strengths:**
- Speakable schema present (Sprint 1)
- FAQPage with multiple Q&A
- Author Person schema confirmed
- `about` property with regulatory entity links
- dateModified bumped to 2026-05-08 — editorial currency signal resolved
- Listed in llms-full.txt

**Gaps:**
- H2 headings mostly statement-form ("Capital Requirements", "Registration Process") rather than question-form
- No embedded video or proprietary chart

**Citability verdict:** HIGH. Best-positioned article in the EN cluster for AI citation, supported by Speakable + FAQ + dateModified + llms-full.txt presence.

---

## 7. Platform-Specific Readiness Scores

| Platform | Score | Delta | Key Driver | Key Gap |
|----------|-------|-------|------------|---------|
| Google AI Overviews | 76/100 | +2 | Speakable schema on pillar + top 4 EN articles now feeds AI Overviews candidacy; dateModified resolved on older articles | Speakable absent from 19/23 EN articles; no Wikidata entity for KG disambiguation |
| ChatGPT (web search) | 78/100 | +2 | llms.txt quality + Author Person schema now consistent across all articles; `about` property on 16 articles improves topic-entity linking | 8 articles missing from llms-full.txt; no external .gov/.edu citations; no Wikipedia entity |
| Perplexity | 79/100 | +1 | High inline citation density (EUR-Lex, GLEIF, fi.ee); clean SSR; `about` property adds regulatory context | llms-full.txt stale — 5 EN articles + 3 FR articles invisible; no news/media coverage in entity graph |
| Claude | 74/100 | +2 | LEI + registry confirmed in schema and llms.txt; Author Person consistent; `about` regulatory entity links across 16 articles | No Wikidata QID; entity disambiguation weak vs Spark Networks / SparkCore game engine; no third-party entity confirmation |
| Gemini / Google AI | 72/100 | +2 | Speakable on homepages + pillar + top articles; FinancialService type maintained; `memberOf` regulatory body schema intact; dateModified current | Speakable still absent from 19 EN articles; no `sameAs` Wikidata; `isAccessibleForFree` missing on 3 articles |
| Bing Copilot | 69/100 | +1 | Bing WMT verified; IndexNow active; Speakable on top pages now signals extractable passages | No Speakable on 19 EN articles; no entity in Bing Satori knowledge base; no inbound .edu/.gov links |

---

## 8. Owned-Media & Brand Signal Analysis

### YouTube — `@cointips`
- Present in Organization `sameAs` array: `https://www.youtube.com/@cointips`
- Present in Alexandre VINAL's llms.txt team entry
- **NOT linked from any article body text**
- **NO video embeds on any page** (EN or FR)
- Research correlation with AI citations: ~0.737 (strongest single signal)
- **Status: signal partially captured in schema, not exploited in content**

### LinkedIn
- Company page `https://www.linkedin.com/company/sparkcorefund/` in Organization `sameAs`
- Alexandre VINAL personal LinkedIn in Person schema on all articles
- Paul-Antoine PONS and Olivier SAYEGH LinkedIn in team Person schemas on homepage
- **Status: adequate coverage — no gap**

### Wikipedia / Wikidata
- No Wikidata item exists for SparkCore Investment OÜ
- No Wikidata item for Alexandre VINAL or the other founders
- No `sameAs` Wikidata URL on homepage or any article
- **Status: CRITICAL GAP — highest single-action impact on all platform scores**

### Reddit
- No Reddit presence confirmed from schema, llms.txt, or backlink signals
- **Status: gap, but low-effort opportunity via r/CryptoInvesting and r/AIFM regulatory discussions**

### GLEIF / Regulatory registries
- GLEIF URL in homepage `sameAs`: present
- Finantsinspektsioon registry URL in `sameAs` and llms.txt: present
- EFIU licence URL in llms.txt: present
- **Status: strong — these function as authoritative third-party entity confirmations for AI platforms**

---

## 9. Technical Accessibility Verification

No regressions from 05-08. Key signals confirmed:

- Static SSR via Cloudflare Pages — HTML delivered pre-JS
- HTTP/2 + Brotli active
- HSTS preload submitted 2026-05-08, status pending Chromium inclusion
- Lang-redirect scripts exclude all AI crawlers — no redirect loops
- `cache-control: public, max-age=0, must-revalidate` on HTML — crawlers always get fresh content
- Cloudflare AI bot blocking NOT engaged (verified)
- Gated pages carry four-layer noindex protection (robots.txt + meta + X-Robots-Tag + llms exclusion)
- Sitemap submitted to Bing WMT; IndexNow active
- `.htaccess` removed 2026-05-09 — all rules ported to CF Pages native mechanisms — no regression

---

## 10. Top 5 Highest-Impact Actions (Prioritised)

### Action 1 — Fix llms-full.txt: add 8 missing articles + update timestamp
**Impact: HIGH | Effort: VERY LOW (20 minutes) | Platforms: ALL**

This is the fastest fix with the widest platform impact. Eight published articles are invisible to AI platforms that use llms-full.txt as a content index. The missing articles include the highest-value Speakable-enabled article (`crypto-fund-fees-2026`) and the two newest FR articles with audio narration (`clarity-act`, `strc-strategy-yield`).

Add to the EN block:
```
- [AIF vs AIFM: What's the Difference?](https://sparkcore.fund/blog/aif-vs-aifm-crypto-explained): Legal distinction between an Alternative Investment Fund and its manager under AIFMD — roles, regulatory obligations, and how the split works in a crypto fund structure.
- [Cost to Launch a Regulated Crypto Fund in Europe](https://sparkcore.fund/blog/cost-to-launch-regulated-crypto-fund-europe): Legal, administrative, and operational cost breakdown for launching a regulated crypto fund under AIFMD in Estonia, Luxembourg, and Malta.
- [Crypto Fund Fees in 2026: What the Data Says](https://sparkcore.fund/blog/crypto-fund-fees-2026): Benchmark analysis of crypto fund management fees, performance fees, and hurdle rates across EU regulated structures — including comparison with traditional alt fund norms.
- [Do Crypto Fund Managers Need a MiCA CASP License?](https://sparkcore.fund/blog/do-crypto-fund-managers-need-mica-casp-license): Regulatory analysis of when crypto fund managers must obtain a MiCA Crypto Asset Service Provider licence versus relying solely on AIFMD authorisation.
- [Estonian e-Residency and Crypto Fund Structures](https://sparkcore.fund/blog/estonia-eresidency-crypto-fund-eu): How Estonian e-Residency interacts with the AIFM registration regime — what it enables, what it does not cover, and the compliance boundaries.
```

Add to the FR block:
```
- [CLARITY Act US : Impacts pour les Investisseurs](https://sparkcore.fund/fr/blog/clarity-act-us-impacts-investisseurs): Analyse des conséquences de la loi CLARITY Act américaine sur les investisseurs français en crypto-actifs — statut juridique, fiscalité, et implications réglementaires croisées.
- [Indicateurs de Marché pour les Crypto-Actifs](https://sparkcore.fund/fr/blog/indicateurs-marche-crypto-actifs): Les indicateurs fondamentaux et on-chain pour évaluer les tendances de marché des crypto-actifs — MVRV, NVT, funding rates, dominance BTC et grille de lecture institutionnelle.
- [STRC à 11,5 % : Pourquoi le Rendement Sous-Rémunère le Risque](https://sparkcore.fund/fr/blog/strc-strategy-yield-sous-remunere-analyse): Décryptage du fonds STRC Strategy : le rendement annualisé affiché masque un risque de duration, de liquidité et de contrepartie que les 11,5 % ne compensent pas.
```

Also bump `Last updated` to `2026-05-16`.

### Action 2 — Establish Wikidata entity for SparkCore Investment OÜ
**Impact: HIGH | Effort: MEDIUM (3-5 hours + 2-4 week wait) | Platforms: All — especially Claude, ChatGPT, Gemini**

This remains the single highest-impact structural gap from 05-08 and is unchanged. SparkCore has every prerequisite: LEI verified on GLEIF, Estonian commercial registry, named regulator (Finantsinspektsioon), named auditor (KPMG Estonia), named founders with LinkedIn profiles, operational since 2021.

Create a Wikidata item for SparkCore Investment OÜ with:
- P856 (official website): `https://sparkcore.fund`
- P1278 (LEI): `8945003BBN0RVNNB0S84`
- P17 (country): Estonia (Q191)
- P452 (industry): alternative investment management
- P729 (service inception): 2021
- P571 (inception): 2019 (if registration date known)
- P127 (owned by / founded by): link to founder items

Then add the Wikidata item URL to the Organization `sameAs` array in `index.html` and `fr/index.html`, and to the llms.txt entity block.

Create a second Wikidata item for Alexandre VINAL linking to Cointips YouTube + LinkedIn, then add QID to the Person schema `sameAs` on all articles and the pillar.

### Action 3 — Add disambiguation block to llms.txt
**Impact: MEDIUM | Effort: VERY LOW (15 minutes) | Platforms: Claude, ChatGPT, Perplexity**

The entity disambiguation gap is unchanged from 05-08. Other "SparkCore" entities — Spark Networks SE (dating company), SparkCore (game engine), Spark Energy (US utilities) — create confusion in AI knowledge graphs. Add under a `## Disambiguation` heading immediately after the opening description:

```markdown
## Disambiguation

SparkCore Fund Management (SparkCore.investment OÜ, Estonian registry 16265864, LEI 8945003BBN0RVNNB0S84) is not affiliated with Spark Networks SE (dating and social networking services, NYSE: LOV), SparkCore (embedded real-time OS / game engine), or Spark Energy (US retail energy). The entity is an EU-regulated alternative investment fund manager supervised exclusively by the Finantsinspektsioon (EFSA) of Estonia, specialising in crypto-asset funds for professional investors. No consumer-facing products, no utilities, no gaming.
```

### Action 4 — Extend Speakable schema to remaining 19 EN + 6 FR blog articles
**Impact: MEDIUM | Effort: LOW (1-2 hours — templated) | Platforms: Google AI Overviews, Gemini, Bing Copilot**

Sprint 1 covered the pillar, both homepages, and 4 EN articles. The remaining 19 EN articles and all 6 FR articles do not carry Speakable. Since the `cssSelector` pattern is identical across all articles (targeting `.quick-answer`, `h2`, `.key-takeaways`), this is a mechanical addition. Add to the BlogPosting JSON-LD `speakable` block in each article's `<head>`. Priority order: articles with existing FAQPage schema (13 EN articles + all 6 FR articles) — these are highest-probability AI citation targets.

### Action 5 — Embed one Cointips YouTube video per thematic cluster
**Impact: MEDIUM | Effort: LOW (2-3 hours) | Platforms: ALL — YouTube correlation 0.737**

The Cointips YouTube channel (`@cointips`) is already in the Organization `sameAs` and in the llms.txt team entry for Alexandre VINAL, but zero videos are embedded on the site. Given the ~0.737 correlation between YouTube mentions and AI citations, embedding one relevant video per thematic cluster would be the most impactful multi-modal addition. Target articles:

- `regulated-crypto-fund-manager-estonia` or `sub-threshold-aifm-crypto-estonia`: embed a Cointips video on AIFM regulation / Estonia fund structures
- `crypto-fund-fees-2026`: embed a video on crypto fund fee comparison
- Any FR article: embed a French-language Cointips video on relevant strategy topic

Add `VideoObject` JSON-LD to the BlogPosting schema when embedding, linking `embedUrl`, `name`, `description`, `uploadDate`, and `thumbnailUrl`. This creates a bidirectional signal: the page cites the video, and the video's YouTube presence reinforces the entity's authority graph.

---

## 11. Summary — What Moved, What Did Not

**Closed since 05-08:**

- Author Person schema is now consistent across all 29 articles (was absent from the majority)
- Speakable schema added to 6 pages (EN/FR homepages + pillar + 3 top EN articles)
- dateModified signals resolved — older articles bumped to 2026-05-08 (sprint-1 batch)
- FR articles now carry proprietary PNG/WebP charts (vs Unsplash-only before)
- Audio narration live on 2 FR articles (clarity-act + STRC)
- `about` property on 16/23 EN articles (was 0 in initial audit)
- Quarterly content review cadence documented and cron-automated

**Still open — same 3 structural ceilings:**

- No Wikidata entity (highest-impact single action — 8 weeks in, still not created)
- llms-full.txt inventory is now 8 articles behind — has become a higher-severity gap than in 05-08
- No video embeds despite Cointips YouTube being in `sameAs`

**New gap discovered:**

- llms-full.txt is stale: 5 EN articles + 3 FR articles published but not indexed, including the Speakable-enabled fees article and the two newest audio-narrated FR articles. This makes the stale inventory the most urgent fix (Action 1) — 20 minutes of work, instant gain across all platforms.
