# Content Quality & E-E-A-T Audit — sparkcore.fund
**Audit date:** 2026-05-08 · **Auditor:** Claude Code (content-quality specialist) · **Framework:** Google QRG September 2025

---

## Scores

| Dimension | Score | Grade |
|---|---|---|
| **E-E-A-T (YMYL weighted)** | **61 / 100** | C+ |
| **Content Depth & Coverage** | **78 / 100** | B+ |
| **Readability (institutional fit)** | **82 / 100** | B+ |
| **Keyword optimization** | **74 / 100** | B |
| **AI Citation Readiness** | **70 / 100** | B− |
| **Freshness signals** | **52 / 100** | D+ |
| **Hub-Spoke architecture** | **68 / 100** | C+ |
| **Overall Content Quality** | **69 / 100** | C+ |

---

## E-E-A-T Breakdown (YMYL financial site)

### Experience — 14 / 20

**What's strong:** The SparkCore article on `regulated-crypto-fund-manager-estonia` includes a first-person case study section ("SparkCore Fund Management: A Case Study") that references actual compliance infrastructure — dual MLRO structure, KPMG for fund accounting, KYC/KYB programme — demonstrating lived operational experience rather than generic summarisation. The `crypto-fund-fees-2026` article cites data from five named third-party sources (PwC/Elwood, AIMA, bfinance, Crypto Insights Group, 21e6 Capital) and frames them from the perspective of an active AIFM. These are real first-hand signals.

**What's missing:**
- No authored author-bio box on any article page. The byline `By Alexandre VINAL` with a LinkedIn link is present in visible HTML on all sampled pages, but there is no below-the-fold bio section with credentials, years of experience, or fund track record. For YMYL financial content this is a material gap — Google's QRG specifically tests whether the author has verifiable expertise.
- No "About the author" schema `sameAs` array on the `Person` block in article JSON-LD. The schema only has `"url": "https://www.linkedin.com/in/alexandrevinal/"` — no `sameAs` list pairing the LinkedIn URL with e.g. the YouTube channel or company page. The Organisation schema on the homepage correctly uses `sameAs` for founders, but the pattern is not replicated at the article level.
- No audited track-record snippet, performance history, or NAV link from article pages. This is expected for gated content, but no article even references that audited NAV exists.

### Expertise — 18 / 25

**What's strong:** The EN regulatory cluster demonstrates genuine technical expertise. The article `regulated-crypto-fund-manager-estonia` correctly describes AIFMD Article 3(2) sub-threshold thresholds (€100M leveraged / €500M unleveraged), the usaldusfond structure, the dual FI supervision model (Finantsinspektsioon + FIU), and the MLRO requirement — all technically accurate and specific to Estonian law. Citations include the actual Estonian Investment Funds Act (riigiteataja.ee), the AIFMD text on EUR-Lex, the FI.ee registry, and GLEIF. These are primary source citations, not secondary summaries. The fees article accurately sources the PwC/Elwood 2019 baseline, bfinance 231-fund April 2024 sample, and distinguishes open-ended funds from SMAs and FoFs.

**What's missing:**
- The pillar page `/resources/regulated-crypto-fund-estonia/` uses only `"url": "https://www.linkedin.com/in/alexandrevinal/"` in its standalone `Person` schema — `sameAs` array is absent. The pillar is the highest-authority page on the site and should have the strongest author credentials.
- No explicit qualifications listed (e.g., CFA, CAMS, legal background) for any of the three founders anywhere in the article content. The homepage body references "over 7 years in financial markets" and "20+ years in trading" (from the FAQ schema) but this is not surfaced in visible article bylines or bio boxes.
- The FR cluster (`strategies-options-protection-portefeuille-actions`, `le-vrai-cout-du-market-timing`) covers options hedging and market timing — topics where financial credentials are important for YMYL treatment. Alexandre VINAL is the sole author across all articles; his options/derivatives expertise is not established anywhere on the site.

### Authoritativeness — 14 / 25

**What's strong:** The Organisation schema on the homepage has `sameAs` pointing to LinkedIn, GLEIF record, and the FI.ee public registry entry — three independently verifiable authoritative external references. The footer on every page links to the actual Finantsinspektsioon public registry entry and the EFIU licence page (mtr.ttja.ee). KPMG Estonia and Hedman Partners are named on the homepage as auditor and legal counsel.

**What's missing:**
- No third-party editorial coverage or backlinks from authoritative financial media visible in the content (no "as seen in", no external mentions cited). For a YMYL financial site, lack of external validation is the weakest point. The site is self-referential — it establishes regulatory status through its own claims and links to regulators who confirm existence, but has no press mentions, analyst citations, or industry database inclusions referenced.
- The `legalName` in schema is inconsistently formatted: homepage uses `"SparkCore.investment OÜ"` (with period, matching the commercial registry), but this is unusual. This is technically correct but the period in the company name may confuse structured data parsers.
- No explicit mention of KPMG audit in any article (only homepage visible text). An article-level reference to the auditor would strengthen authoritativeness signals on content pages.

### Trustworthiness — 15 / 30

**What's strong:** Every page footer (EN and FR) contains: Finantsinspektsioon hyperlink, EFIU licence link, Reg. No. 16265864, LEI `8945003BBN0RVNNB0S84`, physical address. Both articles and footer carry a risk disclaimer. The pillar page and blog-en-1 carry a full inline disclaimer box: "This article is provided for informational purposes only and does not constitute investment advice, a solicitation, or an offer to invest. Investing in crypto-asset funds involves significant risk, including the possible loss of all capital invested." Qualified investor language is present on all sampled pages. The homepage has no standalone risk disclaimer in the visible body (footer disclaimer only) — this is a gap for the homepage, which is the first page most visitors land on.

**What's missing:**
- **Homepage lacks a visible investment disclaimer in the body.** The footer disclaimer exists but a YMYL financial homepage for a regulated fund manager should carry a prominent disclaimer above the fold or immediately after the CTA section. Google QRG rates trustworthiness lower when risk disclosures are buried.
- `dateModified` equals `datePublished` on all four sampled pages. This signals content has never been reviewed or updated after publication. For a YMYL financial site covering rapidly evolving regulatory topics (AIFMD II transposition April 2026, MiCA legacy VASP licence expiry July 2026), stale `dateModified` signals are a significant trust deficit. The pillar was published 2026-05-06 and `dateModified` is also 2026-05-06 despite covering AIFMD II whose transposition date was April 2026.
- No editorial review signal anywhere. No "reviewed by" field, no "last reviewed" date, no compliance team sign-off. For a Finantsinspektsioon-supervised entity publishing investment-related content, absence of an editorial review process is a QRG red flag.
- No terms of use or cookie/consent disclosures linked from article pages (only Privacy Policy is linked in the footer).

---

## Content Depth Findings

| Page | Body word count | Schema `wordCount` | Min for type | Status |
|---|---|---|---|---|
| Homepage | ~1,038 | — | 500 | PASS |
| Pillar `/resources/regulated-crypto-fund-estonia/` | ~3,810 | 3,000 | 1,500 | PASS |
| `regulated-crypto-fund-manager-estonia` | ~2,876 | 2,462 | 1,500 | PASS |
| `crypto-fund-fees-2026` | ~2,545 | 2,600 | 1,500 | PASS |
| `strategies-options-protection-portefeuille-actions` (FR) | ~5,474 | 4,800 | 1,500 | PASS |

All sampled pages clear the blog post minimum (1,500 words). The FR options article at ~5,474 words is the deepest piece in the sample — it includes SVG charts, cost tables, and VIX call mechanics. `crypto-fund-fees-2026` at ~2,545 words is adequate but the schema `wordCount` (2,600) is within rounding of the actual count.

**Information gain check (`crypto-fund-fees-2026`):** This article adds genuine original structuring of third-party data. It places PwC/Elwood 2019 (23.5% perf fee) alongside 2025 Crypto Insights Group (20%) to show convergence, compares crypto vs. traditional hedge funds side-by-side using Preqin data, and provides two original SVG bar/line charts and a donut chart showing HWM vs. hurdle rate prevalence. The charts are not generic stock imagery — they encode actual data points. This is above the threshold of "synthesises public knowledge with original framing."

**Schema `wordCount` discrepancy:** `blog-en-1` schema reports 2,462 words vs. measured ~2,876. This is a 17% understatement. Minor but worth correcting for accuracy.

---

## Readability Assessment

The EN regulatory cluster (`regulated-crypto-fund-manager-estonia`, pillar) is written at a professional institutional level. Sentences are complex but structured: "The usaldusfond is not a separate legal entity; rather, it is a pool of assets managed by a general partner (the AIFM) on behalf of limited partners (the investors)." Estimated Flesch-Kincaid Grade Level: 14-16 (appropriate for the target audience of fund managers, family offices, legal counsel evaluating jurisdiction choice). No unnecessary jargon padding; technical terms (usaldusfond, tegevusloata väikefondi valitseja) are defined on first use.

The FR cluster (`strategies-options-protection-portefeuille-actions`) is equally dense and data-driven. The opening paragraph mentions JHEQX -8.06% vs. S&P -18.1% in 2022 and Universa +4,144% Q1 2020 — precision expected by the HNW investor audience.

No readability issues found for this audience. Readability score: 82/100.

---

## Duplicate Content Risk

**EN vs FR clusters are genuinely independent.** The FR article (`strategies-options`) has zero cross-links to any EN `/blog/` URL. The EN cluster has zero hreflang alternates pointing to FR. Topic overlap is minimal: EN covers regulatory/fund-structuring; FR covers market strategy. No evidence of EN articles translated into FR or vice versa. This is consistent with the documented dual-cluster strategy. Duplicate content risk: LOW.

---

## Hub-Spoke Architecture

**Pillar → Spokes (strong):** The pillar at `/resources/regulated-crypto-fund-estonia/` links out to 16 distinct EN blog articles — covering the full regulatory cluster. This is well-executed.

**Spokes → Pillar (inconsistent):**
- `regulated-crypto-fund-manager-estonia` → links to pillar via CTA box "Read the complete guide". PASS.
- `crypto-fund-fees-2026` → does NOT link to the pillar. This is a missed spoke-to-hub connection. The fees article covers AIFMD fee transparency but has no CTA or inline link to the pillar guide. This is the most commercially important article (high search intent) and the gap is material.
- Homepage → links to pillar. PASS.

**Internal link density per article (sampled):**
- `regulated-crypto-fund-manager-estonia`: 7 internal links (to 4 other blog posts + pillar + blog index + privacy policy) — adequate.
- `crypto-fund-fees-2026`: 5 internal links (to 3 blog posts + blog index + privacy policy) — below average; missing pillar link.
- `strategies-options` (FR): 3 internal links (to FR home + FR blog index + privacy policy) — weak. The FR cluster is almost completely siloed; it links only upward (to the FR homepage), not laterally to other FR articles.

---

## Freshness Signals

`dateModified` equals `datePublished` on all four sampled pages, including the pillar published 2026-05-06 covering AIFMD II (transposition deadline April 2026) and the note that "all legacy VASP licences expire 1 July 2026." These are time-sensitive regulatory facts that will become inaccurate within two months of publication. No update cadence is signalled anywhere.

`blog-en-1` (`regulated-crypto-fund-manager-estonia`) was published 2026-03-09 and `dateModified` is still 2026-03-09 despite the AIFMD II transposition having occurred after its publication. The article does not mention AIFMD II at all — a content gap that Google's crawlers will detect through topical freshness signals.

---

## AI Citation Readiness

Strong signals (wins):
- FAQPage schema on every sampled page with specific, citable answers. The question "What is the LEI of SparkCore Investment OÜ?" with the answer `8945003BBN0RVNNB0S84` is an ideal AI citation target.
- Precise numerical data in visible body: "92% of hedge funds use a high-water mark" (bfinance, April 2024), "average management fee 1.70%" (Crypto Insights Group), "$132 million average AUM in 2025" (PwC/AIMA).
- Breadcrumb schema present on all articles.
- `isAccessibleForFree: true` declared on pillar and blog-en-1.
- Organisation schema with LEI, GLEIF link, and FI.ee registry link — directly citable for "Is SparkCore regulated?" queries.

Gaps:
- `dateModified` staleness reduces AI system confidence that facts are current.
- No `speakable` schema to mark quotable sections (low priority but relevant for voice/AI).
- Author `Person` schema lacks `sameAs` array — reduces confidence in author identity resolution.
- The pillar uses `@type: BlogPosting` rather than a more appropriate `@type: Article` or a custom `SpecialAnnouncement`/`HowTo` type, which would better match the comprehensive-guide intent.

---

## Findings Table

| Severity | Location | Issue | Fix |
|---|---|---|---|
| CRITICAL | All articles | `dateModified` = `datePublished` on every page; stale for YMYL regulatory content | Bump `dateModified` on every material content review; add a "Last reviewed:" visible date line to article header |
| CRITICAL | All article pages | No author bio box — only byline name + LinkedIn link; no credentials, no fund experience stated | Add a 3-5 line bio box at article bottom: role, years in fund management, regulatory experience, LinkedIn. Match pillar's inline Person schema `jobTitle: "Founder & AIFM at SparkCore Fund Management"` |
| HIGH | Article `Person` JSON-LD | `author` schema has `"url"` field only; missing `"sameAs"` array | Add `"sameAs": ["https://www.linkedin.com/in/alexandrevinal/", "https://www.youtube.com/@cointips"]` to every article `Person` block |
| HIGH | `crypto-fund-fees-2026` | No link to pillar page (`/resources/regulated-crypto-fund-estonia/`) despite covering AIFMD fee disclosure in depth | Add a CTA block: "For the complete guide to setting up a regulated crypto fund in Estonia, see our pillar guide →" |
| HIGH | Homepage body | No visible investment risk disclaimer in the page body (only footer) | Add a 1-sentence disclaimer under the fund cards section: "Investing in crypto-asset alternative investment funds involves risk including loss of capital. For professional and qualified investors only." |
| HIGH | `regulated-crypto-fund-manager-estonia` | Published 2026-03-09; AIFMD II transposition occurred April 2026; article does not mention AIFMD II | Add a paragraph in Section 6 (Compliance Infrastructure) noting AIFMD II transposition and its practical scope for crypto fund managers; bump `dateModified` |
| MEDIUM | FR cluster (`strategies-options`) | Only 3 internal links — home, FR blog index, privacy policy; zero lateral links to other FR articles | Add 2 internal links to related FR articles (`indicateurs-marche-crypto-actifs`, `le-vrai-cout-du-market-timing`) in closing section |
| MEDIUM | All EN blog articles | No explicit "fact-checked" or "reviewed by" signal; no editorial review process documented | Add a minimal "This article was reviewed by the SparkCore compliance team on [date]" line or schema `reviewedBy` field |
| MEDIUM | `blog-en-1` schema | `wordCount` reports 2,462 but body count is ~2,876 (17% understatement) | Update `wordCount` to 2,876 |
| MEDIUM | Homepage | Risk disclaimer only in footer; "For qualified investors" language in meta but not prominent in body hero or fund cards | Reinforce qualified-investor gate language in visible body near the fund cards |
| LOW | Pillar JSON-LD | Uses `@type: BlogPosting`; a comprehensive guide is better typed as `@type: Article` with `articleSection` properties | Change to `"@type": "Article"` and add `"articleSection": "Regulated Crypto Funds"` |
| LOW | `legalName` in all schema | `"SparkCore.investment OÜ"` includes a period that may confuse parsers; commercial registry name should be checked for exact spelling | Verify against e-Business Registry record; if the period is official, add `"alternateName": "SparkCore Investment OÜ"` |
| LOW | All EN articles | OG image defaults to `meta-image.webp` (generic site logo) on most articles; pillar and FR article use Unsplash per-article images | Use distinct per-article OG images for all EN blog posts to improve social sharing signal differentiation |

---

## Summary

sparkcore.fund has a structurally sound content foundation for a YMYL financial site: every page carries regulatory status in the footer (LEI, Finantsinspektsioon link, EFIU licence, Reg. No.), investment disclaimers are present in article bodies, qualified investor language is consistent, and the EN regulatory cluster demonstrates genuine technical expertise with primary source citations.

The two critical deficits blocking a higher E-E-A-T score are: (1) the complete absence of author bio boxes with verifiable credentials on any article page — for Google QRG, the byline `By Alexandre VINAL` with a LinkedIn URL is necessary but not sufficient; (2) `dateModified` frozen at `datePublished` on every page, which signals to both Google and AI systems that YMYL regulatory content covering AIFMD II and MiCA has never been reviewed since launch. For a site covering a regulatory framework with an April 2026 transposition deadline, this is a credibility gap that erodes trust scores across the EN cluster.

The hub-spoke architecture is 70% complete: the pillar links out comprehensively to spokes, but two high-traffic articles (`crypto-fund-fees-2026` and the FR options piece) do not link back to the hub. The FR cluster is correctly independent from EN in topic and linking, with zero duplication risk, but it is internally under-linked (3 links per article vs. 7 in the best EN article).
