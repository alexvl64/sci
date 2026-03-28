#!/usr/bin/env python3
"""Build blog/white-label-aifm-complete-guide-2026.html from the markdown source."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / "white-label-aifm-complete-guide-2026.md"
OUT = ROOT / "blog" / "white-label-aifm-complete-guide-2026.html"

INTERNAL = {
    '[INTERNAL-LINK: "EU AIF regulation overview" -> pillar article on AIFMD compliance basics]':
        '<a href="/blog/crypto-fund-compliance-guide" class="text-darkGray underline underline-offset-2 hover:text-steelBlue transition-colors duration-200">EU AIF regulation and AIFMD compliance basics</a>',
    '[INTERNAL-LINK: "AIFMD sub-threshold exemption explained" -> supporting article on de minimis registration]':
        '<a href="/blog/crypto-fund-compliance-guide" class="text-darkGray underline underline-offset-2 hover:text-steelBlue transition-colors duration-200">AIFMD sub-threshold and de minimis registration</a>',
    '[INTERNAL-LINK: "NPPR vs EU passport: which route is right for you?" -> supporting comparison article]':
        '<a href="/blog/crypto-fund-for-qualified-investors" class="text-darkGray underline underline-offset-2 hover:text-steelBlue transition-colors duration-200">NPPR vs EU passport for qualified investors</a>',
    '[INTERNAL-LINK: "How to set up a Luxembourg AIFM: timeline and costs" -> supporting article on in-house AIFM setup]':
        '<a href="/blog/how-to-launch-a-crypto-fund-estonia" class="text-darkGray underline underline-offset-2 hover:text-steelBlue transition-colors duration-200">Launching a regulated fund: timelines and jurisdiction choices</a>',
    '[INTERNAL-LINK: "ELTIF 2.0: what fund managers need to know" -> supporting article on ELTIF distribution]':
        '<a href="/blog/white-label-crypto-fund-platform" class="text-darkGray underline underline-offset-2 hover:text-steelBlue transition-colors duration-200">White-label fund platforms and distribution channels</a>',
    '[INTERNAL-LINK: "AIFMD Annex IV reporting guide" -> supporting article on regulatory reporting obligations]':
        '<a href="/blog/crypto-fund-compliance-guide" class="text-darkGray underline underline-offset-2 hover:text-steelBlue transition-colors duration-200">Regulatory reporting and fund compliance</a>',
    '[INTERNAL-LINK: "AIFMD II delegation rules: what every fund manager must know" -> supporting article on delegation under AIFMD II]':
        '<a href="/blog/crypto-fund-compliance-guide" class="text-darkGray underline underline-offset-2 hover:text-steelBlue transition-colors duration-200">AIFMD delegation and compliance for fund managers</a>',
    '[INTERNAL-LINK: "AIFM letterbox entity risk: a practical guide" -> supporting article on Article 82 compliance]':
        '<a href="/blog/crypto-fund-compliance-guide" class="text-darkGray underline underline-offset-2 hover:text-steelBlue transition-colors duration-200">AIFM substance and delegation risk</a>',
    '[INTERNAL-LINK: "Luxembourg vs Ireland for your AIF: a 2026 comparison" -> supporting comparison article]':
        '<a href="/blog/white-label-crypto-fund-platform" class="text-darkGray underline underline-offset-2 hover:text-steelBlue transition-colors duration-200">White-label fund platform and domicile considerations</a>',
    '[INTERNAL-LINK: "How U.S. fund managers can access EU investors in 2026" -> supporting guide for non-EU managers]':
        '<a href="/blog/regulated-crypto-investment-fund" class="text-darkGray underline underline-offset-2 hover:text-steelBlue transition-colors duration-200">Regulated fund access for institutional investors</a>',
    '[INTERNAL-LINK: "Luxembourg AIFM setup guide: CSSF application step by step" -> supporting operational article]':
        '<a href="/blog/how-to-launch-a-crypto-fund-estonia" class="text-darkGray underline underline-offset-2 hover:text-steelBlue transition-colors duration-200">How to launch a regulated fund: operational steps</a>',
    '[INTERNAL-LINK: "Book a fund structuring consultation" -> contact or consultation page]':
        '<a href="/" class="text-darkGray underline underline-offset-2 hover:text-steelBlue transition-colors duration-200">Contact SparkCore</a> for a fund structuring conversation',
}

BOOK_CONSULT = '[INTERNAL-LINK: "Book a fund structuring consultation" -> contact or consultation page]'

FAQ = [
    (
        "What is a white label AIFM and how does it differ from setting up your own AIFM?",
        "A white label AIFM is a pre-authorized management company that takes on regulatory accountability for your fund under AIFMD, while you retain investment decision-making via delegation. Setting up your own AIFM takes 12 to 24 months and costs €1.5 million+ per year (Aztec Group, 2024). A white label appointment takes two to four weeks at a fraction of the cost.",
    ),
    (
        "How much does a white label AIFM cost in 2025-2026?",
        "Annual fees for a white label or outsourced AIFM start at approximately USD 50,000 (around €45,000) and scale with AUM and service scope (ICLG Luxembourg, 2025). Additional costs include depositary fees, fund administration, and NCA notification filing fees. Total annual costs for a smaller fund commonly range from €80,000 to €200,000 depending on complexity and jurisdiction.",
    ),
    (
        "Can a U.S.-based fund manager use a white label AIFM?",
        "Yes. U.S. managers are among the most active users of white label AIFM structures. The AIFM acts as the EU-regulated entity, allowing a U.S. investment adviser to distribute to professional investors across all 30 EEA Member States without establishing its own EU presence. 60% of U.S. managers surveyed already use this route (Carne Atlas, 2024).",
    ),
    (
        "What is the letterbox entity rule and how does it affect white label AIFMs?",
        "The letterbox entity rule (Article 82) prevents an AIFM from delegating so much of its function that it becomes a shell. Four triggers apply: loss of supervisory expertise, loss of senior management decision power, loss of instruction rights over delegates, and delegation exceeding retained functions by a substantial margin (Datatracks, 2024). White label providers must structure delegation agreements to avoid all four triggers.",
    ),
    (
        "What changed for white label AIFMs under AIFMD II?",
        "AIFMD II, with national transposition required by April 16, 2026, introduces: a minimum of two full-time EU-resident senior managers per AIFM (Trustmoore, 2024), mandatory NCA disclosure of conflicts-of-interest management frameworks, clarification that distribution agreements are not delegation, and enhanced Annex IV reporting from April 2027. These changes specifically tighten oversight of white label and third-party AIFM structures.",
    ),
    (
        "Which jurisdiction is best for a white label AIFM: Luxembourg or Ireland?",
        "Luxembourg is the larger and more established market, with 260+ authorized AIFMs and deep PE and credit fund infrastructure (ICLG/ALFI, 2025). Ireland offers a common-law framework familiar to U.S. and UK managers and strong UCITS infrastructure. The right choice depends on your fund structure, target investor base, and the asset classes you manage. Both offer full EU passport rights.",
    ),
]


def md_link(text, url):
    return (
        f'<a href="{url}" class="text-darkGray underline underline-offset-2 '
        f'hover:text-steelBlue transition-colors duration-200" target="_blank" rel="noopener noreferrer">{text}</a>'
    )


def inline_md(s: str) -> str:
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: md_link(m.group(1), m.group(2)), s)
    s = re.sub(r"\*\*([^*]+)\*\*", r'<strong class="text-darkGray">\1</strong>', s)
    return s


def main():
    raw = MD.read_text(encoding="utf-8")
    front = {}
    if raw.startswith("---"):
        parts = raw.split("---", 2)
        fm = parts[1].strip().splitlines()
        raw = parts[2].lstrip("\n")
        for ln in fm:
            if ":" in ln:
                k, v = ln.split(":", 1)
                front[k.strip()] = v.strip().strip('"')
    title = front.get("title", "White Label AIFM: The Complete Guide for 2026")
    desc = front.get(
        "description",
        "A comprehensive guide to white label AIFM services for 2026.",
    )
    date_pub = front.get("date", "2026-03-27")
    slug = "white-label-aifm-complete-guide-2026"
    canonical = f"https://sparkcore.fund/blog/{slug}"
    word_count = 4300

    raw = re.sub(r"^# .+\n+", "", raw, count=1)
    raw = re.sub(r"^!\[.*\]\([^)]+\)\n+", "", raw, count=1, flags=re.MULTILINE)

    lines = raw.splitlines()
    out = []
    i = 0
    in_fence = False
    fence_buf = []

    def flush_p(paragraph_lines):
        if not paragraph_lines:
            return
        text = " ".join(x.strip() for x in paragraph_lines if x.strip())
        if not text:
            return
        if text.startswith("[CHART:"):
            return
        if text.startswith("> "):
            inner = text[2:].strip()
            if inner.startswith("**Key Takeaways**"):
                return
            if inner.startswith("**Citation Capsule:**"):
                inner = inner.replace("**Citation Capsule:**", "").strip()
                out.append(
                    '<blockquote class="border-l-4 border-steelBlue pl-4 my-6 font-inter text-base '
                    'text-mediumGray leading-160 italic"><span class="font-semibold not-italic text-darkGray">'
                    f'Citation capsule.</span> {inline_md(inner)}</blockquote>'
                )
                return
            out.append(
                f'<blockquote class="border-l-4 border-lightGray pl-4 my-6 font-inter text-base text-mediumGray leading-160">{inline_md(inner)}</blockquote>'
            )
            return
        if text.startswith("[PERSONAL EXPERIENCE]:"):
            t = text.split(":", 1)[1].strip()
            out.append(
                f'<p class="font-inter text-base text-mediumGray leading-160 mb-4"><span class="font-semibold text-darkGray">Practitioner note.</span> {inline_md(t)}</p>'
            )
            return
        if text.startswith("[UNIQUE INSIGHT]:"):
            t = text.split(":", 1)[1].strip()
            out.append(
                f'<p class="font-inter text-base text-mediumGray leading-160 mb-4"><span class="font-semibold text-darkGray">Insight.</span> {inline_md(t)}</p>'
            )
            return
        if text.startswith("[ORIGINAL DATA]:"):
            t = text.split(":", 1)[1].strip()
            out.append(
                f'<p class="font-inter text-base text-mediumGray leading-160 mb-4"><span class="font-semibold text-darkGray">Original analysis.</span> {inline_md(t)}</p>'
            )
            return
        ts = text.strip()
        if ts == BOOK_CONSULT:
            out.append(
                f'<p class="font-inter text-base text-mediumGray leading-160 mb-4">Next step: {INTERNAL[BOOK_CONSULT]}</p>'
            )
            return
        if ts in INTERNAL:
            out.append(
                f'<p class="font-inter text-base text-mediumGray leading-160 mb-4">Related reading: {INTERNAL[ts]}</p>'
            )
            return
        for k, v in INTERNAL.items():
            if k in text:
                text = text.replace(k, v)
        if "[CHART:" in text and "EU AIF market NAV" in text:
            out.append(
                '<p class="font-inter text-base text-mediumGray leading-160 mb-4">'
                "For a domicile-by-domicile breakdown of EU alternative investment fund NAV, see the "
                f'{md_link("ESMA EU Alternative Investment Funds Report 2023", "https://www.esma.europa.eu/sites/default/files/2024-01/ESMA50-524821-3095_EU_Alternative_Investment_Funds_2023.pdf")}'
                " (ESMA, 2023). Luxembourg and Ireland typically account for the largest shares of the EU AIF market by NAV.</p>"
            )
            return
        if text.startswith("*") and text.endswith("*") and text.count("*") == 2:
            inner = text.strip("*").strip()
            out.append(
                f'<p class="font-inter text-sm text-mediumGray leading-160 mb-4 italic border-t border-lightGray pt-8 mt-10">{inline_md(inner)}</p>'
            )
            return
        out.append(f'<p class="font-inter text-base text-mediumGray leading-160 mb-4">{inline_md(text)}</p>')

    if lines and lines[0].strip() == "> **Key Takeaways**":
        items = []
        j = 1
        while j < len(lines) and lines[j].startswith("> - "):
            items.append(lines[j][4:].strip())
            j += 1
        out.append('<div class="border-l-4 border-steelBlue bg-[#F9FAFB] pl-5 py-4 pr-4 mb-8 rounded-r-lg">')
        out.append('<p class="font-inter text-sm font-semibold text-darkGray mb-3">Key takeaways</p>')
        out.append('<ul class="font-inter text-base text-mediumGray leading-160 list-disc pl-5 space-y-2">')
        for it in items:
            out.append(f"<li>{inline_md(it)}</li>")
        out.append("</ul></div>")
        lines = lines[j:]

    paragraph = []
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("```"):
            if in_fence:
                svg = "\n".join(fence_buf).strip()
                if svg.startswith("<svg"):
                    out.append(f'<figure class="my-8 overflow-x-auto">{svg}</figure>')
                fence_buf = []
                in_fence = False
            else:
                flush_p(paragraph)
                paragraph = []
                in_fence = True
            i += 1
            continue
        if in_fence:
            fence_buf.append(line)
            i += 1
            continue

        if line.strip() == "---":
            flush_p(paragraph)
            paragraph = []
            i += 1
            continue

        if line.startswith("#"):
            flush_p(paragraph)
            paragraph = []
            level = len(line) - len(line.lstrip("#"))
            title_h = inline_md(line.lstrip("#").strip())
            if level == 2:
                out.append(
                    f'<h2 class="font-funnel-display text-2xl sm:text-custom-3xl text-darkGray mt-10 mb-4">{title_h}</h2>'
                )
            elif level == 3:
                out.append(
                    f'<h3 class="font-funnel-display text-xl sm:text-2xl text-darkGray mt-8 mb-3">{title_h}</h3>'
                )
            i += 1
            continue

        if "|" in line and line.strip().startswith("|") and i + 1 < len(lines) and "---" in lines[i + 1]:
            flush_p(paragraph)
            paragraph = []
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(lines[i])
                i += 1
            out.append(
                '<div class="overflow-x-auto my-8"><table class="w-full font-inter text-sm text-mediumGray border border-lightGray rounded-lg overflow-hidden">'
            )
            header_done = False
            for row in rows:
                cells = [c.strip() for c in row.strip("|").split("|")]
                if set("".join(cells)) <= set("-:"):
                    continue
                out.append("<tr>")
                for ci, c in enumerate(cells):
                    is_head = not header_done
                    tag = "th" if is_head else "td"
                    cell_cls = (
                        "px-4 py-3 text-left border-b border-lightGray bg-[#F9FAFB] font-semibold text-darkGray"
                        if is_head
                        else "px-4 py-3 text-left border-b border-lightGray"
                    )
                    out.append(f'<{tag} class="{cell_cls}">{inline_md(c)}</{tag}>')
                out.append("</tr>")
                header_done = True
            out.append("</table></div>")
            continue

        if line.strip().startswith("- "):
            flush_p(paragraph)
            paragraph = []
            bullets = []
            while i < len(lines):
                if lines[i].strip().startswith("- "):
                    bullets.append(lines[i].strip()[2:])
                    i += 1
                    continue
                if lines[i].strip() == "" and i + 1 < len(lines) and lines[i + 1].strip().startswith("- "):
                    i += 1
                    continue
                break
            out.append(
                '<ul class="font-inter text-base text-mediumGray leading-160 list-disc pl-6 mb-6 space-y-2">'
            )
            for b in bullets:
                out.append(f"<li>{inline_md(b)}</li>")
            out.append("</ul>")
            continue

        if line.strip() == "":
            flush_p(paragraph)
            paragraph = []
            i += 1
            continue

        if line.strip().startswith("!["):
            flush_p(paragraph)
            paragraph = []
            i += 1
            continue

        paragraph.append(line)
        i += 1

    flush_p(paragraph)

    body = "\n".join(out)

    title_short = "White Label AIFM: Complete Guide 2026"
    desc_esc = html_escape_attr(desc)
    title_short_esc = html_escape_attr(title_short)

    ld_blog = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": title,
        "description": desc,
        "datePublished": date_pub,
        "author": {
            "@type": "Person",
            "name": "Alexandre VINAL",
            "url": "https://www.linkedin.com/in/alexandrevinal/",
        },
        "publisher": {
            "@type": "Organization",
            "name": "SparkCore Investment OÜ",
            "url": "https://sparkcore.fund",
            "logo": {
                "@type": "ImageObject",
                "url": "https://sparkcore.fund/assets/images/png/favicon-192x192.png",
            },
        },
        "mainEntityOfPage": {"@type": "WebPage", "@id": canonical},
        "url": canonical,
        "image": "https://sparkcore.fund/meta-image.webp",
        "dateModified": date_pub,
        "wordCount": word_count,
        "inLanguage": "en",
        "keywords": [
            "white label AIFM",
            "AIFMD",
            "AIFMD II",
            "alternative investment fund",
            "Luxembourg AIFM",
            "EU fund passport",
            "third-party AIFM",
        ],
        "isAccessibleForFree": True,
    }
    ld_crumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://sparkcore.fund/"},
            {"@type": "ListItem", "position": 2, "name": "Insights", "item": "https://sparkcore.fund/blog/"},
            {"@type": "ListItem", "position": 3, "name": title_short, "item": canonical},
        ],
    }
    ld_faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in FAQ
        ],
    }

    blog_json = json.dumps(ld_blog, ensure_ascii=False, indent=4)
    crumb_json = json.dumps(ld_crumb, ensure_ascii=False, indent=4)
    faq_json = json.dumps(ld_faq, ensure_ascii=False, indent=4)

    html = f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <script defer src="/assets/js/analytics.js"></script>
    <title>{title_short} | SparkCore</title>
    <meta name="description" content="{desc_esc}" />
    <meta name="robots" content="index, follow" />
    <meta name="author" content="Alexandre VINAL" />

    <link rel="canonical" href="{canonical}" />
    <link rel="alternate" hreflang="en" href="{canonical}" />
    <link rel="alternate" hreflang="x-default" href="{canonical}" />

    <meta property="og:type" content="article" />
    <meta property="article:published_time" content="{date_pub}T00:00:00+00:00" />
    <meta property="article:author" content="https://www.linkedin.com/in/alexandrevinal/" />
    <meta property="og:url" content="{canonical}" />
    <meta property="og:title" content="{title_short_esc}" />
    <meta property="og:description" content="{desc_esc}" />
    <meta property="og:image" content="https://sparkcore.fund/meta-image.webp" />

    <meta property="twitter:card" content="summary_large_image" />
    <meta property="twitter:url" content="{canonical}" />
    <meta property="twitter:title" content="{title_short_esc}" />
    <meta property="twitter:description" content="{desc_esc}" />
    <meta property="twitter:image" content="https://sparkcore.fund/meta-image.webp" />

    <link rel="icon" href="/favicon.ico" type="image/x-icon">
    <link rel="icon" type="image/png" sizes="16x16" href="/assets/images/png/favicon-16x16.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/assets/images/png/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="48x48" href="/assets/images/png/favicon-48x48.png">
    <link rel="apple-touch-icon" sizes="192x192" href="/assets/images/png/favicon-192x192.png">
    <link rel="manifest" href="/site.webmanifest">

    <link rel="preload" href="/assets/css/style.css?v=1.4" as="style">
    <link rel="stylesheet" href="/assets/css/style.css?v=1.4" />
    <link rel="stylesheet" href="/assets/css/tailwind.min.css?v=1.0" />

    <script type="application/ld+json">
{blog_json}
    </script>

    <script type="application/ld+json">
{crumb_json}
    </script>

    <script type="application/ld+json">
{faq_json}
    </script>
  </head>
  <body class="bg-white">
    <header class="bg-white sticky top-0 z-10 drop-shadow-lg">
      <nav class="max-w-[1440px] mx-auto lg:px-8 md:px-6 px-4 py-4 lg:py-[17px] flex justify-between items-center">
        <a rel="noopener noreferrer" href="/"><img class="md:w-[209px] md:h-10 w-[125px] h-6" src="/assets/images/svg/logo.svg" alt="SparkCore Investment OÜ" width="210" height="40"></a>
        <div class="flex item-center gap-7">
          <a href="/" class="font-inter font-normal md:h-[54px] md:px-6 md:py-4 px-4 py-3 h-11 rounded text-sm md:text-base bg-darkGray text-white !leading-140 hover:bg-transparent hover:text-darkGray border border-transparent hover:border-darkGray duration-300 flex items-center justify-center">Contact Us</a>
        </div>
      </nav>
    </header>

    <main class="py-12 sm:py-16 lg:py-20">
      <article class="max-w-[800px] mx-auto px-6">

        <p class="font-inter text-sm text-steelBlue mb-4">Published on 27 March 2026 &middot; By <a href="https://www.linkedin.com/in/alexandrevinal/" target="_blank" rel="noopener noreferrer" class="hover:underline">Alexandre VINAL</a> &middot; 22 min read</p>

        <h1 class="font-funnel-display text-custom-5xl max-md:text-custom-4xl max-sm:text-custom-3xl text-darkGray mb-8 leading-tight">
          {html_escape(title)}
        </h1>

{body}

        <div class="border border-lightGray rounded-lg p-6 bg-[#F9FAFB] mt-10 mb-10">
          <p class="font-inter text-sm text-mediumGray leading-160">
            <strong class="text-darkGray">Disclaimer:</strong> This article is provided for informational purposes only and does not constitute investment advice, a solicitation, or an offer to invest. Investing in crypto-asset funds involves significant risk, including the possible loss of all capital invested. Past performance does not guarantee future results. SparkCore Investment OÜ is registered as a small alternative investment fund manager with the Estonian Financial Supervision Authority (<a href="https://www.fi.ee/" class="text-darkGray underline underline-offset-2 hover:text-steelBlue transition-colors duration-200" target="_blank" rel="noopener noreferrer">Finantsinspektsioon</a>). This content is intended for professional and qualified investors only. Readers should seek independent legal, tax and financial advice before making any investment decision.
          </p>
        </div>

        <div class="text-center py-10 border-t border-lightGray">
          <a href="/blog/" class="font-inter text-sm text-steelBlue hover:text-darkGray transition-colors duration-200 inline-flex items-center gap-2">
            &larr; Back to all articles
          </a>
        </div>

      </article>
    </main>

    <footer>
      <div class="py-8 sm:py-12 lg:py-16 sm:border-t sm:border-lightGray">
        <div class="max-w-[1360px] px-6 mx-auto">
          <div class="flex items-center justify-between custom-xs:mb-4 mb-6">
            <a rel="noopener noreferrer" href="/" class="w-[209px] max-custom-xs:w-[167px] max-custom-xs:h-8 h-10">
              <img class="w-full h-full" src="/assets/images/svg/logo.svg" alt="SparkCore Investment OÜ" width="210" height="40">
            </a>
          </div>
          <p class="font-inter font-normal sm:text-base text-lg text-steelBlue leading-140">
            @<span id="year"></span> SparkCore.investment OÜ — All rights reserved.
          </p>
          <div class="w-full h-px bg-paleBlue custom-xs:my-4 my-6"></div>
          <div class="flex gap-3 flex-wrap max-custom-xs:flex-col items-start justify-start">
            <p class="font-inter text-steelBlue text-base sm:text-sm leading-140">
              <span class="font-inter font-normal leading-140 text-darkGray">Asset management company specialising in crypto-assets, registered in Estonia. Supervised by Finantsinspektsioon:</span>
              <a rel="noopener noreferrer" href="https://www.fi.ee/en/guides/fund-management-companies/investment-market/small-fund-managers-without-activity-licence/sparkcoreinvestment-ou" target="_blank" class="underline underline-offset-2">Estonian Financial Supervisory Authority (Small Fund Manager)</a>
            </p>
            <p class="font-inter text-steelBlue text-base sm:text-sm leading-140">
              <span class="font-inter font-normal leading-140 text-darkGray">Licence:</span>
              <a rel="noopener noreferrer" href="https://mtr.ttja.ee/taotluse_tulemus/609065" target="_blank" class="underline underline-offset-2">EFIU (Financial Institution)</a>
            </p>
          </div>
          <p class="font-inter font-normal text-base text-sm leading-140 text-steelBlue custom-xs:mt-4 mt-6">
            <span class="font-inter font-normal leading-140 text-darkGray">Reg. No. 16265864 — Männimäe 1, Pudisoo, 74626 Harju County, Estonia</span>
            — <a rel="noopener noreferrer" href="https://search.gleif.org/#/record/8945003BBN0RVNNB0S84" target="_blank" class="underline underline-offset-2">LEI: 8945003BBN0RVNNB0S84</a>
          </p>
          <p class="font-inter font-normal text-base text-sm leading-140 text-steelBlue custom-xs:mt-4 mt-6">
            <span class="text-darkGray">Disclaimer:</span>
            Past performance does not guarantee future results. Crypto-assets carry a high level of risk, including the risk of total loss. This website and performance charts are provided for informational purposes only and do not constitute an investment offer. Access to the strategies is reserved for qualified or professional investors. Please assess your personal situation and seek independent advice before investing.
          </p>
          <p class="font-inter font-normal text-sm leading-140 text-steelBlue custom-xs:mt-2 mt-3">
            <a rel="noopener noreferrer" href="/privacy-policy" class="underline underline-offset-2 hover:text-darkGray transition-colors duration-200">Privacy Policy</a>
          </p>
        </div>
      </div>
    </footer>
    <script src="/assets/js/set-year.js"></script>
  </body>
</html>
"""
    OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT}")


def html_escape_attr(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace('"', "&quot;")
        .replace("<", "&lt;")
    )


def html_escape(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


if __name__ == "__main__":
    main()
