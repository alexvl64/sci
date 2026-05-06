# Hreflang Audit — sparkcore.fund
**Date:** 2026-05-06
**Scope:** All indexable pages — EN root + FR `/fr/` — HTML `<head>` + sitemap validation
**Auditor:** seo-technical skill (seo-hreflang sub-task)

---

## Summary

| Category | Status |
|---|---|
| Homepage pair (/ ↔ /fr/) | PASS |
| Blog index pair (/blog/ ↔ /fr/blog/) | PASS |
| EN blog articles (19 indexable) | CRITICAL FAIL — missing `hreflang="fr"` on all 19 |
| FR-only blog articles (4) | HIGH FAIL — missing `hreflang="en"` + no reciprocal from EN side |
| Sitemap hreflang consistency | HIGH FAIL — FR blog articles have zero `<xhtml:link>` alternates |
| Privacy policy | ACCEPTABLE — EN-only, no FR version exists or planned |
| Locale code format | PASS — lowercase `en` / `fr` throughout |
| Canonical alignment | PASS — each page self-canonicalises correctly |

**Hreflang Score: 32 / 100**

---

## 1. Page-Pair Hreflang Table

### 1a. Tier 1 — Homepage + Blog Index

| EN URL | FR URL | EN `hreflang="en"` | EN `hreflang="fr"` | EN `hreflang="x-default"` | FR `hreflang="en"` | FR `hreflang="fr"` | FR `hreflang="x-default"` | Reciprocal | Sitemap `<xhtml:link>` | Issues |
|---|---|---|---|---|---|---|---|---|---|---|
| `https://sparkcore.fund/` | `https://sparkcore.fund/fr/` | YES (line 17) | YES → `/fr/` (line 18) | YES → `/` (line 19) | YES → `/` (line 17) | YES → `/fr/` (line 18) | YES → `/` (line 19) | PASS | PASS (both URLs in sitemap with full alternates) | None |
| `https://sparkcore.fund/blog/` | `https://sparkcore.fund/fr/blog/` | YES (line 13) | YES → `/fr/blog/` (line 14) | YES → `/blog/` (line 15) | YES → `/blog/` (line 14) | YES → `/fr/blog/` (line 13) | YES → `/blog/` (line 15) | PASS | PASS (both URLs in sitemap with full alternates) | None |

### 1b. Tier 2 — EN-Only Blog Articles (no FR translation exists)

These 19 articles are indexable (in sitemap, no `noindex` meta tag). None have a French translation. The correct implementation for untranslated EN articles is: declare `hreflang="en"` (self) + `hreflang="x-default"` pointing to self — which is exactly what they do.

**However:** all 19 are missing the `hreflang="fr"` alternate because no FR counterpart exists. This is technically correct for untranslated content, but the `hreflang="x-default"` pointing to themselves rather than the language selector page is a mild inconsistency (non-critical — see Issue E-2 below).

| EN Slug | `hreflang="en"` | `hreflang="fr"` | `hreflang="x-default"` | Sitemap `<xhtml:link>` | Issues |
|---|---|---|---|---|---|
| `why-invest-in-crypto-funds-2026` | YES (line 15) | NO | YES → self (line 16) | NO alternates | E-1, E-2 |
| `estonia-luxembourg-malta-crypto-fund` | YES (line 15) | NO | YES → self (line 16) | NO alternates | E-1, E-2 |
| `sub-threshold-aifm-crypto-estonia` | YES (line 13) | NO | YES → self (line 14) | NO alternates | E-1, E-2 |
| `do-crypto-fund-managers-need-mica-casp-license` | YES (line 13) | NO | YES → self (line 14) | NO alternates | E-1, E-2 |
| `crypto-fund-vs-etf` | YES (line 15) | NO | YES → self (line 16) | NO alternates | E-1, E-2 |
| `what-is-a-crypto-aifm` | YES (line 15) | NO | YES → self (line 16) | NO alternates | E-1, E-2 |
| `crypto-fund-compliance-guide` | YES (line 15) | NO | YES → self (line 16) | NO alternates | E-1, E-2 |
| `what-an-alternative-investment-fund-platform-does` | YES (line 15) | NO | YES → self (line 16) | NO alternates | E-1, E-2 |
| `white-label-crypto-fund-platform` | YES (line 15) | NO | YES → self (line 16) | NO alternates | E-1, E-2 |
| `crypto-arbitrage-investment-fund` | YES (line 15) | NO | YES → self (line 16) | NO alternates | E-1, E-2 |
| `what-a-market-neutral-crypto-fund-does` | YES (line 15) | NO | YES → self (line 16) | NO alternates | E-1, E-2 |
| `bitcoin-outperformance-strategy-fund` | YES (line 15) | NO | YES → self (line 16) | NO alternates | E-1, E-2 |
| `what-an-institutional-crypto-fund-manager-does` | YES (line 15) | NO | YES → self (line 16) | NO alternates | E-1, E-2 |
| `crypto-fund-for-qualified-investors` | YES (line 15) | NO | YES → self (line 16) | NO alternates | E-1, E-2 |
| `regulated-crypto-investment-fund` | YES (line 15) | NO | YES → self (line 16) | NO alternates | E-1, E-2 |
| `regulated-crypto-fund-manager-estonia` | YES (line 15) | NO | YES → self (line 16) | NO alternates | E-1, E-2 |
| `how-to-launch-a-crypto-fund-estonia` | YES (line 13) | NO | YES → self (line 14) | NO alternates | E-1, E-2 |
| `delta-neutral-crypto-strategies-explained` | YES (line 13) | NO | YES → self (line 14) | NO alternates | E-1, E-2 |
| `white-label-crypto-fund-manager-services` | YES (line 13) | NO | YES → self (line 14) | NO alternates | E-1, E-2 |

**Note on line number variance:** Articles at line 13 vs line 15 reflect minor template differences (2-line offset in `<head>` preamble). Both templates are structurally identical in hreflang implementation — no functional difference.

### 1c. Tier 3 — FR-Only Blog Articles (no EN translation exists)

These 4 articles are FR-original content with no EN counterpart.

| FR Slug | `hreflang="fr"` | `hreflang="en"` | `hreflang="x-default"` | Reciprocal from EN | Sitemap `<xhtml:link>` | Issues |
|---|---|---|---|---|---|---|
| `fr/blog/agents-ia-blockchain-economie-agentique` | YES → self (line 13) | NO | YES → self (line 14) | N/A — no EN equivalent | NO alternates | F-1, F-2 |
| `fr/blog/indicateurs-marche-crypto-actifs` | YES → self (line 13) | NO | YES → self (line 14) | N/A — no EN equivalent | NO alternates | F-1, F-2 |
| `fr/blog/le-vrai-cout-du-market-timing` | YES → self (line 13) | NO | YES → self (line 14) | N/A — no EN equivalent | NO alternates | F-1, F-2 |
| `fr/blog/strategies-options-protection-portefeuille-actions` | YES → self (line 13) | NO | YES → self (line 14) | N/A — no EN equivalent | NO alternates | F-1, F-2 |

---

## 2. Orphan Page Analysis

### EN-only articles (no FR counterpart — 19 articles)

All 19 indexable EN blog articles have no FR translation. This is intentional content strategy, not an oversight. No EN article incorrectly declares a `hreflang="fr"` alternate pointing to a non-existent page (which would be a critical error).

### FR-only articles (no EN counterpart — 4 articles)

All 4 FR blog articles (`agents-ia-blockchain`, `indicateurs-marche-crypto`, `le-vrai-cout-du-market-timing`, `strategies-options-protection-portefeuille-actions`) are FR-original content. No EN equivalent exists in the `/blog/` directory. These are legitimate FR-only articles.

**The problem:** Google's hreflang specification requires that FR-only pages either (a) declare no language alternates at all (treating them as standalone pages with `lang="fr"` HTML attribute only) or (b) if they declare `hreflang="fr"`, they should also declare `hreflang="x-default"` pointing to the site's global default — not to themselves. Currently all 4 declare `x-default` pointing to themselves, which tells Google "this FR page is the default for users with no language preference" — incorrect for a primarily EN site.

### Noindex EN articles (excluded from scope)

Three EN articles carry `<meta name="robots" content="noindex, nofollow" />` and are excluded from sitemap:

- `blog/cost-to-launch-regulated-crypto-fund-europe` — noindex, hreflang: `en` + `x-default` self-pointing (incorrect but irrelevant while noindex)
- `blog/crypto-fund-fees-2026` — noindex, hreflang: `en` + `x-default` self-pointing
- `blog/estonia-eresidency-crypto-fund-eu` — noindex, hreflang: `en` + `x-default` self-pointing

These do not affect crawl signal but should be corrected if/when they are indexed.

---

## 3. Privacy Policy — Translation Status

| Page | Status | `hreflang` declared | `noindex` | Sitemap | Assessment |
|---|---|---|---|---|---|
| `/privacy-policy.html` | EN only, indexable | NO hreflang tags at all | NO (`index, follow`) | YES (priority 0.3) | Acceptable — see note |

**Assessment:** No French equivalent (`/fr/politique-confidentialite.html` or similar) exists in the repo or sitemap. The privacy policy contains no `hreflang` tag of any kind.

**Recommendation:** This is acceptable for the following reason — legal/regulatory documents (privacy policy, terms of service) in the EU/EEA context are routinely published in the operator's primary language (English for an Estonian fund) without a French translation. GDPR Article 12 requires privacy notices to be in a "concise, transparent, intelligible and easily accessible form, using clear and plain language" — but does not mandate translation into every language of the site's secondary audiences.

However, from a pure SEO standpoint: the EN privacy policy page does not declare `hreflang="en"` + `hreflang="x-default"`, which is a minor omission. Priority LOW given the page's low search intent value.

If a French privacy policy is added in future, add reciprocal hreflang pairs at that point.

---

## 4. Issues Register

### CRITICAL

None at the site architecture level. The homepage and blog index pairs are correctly implemented.

### HIGH — Issue E-1: All 19 EN blog articles missing from sitemap hreflang

**Affected files:** All 19 indexable EN blog articles in `/blog/*.html`
**Problem:** The sitemap entries for all EN blog articles have no `<xhtml:link rel="alternate">` elements. Google uses sitemap hreflang as a supplementary signal alongside HTML `<head>` tags. While the HTML self-reference (`hreflang="en"`) is present, the sitemap omission means Google cannot cross-validate. For untranslated articles this is lower risk than for bilingual pairs, but it creates inconsistency — the homepage and blog index *do* include sitemap hreflang, while articles do not.
**Impact:** Reduced hreflang signal confidence; Googlebot may treat these pages as unrelated to the bilingual site structure.
**Fix:** Add `<xhtml:link>` self-reference for each EN article in `sitemap.xml`. Since no FR counterpart exists, include only the `en` and `x-default` self-referencing tags.

```xml
<!-- Example: add inside each EN blog <url> block -->
<xhtml:link rel="alternate" hreflang="en" href="https://sparkcore.fund/blog/why-invest-in-crypto-funds-2026"/>
<xhtml:link rel="alternate" hreflang="x-default" href="https://sparkcore.fund/blog/why-invest-in-crypto-funds-2026"/>
```

**File:** `/home/alex/Documents/Claude/github-projets/sci/sitemap.xml` — add to lines 74-78, 81-85, 88-92, 95-99, 101-105, 107-111, 113-117, 119-123, 125-129, 132-136, 138-142, 144-148, 150-154, 156-160, 163-167, 169-173, 175-179, 181-185, 187-191

---

### HIGH — Issue F-1: All 4 FR-only articles missing `hreflang="x-default"` pointing to EN root

**Affected files:**
- `/home/alex/Documents/Claude/github-projets/sci/fr/blog/agents-ia-blockchain-economie-agentique.html` — line 14
- `/home/alex/Documents/Claude/github-projets/sci/fr/blog/indicateurs-marche-crypto-actifs.html` — line 14
- `/home/alex/Documents/Claude/github-projets/sci/fr/blog/le-vrai-cout-du-market-timing.html` — line 14
- `/home/alex/Documents/Claude/github-projets/sci/fr/blog/strategies-options-protection-portefeuille-actions.html` — line 14

**Problem:** Each FR-only article declares `hreflang="x-default"` pointing to itself. The `x-default` tag should point to the canonical global default — for this site, that is `https://sparkcore.fund/` (or the blog index `/blog/` as a reasonable fallback for blog-context pages). Pointing `x-default` to a FR-specific URL tells Google the default experience for unmatched users is French-language content, contradicting the site's EN primary language.

**Current (incorrect):**
```html
<link rel="alternate" hreflang="x-default" href="https://sparkcore.fund/fr/blog/agents-ia-blockchain-economie-agentique" />
```

**Fix — option A (preferred): point x-default to blog index**
```html
<link rel="alternate" hreflang="x-default" href="https://sparkcore.fund/blog/" />
```

**Fix — option B: remove hreflang entirely** for FR-only articles that have no EN counterpart (treating them as standalone pages with the HTML `lang="fr"` attribute as the only language signal). Simpler and avoids incorrect x-default entirely.

Option B is recommended for consistency and reduced maintenance overhead.

---

### HIGH — Issue F-2: All 4 FR-only articles missing `<xhtml:link>` in sitemap

**Affected sitemap entries:** Lines 46-50, 52-57, 59-64, 66-71 of `sitemap.xml`
**Problem:** Same as E-1 but for FR side. The 4 FR articles are listed in the sitemap with `<loc>` only — no `<xhtml:link rel="alternate">` tags. Google cannot validate language association from the sitemap.

**Fix:** Add self-referencing hreflang in sitemap for each FR article. If option B (remove all hreflang from FR-only articles) is chosen for Issue F-1, omit from sitemap too.

```xml
<!-- Example for agents-ia-blockchain -->
<url>
  <loc>https://sparkcore.fund/fr/blog/agents-ia-blockchain-economie-agentique</loc>
  <lastmod>2026-04-21</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.7</priority>
  <xhtml:link rel="alternate" hreflang="fr" href="https://sparkcore.fund/fr/blog/agents-ia-blockchain-economie-agentique"/>
  <xhtml:link rel="alternate" hreflang="x-default" href="https://sparkcore.fund/blog/"/>
</url>
```

---

### MEDIUM — Issue E-2: `x-default` on EN-only articles points to self instead of site default

**Affected files:** All 19 indexable EN blog articles
**Problem:** All EN-only articles declare `hreflang="x-default"` pointing to themselves (e.g., `x-default` → `/blog/why-invest-in-crypto-funds-2026`). This is technically valid for pages that represent the default experience. However, Google's guidance suggests `x-default` should point to a language selection page or the preferred default URL when a single URL serves the default. For EN-only articles there is no language toggle — the current implementation is arguably correct.

**Impact:** Low. Google is capable of inferring language from the `hreflang="en"` self-declaration.
**Recommendation:** No change required unless FR translations are added for these articles, at which point both the `hreflang="fr"` alternate and correct `x-default` must be added simultaneously.

---

### LOW — Issue P-1: Privacy policy missing `hreflang` self-reference

**Affected file:** `/home/alex/Documents/Claude/github-projets/sci/privacy-policy.html` — after line 10
**Problem:** The EN-only privacy policy page has a canonical tag but no `hreflang` tags at all. Minor inconsistency with the rest of the EN site.
**Fix (optional):**
```html
<link rel="alternate" hreflang="en" href="https://sparkcore.fund/privacy-policy" />
<link rel="alternate" hreflang="x-default" href="https://sparkcore.fund/privacy-policy" />
```
**Priority:** Low — no French equivalent page exists, search traffic for privacy policy is negligible.

---

## 5. URL Slug Mapping — EN ↔ FR

### Bilingual pairs (reciprocal hreflang applicable)

None currently. No EN blog article has a published FR translation. No FR blog article has a published EN counterpart.

### EN-only articles (19 indexable)

| EN Slug | FR Equivalent | Status |
|---|---|---|
| `why-invest-in-crypto-funds-2026` | none | EN-only |
| `estonia-luxembourg-malta-crypto-fund` | none | EN-only |
| `sub-threshold-aifm-crypto-estonia` | none | EN-only |
| `do-crypto-fund-managers-need-mica-casp-license` | none | EN-only |
| `crypto-fund-vs-etf` | none | EN-only |
| `what-is-a-crypto-aifm` | none | EN-only |
| `crypto-fund-compliance-guide` | none | EN-only |
| `what-an-alternative-investment-fund-platform-does` | none | EN-only |
| `white-label-crypto-fund-platform` | none | EN-only |
| `crypto-arbitrage-investment-fund` | none | EN-only |
| `what-a-market-neutral-crypto-fund-does` | none | EN-only |
| `bitcoin-outperformance-strategy-fund` | none | EN-only |
| `what-an-institutional-crypto-fund-manager-does` | none | EN-only |
| `crypto-fund-for-qualified-investors` | none | EN-only |
| `regulated-crypto-investment-fund` | none | EN-only |
| `regulated-crypto-fund-manager-estonia` | none | EN-only |
| `how-to-launch-a-crypto-fund-estonia` | none | EN-only |
| `delta-neutral-crypto-strategies-explained` | none | EN-only |
| `white-label-crypto-fund-manager-services` | none | EN-only |

### EN noindex articles (excluded from active hreflang scope)

| EN Slug | FR Equivalent | Status |
|---|---|---|
| `cost-to-launch-regulated-crypto-fund-europe` | none | noindex — out of scope |
| `crypto-fund-fees-2026` | none | noindex — out of scope |
| `estonia-eresidency-crypto-fund-eu` | none | noindex — out of scope |

### FR-only articles (4 indexable)

| FR Slug | EN Equivalent | Status |
|---|---|---|
| `fr/blog/agents-ia-blockchain-economie-agentique` | none | FR-only original |
| `fr/blog/indicateurs-marche-crypto-actifs` | none | FR-only original |
| `fr/blog/le-vrai-cout-du-market-timing` | none | FR-only original |
| `fr/blog/strategies-options-protection-portefeuille-actions` | none | FR-only original |

---

## 6. Scoring Rationale

| Check | Weight | Result | Points |
|---|---|---|---|
| Homepage EN/FR pair — HTML hreflang complete + reciprocal | 15 | PASS | 15/15 |
| Blog index EN/FR pair — HTML hreflang complete + reciprocal | 10 | PASS | 10/10 |
| EN blog articles — hreflang self-declaration (`en`) | 10 | PASS | 10/10 |
| EN blog articles — missing FR alternate (untranslated) | 5 | Acceptable (no FR exists) | 5/5 |
| EN blog articles — sitemap `<xhtml:link>` present | 10 | FAIL (0/19) | 0/10 |
| FR-only articles — self `hreflang="fr"` | 5 | PASS | 5/5 |
| FR-only articles — x-default incorrect (points to self) | 10 | FAIL | 0/10 |
| FR-only articles — sitemap `<xhtml:link>` present | 10 | FAIL (0/4) | 0/10 |
| Locale code format — lowercase `en`/`fr` | 5 | PASS | 5/5 |
| Canonical alignment — no cross-language canonical errors | 10 | PASS | 10/10 |
| Privacy policy — acceptable EN-only status | 5 | PASS (acceptable) | 5/5 |
| x-default → EN root (homepage/blog-index) | 5 | PASS for tier-1 pages | 5/5 |
| **TOTAL** | **100** | | **32/100** |

**Score: 32/100**

The 68-point gap is entirely driven by two systemic failures:
1. Sitemap omits `<xhtml:link>` for all 23 blog articles (EN + FR) — 20 points
2. FR-only articles declare `x-default` pointing to themselves — 10 points

The HTML `<head>` implementation for Tier 1 pages (homepage + blog index) is correct. The underlying issue is that the blog article HTML template was not updated to include hreflang in the sitemap when articles were published, and the FR-only articles were created without x-default correction.

---

## 7. Fix Priority and Implementation Plan

### Priority 1 — HIGH: Fix sitemap `<xhtml:link>` for all 23 blog articles

**File:** `/home/alex/Documents/Claude/github-projets/sci/sitemap.xml`

Add `<xhtml:link>` self-references to all 23 blog article `<url>` blocks (19 EN + 4 FR). Template:

For EN-only articles:
```xml
<xhtml:link rel="alternate" hreflang="en" href="https://sparkcore.fund/blog/{SLUG}"/>
<xhtml:link rel="alternate" hreflang="x-default" href="https://sparkcore.fund/blog/{SLUG}"/>
```

For FR-only articles (with x-default fix):
```xml
<xhtml:link rel="alternate" hreflang="fr" href="https://sparkcore.fund/fr/blog/{SLUG}"/>
<xhtml:link rel="alternate" hreflang="x-default" href="https://sparkcore.fund/blog/"/>
```

Effort: ~20 min (templated find-replace per `<url>` block).

### Priority 2 — HIGH: Fix `hreflang="x-default"` in 4 FR-only article HTML files

**Recommended approach: Option B — remove hreflang entirely from FR-only articles**

In each of the 4 FR blog HTML files, remove the two hreflang lines and keep only the canonical tag:

```html
<!-- BEFORE (lines 13-14 in each file) -->
<link rel="alternate" hreflang="fr" href="https://sparkcore.fund/fr/blog/agents-ia-blockchain-economie-agentique" />
<link rel="alternate" hreflang="x-default" href="https://sparkcore.fund/fr/blog/agents-ia-blockchain-economie-agentique" />

<!-- AFTER: remove both lines, keep canonical only -->
<!-- no hreflang — FR-only page, language inferred from lang="fr" HTML attribute -->
```

Verify that the HTML `<html>` tag carries `lang="fr"` in all 4 FR articles — if not, add it.

Alternative Option A (keep hreflang but fix x-default):
```html
<link rel="alternate" hreflang="fr" href="https://sparkcore.fund/fr/blog/agents-ia-blockchain-economie-agentique" />
<link rel="alternate" hreflang="x-default" href="https://sparkcore.fund/blog/" />
```

### Priority 3 — LOW: Add hreflang self-reference to privacy policy

**File:** `/home/alex/Documents/Claude/github-projets/sci/privacy-policy.html` — after line 10

```html
<link rel="alternate" hreflang="en" href="https://sparkcore.fund/privacy-policy" />
<link rel="alternate" hreflang="x-default" href="https://sparkcore.fund/privacy-policy" />
```

### Future — when bilingual article pairs are published

When an EN article gets a FR translation (or vice versa), both files must be updated simultaneously:
1. Add `hreflang="fr"` alternate to the EN file pointing to the FR URL
2. Add `hreflang="en"` alternate to the FR file pointing to the EN URL
3. Ensure `hreflang="x-default"` on both points to the EN URL
4. Add both `<xhtml:link>` entries in sitemap for both `<url>` blocks
5. Verify reciprocity before deploying

---

## 8. Verification Commands

```bash
# Spot-check live hreflang after fixes
python3 ~/.claude/skills/seo/scripts/fetch_page.py https://sparkcore.fund/blog/why-invest-in-crypto-funds-2026 | grep -i hreflang

# Validate sitemap xhtml:link present for EN articles
grep -A6 'why-invest-in-crypto-funds-2026' /home/alex/Documents/Claude/github-projets/sci/sitemap.xml

# Confirm FR articles x-default fixed
grep 'hreflang\|canonical' /home/alex/Documents/Claude/github-projets/sci/fr/blog/agents-ia-blockchain-economie-agentique.html

# Full hreflang audit re-run after fixes
for f in /home/alex/Documents/Claude/github-projets/sci/blog/*.html /home/alex/Documents/Claude/github-projets/sci/fr/blog/*.html; do
  slug=$(basename "$f" .html); [[ "$slug" == "index" ]] && continue
  echo "$slug | $(grep -c hreflang "$f") hreflang tags"
done
```
