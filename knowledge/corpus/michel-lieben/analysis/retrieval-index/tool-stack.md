---
type: corpus
aliases: ["Tool Stack -- Michel Lieben"]
corpus: michel-lieben
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
---

# Tool Stack -- Michel Lieben

**Corpus:** michel-lieben
**Generated:** 2026-03-25

---

## Tool Inventory by Category

### Data Sourcing
| Tool | What ColdIQ Uses It For | Michel's Take |
|------|------------------------|---------------|
| Apollo | B2B contact and company data. Firmographic/technographic filtering at scale. Primary database in budget stack. | $49/mo entry. First provider in waterfall enrichment. Free plan available. |
| Openmart | 200M+ local business records. Filter by category and location. | Good for niche/local targeting. |
| LinkedIn Sales Navigator | Account-level research, prospect discovery. | Used as data source alongside Apollo. |
| Ocean.io | "Lookalike" list generation from converting companies. | Feed successful companies in, get similar ones out. Keeps winning sequences fresh. |
| Wiza | LinkedIn profile to verified contact data. 50+ data points per contact. | Part of waterfall enrichment cascade. |
| Apify | Pre-built scrapers for LinkedIn, Google Maps, Instagram, any website. | Thousands of "mining actors." Used for conference attendee lists, bulk data extraction. |

### Email & Phone Enrichment
| Tool | What ColdIQ Uses It For | Michel's Take |
|------|------------------------|---------------|
| Prospeo | 98%+ verified email accuracy. Person/company enrichment, domain search. | Strong on European domains. Core email finder. |
| FullEnrich | One API cascading through 20+ providers for verified emails and phones. 80%+ find rates. | ColdIQ's #1 platform for phone numbers. $0 to $1.8M ARR in year 1. |
| LeadMagic | Email and phone finding. | Part of waterfall cascade. |
| Icypeas | Email enrichment. | Used alongside Prospeo and LeadMagic. |

### Intent Signals
| Tool | What ColdIQ Uses It For | Michel's Take |
|------|------------------------|---------------|
| Common Room | Consolidates community, product, and GTM signals. GitHub, Discord, LinkedIn, G2. | "The most comprehensive signal platform." |
| PredictLeads | Hiring spikes, funding rounds, tech adoption across 110M+ companies. | Feeds into ICP scoring and Clay enrichment. |
| Teamfluence | Auto re-engage LinkedIn engagers and profile viewers. | Monitors social interactions for outbound triggers. |
| Trigify | LinkedIn social interaction monitoring. | Used alongside Teamfluence. |
| Unify | Intent signals. | Part of signal stack. |

### Visitor Identification
| Tool | What ColdIQ Uses It For | Michel's Take |
|------|------------------------|---------------|
| RB2B | Person-level website visitor identification. | "Wow effect" for agency clients: install tracking script, client sees exact names/titles in Slack. |
| Midbound | De-anonymize website visitors. | Part of visitor ID stack. |
| Vector | De-anonymize website visitors. | Part of visitor ID stack. |

### Sales Engagement
| Tool | What ColdIQ Uses It For | Michel's Take |
|------|------------------------|---------------|
| Instantly | Cold email campaigns, warmup, analytics, webhooks on replies. | "No one ships faster." Best for all-in-one emailing. Primary sending platform (~70% of volume). Budget entry at $39/mo (via Smartlead alternative). |
| lemlist | Multichannel sequences: email + LinkedIn + calls + WhatsApp. | Best at multichannel outreach. $34M ARR umbrella with Taplio, Tweet Hunter, lemcal. |
| Smartlead | Cold email sequencing. | Budget-friendly at $39/mo. Part of budget stack. |
| Woodpecker | Cold email. | Client-dependent choice. |
| HeyReach | LinkedIn outreach at scale across multiple accounts. | Budget-friendly LinkedIn automation. |
| Expandi | LinkedIn outreach. | "OG of LinkedIn outreach." $10M ARR, bootstrapped, from Netherlands. |

### CRM
| Tool | What ColdIQ Uses It For | Michel's Take |
|------|------------------------|---------------|
| Attio | AI-native CRM. People, companies, deals, custom objects, webhooks. | Replaced HubSpot. Auto-ingests calls/emails, extracts insights, populates fields, triggers workflows. |
| HubSpot | Former CRM. Calendar scheduling. | Being replaced by Attio. |

### Workflow & Automation
| Tool | What ColdIQ Uses It For | Michel's Take |
|------|------------------------|---------------|
| Clay | Central orchestration. Waterfall enrichment, AI scoring, qualification, data workflows. | "Central piece of our agency." Starts at $149/mo. Recommendation if budget allows. |
| n8n | Open-source workflow automation. API connections, event-triggered workflows. | Used for internal automation, onboarding processes, data syncs. |
| Make | Automation (alternative to n8n for simpler workflows). | Used alongside n8n. |
| Relevance AI | Agentic workflow builder. Custom AI agents for GTM. | "Agentic layer to build workflows on top of Claude Code/Codex." |
| Puzzle | Process mapping and high-level overview of automations. | Visualization tool for complex workflows. |
| Cargo extension | Free Google Sheets extension for AI qualification. | Budget alternative to Clay. Requires own API keys. "Messier to set up." |

### AI & Coding
| Tool | What ColdIQ Uses It For | Michel's Take |
|------|------------------------|---------------|
| Claude Code | Full outbound campaign building from terminal. ICP scoring, enrichment, copy generation, campaign upload. Also used for content creation, mini-tools, custom scripts. | Core of autonomous GTM brain. 32 skills, 12 agents, 2,108 files in ColdIQ's system. |
| Conductor | UI interface for Claude Code and Codex. Multiple sessions for different content tasks. | "Much nicer to write and repurpose posts compared to running agents in a terminal." |
| Cursor | AI-assisted coding for custom scripts and integrations. | Used by GTM Engineers for custom tooling. |
| OpenAI API | Lead scoring, qualification, copy generation inside Clay and Google Sheets. | Connected via Clay credits or directly via Cargo. |

### Content & Marketing
| Tool | What ColdIQ Uses It For | Michel's Take |
|------|------------------------|---------------|
| Taplio | LinkedIn content ideation, planning, analytics. | Primary ideation tool. Filter for 300+ likes posts in niche. |
| Scripe | LinkedIn content ideation, author-level analysis. | Complements Taplio. Spots viral publications by topic. |
| Kleo | Chrome extension for LinkedIn post inspiration. | Used earlier in stack evolution, still referenced. |
| Figma | Professional carousel and infographic design. | Used by design team (Ada, Pilar, Maria Luisa). |
| Canva | Beginner-friendly social media visuals. | Where Michel started. Recommends for early stage. |
| AirOps | Programmatic SEO page generation. | Automates blog content production at scale. |
| Ahrefs | Keyword research, ranking monitoring. | Core SEO tool. |
| Surfer | SEO copy optimization. | Used for blog article optimization. |
| beehiiv | Newsletter platform. | 5K+ subscribers, 2-4 weekly emails. |

### Inbound & Conversion
| Tool | What ColdIQ Uses It For | Michel's Take |
|------|------------------------|---------------|
| Webflow | Website hosting and CMS. | Hosts blog, landing pages, mini-tools. |
| Wistia | VSL (Video Sales Letter) hosting. | VSL in Featured section + homepage. Conversion 3x'd with first VSL. |
| Default | Lead routing and form automation. | Automates lead routing to right salesperson. |
| Customer.io | Email marketing, lead nurture sequences. | Re-engages leads who filled form but didn't book. |
| Breakcold | Social selling on LinkedIn. | Engages warm leads via social interactions. |
| Lovable | AI-built web apps from natural language. | Building free mini-tools for interactive SEO. |
| Vercel | Deployment platform for mini-tools. | Deploys interactive SEO tools. |

### Analytics & Attribution
| Tool | What ColdIQ Uses It For | Michel's Take |
|------|------------------------|---------------|
| Google Analytics | Traffic and engagement metrics. | Basic tracking. |
| HockeyStack | Channel attribution and budget allocation. | Evaluates how much budget to allocate per channel. |
| Usermaven | Web analytics. | Added in 2026 stack. |
| Fibbler | LinkedIn Ads analytics. | Used by Ivan for paid campaign optimization. |
| Dreamdata | B2B revenue attribution. Tracks every touchpoint from signal to closed deal. | Part of Claude Code API stack. |

### Sales Operations
| Tool | What ColdIQ Uses It For | Michel's Take |
|------|------------------------|---------------|
| Attention | Meeting recording, transcription, AI insights. | Captures competitor mentions, objections. Natural language search across call history. |
| Qwilr | Proposal creation and delivery. | Used for all client proposals. |
| PandaDoc | Digital contracts and signatures. | Contract execution. |
| Hyperline | Billing, subscriptions, usage metering, invoicing, CPQ. | Webhooks for payment events. ARR/MRR/churn analytics. |
| Cal.com | Scheduling infrastructure. | Booking links in emails, auto-route meetings, sync to CRM. |

### Payments & Banking
| Tool | What ColdIQ Uses It For | Michel's Take |
|------|------------------------|---------------|
| Stripe | Recurring subscription payments. | Primary payment processor. |
| Ramp | Payment and expense management. | Corporate card/expenses. |
| Mercury | Business banking. | Primary bank account. |
| Revolut Business | Business banking. | Secondary bank account. |

---

## Tools Michel Rejects

| Tool/Category | Why |
|---------------|-----|
| Outreach, SalesLoft | Legacy platforms. Teams struggle to get 10% open rates. "Just change tool." |
| G2 (for tool evaluation) | Heavily biased toward companies paying for intent data packages. |
| Broad Google Ads | Algorithm bids on brand name, pays for clicks you'd win organically. Attribution flaws. |
| AI SDRs (without proven motion) | If manual outreach hasn't proven the product can be sold, AI just automates failure. |
| X/Twitter (as content platform) | Michel explicitly excludes it. Mastering one platform (LinkedIn) yields 1000x more than spreading across 15. |
