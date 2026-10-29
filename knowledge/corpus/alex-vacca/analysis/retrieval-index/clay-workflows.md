---
type: corpus
aliases: ["Clay Workflows — Retrieval Index"]
corpus: alex-vacca
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
---

# Clay Workflows — Retrieval Index

**Corpus:** Alex Vacca
**Knowledge type:** [CW] Clay Workflows
**Last updated:** 2026-03-24

---

## Job-Opening Trigger Workflow

The most detailed Clay workflow in the corpus. Monitors hiring signals and converts them into personalized outbound campaigns.

**Step 1: Signal capture**
Trigify monitors LinkedIn, Greenhouse, and Indeed for specific role postings (e.g., SDRs, BDRs). Filter parameters: 10-1,000 employees, posted within last 30 days. Trigify pushes matching leads to Clay daily via webhook.
`[S]→[D] | N36, L22, L30`

**Step 2: Company name normalization**
AI strips "LLC," "GmbH," and other suffixes from company names so they read naturally in email subject lines and body copy.
`[S]→[D] | N29, N36, N41`

**Step 3: Recruitment agency filter**
ChatGPT prompt reads the job description and looks for phrases like "our client is" or "on behalf of our client." Conditional formula halts the workflow if a recruitment firm is detected. This prevents outreach to intermediaries who cannot buy.
`[S] | N36, N41`

**Step 4: Dynamic decision-maker targeting**
Conditional logic based on company headcount:
- Under 50 employees: target CEO, Founder, Managing Director, COO
- Over 50 employees: target VP of Sales, Director, CRO

Also finds a colleague in the same department for a name-drop in follow-up emails.
`[S]→[D] | N29, N36`

**Step 5: Waterfall email enrichment**
Sequential provider testing (see Waterfall Enrichment section below). Final validation via DeBounce. Catch-all emails routed through BounceBan.
`[S]→[D] | N26, N36, N38, L30`

**Step 6: AI variable generation**
AI generates:
- 3 outbound campaign ideas based on the company description
- An icebreaker summary of what the company does
- Salary calculation by role and geographic location (e.g., "GBP 45,000 for an SDR in the UK")

The salary figure becomes a financial comparison hook in the email: "The average salary for this role in [Location] is [Salary]. If we could generate 3x more qualified leads for a third of the cost..."
`[S] | N36, N37, N41`

**Step 7: Push to sending platform**
Assembled campaign pushed to Smartlead or Instantly with spintax applied to greetings and variable fields.
`[S] | N36`

---

## 500-Lead Qualification Workflow

A scoring workflow that qualifies leads before they enter any outreach sequence. Each criterion adds a check to a composite scoring formula. Only "high" priority leads get outreach.

**Scoring criteria:**

1. **BounceBan catch-all verification** — pass if status returns "deliverable"
2. **Semrush monthly web traffic** — pass if site has over 5,000 monthly visitors
3. **Social media presence** — Zenrows extracts Facebook, Instagram, YouTube handles from company domain
4. **Recent press/news** — Clay Agent scrapes for press releases, news mentions, or funding announcements; pass if found
5. **Headcount growth** — pass if company grew over 15% in the last 3 months
6. **Active job openings** — pass if company has more than 4 open positions

**Additional data points checked:**
- Company tech stack (HubSpot, Salesforce, etc.)
- Whether the specific prospect has posted on LinkedIn recently (enables icebreaker personalization)

Final formula calculates composite priority score. Outreach begins only with high-priority prospects.
`[S] | N39, N40`

---

## LinkedIn Engager Workflow

Captures engagement on LinkedIn content (likes, comments, profile views) and routes qualified engagers into outbound sequences.

**Step 1: Engagement capture**
Trigify and Teamfluence capture real-time engagement events (likes, comments, profile views, company page activity) from LinkedIn posts.
`[S]→[D] | N109, L30, B12`

**Step 2: Enrichment in Clay**
Clay enriches each contact: job title, company size, tech stack, hiring signals, funding status.
`[S]→[D] | L30, B12`

**Step 3: AI qualification scoring**
ChatGPT and Claude score each lead against ICP criteria: B2B vs. B2C, geographic fit, industry match, company size, estimated customer lifetime value, seniority and function. Unqualified contacts are filtered out to save enrichment credits.
`[S]→[D] | L30, B12`

**Step 4: CRM deduplication**
Check against Attio (or HubSpot) for existing customers, active conversations, and net-new status. Only net-new leads proceed.
`[S]→[P] | B12, L30`

**Step 5: Waterfall email enrichment**
Prospeo > FullEnrich > LeadMagic. Stacking three providers pushes coverage close to 95%.
`[D] | L30`

**Step 6: Contextual outreach**
Personalized email references the exact post they engaged with. High-priority leads get multichannel outreach via lemlist (email plus LinkedIn). Standard leads get email-only via Instantly.
`[S]→[D] | N109, L30, B12`

**Step 7: CRM logging**
All activity logged to Attio/HubSpot, sales team alerted for high-intent leads.
`[S]→[D] | N109, L30`

System runs 24/7 without human intervention. ColdIQ reports 144 meetings in one month from this workflow.
`[D] | L30`

---

## Website Visitor Workflow

Converts anonymous website visitors into qualified outreach targets.

**Step 1: Visitor identification**
RB2B (US only) or Vector identifies the person visiting the website.
`[S]→[D] | N46, N75, B6`

**Step 2: Domain fill**
Clay Agent fills in missing company domain via web search if RB2B/Vector only returned partial data.
`[S] | N46, N87`

**Step 3: CRM exclusion check**
Halt workflow if the visitor is already in HubSpot/Attio pipeline as an active deal. Prevents annoying prospects who are already in conversation.
`[S] | N46, N75, N87`

**Step 4: AI tier scoring**
AI evaluates the visitor's company by industry, description, and employee count. Assigns Tier 1, 2, or 3.
`[S] | N87`

**Step 5: Contact discovery**
If Tier 1, Apollo finds GTM leaders at the visitor's company.
`[S] | N46, N87`

**Step 6: Dual-channel outreach**
Simultaneously triggers LinkedIn connection request via Lemlist and email sequence via Instantly.
`[S] | N46, N87`

Books approximately 1 meeting per day.
`[S] | N5`

---

## Waterfall Enrichment

The core enrichment pattern used across all workflows. Sequential testing of multiple email-finding providers to push contact coverage from approximately 50% (single provider) to 75-95%.

**The principle:** Run providers in sequence. Each provider is called only for contacts where the previous provider returned no result. This maximizes coverage while controlling costs through conditional runs.

**Provider sequences vary by context:**

NotebookLM versions:
- Prospero > Lead Magic > Datagma > Dropcontact > Find Email `[S] | N26`
- Prospero > Datagma > Dropcontact > Find Email > Lead Magic `[S] | N30`
- Apollo > Prospero > Lead Magic > Datagma > Dropcontact > Find Email `[S] | N38`
- Prospero > Datagma > Dropcontact > Find Email > Lima Data (Claude Code) `[S] | N63`

LinkedIn version:
- Prospeo > FullEnrich > LeadMagic (stacking 3 = approximately 95%) `[D] | L30`

Blog versions:
- Apollo > Prospeo > FullEnrich > Wiza/LeadMagic `[P] | B11`
- Wiza > Prospeo > FullEnrich > LeadMagic (LinkedIn-to-pipeline workflow) `[P] | B12`
- FullEnrich alone (runs 15+ providers in single request) `[P] | B19`

**Coverage rates:**
- Single provider: 40-60% `[S]→[P] | N38, B19`
- Waterfall (multi-provider): 70-90% `[S]→[P] | N38, B19`
- Stacking 3+ providers: approximately 95% `[D] | L30`

**Geographic logic:** Prospeo first for European contacts, Wiza first for US contacts. `[P] | B19`

**Reconciled guidance:** The specific provider order is not fixed doctrine. Alex states the order can be customized. The agent should treat waterfall as a principle (sequential testing until found) rather than a fixed sequence. FullEnrich shortcuts the question entirely by running 15+ providers in a single request.
`Pass 2 Tension 3 reconciliation`

**Validation step:** Once an email is found, run final validation via DeBounce or Lead Magic. Catch-all emails get a separate pass through BounceBan via Clay integration. Only include catch-all emails if BounceBan returns "deliverable." If verification fails, exclude entirely to protect sender reputation.
`[S] | N27, N30`

---

## Waterfall Personalization

A cascading personalization approach where Clay tries progressively broader icebreakers until one succeeds. Used in a 65-step Clay automation that generated 657 leads for a $1M recruitment client.

**Cascade order:**
1. If prospect posted on LinkedIn in the last 2 weeks, reference their content
2. No recent post? Check for recent hires in their department, congratulate on the growth
3. No hiring signal? Look for work anniversaries, mention the milestone
4. Nothing found? Default to niche expertise icebreaker

Content-based CTAs instead of meeting requests. "Target the right people first. Personalize next. Automate last."
`[D] | L28`

---

## AI Agent Tasks Inside Clay

Distinct AI micro-tasks that each produce a variable for copy or qualification. These run as individual Clay Agent or ChatGPT calls within Clay tables.

1. **Company name + job title normalization** — strip LLC/GmbH, remove location tags, simplify long titles
2. **Recruitment agency filtering** — ChatGPT prompt reads job descriptions for intermediary language
3. **Outbound idea generation** — "come up with three creative outbound ideas based on the company description"
4. **Salary estimation** — estimate average yearly salary for the target role by geographic location
5. **Customer LTV determination** — "does this company have a product/service with LTV over $1,000?"
6. **Seniority level classification** — categorize as entry/mid/senior/director/VP/C-suite/partner/consultant
7. **Business address extraction** — pull physical address for localized outreach
8. **Recent news/press release scraping** — find recent mentions for icebreaker material
`[S] | N41`

**Quality control for AI outputs:** Conditional formulas in Clay only accept AI output if it starts with expected words. This blocks broken or robotic outputs (e.g., "The final answer is [snippet]") from entering the email sequence.
`[S]→[P] | N42, N54, B23`

---

## 12 Claude Skill Files for Clay

Named Claude Skill files built from hundreds of Clay tables across 80+ B2B clients:

1. Company Research Agent
2. Personalization Writer
3. ICP Scorer
4. LinkedIn Profile Analyzer
5. Data Cleaner & Normalizer
6. Objection Handler
7. Email Sequence Writer
8. Competitor Analyzer
9. Job Posting Analyzer
10. Technographic Qualifier
11. News & Signal Synthesizer
12. Account Brief Generator

Usage: drop skill file into Clay, map columns, run. The actual contents of these files are behind a lead magnet and remain a confirmed gap in the corpus. Two files are partially described: a Copy Framework markdown (word count 50-80, subject line format, CTA format) and a Scoring Criteria markdown (points by industry, employee count, funding stage, revenue, tech stack, classifying into Tier 1/2/3).
`[D] | L3, X218 | Gap: file contents are [A] Absent`

---

## 4 Sourcing Stacks

Different Clay configurations for different prospecting situations.

**Stack 1 — Broad B2B:** Apollo or LinkedIn Sales Nav > export via Wiza > Clay waterfall enrichment > campaign in a day.

**Stack 2 — Niche vertical:** Exa Websets or Claygent for AI sourcing > Apify for industry directories > FullEnrich for maximum coverage. Produces lists competitors cannot replicate.

**Stack 3 — Competitor displacement:** BuiltWith + PredictLeads for technographics > focus on recent competitor churn or complementary tool adoption > TheirStack job postings to confirm investment > Prospeo/Wiza for contacts.

**Stack 4 — Intent-driven prioritization:** Broad list from any database > layer PredictLeads + Common Room intent signals > score by signal type and recency > 2+ signals in 30 days = priority outreach, single signal = nurture sequence.
`[P] | B18, B19`

---

## Mobile Number Waterfall

Same sequential testing logic as email waterfall, but for finding prospect mobile phone numbers. FullEnrich is specifically recommended for phone numbers.
`[S] | N47, N63`

---

## Recent LinkedIn Post Scraping

Workflow scrapes the target prospect's most recent personal LinkedIn post so AI can reference it as a personalized icebreaker in email copy. Distinct from company-level icebreakers.
`[S] | N48`
