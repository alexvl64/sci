# Schema.org / JSON-LD Audit — sparkcore.fund
**Date:** 2026-05-16 | **Baseline:** 52/100 (2026-05-08) | **Sprint 1 commit:** a3df92f (Speakable + WebSite)

Raw extracts: `MD/seo/audit-2026-05-16/data/jsonld-extracts.json`

---

## Pages Audited

| Label | URL | Blocks |
|---|---|---|
| homepage_en | `https://sparkcore.fund/` | 3 |
| homepage_fr | `https://sparkcore.fund/fr/` | 2 |
| pillar | `https://sparkcore.fund/resources/regulated-crypto-fund-estonia/` | 4 |
| article_en_1 | `/blog/regulated-crypto-fund-manager-estonia` | 3 |
| article_en_2_fees | `/blog/crypto-fund-fees-2026` | 3 |
| article_en_3 | `/blog/estonia-luxembourg-malta-crypto-fund` | 3 |
| article_fr_1 | `/fr/blog/clarity-act-us-impacts-investisseurs` | 3 |
| article_fr_2_strc | `/fr/blog/strc-strategy-yield-sous-remunere-analyse` | 3 |
| privacy_policy | `/privacy-policy` | 0 |
| blog_index_en | `/blog/` | 1 |
| blog_index_fr | `/fr/blog/` | 1 |

Note: The task brief referenced `/fr/blog/strc-strategy-yield-analysis` — that slug returns HTTP 404. The live URL is `/fr/blog/strc-strategy-yield-sous-remunere-analyse` (audited correctly above).

---

## Sprint 1 — Closed Findings (from 2026-05-08)

| 2026-05-08 Finding | Status | Evidence |
|---|---|---|
| **CRITICAL** — No `@id` on Organization, FinancialService, Person, BlogPosting | **CLOSED** | All homepage `@graph` nodes carry `@id`; all BlogPosting blocks carry `@id`; three founder Person nodes carry `@id` anchors in homepage `@graph` |
| **CRITICAL** — Author Person missing `sameAs` and `jobTitle` on all articles | **CLOSED** | All sampled BlogPosting blocks now include inline author with `@id`, `jobTitle`, and `sameAs` array (LinkedIn + YouTube) |
| **CRITICAL** — Pillar typed `BlogPosting` | **CLOSED** | Pillar now `"@type": "Article"` with `"articleSection": "Regulatory Guide"` |
| **HIGH** — No `WebSite` schema | **CLOSED** — partial | `WebSite` node present in homepage `@graph` with `@id`; but `potentialAction` / `SearchAction` is still absent (see finding H-1 below) |
| **HIGH** — `image` is bare string URL | **CLOSED** | All audited articles now use `{"@type": "ImageObject", "url": ..., "width": ..., "height": ...}` |
| **HIGH** — `crypto-fund-fees-2026` future `datePublished: 2026-05-12` | **CLOSED** | `datePublished` is now `2026-04-01` (past date, correct) |
| **MEDIUM** — No `speakable` anywhere | **CLOSED** — partial | Speakable added on pillar, article_en_1/2/3, homepage EN/FR WebPage nodes; but `article_fr_1` (clarity-act) is **missing** speakable (see finding M-1) |
| **MEDIUM** — No `WebPage` schema on homepage | **CLOSED** | `WebPage` nodes with `@id`, `isPartOf`, `about`, `speakable` present on both homepage EN and FR |
| **INFO** — Publisher URL trailing-slash inconsistency | **PARTIALLY CLOSED** | Organization `url: "https://sparkcore.fund/"` is correct on homepage `@graph`. Blog index `publisher.url` still uses `"https://sparkcore.fund"` (no trailing slash, no `@id`) — see finding M-2 |

---

## What Passes

**All JSON-LD blocks are syntactically valid.** No parse errors across 11 pages.

**`@context`** is `"https://schema.org"` (HTTPS) on all blocks. No HTTP variants.

**Homepage `@graph` (EN and FR)** — comprehensive and well-structured:
- `Organization` with `@id`, `leiCode`, `taxID`, `sameAs` (LinkedIn, YouTube, GLEIF, Finantsinspektsioon registry), `logo` as `ImageObject`, correct `legalName`
- `FinancialService` with `@id`, `memberOf GovernmentOrganization` (Finantsinspektsioon), `areaServed`, `PostalAddress`
- `WebSite` with `@id`, `publisher` referencing org by `@id`
- `WebPage` with `@id`, `isPartOf`, `about` (org reference), `inLanguage`, `speakable`
- Three founder `Person` nodes with `@id`, `jobTitle`, `sameAs`, `worksFor` (org reference by `@id`)

**Article author Person** — now correct template: `@id` references homepage anchor, `jobTitle` (EN/FR localised per CLAUDE.md convention), `sameAs` array with LinkedIn and YouTube.

**BreadcrumbList** — present on pillar and all blog articles. ItemListElement has correct `position`, `name`, `item`.

**Pillar `Article`** — correct `@type: Article`, `articleSection: "Regulatory Guide"`, `speakable`, `isAccessibleForFree: true`, `image` as `ImageObject`, `about` array with `Thing` references to AIFMD/AIFMDII/MiCA/Finantsinspektsioon with `sameAs` EU Lex URLs.

**BlogPosting articles (EN articles 1, 3; FR articles 1, 2)** — all have `@id`, `isAccessibleForFree: true`, `image` as `ImageObject`, `about` array, `inLanguage`, `wordCount`, `keywords`.

**New FR article (strc)** — all required fields present: `@id`, author with full `@id`/`jobTitle`/`sameAs`, `image` as `ImageObject` (1260×750), `BreadcrumbList`, `FAQPage`. `isAccessibleForFree` is **missing** (see M-3).

**FAQPage** — present on homepage EN/FR (6 questions each), pillar (6 Q), and all sampled blog articles. Answers match visible content (spot-checked pillar and fees article).

**Dates** — all audited articles use valid ISO 8601 `YYYY-MM-DD`. No future dates found.

---

## Findings

### Critical

None. The three 2026-05-08 critical findings are fully resolved.

---

### High

**H-1 — WebSite present but `potentialAction` / `SearchAction` still missing**
Both homepage EN and FR carry a `WebSite` node, but it has no `potentialAction`. The 2026-05-08 snippet (4a) recommended `SearchAction` for sitelinks searchbox. The `WebSite` block is already deployed — adding `SearchAction` is a one-line JSON addition, zero risk.

Fix: add to the `WebSite` node in both homepage `@graph` blocks:
```json
"potentialAction": {
  "@type": "SearchAction",
  "target": {
    "@type": "EntryPoint",
    "urlTemplate": "https://sparkcore.fund/blog/?s={search_term_string}"
  },
  "query-input": "required name=search_term_string"
}
```

**H-2 — Pillar `Article` `@id` has no trailing slash, but `url` and `mainEntityOfPage` have one**

The `@id` is `https://sparkcore.fund/resources/regulated-crypto-fund-estonia#article` (no slash before `#`), while `url` and `mainEntityOfPage["@id"]` are `https://sparkcore.fund/resources/regulated-crypto-fund-estonia/` (with trailing slash). For entity merging, the base URL component of `@id` should be canonical and match the page URL exactly.

Fix: change `@id` to `"https://sparkcore.fund/resources/regulated-crypto-fund-estonia/#article"` (add slash before `#`).

**H-3 — Pillar standalone `Person` block duplicates the homepage `@graph` Person but is missing `@id`**

The pillar carries a 4th JSON-LD block: a `Person` for Alexandre VINAL with `name`, `url`, `jobTitle`, `sameAs`, `worksFor`. This standalone block has no `@id`, so it cannot be merged with the canonical `https://sparkcore.fund/#person-alexandre-vinal` anchor. It also has a different `jobTitle` value (`"Founder & AIFM at SparkCore Fund Management"`) than the homepage (`"Founder & Managing Partner, SparkCore Fund Management"`), creating divergent signals. The inline author object on the `Article` block is already correct (uses `@id` reference). The standalone block is redundant.

Fix: remove the standalone `Person` JSON-LD block from the pillar (the inline author on the `Article` block is sufficient and correct). If kept, add `"@id": "https://sparkcore.fund/#person-alexandre-vinal"` and align `jobTitle` with the homepage value.

---

### Medium

**M-1 — `speakable` missing on `article_fr_1` (clarity-act)**

All EN articles, the pillar, and homepage EN/FR now have `speakable`. The `clarity-act-us-impacts-investisseurs` FR article does not. Sprint 1 commit a3df92f added speakable to the EN template; the FR article template appears not to have received the same treatment.

Fix: add to the `BlogPosting` block:
```json
"speakable": {
  "@type": "SpeakableSpecification",
  "cssSelector": ["h1", "h2"]
}
```

**M-2 — Blog index `publisher` is inline Object without `@id` and missing trailing slash**

Both `/blog/` and `/fr/blog/` have a `Blog` block with an inline `publisher` Organization object (`url: "https://sparkcore.fund"`, no trailing slash, no `@id`). This prevents entity merging with `#organization`. The `Blog` node itself also has no `@id`.

Fix: replace inline publisher with a reference, and add `@id` to the Blog:
```json
{
  "@type": "Blog",
  "@id": "https://sparkcore.fund/blog/#blog",
  ...
  "publisher": { "@id": "https://sparkcore.fund/#organization" }
}
```
Apply the same pattern to `/fr/blog/` with `@id: "https://sparkcore.fund/fr/blog/#blog"`.

**M-3 — `isAccessibleForFree` missing on `crypto-fund-fees-2026` and `strc` FR article**

`article_en_2_fees` (`/blog/crypto-fund-fees-2026`) and `article_fr_2_strc` (strc) are both missing `"isAccessibleForFree": true`. All other sampled articles carry this property. For a YMYL financial site, signalling open access (vs paywalled) helps Google's quality assessors and rich result eligibility.

Fix: add `"isAccessibleForFree": true` to both BlogPosting blocks.

**M-4 — `dateModified` frozen at `datePublished` on strc FR article**

`strc-strategy-yield-sous-remunere-analyse` has `datePublished: 2026-05-11` and `dateModified: 2026-05-11` (identical). Per CLAUDE.md Mode A quarterly review cadence, this is expected for a brand-new article, but should be tracked for the July 2026 quarterly pass. No immediate action, but flagged per audit process.

**M-5 — Nav `ItemList` incomplete — missing Resources and Contact entries**

The homepage EN `ItemList` still lists only 3 nav items: Home, Blog, Privacy Policy. The live site navigation includes a Resources section (pillar at `/resources/`) and the sidebar CTA. This mismatch was flagged at 2026-05-08 as High, but since ItemList is cosmetic (no rich result tied to it) and the homepage `@graph` now has proper `WebSite`, this is downgraded to Medium.

Fix: extend `itemListElement` to include:
```json
{ "@type": "SiteNavigationElement", "position": 4, "name": "Resources", "url": "https://sparkcore.fund/resources/regulated-crypto-fund-estonia/" }
```

**M-6 — `/privacy-policy` still has zero schema**

No schema whatsoever. A minimal `WebPage` block would complete the entity graph and signal to crawlers that this page belongs to the site.

Fix (from 2026-05-08 snippet 4f, unchanged):
```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "@id": "https://sparkcore.fund/privacy-policy#webpage",
  "url": "https://sparkcore.fund/privacy-policy",
  "name": "Privacy Policy — SparkCore Fund Management",
  "inLanguage": "en",
  "isPartOf": { "@id": "https://sparkcore.fund/#website" },
  "publisher": { "@id": "https://sparkcore.fund/#organization" },
  "breadcrumb": {
    "@type": "BreadcrumbList",
    "itemListElement": [
      { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://sparkcore.fund/" },
      { "@type": "ListItem", "position": 2, "name": "Privacy Policy", "item": "https://sparkcore.fund/privacy-policy" }
    ]
  }
}
```

---

### Info

**I-1 — `speakable` uses generic `["h1", "h2"]` CSS selectors across all pages**

Every speakable block uses `cssSelector: ["h1", "h2"]`. Google's speakable spec works best when the selector points to specific, stable, authoritative content regions (e.g., a hero summary paragraph, a key-facts div). Using heading tags selects the full heading text of every section — appropriate as a baseline but imprecise for GEO/voice citation purposes. Consider adding a third selector pointing to the intro paragraph or a `.key-takeaways` block on article pages.

No urgent action. The current implementation is valid and better than no speakable.

**I-2 — `FAQPage` on commercial financial site**

FAQPage blocks are present on homepage (EN+FR) and all blog articles. Per agent rules: FAQPage rich results were restricted by Google to government and healthcare sites in August 2023. These blocks will not generate Google FAQ rich results. They remain beneficial for AI/LLM citation (GEO signal). Status unchanged from 2026-05-08. Document the decision as a code comment if not already done.

**I-3 — `article_en_3` missing `isAccessibleForFree` — verified present**

2026-05-08 listed this as missing. Confirmed present in live data: `"isAccessibleForFree": true`. Closed.

**I-4 — `dateModified` review cadence**

`article_en_1` (`regulated-crypto-fund-manager-estonia`) shows `dateModified: 2026-05-08` vs `datePublished: 2026-03-09`. This is the first modifier bump. Next quarterly review target: August 2026 (Mode A cadence per CLAUDE.md). For an article covering AIFMD II transposition (April 2026 deadline), a content update is editorially warranted before August.

---

## Score: 74 / 100

| Area | Weight | 2026-05-08 | 2026-05-16 | Delta |
|---|---|---|---|---|
| Entity identity (`@id` consistency, org/person anchors) | 25% | 8/25 | 22/25 | +14 |
| Article schema completeness (author, image, dates, isAccessibleForFree) | 20% | 10/20 | 17/20 | +7 |
| YMYL signals (leiCode, taxID, sameAs GLEIF, memberOf regulator) | 15% | 14/15 | 14/15 | 0 |
| Rich result eligibility (BreadcrumbList, correct types) | 15% | 11/15 | 13/15 | +2 |
| Speakable / GEO readiness | 10% | 2/10 | 8/10 | +6 |
| WebSite + SearchAction | 5% | 0/5 | 3/5 | +3 |
| Supporting pages (privacy-policy, blog index) | 5% | 1/5 | 2/5 | +1 |
| Schema syntax and format hygiene | 5% | 6/5 | 5/5 | — |
| **Total** | | **52/100** | **74/100** | **+22** |

Sprint 1 (commit a3df92f) delivered the bulk of the gain. The 6-point gap to 80 lives in four low-effort fixes: H-1 (SearchAction), H-2 (pillar @id slash), M-1 (clarity-act speakable), M-2 (blog index publisher @id) and M-3 (isAccessibleForFree on 2 articles).

---

## Priority Actions (post-Sprint-1)

| Priority | Finding | Effort | Impact |
|---|---|---|---|
| P1 | H-1 — Add `SearchAction` to existing `WebSite` node (both homepages) | 5 min | Unlocks sitelinks searchbox |
| P2 | H-2 — Fix pillar `Article` `@id` trailing slash | 2 min | Entity URL consistency |
| P3 | H-3 — Remove redundant standalone `Person` block from pillar (or add `@id`) | 5 min | Removes conflicting jobTitle signal |
| P4 | M-1 — Add `speakable` to `clarity-act` FR article | 2 min | Completes speakable across all pages |
| P5 | M-2 — Blog index `publisher` → `{"@id": "...#organization"}` | 5 min | Entity graph closure |
| P6 | M-3 — Add `isAccessibleForFree: true` to fees article and strc article | 2 min | Rich result eligibility hygiene |
| P7 | M-6 — Add minimal `WebPage` schema to `/privacy-policy` | 10 min | Complete site entity graph |
| P8 | M-5 — Extend nav `ItemList` with Resources entry | 5 min | Accuracy |

Total estimated effort for P1–P8: under 40 minutes. Expected score post-fix: **80–82 / 100**.
