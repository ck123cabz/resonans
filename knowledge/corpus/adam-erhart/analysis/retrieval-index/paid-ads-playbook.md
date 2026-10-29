---
type: corpus
aliases: ["Paid Ads Playbook"]
corpus: adam-erhart
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-19
---

# Paid Ads Playbook

Platform settings, budgets, creative testing, and the metric thresholds that decide kill or scale. Source: `q38`, `q39`. Provenance `[S]`.

Ads are an accelerator, never an initiator. They amplify a clear offer and a working backend. On an unoptimised listing or a broken offer they only make it fail faster.

---

## Meta (Facebook and Instagram)

### Objective
Align the campaign objective with the business outcome: **Leads** or **Sales**. He warns explicitly against Brand Awareness, Traffic or Video Views when the goal is client acquisition.

Settings: Manual Control (or Tailored Leads for simplicity), A/B testing off at campaign level, Advantage Campaign Budget on when scaling across ad sets.

### Targeting
Leave it broad, open age, gender and region, on roughly half of campaigns, and let the creative and hook do the qualifying. The algorithm is good enough now.

When using detailed targeting, stay at broad industry pools. Do not over-segment into tiny ad sets.

Retarget from **Meta Sources** (video watch time, lead form opens, page and profile engagement) rather than the website pixel, because of tracking and privacy changes.

### Budget
**Daily ad-set budget at 3 to 5x your target CPA.** A $5 lead goal means $15–$25/day per ad set. This gives the algorithm 3 to 5 conversions a day, which is what it needs to exit the learning phase.

### Structure
| Monthly spend | Campaigns | Ad sets | Ads per set |
|---|---|---|---|
| Under $1,000 | 1 | 2–3 | 2–3 |
| Under $10,000 | max 3 |, |, |

The anti-pattern is **lump-and-dump**: every audience, retargeting group and variation in one campaign, or micromanaging $1–$5/day budgets. That is outdated pre-algorithm practice and it produces inflated costs, ad fatigue and prematurely killed winners.

### Creative
Turn on **Dynamic Creative** at the ad set level: 2 to 3 primary texts, 2 to 3 headlines, 2 to 3 visuals.

**The 5 visual angles** for generation:
1. Literal, the product or service directly
2. Metaphorical, an abstract visual for the concept
3. Dream / ideal outcome, the final result or the freedom
4. Funny or weird, scroll-stopping
5. Text on colour, plain text on bold blocks

*In a single Dynamic Creative test slot he collapses this to three: literal, metaphorical, ideal outcome. Five for generation, three per test.*

**Ugly beats polished.** Raw graphics, plain text on colour, casual iPhone footage and MS-Paint-style design break the feed pattern, stop the scroll and cost less per click than agency-produced visuals. The brain automatically filters out what looks like an ad.

### Lead capture
Prefer Meta's native **Instant Forms** over sending traffic to an external site. They keep the user in-app, remove page-load friction and bypass pixel issues. Select "More Volume" and mirror the ad headline on the form greeting.

### Comment-to-DM
Pair a Reel or image post with automation (HighLevel or ManyChat). The CTA is "Comment START below and I'll DM you the free guide." On a comment, the software posts a public reply ("Just sent it to your DMs!") and fires a private DM with the opt-in or booking link.

He claims up to 5,000+ leads a day from this. That figure is far above anything else in the corpus and is unverified, the mechanism is sound, the number is not established.

---

## Google Ads

Google is high-intent search. People there are actively looking for a solution now.

**Keywords.** Target ready-to-buy queries, "24-hour emergency roofer in Denver", "best CRM for coaches", not informational ones like "what is a CRM".

**Negatives.** Run them heavily: "free", "cheap", "diy", "jobs".

**Bidding.** Move off Maximize Conversions, which hands Google a blank cheque against your daily budget. Use **Target CPA**. Start conservative at around $11. If it will not spend after 3 to 4 days, raise the tCPA in $5 steps, $16, $21, until traffic flows at the lowest profitable cost.

**Testing window.** $10–$20/day, and leave it untouched for at least 3 to 4 days before diagnosing anything.

---

## YouTube

From a session with Alec of AdOutreach, so this is a guest's methodology relayed through Erhart.

### Script, three steps
1. **Hook, 0–15 seconds.** A pattern interrupt naming the exact target market.
2. **Educate, 15–60+ seconds.** Real actionable substance, or bust a common industry myth. Scratch the learner mindset.
3. **CTA, 30–40 seconds total.** Force a clear decision. Repeat the CTA three times.

### Production
Authentic casual video on an iPhone with a handheld gimbal outperforms overproduced commercials.

**Upload ad videos as Unlisted** on your main channel. Running public videos as ads wrecks the channel's average view duration.

### Settings
| Setting | Value |
|---|---|
| Objective | Leads. Uncheck native lead forms if sending to an external VSL. |
| Bidding | Target CPA, $11–$16 start |
| Device exclusions | Exclude TV screens. Saves 5–10%. |
| Enhancements | Turn off Video Enhancements, which warps horizontal video into distorted Shorts. |
| Frequency | Cap at 3 views per month per user |

### Alpha AI Targeting
Do not rely on Google's pre-built audiences, which give average results. Build **Custom Segments** across three inputs:

1. **Search intent**, the exact queries typed into Google and YouTube ("how to scale a marketing agency", "best HVAC software").
2. **URLs**, competitor sites, industry software tools, the blogs your audience reads.
3. **YouTube remarketing**, past channel viewers, likers, subscribers.

Built with a tool like KeywordSearch.com, across 3 to 5 sub-categories.

**Uncheck Optimized Targeting** on launch. It lets Google expand outside your segments and dilutes the test data.

---

## Other platforms

### Snapchat
Reaches 75–90% of ages 13–34 in 25+ countries. Use Advanced Create, not Instant Create, for full bidding and audience control. Install the Snap Pixel via a partner integration. Test at $10–$30/day per ad set for 4 to 15 days. Auto Bid first, then manual or value optimisation once conversion data builds. Creative: 10 to 15 second vertical video, sound-on with captions, attention in the first 1 to 2 seconds, UGC works. Sequential retargeting, brand intro, product demo, limited discount, plus dynamic cart abandonment. Scale 10–20% every few days.

### LinkedIn
B2B decision-makers and high-ticket consulting. Single image, carousel, video, document ads and lead gen forms. Higher CPC than Meta, justified by reaching vetted professionals. Pair paid with profile SEO using Google Keyword Planner terms in the headline and bio.

### Amazon Sponsored Display for non-Amazon sellers
Amazon opened Sponsored Display to businesses that do not sell on Amazon (US beta). Service brands can target on Amazon's first-party shopping, browsing and streaming signals. Flexible daily budget (a $100 test), no minimum, CPC or vCPM. Three audience strategies: Amazon Audiences (lifestyle, in-market, life events), Views (retargeting people who viewed related product categories), Purchases (recent buyers in adjacent categories). Upload a logo, a headline and a clean lifestyle image; Amazon re-crops it or supplies free Shutterstock imagery.

---

## Red / Yellow / Green

| Light | Threshold | Action |
|---|---|---|
| **Red** | Below breakeven after the learning phase | Pause immediately. Read CTR, opt-in and sales conversion, find the leak, fix it, relaunch. Do not bleed hoping for a miracle. |
| **Yellow** | Breakeven to 1.5x, spend $100, make back $101–$110 | Keep running. **Optimise, do not scale.** |
| **Green** | 3x+ ROAS | Scale, duplicate campaigns and audiences, double down. |

**Do not scale a yellow light.** Cranking budget on a breakeven ad spikes CPM and CPC and turns it red. He says this is the rule people break most.

---

## Benchmarks

**The magic metric: $1 in, $1 out.** Break even on the front end and you can run unlimited volume without depleting capital, while backend follow-up and lifetime value are the profit.

| Metric | Target |
|---|---|
| Landing page / lead magnet opt-in | 20–30%, up to 33% optimised |
| High-commitment direct sales page | 2–5% |
| Discovery call close, beginner | 25% |
| Discovery call close, with pre-call framing | 33–45%+ |
| Cold email, bulk | 1% |
| Personalised 2-minute Loom audit | 10–15% |
| Link click-through rate | 1–3%+, winners 2.75–3.04% |
| LTV:CAC over the client lifetime | 3x–10x |

**Link CTR, not CTR.** He ignores overall click-through rate, which counts likes, comments and image expands, and tracks Link CTR only. A high CTR with low sales is performance theatre.

**CPL against EPL.** Always judge cost per lead against earnings per lead. A $10 CPL yielding $100 EPL beats a $5 CPL yielding nothing.

**The local conversion stack.** An unoptimised local business closes about 10% of inbound. Stacking the AI receptionist, missed-call text-back and review automation at a claimed 20% lift each compounds past 20%.

---

## Timing and testing

**The 72-hour rule.** Launch and do not touch it for 3 to 4 days. No obsessive dashboard-watching, no panic edits while the algorithm gathers data.

**Kill** anything still below breakeven after 3 to 4 days with no qualified leads.

**Scale** green lights by 10–20% every few days on Meta and social, to avoid throwing the algorithm back into learning. On Google, step the tCPA up $5 at a time.

**Test one variable at a time**, three headline hooks against identical body and image, and wait for significance. Never judge on ten clicks.

*Note the tension: the single-variable rule and Dynamic Creative, which varies three things at once, are both recommended. He does not reconcile them.*
