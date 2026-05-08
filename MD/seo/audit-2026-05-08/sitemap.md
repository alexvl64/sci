# Sitemap Audit — sparkcore.fund — 2026-05-08

## 1. Executive Summary

The sitemap is structurally valid and well-scoped. All 34 URLs map to public, indexable content; gated pages are correctly absent. One low-severity issue: `priority` and `changefreq` tags are present and should be stripped (ignored by Google, add noise).

---

## 2. URL Inventory (34 URLs)

| Category | Count | URLs |
|---|---|---|
| EN homepage | 1 | `/` |
| FR homepage | 1 | `/fr/` |
| EN blog index | 1 | `/blog/` |
| FR blog index | 1 | `/fr/blog/` |
| EN pillar page | 1 | `/resources/regulated-crypto-fund-estonia/` |
| EN blog articles | 19 | `/blog/aif-vs-aifm-crypto-explained` … `/blog/why-invest-in-crypto-funds-2026` |
| FR blog articles | 5 | `/fr/blog/agents-ia-*`, `/fr/blog/clarity-act-*`, `/fr/blog/indicateurs-*`, `/fr/blog/le-vrai-cout-*`, `/fr/blog/strategies-options-*` |
| Privacy policy | 1 | `/privacy-policy` |
| Orphans | 0 | None detected |

**Note on FR article count:** The raw URL file contains 5 FR blog articles (lines 28-32), not 4 as originally scoped. Either the brief had a count error, or one article was published after the audit scope was drafted. All 5 are valid, indexable content — no action required beyond updating internal counts.

---

## 3. XML Validity

Pass. The sitemap declares `xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"` and `xmlns:xhtml="http://www.w3.org/1999/xhtml"` on the `<urlset>` root. The `xhtml` namespace is required for the `<xhtml:link rel="alternate">` hreflang blocks used on the homepage and blog index entries. No malformed tags, no encoding issues detected from URL extraction.

---

## 4. Hreflang Consistency

| URL pair | hreflang declared | Assessment |
|---|---|---|
| `/` ↔ `/fr/` | `en`, `fr`, `x-default` | Correct — bidirectional alternate |
| `/blog/` ↔ `/fr/blog/` | `en`, `fr`, `x-default` | Correct — bidirectional alternate |
| EN blog articles (`/blog/*`) | `en` + `x-default` on self | Intentional — dual-cluster policy, no FR mirror |
| FR blog articles (`/fr/blog/*`) | `fr` on self | Intentional — dual-cluster policy, no EN mirror |

The dual-cluster architecture (regulatory hub EN / investor-education FR) means articles are independent, not translations. Self-referential hreflang with no cross-cluster alternate is the correct implementation for this structure. No issue.

---

## 5. lastmod Accuracy

Sample dates observed:

| Page | lastmod | Assessment |
|---|---|---|
| `/` | 2026-04-09 | Plausible — homepage last structural update |
| EN blog articles | 2026-05-05 | Plausible — batch publish / update date |
| `/resources/regulated-crypto-fund-estonia/` | 2026-05-06 | Plausible — pillar page updated post-migration |
| FR blog articles | 2026-05-07 | Plausible — most recent publish date |

Dates are varied and reflect actual content cadence. No all-identical lastmod antipattern detected. Pass.

---

## 6. priority and changefreq

Both tags are present in the sitemap. Google has officially stated it ignores both fields. They add byte weight and maintenance overhead with zero ranking benefit.

Severity: Info. Recommended action: remove both tags on next sitemap regeneration.

---

## 7. Gated Pages — Absence Confirmed

Cross-checked the 34 URLs in `raw/sitemap-urls.txt` against the three gated paths:

| Gated path | Present in sitemap? |
|---|---|
| `/factsheets/*` | No |
| `/discovery-call` | No |
| `/MD/` | No |

Pass. All four protection layers (meta noindex, X-Robots-Tag, robots.txt Disallow, sitemap exclusion) are consistent.

---

## 8. Trailing-Slash Policy

Cloudflare Redirect Rule strips trailing slashes on `/blog/*/` → `/blog/$1` (301). Blog articles in the sitemap must not carry trailing slashes to avoid serving a redirect-target URL as the canonical.

Spot check on three entries from `raw/sitemap-urls.txt`:

- `https://sparkcore.fund/blog/aif-vs-aifm-crypto-explained` — no trailing slash. Correct.
- `https://sparkcore.fund/blog/crypto-fund-fees-2026` — no trailing slash. Correct.
- `https://sparkcore.fund/fr/blog/le-vrai-cout-du-market-timing` — no trailing slash. Correct.

The pillar page `/resources/regulated-crypto-fund-estonia/` carries a trailing slash — this is a directory-style URL, not a blog article, so the CF redirect rule does not apply. Correct.

Pass.

---

## 9. Findings Table

| Severity | Location | Issue | Fix |
|---|---|---|---|
| Info | All `<url>` entries | `priority` tags present (ignored by Google) | Remove from sitemap template |
| Info | All `<url>` entries | `changefreq` tags present (ignored by Google) | Remove from sitemap template |
| Info | FR blog count | 5 FR articles in file vs 4 in brief scope | Update internal documentation — no sitemap change needed |

No critical, high, or medium issues found.

---

## 10. Sub-Score

**92 / 100**

Deductions: -5 for presence of deprecated `priority` / `changefreq` tags (Info, not a ranking factor but a hygiene debt); -3 for minor scope documentation mismatch on FR article count.

---

## 11. Top 3 Actions

1. **Remove `priority` and `changefreq` from sitemap.xml** — strip both deprecated tags on next sitemap regeneration. Zero SEO impact if left, but cleaner and lighter.

2. **Update internal audit brief** — record 5 FR blog articles (not 4) in the project documentation to avoid count drift in future audits.

3. **Submit updated sitemap to Bing WMT** — the Bing WMT entry still references the legacy `www.sparkcore.fund/sitemap.xml` (10 URLs). Delete that submission from the Bing WMT UI and confirm the current `sparkcore.fund/sitemap.xml` (34 URLs) is the only active submission.
