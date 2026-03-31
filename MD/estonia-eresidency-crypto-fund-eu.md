---
title: "Can Estonia e-Residency Help You Launch a Crypto Fund?"
description: "Estonia e-Residency lets you register an OÜ in one day, but a CASP license requires €100K capital and FSA authorization. Full 2025–2026 roadmap for crypto fund managers."
date: "2026-03-29"
lastUpdated: "2026-03-29"
author: "Neutralis Finance"
tags: ["Estonia e-residency crypto fund", "Estonia crypto license", "AIFM crypto fund EU", "MiCA CASP license Estonia", "e-Residency OÜ company", "launch crypto fund Europe"]
og_title: "Can Estonia e-Residency Help You Launch a Crypto Fund?"
og_description: "Full guide to Estonia e-residency crypto fund structures: CASP vs AIFM, MiCA 2026 deadline, capital requirements, and step-by-step FSA authorization."
og_image: "/images/estonia-eresidency-crypto-fund-og.jpg"
og_type: "article"
canonical: "https://neutralis.finance/fr/insights/estonia-eresidency-crypto-fund-eu"
---

# Can Estonia e-Residency Help You Launch a Crypto Fund?

Estonia's **e-Residency** program gets a lot of attention from crypto entrepreneurs researching an **Estonia e-residency crypto fund** structure. Over 132,000 people from 185 countries have applied for a digital ID card that lets them register and run an EU company entirely online ([e-resident.gov.ee, 2025](https://www.e-resident.gov.ee)). The appeal is obvious: EU legitimacy, digital-first processes, and no flights required.

But there's a gap between what e-Residency delivers and what crypto fund managers actually need. Registering an Estonian company is step one. Getting the regulatory authorizations to legally manage third-party capital, operate a crypto exchange, or custody client assets is a separate, multi-month process with meaningful capital requirements. The two are often conflated. That conflation can lead operators to believe they're compliant when they're not.

This guide maps the full architecture: what e-Residency actually provides, how Estonia's company structure works, which of three distinct regulatory tracks applies to your business model, and how the new MiCA framework changes everything by July 1, 2026. The goal is a clear, honest picture so you can make an informed decision before spending money on applications.


---

> **Key Takeaways**
> - e-Residency lets you register an Estonian OÜ remotely but does NOT grant physical EU presence, tax residency, or a passport
> - Running a crypto exchange or custody service requires a CASP license from Estonia's FSA (€3,000 application fee, €100K–€250K min. capital)
> - Managing pooled third-party capital requires an AIFM authorization and a separate LPF entity, not a CASP license
> - The July 1, 2026 MiCA transition deadline is a hard cutoff: existing FIU-registered VASPs must fully reapply or shut down ([fi.ee, 2025](https://www.fi.ee/en/investeerimine/investeerimisvaldkonna-tegevuslubade-taotlemine/kruptovaraturu-tegevusluba))

---

## What Estonia e-Residency Actually Is (and Isn't)

Estonia e-Residency is a government-issued digital identity that lets non-citizens register and manage an Estonian company fully online. It does not grant physical residency, EU citizenship, tax residency in Estonia, or the right to work in Estonia. More than 132,000 people from 185 countries hold an e-Residency card, and the program has contributed a cumulative €342 million in direct economic impact since 2014 ([e-resident.gov.ee, 2025](https://www.e-resident.gov.ee); [Invest in Estonia, H1 2025](https://investinestonia.com)).


### What e-Residency Gives You

The e-Residency card is, at its core, a digital signature tool. It lets you:

- Sign documents and contracts electronically with legal weight in the EU
- Register and manage an Estonian company (OÜ) through the Company Registration Portal
- Submit filings to Estonian state registries digitally
- Access Estonian business banking and fintech services remotely
- Act as a director or shareholder of record in an Estonian legal entity

### What e-Residency Does NOT Give You

This list is where most entrepreneurs get into trouble. e-Residency explicitly does not provide:

- **Physical residency** in Estonia or anywhere in the EU
- **EU passport or visa rights** of any kind
- **Estonian tax residency**: you pay taxes where you actually live ([emta.ee, 2025](https://www.emta.ee))
- **The right to work** in Estonia or the EU
- **Regulatory substance**: required by both the CASP and AIFM authorization regimes

That last point is the critical one for crypto fund managers. Both major regulatory pathways in Estonia require your company to have genuine physical presence in the country. An e-Residency card alone does not satisfy that requirement.

<!-- [UNIQUE INSIGHT] -->
Most guides covering Estonia e-Residency treat it as a near-complete solution for crypto business formation. The practical reality is different. The e-Residency card solves the administrative problem of company registration. It does nothing for the regulatory problem of authorization. Conflating the two has led a number of operators to register companies in Estonia and begin marketing crypto services without realizing they lack the required license.

> **Citation capsule:** Estonia's e-Residency program has issued cards to more than 132,000 individuals from 185 countries as of 2025, generating €342 million in cumulative economic impact since its 2014 launch. The program enables digital company registration and electronic document signing within the EU, but explicitly does not confer physical residency, EU citizenship, tax residency, or the right to work in Estonia. ([e-resident.gov.ee, 2025](https://www.e-resident.gov.ee); [Invest in Estonia, H1 2025](https://investinestonia.com))

---

## Registering an Estonian OÜ: The Starting Point

An Estonian **OÜ** (osaühing, or private limited company) is the standard entity type for e-residents. It can be registered online in approximately one business day through the Company Registration Portal, with a state fee of €265 ([learn.e-resident.gov.ee, 2025](https://learn.e-resident.gov.ee)). More than 38,500 companies have been registered by e-residents since the program launched ([e-resident.gov.ee, 2025](https://www.e-resident.gov.ee)).

<figure>
<svg viewBox="0 0 680 320" xmlns="http://www.w3.org/2000/svg" font-family="system-ui, sans-serif" role="img" aria-label="Grouped bar chart showing Estonia e-Residency new applications and new companies registered per year from 2022 to H1 2025">
  <title>Estonia e-Residency Growth: New Applications vs. New Companies (2022–H1 2025)</title>
  <!-- Background -->
  <rect width="680" height="320" fill="#0f1117" rx="10"/>
  <text x="340" y="26" text-anchor="middle" font-size="13" font-weight="700" fill="#e2e8f0">e-Residency Growth: New Applications vs. New Companies</text>
  <!-- Y-axis -->
  <line x1="80" y1="240" x2="640" y2="240" stroke="#2d3148" stroke-width="1.5"/>
  <line x1="80" y1="50" x2="80" y2="240" stroke="#2d3148" stroke-width="1.5"/>
  <!-- Y-axis labels -->
  <text x="72" y="244" text-anchor="end" font-size="9" fill="#718096">0</text>
  <text x="72" y="194" text-anchor="end" font-size="9" fill="#718096">4,000</text>
  <text x="72" y="144" text-anchor="end" font-size="9" fill="#718096">8,000</text>
  <text x="72" y="94" text-anchor="end" font-size="9" fill="#718096">12,000</text>
  <text x="72" y="60" text-anchor="end" font-size="9" fill="#718096">16,000</text>
  <!-- Grid lines -->
  <line x1="80" y1="194" x2="640" y2="194" stroke="#1e2235" stroke-width="1"/>
  <line x1="80" y1="144" x2="640" y2="144" stroke="#1e2235" stroke-width="1"/>
  <line x1="80" y1="94" x2="640" y2="94" stroke="#1e2235" stroke-width="1"/>
  <!-- Scale: 16,000 = 190px height; 1,000 = 11.875px -->
  <!-- 2022 Group: 14,000 apps = 166px; 4,000 companies = 47.5px -->
  <rect x="110" y="74" width="30" height="166" fill="#4a90d9" rx="2"/>
  <rect x="145" y="193" width="30" height="47" fill="#7bc8a4" rx="2"/>
  <text x="137" y="258" text-anchor="middle" font-size="10" fill="#a0aec0">2022</text>
  <!-- 2023 Group: 14,500 apps = 172px; 4,500 companies = 53.4px -->
  <rect x="250" y="68" width="30" height="172" fill="#4a90d9" rx="2"/>
  <rect x="285" y="187" width="30" height="53" fill="#7bc8a4" rx="2"/>
  <text x="277" y="258" text-anchor="middle" font-size="10" fill="#a0aec0">2023</text>
  <!-- 2024 H1 Group: 6,500 apps = 77px; 2,440 companies = 29px -->
  <rect x="390" y="163" width="30" height="77" fill="#4a90d9" rx="2" opacity="0.75"/>
  <rect x="425" y="211" width="30" height="29" fill="#7bc8a4" rx="2" opacity="0.75"/>
  <text x="417" y="258" text-anchor="middle" font-size="10" fill="#a0aec0">2024 H1</text>
  <!-- 2025 H1 Group: 7,994 apps = 95px; 2,634 companies = 31px -->
  <rect x="520" y="145" width="30" height="95" fill="#4a90d9" rx="2" opacity="0.75"/>
  <rect x="555" y="209" width="30" height="31" fill="#7bc8a4" rx="2" opacity="0.75"/>
  <text x="547" y="258" text-anchor="middle" font-size="10" fill="#a0aec0">2025 H1</text>
  <!-- Value labels on bars -->
  <text x="125" y="70" text-anchor="middle" font-size="8" fill="#4a90d9">14,000</text>
  <text x="160" y="189" text-anchor="middle" font-size="8" fill="#7bc8a4">4,000</text>
  <text x="265" y="64" text-anchor="middle" font-size="8" fill="#4a90d9">14,500</text>
  <text x="300" y="183" text-anchor="middle" font-size="8" fill="#7bc8a4">4,500</text>
  <text x="405" y="159" text-anchor="middle" font-size="8" fill="#4a90d9">6,500</text>
  <text x="440" y="207" text-anchor="middle" font-size="8" fill="#7bc8a4">2,440</text>
  <text x="535" y="141" text-anchor="middle" font-size="8" fill="#4a90d9">7,994</text>
  <text x="570" y="205" text-anchor="middle" font-size="8" fill="#7bc8a4">2,634</text>
  <!-- Legend -->
  <rect x="200" y="278" width="12" height="10" fill="#4a90d9"/>
  <text x="216" y="287" font-size="9" fill="#a0aec0">New e-Residency applications</text>
  <rect x="400" y="278" width="12" height="10" fill="#7bc8a4"/>
  <text x="416" y="287" font-size="9" fill="#a0aec0">New companies registered</text>
  <!-- Footer -->
  <text x="340" y="308" text-anchor="middle" font-size="8" fill="#4a5568">Sources: Invest in Estonia / e-resident.gov.ee (2025). H1 figures are half-year only.</text>
</svg>
<figcaption>Estonia e-Residency program growth from 2022 through H1 2025. Applications recovered to 7,994 in the first half of 2025, with 2,634 new companies registered in the same period. Sources: Invest in Estonia; e-resident.gov.ee, 2025.</figcaption>
</figure>

The OÜ structure is genuinely simple to set up. The online incorporation process takes minutes if your documents are in order. There is no minimum share capital requirement for a standard OÜ (the minimum is €0.01 per share), though regulatory applications will require you to demonstrate adequate capital later.

### What You Need Beyond the State Fee

The €265 registration fee is just the beginning. Operating a compliant OÜ requires:

- **Registered local address**: €200–400 per year from a registered address provider
- **A contact person** (Estonian resident): required if no board member lives in Estonia
- **Accounting and bookkeeping**: Estonian law requires annual financial reporting
- **Business banking**: Estonian banks or EU fintech institutions

Realistic setup costs for a basic OÜ, including legal address, a service agent, and initial accounting, run €700–€1,300 in year one ([multiple Estonian registrars, 2025](https://learn.e-resident.gov.ee)).

### What Registering an OÜ Does Not Authorize

This is the gap many operators miss. An OÜ is a legal container. It lets you sign contracts, open bank accounts, and employ people. It does not authorize you to:

- Operate a crypto exchange, custody service, or brokerage
- Manage pooled third-party investment capital
- Offer crypto investment advice as a regulated service

Those activities require separate FSA authorizations, which we cover in the next section.

---

## Three Regulatory Tracks for Crypto Operators in Estonia

Estonia now offers three distinct regulatory pathways for crypto-related businesses, each serving a fundamentally different business model. Choosing the wrong track (say, getting a CASP license when you need an AIFM authorization) means you are not legally permitted to do what you intend. The FSA does not treat these licenses as interchangeable ([fi.ee, 2025](https://www.fi.ee/en/investeerimine/investeerimisvaldkonna-tegevuslubade-taotlemine/kruptovaraturu-tegevusluba)).

[CHART: Regulatory Track Comparison Table SVG - see below]

<figure>
<svg viewBox="0 0 760 280" xmlns="http://www.w3.org/2000/svg" font-family="system-ui, sans-serif" role="img" aria-label="Comparison table of three Estonian crypto regulatory tracks: CASP, AIFM, and MiFID II">
  <title>Estonia Crypto Regulatory Tracks: CASP vs AIFM vs MiFID II</title>
  <!-- Background -->
  <rect width="760" height="280" fill="#0f1117" rx="10"/>
  <!-- Header row -->
  <rect x="0" y="0" width="760" height="40" fill="#1a1d2e" rx="10"/>
  <rect x="0" y="30" width="760" height="10" fill="#1a1d2e"/>
  <text x="90" y="25" text-anchor="middle" font-size="11" font-weight="700" fill="#a0aec0">TRACK</text>
  <text x="235" y="25" text-anchor="middle" font-size="11" font-weight="700" fill="#a0aec0">LICENSE</text>
  <text x="370" y="25" text-anchor="middle" font-size="11" font-weight="700" fill="#a0aec0">REGULATOR</text>
  <text x="510" y="25" text-anchor="middle" font-size="11" font-weight="700" fill="#a0aec0">MIN. CAPITAL</text>
  <text x="665" y="25" text-anchor="middle" font-size="11" font-weight="700" fill="#a0aec0">BEST FOR</text>
  <!-- Divider lines -->
  <line x1="155" y1="0" x2="155" y2="280" stroke="#2d3148" stroke-width="1"/>
  <line x1="310" y1="0" x2="310" y2="280" stroke="#2d3148" stroke-width="1"/>
  <line x1="440" y1="0" x2="440" y2="280" stroke="#2d3148" stroke-width="1"/>
  <line x1="580" y1="0" x2="580" y2="280" stroke="#2d3148" stroke-width="1"/>
  <!-- Row 1: CASP -->
  <rect x="0" y="40" width="760" height="70" fill="#141728"/>
  <rect x="0" y="40" width="4" height="70" fill="#4a90d9"/>
  <text x="90" y="65" text-anchor="middle" font-size="12" font-weight="700" fill="#4a90d9">Track 1</text>
  <text x="90" y="83" text-anchor="middle" font-size="11" fill="#e2e8f0">CASP (MiCA)</text>
  <text x="235" y="65" text-anchor="middle" font-size="11" fill="#e2e8f0">CASP Authorization</text>
  <text x="235" y="83" text-anchor="middle" font-size="10" fill="#718096">(Finantsinspektsioon)</text>
  <text x="370" y="65" text-anchor="middle" font-size="11" fill="#e2e8f0">Estonia FSA</text>
  <text x="510" y="65" text-anchor="middle" font-size="11" fill="#e2e8f0">€100K–€250K</text>
  <text x="510" y="83" text-anchor="middle" font-size="10" fill="#718096">(by service class)</text>
  <text x="665" y="65" text-anchor="middle" font-size="11" fill="#e2e8f0">Exchange, custody,</text>
  <text x="665" y="83" text-anchor="middle" font-size="11" fill="#e2e8f0">brokerage services</text>
  <!-- Row 2: AIFM -->
  <rect x="0" y="110" width="760" height="70" fill="#0f1117"/>
  <rect x="0" y="110" width="4" height="70" fill="#7bc8a4"/>
  <text x="90" y="135" text-anchor="middle" font-size="12" font-weight="700" fill="#7bc8a4">Track 2</text>
  <text x="90" y="153" text-anchor="middle" font-size="11" fill="#e2e8f0">AIFM / Small AIF</text>
  <text x="235" y="135" text-anchor="middle" font-size="11" fill="#e2e8f0">AIFM Authorization</text>
  <text x="235" y="153" text-anchor="middle" font-size="10" fill="#718096">or Registration</text>
  <text x="370" y="135" text-anchor="middle" font-size="11" fill="#e2e8f0">Estonia FSA</text>
  <text x="510" y="135" text-anchor="middle" font-size="11" fill="#e2e8f0">€25K (small AIFM)</text>
  <text x="510" y="153" text-anchor="middle" font-size="10" fill="#718096">€125K (full AIFM)</text>
  <text x="665" y="135" text-anchor="middle" font-size="11" fill="#e2e8f0">Pooled crypto fund</text>
  <text x="665" y="153" text-anchor="middle" font-size="11" fill="#e2e8f0">management (LPs)</text>
  <!-- Row 3: MiFID II -->
  <rect x="0" y="180" width="760" height="70" fill="#141728"/>
  <rect x="0" y="180" width="4" height="70" fill="#f5a623"/>
  <text x="90" y="205" text-anchor="middle" font-size="12" font-weight="700" fill="#f5a623">Track 3</text>
  <text x="90" y="223" text-anchor="middle" font-size="11" fill="#e2e8f0">MiFID II (CySEC)</text>
  <text x="235" y="205" text-anchor="middle" font-size="11" fill="#e2e8f0">CIF Authorization</text>
  <text x="235" y="223" text-anchor="middle" font-size="10" fill="#718096">(Cyprus, not Estonia)</text>
  <text x="370" y="205" text-anchor="middle" font-size="11" fill="#e2e8f0">CySEC (Cyprus)</text>
  <text x="510" y="205" text-anchor="middle" font-size="11" fill="#e2e8f0">€125K–€730K</text>
  <text x="510" y="223" text-anchor="middle" font-size="10" fill="#718096">(by service type)</text>
  <text x="665" y="205" text-anchor="middle" font-size="11" fill="#e2e8f0">Derivatives, futures,</text>
  <text x="665" y="223" text-anchor="middle" font-size="11" fill="#e2e8f0">regulated instruments</text>
  <!-- Footer -->
  <text x="380" y="265" text-anchor="middle" font-size="9" fill="#4a5568">Sources: fi.ee (2025); esma.europa.eu; CoinTelegraph (June 2025)</text>
</svg>
<figcaption>Three regulatory tracks for crypto operators in Estonia and the EU. Track selection depends on whether you provide services to clients (CASP) or manage pooled investor capital (AIFM). MiFID II via CySEC is the relevant path for derivatives-heavy strategies based in Cyprus.</figcaption>
</figure>

### Track 1: CASP License - For Crypto Service Providers

A **CASP (Crypto-Asset Service Provider)** authorization under the Markets in Crypto-Assets Regulation (MiCA) covers operating a crypto exchange, providing custody of crypto assets, executing orders on behalf of clients, or offering crypto-asset transfer services. This is the license for businesses that serve customers, not for fund managers.

Key parameters under Estonia's FSA regime ([fi.ee, 2025](https://www.fi.ee/en/investeerimine/investeerimisvaldkonna-tegevuslubade-taotlemine/kruptovaraturu-tegevusluba)):

- **Application fee**: €3,000 (non-refundable)
- **Minimum capital**: €100,000 for Class 2 services (custody and exchange); up to €250,000 for transfer services ([Hacken, 2025](https://hacken.io/discover/casp-license-estonia/))
- **Review timeline**: 25 working days for completeness check, plus 40 working days for substantive assessment
- **Key benefit**: EU-wide passporting under MiCA Article 65. Once authorized in Estonia, you can passport services to all 27 EU member states ([esma.europa.eu](https://www.esma.europa.eu))

### Track 2: AIFM Authorization - For Fund Managers

An **AIFM (Alternative Investment Fund Manager)** authorization is what you need if you manage pooled capital on behalf of investors. This is legally required the moment you accept funds from multiple investors and make investment decisions on their behalf. A CASP license does not cover this activity.

The AIFM route requires two entities in Estonia:

- **An OÜ** as the fund management company, registered as a small AIFM with the FSA
- **An LPF (Limited Partnership Fund)** as the investment vehicle, registered in the Commercial Register

The **small AIFM** (sub-threshold) registration applies if your AUM stays below €100 million for leveraged strategies or €500 million for unleveraged, closed-ended strategies with five-year-plus lock-ups ([AIFMD Article 3, EUR-Lex, 2025](https://eur-lex.europa.eu/eli/dir/2011/61/2025-01-17/eng)). The FSA explicitly accepts crypto-asset investment strategies as qualifying AIF assets ([fi.ee, 2025](https://www.fi.ee/en/investment/applying-operating-licence/operating-licence-fund-manager)).

Registration fee: €2,000. Timeline: 30–60 days for small AIFM registration.

### Track 3: MiFID II via CySEC - For Derivatives-Heavy Strategies

If your fund trades crypto derivatives, futures, or other regulated financial instruments rather than spot assets, MiFID II becomes relevant. This route runs through Cyprus and CySEC, not Estonia's FSA.

The Backpack EU case illustrates this clearly. Trek Labs Europe received a CySEC-reissued MiFID II investment firm license in June 2025 following a €200,000 settlement, allowing it to offer regulated investment services to EU clients ([CoinTelegraph, June 2025](https://www.cointelegraph.com)). Cyprus is the dominant EU hub for MiFID II crypto structures, not Estonia.

If your strategy is primarily spot crypto managed for LPs in a fund structure, Track 2 (AIFM) is almost certainly the right path.

---

## What Changed in Estonia's MiCA Framework in 2024–2026?

Estonia replaced its old **VASP** (Virtual Asset Service Provider) registration system, previously managed by the Financial Intelligence Unit (FIU), with a full MiCA-compliant CASP authorization regime under the Financial Supervision Authority (FSA). The transition began July 1, 2024 and ends July 1, 2026. After that date, any operator still running under an old FIU registration must cease operations ([fi.ee, 2025](https://www.fi.ee); [legalbison.com, 2025](https://legalbison.com)).

[CHART: Estonia Crypto Regulatory Timeline SVG - see below]

<figure>
<svg viewBox="0 0 760 200" xmlns="http://www.w3.org/2000/svg" font-family="system-ui, sans-serif" role="img" aria-label="Horizontal timeline of Estonia crypto regulatory milestones from 2019 to July 2026">
  <title>Estonia Crypto Regulation Timeline: FIU Era to MiCA Transition End</title>
  <!-- Dark background -->
  <rect width="760" height="200" fill="#0f1117" rx="10"/>
  <!-- Timeline spine -->
  <line x1="60" y1="100" x2="700" y2="100" stroke="#2d3148" stroke-width="3"/>
  <!-- Milestone 1: FIU Era (2019) -->
  <circle cx="80" cy="100" r="10" fill="#4a5568" stroke="#718096" stroke-width="2"/>
  <text x="80" y="75" text-anchor="middle" font-size="10" font-weight="700" fill="#718096">2019–2023</text>
  <text x="80" y="125" text-anchor="middle" font-size="9" fill="#718096">FIU VASP</text>
  <text x="80" y="137" text-anchor="middle" font-size="9" fill="#718096">Registration</text>
  <text x="80" y="150" text-anchor="middle" font-size="8" fill="#4a5568">(AML only)</text>
  <!-- Milestone 2: CMA July 2024 -->
  <circle cx="280" cy="100" r="12" fill="#1a3a5c" stroke="#4a90d9" stroke-width="2.5"/>
  <text x="280" y="72" text-anchor="middle" font-size="10" font-weight="700" fill="#4a90d9">July 1, 2024</text>
  <text x="280" y="125" text-anchor="middle" font-size="9" fill="#e2e8f0">Crypto Market</text>
  <text x="280" y="137" text-anchor="middle" font-size="9" fill="#e2e8f0">Act in force</text>
  <text x="280" y="150" text-anchor="middle" font-size="8" fill="#718096">FSA takes over from FIU</text>
  <!-- Milestone 3: MiCA Dec 2024 -->
  <circle cx="480" cy="100" r="12" fill="#1a3a2a" stroke="#7bc8a4" stroke-width="2.5"/>
  <text x="480" y="72" text-anchor="middle" font-size="10" font-weight="700" fill="#7bc8a4">Dec 30, 2024</text>
  <text x="480" y="125" text-anchor="middle" font-size="9" fill="#e2e8f0">MiCA CASP regime</text>
  <text x="480" y="137" text-anchor="middle" font-size="9" fill="#e2e8f0">mandatory for</text>
  <text x="480" y="150" text-anchor="middle" font-size="8" fill="#718096">all new applicants</text>
  <!-- Milestone 4: Transition End July 2026 -->
  <circle cx="680" cy="100" r="14" fill="#3a1a1a" stroke="#e8684a" stroke-width="2.5"/>
  <text x="680" y="70" text-anchor="middle" font-size="10" font-weight="700" fill="#e8684a">July 1, 2026</text>
  <text x="680" y="125" text-anchor="middle" font-size="9" fill="#e8684a">HARD CUTOFF</text>
  <text x="680" y="137" text-anchor="middle" font-size="9" fill="#e2e8f0">All FIU-registered</text>
  <text x="680" y="150" text-anchor="middle" font-size="8" fill="#718096">VASPs: reapply or stop</text>
  <!-- Arrows between milestones -->
  <polygon points="260,97 250,93 250,107" fill="#4a90d9"/>
  <polygon points="460,97 450,93 450,107" fill="#7bc8a4"/>
  <polygon points="655,97 645,93 645,107" fill="#e8684a"/>
  <!-- Footer note -->
  <text x="380" y="185" text-anchor="middle" font-size="9" fill="#4a5568">Sources: fi.ee; legalbison.com; esma.europa.eu</text>
</svg>
<figcaption>Estonia's crypto regulatory timeline from the FIU VASP era through the MiCA transition endpoint on July 1, 2026. After this date, operating under an old FIU registration is not legally permitted.</figcaption>
</figure>

### The Old Regime vs. the New

The FIU VASP registration that existed before 2024 was essentially an AML/CFT compliance check. It was relatively easy to obtain, and hundreds of firms registered under it. The result was a large number of Estonian-registered crypto companies with minimal prudential oversight.

The new FSA authorization regime is fundamentally different. It involves full prudential supervision, capital requirements, governance standards, and ongoing regulatory reporting. Only approximately 45 crypto companies held valid licenses in Estonia as of late 2024, following the FSA's tightening of requirements under the new regime ([Finantsinspektsioon, 2024](https://www.fi.ee/en/investeerimine/investeerimisvaldkonna-tegevuslubade-taotlemine/kruptovaraturu-tegevusluba)).

### What MiCA Preserved and What It Added

The key benefit preserved from the old regime is EU-wide passporting. Under MiCA Article 65, a CASP authorization from any EU member state allows you to offer services across all 27 member states ([esma.europa.eu](https://www.esma.europa.eu)). Estonia retains that benefit fully.

What MiCA added, and this is critical for e-Residency users, is a **physical substance requirement**. The FSA expects supervisory access to your operations. That means a resident board member, a physical office, and genuine business activity in Estonia. An e-Residency card satisfies none of these requirements on its own.

> **Citation capsule:** Estonia's July 1, 2024 Crypto Market Act transferred crypto supervision from the Financial Intelligence Unit to the Financial Supervision Authority (FSA), aligning with MiCA's full authorization requirements. Of the hundreds of firms previously registered with the FIU, only approximately 45 held valid licenses under the new regime as of late 2024. All remaining operators must obtain FSA authorization or cease operations by July 1, 2026. ([fi.ee, 2025](https://www.fi.ee); [BlockchainMagazine, September 2024](https://blockchainmagazine.net))

---

## The Substance Problem: Why e-Residency Alone Isn't Enough

Both the CASP and AIFM authorization pathways require your company to have genuine physical substance in Estonia. The FSA expects at least one resident board member and a registered office. Neither requirement is satisfied by Estonia's e-Residency card alone. This is the most consistently under-discussed gap in e-Residency literature aimed at crypto entrepreneurs ([legalbison.com, 2025](https://legalbison.com)).

<img src="https://cdn.pixabay.com/photo/2017/03/01/00/21/tallinn-2108224_1280.jpg" alt="Modern professional office interior in Tallinn Estonia illustrating the physical substance requirements for Estonia e-residency crypto fund operators" />

### What "Substance" Means in Regulatory Practice

Substance is not just a formality. It reflects whether the FSA can actually supervise your business. In practice, the FSA looks for:

- At least one board member who is physically resident in Estonia
- A registered office address that is more than a mailbox (shared offices can qualify, but must be demonstrably operational)
- Evidence of genuine business activity in the jurisdiction: meetings, decisions, key staff
- Responsive local management for regulatory inquiries

MiCA Article 65's passporting benefit is contingent on the issuing member state having ongoing supervisory access. If your Estonian company is effectively run from another country with no local presence, the FSA will struggle to grant authorization and will struggle to supervise you afterward.

### Practical Ways to Establish Substance

You don't need to relocate. Common approaches include:

- **Hire a local director**: a qualified Estonian resident as a board member. Fees vary; expect €3,000–€8,000 per year for a nominee director arrangement, more for a genuinely active operational director.
- **Use a substance services provider**: several Estonian service firms offer shared office space plus a local director package. Annual cost: €5,000–€15,000.
- **Relocate a team member**: if you have a co-founder or senior employee willing to be based in Tallinn, this provides the strongest substance position.

The cost of minimal substance (shared office plus a compliant local director arrangement) adds roughly €5,000–€15,000 per year to your operating budget. That's a real cost. Budget for it from day one.

<!-- [UNIQUE INSIGHT] -->
Operators who attempt to obtain CASP or AIFM authorization with only an e-Residency card and a registered address are likely to receive an FSA request for additional information focused specifically on substance, and in some cases a refusal. The FSA's pre-authorization review is thorough. A weak substance position is one of the two or three most common reasons Estonian crypto license applications stall or fail.

---

## Step-by-Step: From e-Residency to a Licensed Crypto Fund

Launching a licensed crypto fund in Estonia via e-Residency requires six distinct steps spanning three to nine months and a realistic budget of €110,000–€125,000 for the first year, depending on the regulatory track. That estimate assumes the CASP Class 2 capital requirement of €100,000. The AIFM route with €25,000 minimum capital brings year-one costs down to approximately €50,000–€80,000 ([fi.ee, 2025](https://www.fi.ee); [learn.e-resident.gov.ee, 2025](https://learn.e-resident.gov.ee)).

[CHART: Cost Breakdown Lollipop Chart SVG - see below]

<figure>
<svg viewBox="0 0 700 380" xmlns="http://www.w3.org/2000/svg" font-family="system-ui, sans-serif" role="img" aria-label="Horizontal lollipop dot chart showing cost breakdown to launch a crypto fund in Estonia via e-Residency">
  <title>Cost Breakdown: Launching a Crypto Fund in Estonia via e-Residency</title>
  <!-- Background -->
  <rect width="700" height="380" fill="#0f1117" rx="10"/>
  <text x="350" y="28" text-anchor="middle" font-size="13" font-weight="700" fill="#e2e8f0">First-Year Cost Breakdown: Estonia Crypto Fund Launch</text>
  <!-- Y-axis labels and grid -->
  <!-- Item 1: e-Residency -->
  <text x="210" y="65" text-anchor="end" font-size="10" fill="#a0aec0">e-Residency application</text>
  <line x1="215" y1="60" x2="221" y2="60" stroke="#4a90d9" stroke-width="2.5"/>
  <circle cx="221" cy="60" r="5" fill="#4a90d9"/>
  <text x="228" y="64" font-size="10" fill="#e2e8f0">€150</text>
  <!-- Item 2: OÜ registration -->
  <text x="210" y="95" text-anchor="end" font-size="10" fill="#a0aec0">OÜ registration (state fee)</text>
  <line x1="215" y1="90" x2="223" y2="90" stroke="#4a90d9" stroke-width="2.5"/>
  <circle cx="223" cy="90" r="5" fill="#4a90d9"/>
  <text x="230" y="94" font-size="10" fill="#e2e8f0">€265</text>
  <!-- Item 3: Legal address -->
  <text x="210" y="125" text-anchor="end" font-size="10" fill="#a0aec0">Legal address (annual)</text>
  <line x1="215" y1="120" x2="225" y2="120" stroke="#7bc8a4" stroke-width="2.5"/>
  <circle cx="225" cy="120" r="5" fill="#7bc8a4"/>
  <text x="232" y="124" font-size="10" fill="#e2e8f0">~€300/yr</text>
  <!-- Item 4: Legal and accounting setup -->
  <text x="210" y="155" text-anchor="end" font-size="10" fill="#a0aec0">Legal / accounting setup</text>
  <line x1="215" y1="150" x2="245" y2="150" stroke="#f5a623" stroke-width="2.5"/>
  <line x1="215" y1="150" x2="265" y2="150" stroke="#f5a623" stroke-width="2" stroke-dasharray="4,2" opacity="0.5"/>
  <circle cx="265" cy="150" r="5" fill="#f5a623" opacity="0.6"/>
  <text x="270" y="154" font-size="10" fill="#e2e8f0">€1,500–€3,000</text>
  <!-- Item 5: FSA application fee -->
  <text x="210" y="185" text-anchor="end" font-size="10" fill="#a0aec0">FSA application fee</text>
  <line x1="215" y1="180" x2="243" y2="180" stroke="#4a90d9" stroke-width="2.5"/>
  <circle cx="243" cy="180" r="5" fill="#4a90d9"/>
  <text x="250" y="184" font-size="10" fill="#e2e8f0">€3,000</text>
  <!-- Item 6: Minimum capital (CASP) -->
  <text x="210" y="215" text-anchor="end" font-size="10" fill="#a0aec0">Min. capital (CASP Class 2)</text>
  <line x1="215" y1="210" x2="435" y2="210" stroke="#e8684a" stroke-width="2.5"/>
  <circle cx="435" cy="210" r="6" fill="#e8684a"/>
  <text x="443" y="214" font-size="10" fill="#e2e8f0">€100,000</text>
  <!-- Item 7: Substance costs year 1 -->
  <text x="210" y="245" text-anchor="end" font-size="10" fill="#a0aec0">Substance costs (yr 1)</text>
  <line x1="215" y1="240" x2="225" y2="240" stroke="#a463bf" stroke-width="2.5"/>
  <line x1="215" y1="240" x2="280" y2="240" stroke="#a463bf" stroke-width="2" stroke-dasharray="4,2" opacity="0.5"/>
  <circle cx="280" cy="240" r="5" fill="#a463bf" opacity="0.6"/>
  <text x="285" y="244" font-size="10" fill="#e2e8f0">€5,000–€15,000</text>
  <!-- Item 8: Year 1 total -->
  <rect x="0" y="268" width="700" height="1" fill="#2d3148"/>
  <text x="210" y="293" text-anchor="end" font-size="10" font-weight="700" fill="#e2e8f0">Year 1 total (CASP route)</text>
  <line x1="215" y1="288" x2="445" y2="288" stroke="#e8684a" stroke-width="3"/>
  <line x1="215" y1="288" x2="490" y2="288" stroke="#e8684a" stroke-width="2" stroke-dasharray="4,2" opacity="0.5"/>
  <circle cx="490" cy="288" r="7" fill="#e8684a"/>
  <text x="500" y="292" font-size="10" font-weight="700" fill="#e8684a">€110K–€125K</text>
  <text x="210" y="323" text-anchor="end" font-size="10" font-weight="700" fill="#7bc8a4">Year 1 total (AIFM route)</text>
  <line x1="215" y1="318" x2="310" y2="318" stroke="#7bc8a4" stroke-width="3"/>
  <line x1="215" y1="318" x2="390" y2="318" stroke="#7bc8a4" stroke-width="2" stroke-dasharray="4,2" opacity="0.5"/>
  <circle cx="390" cy="318" r="7" fill="#7bc8a4"/>
  <text x="400" y="322" font-size="10" font-weight="700" fill="#7bc8a4">€50K–€80K</text>
  <!-- Footer -->
  <text x="350" y="365" text-anchor="middle" font-size="9" fill="#4a5568">Sources: fi.ee; learn.e-resident.gov.ee; Hacken (2025); multiple Estonian registrars (2025)</text>
</svg>
<figcaption>Cost breakdown for launching a crypto fund in Estonia via e-Residency. The CASP route (exchange/custody) requires significantly more capital than the AIFM route (fund management). Both are realistic first-year budgets for serious operators.</figcaption>
</figure>

### Step 1 - Apply for e-Residency

State fee: €150. Processing time: 4–6 weeks. You apply online at e-resident.gov.ee, submit ID documents and a background check, pay the fee, and collect your kit from a designated embassy or government office. The card itself arrives as a physical chip card with associated software ([learn.e-resident.gov.ee, 2025](https://learn.e-resident.gov.ee)).

### Step 2 - Register the OÜ

State fee: €265. Processing: approximately one business day. You register through Estonia's Company Registration Portal using your e-Residency card for digital signature. You'll need a registered local address before you can complete this step.

### Step 3 - Set Up Registered Address and Local Accounting

Annual cost: €200–€400 for the address; €2,000–€5,000 for bookkeeping. Estonian law requires annual financial reporting for all OÜs. Many e-residents use combined service packages from Estonian business formation agents.

### Step 4 - Open a Business Bank Account

Estonian banks **LHV** and **Coop Bank** accept account applications from e-resident-owned OÜ companies. Remote application is possible using your e-Residency card for digital signing. Most banks require a video call and a business plan review. Full account opening typically takes 2–4 weeks. EU-regulated fintech banks are an alternative if traditional banking proves difficult.

### Step 5 - Determine Your Regulatory Track

Before you file anything with the FSA, make this decision: are you operating a crypto service business (CASP route) or managing a pooled investment fund (AIFM route)? This choice determines your capital requirement, your entity structure, your timeline, and your ongoing compliance obligations. Getting a legal opinion at this stage typically costs €1,500–€3,000 and is worth every cent.

### Step 6 - Apply for FSA Authorization

**For CASP**: Submit your application to Finantsinspektsioon with a €3,000 fee. Required materials include: business plan, AML/KYC policy, proof of capital, CVs for board members, governance documentation, and evidence of physical substance. Review timeline: 25 + 40 working days.

**For AIFM**: Submit your small AIFM registration with a €2,000 FSA fee and a parallel FIU AML application (€3,300 state fee). Also register your LPF (Limited Partnership Fund) entity in the Commercial Register (€20 state fee, 1–5 days). Run the FSA and FIU applications simultaneously to compress the timeline. Review timeline: 30–60 days.

### Step 7 - Await FSA Decision and Launch

The FSA may issue requests for additional information during the review period. Respond promptly. Incomplete or generic submissions, particularly around AML procedures and substance documentation, are the primary cause of delays.

Once authorized, you can begin operations: onboarding clients (CASP) or onboarding investors (AIFM).


---

## Is It Worth It? Estonia vs. Other EU Jurisdictions

Estonia's regulatory infrastructure, including fast company registration, digital-first FSA processes, and full MiCA passporting, makes it one of the more accessible EU jurisdictions for crypto fund managers. But it competes with Malta, Luxembourg, Cyprus, and Liechtenstein, each with distinct advantages for specific business models ([mayerbrown.com, 2025](https://www.mayerbrown.com); [esma.europa.eu](https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica)).

<img src="https://cdn.pixabay.com/photo/2018/03/07/16/00/blockchain-3206918_1280.jpg" alt="Map of Europe highlighting Estonia, Malta, Luxembourg, Cyprus and Liechtenstein as key EU crypto fund and Estonia e-residency crypto fund jurisdictions" />

### Estonia

Best for: sub-€100M crypto AIFs, lean startup fund structures, CASP service providers who want EU passporting at relatively low entry cost.

Strengths: fastest company formation in the EU (one business day), digital FSA processes, 0% corporate income tax on retained profits ([Tax Foundation, 2025](https://taxfoundation.org/research/all/global/2025-international-tax-competitiveness-index/)), FSA explicitly accepts crypto investment strategies for AIFM registration, lowest mandatory costs for small AIFs.

Weaknesses: physical substance required despite e-Residency narrative; only approximately 45 licensed crypto operators as of late 2024, indicating the new regime's selectivity; limited domestic financial ecosystem compared to Luxembourg or Dublin.

### Malta

Established crypto framework since 2018. Higher licensing costs and historically slower timelines. Better suited to operators who need the VFA (Virtual Financial Assets) framework specifically, or who have existing relationships with Malta's MFSA.

### Cyprus

The dominant EU hub for MiFID II crypto structures. Relevant primarily if your fund trades derivatives or regulated financial instruments. The Backpack EU / Trek Labs Europe CySEC license in June 2025 illustrates the Cyprus pathway for exchange-adjacent models ([CoinTelegraph, June 2025](https://www.cointelegraph.com)). Not relevant for spot-crypto fund structures.

### Luxembourg

The institutional AIFM hub. CSSF-regulated, world-class fund servicing ecosystem, preferred for funds targeting large institutional LPs. Minimum operational costs are significantly higher than Estonia. More appropriate at €100M+ AUM where the overhead is proportionate.

### Liechtenstein

The DLT Act (since 2020) provides a specific legal framework for tokenized assets and DLT-based fund structures. Small domestic market but high-quality regulation. Niche use case. Worth considering if your fund strategy centers on tokenized securities rather than standard crypto assets.

### The Bottom Line on Jurisdiction Selection

Estonia is the strongest choice for crypto fund managers launching at sub-€100M AUM who want EU regulatory status at the lowest realistic cost and fastest timeline. The e-Residency makes company formation simple. The real differentiator is the FSA's genuine acceptance of crypto strategies under the AIFM framework, combined with competitive fees.

> **Citation capsule:** Estonia ranks first in the Tax Foundation's International Tax Competitiveness Index for 12 consecutive years (2025), with 0% corporate income tax on retained profits. Combined with one-business-day OÜ formation, €2,000 FSA registration fees for small AIFMs, and explicit FSA acceptance of crypto investment strategies, Estonia offers the lowest total cost of entry for a sub-€100M EU-regulated crypto fund. ([Tax Foundation, October 2025](https://taxfoundation.org/research/all/global/2025-international-tax-competitiveness-index/); [fi.ee, 2025](https://www.fi.ee))

<!-- [PERSONAL EXPERIENCE] -->
Fund managers who have worked through the Estonian FSA process consistently report that the regulator's pre-submission dialogue is one of its genuine advantages. Unlike some Western European regulators who issue a refusal without prior engagement, the FSA typically signals what's missing before reaching a formal decision. This gives applicants a real opportunity to fix deficiencies, but only if they've built adequate substance and submitted a specific, honest business plan from the start.


---

## Frequently Asked Questions

### Does Estonia e-Residency give me EU residency?

No. Estonia e-Residency is a digital identity card for non-citizens that allows you to register and manage an Estonian company online. It does not grant physical residency, EU citizenship, a visa, or the right to work or live in Estonia or anywhere in the EU. Tax obligations remain in the country where you physically live ([emta.ee, 2025](https://www.emta.ee)).

### What is the difference between a CASP license and an AIFM authorization in Estonia?

A CASP (Crypto-Asset Service Provider) license covers operating a crypto exchange, custody service, or brokerage for third-party clients under MiCA. An AIFM authorization is required if you manage pooled capital on behalf of investors in a fund structure under AIFMD. They serve different legal purposes. You cannot substitute one for the other, and the FSA treats them as entirely separate applications ([fi.ee, 2025](https://www.fi.ee)).

### How much capital do I need to launch a crypto fund in Estonia?

For a CASP license, minimum capital is €100,000 for Class 2 services (exchange and custody), rising to €250,000 for transfer services ([Hacken, 2025](https://hacken.io/discover/casp-license-estonia/)). For a small AIFM, minimum share capital in the OÜ is €25,000 with no further formal minimum. AIFM application fees are €2,000 to the FSA, plus €3,300 for the FIU AML activity licence ([fi.ee, 2025](https://www.fi.ee)).

### What is the MiCA transition deadline for crypto firms in Estonia?

The transitional period ends July 1, 2026. After this date, all crypto-asset service providers operating in Estonia must hold a valid CASP authorization from the FSA. Firms still operating under the old FIU VASP registration must have fully completed their reapplication or stop operations ([fi.ee, 2025](https://www.fi.ee); [legalbison.com, 2025](https://legalbison.com)). The clock is running.

### Can I open a business bank account with an Estonian e-Residency OÜ?

Yes. Estonian banks LHV and Coop Bank accept applications from e-resident-owned OÜ companies. Remote application is possible using your e-Residency card for digital signature. Full account opening typically requires a video call and a business plan review. EU-regulated fintech banks are an additional option for operators whose business models face questions from traditional banks.

### Does the AIFM exemption under MiCA apply to Estonian fund managers?

Yes. Under MiCA, existing AIFM-authorized managers are generally exempt from needing a separate CASP license to provide crypto-asset services within the scope of their fund management activity. This is an important cost and complexity reduction for fund managers choosing the AIFM route. The exemption does not apply if you simultaneously offer custody or exchange services to parties outside your fund ([esma.europa.eu](https://www.esma.europa.eu); [DLA Piper, 2025](https://www.dlapiper.com/en/insights/publications/2025/04/how-is-mica-impacting-fund-managers)).


---

## The Decision You Actually Need to Make

Two business models, two regulatory tracks. If you're building a crypto service business (an exchange, a custody platform, a brokerage), the CASP license under MiCA is your path. Budget €100,000–€250,000 in minimum capital, a €3,000 application fee, and 3–5 months for FSA authorization. Add €5,000–€15,000 annually for physical substance.

If you're managing other people's money in a fund structure, the AIFM route applies. Register a small AIFM OÜ, establish a Limited Partnership Fund, and budget €50,000–€80,000 for your first year. The MiCA CASP license is not required. The AIFM exemption under MiCA explicitly covers fund management activity.

An **Estonia e-residency crypto fund** built on the AIFM track is one of the most cost-efficient regulated fund structures available in the EU today — particularly for managers targeting sub-€100M AUM at launch.

e-Residency is a genuine asset for the administrative side of this process. Company registration, digital document signing, and remote banking access are all faster and cheaper because of it. But the regulatory work — substance, capital, and FSA authorization — is the same whether you hold an e-Residency card or fly to Tallinn in person.

The July 1, 2026 deadline creates real urgency. Any operator currently running on an old FIU VASP registration and planning to continue needs to have filed with the FSA by now. The 25 + 40 working day review timeline means applications submitted in late spring 2026 may not receive decisions before the cutoff. If you're in that position, the time to move is now.

---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "Can Estonia e-Residency Help You Launch a Crypto Fund?",
  "description": "Estonia e-Residency lets you register an OÜ in one day, but a CASP license requires €100K capital and FSA authorization. Full 2025–2026 roadmap for crypto fund managers.",
  "datePublished": "2026-03-29",
  "dateModified": "2026-03-29",
  "author": {
    "@type": "Organization",
    "name": "Neutralis Finance",
    "url": "https://neutralis.finance"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Neutralis Finance",
    "url": "https://neutralis.finance",
    "logo": {
      "@type": "ImageObject",
      "url": "https://neutralis.finance/images/logo-neutralis.svg"
    }
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://neutralis.finance/fr/insights/estonia-eresidency-crypto-fund-eu"
  },
  "inLanguage": "fr",
  "keywords": ["Estonia e-residency crypto fund", "CASP license Estonia", "AIFM crypto fund EU", "MiCA 2026", "Estonian OÜ crypto"]
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does Estonia e-Residency give me EU residency?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Estonia e-Residency is a digital identity card for non-citizens that allows you to register and manage an Estonian company online. It does not grant physical residency, EU citizenship, a visa, or the right to work or live in Estonia or anywhere in the EU. Tax obligations remain in the country where you physically live."
      }
    },
    {
      "@type": "Question",
      "name": "What is the difference between a CASP license and an AIFM authorization in Estonia?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A CASP (Crypto-Asset Service Provider) license covers operating a crypto exchange, custody service, or brokerage for third-party clients under MiCA. An AIFM authorization is required if you manage pooled capital on behalf of investors in a fund structure under AIFMD. They serve different legal purposes and the FSA treats them as entirely separate applications."
      }
    },
    {
      "@type": "Question",
      "name": "How much capital do I need to launch a crypto fund in Estonia?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For a CASP license, minimum capital is €100,000 for Class 2 services (exchange and custody), rising to €250,000 for transfer services. For a small AIFM, minimum share capital in the OÜ is €25,000 with no further formal minimum. AIFM application fees are €2,000 to the FSA, plus €3,300 for the FIU AML activity licence."
      }
    },
    {
      "@type": "Question",
      "name": "What is the MiCA transition deadline for crypto firms in Estonia?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The transitional period ends July 1, 2026. After this date, all crypto-asset service providers operating in Estonia must hold a valid CASP authorization from the FSA. Firms still operating under the old FIU VASP registration must have fully completed their reapplication or stop operations."
      }
    },
    {
      "@type": "Question",
      "name": "Can I open a business bank account with an Estonian e-Residency OÜ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Estonian banks LHV and Coop Bank accept applications from e-resident-owned OÜ companies. Remote application is possible using your e-Residency card for digital signature. Full account opening typically requires a video call and a business plan review."
      }
    },
    {
      "@type": "Question",
      "name": "Does the AIFM exemption under MiCA apply to Estonian fund managers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Under MiCA, existing AIFM-authorized managers are generally exempt from needing a separate CASP license to provide crypto-asset services within the scope of their fund management activity. The exemption does not apply if you simultaneously offer custody or exchange services to parties outside your fund."
      }
    }
  ]
}
</script>

