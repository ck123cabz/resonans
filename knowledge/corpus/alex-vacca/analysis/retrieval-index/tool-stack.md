---
type: corpus
aliases: ["Tool Stack — Retrieval Index"]
corpus: alex-vacca
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
---

# Tool Stack — Retrieval Index

**Corpus:** Alex Vacca
**Knowledge type:** [T] Tool Stack
**Last updated:** 2026-03-24

Complete categorized inventory of tools referenced in the Alex Vacca corpus. Tools ColdIQ actively uses are marked **[active]**. Tools evaluated and replaced or rejected are marked **[replaced]** or **[rejected]**. Tools mentioned in peer/client stacks but not confirmed as ColdIQ's own are marked **[ecosystem]**.

---

## Data Sourcing

### Apollo **[active]**
Primary lead database. 275M contacts. Firmographic and technographic data. Built-in sequencing capability (not used by ColdIQ for sending). Used as the first provider in several waterfall enrichment sequences and as the contact-finding API in Claude Code terminal workflows.
`[S]→[D] | N38, N43, N59, L25, L31`

### LinkedIn Sales Navigator **[active]**
B2B filtering, job change monitoring, boolean search. Most comprehensive source for people data. Used for manual prospecting and as input for Apify scrapers.
`[S]→[D] | N28, N59, L25, L36`

### Crunchbase **[active]**
Funding round data. Used as a trigger signal source (Series A/B/C rounds create a 30-90 day outreach window, strongest in the first 2 weeks after announcement).
`[S] | N28, N59`

### Ocean.io **[active]**
Niche B2B database using bottom-up company categorization from website text rather than LinkedIn's top-down taxonomy. Generates lookalike companies from 3-5 existing customer URLs. Used to scale target account lists from positive-reply leads.
`[S]→[D] | N59, N84, L50, B17`

### Openmart **[active]**
200M+ local business records. Used for SMB and local business prospecting.
`[D] | L31, L36`

### Exa Websets **[ecosystem]**
Fastest prompt-to-list AI sourcing. Mentioned in niche vertical sourcing stack.
`[P] | B18`

### DiscoLike **[ecosystem]**
Lookalike search from existing customers. Mentioned in sourcing methods.
`[P] | B29`

---

## Intent & Signal Tracking

### RB2B **[active]**
Deanonymizes website visitors at the person level. US only. Pushes visitor data to Clay, which triggers automatic outreach. Core component of the website visitor workflow and the circular sales system.
`[S]→[D] | N2, N6, N46, N60, N75, L25, L36, B6`

### Vector **[active]**
Same function as RB2B (website visitor deanonymization). Pairs with RB2B for expanded coverage.
`[S]→[D] | N6, N60, L36, L54, B6`

### Trigify **[active]**
LinkedIn post engager tracking, profile view monitoring, and job board monitoring. Core trigger source for the job-opening workflow and the LinkedIn engager workflow. Pushes data to Clay via webhook.
`[S]→[D] | N2, N6, N36, N61, L30, B30`

### Common Room **[active]**
Monitors 70+ sales triggers: leadership changes, headcount growth, job postings, website visits, social mentions, community activity. Signal-based campaigns using Common Room data convert at 3-5x the rate of pure cold outreach.
`[S]→[D] | N6, N61, L18, L31, L32, B6, B17, B30`

### Teamfluence **[active]**
Captures LinkedIn engagement events in real-time across the entire team. Used alongside Trigify in the engagement-to-pipeline workflow.
`[D] | L30, L36`

### Sixsense **[active]**
Intent and active research monitoring. Used as a data sourcing trigger alongside LinkedIn Sales Nav and Crunchbase.
`[S] | N28`

### PredictLeads **[active]**
Hiring surges, funding events, technology adoption signals. API integration into Clay and Claude Code for signal layering.
`[D] | L31 | [P] | B18, B19, B29, B30`

### LoneScale **[ecosystem]**
Job change tracking. Mentioned in lemlist's stack and ColdIQ's lead generation layer.
`[D] | L35, L55`

### Midbound **[active]**
Website visitor identification. Part of the intent capture layer alongside Instantly and Vector.
`[D] | L18, L44`

### Unify **[ecosystem]**
Intent signal aggregation. Mentioned in ColdIQ funnel descriptions.
`[D] | L44, L51`

---

## Enrichment & Research

### Clay **[active]**
Central orchestration hub. Connects 100+ data providers. Runs waterfall enrichments, conditional qualification logic, AI agent tasks (Claygent), and scoring formulas. Replaced CSV download/upload cycles and killed virtual assistant workflow for first-line writing overnight. The "Swiss Army knife" of lead enrichment and list building.
`[S]→[D] | N6, N41, N62, L3, L11, L25, L30, L31, B6, B17`

### Prospeo (also spelled Prospero in some sources) **[active]**
Email finding and verification. Strong EMEA coverage. 98%+ email accuracy, 200M+ database. Typically runs first in European-focused waterfalls.
`[S]→[D] | N26, N63, L30, L31, B5, B11, B19`

### Lead Magic / LeadMagic **[active]**
Credit-based contact enrichment, high volume. Used in waterfall sequences and as final email validation.
`[S]→[D] | N26, N63, L30, B5, B12`

### Datagma **[active]**
Contact data enrichment. Mid-sequence in waterfall enrichments.
`[S] | N26, N30, N38, N63`

### Dropcontact **[active]**
Contact data enrichment. Mid-to-late sequence in waterfalls.
`[S] | N26, N30, N38, N63`

### Find Email **[active]**
Email finder. Late sequence in Clay waterfalls.
`[S] | N26, N30, N38, N63`

### FullEnrich **[active]**
Runs built-in waterfall across 15+ providers in a single request. Simplest option for email and phone enrichment. ColdIQ's "#1 tool for finding contact info." Especially used for phone number waterfalls.
`[D] | L6, L30, L31 | [P] | B5, B6, B11, B12, B19`

### Lima Data **[active]**
Email verification API used specifically in the Claude Code terminal workflow (not in Clay workflows).
`[S] | N43, N63`

### Wiza **[active]**
LinkedIn-direct contact extraction. 50+ data points. Most current data because it pulls from LinkedIn profiles directly. Preferred first in US-focused waterfalls.
`[D] | L31 | [P] | B11, B12, B19, B29`

### Icypeas **[active]**
Email finder. Part of the outbound data layer at $5M ARR.
`[D] | L11, L35`

### Clay Agent (Claygent) **[active]**
AI web scraper within Clay for custom data: company descriptions, press releases, LTV estimation, domain finding, business addresses. Stays inside Clay's environment.
`[S]→[D] | N41, N62, L18, B17, B29`

### Zenrows **[active]**
Social media handle extraction from company domains. Also used for anti-bot web scraping at scale.
`[S] | N39, N61 | [D] | L20`

### Serper **[active]**
Google Maps listings and search results via API. Used for local business data sourcing.
`[S] | N61 | [D] | L20`

---

## Verification

### DeBounce **[active]**
Email validation. Final verification step after waterfall enrichment returns an email. Used for standard (non-catch-all) emails.
`[S] | N26, N27, N30, N38`

### BounceBan **[active]**
Catch-all email verification specifically. Filters out risky catch-all addresses via Clay integration. Only includes catch-all emails in campaigns if BounceBan returns "deliverable" status.
`[S] | N27, N39`

---

## Sending & Sales Engagement

### Instantly **[active]**
Primary cold email platform. Multi-domain rotation, inbox warming, campaign sequencing, AI spam word checker, spintax support. Built-in deliverability infrastructure solved the "black box" problem. Also used for website visitor identification (newer capability).
`[S]→[D] | N19, N43, N65, L5, L6, L29, L31, B5, B6`

### Smartlead **[replaced]**
Alternative to Instantly. Optimized for high-volume cold email with no per-profile costs. Appeared in earlier ColdIQ stacks (Nov 2023) but does not appear in later stacks, suggesting it was evaluated and replaced by Instantly.
`[S] | N19, N65 | [D] | L50`

### lemlist **[active]**
LinkedIn outreach automation combined with email and phone sequencing in one platform. Multichannel sequences. AI copy generation (80% there, human refinement needed for sharp hooks/CTAs). ColdIQ's #1 multichannel recommendation. Also used to auto-trigger LinkedIn connection requests.
`[S]→[D] | N6, N65, L4, L6, L24, L31, B5`

### HeyReach **[active]**
Scales LinkedIn outreach by rotating multiple LinkedIn avatars, solving LinkedIn's per-account outreach limits.
`[S] | N65 | [D] | L25, L36`

### Orum **[ecosystem]**
High-volume cold calling platform.
`[S] | N65`

### Nooks **[ecosystem]**
High-volume cold calling platform. Used in Tier 1 manual multichannel outreach.
`[S] | N65 | [P] | B1`

### Sendspark **[ecosystem]**
Personalized video prospecting at scale.
`[S] | N65`

### Woodpecker **[active]**
Cold email sending platform. Appears in later ColdIQ stack descriptions alongside Instantly and lemlist.
`[D] | L32, L35, L55`

### Expandi **[ecosystem]**
LinkedIn automation. Mentioned in GTM Engineer tool stacks.
`[D] | L51 | [P] | B13, B30`

---

## CRM & Deal Closing

### HubSpot **[replaced]**
Was ColdIQ's primary CRM. Integrates with everything, centralizes data, tags intent, triggers sales alerts. Called "the dinosaur." Replaced by Attio in 2025. ColdIQ's take: teams under 100 people do not need a $50K/year CRM. HubSpot is also specifically rejected for cold email sending (designed for inbound marketing, causes spam).
`[S]→[D] | N67, L6, B6`

### Attio **[active]**
Modern customizable CRM for pipeline and triggers. AI-native with full API and real-time webhooks. Replaced HubSpot in 2025. "Best decision we made."
`[D] | L6, L31, L36, B6`

### Breakcold **[active]**
Social selling CRM. Tracks LinkedIn engagement natively. Used for sales enablement alongside Attio.
`[S] | N67 | [D] | L36, L55`

### Qwilr **[active]**
Digital sales room and proposal tool. Used for deal closing.
`[S] | N67 | [D] | L7, L25, L36`

### PandaDoc **[active]**
Contracts and proposals.
`[D] | L25, L36, L44`

### Attention **[active]**
AI note-taker for sales calls. Cross-conversation intelligence: queried 445+ calls to find "how prospects hear about us." Post-meeting auto-summary and CRM update saves 10-15 minutes per call. Needs 50+ calls per month for pattern detection.
`[S] | N67 | [D] | L7, L25, L31, L36, B17`

### Default **[active]**
Lead routing and scheduling tool. Smart forms for auto-routing inbound leads.
`[D] | L32, L36, L44`

### Cal.com **[ecosystem]**
Scheduling tool. Listed in Claude Code API layer.
`[D] | L31`

---

## Automation & RevOps

### Make.com **[active]**
Backend operations automation. Primary use cases: domain purchasing, mailbox setup, SPF/DKIM/DMARC record configuration, and the WhatsApp AI voice clone workflow. Replaced hours of manual infrastructure work. Makes 1,250 domains manageable.
`[S]→[D] | N19, N66, N80, N81, N86, L14`

### n8n **[active]**
Workflow orchestration for complex AI agent workflows. Replaced Zapier for advanced use cases. Runs the Intelligent Follow-Up workflow (calendar sync, meeting booking), four GTM agents (Lead Research, Local Prospecting, Brand Content Generator, Reddit Intel Collector), and the engagement-to-pipeline orchestration.
`[S]→[D] | N66, N83, N84, L14, L23, L33, B15`

### Cargo **[active]**
RevOps in Google Sheets. Runs the "Infinite Lookalike Machine": when a prospect replies positively, auto-generates 10 lookalike leads from that lead's data and dumps them back into the active sequence.
`[S] | N66, N84`

### Zapier **[replaced]**
General automation. Replaced by n8n and Make.com for complex workflows around 2024. Still used for simple form connections and Slack notifications.
`[D] | L7, L14`

### Relevance AI **[active]**
Custom multi-step AI agent builder. Powers signal analysis where agent weighs hiring activity, tech stack changes, and funding to determine buying intent vs. noise. Also used for internal workflows (weekly LinkedIn content digest agent, competitor monitoring).
`[D] | L12, L51 | [P] | B15, B17`

---

## Copywriting & AI

### Twain **[active]**
AI email generation from Clay trigger data. Generates fully AI-written emails based on enrichment variables.
`[S] | N54, N64`

### Claude Code **[active]**
Terminal-based end-to-end campaign automation. Replaces Clay UI interaction for campaign building. Setup: local folder with markdown files (copy framework, ICP scoring criteria) and API keys (Apollo, Lima Data, Instantly). One person plus Claude Code replaces a three-person campaign ops team. Builds complete outbound campaign in under 20 minutes. Also used for content creation (hook variations, repurposing, brainstorming angles with business context).
`[S]→[D] | N43, N76-79, L3, L31, B6, B11, B20, B25, X218`

### Claude (models) **[active]**
Used for ICP scoring alongside ChatGPT, content drafting with brand context (Claude project with 15-20 best posts and brand guidelines), and copy improvement.
`[S]→[D] | N112, L30, L54, B12, B20`

### ChatGPT / OpenAI API **[active]**
Job title cleaning, recruitment agency filtering, personalized lines inside Clay, ICP scoring, AI variable generation. Used across Clay workflows and n8n automations.
`[S] | N29, N36, N41, N62 | [D] | L30`

### Grammarly **[active]**
Spelling, tone, and clarity checking for 150+ monthly LinkedIn posts. Essential for Alex as a non-native English speaker.
`[S] | N68 | [D] | L17, L38`

### Octave/Opave **[ecosystem]**
Sales messaging tool to unlock copywriting flow. Minor mention, not detailed.
`[S] | N64`

---

## Scraping

### Apify **[active]**
Pre-built scraper actors for Google Maps (by Compass), LinkedIn (search + profile), Instagram, TikTok, YouTube, Yelp, ProductHunt, and more. Google Maps Scraper filters: must have website, >50 reviews, 4+ star rating. LinkedIn scraper requires session cookies for authentication. TikTok/Instagram scrapers extract hashtags, view counts, engagement metrics for UGC campaign targeting.
`[S]→[D] | N44, N45, N61, N69-71, L20, L33, B29`

### Instant Data Scraper **[active]**
Free browser extension for fallback web extraction. Zero setup.
`[S] | N61 | [D] | L20 | [P] | B29`

### Firecrawl **[ecosystem]**
AI-powered web scraping. Clean markdown/JSON from any URL, handles JavaScript rendering. Recommended when Claude Code's native browsing hits scale or anti-bot limits.
`[P] | B25, B29`

### Jina AI **[ecosystem]**
Similar capability to Firecrawl for clean data extraction from URLs.
`[P] | B25`

### Browse AI **[ecosystem]**
Website extraction tool for B2B data scraping.
`[D] | L20`

### PhantomBuster **[ecosystem]**
LinkedIn data extraction. Part of budget data scraping stack.
`[D] | L20`

### Airtop **[ecosystem]**
Browser-based scraping with login capability. Multi-step navigation.
`[P] | B29`

---

## Content Creation

### Scripe **[active]**
LinkedIn analytics, viral post search, and inspiration storage. Replaced both Taplio and Kleo as a combined solution. Aggregates posts by author to spot viral publications by topic.
`[S]→[D] | N68, L54, B20`

### Taplio **[replaced by Scripe]**
High-performing LinkedIn post search by topic. Used to find outlier posts (300+ likes, past month) and reverse-engineer hooks, structures, and CTAs. 30 minutes per week on ideation. Replaced by Scripe at the $6M ARR stage, though still appears in some stack snapshots.
`[S] | N68 | [D] | L17, L25, L36, L38, B20`

### Kleo **[replaced by Scripe]**
LinkedIn engagement metrics across profiles. Reverse-engineer high-performing posts. Replaced by Scripe.
`[D] | L17, L38`

### Figma **[active]**
Carousel and infographic design. Team designers (Ada, Pilar, Maria Luisa) use Figma for visual assets. Carousel posts consistently outperform all other LinkedIn formats.
`[S] | N68 | [D] | L38, B5, B20`

### Canva **[active]**
Beginner-friendly design for carousels and infographics. Alternative to Figma for simpler visual assets.
`[S] | N68 | [D] | L11, L38`

### Notion **[active]**
Central content hub and calendar. All content drafts organized here. Weekly workflow: Sunday ideation, Mon-Fri drafting. Also used for SOPs and content coordination across the team. Manually copy-paste from Notion to LinkedIn (no schedulers).
`[S]→[D] | N68, N117, L11, L17, L25, L36, L38, B20`

### OpusClip **[active]**
AI-powered long-form video to short-form clips. Got 50K+ views on repurposed clips.
`[S] | N68 | [D] | L17, L38, B20`

### Ezgif / Easy GIF **[active]**
Video to GIF conversion. GIFs get higher LinkedIn impressions than raw video because they auto-play when muted in the feed.
`[S] | N68 | [D] | L17, L38`

### Screen Studio **[active]**
Mac screen recording with auto-zoom.
`[D] | L38, B20`

### 11 Labs **[active]**
Professional voice cloning. Trained on high-quality, background-noise-free audio from Alex's YouTube and podcast appearances. Replicates his French accent. Used in the WhatsApp AI voice clone workflow.
`[S] | N68, N81`

### Tella **[active]**
Screen recording tool. Mentioned in content creation stacks.
`[D] | L36, L54`

### Descript **[ecosystem]**
Video/audio editing. Appeared in earlier stack snapshots.
`[D] | L25`

---

## SEO & Website

### Ahrefs **[active]**
Keyword research and SEO analysis. Part of the content engine alongside Surfer.
`[D] | L11, L25, L36, L44, L54`

### Surfer **[active]**
Content optimization for SEO.
`[D] | L36, L44, L54`

### Webflow **[active]**
Website CMS.
`[D] | L36, L44`

### AirOps **[active]**
SEO content automation. Part of the lead generation layer. Also referenced in the AirOps ABM case study ($3M pipeline).
`[D] | L35, L44, L55 | [P] | B7`

### Wistia **[active]**
Video hosting and analytics for website VSLs.
`[D] | L36, L44`

---

## Newsletter & Email Marketing

### beehiiv **[active]**
Newsletter platform. 4x/week newsletter cadence.
`[D] | L25, L36, L44, L54`

### Customer.io **[active]**
Email marketing and automated nurture sequences. Used for lead management and follow-up.
`[D] | L7, L35, L44, L55`

---

## Finance & Operations

### Stripe **[active]**
Payment processing.
`[D] | L25, L36`

### Mercury **[active]**
Banking.
`[D] | L25, L36, L54`

### Revolut **[active]**
Banking (secondary).
`[D] | L25`

### Ramp **[active]**
Corporate card and expense management.
`[D] | L36`

### Fuelfinance **[active]**
Financial analytics and reporting.
`[D] | L25, L36`

### Puzzle **[active]**
Process mapping.
`[D] | L36, L54`

### Hyperline **[active]**
Billing, subscriptions, and usage metering. Replaced Salesforce CPQ (end-of-sale March 2025). Handles hybrid usage-based pricing.
`[D] | L31 | [P] | B6`

### Airtable **[active]**
Database and operational tracking alongside Notion.
`[D] | L25, L36`

---

## Tools Tested and Rejected

| Tool | Why Rejected |
|------|-------------|
| HubSpot (for cold email) | Designed for inbound marketing. Causes spam. `[S] | N73` |
| Single email finders (Apollo alone) | 45-50% success rate. Must use waterfall. `[S] | N73` |
| LinkedIn schedulers (native + third-party) | Hurt organic reach. Organize in Notion, copy-paste manually. `[S]→[D] | N73, N117, L17` |
| Outreach / Salesloft (legacy SEPs) | 5-10% open rates. Per-seat pricing model. `[S]→[D] | N73, L4` |
| Smartlead | Appeared in early stacks, absent from later ones. Replaced by Instantly. `[D] | L50` |
| Humanlinker | DISC personality analysis for outreach. In early stack (Nov 2023), absent later. `[D] | L50` |
| Sybill | AI transcription. In early stack, replaced by Attention. `[D] | L50` |
| ZoomInfo | $30K/year. Replaced by Clay + FullEnrich at a fraction of the cost. `[P] | B6` |

---

## Tool Evaluation Criteria

ColdIQ's framework for evaluating new tools:

1. **Reliability and community usage** — check reviews, ratings, usage volume
2. **Data accuracy** — read docs to confirm specific outputs match needs
3. **Integration/centralization** — prefer tools that connect to the existing stack (HubSpot was chosen because it integrates with everything; Clay was chosen because it eliminated CSV cycles)
4. **Deliverability** — email tools evaluated on secondary domain handling, inbox rotation, warm-up quality
5. **Pricing vs. volume** — compare per-result vs. per-run pricing, test free tiers first

Budget-friendly Clay alternative: Cargo extension plus OpenAI API keys can achieve similar AI research capability for under $200/month.
`[S] | N72, N74`
