---
type: corpus
aliases: ["Infrastructure: Tool Stack -- Christian Bonnier Retrieval Index"]
corpus: christian-bonnier
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
knowledge_type: "[IN]"
provenance: "[S], [V]"
last_updated: 2026-03-20
---

# Infrastructure: Tool Stack -- Christian Bonnier Retrieval Index

The Copywriter Agent uses this file to understand which tools Christian uses and how they integrate. Tool selection affects copy generation (what's automatable vs. manual) and campaign architecture.

---

## Core Tool Stack

### ListKit -- Lead Database

**Role:** B2B lead database. Triple-verified data. Granular filtering.

| Feature | Purpose | Source |
|---------|---------|--------|
| Industry + keyword filtering | Precise audience targeting (not broad categories) | NLM Signal 58 |
| Employee headcount filter | Better signal than revenue for private companies | NLM Signal 58 |
| Data visualization | Pre-export QA to exclude irrelevant job titles/countries | NLM Signal 58 |
| API integration with Smartlead | Eliminates CSV handling | NLM Signal 57, 58 |
| Triple-verified emails | Target <1% bounce rate | NLM Signal 58 |
| Intent data | Identify actively in-market contacts | LinkedIn Signal 40 |
| AI Company Search | Plain text input finds companies, replaces manual filtering | LinkedIn Signal 40 |
| AI Lookalikes | Find companies similar to existing converters | LinkedIn Signal 40 |
| Deep Company Research | Enrichment for personalization (services, target customer, industry) | LinkedIn Signal 40 |

### Smartlead.ai -- Sending & Automation

**Role:** Sending tool, domain warm-up, campaign management, master inbox.

| Feature | Purpose | Source |
|---------|---------|--------|
| Domain warm-up | Automated warm-up pool at 35 dummy emails/day | NLM Signal 55 |
| A/B/C/D testing | Test up to 4 email variants simultaneously | NLM Signal 7, 12 |
| Master inbox | Unified inbox for all burner domain replies | NLM Signal 12 |
| Subsequences | Automated post-reply follow-up drip | NLM Signal 6, 47 |
| Tagging system | Tag replies by type ("interested," "50 free leads") | NLM Signal 47 |
| Campaign scheduling | Time zone-aware sending | NLM Signal 12 |
| Blank subject follow-ups | Threads into existing conversation | NLM Signal 6 |

### Loom -- Video Pitches

**Role:** Custom video recording for personalized pitches.

| Feature | Purpose | Source |
|---------|---------|--------|
| Screen recording | Pull up prospect's website in first 5 seconds | LinkedIn Signal 10 |
| GIF thumbnail embedding | Use GIF in delivery email, not plain link | NLM Signal 4 |
| Timestamp highlights | Include two timestamps as hooks in delivery email | NLM Signal 4 |

**Key rule:** Only record the Loom video AFTER the prospect replies "yes" to the pitch email. Never record before they express interest. (NLM Signal 3, LinkedIn Signal 10)

### Calendly -- Pre-Call Automation

**Role:** Scheduling with automated confirmation and reminders.

| Feature | Purpose | Source |
|---------|---------|--------|
| Immediate text confirmation | Sent when call is booked | NLM Signal 6 |
| 24-hour email reminder | Before scheduled call | NLM Signal 6 |
| 1-hour text reminder | Before scheduled call | NLM Signal 6 |

**Key rule:** Calendly is for the backend automation, not the CTA. Never send a Calendly link as a CTA in cold email. Propose specific times first; Calendly link only as a last-resort backup. (NLM Signal 25, X Signal 1, LinkedIn Signal 22)

---

## AI Tool Roles

Christian uses four AI tools with strict role separation. Each tool does one thing.

### Deepseek -- Industry Slang Injection

**Role:** Take a generic cold email script and make it hyper-specific to an industry.

**The Prompt (verbatim):**
> "Do not make this script any longer or any shorter just change up the messaging to be hyper relevant for [Industry] companies using their lingo, pain points and desires."
> -- NLM Signal 10

**When to use:** After writing the base script. Feed Deepseek the generic version and it swaps vocabulary to match the target industry.

**Why Deepseek over ChatGPT:** Christian names Deepseek as "best for cold email copy/slang injection." (NLM Signal 57)

### ChatGPT -- Research & Pain Point Discovery

**Role:** Uncovering deep industry pain points for offer construction.

**The Prompt (verbatim):**
> "What are a few common pain points for [Target Audience] when it comes to marketing their [Business]?"
> -- NLM Signal 10

**Process:** Ask the initial question, drill deeper on responses, look for the single "golden nugget" pain point that's specific enough to use in copy.

**What NOT to use it for:** Never let ChatGPT write cold email copy from scratch. It produces "fluffy, long-winded, vague copy that fails to convert." (NLM Signal 27)

> "ChatGPT is the most brilliant research assistant in the world and the worst employee in the world."
> -- NLM Signal 27, confirmed `[D]`

### Claude Projects ("CB Writes Copy Bot") -- Sequence Generation

**Role:** Generate three-step cold email sequences in 30 seconds.

**Setup:** A Claude Project fed with Christian's rules and best templates. (NLM Signal 10)

**Gap note:** The actual prompt/configuration for "CB Writes Copy Bot" is not in any corpus source. This is a HIGH priority gap identified in Pass 2.

### Manis -- Dream 100 Personalization

**Role:** Deep 1:1 personalization for high-value prospects.

**Process:** Scrapes prospect's website and LinkedIn. Returns verified, accurate personalized outreach data. (NLM Signal 10)

**Time savings:** Old manual Dream 100 process took 1 hour per prospect (15 min website, 20 min LinkedIn, 15 min case study hunting, 10 min message crafting). AI-assisted process takes 30 seconds. (LinkedIn Signal 9)

---

## The Division of Labor

Christian's AI philosophy boils down to one principle: the human provides the framework and structure, AI provides vocabulary and research.

> "Write the foundational offer and structure yourself, then use AI to inject hyper-specific market research, lingo, and targeted pain points into that existing structure."
> -- NLM Signal 27

**Anti-AI stance (2025):** "there's no AI personalization here, there's no Clay workflows, it's just cold hard copywriting." Christian explicitly rejects Clay-style automation workflows. His argument: better copy matters more than better tooling. (NLM Signal 65)

---

## Domain Infrastructure

| Component | Spec | Source |
|-----------|------|--------|
| Domain registrars | GoDaddy, Google Domains, Porkbun | NLM Signal 57 |
| Domains required | 25 for 1,000 emails/day | NLM Signal 55 |
| Email provider | Google Workspace | NLM Signal 55 |
| DNS records | SPF, DKIM, DMARC | NLM Signal 56 |
| Domain forwarding | All burner domains -> main site | NLM Signal 55 |

---

## Complete Campaign Setup Sequence (7 Steps)

1. Craft offer via XYZ Framework
2. Buy burner domains, set up Google Workspace, configure SPF/DKIM/DMARC, set up domain forwarding
3. Connect to Smartlead, warm up with dummy emails, ramp from 5/day to 40/day over 4 weeks
4. Build lead list with ListKit (filter by industry, location, headcount, job title, keywords; export 1-3 decision-makers per company; triple-verified data)
5. Write 5-step sequence with A/B/C/D variants
6. Import to Smartlead, check variables, schedule by time zone, blank subject lines on follow-ups
7. Monitor master inbox, push to calls with specific times, use subsequences for automation

(NLM Signal 12)

---

## Agent Instructions

When advising on tool selection or integration:
1. ListKit for leads, Smartlead for sending. This pairing is assumed.
2. AI tools have strict roles: Deepseek for slang, ChatGPT for research, Claude for sequences, Manis for Dream 100.
3. Never recommend AI-generated first lines or Clay workflows. Christian explicitly rejects these.
4. The Loom video pipeline requires a consent gate: pitch the video first, only record after "yes."
5. Calendly is infrastructure, not a CTA. Never recommend sending a Calendly link in a cold email.
