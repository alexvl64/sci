# Schema.org / Structured Data Audit — sparkcore.fund
**Date:** 2026-05-08 | **Context:** Regulated crypto AIFM (YMYL financial) | **Format:** JSON-LD

---

## 1. Per-Page Schema Inventory

| Page | Blocks | Types Present | BreadcrumbList | FAQPage |
|---|---|---|---|---|
| `/` (homepage EN) | 3 | Organization, WebPage, FinancialService, ItemList (nav), FAQPage | No | Yes (6 Q) |
| `/fr/` (homepage FR) | 2 | Organization, WebPage, FinancialService, FAQPage | No | Yes (6 Q) |
| `/blog/` | 1 | Blog (with 20 blogPost stubs) | No | No |
| `/fr/blog/` | 1 | Blog (with 5 blogPost stubs) | No | No |
| `/resources/regulated-crypto-fund-estonia/` | 4 | BlogPosting, BreadcrumbList, FAQPage, Person | Yes | Yes |
| `/blog/regulated-crypto-fund-manager-estonia` | 3 | BlogPosting, BreadcrumbList, FAQPage | Yes | Yes |
| `/blog/crypto-fund-fees-2026` | 3 | BlogPosting, BreadcrumbList, FAQPage | Yes | Yes |
| `/fr/blog/strategies-options-...` | 3 | BlogPosting, BreadcrumbList, FAQPage | Yes | Yes |
| `/privacy-policy` | 0 | None | No | No |

---

## 2. Validation Results

All JSON-LD blocks parse as valid JSON. No syntax errors. `@context` is correctly `https://schema.org` across all pages. Dates are `YYYY-MM-DD` format (ISO 8601 date-only — valid but time+timezone recommended for YMYL). Issues below are semantic/completeness failures, not syntax failures.

---

## 3. Findings

| Severity | Page(s) | Issue | Fix |
|---|---|---|---|
| **Critical** | All | `Organization` and `FinancialService` nodes have no `@id`. Without `@id`, Google cannot deduplicate the entity across pages. Cross-page linking of publisher/author to the same entity is broken. | Add `"@id": "https://sparkcore.fund/#organization"` to both nodes on every page that renders them. |
| **Critical** | All blog articles (EN + FR) | `author` Person object is missing `sameAs` and `jobTitle`. For YMYL financial content, Google's quality evaluator guidelines require demonstrable E-E-A-T signals on the author. `url` alone is insufficient. | Add `"sameAs"` (LinkedIn URL) and `"jobTitle"` to the inline author object on every BlogPosting. |
| **Critical** | `/resources/regulated-crypto-fund-estonia/` | `@type: BlogPosting` is incorrect for a long-form pillar / resource guide. Google treats resource guides as `Article` (or `TechArticle`). The pillar has its own `BreadcrumbList` with a "Resources" crumb — confirming it is not a blog post. | Change `@type` to `Article` (or keep `BlogPosting` only if the page is editorially a blog post — currently it is not). |
| **High** | All pages | No `WebSite` schema with `potentialAction: SearchAction` anywhere on the site. This enables sitelinks searchbox in SERPs for navigational queries on a branded YMYL entity. | Add one `WebSite` block to the homepage (see snippet below). |
| **High** | `/` and `/fr/` | `ItemList` (nav) only lists 3 items: Home, Blog, Privacy Policy. The live navigation includes Resources and likely About/Funds pages. Incomplete nav schema gives a partial picture to crawlers. | Enumerate all top-level nav URLs or remove the ItemList if it cannot be kept current. |
| **High** | `blog-en-1`, `blog-en-2`, `blog-fr-1` | `author` inline object is missing `jobTitle` and `sameAs`. Only `name` and `url` present. The standalone `Person` block exists only on the pillar page — it is not referenced from blog articles. | Add `sameAs` + `jobTitle` to the inline author on all BlogPosting blocks (see snippet). Optionally add `@id` to the Person so articles can reference it. |
| **High** | `/blog/` and `/fr/blog/` | `Blog` and its `blogPost` entries have no `@id`. The `publisher` url (`https://sparkcore.fund`) differs from the Organization `url` (`https://sparkcore.fund/`) by a missing trailing slash — these resolve to different canonical URIs for entity matching. | Normalise publisher `url` to `https://sparkcore.fund/` with trailing slash across all pages. |
| **High** | `blog-en-2` | `datePublished: 2026-05-12` is a future date (audit date 2026-05-08). If this is a scheduled-publish article it should not carry today's or a future schema date. `isAccessibleForFree` is also missing on this article and `blog-fr-1`. | Set `datePublished` to the actual publication date. Add `"isAccessibleForFree": true`. |
| **Medium** | All BlogPosting | `image` is a string URL, not an `ImageObject`. Google's Article rich result requires `image` to be an `ImageObject` with `url`, `width`, `height` for full eligibility. | Wrap image URL in `{"@type": "ImageObject", "url": "...", "width": 1200, "height": 630}`. |
| **Medium** | All pages | No `speakable` property on Organization, WebPage, or Article nodes. For an AI-cited YMYL financial entity, `speakable` signals which content is authoritative for voice/LLM citation. | Add `speakable` with `cssSelector` pointing to the hero description and key facts section (see snippet). |
| **Medium** | All pages | No standalone `Person` profiles for co-founders Paul-Antoine PONS and Olivier SAYEGH. Only Alexandre VINAL has a Person block (pillar page only). For a regulated YMYL fund, all named principals should have entity-level schema. | Add three standalone `Person` blocks to the homepage `@graph` or as separate JSON-LD on an About page. |
| **Medium** | `/privacy-policy` | Zero schema. At minimum a `WebPage` with `@type: WebPage` (or `PrivacyPolicy`) and breadcrumb linking back to the Organization. | Add minimal `WebPage` + `BreadcrumbList` (see snippet). |
| **Info** | All pages | `FAQPage` on a commercial financial site. Google restricted FAQPage rich results to government and healthcare sites (August 2023). These blocks will not trigger Google rich results. They remain beneficial for AI/LLM citation (GEO signal). | No change needed if GEO discoverability is the goal. Consider adding a comment in source to document this decision. |
| **Info** | `blog-en-2` | `datePublished` and `dateModified` are identical (`2026-05-12`). For an article published on that date this is fine, but if it was previously published and modified, both dates should differ. | Verify publication vs modification dates on all articles. |

---

## 4. Generated JSON-LD Snippets

### 4a. WebSite with SearchAction (add to homepage `<head>`, standalone block)

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": "https://sparkcore.fund/#website",
  "url": "https://sparkcore.fund/",
  "name": "SparkCore Fund Management",
  "description": "Regulated crypto AIFM based in Estonia, supervised by Finantsinspektsioon.",
  "inLanguage": ["en", "fr"],
  "publisher": {
    "@id": "https://sparkcore.fund/#organization"
  },
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://sparkcore.fund/blog/?s={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  }
}
```

### 4b. Organization with `@id` (replace existing Organization node in `@graph`)

```json
{
  "@type": "Organization",
  "@id": "https://sparkcore.fund/#organization",
  "name": "SparkCore Fund Management",
  "legalName": "SparkCore.investment OÜ",
  "alternateName": ["SparkCore", "SparkCore Asset Management"],
  "url": "https://sparkcore.fund/",
  "logo": {
    "@type": "ImageObject",
    "url": "https://sparkcore.fund/assets/images/png/favicon-192x192.png"
  },
  "leiCode": "8945003BBN0RVNNB0S84",
  "taxID": "16265864",
  "sameAs": [
    "https://www.linkedin.com/company/sparkcorefund/",
    "https://www.youtube.com/@cointips",
    "https://search.gleif.org/#/record/8945003BBN0RVNNB0S84",
    "https://www.fi.ee/en/guides/fund-management-companies/investment-market/small-fund-managers-without-activity-licence/sparkcoreinvestment-ou"
  ],
  "memberOf": {
    "@type": "GovernmentOrganization",
    "name": "Finantsinspektsioon (EFSA)",
    "url": "https://www.fi.ee/"
  },
  "founder": [
    {
      "@type": "Person",
      "@id": "https://sparkcore.fund/#person-pap",
      "name": "Paul-Antoine PONS",
      "jobTitle": "Managing Partner",
      "sameAs": "https://www.linkedin.com/in/paul-antoine-pons-523aa919a/"
    },
    {
      "@type": "Person",
      "@id": "https://sparkcore.fund/#person-os",
      "name": "Olivier SAYEGH",
      "jobTitle": "Managing Partner",
      "sameAs": "https://www.linkedin.com/in/olivier-sayegh-5b89b3135/"
    },
    {
      "@type": "Person",
      "@id": "https://sparkcore.fund/#person-av",
      "name": "Alexandre VINAL",
      "jobTitle": "Managing Partner",
      "sameAs": [
        "https://www.linkedin.com/in/alexandrevinal/",
        "https://www.youtube.com/@cointips"
      ]
    }
  ]
}
```

### 4c. BlogPosting author fix (apply to ALL blog articles)

Replace the current inline `author` object:

```json
"author": {
  "@type": "Person",
  "@id": "https://sparkcore.fund/#person-av",
  "name": "Alexandre VINAL",
  "jobTitle": "Managing Partner & Founder, SparkCore Fund Management",
  "url": "https://www.linkedin.com/in/alexandrevinal/",
  "sameAs": [
    "https://www.linkedin.com/in/alexandrevinal/",
    "https://www.youtube.com/@cointips"
  ]
}
```

Also add to every BlogPosting:
```json
"isAccessibleForFree": true,
"image": {
  "@type": "ImageObject",
  "url": "https://images.unsplash.com/photo-XXXXX?w=1200&h=630&fit=crop&q=80",
  "width": 1200,
  "height": 630
}
```

### 4d. Pillar page — change `@type` from `BlogPosting` to `Article`

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "@id": "https://sparkcore.fund/resources/regulated-crypto-fund-estonia/",
  "headline": "Launching a Regulated Crypto Fund in Estonia: The Complete Guide",
  "articleSection": "Resources",
  "author": {
    "@type": "Person",
    "@id": "https://sparkcore.fund/#person-av",
    "name": "Alexandre VINAL",
    "jobTitle": "Managing Partner & Founder, SparkCore Fund Management",
    "sameAs": ["https://www.linkedin.com/in/alexandrevinal/", "https://www.youtube.com/@cointips"]
  },
  "publisher": {
    "@id": "https://sparkcore.fund/#organization"
  }
}
```

### 4e. `speakable` on homepage WebPage node (add property to existing WebPage node)

```json
"speakable": {
  "@type": "SpeakableSpecification",
  "cssSelector": [".hero-description", ".about-intro", ".regulated-summary"]
}
```

Adjust `cssSelector` values to match actual class names on the live page.

### 4f. Privacy Policy minimal schema

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "@id": "https://sparkcore.fund/privacy-policy",
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

## 5. Schema Sub-Score

**Score: 52 / 100**

Strong foundations: all JSON is syntactically valid, YMYL-critical fields `leiCode`, `taxID`, `sameAs`, `memberOf`, `areaServed`, and `address` are present on Organization/FinancialService; BreadcrumbList exists on all article pages; FAQPage is present and answers match visible content. Deductions: missing `@id` on all Organization/FinancialService/BlogPosting nodes breaks cross-page entity disambiguation (the single most impactful YMYL trust signal for Google); `author` Person objects lack `sameAs` and `jobTitle` on all 20+ blog articles; no `WebSite` schema; the pillar resource page carries a `BlogPosting` type when it is editorially an `Article`; `image` is a string not an `ImageObject` on all articles; `isAccessibleForFree` missing on 2 of 4 audited articles; publisher URL trailing-slash inconsistency across Blog vs Organization nodes.

---

## 6. Top 3 Priority Actions

**P1 — Add `@id` to Organization, FinancialService, and Person nodes (Critical, 1-2h)**
Every page re-renders the Organization node without an `@id`. Google cannot merge these into a single Knowledge Graph entity. Add `"@id": "https://sparkcore.fund/#organization"` to Organization and `"@id": "https://sparkcore.fund/#financialservice"` to FinancialService in the site template. Add `@id` anchors to the three founder Person objects (4d above). This is the highest-leverage YMYL trust fix available.

**P2 — Fix author Person on all BlogPosting blocks: add `sameAs` + `jobTitle` (Critical, 30min template change)**
All 20+ blog articles (EN and FR) carry an author object with only `name` and `url`. For a regulated financial YMYL site, Google's quality rater guidelines weight demonstrable author expertise heavily. The standalone `Person` block on the pillar page is correct — replicate that pattern as the inline author object across all BlogPosting pages (snippet 4c). This is a template-level change, not a per-article edit.

**P3 — Add `WebSite` block with `SearchAction` to homepage, and convert pillar `@type` from `BlogPosting` to `Article` (High, 30min)**
The `WebSite` + `SearchAction` block enables sitelinks searchbox for branded queries at no cost (snippet 4a). The pillar type mismatch (`BlogPosting` vs `Article`) matters because the BreadcrumbList already labels it under "Resources" — the schema type contradicts the editorial classification, which can confuse Google's content type classifiers for a YMYL page.
