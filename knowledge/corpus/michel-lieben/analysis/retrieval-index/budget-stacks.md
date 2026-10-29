---
type: corpus
aliases: ["Budget Stacks -- Michel Lieben"]
corpus: michel-lieben
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
---

# Budget Stacks -- Michel Lieben

**Corpus:** michel-lieben
**Generated:** 2026-03-25

---

## Under-$200/Month Cold Email Stack

Michel's recommended entry-level stack for founders and early-stage teams who can't afford premium tools.

| Tool | Function | Monthly Cost | Notes |
|------|----------|-------------|-------|
| Apollo | Data sourcing (leads by firmographics) | ~$49 | Free plan available to start |
| Smartlead | Email sequencing (automated sending) | $39 | Entry-level plan, up to 6K contacts |
| HeyReach | LinkedIn outreach (multi-account) | Fits remaining budget | Exact cost not specified |
| Google Sheets + Cargo extension | AI qualification + personalization | Free (extension) | Install Cargo extension into Google Sheets |
| OpenAI API | AI-powered lead research + copy | Usage-based (minimal) | Connected via Cargo extension |

**Total:** Under $200/month

### The Cargo+OpenAI Workaround

This is Michel's budget alternative to Clay (which starts at $149/month).

**Workflow:**
1. Extract leads from Apollo into Google Sheets
2. Install free Cargo extension in Google Sheets
3. Connect OpenAI API key
4. Use Cargo+OpenAI inside the spreadsheet to:
   - Search and qualify leads against specific criteria
   - Generate personalized opening lines
   - Build automated "lookalike" loops (detect conversion, auto-generate 10 similar leads)

**Vs. Clay:**
- Clay advantage: one subscription gives access to dozens of data sources via Clay credits. No individual API key management. Simpler setup.
- Cargo advantage: own API keys enable "much more complex workflows." Better for later-stage companies who need deeper customization.
- Michel's recommendation: if budget allows, just use Clay for ease of use. Cargo+OpenAI is "messier to set up" but functional at a fraction of the cost.

**Provenance:** [S]->[D] (NotebookLM Q6, Q7 confirmed by LinkedIn/Blog)

---

## Tool Evaluation Criteria

Michel evaluates sales technology based on practical function, not brand recognition or paid reviews.

**Primary criteria:**
1. **Deliverability over everything.** For email sequencers, the #1 question is: can it reliably get messages into the primary inbox? Prioritize platforms with secondary domain setup, inbox rotation, and warm-up pools.
2. **Cost-efficiency for core pillars.** A stack needs to handle data extraction, sequencing, and personalization. One tool per pillar is enough.
3. **Expert usability over biased reviews.** G2 reviews are heavily biased toward large companies paying for intent data packages. Michel built ColdIQ's directory to evaluate tools based on how GTM experts actually use them in real campaigns.

**What he rejects:**
- **Legacy sales engagement platforms** (Outreach, SalesLoft) for cold email. Smaller, newer platforms innovate faster. Many teams on legacy platforms struggle to get 10% open rates. Direct advice: "just change tool."
- **Premium enrichment on strict budgets.** Clay is excellent but $149/month minimum. Use Cargo+OpenAI workaround instead.
- **All-in-one AI SDRs without a proven motion.** If you haven't manually proven your product can be sold via cold outreach, plugging an AI tool into it automates failure.

**Provenance:** [S]->[D] (NotebookLM Q8 confirmed by LinkedIn posts)

---

## Full Agency Stack (at various ARR stages)

Michel has published his complete tool stack at multiple revenue milestones. The stack grows over time but the core categories remain stable.

### Stack at $7M ARR (Feb 2026)

**Content:**
- Taplio, Scripe (LinkedIn ideation)
- Figma, Adobe Suite (design, team of designers)
- Claude Code via Conductor (copywriting, hook variations, repurposing)
- Tella, Screen Studio (video recording)
- OpusClip (AI short-form video)
- Ahrefs, AirOps (SEO, programmatic SEO)
- beehiiv (newsletter)
- Notion (content calendar + project management)
- Grammarly (non-native English correction)

**Outbound:**
- Clay (central orchestration, waterfall enrichment, AI scoring)
- Apollo, Openmart, LinkedIn, Wiza (data sourcing)
- Prospeo, Icypeas, LeadMagic, FullEnrich (email/phone enrichment)
- Common Room, Teamfluence, Trigify (intent signals)
- PredictLeads (company signals: hiring, funding, tech adoption)
- Instantly, lemlist, Expandi, Woodpecker (sales engagement)
- Midbound, Vector, RB2B (visitor identification)

**Agency Management:**
- Airtable (operations, source of truth)
- Notion (project management, documentation)
- n8n, Make (automation)
- Relevance AI (agentic workflows)
- Puzzle (process mapping)
- Slack, Google Meet, Norrsken Barcelona (communications)

**Inbound Funnel:**
- Webflow (website)
- Wistia (VSL hosting)
- Default (lead routing)
- Google Analytics, Usermaven (traffic tracking)
- HockeyStack (channel attribution)
- Breakcold (social selling)
- Customer.io (email marketing, lead nurture)
- Lovable, Vercel (mini-tools)

**Sales:**
- Attio (CRM, replaced HubSpot)
- Attention (meeting recording + notes)
- Qwilr, PandaDoc (proposals, contracts)
- Hyperline (CPQ)
- Stripe (recurring payments)
- Ramp (payments + expenses)
- Mercury, Revolut Business (banking)

**AI/Automation:**
- Claude Code (campaign building, content, custom tooling)
- Conductor (Claude Code interface)
- Relevance AI (agent builder)
- n8n (workflow automation)
- OpenAI, Claude APIs (lead scoring, qualification, copy generation)
- Apify (web scraping)

**Provenance:** [D] (LinkedIn posts across multiple dates, confirmed by blog)
