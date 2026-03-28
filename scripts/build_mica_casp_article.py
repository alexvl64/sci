#!/usr/bin/env python3
"""Build blog/do-crypto-fund-managers-need-mica-casp-license.html from MD/do-crypto-fund-managers-need-mica-casp-license.md."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / "MD" / "do-crypto-fund-managers-need-mica-casp-license.md"
OUT = ROOT / "blog" / "do-crypto-fund-managers-need-mica-casp-license.html"
SLUG = "do-crypto-fund-managers-need-mica-casp-license"

INTERNAL = {
    "[INTERNAL-LINK: MiCA Article 3 crypto-asset services list → explainer on all nine CASP service categories under MiCA]": (
        '<a href="/blog/crypto-fund-compliance-guide" class="text-darkGray underline underline-offset-2 '
        'hover:text-steelBlue transition-colors duration-200">MiCA, CASP categories, and fund compliance</a>'
    ),
    "[INTERNAL-LINK: AIFMD authorization scope and requirements → guide to obtaining full AIFMD authorization in the EU]": (
        '<a href="/blog/what-is-a-crypto-aifm" class="text-darkGray underline underline-offset-2 '
        'hover:text-steelBlue transition-colors duration-200">AIFMD authorization and the crypto AIFM role</a>'
    ),
    "[INTERNAL-LINK: Article 60 notification checklist → step-by-step compliance guide for AIFMD managers adding crypto services]": (
        '<a href="/blog/crypto-fund-compliance-guide" class="text-darkGray underline underline-offset-2 '
        'hover:text-steelBlue transition-colors duration-200">Compliance guide for fund managers</a>'
    ),
    "[INTERNAL-LINK: Full CASP authorization process → step-by-step guide to applying for a MiCA CASP license in the EU]": (
        '<a href="/blog/crypto-fund-compliance-guide" class="text-darkGray underline underline-offset-2 '
        'hover:text-steelBlue transition-colors duration-200">EU crypto licensing and compliance steps</a>'
    ),
    "[INTERNAL-LINK: Estonia MiCA licensing in 2026 → guide to applying for a CASP license with Estonia's FSA]": (
        '<a href="/blog/regulated-crypto-fund-manager-estonia" class="text-darkGray underline underline-offset-2 '
        'hover:text-steelBlue transition-colors duration-200">Regulated crypto fund management in Estonia</a>'
    ),
    "[INTERNAL-LINK: MiCA grandfathering explained → detailed guide to national transition periods by member state]": (
        '<a href="/blog/crypto-fund-compliance-guide" class="text-darkGray underline underline-offset-2 '
        'hover:text-steelBlue transition-colors duration-200">Regulatory timelines and fund compliance</a>'
    ),
    "[INTERNAL-LINK: Choosing the right EU jurisdiction for your CASP license → comparison of MiCA licensing hubs across member states]": (
        '<a href="/blog/how-to-launch-a-crypto-fund-estonia" class="text-darkGray underline underline-offset-2 '
        'hover:text-steelBlue transition-colors duration-200">Launching a fund and choosing a jurisdiction</a>'
    ),
    "[INTERNAL-LINK: MiCA CASP application roadmap → step-by-step authorization guide for EU crypto fund managers]": (
        '<a href="/blog/crypto-fund-compliance-guide" class="text-darkGray underline underline-offset-2 '
        'hover:text-steelBlue transition-colors duration-200">Crypto fund compliance and authorization roadmap</a>'
    ),
}

FAQ = [
    (
        "Does an AIFM managing a crypto-only fund need a MiCA CASP license?",
        "Not if it holds full AIFMD authorization. A fully authorized AIFM can manage a crypto-only fund and provide crypto portfolio management to clients using MiCA's Article 60 notification pathway — 40 working days' advance notice to its home regulator, with deemed authorization on expiry of the window. Sub-threshold registered AIFMs are explicitly excluded from this pathway under Article 60(5).",
    ),
    (
        "Can a grandfathered firm passport its crypto services across the EU?",
        "No. Firms operating under national grandfathering provisions during the MiCA transition period are not considered MiCA-authorized CASPs and cannot exercise EU passporting rights. Cross-border crypto service provision to clients in other member states requires a full MiCA CASP authorization obtained in a home member state.",
    ),
    (
        "Is Estonia still a viable jurisdiction for crypto fund managers post-MiCA?",
        "Estonia remains a credible option, but it is no longer a low-cost shortcut. All legacy FIU-issued VASP licenses expire 1 July 2026, and the FSA now applies full MiCA standards. Firms choosing Estonia today get an FSA with growing MiCA implementation experience and an established crypto regulatory culture, but no regulatory advantage over other EU jurisdictions that have moved aggressively on MiCA authorization.",
    ),
    (
        "What's the minimum capital requirement for a CASP providing portfolio management?",
        "Portfolio management falls under the €125,000 minimum own funds tier under MiCA Article 67. That figure represents the floor — the actual requirement is the higher of €125,000 or 25% of the firm's prior-year fixed overheads. Firms providing only advisory services face the lower €50,000 threshold; firms operating a trading platform face €150,000.",
    ),
    (
        "Can a UCITS management company also use Article 60 for crypto services?",
        "Yes. UCITS management companies authorized under Directive 2009/65/EC are listed explicitly in MiCA Article 60 alongside AIFMs and MiFID II investment firms. They follow the same 40-working-day notification procedure and are subject to the same deemed-authorization mechanism. The same filing requirements apply: service description, operational program, AML/CFT documentation, ICT architecture, asset segregation policy, and market abuse detection procedures.",
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
    s = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", s)
    return s


def parse_frontmatter(raw: str):
    front = {}
    if not raw.startswith("---"):
        return raw, front
    parts = raw.split("---", 2)
    fm = parts[1].strip().splitlines()
    body = parts[2].lstrip("\n")
    for ln in fm:
        if ":" in ln:
            k, v = ln.split(":", 1)
            front[k.strip()] = v.strip().strip('"').strip("'")
    return body, front


def preprocess(lines: list[str]) -> list[str]:
    out = []
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if s == "<!-- [PERSONAL EXPERIENCE] -->":
            i += 1
            while i < len(lines) and not lines[i].strip():
                i += 1
            if i < len(lines):
                out.append("[PERSONAL EXPERIENCE]: " + lines[i])
                i += 1
            continue
        if re.fullmatch(r"<!--\s*\[UNIQUE INSIGHT\]\s*-->", s):
            i += 1
            while i < len(lines) and not lines[i].strip():
                i += 1
            if i < len(lines) and not lines[i].lstrip().startswith(">"):
                out.append("[UNIQUE INSIGHT]: " + lines[i])
                i += 1
            elif i < len(lines):
                out.append(lines[i])
                i += 1
            continue
        if s.startswith("<!--") and s.endswith("-->"):
            i += 1
            continue
        out.append(lines[i])
        i += 1
    return out


def main():
    raw_full = MD.read_text(encoding="utf-8")
    raw, front = parse_frontmatter(raw_full)
    title = front.get("title", "Do Crypto Fund Managers Need a MiCA CASP License?")
    desc = front.get("description", "")
    date_pub = front.get("date", "2026-03-28").strip('"')
    og_image = front.get("ogImage", "https://sparkcore.fund/meta-image.webp")
    if not og_image.startswith("http"):
        og_image = "https://sparkcore.fund/meta-image.webp"
    canonical = f"https://sparkcore.fund/blog/{SLUG}"
    title_short = "MiCA CASP License for Crypto Fund Managers?"
    word_count = 3800
    months = (
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    )
    try:
        y, m, d = date_pub.split("-")
        published_human = f"{int(d)} {months[int(m) - 1]} {y}"
    except (ValueError, IndexError):
        published_human = date_pub

    raw = re.sub(r"^# .+\n+", "", raw, count=1)
    cover = front.get("coverImage", "").strip().strip('"').strip("'")
    alt_c = front.get("coverImageAlt", "").strip().strip('"').strip("'") or "Article illustration"
    hero_html = ""
    if cover.startswith("http"):
        hero_html = (
            f'<figure class="my-8"><img src="{html_escape_attr(cover)}" alt="{html_escape_attr(alt_c)}" '
            'class="w-full rounded-lg object-cover max-h-[420px]" loading="lazy" width="1260" height="750" /></figure>\n'
        )
    raw = re.sub(r"\n!\[[^\]]*\]\([^\)]+\)\s*\n", "\n\n", raw, count=1)

    lines = preprocess(raw.splitlines())
    out = []
    hero_pending = hero_html or ""

    i = 0
    paragraph = []

    def flush_p(paragraph_lines):
        if not paragraph_lines:
            return
        text = " ".join(x.strip() for x in paragraph_lines if x.strip())
        if not text:
            return
        if text.startswith("> "):
            inner = text[2:].strip()
            if inner.startswith("**Key Takeaways**"):
                return
            if inner.startswith("**Our analysis:**"):
                inner = inner.replace("**Our analysis:**", "").strip()
                out.append(
                    '<blockquote class="border-l-4 border-steelBlue pl-4 my-6 font-inter text-base '
                    'text-mediumGray leading-160 italic"><span class="font-semibold not-italic text-darkGray">'
                    f'Our analysis.</span> {inline_md(inner)}</blockquote>'
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
        ts = text.strip()
        if ts in INTERNAL:
            out.append(
                f'<p class="font-inter text-base text-mediumGray leading-160 mb-4">Related reading: {INTERNAL[ts]}</p>'
            )
            return
        for k, v in INTERNAL.items():
            if k in text:
                text = text.replace(k, v)
        if text.startswith("*") and text.endswith("*") and text.count("*") == 2:
            inner = text.strip("*").strip()
            out.append(
                f'<p class="font-inter text-sm text-mediumGray leading-160 mb-4 italic border-t border-lightGray pt-8 mt-10">{inline_md(inner)}</p>'
            )
            return
        out.append(f'<p class="font-inter text-base text-mediumGray leading-160 mb-4">{inline_md(text)}</p>')

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped == "> **Key Takeaways**":
            flush_p(paragraph)
            paragraph = []
            if hero_pending:
                out.append(hero_pending.rstrip())
                hero_pending = ""
            items = []
            j = i + 1
            while j < len(lines) and lines[j].startswith("> - "):
                items.append(lines[j][4:].strip())
                j += 1
            out.append('<div class="border-l-4 border-steelBlue bg-[#F9FAFB] pl-5 py-4 pr-4 mb-8 rounded-r-lg">')
            out.append('<p class="font-inter text-sm font-semibold text-darkGray mb-3">Key takeaways</p>')
            out.append('<ul class="font-inter text-base text-mediumGray leading-160 list-disc pl-5 space-y-2">')
            for it in items:
                out.append(f"<li>{inline_md(it)}</li>")
            out.append("</ul></div>")
            i = j
            continue

        if stripped.startswith("<figure"):
            flush_p(paragraph)
            paragraph = []
            fig_lines = [line]
            i += 1
            while i < len(lines) and "</figure>" not in lines[i]:
                fig_lines.append(lines[i])
                i += 1
            if i < len(lines):
                fig_lines.append(lines[i])
            fig_html = "\n".join(fig_lines)
            fig_html = fig_html.replace("<figure>", '<figure class="my-8 overflow-x-auto">', 1)
            out.append(fig_html)
            i += 1
            continue

        if stripped == "---":
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
                for c in cells:
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

        if re.match(r"^\d+\.\s", stripped):
            flush_p(paragraph)
            paragraph = []
            items = []
            while i < len(lines):
                st = lines[i].strip()
                if re.match(r"^\d+\.\s", st):
                    items.append(re.sub(r"^\d+\.\s*", "", st))
                    i += 1
                    continue
                if st == "" and i + 1 < len(lines) and re.match(r"^\d+\.\s", lines[i + 1].strip()):
                    i += 1
                    continue
                break
            out.append(
                '<ol class="font-inter text-base text-mediumGray leading-160 list-decimal pl-6 mb-6 space-y-3">'
            )
            for it in items:
                out.append(f"<li>{inline_md(it)}</li>")
            out.append("</ol>")
            continue

        if stripped.startswith("- "):
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

        if stripped == "":
            flush_p(paragraph)
            paragraph = []
            i += 1
            continue

        paragraph.append(line)
        i += 1

    flush_p(paragraph)
    if hero_pending:
        out.append(hero_pending.rstrip())

    body = "\n".join(out)

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
        "image": og_image,
        "dateModified": date_pub,
        "wordCount": word_count,
        "inLanguage": "en",
        "keywords": [
            "MiCA",
            "CASP",
            "crypto fund manager",
            "AIFMD",
            "Article 60",
            "EU crypto regulation",
            "Estonia",
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
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in FAQ
        ],
    }

    desc_esc = html_escape_attr(desc)
    title_short_esc = html_escape_attr(title_short)
    blog_json = json.dumps(ld_blog, ensure_ascii=False, indent=4)
    crumb_json = json.dumps(ld_crumb, ensure_ascii=False, indent=4)
    faq_json = json.dumps(ld_faq, ensure_ascii=False, indent=4)
    og_esc = html_escape_attr(og_image)

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
    <meta property="og:image" content="{og_esc}" />

    <meta property="twitter:card" content="summary_large_image" />
    <meta property="twitter:url" content="{canonical}" />
    <meta property="twitter:title" content="{title_short_esc}" />
    <meta property="twitter:description" content="{desc_esc}" />
    <meta property="twitter:image" content="{og_esc}" />

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

        <p class="font-inter text-sm text-steelBlue mb-4">Published on {published_human} &middot; By <a href="https://www.linkedin.com/in/alexandrevinal/" target="_blank" rel="noopener noreferrer" class="hover:underline">Alexandre VINAL</a> &middot; 19 min read</p>

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
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;")


def html_escape(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


if __name__ == "__main__":
    main()
