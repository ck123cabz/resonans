---
type: corpus
aliases: ["Evidence: Campaign Metrics & Benchmarks -- Christian Bonnier Retrieval Index"]
corpus: christian-bonnier
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
knowledge_type: "[E]"
provenance: "[D]"
last_updated: 2026-03-20
---

# Evidence: Campaign Metrics & Benchmarks -- Christian Bonnier Retrieval Index

The Copywriter Agent uses this file to set expectations, diagnose performance, and calculate volume requirements. All benchmarks reflect Christian's system at scale.

---

## North Star Benchmark

**1 client per 1,000 emails sent.**

This is the governing metric for Christian's entire system. Everything else derives from it.

> "1 client per 1,000 emails = 5 clients from $500 spend. CAC = $100."
> -- LinkedIn Signal 27 `[V]`

> "North Star: 1 client per 1,000 emails sent."
> -- NLM Signal 41 `[S]`

Confirmed `[D]` -- same number appears in both NLM extraction and Christian's own LinkedIn post.

---

## Funnel Conversion Rates

| Stage | Rate | Derivation | Source |
|-------|------|-----------|--------|
| Emails sent -> Positive reply | 1-2% | 1-2 per 100 emails | NLM Signal 41 |
| Emails sent -> Booked call | 0.1% | 1 per 1,000 emails = ~10-20 booked calls | NLM Signal 41 |
| Emails sent -> Closed deal | 0.1% | 1-2 deals per 1,000 emails | NLM Signal 41 |
| Booked calls -> Closed deal | ~20-50% | Implied by 10-20 calls -> 1-2 deals | Calculated |

**Volume requirement for 100 booked calls/month:** Contact 10,000 prospects at 1% booking rate. (NLM Signal 41)

---

## Cost Benchmarks

| Metric | Value | Source |
|--------|-------|--------|
| Cost to email 5,000 prospects | <$500/month | LinkedIn Signal 27 |
| CAC (cold email only) | $100 | LinkedIn Signal 27 |
| CAC (omnichannel, in-house) | <$1,000 | X Signal 16 |
| iPhone video ad cost per call | $75/call ($1,868 spend for 25 calls) | LinkedIn Signal 28 |

**Comparison to paid ads:** "You need thousands upfront just to get profitable" with paid ads vs. <$500 to start with cold email. (LinkedIn Signal 27)

---

## Reply Rate Benchmarks by Campaign Type

| Campaign Type | Positive Reply Rate | Notes |
|--------------|-------------------|-------|
| ListKit 47-word script | 75/19,000 (0.39%) | Lead magnet CTA, NLM Signal 43 |
| Movie script AI tool | 297/23,000 (1.29%) | Outlier performer, NLM Signal 43 |
| Real estate | 164/15,000 (1.09%) | NLM Signal 43 |
| Custom merchandise | 611 over 15 months | Highest absolute volume, NLM Signal 43 |
| Ecom "AI Avatar" angle | 8/2,400 (0.33%) | Underperformer, NLM Signal 43 |
| Low-volume targeted (web design) | 9/1,200 (0.75%) | 2-week campaign, LinkedIn Signal 26 |

---

## Booking Rate Data

| Campaign | Emails Sent | Calls Booked | Booking Rate |
|----------|------------|-------------|-------------|
| ListKit | 494,000 | 685 | 0.14% |

**Booking rate improvement tactics:**
- Remove Calendly links, propose specific times: "booking rate jumped immediately" (LinkedIn Signal 32)
- Double-book calendar slots: 50-80 extra live calls/month (LinkedIn Signal 43)
- Follow up 20-30+ times (NLM Signal 63, constants across all periods)
- Extreme case: 50-60 follow-ups on a single prospect before booking (Dallas, NLM Signal 46)

---

## Open Rates (Deprecated Metric)

> Open rates: >50%
> -- NLM Signal 41

Christian no longer tracks open rates. The tracking pixel triggers Google/Microsoft spam filters. Measure success by positive reply rate only. (NLM Signal 56)

---

## Aggregate Business Metrics (Scale Context)

| Metric | Value | Period |
|--------|-------|--------|
| Total emails sent | 1-3.5 million | 3 years |
| Total emails referenced in teaching | 15 million+ | Career to date (LinkedIn Signal 14) |
| Cash collected | $3.5M | Aug 2021 - late 2023 |
| Agency margin | 82.5% ($660K profit on $800K revenue) | 2022 |
| In-house lead gen results | 19 deals, $40K cash, $13K MRR | 3 months (2026) |

---

## Diagnostic Framework

When a campaign underperforms, diagnose in this order:

| Check | Threshold | Action |
|-------|-----------|--------|
| Positive reply rate | <0.5% after 2,000+ emails | Offer or angle problem. Test new angles (4 at a time). |
| Positive reply rate | 0.5-1% | Acceptable. Optimize angle, don't overhaul. |
| Positive reply rate | >1% | Campaign is working. Scale volume. |
| Booking rate | 0 bookings from 10+ positive replies | Post-reply process problem. Check CTA, follow-up timing, Calendly usage. |
| Booking rate | Bookings happening but no shows | Check: sending Calendly link vs. specific times, confirmation automations. |
| Deal close rate | Calls happening but not closing | Not a copy problem. Sales process or offer-market fit issue. |

---

## Volume-to-Testing Capacity Rules

| Monthly Lead Volume | Angles to Test | Source |
|--------------------|---------------|--------|
| 50,000 leads/month | 8 angles | LinkedIn Signal 6 |
| 2,000 leads/month | 4 angles max | LinkedIn Signal 6 |

> "More volume = more testing opportunities. Less volume = focus on fewer, stronger angles."
> -- LinkedIn Signal 6

---

## Agent Instructions

When advising on campaign performance:
1. Use 1 client per 1,000 emails as the baseline. Anything better = outperformance.
2. Never reference open rates. They are a deprecated metric.
3. Positive reply rate is the primary metric. Contacts-per-positive-response is the diagnostic number.
4. When a campaign is underperforming, diagnose offer first, copy second, infrastructure third.
5. Volume determines testing capacity. Don't run 8 angle tests on a 2,000-lead/month list.
