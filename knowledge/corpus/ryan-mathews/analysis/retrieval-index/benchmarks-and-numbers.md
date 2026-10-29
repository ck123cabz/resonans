---
type: corpus
aliases: ["Benchmarks and numbers"]
corpus: ryan-mathews
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-10-08
generated: 2026-10-07
source_data: analysis/pass-1/lanes-5-7-offer-metrics-ai.md, lanes-1-2-funnel-vsl.md, lanes-3-4-format-page.md, inventory-examples.tsv
---

# Benchmarks and numbers

Every number in the corpus that a funnel decision could lean on, one heading per metric, with the file and upload date. Most are single-client tests. Ryan hedges his own wins ("probably not repeatable", "it's inclusive [inconclusive]") and separates organic from paid on almost every test; the hedges are kept here because NotebookLM stripped them.

Where two of his videos give two numbers for the same thing, both are kept. File paths are relative to `knowledge/corpus/ryan-mathews/.raw/`.

## VSL watch time and retention: no figure exists

- **Type:** [METRIC]
- **Provenance:** [A]
- **Date:** n/a, all 73 transcripts searched
- **Source:** nearest lines in `video/alex-hormozi-s-advice-for-sales-funnels.md` and `video/i-ran-200-sales-funnel-experiments-here-s-what-converts.md`
- No VSL watch-time, play-rate, completion or drop-off-by-minute figure anywhere. Nearest: Vidalytics "Your play rate is going to go through the roof". The only percentage watched: retargeting people who "watched 95%" of an ad (Mr X, FHL 2025).

## Revenue and ROAS: Steve's $1.3M in 141 days, 9.5x, $11 per booked call

- **Type:** [METRIC]
- **Provenance:** [D]
- **Date:** 2026-03-05
- **Source:** `video/the-only-vsl-funnel-training-you-ll-ever-need-1-3m-vsl.md`
- $1.3M and 1,800+ leads in 141 days, mostly organic. Meta ads at low spend in 2026: "9.5x return on ad spend so far", first-week cost per booked call $11.
- $1.3M over 141 days is about $9,200 a day. The "$6,500 a day" line (`video/how-to-create-a-1m-video-sales-letter-vsl.md`, 2025-12-02; `video/the-ultimate-funnel-for-selling-high-ticket-offers.md`, 2025-11-19) is from an earlier date and most likely the same client.

## Opt-in rate before a VSL: 20 to 30%, $10 to $20 per viewer

- **Type:** [METRIC]
- **Provenance:** [D]
- **Date:** 2025-03-12
- **Source:** `video/how-iman-gadzhi-made-100m-online-genius-strategy.md`
- "typically they have a 20 to 30% optin rate so they're paying typically $10 to $20 to get someone just to start watching their vsl", at $1–5 a click.

## Lead-to-sale on a traditional VSL: about 1%

- **Type:** [METRIC]
- **Provenance:** [D], a rule of thumb
- **Date:** 2025-03-12
- **Source:** `video/how-iman-gadzhi-made-100m-online-genius-strategy.md`
- "a traditional vssl ... probably converts about 1% lead to conversion". His guess for Iman's YouTube-hosted VSL: near 0.2%.

## Opt-in-to-call ratio: about 80% at comparable clients

- **Type:** [METRIC]
- **Provenance:** [D]
- **Date:** 2024-10-23
- **Source:** `video/repaired-transcript-how-to-find-optimizations-in-your-sales-funnel-mic.md`
- "I see kpis of other clients who have similar funnels that have like an 80% opt-in to call ratio but mine is lower than that". His own figure is not given.

## Booking rate: 38% to 50% with testimonials under the calendar

- **Type:** [METRIC]
- **Provenance:** [D]
- **Date:** 2026-06-05
- **Source:** `video/i-ran-200-sales-funnel-experiments-here-s-what-converts.md`
- "it went from 38% booking rate to a 50% uh booking rate so it's a 32% relative lift on their organic funnel". Unnamed client, not Steve.
- Same video: swapping a client's calendar for iClosed, "we went from a 35% booking rate to a 15".

## Booking rate: 5% to 20% with more content on the page

- **Type:** [METRIC]
- **Provenance:** [D]
- **Date:** 2025-05-05
- **Source:** `video/repaired-transcript-he-built-a-4-step-10-000-000-funnel-full-breakdown.md`
- Opt-ins fell, strategy-session booking went "from like 5% to 20%", cost per call "from like getting close to $1,000 down to like $250". He calls it early and inconclusive.

## Show rate: 50%, plus 25% with a 2-to-3-day booking cap

- **Type:** [METRIC]
- **Provenance:** [D]; AJ&Smart's 80% [X:Courtney]
- **Date:** 2025-05-05
- **Source:** `video/repaired-transcript-he-built-a-4-step-10-000-000-funnel-full-breakdown.md`; `video/this-landing-page-makes-him-116-000-day-copy-it.md`
- "We've seen show rate be at 50%. And you change nothing else by not letting people book no more than 3 days out ... and show rate like immediately jumps up 25%." Relative or points: not said.
- AJ&Smart's show rate "about 80%. Which is decent", booking 4 days out.
- 2025: "one of the hardest metrics to get right especially with paid ads is show rate" (`video/the-ultimate-funnel-for-selling-high-ticket-offers.md`, 2025-11-19). No baseline for his own funnels. [A]

## Show rate: pre-call objection emails, +0.2%

- **Type:** [METRIC]
- **Provenance:** [D]
- **Date:** 2026-03-26
- **Source:** `video/this-landing-page-makes-him-116-000-day-copy-it.md`
- Four objection emails 6 hours apart, over 225 booked calls: "we saw show rate go up by 0.2% so literally nothing", close rate "literally exactly the same". He planned another 500 calls.

## Close rate: 25 to 30% on a traditional VSL-to-call funnel

- **Type:** [METRIC]
- **Provenance:** [D]; scale thresholds [X:Cole Gordon]
- **Date:** 2026-04-16; 2024-12-11; 2025-09-30
- **Source:** `video/this-funnel-generates-1-6m-mo-without-sales-calls.md`; `video/repaired-transcript-how-i-grew-a-clients-business-by-500-in-10-months.md`; `video/scaling-to-1m-isn-t-hard-if-you-copy-this.md`
- "you have a 25 30% close rate if you're good and you know you sell a 5,10 or $15,000 typically one-time offer".
- A part-time closer trained with a 45-minute Loom: "his close rate was over 40% from day one" on $1,000 coaching.
- Cole Gordon's raise-the-price thresholds: close rate above 25%, upfront cash above 40%, AR above 80%.

## Close rate: 60% vs 30%, low-ticket buyers vs straight-to-VSL

- **Type:** [METRIC]
- **Provenance:** [D]
- **Date:** 2025-09-10
- **Source:** `video/repaired-transcript-i-made-this-business-owner-249-000-mo-learned-this.md`
- "the calls were converting at 30% rather than 60%". Low-ticket buyers were about twice as likely to buy the back end. Quote: "once someone hands you even just $1, they're much more likely to hand you more".

## Apply button under the VSL: 5–15% or 10–20%

- **Type:** [METRIC]
- **Provenance:** [D], two videos, two ranges
- **Date:** 2025-10-07; 2025-11-19
- **Source:** `video/the-only-funnel-training-you-ll-ever-need-1m-funnel.md`; `video/the-ultimate-funnel-for-selling-high-ticket-offers.md`
- "you're probably missing out on 5 to 15% of more applications" vs "we've seen 10 to 20% more conversions or more applications in this case by just adding that button".

## Logo bar under the VSL: +10%

- **Type:** [METRIC]
- **Provenance:** [D]
- **Date:** 2026-03-05
- **Source:** `video/the-only-vsl-funnel-training-you-ll-ever-need-1-3m-vsl.md`
- Big-tech logos under Steve's button: "we AB tested we didn't have this at first and it improved conversions by 10%".
- An earlier proof addition on Steve's landing page: "something like 30%", test not finished (`video/alex-hormozi-s-advice-for-sales-funnels.md`, 2026-02-03).

## Survey embedded on the page: +31%; 4.4% to 5.9%

- **Type:** [METRIC]
- **Provenance:** [D]
- **Date:** 2026-06-05; 2024-10-23
- **Source:** `video/i-ran-200-sales-funnel-experiments-here-s-what-converts.md`; `video/repaired-transcript-how-to-find-optimizations-in-your-sales-funnel-mic.md`
- Application funnel: "we moved it to the page and we saw a 31% increase in conversion rate".
- Lead funnel, the same fix: "going from 4.4 to 5.9 that's like a I think it was a 32% increase in leads". Microcopy under the fields then took it to 7.1% against a 6% goal.

## Vidalytics: +10 to 25% on average, +66% applications for one client

- **Type:** [METRIC]
- **Provenance:** [D]; affiliate link disclosed on camera
- **Date:** 2026-06-05; 2025-06-12; 2026-02-03
- **Source:** `video/i-ran-200-sales-funnel-experiments-here-s-what-converts.md`; `video/repaired-transcript-how-karlton-dennis-made-a-11-5m-sales-funnel-geniu.md`; `video/alex-hormozi-s-advice-for-sales-funnels.md`
- "it averages a 10 to 25% increase in conversions"; smallest seen "like a 16% increase"; one live test "30 or 40% better than the control".
- A client test "quite literally increased applications on their funnel by 66% at a 100% statistical significance".
- Limit: it only gets more people to watch, so it does nothing when the VSL is bad.

## Form fields: 5 to 40% each; phone field 30 to 46%

- **Type:** [METRIC]
- **Provenance:** [D]; the 11-vs-4 study [X:study he cites]
- **Date:** 2025-05-23; 2026-06-05; 2024-07-24
- **Source:** `video/how-codie-sanchez-built-a-12-000-000-sales-funnel-copy-it.md`; `video/i-ran-200-sales-funnel-experiments-here-s-what-converts.md`; `video/repaired-transcript-how-ryan-pineda-built-a-21-9m-sales-funnel-genius.md`
- "every single form field you add to your forms is going to decrease conversions depending on what it is by 5 to 40% I would say". Phone on an opt-in: "typically you can see 30 40% improvement in optin rate if you don't have that". A dropdown: about 10%.
- Unused phone field removed from a checkout: "we saw an increase in conversion by 46%".
- Study cited on the Pineda video: 11 fields vs 4, "160% Improvement in conversion rate".

## Trustpilot badge under every CTA: +149.2%

- **Type:** [METRIC]
- **Provenance:** [D], Ryan's client (not Ravi Abuvala's)
- **Date:** 2024-05-21
- **Source:** `video/how-ravi-abuvala-made-a-25m-sales-funnel-genius-strategy.md`
- "because it was a long landing page and their conversion rate went up by 149. 2%". One test.

## Above the fold: 60% never scroll

- **Type:** [METRIC]
- **Provenance:** [X:Hormozi], which Ryan agrees with
- **Date:** 2026-02-03
- **Source:** `video/alex-hormozi-s-advice-for-sales-funnels.md`
- "something like 60% of people never get below that". Approximate in his words.
- One client's Claude audit (`video/claude-just-changed-landing-pages-forever.md`, 2026-05-01): scroll depth 41% on the main page, 25–35% on affiliate pages, bounce 54–79% on affiliate pages, some users leaving "sometimes within six seconds". One client, not a benchmark.

## Lead-page length: cutting below the fold, +51% and more

- **Type:** [METRIC]
- **Provenance:** [D]
- **Date:** 2026-04-02; 2024-11-14; 2024-05-31
- **Source:** `video/repaired-transcript-the-psychology-of-premium-landing-pages.md`; `video/i-fixed-sabri-suby-s-7-8b-sales-funnel.md`; `video/repaired-transcript-the-5-variables-behind-20-000-successful-sales-fun.md`
- "they went from a 2.32% conversion rate to a 3.51, which was a 51.17% improvement by just removing everything below the fold" (1,293 vs 1,283 visitors, 30 vs 45 leads).
- Other clients: +52%, +12%; "10, 20, 30%" generally. CTA moved above the fold: "7.5% more leads". Review badge: +10% (running), +16% (finished).
- For opt-in pages only. Application pages go the other way (booking 5% → 20%).

## Page load time: $41 to $8 cost per lead

- **Type:** [METRIC]
- **Provenance:** [D]
- **Date:** 2024-10-23
- **Source:** `video/repaired-transcript-how-to-find-optimizations-in-your-sales-funnel-mic.md`
- A webinar pop-up took "10 seconds all the way up to 2 minutes to load". A custom form: "conversion rate went from 10% to over 20% cutting their lead cost down from $41 to $8". Doubling alone would not give $8; possibly a caption error.

## Removing the video: about 40% drop (Hormozi's story)

- **Type:** [METRIC]
- **Provenance:** [X:Hormozi], secondhand
- **Date:** 2026-01-07
- **Source:** `video/i-dissected-a-failing-ad-funnel-losing-250-000.md`
- Hormozi said in the Skool Games that someone took the video off a Skool About page: "something like a 40% drop in conversions by just removing the video". Ryan forgets the exact number. Not his test.

## Removing the founder section: +74% webinar sales

- **Type:** [METRIC]
- **Provenance:** [D]
- **Date:** 2026-02-03
- **Source:** `video/alex-hormozi-s-advice-for-sales-funnels.md`
- "it resulted in 74% more sales of people that then watched the webinar and bought". His caveat: "I don't think that's going to be the result that necessarily holds".

## Social proof 3 to 5x: organic −50%, ads +32% (inconclusive)

- **Type:** [METRIC]
- **Provenance:** [D]
- **Date:** 2026-06-05
- **Source:** `video/i-ran-200-sales-funnel-experiments-here-s-what-converts.md`
- "the conversion rate bombed on organic it was like 50% lower for organic traffic and all we did was 3 to 5x the social proof on the page". On ads +32%, "so far it's not conclusive on ads".
- Contradicts his earlier line "It's really hard to overdo social proof" (`video/repaired-transcript-the-5-variables-behind-20-000-successful-sales-fun.md`, 2024-05-31). Not reconciled.

## Earnings per visitor (EPV): 11 cents to $2.80

- **Type:** [METRIC]
- **Provenance:** [D]
- **Date:** 2026-02-03; 2024-12-11
- **Source:** `video/alex-hormozi-s-advice-for-sales-funnels.md`; `video/repaired-transcript-how-i-grew-a-clients-business-by-500-in-10-months.md`
- EPV = revenue over unique visitors; "probably the single best North Star". One client went "from about 11 cents to $2.80" over two years ($7K to $450–500K a month).

## Conversion rate: 4.53% to 8.8% (Joel Turner) and 0.5% to 3.68% (Frankenfunnel)

- **Type:** [METRIC]
- **Provenance:** [D]
- **Date:** 2023-05-17; 2025-09-10
- **Source:** `video/rogan-shared-my-funnel-on-his-podcast-it-blew-up.md`; `video/repaired-transcript-i-made-this-business-owner-249-000-mo-learned-this.md`
- Joel Turner, total visitors to sales, within 30 days of a rebuild. AOV $185 → about $260.
- Frankenfunnel client: under 0.5% to 3.68% over a year of tests, "like a 7x improvement", each test "a 20% boost ... a 50% boost ... a 30% boost".

## Upsells and OTOs: 10 to 15% revenue, up to 41%

- **Type:** [METRIC]
- **Provenance:** [D]
- **Date:** 2025-10-07; 2026-06-05; 2025-10-21
- **Source:** `video/the-only-funnel-training-you-ll-ever-need-1m-funnel.md`; `video/i-ran-200-sales-funnel-experiments-here-s-what-converts.md`; `video/this-one-page-will-instantly-increase-your-revenue-15.md`
- "they can add 15% to the business"; "a good Otto easy 10 to 15% increase in revenue"; the OTO video says 15–40%.
- Annual-upgrade OTO (George Gammon): 10–13% take, AOV +115% and +150% in the same story. An unnamed community client: "$13,995 in extra revenue That's a 41% increase in revenue from one page".
- A complementary OTO ($147 on a $99 course): "converted at 70%". A $47 OTO: ~12% take.
- Start OTOs at $97. Low-ticket only.

## Order form embedded on the page: +239%, probably not repeatable

- **Type:** [METRIC]
- **Provenance:** [D]
- **Date:** 2026-06-05
- **Source:** `video/i-ran-200-sales-funnel-experiments-here-s-what-converts.md`
- "that number is crazy probably not repeatable we've tried it with few other clients and haven't seen that result". Some saw a decrease.

## Payment plan option: about +20% sales

- **Type:** [METRIC]
- **Provenance:** [D]
- **Date:** 2025-05-23
- **Source:** `video/how-codie-sanchez-built-a-12-000-000-sales-funnel-copy-it.md`
- $247 one-time or 3 × $89: "we saw no less people took the 247 but about 20% more people took the 89".

## Post-purchase survey completion: 90% and 98%

- **Type:** [METRIC]
- **Provenance:** [D]
- **Date:** 2026-01-07; 2025-06-12
- **Source:** `video/i-dissected-a-failing-ad-funnel-losing-250-000.md`; `video/repaired-transcript-how-karlton-dennis-made-a-11-5m-sales-funnel-geniu.md`
- "we have like a 90% completion rate of purchases who end up submitting this application"; another client "like 98% of buyers submitting that survey".

## Ad results: 12.43x ROAS, and $90K to $210K a month by doubling spend

- **Type:** [METRIC]
- **Provenance:** [D]; strategies [X:Hormozi] and [X:Cole Gordon]
- **Date:** 2026-03-19; 2022-11-28
- **Source:** `video/how-i-automated-alex-hormozi-s-entire-ad-strategy-with-ai.md`; `video/repaired-transcript-i-spent-1-000-000-on-youtube-ads-here-s-what-i-lea.md`
- Hormozi's organic-posts-as-ads, 77 ads the old way vs 8 his way: "one of our best performing ads at a 12.43x return on ad spend and cut our cost per sale by 2/3". More than half the 8 flopped.
- Cole Gordon told him to double spend for 30 days: "we went from 90 000 to 150 000 in 30 days", then $175K, then $210K (Nov 2022 video). His own YouTube ads rarely beat 2.5x ROAS.

## The MECLABS conversion heuristic: C = 4M + 3V + 2(I − F) − 2A

- **Type:** [METRIC]
- **Provenance:** [X:MECLABS]
- **Date:** 2024-05-31
- **Source:** `video/repaired-transcript-the-5-variables-behind-20-000-successful-sales-fun.md`
- From "a lab in Jacksonville, Florida" and "over 20,000 split tests": motivation, value, incentive, friction, anxiety. Motivation is the one you cannot add to; conversion "just like double in January from December" for that reason. He states the formula three slightly different ways; this is the form most sources give.

## ICE score for picking the next test

- **Type:** [METRIC]
- **Provenance:** [D]; ICE is a standard growth-team tool
- **Date:** 2026-02-03
- **Source:** `video/alex-hormozi-s-advice-for-sales-funnels.md`
- Impact, confidence, ease, each 1–10, averaged. An above-fold headline scores "a nine impact nine confidence and like a 10 east".

## Statistical significance: from 3-day splits to a calculator

- **Type:** [METRIC]
- **Provenance:** [D]
- **Date:** 2026-06-05; 2026-09-11
- **Source:** `video/i-ran-200-sales-funnel-experiments-here-s-what-converts.md`; `video/the-easiest-way-to-double-your-sales-funnel-revenue.md`
- At his old business he ran ClickFunnels splits for about 3 days and called them. Now: one variable, an even split, a significance calculator, and a free A/B price calculator that judges by revenue per visitor.
