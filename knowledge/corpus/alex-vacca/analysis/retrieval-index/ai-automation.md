---
type: corpus
aliases: ["AI Automation — Retrieval Index"]
corpus: alex-vacca
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
---

# AI Automation — Retrieval Index

**Corpus:** Alex Vacca
**Knowledge type:** [AI] AI Automation
**Last updated:** 2026-03-24

---

## Claude Code Terminal Campaign Workflow

The new paradigm that replaces Clay UI interaction for campaign building. One person plus Claude Code replaces a three-person campaign ops team. Entire process takes approximately 15 minutes vs. hours of manual Clay work.

### Setup

Local folder containing:
- **Copy Framework markdown** — word count 50-80, subject line format, CTA format, cut fluff
- **Scoring Criteria markdown** — points by industry, employee count, funding stage, revenue, tech stack; classifies companies into Tier 1/2/3
- **API keys** — Apollo (contact finding), Lima Data (email verification), Instantly (campaign push)

These markdown files are the "skill files" that encode the agency's methodology for Claude. Two files are confirmed. ColdIQ references 12 total Claude Skill files (contents gated behind lead magnet).
`[S]→[D] | N43, N78, L3, B11`

### Execution Steps (Verbatim Prompts)

**Step 1 — ICP filtering and tiering:**
"Go through my lists of companies and start filtering and tiering based on ICP criteria."

Claude reads the Scoring Criteria markdown and scores contextually across hundreds of accounts. Changing criteria requires updating the prompt, not rebuilding formulas.
`[S]→[D] | N76, B11`

**Step 2 — Contact discovery with verification checkpoint:**
"Find me the right contact person at all of those companies and list me three examples just to make sure we are targeting the right job titles."

The "list me three examples" pattern is a verification checkpoint before burning API credits on the full list.
`[S] | N76`

**Step 3 — Full contact enrichment:**
"Find me the best contacts for each of the company in the list and find the correct email address for every single prospect."

Waterfall enrichment via API: Apollo first > Prospeo for gaps > FullEnrich third pass > Wiza/LeadMagic for remaining. Single loop, no manual CSV exports.
`[S]→[P] | N76, B11`

**Step 4 — Copy generation with sample review:**
"Do we have everything we need to write the copy for every prospect in the list? Only write the copy for the first 10 prospects to use it as an example."

Claude reads the Copy Framework markdown and generates copy following the rules: under 100 words per email, no jargon, subject lines that look like they came from a colleague, yes/no CTAs, first line answers "why you, why now." Includes fallback copy for empty personalization variables.
`[S]→[P] | N76, B11, B23`

**Step 5 — Campaign push to Instantly:**
"Could you please create the email campaign in Instantly directly? Just do it for the first 10 contacts and write a sequence of two emails for each prospect."

Claude creates the campaign via Instantly API, injects enriched leads, writes emails, sets schedule (3-day gap between emails), saves as **draft** in Instantly. The draft-first pattern is a safety mechanism: no auto-send without human review. Team previews in browser before launching.
`[S]→[P] | N76, N79, B11`

### Self-Correction Behavior

During live testing, Claude flagged its own errors before being asked:
- "Email 2 for nonVC companies doesn't work" (copy mismatched to segment)
- "Super long company names in subject line" (display issue)

Alex responded: "Yes please apply the two recommendations you made, only write the sequence for the first 10 contacts." Claude fixed errors before pushing to Instantly.

This self-correction against the copy framework is a key quality pattern. The AI evaluating its own output replaces a human QA step.
`[S]→[D] | N77`

### Quality Gates (4 layers)

1. **Formula fallbacks in Clay** — reject AI output that starts with wrong words ("The final answer is...")
2. **Strict framework rules via markdown** — 50-80 word limit, CTA format, cut fluff
3. **AI self-correction** — Claude flags its own errors against the framework
4. **Pre-launch visual preview** — human review in Instantly/Smartlead browser before sending
`[S]→[P] | N54, N55, N77, B23`

### Impact

Single GTM engineer launches 5-10 campaigns per week instead of 2-3. One person plus Claude Code replaces three-person campaign ops team. ColdIQ passed 10 billion OpenAI tokens with hands-on AI usage.
`[P]→[D] | B11, L58`

### 19 APIs Worth Connecting via Claude Code

Organized by functional layer:

**Signal layer:** PredictLeads (hiring surges, funding, tech adoption), Common Room (community/product/GTM signals), Attention (sales call analysis), RB2B/Vector (anonymous visitor ID)

**Data layer:** Openmart (200M+ local business records), Wiza (LinkedIn to verified contacts, 50+ data points), Prospeo (98%+ email accuracy, 200M+ database), FullEnrich (waterfall through 20+ providers, 80%+ find rates), Apollo (firmographic/technographic data)

**Action layer:** Instantly (programmatic cold email), lemlist (multichannel email+LinkedIn+calls), LinkedIn Ads (programmatic ABM campaigns)

**Automation layer:** n8n (workflow orchestration for AI agents)

**System of record:** Attio (AI-native CRM with full API, real-time webhooks)

**Conversion:** Cal.com (scheduling)

**Revenue:** Hyperline (billing, subscriptions, usage metering)

Key insight: "The stack isn't the advantage. Making all the tools interconnected is."
`[D] | L31`

---

## WhatsApp AI Voice Clone

Architecture for an AI assistant that responds to WhatsApp messages in Alex's cloned voice. Fully detailed in the corpus with tool chain and prompt constraints.

### Architecture

**Incoming message flow:**
1. Make.com webhook listens for incoming WhatsApp messages
2. Router logic:
   - If audio voice note: OpenAI Whisper (Speech-to-Text) transcribes to text first
   - If written text: bypass transcription
3. Text query sent to OpenAI Assistants API agent

**Knowledge base:**
Transcripts of all Alex's YouTube videos. Auto-updated by a separate automation that scrapes new video transcripts as they publish.

**Agent instructions (prompt constraints):**
- Act as Alex
- Friendly, conversational tone
- Never make up information if it is not in the knowledge base
- Never output bullet points or numbered lists (sounds unnatural when spoken aloud)
- Never cite sources (ruins voice note illusion)
`[S] | N80`

### Quality Controls

1. **Source-stripping step:** Extra OpenAI module with an "expert answer improver" prompt that strips all source citations from the AI response. Citations ruin the voice note illusion.
2. **Professional voice clone:** 11 Labs "professional voice clone" (not instant clone) trained on high-quality, background-noise-free audio from YouTube and podcast appearances. Replicates Alex's French accent.
3. **Audio delivery:** Final audio file uploaded back to WhatsApp via Make.com into the same Chat ID.
`[S] | N81`

The source-stripping step is a post-processing pattern applicable to other voice AI systems beyond this specific implementation.

---

## Make.com Automation Scenarios

### Email Infrastructure Automation
Automates domain purchasing, mailbox setup, and SPF/DKIM/DMARC record configuration. Replaced hours of manual backend work. This is the automation layer that makes ColdIQ's 1,250 domains manageable.
`[S]→[D] | N19, N86`

### WhatsApp AI Voice Clone
See dedicated section above. Make.com serves as the orchestration layer for incoming message routing, Whisper transcription, OpenAI Assistants API calls, 11 Labs voice synthesis, and WhatsApp message delivery.
`[S] | N80, N81`

---

## n8n Workflows

### Intelligent Follow-Up
AI agent syncs with sales team calendars. When a lead shows interest, AI suggests specific available times and handles the back-and-forth scheduling to book the meeting. Replaces the anti-pattern of dropping a Calendly link (identified as the worst follow-up method).
`[S] | N83`

### Four GTM Agents (Saving 2-5 Hours Per Client Daily)

**Agent 1 — Lead Research:**
GhostGenius captures LinkedIn profiles. Filter by credibility signals (200+ followers, real website, recent activity). GPT scores against ICP in real-time. LinkedIn ID deduplication prevents re-processing.
`[D] | L33`

**Agent 2 — Local Prospecting:**
Apify pulls from Google Maps. Google Search API fills missing metadata. Scrape websites for keywords, offers, and tech stack. GPT classifies and enriches. Extract missing emails and phone numbers.
`[D] | L33`

**Agent 3 — Brand Content Generator:**
Google Form input triggers generation of LinkedIn posts, carousel copy, newsletters, hooks, and CTAs, all in the brand's tone of voice. Drafts pushed to Notion or Google Docs for review.
`[D] | L33`

**Agent 4 — Reddit Intel Collector:**
Input: brand name and website URL. GPT identifies ICP signals from the brand context. Reddit API scrapes relevant threads. GPT summarizes pain points and the prospect language used. Daily insight report delivered to inbox. "This is the closest thing to reading your market's mind."
`[D] | L33 | Note: mentioned once, no cross-source confirmation`

---

## Cargo Infinite Lookalike Machine

When a prospect replies positively to a campaign, the workflow auto-generates 10 lookalike leads from that specific lead's data (using Ocean or Cargo's native capability) and dumps them back into the active sequence. Creates a self-reinforcing feedback loop: positive replies generate more targets who look like the people who already responded.
`[S] | N84`

---

## 4-Agent Campaign Strategy Builder

A multi-agent system that converts a single website URL into a complete campaign strategy.

**Agent 1 — Analysis Agent:**
Reads the website. Outputs company thesis, service lines, and market positioning.

**Agent 2 — ICP & Scoring Agent:**
Builds ICP matrix with weights:
- Product-market fit: 30%
- Outbound readiness: 25%
- (Remaining weights not specified in corpus)

Classifies prospects into Tier 1/2/3. Maps pain points, fears, and tech stack disqualifiers.

**Agent 3 — Prompt Generator:**
Outputs exact text prompts for the list-building tool (Apollo, LinkedIn Sales Nav) to extract the specific leads matching the ICP matrix.

**Agent 4:** Not explicitly described in the corpus. The system is referred to as "4-Agent" but only three are detailed.
`[S]→[P] | N85, B22`

### Multi-Agent Orchestration Patterns

ColdIQ uses three patterns depending on the task:

1. **Hierarchical:** Manager agent coordinates specialized sub-agents (calendar checker, data puller, email drafter). Manager reviews and approves final output. Maps to Clay/Relevance AI workflows. Best for multi-step tasks with dependencies and quality control needs.

2. **Human-in-the-loop:** Agent does research and drafts, taps human for approval on high-stakes decisions. Best for maintaining quality on important accounts (Tier 1).

3. **Collaborative/peer:** Agents share data and coordinate without a central manager. Each agent specializes and triggers others. Best for parallel tasks where speed matters.
`[P] | B22`

---

## AI Capability Taxonomy (3-Tier Framework)

ColdIQ's calibration on AI agent hype vs. reality.

**Tier 1 — Non-agentic workflows (basic AI):**
One input, LLM request, one output. Human thinking, AI doing. Examples: LinkedIn profile to enriched data, campaign brief to personalized sequences, transcript to action items. No automation because the task will not repeat. Use for one-off tasks requiring judgment.
`[S]→[D] | N14, L23, B15`

**Tier 2 — Agentic workflows (the "sweet spot for revenue"):**
Multiple tools in sequence with basic decision-making. Automated triggers, fixed logic. This is the bulk of the outbound pipeline. Real ColdIQ example: monitors LinkedIn engagement > enriches in Clay > scores against ICP > routes qualified leads to different sequences > triggers personalized outreach in Instantly > updates CRM. Runs 24/7 without human intervention. Brittle when context changes. Thousands of leads per week processed.
`[S]→[D] | N14, L23, B15`

**Tier 3 — True AI agents (overhyped, underdeveloped):**
Goal-oriented autonomy. Tasks requiring adaptive behavior. "99% of what people call AI agents are just well-designed workflows." Real agents should understand context, learn from outcomes, and handle unexpected situations. The technology "isn't quite there yet." Only use for context-dependent, adaptive tasks. Add human-in-the-loop for high-stakes decisions regardless of approach.
`[S]→[D] | N14, L23, B15`

**Decision framework:**
- One-off + requires judgment = prompt AI directly (Tier 1)
- Repeatable + predictable steps = workflow (Tier 2)
- Context-dependent + adaptive = agent (Tier 3)
- High-stakes = add human-in-the-loop regardless of tier

Advice: start simple with workflows, build up gradually. Do not jump straight to agents.
`[D] | L23 | [P] | B15`

---

## Automated Inbound-Led Outbound Workflow

The fully automated version of the inbound-led outbound system.

1. Website visitor identified by RB2B/Vector
2. Clay Agent fills missing company domain
3. HubSpot/Attio exclusion check (halt if active deal)
4. AI tier scoring: industry, description, employee count mapped to Tier 1/2/3
5. If Tier 1: Apollo finds GTM leaders at the company
6. Auto-trigger LinkedIn connection via Lemlist and email sequence via Instantly simultaneously
`[S] | N87`

---

## 12 Claude Skill Files

Named files built from hundreds of Clay tables across 80+ B2B clients at $7M ARR:

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

Usage: drop skill file into Clay, map columns, run. Each file encodes a specific methodology. The actual contents remain a P0 gap in the corpus (behind a lead magnet). Two files are partially described through the corpus: the Copy Framework markdown and the Scoring Criteria markdown.
`[D] | L3, X218 | Gap: file contents are [A] Absent`
