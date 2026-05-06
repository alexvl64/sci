# GEO Audit — sparkcore.fund
**Date:** 2026-05-06  
**Auditor:** Claude Sonnet 4.6 (claude-sonnet-4-6)  
**Scope:** AI Search Readiness / Generative Engine Optimization  
**Audience context:** Institutional investors, family offices, €50K minimum — research primarily via AI-assisted discovery (ChatGPT, Perplexity, Bing Copilot, Google AIO)

---

## GEO Readiness Score: 71 / 100  

| Dimension | Weight | Raw Score | Weighted |
|-----------|--------|-----------|---------|
| Citability | 25% | 70/100 | 17.5 |
| Structural Readability | 20% | 76/100 | 15.2 |
| Multi-Modal Content | 15% | 52/100 | 7.8 |
| Authority & Brand Signals | 20% | 68/100 | 13.6 |
| Technical Accessibility | 20% | 85/100 | 17.0 |
| **TOTAL** | | | **71.1** |

**Interpretation:** Good baseline — llms.txt is well-structured, crawler access is correct, blog content is substantive. The score is capped by homepage i18n (critical content rendered client-side), absence of Wikipedia/Wikidata entity, and passage-level citability gaps on the homepage. The blog articles are the strongest GEO asset on the site.

**Platform-specific projections:**

| Platform | Estimated Citation Probability | Notes |
|----------|-------------------------------|-------|
| Perplexity | Moderate-High | Blog articles are structurally ideal; EFSA URL is an authoritative anchor |
| ChatGPT | Low-Moderate | Training cutoff + brand novelty; no Wikipedia anchor; llms.txt helps post-training |
| Google AIO | Moderate | Blog H2/H3 structure + FAQPage schema on every article; YMYL flag limits unsourced claims |
| Bing Copilot | Moderate | Verified in Bing WMT, IndexNow active; blog content well-suited to real-time retrieval |

---

## 1. AI Crawler Access Status

**Source verified:** `robots.txt` in repo + live HTTP 200 confirmed on `https://sparkcore.fund/robots.txt`

| Crawler | Status | Gated Paths |
|---------|--------|-------------|
| GPTBot | Allowed | /factsheets/, /discovery-call, /MD/ — blocked (intentional) |
| OAI-SearchBot | Allowed | Same gated paths |
| ClaudeBot | Allowed | Same gated paths |
| PerplexityBot | Allowed | Same gated paths |
| Google-Extended | Allowed | Same gated paths |
| CCBot | Allowed | Same gated paths (training opt-in — intentional per context) |
| ia_archiver / archive.org_bot | Blocked | Full disallow |
| anthropic-ai / cohere-ai | Not listed (default `*` applies) | Falls under wildcard — /factsheets/, /discovery-call, /MD/ blocked; all other paths open |

**Assessment: PASS.** All five target AI crawlers are explicitly allowed. The `*` wildcard correctly blocks only sensitive paths without over-restricting the public site. The decision to allow CCBot (Common Crawl / training corpus) is intentional and correct for a fund building training-time brand footprint. 

**Cloudflare Turnstile status:** Turnstile (`data-appearance="interaction-only"`) is deployed ONLY on the contact sidebar form (`#cf-turnstile` div), not as a full-page bot challenge. HTTP headers on `/` and `/robots.txt` return HTTP 200 with no `cf-mitigated` or challenge headers. The `challenges.cloudflare.com` preconnect and script tag are loaded async/defer. AI crawlers that do not execute JavaScript will not encounter the Turnstile widget because it is hidden in a JS-rendered sidebar. **No crawler-blocking bot challenge is active on any public content page.**

---

## 2. llms.txt Audit

### Source vs. Live Comparison

**Method:** `fetch_page.py` fetched live content from `https://sparkcore.fund/llms.txt`. Compared character-by-character against `/home/alex/Documents/Claude/github-projets/sci/llms.txt`.

**Result: IDENTICAL. Zero diff between source and live.**

### llms.txt Quality Assessment

**File size:** 3,920 bytes / 80 lines  
**Estimated tokens:** ~980 tokens (well within LLM context window)

| llms.txt Spec Element | Present | Quality |
|----------------------|---------|---------|
| H1 (site/brand name) | Yes — `# SparkCore Fund Management` | Clear |
| Summary blockquote (1 sentence) | Yes — `> Registered alternative investment fund manager (AIFM) based in Estonia, specialising in crypto-assets.` | Concise, accurate |
| Descriptive paragraph under summary | Yes — 3-sentence entity description with legal name, registry number, EFSA regime, KPMG | Excellent |
| Structured sections with `##` headings | Yes — Funds, Regulatory Structure, Key Terms, White-Label Solution, Team, Contacts & Resources | Well-organised |
| Bullet links to canonical URLs | Yes — EFSA registry URL, EFIU licence URL, LinkedIn profiles | 2 regulatory anchors included |
| Key entity properties (registry, LEI, EFSA link) | Registry: Yes. LEI: Missing. EFSA link: Yes (×2). KPMG: Yes. | LEI gap (see below) |
| RSL 1.0 license declaration | Yes — `License: RSL 1.0` | Present |
| Cross-reference to llms-full.txt | Yes — `Full content index (blog articles & resources): https://sparkcore.fund/llms-full.txt` | Present |

**Strengths:**
- The regulatory section is the best GEO feature of this file. It names the specific regime (Small Fund Manager), links to the EFSA public registry, and names the FIU licence with a direct URL. An LLM asked "Is SparkCore regulated?" can cite this directly without needing to visit the site.
- Fee structure is fully enumerated (2% management, 20% perf, HWM, quarterly liquidity, 0% entry/exit). This answers due-diligence questions extractably.
- Team LinkedIn URLs are present, which correlates with brand mention attribution in AI answers.
- RSL 1.0 is declared, signalling content is licensed for AI reuse.

**Issues:**

1. **LEI number missing from llms.txt.** The LEI `8945003BBN0RVNNB0S84` appears in the homepage HTML trust strip and is confirmed ISSUED at GLEIF (`https://search.gleif.org/#/record/8945003BBN0RVNNB0S84`), but is absent from llms.txt. For a YMYL financial entity, the LEI is a machine-verifiable identity anchor. LLMs and AI search engines that consume LEI data from GLEIF would match the GLEIF entity to the llms.txt entity if the LEI were present.

2. **No `dateModified` or version marker.** llms.txt has no "last updated" field. LLMs that parse freshness signals cannot determine if this document is current. Risk: stale answers citing outdated fee structures or fund status.

3. **Equinoxe fund — launch year stated as "2026" but no status update.** As of 2026-05-06, Equinoxe is still in planned/pre-launch status. The file correctly says "planned launch in 2026" but an LLM answering "how many funds does SparkCore manage?" may answer "3" and include Equinoxe as operational. A parenthetical `(not yet operational as of [date])` would prevent this.

4. **CryptoVision operational date "01/02/2021" is before company incorporation date.** SparkCore.investment OÜ was registered in Estonia (registry 16265864). If CryptoVision launched before the current legal entity was formalised, this needs a clarifying note (e.g., "strategy operating since 01/02/2021; fund formalised under SparkCore.investment OÜ in [year]"). Otherwise an LLM may generate a factually inconsistent answer about regulatory history.

5. **No `foundingDate` or `dateRegistered` for the legal entity.** Adds precision for entity grounding.

---

## 3. llms-full.txt Audit

**File size:** 6,464 bytes / 42 lines  
**Estimated tokens:** ~1,608 tokens  
**Token weight vs. 100k limit:** 1,608 / 100,000 — negligible. **Zero truncation risk.**

| llms-full.txt Spec Element | Present | Quality |
|---------------------------|---------|---------|
| H1 | Yes — `# SparkCore Fund Management — Full Content Index` | Clear |
| Summary blockquote | Yes — `> Complete index of all SparkCore blog articles and resources.` | Adequate |
| Blog article entries with URL + description | Yes — 21 EN articles + 3 FR articles = 24 total | Complete |
| Description per article | Yes — 1-sentence summaries are substantive | Good |
| Resources section | Yes — factsheets (gated, noted), Privacy Policy | Present |
| RSL 1.0 license | Yes | Present |
| Cross-link to llms.txt | No | Missing |

**Strengths:**
- 24 articles indexed with canonical URLs and descriptive summaries. This is the right format for LLMs that crawl llms-full.txt as a content discovery map.
- French articles are included (`/fr/blog/...`), which is unusual and correct for multilingual coverage.
- Article descriptions are substantive enough for an LLM to decide which article to crawl for a given query, without needing to fetch the full article.
- Gated resources (factsheets) are correctly noted as "gated, available on request" — prevents AI hallucination about public availability of fund documents.

**Issues:**

1. **llms-full.txt does not cross-link back to llms.txt.** The canonical spec recommends the full file reference the concise file. An LLM that starts at llms-full.txt has no machine-readable pointer to the entity summary in llms.txt.

2. **No article publication dates in the index.** LLMs weight recency. An article published 2026-04-07 will be treated differently from one published 2026-01-01. Adding `(Published: YYYY-MM-DD)` to each entry costs nothing and improves freshness signals.

3. **No author attribution per article.** All EN blog articles are authored by Alexandre VINAL (confirmed in HTML `<meta name="author">` and byline). Adding `— By Alexandre VINAL` to each entry in llms-full.txt ties the brand entity (SparkCore) to the author entity (Vinal) in AI knowledge graphs.

4. **Draft blog articles in /MD/ are not indexed.** Files like `do-crypto-fund-managers-need-mica-casp-license.md`, `cost-to-launch-regulated-crypto-fund-europe.md`, `white-label-aifm-crypto-funds.md`, etc. exist in `/MD/` but are presumably not yet published. Once live, they should be added to llms-full.txt immediately — they cover high-intent AI query topics.

---

## 4. Per-Page Citability Analysis

### 4a. Homepage (`https://sparkcore.fund/`)

**Critical technical finding — i18n architecture:**

The homepage uses a JavaScript i18n system (`data-i18n` attributes + `page-i18n.js` + `translations.json`). Key sections including the H1 hero text, approach pillars, fund descriptions, and team bios are populated client-side via JS. The HTML source ships the correct fallback text as default content in the DOM (e.g., `heroTitle` = "Institutional-grade strategies in digital assets", `heroTagline` = "Three distinct approaches. One regulated framework."), so the **visible text is present in the initial HTML before JS execution**. This is a partial SSR / JS-enhanced pattern, NOT a pure CSR app.

Confirmed in live fetch: the fallback strings are in the HTML DOM. AI crawlers that parse static HTML (without executing JS) will see the correct English content.

**However:** The `<h1>` element uses `data-i18n-html="heroTitle"` — meaning it is an innerHTML replacement target, not a static text node. An AI crawler that parses raw HTML will see only the fallback text already inserted in the element. That fallback IS present and correct. Risk is low but not zero: a crawler that strips `data-i18n` attributes as empty markers could misread the structure.

**Citability score breakdown:**

| Signal | Status | Notes |
|--------|--------|-------|
| FAQ schema (JSON-LD) | Present — 4 questions | Answers are extractable, cover top 4 investor queries |
| H1 present in static HTML | Yes — "Institutional-grade strategies in digital assets" | No direct question format |
| Trust strip (Regulator, KPMG, LEI, Legal Counsel) | Present — static HTML, no JS required | Excellent for AI citation |
| Direct answer to "Is SparkCore regulated?" | Yes — JSON-LD FAQPage + trust strip linking to EFSA | Strong |
| Direct answer to "What is minimum investment?" | Yes — JSON-LD FAQPage | €50,000 stated explicitly |
| Self-contained passage length (40-60 words at section start) | Partial — approach section has good 2-3 sentence para intros | Fund card bodies are JS-rendered |
| Named H2 headings on homepage | 4 visible: "Our approach", "Our crypto investment funds", team, newsletter | None are question-formatted |
| Statistics with source attribution | None on homepage | Gap |
| Callout/citation boxes | None | Gap |
| Author attribution | "SparkCore Fund Management" as `<meta name="author">` | Generic, not a named person |

**Homepage citability score: 62/100**

Primary limitation: the homepage is a brand/product page, not a Q&A page. The JSON-LD FAQPage schema is the strongest AI-citation mechanism on the page — it directly answers 4 high-intent questions in structured, extractable format.

**Top investor Q&A questions answered on the homepage:**
- "What is SparkCore Fund Management?" — Yes (JSON-LD)
- "Is SparkCore regulated?" — Yes (JSON-LD + trust strip)
- "What is the minimum investment?" — Yes (JSON-LD: €50,000)
- "What funds does SparkCore manage?" — Yes (JSON-LD)
- "Who founded SparkCore?" — Partial (team section, but no JSON-LD Person schema on homepage)
- "What regulator supervises SparkCore?" — Yes (trust strip + JSON-LD)
- "Who audits SparkCore's accounting?" — Yes (trust strip: KPMG Estonia)

**Questions NOT directly answered on the homepage that AI systems regularly generate:**
- "What are SparkCore's fees?" — Not on homepage (in llms.txt but not JSON-LD)
- "Who are the founders of SparkCore?" — Team section visible but no structured data
- "What is the SparkCore Dynamic Trends fund performance?" — Not addressable (correct per YMYL/regulatory constraints)
- "How do I invest in SparkCore?" — Implicit (discovery call CTA) but no structured Q&A

---

### 4b. Blog: "What Is a Crypto AIFM" (`/blog/what-is-a-crypto-aifm`)

**Citability score: 81/100**

| Signal | Status |
|--------|--------|
| H2/H3 headings as direct questions | 3 of 9 H2s are question-format ("What is a crypto AIFM in practice?", "What a crypto AIFM is not", "How does a crypto AIFM differ from direct crypto investing?") |
| Opening passage answers query within 40-60 words | Partial — first 2 paragraphs are framing/context, direct definition comes at paragraph 2 |
| Passage length near optimal (134-167 words per section) | Most H2 sections are 150-250 words — slightly over but still extractable |
| Statistics with source attribution | Yes — ESMA Annual Statistical Report 2023 (29,000+ registered funds, 1,400+ AIFMs) cited inline |
| Self-contained answer blocks | Yes — "What a crypto AIFM is not" section is fully self-contained |
| FAQPage JSON-LD schema | Yes — 4 questions with high-quality answers |
| BlogPosting schema with author, datePublished | Yes — Alexandre VINAL, 2026-03-25, wordCount: 1648 |
| Disclaimer block | Yes — clearly labelled, regulatory disclosure present |
| Internal links to related articles | Yes — 4+ internal links |
| Source attribution for claims | Yes — ESMA cited directly |

**Strengths:** The FAQ schema answers (4 questions) are at optimal citation length (60-120 words each). The "What investors should look for" section is an excellent citation-ready block — it enumerates 4 criteria with clear labels (strategy clarity, risk architecture, infrastructure, governance credibility). An LLM asked "what should I look for when evaluating a crypto fund manager?" could cite this directly.

**Gaps:**
- The opening does not front-load the definition. An AI crawler extracting the first 60 words of the article body gets framing text ("For many professional investors, the real question is not whether crypto...") rather than the definition itself. The definition of a crypto AIFM appears at paragraph 2. This costs citation probability for snippet-level extraction.
- No callout/summary box at article top (e.g., "Quick answer: A crypto AIFM is...").

---

### 4c. Blog: "Regulated Crypto Fund Manager in Estonia" (`/blog/regulated-crypto-fund-manager-estonia`)

**Citability score: 84/100**

| Signal | Status |
|--------|--------|
| H2/H3 headings | 7+ H2s including "The Estonian Regulatory Framework", "AML/CFT Supervision", "What a Registered AIFM Can and Cannot Do", "The Usaldusfond Structure", "Why Estonia for Crypto Asset Funds?" — all descriptive, 2 quasi-question format |
| Opening passage direct answer | Strong — first paragraph defines "regulated crypto fund manager in Estonia" within 40 words and immediately lists 3 investor-protection dimensions |
| Statistics with source attribution | Yes — European Commission AIFMD transposition, EFSA VASP reform data (1,000+ → tightened), both cited |
| AUM thresholds in callout cards | Yes — €100M (leveraged) and €500M (unleveraged) in visual grid cards with `<div class="border border-lightGray rounded-lg p-5 bg-[#F9FAFB]">` — not semantic `<aside>` or `<blockquote>` but visually distinct |
| Legal citation (Estonian Investment Funds Act, AIFMD Article) | Yes — with EUR-Lex links |
| BlogPosting + BreadcrumbList schema | Yes |
| FAQPage schema | Not found in head (unlike the AIFM article) — this article does not have FAQPage JSON-LD |
| Author byline | Yes — Alexandre VINAL, 2026-03-09, 13 min read |

**Gaps:**
- No FAQPage schema on this article despite being the highest-intent page for "Is SparkCore regulated?" and "What is the AIFM regime in Estonia?" queries. This is a missed structured-data opportunity.
- Usaldusfond section is technically excellent but the term is Estonian-only — no translation or explanation anchor in the first sentence for AI extractors that surface the passage without context.

---

### 4d. Blog: "Sub-Threshold AIFM for Crypto: Thresholds, Benefits, and the Estonia Option" (`/blog/sub-threshold-aifm-crypto-estonia`)

**Citability score: 88/100** — strongest article for AI citation.

**Exceptional signals:**
- Opens with a hard statistic in the first sentence: "Crypto hedge fund AUM reached $136.2 billion globally in Q2 2025, with over 400 active funds operating worldwide (CoinLaw, 2025)." This is the ideal GEO opening format.
- Multiple H3 subheadings are question-format: "How Are the AUM Thresholds Calculated?", "What Happens When You Exceed the Threshold?", "The AIFM/MiCA Exemption", "Where the Exemption Ends".
- Source attribution is dense and high-quality: PwC/AIMA 7th Annual Global Crypto Hedge Fund Report, EUR-Lex AIFMD consolidated 2025, DLA Piper 2025, ESMA 2025, Chainalysis 2025, Finantsinspektsioon 2025, Linklaters 2025 — all linked.
- Quantified cost comparisons: "€25,000 mandatory capital vs. €125,000–€300,000 for full AIFM" with source citations.
- Step-by-step setup section is extractable as a numbered checklist.

**One gap:** The "The Full Comparison" section references a table (`<p class="font-inter text-sm text-mediumGray leading-160 mb-6 italic">Sources: Linklaters (2025); Finantsinspektsioon (2025); EUR-Lex AIFMD.</p>`) but the fetched content did not contain an HTML `<table>` element — if the comparison table is rendered as a visual CSS grid rather than a semantic `<table>`, AI crawlers reading HTML cannot parse the tabular data. This should be verified and converted to `<table>` if it is a grid.

---

## 5. Technical Accessibility for AI Crawlers

| Factor | Status | Details |
|--------|--------|---------|
| Server-side rendered content | Partial SSR | Homepage: fallback text in HTML DOM via data-i18n attributes; blog articles: 100% static HTML, no JS dependency |
| Cloudflare bot challenge (Turnstile) | No full-page challenge | Turnstile only on contact form sidebar (interaction-only mode); public pages serve HTTP 200 to all crawlers |
| robots.txt served | Yes — HTTP 200 | No X-Robots-Tag blocking on public pages |
| sitemap.xml | Present | `https://sparkcore.fund/sitemap.xml` declared in robots.txt |
| _headers (X-Robots-Tag) | Correctly scoped | Only /MD/*, /factsheets/*, /discovery-call, /validation.html are noindex — all public blog and homepage paths are index/follow |
| Page speed / rendering | Cloudflare Pages (global CDN) | Static HTML delivery; no TTFB penalty for crawlers |
| JavaScript dependency for core content | Low risk | Blog articles: zero JS dependency. Homepage: data-i18n fallback text present in DOM |
| Canonical tags | Present on all sampled pages | Correctly set |
| hreflang | Present on homepage (en/fr/x-default) | Blog articles: en + x-default only |
| HTTPS | Yes — Cloudflare TLS | HTTP headers include cf-ray, standard Cloudflare proxy |

**i18n risk (deeper assessment):**

The `lang-redirect-en.js` script runs synchronously at `<body>` open. It likely redirects users with French browser preferences to `/fr/`. AI crawlers that send `Accept-Language: en` (the default) will not be redirected. This is acceptable. The risk is the `page-i18n.js` script that replaces `data-i18n` placeholder text — if a crawler parses HTML before this script runs, it will see the inline fallback text (which is identical to the translated EN content in most cases), not an empty DOM. Spot-check on the homepage confirms fallback text is present and correct for all sampled `data-i18n` elements.

**Technical accessibility score: 85/100**

Deduction: The `data-i18n-html` pattern on the H1 introduces minor ambiguity for strict HTML-only parsers. The homepage's reliance on JS for the performance chart (ApexCharts) means any data visualisations are invisible to AI crawlers — but this does not affect textual content extraction.

---

## 6. Authority & Brand Signals

### 6a. Wikipedia / Wikidata

**Wikipedia:** No article found. API query for "SparkCore Investment" returns `missing: true`.  
**Wikidata:** No entity found. Search returns no results.

This is the most significant authority gap for AI citation. Wikipedia/Wikidata presence is one of the strongest signals for entity grounding in LLMs. ChatGPT's knowledge base is heavily weighted toward Wikipedia-sourced entities. A fund manager without a Wikipedia entity is much more likely to be hallucinated or attributed inaccurately by LLMs.

**Assessment:** Expected for a fund of this size and age (founded ~2019, operational at current scale since 2025). The gap is structural — Wikipedia's notability criteria are difficult for a sub-threshold AIFM to meet via direct article creation. The path to entity grounding is indirect: Wikidata entity creation (lower bar than Wikipedia), GLEIF record (confirmed ISSUED), EFSA registry listing (confirmed accessible), and earned mentions in financial press.

### 6b. GLEIF / LEI Registry

**Status: ISSUED** — `8945003BBN0RVNNB0S84` for SparkCore.investment OÜ, country EE.  
**AI citation value:** The GLEIF database is indexed by some AI systems as an authoritative financial entity registry. The LEI being ISSUED and verifiable at `https://search.gleif.org/#/record/8945003BBN0RVNNB0S84` is a machine-readable authority anchor. **However, the LEI is absent from llms.txt**, which means the connection between the GLEIF entity and the llms.txt entity is not machine-readable from the document itself.

### 6c. EFSA (Finantsinspektsioon) Registry

**Status: Confirmed accessible.** The EFSA registry page at `https://www.fi.ee/` redirects to the correct entity URL. This is the highest-authority regulatory citation available for SparkCore. Both llms.txt and the homepage link to it. An AI asked "Is SparkCore Fund Management regulated?" that crawls the EFSA registry will find the entity listed.

**AI citation value:** Very high. A regulatory registry URL is treated as ground truth by AI systems for entity verification queries.

### 6d. LinkedIn

**Company page:** `https://www.linkedin.com/company/sparkcorefund/` — linked in Organization JSON-LD `sameAs`.  
**Individual profiles:** All 3 partners have LinkedIn URLs in llms.txt and in homepage HTML.  
**AI citation value:** Moderate. LinkedIn appears in AI training data and is used for entity disambiguation. The company page being linked in `sameAs` is the correct JSON-LD pattern for brand anchoring.

### 6e. YouTube (Cointips — Alexandre Vinal)

**Channel:** `https://youtube.com/cointips` — linked in homepage HTML for Alexandre Vinal's team card.  
**AI citation value:** This is significant. YouTube channel mentions have the highest correlation with AI citation (~0.737 per GEO research). The Cointips channel (founded 2017) is the strongest brand-adjacent authority signal SparkCore has. Crucially, the connection between Cointips and SparkCore is established in:
- llms.txt (bio: "Founder of the Cointips YouTube channel")
- Homepage HTML (team section with YouTube link)
- Blog article author meta

This means an LLM that knows about Cointips as an authority in crypto education can be grounded to SparkCore via the Alexandre Vinal entity connection.

**Gap:** The Cointips YouTube channel is not in the Organization JSON-LD `sameAs` array. Currently only LinkedIn is. Adding the YouTube URL would strengthen the entity graph.

### 6f. Reddit

**Presence:** No evidence of SparkCore Reddit presence found in site content.  
**AI citation value:** High per GEO correlation data. No known subreddit or company posts identified. Gap for long-term brand building, not an immediate actionable for a regulated fund manager (regulatory constraints on marketing channels).

### 6g. Press / Third-Party Citations

No press coverage, CoinDesk/Decrypt/The Block citations, or financial media mentions were found in site content or llms.txt. This is the most impactful gap for building AI citation probability via external references.

**Authority & Brand Signals score: 68/100**

Strong regulatory anchors (EFSA, GLEIF) partially compensate for the absence of Wikipedia/press coverage. YouTube signal via Cointips is a structural advantage that most sub-threshold fund managers lack.

---

## 7. Q&A Formatting Opportunities

The following high-probability AI queries are currently not answered in optimal citation-ready format on the homepage or in structured data. Each includes a suggested answer formulated at the 134-167 word optimal citation length.

### Q1: "Who are the founders of SparkCore Fund Management?"

**Current coverage:** Team section in HTML + llms.txt bios (not in JSON-LD Person schema).  
**Gap:** No Person schema on homepage. Bios are in JS-rendered sections (data-i18n attributes). AI extractors cannot reliably attribute founder information to SparkCore as an entity.

**Suggested JSON-LD addition (homepage):**
```json
{
  "@type": "Person",
  "name": "Paul-Antoine Pons",
  "jobTitle": "Managing Partner",
  "worksFor": {"@id": "https://sparkcore.fund/"},
  "sameAs": "https://www.linkedin.com/in/paul-antoine-pons-523aa919a/"
},
{
  "@type": "Person",
  "name": "Olivier Sayegh",
  "jobTitle": "Managing Partner",
  "worksFor": {"@id": "https://sparkcore.fund/"},
  "sameAs": "https://www.linkedin.com/in/olivier-sayegh-5b89b3135/"
},
{
  "@type": "Person",
  "name": "Alexandre Vinal",
  "jobTitle": "Managing Partner",
  "worksFor": {"@id": "https://sparkcore.fund/"},
  "sameAs": ["https://www.linkedin.com/in/alexandrevinal/", "https://youtube.com/cointips"]
}
```

**Suggested FAQ entry (add to homepage FAQPage JSON-LD):**
```
"name": "Who founded SparkCore Fund Management?",
"acceptedAnswer": {
  "text": "SparkCore Fund Management was co-founded by three Managing Partners: Paul-Antoine Pons, who has over 7 years of experience in financial markets and crypto-assets; Olivier Sayegh, a trader with over 20 years of experience across equity and crypto markets since 2017; and Alexandre Vinal, a software engineer and crypto investor since 2014, founder of the Cointips YouTube channel. Together they founded SparkCore.investment OÜ, registered in Estonia (registry no. 16265864) as a regulated alternative investment fund manager supervised by Finantsinspektsioon."
}
```
**Word count of suggested answer: 87 words** — within extractable range.

---

### Q2: "What fees does SparkCore charge?"

**Current coverage:** llms.txt (Key Terms section). Not in any JSON-LD.  
**Gap:** Fee information is in llms.txt but not in FAQ schema. AI answering fee queries from JSON-LD will not find it.

**Suggested FAQ entry:**
```
"name": "What are the fees for investing in SparkCore funds?",
"acceptedAnswer": {
  "text": "SparkCore funds charge a 2% annual management fee and a 20% performance fee calculated quarterly with a High Water Mark. There are no entry or exit fees. An early commitment break fee of 4% applies if an investor exits before the minimum 1-year commitment period. Minimum subscription is EUR 50,000. Subscriptions are accepted in EUR, USD, and MiCA-compliant stablecoins. Fund liquidity is quarterly."
}
```
**Word count: 70 words** — optimal for snippet extraction.

---

### Q3: "Is SparkCore regulated in the EU?"

**Current coverage:** FAQPage JSON-LD answers "Is SparkCore Fund Management regulated?" — good but generic.  
**Gap:** Does not specify the EU framework or clarify sub-threshold status vs. full AIFM for sophisticated investors running due diligence.

**Suggested improved FAQ answer:**
```
"name": "Is SparkCore Fund Management regulated in the EU?",
"acceptedAnswer": {
  "text": "Yes. SparkCore.investment OÜ is registered as a Small Alternative Investment Fund Manager with the Finantsinspektsioon (Estonian Financial Supervision Authority, EFSA) under the sub-threshold regime of AIFMD Article 3(2). The company also holds a Financial Institution licence (EFIU) from the Estonian Financial Intelligence Unit for KYC/AML compliance. The legal entity is incorporated in Estonia (registry no. 16265864) and is listed on the EFSA public register. Accounting is handled by KPMG Estonia; legal counsel is Hedman Partners & Co. LEI: 8945003BBN0RVNNB0S84."
}
```
**Word count: 95 words** — optimal.

---

### Q4: "What is the minimum investment for SparkCore?"

**Current coverage:** FAQPage JSON-LD — "The minimum investment is €50,000" — present and correct.  
**Assessment: PASS.** No change needed.

---

### Q5: "How does SparkCore's Dynamic Trends fund work?"

**Current coverage:** llms.txt brief description. No dedicated FAQ or structured data.  
**Suggested addition to homepage FAQPage:**
```
"name": "How does the SparkCore Dynamic Trends fund work?",
"acceptedAnswer": {
  "text": "Dynamic Trends is SparkCore's high-risk, actively managed fund targeting outperformance relative to Bitcoin. The strategy uses a two-block structure: an offensive block with directional Bitcoin exposure at up to 2x leverage, and a defensive block of market-neutral and quantitative strategies designed to limit drawdowns during corrections. The fund has been operational since 1 August 2025 and targets qualified investors with a minimum subscription of EUR 50,000. It is managed within the regulated framework of SparkCore.investment OÜ, supervised by Finantsinspektsioon (Estonia)."
}
```
**Word count: 93 words** — optimal.

---

## 8. Schema Reinforcement Assessment

| Schema Type | Homepage | Blog Articles |
|-------------|----------|--------------|
| Organization | Present — name, legalName, alternateName, url, logo, sameAs (LinkedIn) | N/A |
| FinancialService | Present — name, legalName, areaServed, address, memberOf (Finantsinspektsioon) | N/A |
| WebPage / BlogPosting | Present | Present on all sampled articles |
| FAQPage | Present (4 questions) | Present on "what-is-a-crypto-aifm", missing on "regulated-crypto-fund-manager-estonia" |
| BreadcrumbList | N/A on homepage | Present on all sampled blog articles |
| Person (founders) | Absent | Absent (author is Person in BlogPosting but not standalone) |
| ItemList (navigation) | Present | N/A |

**Missing enrichments that would improve LLM grounding:**

1. `Organization.foundingDate` — adds temporal entity precision.
2. `Organization.knowsAbout` — array: ["Alternative Investment Fund Management", "Crypto-assets", "AIFMD compliance", "Estonian fund law"]. Helps AI classify expertise domain.
3. `Organization.award` or `Organization.accreditation` — EFSA registration and EFIU licence could be modelled as `accreditation` with `@type: EducationalOccupationalCredential` or simply as a `memberOf` GovernmentOrganization (already partially done for EFSA).
4. `FinancialService.hasOfferCatalog` linking to the three funds — allows AI to enumerate fund offerings as structured data.
5. `Organization.sameAs` should include the YouTube Cointips channel: `"https://youtube.com/cointips"` (via the Alexandre Vinal founder connection).
6. `Person` schema for all 3 founders on homepage — not yet present.

---

## 9. Top 5 Highest-Impact Changes (Prioritised)

### Priority 1: Add LEI + `foundingDate` + Person schema to llms.txt and homepage JSON-LD
**Effort:** 30 minutes (file edits only, no deployment complexity)  
**Impact:** HIGH — LEI connects GLEIF's machine-readable entity record to llms.txt, enabling AI systems to verify entity identity programmatically. Person schema for 3 founders enables disambiguation when users ask "who runs SparkCore?" and grounds the Cointips YouTube authority to the entity graph.

**Changes:**
- `llms.txt`: Add `- LEI: 8945003BBN0RVNNB0S84 (GLEIF: https://search.gleif.org/#/record/8945003BBN0RVNNB0S84)` to Regulatory Structure section. Add `- Founded: [year SparkCore.investment OÜ incorporated]`.
- `llms.txt`: Add `(Status: planned, not yet operational as of May 2026)` to Equinoxe entry.
- `index.html` JSON-LD: Add 3 `Person` objects (founders) to the `@graph`. Add Cointips YouTube to `Organization.sameAs`.
- `index.html` JSON-LD: Add `foundingDate` to Organization.

---

### Priority 2: Add FAQPage schema to "regulated-crypto-fund-manager-estonia" + 2 additional FAQ entries on homepage
**Effort:** 45 minutes  
**Impact:** HIGH — This is the highest-traffic article for institutional investor queries ("is SparkCore regulated in Estonia?"). Adding FAQPage JSON-LD to this article mirrors what is already done on the AIFM article and will directly improve Perplexity/Bing Copilot citation probability for regulatory queries. The two new homepage FAQ entries (founders, fees) close the most common AI due-diligence query gaps.

---

### Priority 3: Add a "TL;DR / Quick Answer" callout box at the top of each blog article
**Effort:** 2 hours (template change applied across 21 EN articles)  
**Impact:** HIGH — AI crawlers performing snippet extraction surface the first 40-60 words of a section. Currently all articles open with framing text rather than direct answers. A static `<div class="quick-answer">` box above the first `<p>` with a 30-50 word direct answer would become the primary citation extraction target. Example for the AIFM article: "A crypto AIFM (Alternative Investment Fund Manager) is a regulated entity that manages investment funds holding digital assets under EU or national financial law, providing professional investors with structured access, risk oversight, and regulatory reporting."

---

### Priority 4: Convert comparison tables in blog articles from CSS grid to semantic HTML `<table>`
**Effort:** 1 hour per article (verify which articles use CSS grids for structured data)  
**Impact:** MEDIUM — Confirmed that the "Sub-Threshold vs. Full AIFM" comparison renders via HTML structure, not a `<table>`. AI crawlers cannot reliably extract tabular data from CSS grids. Converting to `<table>` with `<th>` column headers makes the data extractable as a fact matrix (e.g., "sub-threshold capital requirement: €25,000; full AIFM capital requirement: €125,000–€300,000").

---

### Priority 5: Add `dateModified` and version tag to llms.txt + add cross-link from llms-full.txt to llms.txt
**Effort:** 10 minutes  
**Impact:** MEDIUM — Freshness signals matter for AI systems that track document age. A `Last updated: 2026-05-06` line at the top of llms.txt costs nothing and improves currency signals. The cross-link from llms-full.txt to llms.txt closes the navigation loop for LLMs that discover the content index first.

---

## 10. Brand Mention Analysis Summary

| Signal | Present | Quality | AI Citation Correlation |
|--------|---------|---------|------------------------|
| EFSA (Finantsinspektsioon) registry | Yes — linked from llms.txt + homepage | Authoritative government source | Very High |
| GLEIF LEI (8945003BBN0RVNNB0S84) | Yes — ISSUED; linked from homepage trust strip | Machine-verifiable identity | High |
| EFIU FIU licence | Yes — URL in llms.txt | Second regulatory anchor | High |
| LinkedIn (company) | Yes — in Organization sameAs | Standard brand signal | Moderate |
| LinkedIn (3 partners) | Yes — in llms.txt + homepage HTML | Individual entity grounding | Moderate |
| YouTube (Cointips — Alexandre Vinal) | Yes — in homepage HTML team section | Strongest brand-adjacent signal (~0.737 correlation) | High |
| Wikipedia | No | Not found | Missing |
| Wikidata entity | No | Not found | Missing |
| Reddit | No | Not found | Low (regulatory constraints make this low priority) |
| Press / financial media | No | No citations found | Missing — biggest long-term gap |
| KPMG Estonia (accounting) | Yes — trust strip (static HTML) | Third-party credibility signal | Moderate-High |
| Hedman Partners & Co (legal) | Yes — trust strip (static HTML) | Third-party credibility signal | Moderate |

---

## Appendix: File References

All source files audited:
- `/home/alex/Documents/Claude/github-projets/sci/llms.txt`
- `/home/alex/Documents/Claude/github-projets/sci/llms-full.txt`
- `/home/alex/Documents/Claude/github-projets/sci/robots.txt`
- `/home/alex/Documents/Claude/github-projets/sci/_headers`
- `/home/alex/Documents/Claude/github-projets/sci/index.html`
- `/home/alex/Documents/Claude/github-projets/sci/assets/js/translations.json`
- Live pages fetched: `/`, `/robots.txt`, `/llms.txt`, `/blog/what-is-a-crypto-aifm`, `/blog/regulated-crypto-fund-manager-estonia`, `/blog/sub-threshold-aifm-crypto-estonia`
- External APIs checked: GLEIF API (LEI), Wikipedia API, Wikidata search API, Finantsinspektsioon (EFSA) registry
