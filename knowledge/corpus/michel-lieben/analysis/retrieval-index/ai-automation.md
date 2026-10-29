---
type: corpus
aliases: ["AI Automation -- Michel Lieben"]
corpus: michel-lieben
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
---

# AI Automation -- Michel Lieben

**Corpus:** michel-lieben
**Generated:** 2026-03-25

---

## Claude Code Autonomous GTM Brain

ColdIQ's most advanced automation: a single terminal session that handles the complete outbound campaign workflow without tool-to-tool handoffs.

### Architecture
- **32 skills, 12 agents, 2,108 files** in ColdIQ's Claude Code GTM system
- Hosted by Kenny Damian (Head of GTM) and Ivan Falco (Head of Growth)
- Live-demonstrated to 1,400 viewers on Feb 26, 2026

### Campaign Build Workflow
1. **Input:** Drop a CSV of target companies into a folder. Write natural language prompt with scoring criteria.
2. **ICP Scoring:** Claude Code reads every company, assigns priority score based on industry fit, company size, growth signals, tech stack. Understands context (50-person company that just raised Series A scores differently from 50-person company flat for 2 years). Output: ranked list with Tier 1/2/3 accounts. Takes under 3 minutes vs. 45 minutes manually.
3. **Waterfall Email Enrichment:** First call to Apollo API. For contacts Apollo misses, automatically cascades to Prospeo, then FullEnrich, then Wiza/LeadMagic. Filters out low-confidence results. Single loop in the script, no manual CSV exporting between tools.
4. **Copy Generation:** Fed historical best-performing templates as reference material. Copywriting rules: under 100 words, no jargon, subject lines that look like colleague sent them, yes/no CTAs, first line answers "why you, why now." Different triggers produce different copy variations within the same campaign structure.
5. **Campaign Upload:** Pushes complete campaign (leads, sequences, copy) directly into Instantly. Zero manual steps from scoring to send.

**Performance:** Original demo: 57 seconds for the complete workflow. Live demo with audience: under 20 minutes for full campaign.

### Use Cases Beyond Outbound
- **Paid media:** Automated campaign creation, reporting, and optimization across LinkedIn, Meta, and Google ads. Run entirely from terminal.
- **RevOps:** Campaign diagnostics that took hours done in 60 seconds. Live dashboards pulling every data source into one view. Bidirectional CRM sync: Attio, Lemlist, and Instantly.
- **Content creation:** Hook variations, content repurposing, brainstorming angles via Conductor interface.
- **Mini-tools:** Sacha builds interactive SEO tools with Claude Code, deployed via Lovable/Vercel.

---

## 19-API Stack for Claude Code GTM

Organized by functional layer:

### Signal Layer
| API | Function |
|-----|----------|
| PredictLeads | Hiring spikes, funding rounds, tech adoption across 110M+ companies |
| Common Room | Consolidates community, product, and GTM signals from GitHub, Discord, LinkedIn, G2 |
| Attention | Captures and analyzes sales calls. Natural language search across conversation history. Competitor mentions and objections. |
| Midbound / RB2B / Vector | De-anonymize website visitors at the person level |

### Data Layer
| API | Function |
|-----|----------|
| Prospeo | 98%+ verified email accuracy. Person/company enrichment. 200M+ contact database. |
| FullEnrich | Cascades through 20+ providers for verified emails and phones. 80%+ find rates. |
| Openmart | 200M+ local business records. Filter by category/location. |
| Apollo | B2B contact and company data. Search, filter, enrich at scale. |
| Wiza | LinkedIn profile to verified contact data. 50+ data points. |
| Apify | Pre-built scrapers for LinkedIn, Google Maps, Instagram, any website. |

### Action Layer
| API | Function |
|-----|----------|
| Instantly | Cold email campaigns, warmup, analytics, webhooks on replies |
| lemlist | Multichannel sequences: email + LinkedIn + calls |
| LinkedIn Ads | Programmatic campaign building, audience sync, retargeting |

### Automation Layer
| API | Function |
|-----|----------|
| Relevance AI | Agentic layer for building workflows on top of Claude Code/Codex |
| n8n | Workflow orchestration for AI agents and API workflows |

### System of Record
| API | Function |
|-----|----------|
| Attio | AI-native CRM with full API access. People, companies, deals, custom objects, lists, tasks, real-time webhooks. |

### Conversion Layer
| API | Function |
|-----|----------|
| Cal.com | Scheduling infrastructure. Embed booking links, auto-route meetings, sync to CRM. |

### Revenue Layer
| API | Function |
|-----|----------|
| Hyperline | Billing, subscriptions, usage metering, invoicing. Webhooks for payment events. |
| Dreamdata | B2B revenue attribution. Tracks every touchpoint from first signal to closed deal. |

---

## Agent Taxonomy

Michel distinguishes three tiers of automation. Most of what companies call "AI agents" are actually the middle tier.

### A. Non-Agentic Workflows
- Human does all thinking
- AI helps with content generation only
- Example: Manager remembers it's time for business review, checks CRM, prompts ChatGPT to write email, copy-pastes output
- AI takes no initiative

### B. Agentic Workflows
- AI is part of automated system with triggers and logic
- Semi-autonomous, saves time
- Cannot adapt to unexpected scenarios
- Example: Calendar automation detects 90 days since last review, checks availabilities, triggers GPT-4 to draft email, sends automatically
- Does not handle rescheduling, follow-up, or context changes

### C. True AI Agents
- Goal-oriented objective ("keep client engaged and happy")
- Constantly monitors CRM, past conversations, activity
- Detects situations AND checks additional context (usage drop, billing tier)
- Drafts personalized messages referencing specific data
- Monitors response, automatically follows up with alternatives
- Creates agendas from previous conversations, notifies team of red flags
- Personalized, contextual, coordinates multiple tools
- Focused on broad goal (client satisfaction) instead of narrow task (sending email)

---

## AI SDR Position

Michel holds a nuanced view on AI SDRs that sounds contradictory but is internally consistent.

**Warning against:** Never buy AI SDRs without first proving a sales motion manually. Write 50-150 emails by hand. Discover which messaging works. Only then automate. Using AI SDRs to skip the manual phase is "a recipe for failure."

**Bullish on:** Vertical-specific AI SDRs are "very close to being better than human SDRs at email prospecting." AI models already outcompete the average seller. Top-tier creative humans will always win. But the average SDR is being surpassed. Michel admits this is a "controversial take" in unscripted podcast settings.

**Resolution:** The warning is about sequencing (manual first, automation second). The bullishness is about capability (AI is already good enough for email prospecting once the motion is proven).

---

## Clay Formula Trick (Hallucination Prevention)

When using AI inside Clay to generate personalized first lines, a common failure mode is the AI inserting conversational filler:
- "The final answer is: [Personalized Line]"
- "Here's what I came up with: [Line]"

**Fix:** Use Clay's "formula" feature. Set a strict rule that only allows the output to pass into the email sequencer if it starts with the exact formatting you requested. This catches junk data before any email is sent. Prevents embarrassing hallucinations from reaching prospects.

**Provenance:** [S] (NotebookLM Q25, attributed to Alex Vacca)

---

## Automation Patterns

### Onboarding Automation (n8n)
- Automated client onboarding processes
- GSuite to Supabase to Stripe to Slack sync
- Automated admin tasks: Slack invites, onboarding links, secondary domain setup
- Frees GTM Engineers to focus on value-adding work (custom ICP matrix, creative campaigns, copy)

### Lead Scoring Pipeline
- Engagement data (LinkedIn likes, profile views, website visits) flows into Clay
- Clay enriches with firmographic and technographic data
- OpenAI/Claude scores against ICP criteria (B2B vs. B2C, geography, industry, company size, decision-maker seniority)
- Scored leads segmented into tiers
- Tier-appropriate outreach triggered automatically

### Lookalike Generation Loop
- When a lead successfully converts in a campaign, automation detects the conversion
- Tool (Ocean.io or Clay) automatically generates 10 "lookalike" leads matching the same profile
- New leads feed directly back into the winning sequence
- Continuous, self-feeding pipeline

---

## AI Coding Stack

Michel's AI coding stack for GTM engineering:

| Platform | Role | Cost | Notes |
|----------|------|------|-------|
| Conductor | Primary UI wrapper | Included | Wraps Claude Code + Codex, runs agents in parallel, manages branches |
| Claude Code | Central GTM engine | $200/mo Max | APIs, MCPs, list building, enrichment, copy, campaign uploads |
| OpenAI Codex | Backup for complex tasks | $20/mo | Fed full conversation when Claude fails; typically solves the issue |
| Cursor | Rejected | -- | First AI coding tool Michel used; abandoned for Claude Code's better concurrent agents + outputs |
| Lovable | Prototyping only | -- | Most user-friendly; used for first mini-tools; graduated to Claude Code for production |
| Vercel | Hosting | Free tier | All mini-apps deployed here; entire website migrated from Webflow |
| GitHub | Code repository | Standard | All AI-generated repos and scripts |

### Why Claude Code Won
- $200/month nearly unlimited plan enables running multiple agents concurrently
- Models consistently produced better outputs for GTM workflows than same models via Cursor
- Conductor solved the UI gap (terminal was "ugly" compared to Cursor's interface)
- Natural language prompts replace formula rebuilds; scoring criteria updated by editing plain English

### Social Engager Agent (LinkedIn -> Clay -> Outbound)
1. Input a high-performing LinkedIn post URL
2. Claude Code scrapes all engagers (likes, comments)
3. Data pushed to Clay table
4. Enrichments run: ICP scoring, CRM dedup, blocklist check, lead routing
5. Qualified leads pushed to Instantly for email sequences
6. Previously cost $300+/month in scraping tools; now handled by Claude Code

### LinkedIn Ads API Automation (Ivan Falco)
1. Google Sheet as command hub: campaign group, name, targeting, ad copy, Drive folder reference
2. Claude Code reads sheet via API, summarizes proposed actions
3. On confirmation, builds entire campaign via LinkedIn API
4. Targeting uses saved audiences (bottom-of-funnel, ABM company lists)
5. Bulk updates for biddings, account lists, campaign modifications
6. Built via Claude Code "plan mode" trial-and-error; successful code saved as reusable "skills"
7. Custom UI built on top for non-technical team members
8. Results: $15 CPM, $472K at 3x ROI for clients in 6 months
