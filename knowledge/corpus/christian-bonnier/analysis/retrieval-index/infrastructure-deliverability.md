---
type: corpus
aliases: ["Infrastructure: Deliverability -- Christian Bonnier Retrieval Index"]
corpus: christian-bonnier
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
knowledge_type: "[IN]"
provenance: "[S]"
last_updated: 2026-03-20
---

# Infrastructure: Deliverability -- Christian Bonnier Retrieval Index

The Copywriter Agent uses this file as a constraint reference. These are hard rules that override creative preferences. If a piece of generated copy violates a deliverability rule, the copy must be rewritten.

**Provenance note:** Detailed infrastructure specs are almost exclusively from NLM `[S]`. LinkedIn/X infrastructure content is promotional (ListKit features) rather than methodological. The domain-level specs below have not been independently confirmed in Christian's own writing. Use with appropriate confidence.

---

## Domain Setup

| Rule | Value | Source |
|------|-------|--------|
| Burner domains required | 25 (for 1,000 emails/day) | NLM Signal 55 |
| Emails per domain per day | 40 | NLM Signal 55 |
| Total daily capacity | 25 x 40 = 1,000 emails/day | Calculated |
| Domain cost | ~$12 each (GoDaddy, Google Domains, Porkbun) | NLM Signal 55 |
| Email provider | Google Workspace | NLM Signal 55 |
| DNS requirements | SPF, DKIM, DMARC configured | NLM Signal 56 |
| Domain forwarding | All burner domains forward to main site | NLM Signal 55 |

**Never use your main domain for cold email.** All sending happens through burner/secondary domains. (NLM Signal 56)

---

## Warm-Up Protocol

| Phase | Daily Volume per Inbox | Total (25 domains) | Duration |
|-------|----------------------|---------------------|----------|
| Week 1 | 5 emails/day | 125 total | Days 1-7 |
| Week 2 | 10 emails/day | 250 total | Days 8-14 |
| Week 3 | 20 emails/day | 500 total | Days 15-21 |
| Week 4 | 40 emails/day | 1,000 total | Days 22-28 |

Warm-up uses an automated pool at 35 dummy emails/day with 45% reply rate. (NLM Signal 55)

**4-week ramp is mandatory.** Do not skip or compress warm-up. (NLM Signal 55)

---

## Sending Rules (Hard Constraints)

These rules apply to every email the Copywriter Agent generates. Violation of any of these will compromise deliverability.

| Rule | Constraint | Source |
|------|-----------|--------|
| Daily limit per inbox | 20-40 emails | NLM Signal 56 |
| Format | Plain text ONLY | NLM Signal 56 |
| Links | None in cold emails | NLM Signal 56 |
| Images | None in cold emails | NLM Signal 56 |
| HTML | None in cold emails | NLM Signal 56 |
| Open rate tracking | DISABLED (tracking pixel triggers spam filters) | NLM Signal 56 |
| Bounce rate target | Under 1% | NLM Signal 56 |
| Email data | Triple-verified only | NLM Signal 56 |
| Deliverability checks | Weekly | NLM Signal 56 |

> "Do NOT track open rates -- hidden tracking pixel triggers Google/Microsoft spam filters; measure success by positive reply rate only."
> -- NLM Signal 56

---

## Lead List Quality Rules

| Rule | Value | Source |
|------|-------|--------|
| Data source | ListKit (triple-verified) | NLM Signal 58 |
| Decision-makers per company | 1-3 max | NLM Signal 58 |
| Filtering preference | Employee headcount over revenue (private company revenue data is inaccurate) | NLM Signal 58 |
| Pre-export step | Data visualization to exclude irrelevant job titles/countries | NLM Signal 58 |
| Filtering method | Industry + keyword filtering, not broad categories | NLM Signal 58 |
| Intent data | Use for active searchers when available | NLM Signal 58 |

**Against Apollo/ZoomInfo:** Outdated data, requires third-party verification, inefficient export (25 at a time). ListKit API pushes directly to Smartlead, eliminating CSV handling. (NLM Signal 58)

---

## Follow-Up Threading

| Rule | Value | Source |
|------|-------|--------|
| Follow-up subject lines | BLANK (threads into existing conversation) | NLM Signal 6 |
| Follow-up timing | Day 1, Day 4, Day 7, Day 12, Day 33+ | NLM Signal 5 |
| Subsequence subject lines | BLANK (same rule) | NLM Signal 6 |

All follow-ups must thread into the original email. This means no new subject lines on follow-ups. The blank subject line forces threading in most email clients.

---

## Spam Trigger Words

The Copywriter Agent must avoid these in generated copy:

| Category | Examples | Source |
|----------|---------|--------|
| Calendar link language | "book a time here," Calendly URLs | NLM Signal 25, X Signal 1 |
| Pricing in first email | Any dollar amount or pricing range | NLM Signal 9, X Signal 6 |
| Vague intangible metrics | "ROAS," "brand awareness," "ROI" | NLM Signal 22 |
| Self-introduction openers | "My name is," "I work at" | NLM Signal 20 |
| Generic pleasantries | "Hope this finds you well," "Hope you're doing great" | NLM Signal 60 |
| Unprompted links | Any URL in the first email | NLM Signal 56 |

---

## 2026 Evolution: Omnichannel Infrastructure

ListKit now offers done-for-you omnichannel: cold email + cold calling with managed SDRs. (X Signal 21, LinkedIn Signal 39)

| Component | Spec | Source |
|-----------|------|--------|
| Cold calls per day per SDR | 1,500+ | X Signal 21 |
| SDR sourcing | Offshore with near-native accents | X Signal 22 |
| Email volume | 1,000+/day | LinkedIn Signal 39 |
| Sequence structure | 3-step with A/B tests | LinkedIn Signal 39 |
| CRM re-engagement | Dial closed-lost/churned + add to email campaign | LinkedIn Signal 39 |

---

## Private Sending IP

One client campaign reference mentions "ListKit's private sending IP" with a 0.33% bounce rate. (LinkedIn Signal 38) This suggests ListKit offers dedicated IP infrastructure for high-volume or high-value clients.

---

## Agent Instructions

When generating or reviewing email copy:
1. Verify: no links, no images, no HTML, no tracking pixels.
2. Verify: no pricing in Email 1.
3. Verify: no calendar links in Email 1 (or any email until post-reply).
4. Follow-up emails must have blank subject lines.
5. Total word count must stay under 50 for Email 1.
6. If the copy references a URL, video, or external resource, rewrite to ask permission to share it instead of including it.
7. Never recommend open rate as a success metric. Positive reply rate is the only metric.
