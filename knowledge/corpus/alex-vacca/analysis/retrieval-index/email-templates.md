---
type: corpus
aliases: ["Email Templates & Copy Craft — Retrieval Index"]
corpus: alex-vacca
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
---

# Email Templates & Copy Craft — Retrieval Index

**Corpus:** Alex Vacca
**Knowledge type:** [CC] Copy Craft
**Last updated:** 2026-03-24

---

## Core Copy Philosophy

Cold email copy at ColdIQ is built on two constraints that override everything else:

**1. Relevance beats personalization.**
Referencing a prospect's favorite sports team, high school, or restaurant recommendations and then pivoting to a generic pitch fails because the personalization has nothing to do with their business pain. If the email does not solve a real business problem, personal trivia will not save it. A trigger-based signal (job posting, funding round, tech adoption) adds both relevancy and personalization simultaneously.
`[S]→[D] | N11, L9, L13, L22, L34, B10, B24`

**2. Give first, never ask first.**
Never ask for a 30-minute meeting in the first email. Offer extreme value upfront for free. Specific assets to offer: custom 1-2 minute Loom video audit, strategy document, tailored lead magnet (e.g., list of 2,000 enriched prospects customized to their industry), or 6 AI-generated campaign ideas they could implement. The value-first offer is the catalyst that triggers the entire circular sales system when the prospect clicks the link.
`[S]→[D] | N10, L9, L41, B2, B10`

---

## ATL vs. BTL Framing

All copy must be differentiated by persona type. The same email cannot go to both.

**Above The Line (ATL)** — C-suite, VPs, Directors:
- Care about ROI, strategic advantages, competitor positioning
- Subject lines focus on outcomes: "your content teams producing three times more here is how"
- Copy speaks to business impact, revenue, and market position
`[S]→[D] | N8, L13`

**Below The Line (BTL)** — Managers, team leads, daily contributors:
- Care about features, ease of use, eliminating daily friction
- Subject lines focus on pain: "stop sending forwards editing one instagram reel"
- Copy speaks to workflow problems and time savings
`[S]→[D] | N8, L13`

This persona distinction drives all copy variation in the 3x2x3 matrix.

---

## The 3x2x3 Matrix

The copy testing protocol that scientifically finds message-market fit.

**Structure:**
- 3 firmographic segments (defined by ICP segmentation)
- x 2 persona types (ATL and BTL)
- x 3 copy variations per combination
- = 18 unique email variations

**Testing protocol:**
- Minimum batch: 1,000-1,500 contacts per segment
- Split between ATL and BTL lists
- Let the first 2 steps of the email sequence run for approximately 6 days
- Analyze which variation naturally resonated
- Message-market fit is usually found within 1-3 campaigns

Test by volume, not by time. This removes guesswork from copy decisions.
`[S]→[D] | N7, N8, N9, N13, N49, N50, L9, L13, L18, L22`

**Benchmarks:**
- Generic AI email blasts: 0.5% reply rate or lower
- Winning campaign with relevance: 3-5% positive reply rate
- Highly successful campaigns: 2-7% reply rate
- Campaigns with hyperenriched data + micro-targeted lists: 20-30% reply rate
`[S]→[D] | N12, N49, L29`

---

## 4-Step Email Sequence Structure

ColdIQ's standard sequence with 3-day gaps between emails.

**Email 1 — New thread, trigger-based opening:**
Initial outreach targeting a specific trigger with a relevant value proposition. Soft CTA. Answers "why you, why now."
`[S]→[D] | N20, B23`

**Email 2 — Threaded reply to E1, different angle:**
Short follow-up offering a lead magnet or resource. Not a meeting pitch. Takes a different angle on the same pain point.
`[S]→[D] | N20, B23`

**Email 3 — New thread, case study:**
Separate thread with social proof. Includes a case study with specific results and a direct CTA.
`[P]→[D] | B23`

**Email 4 — Threaded reply to E3, breakup:**
Final ask. Breakup email. Conversational tone, provides a last piece of value (e.g., 3 free AI-generated outbound ideas customized to the prospect's company).
`[S]→[D] | N20, B23`

**Copywriting rules fed to Claude Code for this sequence:**
- Under 100 words per email (ColdIQ internal standard: 50-80 words)
- No jargon
- Subject lines that look like they came from a colleague
- Yes/no CTAs
- First line answers "why you, why now"
- Must include fallback copy for empty personalization variables
- Personalization that breaks on missing data is worse than no personalization
`[P]→[D] | B11, B23`

---

## Trigger-Based Salary Hook Template

The most detailed template in the corpus, combining multiple AI-generated variables.

> Hey there team, I was on your site and saw you provide a [AI summary of business]. I noticed that [Company] posted a job opening for [Role]. The average salary for this role in the [Location] is [Calculated Salary]. If we could generate three times more qualified leads for a third of the cost as we did for clients [Case Study 1, 2, 3], would it be worth exploring?

**AI variables required:**
- Business summary (from Clay Agent website scraping)
- Company name (cleaned, no LLC/GmbH)
- Role being hired (from Trigify job posting trigger)
- Geographic location (from job posting or company data)
- Calculated average salary (AI estimation by role and location)
- Case study references (from internal results database)
`[S] | N37, N53`

---

## Word Count Rules

Keep total email copy strictly below 50-80 words per email. A prospect should be able to read the entire email in 10 seconds or less.

**Tension reconciliation:** The 50-80 word limit comes from ColdIQ's internal standard (NotebookLM). Blog articles by Michel reference "under 100 words" as the ceiling for Claude Code's copywriting rules. Both point the same direction. The agent should use 50-80 as the primary constraint and allow 80-100 only when the copy warrants it.
`[S]→[D] | N23, L13, L22 | Pass 2 Tension 4`

---

## Subject Line Rules

1. **Persona-specific:** ATL subjects focus on ROI, BTL subjects focus on friction
2. **Clean company names:** AI strips "LLC"/"GmbH" so the subject line reads naturally
3. **Under 3 words** for highest performance
4. **Test question-based subjects:** "quick question about [pain point]" or "so you're hiring for [role]"
5. **Pattern-interrupt:** the only goal of the subject line is getting the email opened
`[S]→[D] | N22, L9`

---

## Spintax Patterns

Rotate greetings across emails to vary the exact text sent from each mailbox. This protects deliverability by preventing identical copy across thousands of sends.

Examples: "Hey there," / "Hi," / "Happy [day of week]"
`[S] | N25`

---

## CTA Principles

**Never:** "Ask first" — demanding 30 minutes of a stranger's time. Dropping a Calendly link as a follow-up (identified as the worst follow-up method).

**Always:** "Give first" — offer a custom Loom audit, strategy doc, or AI-generated campaign ideas. Keep CTAs conversational and low-friction:
- "Should I send them through?"
- "Would it be worth exploring?"
- "Want to see how?"
- "Happy to share what's working"

Soft CTAs should frame a yes/no decision, not an open-ended time commitment.
`[S]→[D] | N10, N52, N57, L9, L13, L21, L22`

---

## Cold Email Rules Summary (8 Rules for 20% Reply Rates)

From Alex's LinkedIn post, confirmed across multiple sources:

1. **Personalize with name, role, company.** Mention a problem the prospect faces, discuss their KPIs.
2. **Never pitch yourself in the first email.**
3. **Niche down.** "Help cat clothing stores in LA" beats "all e-com websites."
4. **Intriguing subject lines** with questions and company name.
5. **Demonstrate understanding** of their goals. Speak their language. Do not talk to a CFO like an SDR.
6. **Include relevant case study** with real data.
7. **Soft CTA:** ask to send something useful rather than demanding a meeting.
8. **Keep it short:** 10 seconds max to read.
`[D] | L13`

---

## LinkedIn DM Copy Rules

From analysis of 100K+ LinkedIn DMs:

- ICP-tailored copy gets 54.7% more replies
- Messages under 150 characters get 22% more replies
- Contextual outreach (referencing recent activity or role changes) gets +18% replies
- Warm approach sequences (profile visits, likes, follows before connecting) get +30.2% acceptance
- Multi-step sequences (3+ steps) perform 42% better than single messages
- Adding email follow-up after no LinkedIn reply lifts reply rate by 13.8%

**Best-performing DM templates:**
- "Noticed you're hiring [role]" — +18.2% reply rate
- "Saw your post on [topic]" — +19.3%
- "Saw you joined [company]" — +21.5%
- "We analyzed [findings]" — +27.1%

Overall results: 40%+ acceptance rates, 18%+ reply rates, 8%+ positive reply rates.
`[D] | L15`

---

## 5-Step LinkedIn DM Checklist

1. Use triggers: reference something real (milestone, specific challenge from their posts)
2. Be brief
3. Make it personal: show you know who you are talking to
4. Soft CTA: "Want to see how?" beats pushing for a meeting immediately
5. Do not over-sell: focus on the prospect's problem, not what your company does
`[D] | L21`

---

## Manual-First Copy Development Protocol

Before automating any copy, write the first batch by hand. This surfaces patterns that automation can then scale.

- Tier 1 (dream clients): write first 25-50 messages by hand
- General guidance: write first 50 messages by hand before automating
- Extract patterns: shared pain points, winning phrases, correct buyer title
- Scale those patterns as Clay variables to 1,000+ contacts
- If reply rate is below 20%, you probably do not have product-message fit yet

Patterns discovered in manual Tier 1 work get promoted to Tier 2 automated sequences, then tested at Tier 3 scale.
`[P]→[D] | B1, B10, L45`

---

## Lead Magnets as Cold Email Strategy

Every cold email asks for a meeting and gets ignored. Lead magnets give something useful first and generate replies. Once someone engages with a lead magnet, you are no longer cold. You can track intent signals from their engagement.

Most cold email lead magnets fail because they are generic PDFs or swipe files with no context. The effective approach: before writing an email, ask "if this person signed as a client tomorrow, what is the first thing we would do for them?" Then do that for free in the email.

Example: for recruiting firms, ColdIQ built a list of HR Directors at companies hiring 10+ roles and sent it to them for free. This demonstrates competence rather than claiming it.

ColdIQ went from under 200 replies to 50+ booked calls per month using this approach.
`[D] | L41 | [P] | B2`

---

## Copy Formula

Context + Social Proof + Value + Personalization

Used for both cold email and re-engagement messages. Template for re-engagement:
"Hey [name], saw you engaged with my post on [topic]. Are you working on [initiative]? Happy to swap notes if useful."
`[D] | L10, L45`

---

## Tiered Outreach by Account Quality

**Tier 1 (dream clients):** Manual multichannel. Write first 25-50 messages by hand. Email + LinkedIn + phone via Nooks.

**Tier 2 (good fits):** Automated multichannel via Clay + lemlist. Lead with free value like a niche lead list.

**Tier 3 (broad fits):** Email at scale via Instantly. Use as testing ground for copy variations.

Reach the entire TAM every 3-6 months.
`[P]→[D] | B1`
