---
type: corpus
aliases: ["Evidence: ListKit Case Study -- Christian Bonnier Retrieval Index"]
corpus: christian-bonnier
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
knowledge_type: "[E]"
provenance: "[D]"
last_updated: 2026-03-20
---

# Evidence: ListKit Case Study -- Christian Bonnier Retrieval Index

The Copywriter Agent uses this file when it needs to reference Christian's most quantified campaign: the 47-word script that scaled ListKit from $0 to $108K MRR in 90 days.

---

## The 47-Word Script

> "Hey [Name], I noticed you're in charge of [Company Name]'s marketing efforts. We have a B2B database with 500 million email leads similar to Apollo or ZoomInfo. I put together 50 sample leads based on the case studies on your website. Mind if I share the leads here?"

**Word count:** 47
**CTA type:** Lead magnet (free deliverable)
**CTA cadence:** "Mind if I share the leads here?"

---

## Campaign Metrics

| Metric | Value | Source |
|--------|-------|--------|
| Emails sent | 494,000 | NLM Signal 47 |
| Calls booked | 685 | NLM Signal 37, 47 |
| MRR generated | $108,000 | NLM Signal 37, 42 |
| Time to reach MRR | 90 days | NLM Signal 37 |
| Starting MRR | $0 | NLM Signal 37 |
| Booking rate | 685 / 494,000 = 0.14% | Calculated |
| Emails per booking | ~721 | Calculated |

---

## Unit Economics (LinkedIn Confirmation)

> "1 client per 1,000 emails = 5 clients from $500 spend. CAC = $100."
> -- LinkedIn Signal 27

| Metric | Value |
|--------|-------|
| Cost to reach 5,000 prospects | <$500 |
| Expected clients from 5,000 emails | 5 |
| CAC | $100 |
| Revenue per client at $2K/month | $10,000 from $500 investment |

---

## Operational Details

**Delayed fulfillment.** The "50 free leads" were not built before sending. Christian didn't build the sample lead lists until a prospect replied "yes." This means the lead magnet was promised but not created at send time. This is an efficiency optimization that avoids wasted work on non-responders. (NLM Signal 47)

**Subsequence automation.** When a prospect replied positively, they were tagged "50 free leads" in Smartlead. This triggered an automated drip:

1. First auto-reply: "I'm working on your 50 free leads right now... In the meantime, how does next week work for a quick demo?"
2. Subsequent drips: relentless follow-up including the detective emoji at one stage
3. Subject line left blank so replies thread into existing conversation

(NLM Signal 47)

**Follow-up structure.** The Billboard Strategy governed follow-ups: same core offer repeated. No new services introduced. No changes to the guarantee. (NLM Signal 5, 47)

**Unqualified responders.** Prospects who replied but weren't qualified were ignored. No wasted effort on bad-fit leads. (NLM Signal 47)

---

## Why This Script Works (Analysis)

The script obeys every Christian Bonnier copy rule simultaneously:

| Rule | How the Script Obeys It |
|------|------------------------|
| 50-word limit | 47 words |
| 3-second rule | Opens with a relevant observation about their role |
| 2:1 Rule | "you/your" appears 4 times; "I/we" appears 2 times |
| Tangible offer anchoring | "50 sample leads" is a physical deliverable, not vague |
| Industry slang | "B2B database with 500 million email leads" speaks the prospect's language |
| Sell the response | CTA asks permission to share, not to book a call |
| Mind if I cadence | "Mind if I share the leads here?" |
| No links | No URLs, no calendar, no images |
| Specificity | "based on the case studies on your website" shows research |
| Competitor positioning | "similar to Apollo or ZoomInfo" anchors against known tools |

---

## Agent Instructions

This script is the gold standard for the lead magnet CTA approach. When generating a new lead-magnet-style email:
1. Follow the same structure: observation about their role, value proposition in one sentence, tangible deliverable, "Mind if I" CTA.
2. Keep word count at or below 50.
3. The deliverable must be something you can actually create if they say yes (but don't build it until they do).
4. Anchor against a known competitor or reference point.
5. The script works because the offer is genuinely useful and the CTA is genuinely low-friction. Both must be true.
