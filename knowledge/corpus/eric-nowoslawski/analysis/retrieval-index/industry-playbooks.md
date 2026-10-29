---
type: industry-playbooks
aliases: ["Industry Playbooks — Eric Nowoslawski Retrieval Index"]
corpus: eric-nowoslawski
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
last_updated: 2026-03-20
---

# Industry Playbooks — Eric Nowoslawski Retrieval Index

Per-vertical guidance from the corpus and gap resolution NotebookLM queries. The Copywriter Agent uses this to adjust targeting, offers, and copy when generating campaigns for specific industries.

---

## SaaS

### Targeting Adjustments
- LinkedIn industry tags are self-reported and unreliable for SaaS. Verify with AI keyword search or Harmonic.ai data.
- Use Harmonic.ai for SaaS-specific company data (funding stage, tech stack, growth signals).
- Use Ocean.io to build lookalike lists from best customers.
- Target by technographic signals (BuiltWith) when displacing a competitor's tool.
- Job postings are a strong signal: hiring for roles your product supports or replaces indicates budget and priority.

### Offer Adjustments
- "Free trial" rarely works cold -- time-to-value is too long. Prospects won't invest 30 minutes setting up a tool from a cold email.
- Instead: offer "knowledge arbitrage" -- insights, benchmarking data, or trends from your user base that the prospect cannot get elsewhere.
- Creative Ideas campaign is the default recommendation: 3 AI-generated use cases showing how the prospect's specific business could use your product.
- Lead magnets that work: custom ROI calculators, industry benchmark reports, "we built this for you" data analysis.
- Lead magnets that fail: pre-recorded webinars, generic product demos, whitepapers.

### Copy Adjustments
- "Chunk up" to outcomes, not features. Never lead with what your product does -- lead with what the prospect can accomplish.
- For commoditized categories (CRM, project management, analytics), use Flash Roll to reveal the mechanism that differentiates you from competitors.
- Avoid: feature lists, technical specifications, integration counts, "we integrate with 200+ tools."
- Good: "We helped a company like yours add {{quantifiable_result}} in {{timeframe}} without {{risk}}."

### Anti-Patterns
- Do not target individual contributors (developers, designers) with cold email. They hate it and rarely have purchasing authority. Target managers and VPs.
- Do not mention competitor names unless you have a strong displacement story with precise matching (same industry + headcount band).
- Do not lead with "AI-powered" unless your AI capability is genuinely differentiating. Every SaaS company claims AI now.

---

## Marketing Agencies

### Targeting Adjustments
- Target companies that are already spending on marketing but may be dissatisfied with their current agency or team.
- Use SimilarWeb data (via Serper `site:` queries in Clay) to identify companies with traffic but poor conversion metrics.
- LinkedIn Ads Library can reveal companies actively running campaigns (signal of marketing budget).
- Job postings for marketing roles signal in-house team building -- may indicate agency displacement opportunity OR agency augmentation opportunity.

### Offer Adjustments
- "Chunk up" to outcomes, not services. Never sell "we do SEO" -- sell "we helped a company like yours go from 50 to 500 leads per month."
- Give massive upfront value: 5,000 free validated leads, free audit of their current campaigns, custom competitive analysis.
- The lead magnet IS the sales pitch: when you give away part of your actual service, the quality sells itself.
- For competitive displacement: "What can you say that your competitor can't say?" Use Flash Roll to reveal your unique mechanism.

### Copy Adjustments
- Agencies face the "everyone says the same thing" problem. Every agency claims to be data-driven, full-service, and results-oriented.
- Differentiate with specificity: exact methodologies, proprietary frameworks, unique data sources.
- CTA: "Can I walk you through the framework we used?" (offers process, not pitch).
- Show don't tell: include a Google Sheet sample of actual leads you generated, a screenshot of campaign results, or a Loom walkthrough of your audit process.

### Anti-Patterns
- Do not sell services generically. "We offer SEO, PPC, social media, and content marketing" sounds like every agency.
- Do not use case studies unless you can match them precisely to the prospect's industry and company size.
- Do not pitch to the CEO unless it is a <50 person company. Target VP/Director of Marketing.

---

## Local Business

### Targeting Adjustments
- Most local businesses have no LinkedIn presence. Do NOT use LinkedIn Sales Navigator for local targeting.
- Use Google Maps data via D7 Lead Finder, Outscraper, or Apify for prospecting.
- support@ and info@ emails are acceptable for local businesses (unlike B2B where you need named contacts).
- Target by specific local signals: Google review count, Google review rating, Yelp presence, local news mentions.
- Use Claygent to scrape specific negative Google reviews for personalization.

### Offer Adjustments
- Offers must be tangible and immediately understood. No abstract value propositions.
- Performance-based pricing works exceptionally well: "You only pay if we succeed" (Google reputation management = 1:70 ratio).
- Physical lead magnets work in local: free box of product, free sample delivered during a call, free first service.
- Time-bound local offers: reference seasonal events, local regulations, or community-specific triggers.

### Copy Adjustments
- Hyper-casual tone. These are not corporate executives -- write like you are texting a local business owner.
- Reference specific local details: their Google review rating, a specific reviewer's name, their neighborhood, a local restaurant.
- "I was looking at {{company}}'s Google reviews and noticed..." is the canonical local opening.
- Images are MORE acceptable in local campaigns: screenshot of their actual negative review, meme about their industry problem (bed bug meme for hotels = documented success).

### Anti-Patterns
- Do not use corporate language. "Leverage our platform" will get deleted instantly.
- Do not assume they know what your industry jargon means. "SEO," "CRM," "lead generation" need to be explained in plain English if used at all.
- Do not send from generic-looking domains. Local businesses are more suspicious of unfamiliar senders.
- Do not use long sequences. 1-2 emails maximum for local. They either respond or they do not.

---

## Healthcare

### Targeting Adjustments
- Target practice managers, not doctors. Physicians rarely read cold email and are not the decision-makers for most services.
- Office managers, practice administrators, and billing managers are the correct contacts for operational tools.
- For hospital systems, target department heads or VP-level administrators.
- Use state medical board directories and CMS data for targeting instead of LinkedIn.
- Job postings for "practice manager" or "medical office administrator" signal operational growth.

### Offer Adjustments
- Compliance language is mandatory. Any claim must be defensible and any process must be HIPAA-aware.
- Offer: audit of online patient reviews (publicly available, non-HIPAA data) -- mirrors the Google reputation management playbook.
- Free compliance check or regulatory readiness assessment works as a lead magnet.
- Do not offer anything that requires sharing patient data in the initial outreach.
- Time triggers: regulatory changes, open enrollment periods, year-end compliance deadlines.

### Copy Adjustments
- Conservative, professional tone. Less casual than other verticals but still plain language.
- Reference specific public data: their Google/Healthgrades reviews, CMS star ratings, publicly reported quality metrics.
- "Poke the bear" works well: "How do you know your current {{billing/coding/staffing}} process is maximizing your reimbursement rates?"
- Avoid: any language that could be interpreted as a guarantee of patient outcomes.

### Anti-Patterns
- Do not claim to improve patient outcomes unless you have clinical evidence.
- Do not reference specific patient information (obvious HIPAA violation signal).
- Do not target small practices (<5 providers) with enterprise solutions -- the price point and complexity will not match.
- Do not use aggressive follow-up sequences. Healthcare decision-makers are risk-averse and easily annoyed by persistence.

---

## Financial Services

### Targeting Adjustments
- Target CPAs and financial advisors separately -- they have different pain points and buying processes.
- Use Clay to detect "first-time founder" or "first-time CFO" -- these contacts lack existing advisory relationships and are more open to outreach.
- Regulatory filing data (SEC, state regulators) can be used as targeting signals.
- LinkedIn "Changed Jobs" filter is valuable: new CFOs and controllers actively seek advisory relationships.

### Offer Adjustments
- Investment pitch fails cold. Do NOT lead with "grow your portfolio" or "investment opportunities."
- Pivot to tax strategy, depreciation, cost segregation -- specific, actionable financial tactics.
- The tax campaign A/B is the canonical example: "Are you looking for help with taxes?" = near-zero. "How do you know your current tax accountant is using every legal loophole?" = 2-3 leads/day.
- Offer a free tax savings analysis or depreciation study -- specific deliverables with calculable value.

### Copy Adjustments
- "Poke the bear" is the primary technique: challenge the adequacy of their current financial advisor/accountant/strategy.
- Quantify the outcome: "We typically find $50K-$200K in missed depreciation for commercial real estate owners" is more effective than "we help with tax optimization."
- Do not use the word "optimize" -- it is on the banned list AND sounds like every other financial services pitch.
- Reference specific tax code sections or regulatory changes to demonstrate expertise (Flash Roll for financial services).

### Anti-Patterns
- Do not pitch investment products cold -- regulatory concerns and audience fatigue make this category-level difficult.
- Do not use generic financial jargon: "wealth management," "holistic financial planning," "fiduciary responsibility." These are undifferentiated.
- Do not target C-suite at large financial institutions -- they have compliance departments that intercept and flag cold outreach.
- Do not assume all financial services prospects care about the same thing -- a CPA's pain points are different from a wealth manager's.

---

## E-commerce

### Targeting Adjustments
- Use Google Shopping data (via Serper in Clay) to estimate AOV and product category.
- Instagram and TikTok engagement data can signal marketing sophistication and budget.
- BuiltWith data reveals their current tech stack (Shopify vs. WooCommerce vs. custom) -- relevant for tech-displacement campaigns.
- Seasonal targeting matters more in e-commerce than any other vertical. Target 6-8 weeks before peak season (Black Friday, back to school, etc.).
- Use Claygent to scrape their top product pages and identify pricing/positioning.

### Offer Adjustments
- "Show don't tell" with screenshots: show them their own product pages, competitor analysis, or ad performance benchmarks.
- Creative Ideas campaign works well: 3 specific marketing ideas tailored to their product category and audience.
- Free competitive analysis is the strongest lead magnet: "I put together a comparison of your top 3 competitors' ad strategies."
- Do not offer generic "grow your sales" -- too vague. Offer specific: "We can help you reduce your Facebook CAC from $45 to $25."

### Copy Adjustments
- Reference specific products from their store to prove you did research.
- Use revenue/ROI language: e-commerce founders think in ROAS, CAC, AOV, and LTV. Use these terms (they are NOT jargon in this context -- they are the native language of the audience).
- Visual proof works: screenshots of campaign dashboards, before/after ad performance, competitor ad comparisons.
- Time-bound offers tied to seasonal peaks: "With Q4 coming up in 8 weeks, have you locked in your ad strategy?"

### Anti-Patterns
- Do not target DTC brands with B2B SaaS language. They think about customers, not "stakeholders."
- Do not pitch during peak season -- they are too busy executing. Pitch 6-8 weeks before.
- Do not assume Shopify = small. Many large e-commerce operations run on Shopify Plus.
- Do not use the word "omnichannel" -- it has been drained of meaning in e-commerce marketing.

---

## Professional Services (Law, Accounting, Consulting)

### Targeting Adjustments
- Target first-time founders and first-time position holders -- they lack existing advisory relationships and are actively seeking partners.
- Use Clay for "first-time position holder" detection: new GCs, new CFOs, new VPs who haven't yet built their vendor roster.
- Bar association directories and state licensing boards provide accurate contact data for attorneys.
- CPA association membership lists provide targeting for accounting firms.
- Job postings for "first in-house counsel" or "first VP of Finance" are strong signals.

### Offer Adjustments
- Professional services buyers are risk-averse. Offer free initial consultation, free audit, or free assessment -- anything that reduces the commitment required.
- "Doctor diagnosing" positioning is natural here: "I noticed [specific public problem] and wanted to flag it."
- For law firms: reference specific case types, regulatory changes, or jurisdiction-specific issues.
- For accounting: tax savings analysis, compliance gap assessment, or benchmark comparison against peers.

### Copy Adjustments
- More formal than local business, less formal than healthcare. Professional but direct.
- Reference specific regulatory changes, case law developments, or compliance deadlines.
- For attorneys: "I noticed [Company] is expanding into [State] -- have you lined up local counsel for [specific regulation]?"
- For accountants: mirror the financial services playbook -- "poke the bear" on missed deductions or compliance gaps.
- Credential signaling matters more here: mention relevant certifications, bar admissions, or industry associations.

### Anti-Patterns
- Do not pitch to partners at large firms -- they have established referral networks and rarely respond to cold email.
- Do not use legal jargon incorrectly -- a misused legal term destroys credibility instantly.
- Do not pitch generic "consulting services." Be specific about the problem you solve and the outcome you deliver.
- Do not target the wrong decision-maker: in law firms, practice group leaders buy; in accounting firms, managing partners buy.

---

## Cross-Vertical Rules

These apply regardless of industry:

### Offer Hierarchy (Most to Least Effective)
1. Risk-free, performance-based: "You only pay if we succeed"
2. Free deliverable with immediate value: "Here's 5,000 leads / a custom report / an audit"
3. Creative Ideas: "Here are 3 ways you could use our product"
4. Knowledge arbitrage: "Here are insights from our data that you can't get elsewhere"
5. Free consultation: "Can I walk you through our framework?"
6. Standard meeting request: "Would you be open to a quick call?"

### Universal Anti-Patterns
- Never lead with features. Lead with outcomes.
- Never use undifferentiated category language. Every competitor says the same thing.
- Never assume the prospect has context. Write for someone who has never heard of your company.
- Never pitch a "nice to have." Frame as urgent or cost-avoidant.
- Never target ICs when executives are the buyers.
- Never send more than 3 emails to a single prospect in most verticals.

### TAM-Based Sequence Length
| TAM Size | Emails | Rationale |
|----------|--------|-----------|
| >1M | 1 | Massive TAM = fresh prospects always available |
| 50K-100K | 2 | Moderate TAM = worth a follow-up but don't over-invest |
| <50K | 3 | Small TAM = each contact is valuable, maximize touches |
| <20K | 3 + omnichannel | Cold email alone insufficient at this TAM |
