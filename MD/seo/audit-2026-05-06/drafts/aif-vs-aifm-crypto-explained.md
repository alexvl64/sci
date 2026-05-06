---
title: "AIF vs AIFM: What's the Difference and Why It Matters for Crypto Funds"
description: "AIF is the fund vehicle. AIFM is the manager. Under AIFMD, every regulated crypto fund needs both — and conflating them costs trust. Explained."
slug: "aif-vs-aifm-crypto-explained"
date: "2026-05-06"
lastUpdated: "2026-05-06"
author: "Alexandre VINAL"
authorUrl: "https://www.linkedin.com/in/alexandrevinal/"
coverImage: "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=1200&h=630&fit=crop&q=80"
coverImageAlt: "European Union flags outside an EU regulatory institution — symbolising the AIFMD framework that governs alternative investment fund managers across all 27 member states"
ogImage: "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=1200&h=630&fit=crop&q=80"
keywords: ["AIF vs AIFM", "AIFM crypto", "alternative investment fund", "alternative investment fund manager", "AIFMD", "crypto fund manager"]
inLanguage: "en"
type: "explainer"
template: "comparison"
estimatedReadingTime: "6 min"
---

# AIF vs AIFM: What's the Difference and Why It Matters for Crypto Funds

> **Quick answer**
>
> An AIF is the *fund vehicle* — the legal structure pooling investor capital. An AIFM is the *manager* — the regulated entity running the AIF. Under EU AIFMD, every regulated alternative fund needs both: an AIF (what investors subscribe to) and an authorised or registered AIFM (who answers to the regulator). The fund holds the assets; the manager holds the licence.

Founders new to fund regulation often blur these two acronyms. AIF and AIFM look like initials of the same thing, but the legal and operational distinction matters enormously — for fundraising, for compliance, for who the regulator calls when something goes wrong. The Alternative Investment Fund Managers Directive ([Directive 2011/61/EU](https://eur-lex.europa.eu/eli/dir/2011/61/oj), 2011) is built on that two-layer architecture, and every crypto fund manager operating in the EU has to internalise it.

> **Key Takeaways**
>
> - **AIF = the fund** (the legal vehicle holding investor capital). **AIFM = the manager** (the authorised firm running the AIF).
> - AIFMD requires both layers: the AIFM is the regulated counterpart Finantsinspektsioon supervises; the AIF is the contract investors subscribe to.
> - One AIFM can manage multiple AIFs simultaneously — that's the standard model and the foundation of white-label fund platforms.
> - SparkCore.investment OÜ is an Estonian AIFM (LEI 8945003BBN0RVNNB0S84). *Dynamic Trends*, *CryptoVision*, and *Equinoxe* are AIFs under that AIFM.

## What is an AIF (Alternative Investment Fund)?

An AIF is a collective investment vehicle that pools capital from multiple investors and invests it according to a defined policy, on the basis that it is **not** a UCITS (the EU retail mutual fund regime). AIFMD defines it broadly: any non-UCITS fund qualifies, regardless of legal form, jurisdiction, or asset class.

In practice, an AIF can be a Luxembourg SCSp, an Irish ICAV, a German Investment KG, or — relevant for SparkCore — an Estonian *usaldusfond* (limited partnership). The vehicle is just a contract or company structure. What makes it an *alternative* investment fund is what's inside (private equity, real estate, hedge strategies, crypto-assets) and who can subscribe (typically professional investors only).

The common confusion is treating "AIF" as a synonym for "hedge fund". It isn't. AIF is a regulatory category. Hedge funds, PE funds, real estate funds, and crypto funds all sit under it.

<!-- [UNIQUE INSIGHT] -->
> **Citation capsule:** Under AIFMD Article 4(1)(a), an AIF is *"any collective investment undertaking, which raises capital from a number of investors, with a view to investing it in accordance with a defined investment policy for the benefit of those investors, and which does not require authorisation pursuant to Article 5 of Directive 2009/65/EC"* — i.e., it is anything that's a fund but isn't a UCITS ([EUR-Lex, AIFMD](https://eur-lex.europa.eu/eli/dir/2011/61/oj), 2011).

## What is an AIFM (Alternative Investment Fund Manager)?

An AIFM is the regulated firm that manages one or more AIFs. The AIFM is the entity that holds the AIFMD authorisation (or registration), employs portfolio managers, runs risk management, oversees valuation, and answers directly to the regulator. The fund itself doesn't carry a licence — the manager does.

Under AIFMD Article 5, the AIFM is solely responsible for ensuring compliance with the directive's organisational, conduct, transparency, and capital requirements. If something goes wrong with an AIF — mispricing, breach of investment policy, AML failure — the regulator looks at the AIFM, not the fund. The fund is a contract. The manager is a person (or rather, a regulated legal entity with named senior managers and a designated MLRO).

> **Citation capsule:** ESMA tracks AIFMs and AIFs as separate populations in its [Annual Statistical Report on EU Alternative Investment Funds](https://www.esma.europa.eu/data-research/asr-alternative-investment-funds), 2024. The standard market structure shows several AIFs per AIFM — most managers run multiple funds under shared regulatory infrastructure, which is why the AIF / AIFM distinction is operationally fundamental, not academic.

## Who can be an AIFM? Two regimes coexist

AIFMD permits two pathways into the AIFM perimeter, and the choice depends almost entirely on assets under management.

A **fully authorised AIFM** holds an EU passport. It can market its AIFs to professional investors across the entire EU/EEA without re-registering in each member state. Capital requirements start at EUR 125,000 (plus 0.02% of AUM above EUR 250 million), and the authorisation process typically runs three to six months or longer.

A **sub-threshold AIFM** (AIFMD Article 3(2)) operates below either EUR 100 million in leveraged AUM or EUR 500 million in unleveraged, locked-in AUM. It registers with its national regulator only — no EU passport, no full directive obligations, but a much faster path to market. In Estonia, registration with Finantsinspektsioon takes 30 to 60 days.

> **Citation capsule:** Under AIFMD Article 3(2), the EUR 100M / EUR 500M thresholds determine whether an AIFM falls into the lighter sub-threshold registration regime or must obtain full authorisation under Article 6. Crossing either threshold triggers a mandatory upgrade pathway with proportionate capital, reporting, and depositary obligations ([EUR-Lex, AIFMD consolidated text](https://eur-lex.europa.eu/eli/dir/2011/61/oj), 2011).

For deeper detail on the sub-threshold path, see [INTERNAL-LINK: sub-threshold AIFM for crypto in Estonia → /blog/sub-threshold-aifm-crypto-estonia].

## Why the AIF / AIFM distinction matters in practice

Conflating them creates real problems. Three concrete examples.

**Fundraising.** Investors don't subscribe to an AIFM. They subscribe to an AIF. The AIFM provides the regulatory shell, but the fund documentation, NAV, and reporting belong to the AIF. Pitch decks that talk about "investing in our AIFM" confuse counterparties — and good due-diligence teams will notice.

**Compliance scope.** AIFMD obligations attach to the AIFM. AML duties attach to both, but the AIFM is the regulated entity for KYC, transaction monitoring, and suspicious-activity reporting. Crypto-specific obligations under MiCA Article 60 attach to the AIFM, not the AIF — and only fully authorised AIFMs can use that pathway.

**Accountability.** The AIFM signs the regulatory file. If an AIF breaches its investment policy, the regulator suspends or fines the AIFM. The AIF can keep operating under a new AIFM if delegation is restructured, but the AIF itself isn't a regulated entity that can be sanctioned directly.

## AIF vs AIFM in the crypto context

Crypto adds two specific layers on top of the standard AIFMD picture.

First, MiCA ([Regulation (EU) 2023/1114](https://eur-lex.europa.eu/eli/reg/2023/1114/oj), 2023) overlays AIFMD for crypto-asset services. An AIFM managing a crypto AIF can use MiCA Article 60 to provide portfolio management on crypto-assets without needing a separate CASP licence — but only if the AIFM is fully authorised. Sub-threshold AIFMs are explicitly excluded. See [INTERNAL-LINK: do crypto fund managers need a MiCA CASP licence → /blog/do-crypto-fund-managers-need-mica-casp-license] for the full breakdown.

Second, custody. Under AIFMD Article 21, every AIF needs a depositary. For crypto-assets, that depositary must be a MiCA-licensed CASP authorised to safekeep crypto. The AIFM doesn't custody the assets itself — it appoints the depositary. Investors evaluating a crypto AIF should always ask three questions: which entity is the AIFM, which is the AIF, and which is the depositary? The answers should be three distinct legal entities with three distinct roles.

## How SparkCore is structured (a worked example)

SparkCore.investment OÜ is the **AIFM**. It's an Estonian *osaühing* (private limited company), registered with Finantsinspektsioon as a Small Fund Manager under the sub-threshold regime (LEI 8945003BBN0RVNNB0S84, [GLEIF record](https://search.gleif.org/#/record/8945003BBN0RVNNB0S84)). It holds an EFIU Financial Institution licence for AML supervision. KPMG Estonia audits the AIFM.

The **AIFs** under that AIFM are three Estonian *usaldusfond* limited partnerships, each with its own fund documentation, NAV, and investor register:

- **Dynamic Trends** — directional crypto exposure, operational since August 2025
- **CryptoVision** — algorithmic defensive strategy, operational since 2021
- **Equinoxe** — market-neutral, planned launch 2026

Investors subscribe to *Dynamic Trends* or *CryptoVision* — not to "SparkCore" in the abstract. The AIFM is the contractual counterparty for the management agreement and the regulator's point of contact, but the investment relationship is fund-by-fund.

<!-- [PERSONAL EXPERIENCE] -->
In practice, this two-layer structure shows up in due-diligence calls all the time. Family offices ask "are you regulated?" — meaning the AIFM. They then ask "what does the fund hold?" — meaning the AIF. Both answers matter; conflating them costs trust.

## Frequently asked questions

### Can a single AIFM manage multiple AIFs?

Yes — and it's the standard model across the EU. Each AIF maintains independent fund documentation, an independent investor base, and independent assets under management, but they share the AIFM's regulatory authorisation, risk management framework, and operational backbone. White-label fund platforms are built on exactly this architecture.

### Does every AIF need its own AIFM, or can one AIFM run several?

Every AIF must have an AIFM, but not a unique one. The same AIFM can run multiple AIFs simultaneously. What changes per AIF is the fund documentation, the investment policy, the NAV calculation, and the depositary arrangement. The manager — and its AIFMD authorisation — stays constant across the portfolio of funds it manages.

### Is an AIFM the same as a UCITS management company?

No. UCITS management companies fall under the [UCITS Directive](https://eur-lex.europa.eu/eli/dir/2009/65/oj) and manage retail-eligible mutual funds. AIFMs fall under AIFMD and manage non-UCITS alternative funds for professional investors. The two regimes have different capital requirements, distribution rules, and asset eligibility — though some firms hold both authorisations.

## Conclusion

The AIF / AIFM distinction is structural, not pedantic. Investors subscribe to AIFs. Regulators supervise AIFMs. Compliance attaches to the AIFM. Capital sits in the AIF. Get the language right and the rest of the regulatory conversation falls into place.

For the deeper Estonian regulatory framework, see [INTERNAL-LINK: regulated crypto fund managers in Estonia → /blog/regulated-crypto-fund-manager-estonia]. For the launch process itself, [INTERNAL-LINK: how to launch a crypto fund in Estonia → /blog/how-to-launch-a-crypto-fund-estonia]. For the underlying definition of an AIFM, [INTERNAL-LINK: what is a crypto AIFM → /blog/what-is-a-crypto-aifm].

## Sources

- European Parliament & Council, *Directive 2011/61/EU on Alternative Investment Fund Managers (AIFMD)*, retrieved 2026-05-06: https://eur-lex.europa.eu/eli/dir/2011/61/oj
- European Parliament & Council, *Regulation (EU) 2023/1114 on Markets in Crypto-Assets (MiCA)*, retrieved 2026-05-06: https://eur-lex.europa.eu/eli/reg/2023/1114/oj
- European Parliament & Council, *Directive 2009/65/EC (UCITS)*, retrieved 2026-05-06: https://eur-lex.europa.eu/eli/dir/2009/65/oj
- ESMA, *Annual Statistical Report on EU Alternative Investment Funds*, retrieved 2026-05-06: https://www.esma.europa.eu/data-research/asr-alternative-investment-funds
- Finantsinspektsioon, *Small Fund Managers Without Activity Licence — SparkCore.investment OÜ entry*, retrieved 2026-05-06: https://www.fi.ee/en/guides/fund-management-companies/investment-market/small-fund-managers-without-activity-licence/sparkcoreinvestment-ou
- GLEIF, *SparkCore Investment OÜ (LEI 8945003BBN0RVNNB0S84)*, retrieved 2026-05-06: https://search.gleif.org/#/record/8945003BBN0RVNNB0S84

## Risk Disclaimer

This article is provided for informational purposes only and does not constitute investment advice, a solicitation, or an offer to invest. Investing in crypto-asset funds involves significant risk, including the possible loss of all capital invested. Past performance does not guarantee future results. SparkCore.investment OÜ is registered as a small alternative investment fund manager with the Estonian Financial Supervision Authority ([Finantsinspektsioon](https://www.fi.ee/)). This content is intended for professional and qualified investors only. Readers should seek independent legal, tax and financial advice before making any investment decision.
