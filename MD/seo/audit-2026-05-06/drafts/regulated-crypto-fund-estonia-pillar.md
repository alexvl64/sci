---
title: "Launching a Regulated Crypto Fund in Estonia: The Complete Guide"
description: "A complete guide to setting up a regulated crypto AIF in Estonia under AIFMD: jurisdictions compared, sub-threshold vs full AIFM, costs, timelines, MiCA overlay, custody, distribution, and a worked example."
slug: "regulated-crypto-fund-estonia"
url: "/resources/regulated-crypto-fund-estonia/"
date: "2026-05-06"
lastUpdated: "2026-05-06"
author: "Alexandre VINAL"
authorUrl: "https://www.linkedin.com/in/alexandrevinal/"
coverImage: "https://images.unsplash.com/photo-1518780664697-55e3ad937233?w=1200&h=630&fit=crop&q=80"
coverImageAlt: "Modern Estonian capital Tallinn skyline at dusk — symbolising Estonia's position as the EU's lowest-cost AIFM jurisdiction for crypto fund managers"
ogImage: "https://images.unsplash.com/photo-1518780664697-55e3ad937233?w=1200&h=630&fit=crop&q=80"
keywords: ["regulated crypto fund Estonia", "AIFM Estonia", "crypto fund manager Estonia", "AIFMD crypto", "Finantsinspektsioon", "small fund manager Estonia", "MiCA crypto fund", "EU crypto fund"]
inLanguage: "en"
type: "pillar"
template: "pillar-page"
estimatedReadingTime: "16 min"
---

# Launching a Regulated Crypto Fund in Estonia: The Complete Guide

> **Quick answer**
>
> A regulated crypto fund in Estonia is an Alternative Investment Fund (AIF) managed under AIFMD by an authorised or registered AIFM and supervised by Finantsinspektsioon (EFSA). For managers below EUR 100 million in leveraged AUM, the sub-threshold registration regime cuts time to market to 30-60 days with capital around EUR 25,000 — making Estonia the EU's lowest-cost compliant entry point. MiCA Article 60 governs crypto-asset portfolio management; AIFMD Article 21 governs custody.

Estonia has built a distinct reputation in the EU as a jurisdiction where digital-asset fund managers can operate under a clear, structured regulatory framework — without the cost ceiling of Luxembourg or the operational opacity of less-supervised offshore options. For institutional allocators, family offices, and prospective fund managers evaluating the regulated route into crypto-assets, the Estonian regime combines EU-harmonised supervision under AIFMD, a digitally-native administrative infrastructure, and a measurable cost advantage over alternative EU jurisdictions.

This pillar guide is the complete map of how to launch and operate a regulated crypto fund in Estonia in 2026. It covers the regulatory framework, jurisdiction comparison, AIFM regimes, registration steps, capital requirements, the MiCA overlay, custody, distribution rules, costs and timelines, and a concrete worked example using SparkCore Fund Management's own structure. Each section links to the deeper article in our cluster for readers who want the full detail.

> **Key Takeaways**
>
> - **Estonia is the lowest-cost EU AIFM jurisdiction** — roughly EUR 27,000 total entry cost (capital + fees) versus EUR 125,000+ for Luxembourg or Malta, and 30-60 day registration vs 3-6+ months elsewhere.
> - **Two AIFMD regimes coexist:** sub-threshold registration (Article 3(2), under EUR 100M leveraged or EUR 500M unleveraged AUM) and full authorisation (Article 6). The choice is structural — driven by AUM growth ambition, not preference.
> - **MiCA overlays AIFMD** for crypto services. Fully authorised AIFMs can use Article 60 to provide crypto portfolio management without a separate CASP licence. Sub-threshold AIFMs cannot.
> - **Custody must go through a MiCA-licensed CASP.** AIFMD Article 21 makes the depositary mandatory; for crypto-assets, that depositary must be CASP-authorised.
> - **The Estonian *usaldusfond*** (limited partnership) is the standard AIF vehicle — comparable to Luxembourg SCSp or Irish ICAV but with lower mandatory capital and faster registration.

## What "regulated crypto fund" means in the EU

A regulated crypto fund in the EU is a collective investment vehicle that holds crypto-assets, operates under the Alternative Investment Fund Managers Directive ([Directive 2011/61/EU](https://eur-lex.europa.eu/eli/dir/2011/61/oj), 2011), and is managed by an authorised or registered AIFM supervised by a national regulator. The crypto-asset content doesn't change the regulatory category — it's still an AIF — but it triggers additional MiCA obligations on portfolio management and custody.

"Regulated" in this context means three things, all of which are verifiable in public registries:

1. **The AIFM is on the regulator's register.** Finantsinspektsioon publishes the [list of registered Small Fund Managers and authorised AIFMs](https://www.fi.ee/en/finantsinspektsioon-0/finantsinspektsiooni-tegevus/turuosaliste-jarelevalve/turuosaliste-otsing). If the manager isn't on that list, it isn't regulated in Estonia.
2. **The AIFM has a Legal Entity Identifier (LEI).** The LEI is the global machine-verifiable identity record for any entity participating in financial markets, maintained by [GLEIF](https://www.gleif.org/). Every AIFM should have one.
3. **The AIF has a depositary appointed under AIFMD Article 21.** The depositary safekeeps the assets, monitors cash flows, and verifies ownership — independently of the AIFM.

If any of those three conditions are missing, the fund is not regulated in the AIFMD sense, regardless of marketing language.

> **Citation capsule:** AIFMD applies to "any collective investment undertaking which raises capital from a number of investors, with a view to investing it in accordance with a defined investment policy" and is not a UCITS ([EUR-Lex, Directive 2011/61/EU Article 4(1)(a)](https://eur-lex.europa.eu/eli/dir/2011/61/oj), 2011). Crypto-asset funds fall under this definition. The "regulated" status flows from the AIFM's authorisation or registration with a national regulator, not from the asset class.

For the deeper definitional layer, see [INTERNAL-LINK: AIF vs AIFM explained → /blog/aif-vs-aifm-crypto-explained] and [INTERNAL-LINK: what is a crypto AIFM → /blog/what-is-a-crypto-aifm].

## Why Estonia for crypto fund managers

Three factors converge to make Estonia the default EU choice for emerging crypto fund managers in 2026: cost, speed, and clarity.

**Cost.** Estonia's mandatory capital for a sub-threshold AIFM is EUR 25,000, plus a EUR 2,000 EFSA registration fee and EUR 500 annual supervision fee. Total entry cost: ~EUR 27,000. By contrast, Luxembourg's sub-threshold AIFM (under the LFM regime) requires roughly EUR 125,000 in capital plus higher legal and incorporation fees. Malta sits between the two but with longer process times. The cost difference compounds when the AIFM is bootstrapping a first fund of EUR 20-50 million.

**Speed.** Estonia's Finantsinspektsioon publishes 30-60 day target turnarounds for sub-threshold AIFM registrations. Comparable processes in Luxembourg run 3-6+ months. Banking onboarding adds another month or two everywhere — but Estonia's digital infrastructure (e-Residency, LV.ee government APIs, electronic identity) shortens the administrative cycle.

**Clarity.** The Estonian regulatory culture for AIFMs is documented and predictable. The EFSA publishes guidelines, registers, and decisions in English. The legacy crypto-services VASP regime — which Estonia phased out under MiCA — was replaced cleanly: legacy VASP licences expire 1 July 2026, and the EFSA now applies full MiCA standards with growing implementation experience.

> **Citation capsule:** Estonia's small fund manager regime is detailed by Finantsinspektsioon at [fi.ee — Small Fund Managers Without Activity Licence](https://www.fi.ee/en/guides/fund-management-companies/investment-market/small-fund-managers-without-activity-licence) (2025). The €25,000 capital floor and €2,000 registration fee place it as the lowest-cost authorised pathway among the major EU AIFM jurisdictions.

For a side-by-side comparison with Luxembourg and Malta, see [INTERNAL-LINK: Estonia vs Luxembourg vs Malta for crypto funds → /blog/estonia-luxembourg-malta-crypto-fund].

## Sub-threshold vs full AIFM: which regime fits you

AIFMD permits two distinct pathways into the AIFM regulatory perimeter, and the choice is almost always determined by AUM, not preference.

A **sub-threshold AIFM** (AIFMD Article 3(2)) operates below either EUR 100 million in leveraged AUM, or EUR 500 million in unleveraged AUM with a minimum 5-year investor lock-in. Sub-threshold managers register with their national regulator only — no EU passport, no full directive obligations on remuneration / risk management / depositary, but proportionate ongoing supervision. The Estonian process takes 30-60 days post-application.

A **fully authorised AIFM** (AIFMD Article 6) holds the EU passport. It can market its AIFs to professional investors across all EU/EEA member states without re-registering in each. Capital requirements start at EUR 125,000 plus 0.02% of AUM above EUR 250 million, and the authorisation runs 3-6+ months. Full obligations attach: risk management, valuation policy, depositary, organisational requirements, remuneration disclosure.

<!-- [UNIQUE INSIGHT] -->
The trap most new managers fall into: assuming "register sub-threshold first, upgrade later" is friction-free. It isn't. Crossing the threshold triggers a hard switch to full authorisation — same dossier intensity as starting from scratch, but now with a live fund book to manage during the transition. Plan the regime choice against your 24-36 month AUM trajectory, not the launch month.

For the full breakdown of the sub-threshold regime, including capital, ongoing reporting, and how the EUR 100M / 500M thresholds interact with leverage rules, see [INTERNAL-LINK: sub-threshold AIFM for crypto in Estonia → /blog/sub-threshold-aifm-crypto-estonia].

## Registration steps with Finantsinspektsioon

The Estonian sub-threshold AIFM registration process follows seven structured steps. Each is documented in the EFSA's [licensing guidance](https://www.fi.ee/en/finantsinspektsioon-0/finantsinspektsiooni-tegevus/finantssektori-aktsiaseltsi-tegevuslubade-taotlemine).

1. **Choose the legal vehicle for the AIFM.** An *osaühing* (private limited company, OÜ) is the standard form. The AIFM must be incorporated in Estonia and have a registered office.
2. **Set up the Estonian commercial register entry.** This is done electronically via [Ariregister](https://ariregister.rik.ee/eng) and requires a board, share capital deposit, and signed articles of association.
3. **Obtain a Legal Entity Identifier (LEI).** Apply through any [GLEIF-accredited LOU](https://www.gleif.org/en/about-lei/get-an-lei-find-lei-issuing-organizations).
4. **Prepare and submit the Small Fund Manager registration dossier.** The dossier covers: business plan, AUM projections, organisational structure, fit-and-proper documentation for board members and key function holders, AML/CFT framework with designated MLRO, conflict-of-interest policy, and outsourcing arrangements.
5. **Set up the AIF documentation in parallel.** The fund itself (the *usaldusfond* limited partnership in most cases) needs its own formation, partnership agreement, investment policy document (PPM equivalent), subscription agreement template, and depositary appointment.
6. **Complete the EFSA pre-launch review.** Once the dossier is submitted, EFSA conducts iterative review — typically 2-3 rounds of clarifications. This is where 30-60 days becomes 60-90 if the dossier is incomplete on first submission.
7. **Banking and custody onboarding.** This runs in parallel with steps 4-6 but typically becomes the gating item. Local Estonian banks have variable appetite for crypto-AIFM accounts; SEPA-EU banks are usually the practical solution.

For a deeper step-by-step walkthrough including documentation templates, see [INTERNAL-LINK: how to launch a crypto fund in Estonia → /blog/how-to-launch-a-crypto-fund-estonia].

## Capital requirements and the *usaldusfond* vehicle

The fund vehicle most commonly used for AIFs in Estonia is the *usaldusfond* — a limited partnership structured under [Estonian Investment Funds Act §90 et seq.](https://www.riigiteataja.ee/en/eli/ee/Riigikogu/act/512012017002/consolide). It mirrors the Luxembourg SCSp and the Irish ICAV in function: a partnership with a general partner (the AIFM or its nominee) and limited partners (the investors).

**Capital structure.** Investors subscribe through commitment agreements, with capital drawn down as needed. The partnership is tax-transparent at the Estonian level — fund-level taxation is generally pass-through. Distributions are taxed at the investor level under their residence-state rules.

**AIFM capital requirement.** Sub-threshold AIFMs must hold EUR 25,000 minimum own funds at registration. Fully authorised AIFMs require EUR 125,000 plus 0.02% of AUM exceeding EUR 250 million. Both must hold professional indemnity insurance (PII) or additional own funds — typically PII at coverage levels of EUR 500K-1M for sub-threshold managers.

**Investor minimum subscription.** The market-standard minimum for AIFs in Estonia is EUR 50,000 — the same threshold SparkCore applies — but there's no statutory floor under AIFMD itself. The minimum is set by the fund's own documentation and the regulator's expectations on professional-investor restriction.

> **Citation capsule:** AIFMD reserves AIFs primarily for "professional investors" defined in MiFID II Annex II. Distribution to retail investors requires either a UCITS structure or member-state-specific retail-AIF rules — neither applies to crypto-asset funds in practice ([EUR-Lex, AIFMD Article 43](https://eur-lex.europa.eu/eli/dir/2011/61/oj), 2011).

## MiCA + AIFMD: how the two regimes interact

MiCA ([Regulation (EU) 2023/1114](https://eur-lex.europa.eu/eli/reg/2023/1114/oj), 2023) entered full effect on 30 December 2024 and overlays AIFMD for any service involving crypto-assets. The interaction is not symmetric: AIFMs sit *above* MiCA in the regulatory stack, but only if they're fully authorised under AIFMD Article 6.

**Article 60 notification (fully authorised AIFMs).** A fully authorised AIFM can provide crypto-asset portfolio management to its AIFs and to discretionary clients without obtaining a separate CASP authorisation, by filing a notification with its home regulator at least 40 working days before commencing the service. The home regulator can object during the window; absence of objection equals deemed authorisation.

**No Article 60 for sub-threshold AIFMs.** AIFMD Article 60(5) explicitly excludes sub-threshold registered AIFMs from the notification pathway. A sub-threshold AIFM that wants to provide crypto portfolio management to *external* clients (outside its own AIFs) must obtain a standalone CASP licence under MiCA. Managing the AIFs themselves does not require CASP — the AIF is the fund, not a client receiving a service.

**Custody must go through a MiCA-licensed CASP.** AIFMD Article 21 mandates depositary appointment; for crypto-assets, the depositary must be a CASP authorised to safekeep crypto-assets. This is where the operational stack becomes hands-on: CASP custodians with EU authorisation are still relatively few, and onboarding processes can take 6-8 weeks.

For the full MiCA-CASP framework as it applies to crypto fund managers, see [INTERNAL-LINK: do crypto fund managers need a MiCA CASP licence → /blog/do-crypto-fund-managers-need-mica-casp-license].

## White-label vs in-house AIFM: when delegation makes sense

For emerging managers, the decision between obtaining their own AIFM authorisation and using a white-label AIFM is structural. Both routes are legitimate; the trade-off is control vs cost-and-speed.

**In-house AIFM.** The manager incorporates and registers its own Estonian AIFM. Full control over the regulatory entity, board composition, compliance function, and brand positioning. The manager carries the licence and the supervisory burden. Investment: capital + 30-60 days + ongoing compliance overhead (MLRO, reporting, audit).

**White-label AIFM.** The manager partners with an existing authorised or registered AIFM that hosts the AIF on its regulatory licence. The manager focuses on investment strategy and distribution; the host AIFM provides the regulatory shell, fund documentation templates, depositary relationships, and EFSA reporting. Setup cycle compresses to ~30 days, with proportionately lower upfront cost. Trade-off: the manager doesn't carry its own AIFM brand and shares the regulatory stack with the host.

The white-label model is well-suited to managers running their first fund with a defined exit strategy (e.g., raise a track record, then internalise the AIFM at the next strategy launch). For managers with multiple strategies in pipeline, the in-house AIFM amortises faster.

For more on the white-label approach, see [INTERNAL-LINK: white-label crypto fund manager services → /blog/white-label-crypto-fund-manager-services] and [INTERNAL-LINK: what an alternative investment fund platform does → /blog/what-an-alternative-investment-fund-platform-does].

## Investor eligibility and minimum subscription

EU AIFs are restricted to professional investors as defined in [MiFID II Annex II](https://eur-lex.europa.eu/eli/dir/2014/65/oj). Three categories qualify by default: institutional clients, large undertakings meeting two of three balance-sheet criteria, and national/regional governments. Other investors can opt up to "elective professional" status by demonstrating sufficient experience and assets under EUR 500,000+ (some member states require higher).

In practice, for a crypto AIF with a EUR 50,000 minimum subscription, investors fall into three groups:

- **Family offices and high-net-worth individuals** (elective professional status, signed sophistication declaration)
- **Funds of funds and fund-of-one structures** (professional by category)
- **Treasury allocations from operating companies** (professional if the company meets MiFID II large-undertaking criteria)

Marketing to non-professional investors is prohibited. This shapes distribution strategy heavily: digital advertising must be gated by qualified-investor verification; pitch decks must include MiFID II eligibility language; subscription documents must capture the investor's sophistication declaration.

For a deeper dive on the qualified-investor framework, see [INTERNAL-LINK: crypto fund for qualified investors → /blog/crypto-fund-for-qualified-investors].

## Fund strategies that fit the regulated crypto AIF wrapper

The AIFMD wrapper is strategy-agnostic. Crypto fund managers in the EU run AIFs across the full strategy spectrum — directional, arbitrage, market-neutral, options-based, and venture-style.

The strategies that fit the regulated wrapper best are those whose risk and return profile can be documented in a fund's investment policy and reported quarterly to the regulator. Pure directional Bitcoin holding is permitted but typically structured to add value beyond passive exposure (basis trades, hedged tactical allocation). Higher-frequency strategies (HFT, MEV) are operationally challenging within the depositary framework but not categorically excluded.

For strategy-specific deep dives, see:

- [INTERNAL-LINK: what a market-neutral crypto fund does → /blog/what-a-market-neutral-crypto-fund-does]
- [INTERNAL-LINK: delta-neutral crypto strategies explained → /blog/delta-neutral-crypto-strategies-explained]
- [INTERNAL-LINK: crypto arbitrage investment fund → /blog/crypto-arbitrage-investment-fund]
- [INTERNAL-LINK: bitcoin outperformance strategy fund → /blog/bitcoin-outperformance-strategy-fund]
- [INTERNAL-LINK: what an institutional crypto fund manager does → /blog/what-an-institutional-crypto-fund-manager-does]

## Operational reality: timelines, costs, ongoing compliance

Once registered, the AIFM's annual cycle is structured around four recurring obligations:

**Quarterly NAV calculation and reporting.** The depositary or fund administrator computes NAV at least quarterly (some funds compute monthly for investor reporting). The AIFM signs off and reports to investors.

**Annual audited financial statements.** Both the AIFM and each AIF require an audit by a registered auditor. KPMG, PwC, EY and BDO have meaningful Estonian crypto-AIFM practices.

**EFSA reporting.** Sub-threshold AIFMs file an annual reporting return covering AUM, fund counts, key personnel, and material changes. Fully authorised AIFMs file the more comprehensive AIFMD Annex IV report quarterly to the home regulator.

**AML/CFT supervision.** The MLRO files suspicious-activity reports to the [Estonian Financial Intelligence Unit](https://fiu.ee/en) as required, and the AIFM completes annual AML risk-assessment refreshes.

Ongoing costs for a sub-threshold Estonian AIFM running 1-3 AIFs typically land in the EUR 60,000-120,000 / year range (audit + legal + admin + supervision fees + MLRO outsourcing). Fully authorised AIFMs are 3-5x that, scaling with AUM.

For the full operational view of what a regulated crypto fund manager does day-to-day, see [INTERNAL-LINK: regulated crypto fund manager in Estonia → /blog/regulated-crypto-fund-manager-estonia].

## How SparkCore is structured (a worked example)

SparkCore.investment OÜ is the **AIFM** — an Estonian *osaühing* registered with Finantsinspektsioon as a Small Fund Manager (Estonian commercial registry 16265864, LEI [8945003BBN0RVNNB0S84](https://search.gleif.org/#/record/8945003BBN0RVNNB0S84)). It holds an EFIU Financial Institution licence for AML supervision. KPMG Estonia audits the AIFM and the funds.

The **AIFs** under that AIFM are three Estonian *usaldusfond* limited partnerships, each with its own fund documentation, NAV calculation, and investor register:

- **Dynamic Trends** — directional crypto exposure targeting Bitcoin outperformance, operational since August 2025
- **CryptoVision** — algorithmic defensive strategy with controlled volatility, operational since 2021
- **Equinoxe** — market-neutral (delta-neutral and beta-neutral), planned launch 2026

Investor subscriptions go to a specific AIF — not to "SparkCore" in the abstract. Minimum subscription is EUR 50,000 across funds, with a 1-year minimum commitment, 0% entry/exit fees, 2% annual management fee, and 20% performance fee with High Water Mark calculated quarterly.

<!-- [PERSONAL EXPERIENCE] -->
The two-layer structure (AIFM + AIFs) shows up in every due-diligence call. Family offices ask "are you regulated?" — meaning the AIFM. Then they ask "what does the fund hold and how is performance calculated?" — meaning the AIF. Both answers matter, and the operational discipline of keeping them distinct is what makes the regulated wrapper credible to institutional capital. The licence is on the AIFM. The portfolio is in the AIF. The reporting flows from both, with separate sign-off chains.

> **Citation capsule:** SparkCore's regulatory entry is publicly verifiable on the EFSA register at [fi.ee — SparkCore.investment OÜ](https://www.fi.ee/en/guides/fund-management-companies/investment-market/small-fund-managers-without-activity-licence/sparkcoreinvestment-ou) and on the GLEIF register at [search.gleif.org — LEI 8945003BBN0RVNNB0S84](https://search.gleif.org/#/record/8945003BBN0RVNNB0S84). Public verifiability is one of the operational signals that distinguishes a regulated AIF from a non-regulated crypto vehicle.

## Frequently asked questions

### Is Estonia still a viable jurisdiction for crypto fund managers post-MiCA?

Yes. Estonia remains the lowest-cost EU pathway for sub-threshold AIFMs and a credible jurisdiction for full authorisation. The legacy VASP regime is being retired (all legacy VASP licences expire 1 July 2026), but the EFSA now applies full MiCA standards with growing implementation experience. Firms choosing Estonia today get a regulator with crypto-specific expertise, not a regulatory shortcut.

### What's the fastest realistic timeline from incorporation to first investor subscription?

A sub-threshold AIFM with white-label fund delegation can reach first subscription in approximately 60-90 days end-to-end: 30-45 days for fund documentation and EFSA dossier, 30-45 days for banking and custody onboarding, with overlap on critical-path items. An in-house AIFM build with no delegation typically takes 4-6 months. Full AIFMD authorisation is 6-9+ months.

### Do I need to be physically based in Estonia to run an AIFM there?

No, but you need substantive presence. The AIFM must be incorporated in Estonia and have a registered office, board with required Estonian-tax-residence members, and demonstrable substance (decision-making, key personnel, technical infrastructure). Pure paper substance does not satisfy the EFSA. Estonia's e-Residency programme facilitates non-resident foundership, but operational substance must be real.

### How does AIFMD II affect crypto fund managers?

AIFMD II ([Directive (EU) 2024/927](https://eur-lex.europa.eu/eli/dir/2024/927/oj), 2024) tightens delegation rules, expands liquidity-management tooling requirements, and modestly increases sub-threshold reporting. National transposition deadline is 16 April 2026. For crypto fund managers, the practical changes are limited; the regime architecture stays the same.

### Can I market the fund to investors in other EU member states?

A fully authorised AIFM passports its AIFs to professional investors across all EU/EEA member states under AIFMD Article 32, with member-state notification. A sub-threshold AIFM does not have the passport — distribution outside Estonia requires either reverse solicitation or member-state-specific national private placement regimes (NPPR). Practical reach for sub-threshold AIFMs is meaningful but not pan-EU automatic.

### What's the difference between the AIF and an ETF, in plain terms?

An AIF is a regulated fund vehicle for professional investors with quarterly liquidity and active management; an ETF is a publicly listed product with daily trading, retail access, and (for spot crypto ETFs) tracking-only exposure. The two serve different investors, with different distribution rules and different operational stacks. For the side-by-side, see [INTERNAL-LINK: crypto fund vs ETF → /blog/crypto-fund-vs-etf].

## Conclusion

A regulated crypto fund in Estonia is a deliberate operational choice with a well-defined cost, timeline, and supervisory framework. The country offers the EU's lowest-cost AIFM entry, a digitally-native administrative stack, and a regulator with growing crypto-MiCA implementation depth. For emerging managers, the sub-threshold regime under AIFMD Article 3(2) provides a 30-60 day path to market with EUR 25,000 capital — orders of magnitude lighter than full authorisation, with the option to upgrade as AUM grows.

The architecture is two-layer: AIFM + AIF. MiCA overlays for crypto-asset services. Custody goes through a MiCA-licensed CASP. Distribution is restricted to professional investors. None of this is optional, and getting any of it wrong undermines the entire regulatory premise.

For the deeper articles in this cluster, jump into the area you need next:

- [INTERNAL-LINK: regulated crypto fund manager in Estonia → /blog/regulated-crypto-fund-manager-estonia]
- [INTERNAL-LINK: how to launch a crypto fund in Estonia → /blog/how-to-launch-a-crypto-fund-estonia]
- [INTERNAL-LINK: sub-threshold AIFM for crypto in Estonia → /blog/sub-threshold-aifm-crypto-estonia]
- [INTERNAL-LINK: do crypto fund managers need a MiCA CASP licence → /blog/do-crypto-fund-managers-need-mica-casp-license]
- [INTERNAL-LINK: AIF vs AIFM explained → /blog/aif-vs-aifm-crypto-explained]
- [INTERNAL-LINK: what is a crypto AIFM → /blog/what-is-a-crypto-aifm]
- [INTERNAL-LINK: white-label crypto fund manager services → /blog/white-label-crypto-fund-manager-services]
- [INTERNAL-LINK: crypto fund for qualified investors → /blog/crypto-fund-for-qualified-investors]
- [INTERNAL-LINK: Estonia vs Luxembourg vs Malta for crypto funds → /blog/estonia-luxembourg-malta-crypto-fund]
- [INTERNAL-LINK: crypto fund vs ETF → /blog/crypto-fund-vs-etf]

## Sources

- European Parliament & Council, *Directive 2011/61/EU on Alternative Investment Fund Managers (AIFMD)*, retrieved 2026-05-06: https://eur-lex.europa.eu/eli/dir/2011/61/oj
- European Parliament & Council, *Directive (EU) 2024/927 amending Directive 2011/61/EU (AIFMD II)*, retrieved 2026-05-06: https://eur-lex.europa.eu/eli/dir/2024/927/oj
- European Parliament & Council, *Regulation (EU) 2023/1114 on Markets in Crypto-Assets (MiCA)*, retrieved 2026-05-06: https://eur-lex.europa.eu/eli/reg/2023/1114/oj
- European Parliament & Council, *Directive 2014/65/EU on Markets in Financial Instruments (MiFID II)*, retrieved 2026-05-06: https://eur-lex.europa.eu/eli/dir/2014/65/oj
- Riigi Teataja, *Estonian Investment Funds Act (Investeerimisfondide seadus)*, retrieved 2026-05-06: https://www.riigiteataja.ee/en/eli/ee/Riigikogu/act/512012017002/consolide
- Finantsinspektsioon, *Small Fund Managers Without Activity Licence — guidance and registry*, retrieved 2026-05-06: https://www.fi.ee/en/guides/fund-management-companies/investment-market/small-fund-managers-without-activity-licence
- Finantsinspektsioon, *SparkCore.investment OÜ entry on Small Fund Managers register*, retrieved 2026-05-06: https://www.fi.ee/en/guides/fund-management-companies/investment-market/small-fund-managers-without-activity-licence/sparkcoreinvestment-ou
- GLEIF, *SparkCore Investment OÜ (LEI 8945003BBN0RVNNB0S84)*, retrieved 2026-05-06: https://search.gleif.org/#/record/8945003BBN0RVNNB0S84
- Estonian Financial Intelligence Unit, *Reporting and supervision*, retrieved 2026-05-06: https://fiu.ee/en

## Risk Disclaimer

This guide is provided for informational purposes only and does not constitute investment advice, regulatory advice, a solicitation, or an offer to invest. Investing in crypto-asset funds involves significant risk, including the possible loss of all capital invested. Past performance does not guarantee future results. Regulatory frameworks evolve; readers should verify current rules with their national regulator and qualified legal counsel before relying on any specific position taken in this article. SparkCore.investment OÜ is registered as a small alternative investment fund manager with the Estonian Financial Supervision Authority ([Finantsinspektsioon](https://www.fi.ee/)). This content is intended for professional and qualified investors only.
