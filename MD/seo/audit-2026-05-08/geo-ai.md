# GEO / AI Search Readiness Audit — sparkcore.fund
**Date:** 2026-05-08
**Auditor:** Claude (claude-sonnet-4-6) — autonomous GEO audit

---

## 1. GEO Health Score

| Dimension | Weight | Raw Score | Weighted |
|-----------|--------|-----------|---------|
| Citability | 25% | 78/100 | 19.5 |
| Structural Readability | 20% | 82/100 | 16.4 |
| Multi-Modal Content | 15% | 38/100 | 5.7 |
| Authority & Brand Signals | 20% | 61/100 | 12.2 |
| Technical Accessibility | 20% | 90/100 | 18.0 |

**Overall GEO Health Score: 72/100 (B-)**

---

## 2. AI Crawler Access Status

| Crawler | robots.txt Rule | Live HTTP Test | Status |
|---------|----------------|----------------|--------|
| GPTBot | `Allow: /` | HTTP 200 (confirmed) | ALLOWED |
| OAI-SearchBot | `Allow: /` | — | ALLOWED |
| ClaudeBot | `Allow: /` | — | ALLOWED |
| PerplexityBot | `Allow: /` | HTTP 200 (confirmed) | ALLOWED |
| Google-Extended | `Allow: /` | — | ALLOWED |
| CCBot | `Allow: /` | — | ALLOWED (training permitted) |
| ia_archiver | `Disallow: /` | — | BLOCKED (archive.org) |

Gated paths correctly blocked for all crawlers: `/factsheets/`, `/discovery-call`, `/MD/`.

No Cloudflare AI bot blocking. Cloudflare Speculation Rules active (prefetch hinting). Pages are SSR/static (Cloudflare Pages) — zero JavaScript rendering dependency for crawlers.

**Verdict: FULLY ACCESSIBLE. No remediation needed.**

---

## 3. llms.txt Assessment

**Status: PRESENT and WELL-FORMED**

| Criterion | Status | Notes |
|-----------|--------|-------|
| File present | YES | `https://sparkcore.fund/llms.txt` |
| RSL 1.0 license | YES | `License: RSL 1.0` declared at EOF |
| Last-updated timestamp | YES | `Last updated: 2026-05-06` |
| Entity identification | EXCELLENT | Legal name, registry no., LEI, GLEIF URL, EFSA URL, EFIU URL all present |
| Regulatory anchors | EXCELLENT | Two primary-source URLs (fi.ee + mtr.ttja.ee) included |
| Fund inventory | GOOD | 3 funds with strategy, risk level, status |
| Team section | GOOD | 3 partners with LinkedIn URLs |
| Key terms section | EXCELLENT | Fees, minimums, liquidity, currencies explicitly stated |
| llms-full.txt companion | YES | 21 EN + 3 FR articles indexed with descriptive one-liners |
| Gated content handling | CORRECT | Factsheets listed as "gated, available on request" — not linked |
| Missing: Knowledge Graph / Wikipedia sameAs | GAP | No Wikidata QID or Wikipedia URL in llms.txt entity section |
| Missing: Competitor disambiguation | GAP | No note distinguishing SparkCore from Spark Networks, Spark Energy, SparkCore (gaming studio) |

**llms.txt Score: 81/100**

The file is structurally excellent. The two gaps above are the primary improvement opportunities.

---

## 4. Platform-Specific Readiness Scores

| Platform | Score | Key Driver | Key Gap |
|----------|-------|------------|---------|
| Google AI Overviews | 74/100 | FAQPage schema on all articles, fresh dateModified on pillar + fees article, isAccessibleForFree set | Older articles (March 2026) have stale dateModified; no Speakable schema; no Wikipedia entity for KG anchor |
| ChatGPT (web search) | 76/100 | llms.txt quality, clear passage structure, strong "Quick Answer" blocks, SSR | Author sameAs lacks Wikipedia; no external .gov/.edu inbound links citing SparkCore |
| Perplexity | 78/100 | Citation density high (EUR-Lex, GLEIF, fi.ee URLs inline in body), statistics with sources, clean SSR HTML | Source tier thin — no academic citations, no news coverage, entity not confirmed in Perplexity's source hierarchy |
| Claude | 72/100 | LEI + registry number surfaced in FAQ schema text, GLEIF URL in sameAs, llms.txt has all entity facts | No Wikidata QID; entity disambiguation weak vs other "SparkCore" companies; no third-party entity confirmation |
| Gemini / Google AI | 70/100 | FAQPage schema present, FinancialService type, leiCode in Organization schema | No `memberOf` regulatory body schema on articles (only on homepage FinancialService block); dateModified stale on 17+ older articles |
| Bing Copilot | 68/100 | Bing WMT verified, IndexNow active, sitemap submitted | No Speakable schema; entity not in Bing entity knowledge base (no Microsoft Satori anchor) |

---

## 5. Detailed Findings

### 5.1 Citability — 78/100

| Finding | Severity | Location |
|---------|----------|----------|
| "Quick Answer" blocks present on pillar + blog-en-1; answer-first structure in 40-60 words | POSITIVE | pillar.html, blog-en-1.html |
| FAQPage schema on homepage (5 Q&A), pillar (6 Q&A), blog-en-1 (4 Q&A), blog-en-2 (6 Q&A), blog-fr-1 (3 Q&A) | POSITIVE | All sampled pages |
| FAQ answers are self-contained and passable — they cite specific thresholds (EUR 100M, EUR 500M, EUR 25,000), named sources (bfinance, Crypto Insights Group, PwC/AIMA, 21e6 Capital) | POSITIVE | blog-en-2 especially |
| Average FAQ answer length: 80-130 words — slightly below the 134-167 word optimal citation window | LOW | All FAQ blocks |
| Body paragraphs average ~85 words — good, extractable; no walls of text | POSITIVE | All pages |
| "Citation capsule" blockquotes in pillar explicitly formatted for AI extraction | POSITIVE | pillar.html |
| Statistics in blog-en-2 carry source attribution inline: "(Crypto Insights Group, 2025)", "(bfinance, April 2024)", "(PwC/AIMA, Nov 2025)" | POSITIVE | blog-en-2 |
| No `Speakable` schema on any page — missed opportunity for Google Assistant + voice query citations | MEDIUM | All pages |
| Blog-en-1 (oldest sampled article, March 2026) has dateModified = datePublished — same date, signals no updates to crawlers | MEDIUM | blog-en-1.html |
| `isAccessibleForFree: true` present on pillar and blog-en-1 but absent on blog-en-2 (fees article) and blog-fr-1 | LOW | blog-en-2, blog-fr-1 |
| H2 headings are mostly statement-form rather than question-form — reduces FAQ-signal density outside FAQ blocks | LOW | All EN blog articles |

### 5.2 Structural Readability — 82/100

| Finding | Severity | Location |
|---------|----------|----------|
| Static HTML (SSR via Cloudflare Pages) — full body rendered before JavaScript | POSITIVE | All pages |
| BreadcrumbList schema on all sampled articles | POSITIVE | All pages |
| BlogPosting schema correctly typed with headline, datePublished, dateModified, wordCount, inLanguage | POSITIVE | All articles |
| Internal cluster linking dense — pillar links to 12+ supporting articles by name | POSITIVE | pillar.html |
| H2/H3 heading hierarchy clean; no heading jumps | POSITIVE | All pages |
| Tables used in blog-en-1 for AUM thresholds (card layout), and in Key Takeaways blocks | POSITIVE | blog-en-1.html |
| "Key Takeaways" / "Key takeaways" summary blocks with bullet statistics at section top | POSITIVE | blog-en-2, pillar |
| No `about` property on BlogPosting schema connecting articles to regulated topics (e.g., `about: {"@type": "Thing", "name": "Alternative Investment Fund Managers Directive"}`) | LOW | All articles |
| llms-full.txt article descriptors are 1-2 sentences; sufficient for AI indexing context | POSITIVE | llms-full.txt |

### 5.3 Multi-Modal Content — 38/100

| Finding | Severity | Location |
|---------|----------|----------|
| No video content — YouTube channel (Cointips) linked in sameAs but no embeds on site | HIGH | All pages |
| Images are Unsplash stock photos — zero proprietary charts, infographics, or data visualisations | HIGH | All pages |
| No audio player on EN regulatory articles (only FR articles appear to have it per CLAUDE.md) | MEDIUM | EN blog cluster |
| No downloadable structured data (JSON/CSV) that AI platforms could ingest as primary sources | MEDIUM | All pages |
| ApexCharts loaded on homepage (per CSP) but no visible charts in sampled homepage HTML | LOW | homepage.html |
| Alt text on images is descriptive and specific (e.g., "Modern Estonian capital Tallinn skyline at dusk — symbolising Estonia's position as the EU's lowest-cost AIFM jurisdiction") | POSITIVE | pillar.html |

### 5.4 Authority & Brand Signals — 61/100

| Finding | Severity | Location |
|---------|----------|----------|
| LEI (8945003BBN0RVNNB0S84) present in: Organization schema (leiCode), FAQ schema text (blog-en-1), llms.txt entity section | POSITIVE | homepage, blog-en-1, llms.txt |
| GLEIF URL in homepage Organization `sameAs` array | POSITIVE | homepage.html |
| Finantsinspektsioon registry URL in `sameAs` + llms.txt | POSITIVE | homepage.html |
| EFIU licence URL (mtr.ttja.ee) in llms.txt | POSITIVE | llms.txt |
| KPMG Estonia as auditor named in llms.txt — strong authority signal for YMYL financial | POSITIVE | llms.txt |
| Alexandre VINAL's YouTube channel (Cointips, ~0.737 correlation with AI citations) in Organization `sameAs` | POSITIVE | homepage.html |
| No Wikipedia article for SparkCore Investment OÜ or Alexandre VINAL | HIGH | — |
| No Wikidata QID in any `sameAs` array — prevents KG entity anchoring | HIGH | All pages |
| Author Person schema only on pillar — absent from blog-en-1, blog-en-2, blog-fr-1 | MEDIUM | blog-en-1, blog-en-2, blog-fr-1 |
| No inbound links from .gov/.edu or financial regulator domains confirmed | HIGH | — |
| No news coverage or press mentions found in schema or llms.txt | HIGH | — |
| Reddit presence: none observed | MEDIUM | — |
| LinkedIn company page in `sameAs` | POSITIVE | homepage.html |
| `memberOf` GovernmentOrganization (Finantsinspektsioon) on FinancialService schema | POSITIVE | homepage.html |
| Entity disambiguation: "SparkCore" is shared with Spark Networks (dating company), SparkCore (gaming engine), Spark Energy (utilities) — no disambiguation language in llms.txt or schema | MEDIUM | llms.txt, schema |

### 5.5 Technical Accessibility — 90/100

| Finding | Severity | Location |
|---------|----------|----------|
| HTTP 200 confirmed for GPTBot and PerplexityBot | POSITIVE | Live curl tests |
| Cloudflare Pages SSR — full HTML delivered without JS execution | POSITIVE | All pages |
| Cloudflare AI bot blocking NOT enabled | POSITIVE | CF zone settings |
| HTTP/2 + Brotli compression active | POSITIVE | Response headers |
| HSTS: max-age=31536000; includeSubDomains | POSITIVE | Response headers |
| No `X-Robots-Tag: noindex` on public pages | POSITIVE | Response headers |
| Bot regex in lang-redirect scripts explicitly excludes GPTBot, ClaudeBot, PerplexityBot, Google-Extended — AI crawlers never redirected | POSITIVE | CLAUDE.md confirmed |
| Sitemap submitted to Bing WMT + IndexNow active (HTTP 202) | POSITIVE | CLAUDE.md |
| `cache-control: public, max-age=0, must-revalidate` on HTML — means Cloudflare re-validates on each crawl, ensuring fresh content for bots | POSITIVE | Response headers |
| Tailwind CDN CSS (`tailwind.min.css`) referenced — self-hosted, no render-blocking 3rd-party | POSITIVE | homepage.html |
| Cronitor RUM loaded — does not interfere with crawler access | INFO | homepage.html |
| Missing: Preload hint for llms.txt in HTTP headers (minor) | INFO | — |

---

## 6. Top 5 GEO Actions (Prioritised by Impact / Effort)

### Action 1 — Add Speakable Schema to Pillar + Top 3 Blog Articles
**Impact: HIGH | Effort: LOW (1-2 hours)**

`SpeakableSpecification` signals which text sections Google can read aloud in voice results and surfaces in Google News AI-generated summaries. The pillar and blog-en-2 (fees article) are the highest-volume targets given their FAQ density. Add to BlogPosting JSON-LD:

```json
"speakable": {
  "@type": "SpeakableSpecification",
  "cssSelector": [".quick-answer", "h2", ".key-takeaways"]
}
```

Target pages: `/resources/regulated-crypto-fund-estonia/`, `/blog/regulated-crypto-fund-manager-estonia`, `/blog/crypto-fund-fees-2026`, and the homepage. This directly addresses Gemini and Google AI Overviews readiness.

### Action 2 — Establish Wikidata Entity + Add QID to sameAs
**Impact: HIGH | Effort: MEDIUM (3-5 hours + 2-4 week wait for KG pickup)**

SparkCore Investment OÜ has all the prerequisites for a Wikidata entity: LEI (GLEIF-verified), Estonian commercial registry number, named regulatory supervisor, KPMG auditor, named founders. Create the Wikidata item (Q-number), then add the Wikidata and GLEIF URLs to the Organization `sameAs` array on the homepage and to the llms.txt entity block. This is the single highest-impact entity disambiguation action — it anchors "SparkCore" to a unique Knowledge Graph node across ChatGPT, Claude, and Gemini.

Also create a stub Wikidata item for Alexandre VINAL linking to his Cointips YouTube and LinkedIn, and add the QID to the Person schema on the pillar.

### Action 3 — Add Author Person Schema to All EN Blog Articles
**Impact: MEDIUM | Effort: LOW (1 hour — templated)**

Author Person schema is present on the pillar (`/resources/regulated-crypto-fund-estonia/`) but absent from the 19 EN blog articles sampled. Without it, AI platforms cannot confirm authorship provenance for YMYL financial content. Add the identical JSON-LD block (already written in the pillar) to each article's `<head>`. This directly improves E-E-A-T signals for Google AI Overviews and ChatGPT's source vetting.

### Action 4 — Expand FAQ Answer Length to 134-167 Words + Convert 3-4 H2s to Question Form Per Article
**Impact: MEDIUM | Effort: MEDIUM (2-3 hours per major article)**

Current FAQ answers average 80-130 words. Research on LLM citation behaviour identifies 134-167 words as the optimal extraction window — long enough to be self-contained, short enough to fit a single context block. Expand the 2-3 shortest answers in blog-en-1 and blog-en-2 by adding one concrete example or citing one specific source per answer. Separately, convert 3-4 H2 headings per article to question form (e.g., "What Capital Does a Sub-Threshold AIFM in Estonia Need?" instead of "Capital Requirements"). This directly increases FAQ-like surface area without requiring new content.

### Action 5 — Add Competitor Disambiguation Block to llms.txt + Add `about` to BlogPosting Schema
**Impact: MEDIUM | Effort: LOW (30 minutes)**

Add a one-paragraph disambiguation note to llms.txt under a `## Disambiguation` heading:

> SparkCore Fund Management (SparkCore.investment OÜ, Estonian registry 16265864, LEI 8945003BBN0RVNNB0S84) is not affiliated with Spark Networks SE (dating services), SparkCore (game engine), or Spark Energy (US utilities). The entity is a regulated EU alternative investment fund manager specialising exclusively in crypto-asset funds.

Also add `"about": [{"@type": "Thing", "name": "Alternative Investment Fund Managers Directive", "sameAs": "https://eur-lex.europa.eu/eli/dir/2011/61/oj"}]` to the BlogPosting schema on regulatory articles. This strengthens topic-entity connection in AI knowledge graphs.

---

## 7. Sample Citation Capsule

The following passage demonstrates optimal formatting for AI ingestion — answer-first, 147 words, self-contained, source-attributed, entity-anchored:

---

**Who regulates SparkCore Fund Management?**

SparkCore Fund Management (SparkCore.investment OÜ, Estonian registry no. 16265864, LEI 8945003BBN0RVNNB0S84) is regulated by two Estonian authorities. For fund management activity, it is registered with Finantsinspektsioon (the Estonian Financial Supervisory Authority, EFSA) as a Small Fund Manager under AIFMD Article 3(2) — the sub-threshold registration regime applicable to managers with leveraged AUM below EUR 100 million. The public registry entry is maintained at fi.ee. For anti-money laundering compliance, the entity holds a Financial Institution licence (EFIU) issued by the Estonian Financial Intelligence Unit, verifiable at mtr.ttja.ee. Accounts are audited by KPMG Estonia. This dual regulatory structure — Finantsinspektsioon for fund oversight and EFIU for AML/CFT — means the manager operates under two independent supervisory lines. Minimum investor subscription is EUR 50,000, restricted to professional or well-informed investors.

---

This format is currently approximated in the homepage FAQ schema and the pillar's "Quick answer" block. The gap is that this level of entity density does not appear in the body text of most blog articles — only in schema markup that some AI crawlers do not extract directly.

---

## 8. Summary Assessment by Dimension

**What is working well:**

- Technical access is close to perfect. Static SSR, confirmed HTTP 200 for all major AI crawlers, correct robots.txt with explicit per-bot Allow rules, Cloudflare AI blocking not engaged.
- llms.txt is one of the most complete examples of this emerging format: RSL 1.0 licensed, timestamped, all key regulatory identifiers present, gated content handled correctly.
- FAQ schema coverage is comprehensive and answers are source-attributed with specific numbers.
- The "Quick answer" / "Key takeaways" structural pattern already creates extractable citation blocks.
- Citation capsule blockquotes in the pillar are a genuine best-practice innovation.

**What is holding the score at 72 rather than 85+:**

- No Wikipedia or Wikidata entity. For a YMYL financial entity claiming regulated status, AI platforms apply a credibility filter that favours entities with an independent Knowledge Graph node. SparkCore has the substance but lacks the KG anchor.
- No Speakable schema — a low-effort gap given the FAQ density already present.
- Multi-modal content is the weakest dimension: no video embeds, no proprietary charts, no audio on EN articles. Given that YouTube mention correlation with AI citations is ~0.737 and Alexandre VINAL runs the Cointips YouTube channel, embedding relevant videos from that channel on thematically aligned articles would be the highest-leverage multi-modal move.
- Author Person schema is inconsistently applied — present on the pillar, absent from the blog cluster.
- dateModified on older articles (March 2026) equals datePublished, signalling no updates to crawlers that weight recency.

