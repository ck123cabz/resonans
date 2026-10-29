---
type: corpus
aliases: ["Cold Email Frameworks -- Michel Lieben"]
corpus: michel-lieben
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
---

# Cold Email Frameworks -- Michel Lieben

**Corpus:** michel-lieben
**Generated:** 2026-03-25

---

## Named Frameworks

### 1. Hyper-Relevant Free Value Play

**When to use:** When you can identify a specific technical pain point using intent data or public signals.

**Targeting:** Build list based on highly specific criteria. Example targeting stack:
- Missing DMARC records (deliverability protocol gap)
- Using a legacy sales platform known for poor deliverability
- Large SDR team (spending money on outbound that's going to spam)

**Email structure:**
- **Context/Observation:** State what you noticed about their setup ("noticed you're using [Platform] and are missing your DMARC records")
- **Social proof + pain point:** Reference conversations with similar companies ("recently spoke with 5 companies with the same setup, all struggling to get even 10% open rates")
- **Soft CTA (free value offer):** Offer a free resource, not a meeting ("I compiled a guide that explains exactly how we helped them go from 10% to 60%. Do you want this guide?")

**Psychology:** The prospect is actively losing money on a broken system. A free, specific guide is a no-brainer. Proving competence for free naturally leads to paid engagement because buyers have budget but lack time to implement.

**Provenance:** [S]->[D] (NotebookLM Q11 confirmed by LinkedIn/Blog)

---

### 2. Irresistible Offer (Zero Personalization)

**When to use:** When the core offer is so inherently valuable that the value proposition trumps the need for custom research.

**Structure:** Completely templated email. No first name variable. No company mention. No personalization of any kind. The offer itself does all the work.

**Example:** COO of tw. sent unpersonalized email offering to pay prospects for their time to act as product advisors (two hours/month). 20 out of 20 replies were positive (100% response rate).

**Rule:** A great offer with zero personalization always beats a bad offer with deep personalization.

**Provenance:** [S] (NotebookLM Q10, Q12, attributed to Alex Vacca)

---

### 3. Inbound-Led Outbound Contextual Play

**When to use:** To convert cold outreach into "lukewarm" outreach that converts at higher rates.

**Targeting sources:**
- People who liked or commented on team LinkedIn posts
- Profile viewers
- Website visitors (identified via RB2B, Midbound, Vector)
- Newsletter subscribers

**Structure:** Opening references the recent interaction. Examples:
- "Hey {{first_name}}, looks like my post on {topic} landed well. Are you working on {initiative}? Happy to swap notes if useful."
- Context from website visit: "noticed you checked out our [specific use-case page]"

**Pipeline:** Engagement data flows into Clay for enrichment (title, company size, tech stack, hiring, funding). AI scores against ICP criteria. Scored leads enter automated outreach via lemlist or Instantly.

**Results:** 138 meetings in July 2025. 750+ meetings in first half of 2025.

**Provenance:** [D] (LinkedIn posts + Blog articles)

---

### 4. Relevance at Scale

**When to use:** High-volume outbound campaigns requiring deep account research.

**Anti-rule:** Never use AI to fake personalization (mentioning college, using "Sent from my iPhone," fabricating personal connections). Buyers detect gimmicks instantly.

**Correct usage:** AI surfaces real business signals. The message references 4-5 specific data points:
- Company running sustainable initiatives
- Hiring in specific departments
- Recently raised funding
- Leadership changes
- Tech stack indicators

**Goal:** Prospect should feel the email could only have been sent to them because it addresses their exact current business reality. If the message is genuinely relevant, the prospect doesn't care whether an AI or human wrote it.

**Provenance:** [S] (NotebookLM Q10, Q12)

---

## Waterfall Personalization (Clay Workflow)

65-step automation built by Dan Rosenthal. Cascading personalization that finds the best available angle for each prospect.

**Step 1:** Check if prospect posted on LinkedIn in last 2 weeks. If yes, write icebreaker referencing the content of the post.

**Step 2:** If no recent post, check if their department hired someone in the last quarter. If yes, mention the new hire's name and congratulate on growth.

**Step 3:** If no post and no new hires, check how long they've been at the company. Write custom line for any major milestone (new launch, 1 year anniversary, etc.).

**Step 4 (fallback):** Personalize on the fact that they're an owner of a niche business to relate to them.

**Result:** Generated 152 leads in a single campaign.

**Provenance:** [D] (LinkedIn post 388, 511 likes)

---

## Sequence Rules

- **Length:** ~4 steps per sequence (industry shifted from 7-step). Shorter protects deliverability.
- **Re-engagement:** Wait 60 days after sequence finishes, then target different people at the same company.
- **Trigger-based follow-ups:** If prospect re-opens old email 3-4 months later, follow up immediately.
- **Deliverability basics:** <50 emails/day/mailbox, SPF/DKIM/DMARC, no open rate tracking, secondary domains, email warm-up, spintax for variation.

---

## Reply Handling SOPs

- **Speed to lead:** Reply as fast as possible. Don't check Slack channel once a day.
- **No Calendly rule:** Never reply with a Calendly link. Prospects who reply positively almost always have clarifying questions first. Answer questions to keep conversation flowing.
- **Manual follow-up:** Expect to follow up 2-4 times after initial positive reply. Interested prospects get distracted and forget.
- **Routing:** Positive replies auto-push from Smartlead to dedicated client Slack channel + CRM (HubSpot/Attio).

---

## The Manual-First Rule

Before buying automation tools, write 50-150 highly researched emails by hand. This uncovers:
- Which business initiatives signal a good fit
- Which buying signals correlate with replies
- Which job titles are actually the buyer (vs. assumed)
- Which phrases get replies vs. which fall flat

Only after discovering these patterns do you buy tools (Clay, Smartlead, Instantly) to replicate the exact logic at scale.

Michel also recommends the "15-Minute SDR" onboarding hack: ask new agency clients "If you had 15 minutes to research a prospect, what would you research about them?" Their answer becomes the exact blueprint for what gets programmed into Clay.

---

## Copy Rules (from Claude Code campaign workflow)

When generating cold email copy via Claude Code, these rules constrain the output:
- Under 100 words per email
- No jargon
- Subject lines that look like they came from a colleague
- Yes/no CTAs
- First line answers "why you, why now"
- Templates sourced from best-performing historical outreach
- Different triggers produce different copy variations within the same campaign structure
