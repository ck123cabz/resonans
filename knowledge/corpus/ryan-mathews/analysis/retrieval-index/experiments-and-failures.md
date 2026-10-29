---
type: corpus
aliases: ["Experiments and failures"]
corpus: ryan-mathews
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-10-08
generated: 2026-10-07
source_data: analysis/pass-1/lanes-5-7-offer-metrics-ai.md, lanes-1-2-funnel-vsl.md, lane-8-sweep.md, inventory-examples.tsv
---

# Experiments and failures

What Ryan tested, what lost, and the funnels he took apart because they were failing. The profile asks for "any claim about what fails"; this file holds them. Winning tests with a clean number are in `benchmarks-and-numbers.md`; this file keeps the losers, the reversals and the stories around them.

Dates are YouTube upload dates. File paths are relative to `knowledge/corpus/ryan-mathews/.raw/`.

## The 200 experiments video: what converts

- **Type:** [METRIC]
- **Provenance:** [D]
- **Date:** 2026-06-05
- **Source:** `video/i-ran-200-sales-funnel-experiments-here-s-what-converts.md`
- Wins: price $149 → $99 (+112% revenue, Yans Larson); annual-upgrade OTO (10–13% take, George Gammon); survey moved from pop-up to page (+31%); "It all started with a call" cards under the calendar (booking 38% → 50%); unused phone field removed from checkout (+46% sales); order form embedded on the page (+239%, "probably not repeatable").
- Losses: 3–5x more social proof (organic −50%); iClosed calendar (booking 35% → 15%).
- Price tests come first in his offer: "if you come and work with us at Funnel Architecture ... there's a good chance if you sell something you know direct on checkout that this will be one of the first things we do for you".

## More social proof lost: organic conversion halved

- **Type:** [METRIC]
- **Provenance:** [D]
- **Date:** 2026-06-05
- **Source:** `video/i-ran-200-sales-funnel-experiments-here-s-what-converts.md`
- "going back to Robert Kaldin like add social proof ad social proof ad social proof which again in general is a good principle but recently". Tripling to quintupling proof made organic conversion "like 50% lower"; ads +32%, not conclusive. Lesson: "you got to test these like per traffic source".

## A benefit CTA lost to "Apply now"

- **Type:** [METRIC]
- **Provenance:** [D]
- **Date:** 2026-03-05
- **Source:** `video/the-only-vsl-funnel-training-you-ll-ever-need-1-3m-vsl.md`
- He teaches benefit CTAs ("yes let's create my pitch", "send me my book"). On Steve's page a benefit-worded button "slightly lowered conversion rate i think it was probably just too wordy". "Apply now" stayed.

## Pre-call objection emails did nothing

- **Type:** [METRIC]
- **Provenance:** [D]
- **Date:** 2026-03-26
- **Source:** `video/this-landing-page-makes-him-116-000-day-copy-it.md`
- Four objection emails, 6 hours apart, over 225 booked calls. First email ~98% opened. Show rate +0.2%, close rate the same: "not even statistically significant not even close".

## The VSL-to-call funnel that halved a client's close rate

- **Type:** [CASE]
- **Provenance:** [D]
- **Date:** 2025-09-10
- **Source:** `video/repaired-transcript-i-made-this-business-owner-249-000-mo-learned-this.md`
- He replaced a client's low-ticket front end with his own award-winning VSL-to-call funnel. "We sent everyone including the organic audience to the VSSL". More calls, worst month of the year: close rate 60% → 30%, and $30K–50K of low-ticket revenue gone.
- The same funnel type won his first Two Comma Club award elsewhere; the loss was client-specific.

## The swim coach: a failing ad funnel losing $250K a year

- **Type:** [CASE]
- **Provenance:** [D]; credentials [X:swim coach page]; $250K is Ryan's estimate
- **Date:** 2026-01-07
- **Source:** `video/i-dissected-a-failing-ad-funnel-losing-250-000.md`
- Ex-Olympian coach (addressed as Carl), Four-Step Fast Freestyle course, Facebook ads since turned off. Ryan found the ad while training for a triathlon.
- Mistake 1, no video: he calls a page with no video "mistake number one", citing Hormozi's secondhand "something like a 40% drop".
- Mistake 2, the price: "The digital product he was selling was $3.90 which if you know anything about running ads you know that's nearly impossible to make profitable". Test it by EPV.
- Mistake 3, the back end is buried: the coaching application sits on the thank-you page and sells through DMs. Fix: a "last step" survey right after purchase, then a calendar.
- Do not touch the copy, testimonials or credibility; they are excellent.
- A teardown, not an engagement: Ryan changed nothing and reports no outcome. The $250K is "over a quarter million dollars on the table every single year", his estimate.

## The $67 upsell that blocked the back end

- **Type:** [CASE]
- **Provenance:** [D]
- **Date:** 2026-01-07
- **Source:** `video/i-dissected-a-failing-ad-funnel-losing-250-000.md`
- The upsell averaged about $4 a buyer and stood between buyers and the back end. Removing it: "an extra $12,000 a month right So just by thinking to remove this page we 3x the revenue". He forgets the exact figures.

## His own Google Doc VSL flop

- **Type:** [CASE]
- **Provenance:** [D]
- **Date:** 2023-09-12
- **Source:** `video/how-sam-oven-s-made-940-000-in-30-days-genius-strategy.md`
- Modeled on Sam Ovens' WeTube Google Doc. It flopped because he had just sold his list and audience and "in this new market no one really knew me". He says "it's kind of expected that it's going to flop". He does not mention cold ads.

## His 2019 funnel: customised instead of modeled

- **Type:** [CASE]
- **Provenance:** [D]
- **Date:** 2025-07-10
- **Source:** `video/why-your-audience-isn-t-buying-from-you-7-mistakes.md`
- Landing page → video page → calendar → thank-you, on paid ads. It worked poorly because he over-customised instead of copying Sam Ovens' proven funnel. Lesson: copy what works until you surpass your teacher. Also told: a mentor (Spencer Van) saw it and said "dude your funnel is" (`video/3-books-i-used-to-grow-my-business-to-1-000-000.md`, 2022-12-20).

## Hormozi's organic-as-ads: one 12.43x winner, more than half flopped

- **Type:** [METRIC] / [AI]
- **Provenance:** [X:Hormozi] strategy; [D] results
- **Date:** 2026-03-19
- **Source:** `video/how-i-automated-alex-hormozi-s-entire-ad-strategy-with-ai.md`
- He ran 77 ads the traditional way and 8 as organic posts with a "click to to grab a thing" banner (as captioned). One hit 12.43x, "but more than half the ads following his strategy flopped". That miss rate is why he built an AI agent to predict which posts cross over (see `claude-and-ai-workflows.md`).

## Opt-in skipped: fewer calls, lower close (his old test)

- **Type:** [METRIC]
- **Provenance:** [D]
- **Date:** 2025-01-02
- **Source:** `video/how-jeremy-miner-built-a-24m-sales-funnel-genius-marketing.md`
- "a few years ago we did test it and it seemed pretty consistent and if you skip the optin page you got less calls the calls you got closed at a lower rate". His current stance is the reverse; see `page-flow-and-booking.md`.

## Tool and checkout swaps that lost

- **Type:** [METRIC]
- **Provenance:** [D]
- **Date:** 2026-06-05; 2025-07-10; 2023-01-12
- **Source:** `video/i-ran-200-sales-funnel-experiments-here-s-what-converts.md`; `video/why-your-audience-isn-t-buying-from-you-7-mistakes.md`; `video/repaired-transcript-how-i-tripled-a-course-business-in-42-days-3-steps.md`
- iClosed calendar: booking 35% → about 15%.
- Add-to-cart for a 3D kitchen design service (Patrick): conversions dropped "a ton".
- Teachable checkout: moving the cart back to ClickFunnels "immediately the sales went back up and this results in over five thousand dollars in revenue".
- Price inside a band: $197 → $147 changed nothing ("they're both like under 200 bucks"), `video/the-easiest-way-to-double-your-sales-funnel-revenue.md` (2026-09-11).

## Where the Claude page audit got it wrong

- **Type:** [AI]
- **Provenance:** [D]
- **Date:** 2026-05-01; 2026-05-29
- **Source:** `video/claude-just-changed-landing-pages-forever.md`; `video/claude-clarity-new-skill-insane-conversion-rates.md`
- It called a bright blue button dark and nearly invisible; reported placeholder cards visitors never see; over-indexed one PayPal rage-click session; proposed click-through to checkout as the main metric ("what matters is the stinking conversion rate"); changed four things in one variant. "supplemental not a replacement yet".

## The vibe-coded funnel's silent email bug

- **Type:** [AI]
- **Provenance:** [D]
- **Date:** 2026-07-23
- **Source:** `video/i-vibe-coded-a-sales-funnel-to-25k-arr-in-30-days.md`
- Resend abandoned-cart emails sent nothing for 30 days, then the whole sequence at once, then every email twice: "they got all of the emails from the sequence all at once when it was supposed to be dripped over multiple days".

## The AI-built course funnel he would not run

- **Type:** [AI]
- **Provenance:** [D]; copy and price range [X:ChatGPT]
- **Date:** 2023-02-22
- **Source:** `video/repaired-transcript-i-built-an-entire-sales-funnel-using-chatgpt-midjo.md`
- AI Prodigy, a course built in 24 hours with ChatGPT and Midjourney, $2,800. His verdict on the sales page: it would probably not work; "for this type of online course I wouldn't use this sales page funnel I would use a vsl funnel".

## Funnel fatigue: every funnel dies in 6 to 18 months

- **Type:** [FUNNEL]
- **Provenance:** [D]; Ovens' cycle [X:Ovens]; offer fatigue [X:Suby]
- **Date:** 2025-07-10; 2026-07-02
- **Source:** `video/why-your-audience-isn-t-buying-from-you-7-mistakes.md`; `video/sabri-suby-s-meta-ad-strategy-behind-300m-in-ad-spend.md`
- "he went from like a traditional VSSL to this really fancy VSSL that just shot up uh conversions and eventually that dies off". Fix with novelty: same offer, new angle.
- Suby's free-book offer is the exception: "offer fatigue typically is like six to 12 months this is just going which is insane".
