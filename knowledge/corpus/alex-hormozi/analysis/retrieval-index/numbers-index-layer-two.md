---
type: corpus
aliases: ["Numbers Index, Layer Two"]
corpus: alex-hormozi
layer: retrieval
tags: [corpus, machine, money-model, numbers, pricing, unit-economics]
source: skills/corpus-ingestion
created: 2026-10-16
file: numbers-index-layer-two
---

# Numbers Index, Layer Two

This file extends the layer-one map of the same name, `numbers-index.md`, to layer two ($100M
Money Models and $100M Lost Chapters). Every figure in the eight layer-two files that carries a
rule or a claim, with its unit, what it governs, the scale it was stated at, its provenance and
its home. Grep the figure or the thing it measures. Compiled from the eight domain files below,
with `pass-2-reconciliation.md` "Layer two" (L2.1 to L2.6) applied where it overrides Pass 1.
Named frameworks are indexed in `frameworks-index-layer-two.md`.

**Files covered:** `money-model.md` · `attraction-offers.md` · `first-customers-layer-two.md` ·
`upsell-and-downsell.md` · `continuity.md` · `operating-the-model.md` ·
`hormozi-record-layer-two.md` · `layer-two-sweep.md`.

Rules this file obeys:

- Nothing is rounded or dropped. Ranges stay ranges. A figure given two ways keeps both.
- Where two answer files read the same figure differently, both readings sit in one row with the
  file each comes from.
- Where an answer's worked example does not fit its own stated ratio, or its sum does not add up,
  the row says so and gives the real figure. L2.4 rows 18 to 24 are cited where they settle one.
- A row marked "do not use" is one Pass 2 L2.4 says is garbled or a projection.

**Columns.** *Scale:* the scale the figure was stated at: general, gym, local service,
subscription, agency, B2B, e-commerce, info product, software, Gym Launch, his businesses, or US
where a figure depends on US rails. *Marker:* `[D]` matched to his own audio (Pass 2 §2 or L2.1);
`[M*]` NotebookLM's transcription and wording; `[A]` not in the sources. *Home:* file § heading,
exact.

**Standing caution.** These are his figures and NotebookLM's renderings of them, not measured
results. None of the money-model formulas or worked examples was matched to the audio; L2.1 matched
offer structures only. About 25 more sums in layer two are flagged in Pass 1 and not corrected
(L2.4); the ones below are flagged where they sit. q101 and q103 also draw on $100M Offers and
$100M Leads, so a figure here may be layer-one material retold. A figure repeated across files is
one retelling, not independent confirmation.

---

## Money model and customer financed acquisition

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| 30 days | window | the measuring window for gross profit in the money model and CFA | general | [M*] | `money-model.md` § Money model: definition; `money-model.md` § Customer financed acquisition: the three levels |
| GP < CAC; GP = CAC (q74: ≥ 1x CAC); GP ≥ 2x CAC | 30-day GP against CAC | CFA levels 1, 2, 3; q76 labels Level 2 "Good" and Level 3 "Ideal / Minimum Standard"; q75 defines CFA as GP > CAC, then sets Level 2 at "=" | general | [M*] | `money-model.md` § Customer financed acquisition: the three levels |
| ≥ 2x CAC | 30-day GP | his minimum standard for scaling a bootstrapped business (q75, q76); q99's Stage 2 target | general | [M*] | `money-model.md` § Customer financed acquisition: the three levels; `money-model.md` § Money model: four offer types in three stages; `operating-the-model.md` § What to change first: generate flow, monetize flow, then add friction |
| > CAC minimum; ≥ 2x CAC ideal | 30-day GP | q99's baseline | general | [M*] | `money-model.md` § Customer financed acquisition: the three levels; `operating-the-model.md` § Levers: CAC, LTGP and payback period |
| $5,000 | card limit | Level 2: the 30-day interest-free credit limit is the maximum ad budget | general | [M*] | `money-model.md` § Customer financed acquisition: the three levels |
| "two (or more)" (q75); one (q74) | new customers | what Level 3's surplus funds; at exactly 2x CAC it funds one | general | [M*] | `money-model.md` § Customer financed acquisition: the three levels |
| CAC $1,000; price $2,500; fulfilment $500; 30-day GP $2,000; $1,000 left | cash | worked Level 3; the answer says the $1,000 left funds "2 new customers", it funds one | general | [M*] | `money-model.md` § Customer financed acquisition: worked Level 3 example |
| 1, 3, 7, 15, 31, 63, 127, 256, 511, 1,023, 2,047, 4,095 | total customers | Level 3 compounding over 12 months from 1 customer; the series is 2^n − 1, so the eighth term is 255, not 256 | general | [M*] | `money-model.md` § Customer financed acquisition: the compounding series |
| $100 per $1 (100:1) | 30-day GP per ad dollar | his first year at Gym Launch; his claim, no outside record | Gym Launch | [M*] | `money-model.md` § Customer financed acquisition: the compounding series |
| 100 ways; 1, 2, 3 or 4 sessions a week | offers per product | "simple scales, fancy fails": four session counts make one product four offers | general | [M*] | `money-model.md` § Making your own money model: one offer at a time, and the rules |
| about 5 years plus 5 years; years 0, 5 to 10 | time | finding "which way is North", then building generational wealth; the Doom Loop resets to year 0 | general | [M*] | `money-model.md` § The ten-year view |
| over a decade | time | his and his wife's time to $100M net worth | his businesses | [M*] | `money-model.md` § The ten-year view |

---

## CAC, cost per engaged lead and gross profit

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| $1,000 sale; $200 ad spend; $500 true CAC | cash | counting only ad spend; the mistake decides between $1M a month, $10M a month, or going out of business | scaling company | [M*] | `money-model.md` § CAC: formula and what to count; `operating-the-model.md` § Warning: counting only ad spend in CAC |
| $200/month software + $3,000/month manager + $800 commission ($100 x 8) = $4,000; 8 customers; $500 | cost; CAC | outreach channel; arithmetic checks; identical in q75 and q76 | small outreach business | [M*] | `money-model.md` § CAC: worked examples by channel |
| 2 staff at $5,000/month ($10,000) + $1,000 commission ($100 x 10) = $11,000; 10 customers; $1,100 | cost; CAC | content channel; checks | content business | [M*] | `money-model.md` § CAC: worked examples by channel |
| $4,000 media buyer + $20,000 ad spend + $1,000 software + $10,000 commission ($1,000 x 10) = $35,000; 10 customers; $3,500 | cost; CAC | paid-ads channel; checks | paid-ads business | [M*] | `money-model.md` § CAC: worked examples by channel |
| $100,000 payroll ÷ 1,000 engaged leads = $100; 1 in 10; CAC $1,000; LTGP $4,000; 4:1 | CPEL; CAC; ratio | cost per engaged lead worked; checks | business with paid lead getters | [M*] | `money-model.md` § CAC from payroll: cost per engaged lead; `operating-the-model.md` § Cost Per Engaged Lead: payroll as the acquisition cost |
| $100,000/month; 30,000 engaged leads a month; $3.33 | payroll; CPEL | Acquisition.com content team, his claim; checks | his businesses | [M*] | `money-model.md` § CAC from payroll: cost per engaged lead; `operating-the-model.md` § Cost Per Engaged Lead: payroll as the acquisition cost; `hormozi-record-layer-two.md` § Record: other own-business claims in the offer chapters |
| $25 hard cost plus $75 of ads | cost per engaged lead call | layer one's lead-magnet version, named for comparison | general | [M*] | `money-model.md` § CAC from payroll: cost per engaged lead |
| $100 price; $20 fulfilment and shipping; $80 GP; 80%; 4 purchases; $320 LTGP | cash; margin | widget gross profit; "4 times, $320" in q76 only | product | [M*] | `money-model.md` § Gross profit: formula and worked examples |
| 10 packages at $1,000 ($10,000); 1 employee at $2,000; GP $8,000; $800 a customer | cash | service gross profit; checks | service | [M*] | `money-model.md` § Gross profit: formula and worked examples |

---

## LTGP, churn and the LTGP to CAC ratio

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| 5% or less; 20 months (1 ÷ 0.05) | monthly churn; lifespan | the churn target and the lifespan it implies | subscription | [M*] | `money-model.md` § Churn and lifespan: the 5% target and net organic growth |
| 200 clients; 8 cancel (4%, 25 months); 12 referred (6%); +2% a month | clients; rate | net organic growth worked; checks | subscription | [M*] | `money-model.md` § Churn and lifespan: the 5% target and net organic growth |
| $300/month; $60 fulfilment; $240 GP; 5% churn; $4,800 LTGP; $15,000 spend; 10 customers; $1,500 CAC; 3.2:1 | cash; ratio | subscription LTGP; checks; the tidy figures may be the model's own | subscription | [M*] | `money-model.md` § LTGP: worked examples |
| $3,000/month; $6,000/month rep for 10 clients; $30,000 revenue and $24,000 GP per rep (80%); $2,400 per client; 5%; $48,000 LTGP | cash | agency-style service LTGP; checks; the closest example to a retainer | agency | [M*] | `money-model.md` § LTGP: worked examples |
| $400,000 over 12 months; 10,000 customers; CAC $40; $10/month; $2 fulfilment; $8 GP (80%); 5 months; LTGP $40; 1:1 | cash; ratio | lemonade stand LTGP; the same stand has CAC $20 in the payback example, unexplained | illustrative | [M*] | `money-model.md` § LTGP: worked examples |
| below 3:1; 3:1; 5:1 to 10:1+ | LTGP:CAC | inefficient; minimum healthy; world class; layer one holds the same 3:1 floor | general | [M*] | `money-model.md` § LTGP to CAC: benchmarks; `layer-two-sweep.md` § q103 numbers held in other files: where to find them |
| $3,000 LTGP; $1,000 CAC | cash | q76's 3:1 example | general | [M*] | `money-model.md` § LTGP to CAC: benchmarks |
| 36:1 | ratio | his portfolio's lifetime average LTGP:CAC (`money-model.md`); "his career ad return" (`layer-two-sweep.md`); his claim, no record | his businesses | [M*] | `money-model.md` § LTGP to CAC: benchmarks; `layer-two-sweep.md` § q103 numbers held in other files: where to find them |

---

## Payback period

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| 30 days or less (q76: "under 30 days"); 0 to 14 days ideal (q74 only) | days | payback target | general | [M*] | `money-model.md` § Payback period: formula and target |
| longer than 30 days; 4x or more | reinvestment speed | payback past 30 days ties up working capital and slows reinvestment by 4x or more (q74) | general | [M*] | `money-model.md` § Payback period: formula and target |
| CAC $800; $500/month; $100 fulfilment; $400 GP; 30 days | cash; days | 30-day payback on the second payment | service | [M*] | `money-model.md` § Payback period: worked examples |
| CAC $100; $50/month GP; 31 days | cash; days | same two-payment pattern counted differently | subscription | [M*] | `money-model.md` § Payback period: worked examples |
| CAC $20; $8/month GP; −$20, −$12, −$4, +$4 at day 90; 75 to 90 days (q75), 60 to 90 days (q76) | cash; days | slow lemonade stand; by the day figures payback comes at the day-90 payment | illustrative | [M*] | `money-model.md` § Payback period: worked examples |
| CAC $1; $10 paid on day 7 ($8 GP); $7 left; 7 new customers on day 8; $56 GP on day 14; $225+ by day 60 (q75 only); 7 days | cash; days | fast, CFA-optimised lemonade stand | illustrative | [M*] | `money-model.md` § Payback period: worked examples |
| $15/month; $5 fulfilment; $10 GP; 10 months; LTGP $100; CAC $30; −$20; 3 months | cash; months | payback before the upsell fix | subscription | [M*] | `money-model.md` § Payback period: worked examples |
| $100 upsell at 100% margin; 1 in 5; $20 average; 30-day GP $30; 30 days | cash; days | upsell fix; checks; reaches Level 2, not Level 3 | subscription | [M*] | `money-model.md` § Payback period: worked examples |

---

## Diagnostics and pulling cash forward

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| more than 3x; within 3x | CAC against the industry average | above: advertising or sales; within: work LTGP; needs a published industry CAC | general | [M*] | `money-model.md` § Diagnostic: CAC against 3x the industry average; `operating-the-model.md` § What to change first: the 3x industry CAC test |
| industry $300; yours $600 (2x) with LTGP $500 (under 1:1); yours $1,200 (4x) | CAC | worked 3x test: LTGP bottleneck against broken targeting or closing | general | [M*] | `money-model.md` § Diagnostic: CAC against 3x the industry average |
| top 0.1%; 11x | advertisers; creatives | split-testing volume of the best advertisers; unsourced as given; layer one holds it too | general | [M*] | `money-model.md` § Diagnostic: high CAC, advertising or sales; `layer-two-sweep.md` § q103 numbers held in other files: where to find them |
| 20% margin; 20% rise; $100 and $20 to $120 and $40 | price; profit | raising prices doubles profit at 20% margins; checks | general | [M*] | `money-model.md` § Diagnostic: low LTGP, the seven levers |
| 80%+ | gross margin | target for services and digital offers | general | [M*] | `money-model.md` § Diagnostic: low LTGP, the seven levers; `layer-two-sweep.md` § q103 numbers held in other files: where to find them |
| "six primary levers"; seven listed | count | q76 introduces six and lists seven; all seven kept | general | [M*] | `money-model.md` § Diagnostic: low LTGP, the seven levers |
| 60, 90 or 180+ days | payback | payback that locks capital | general | [M*] | `money-model.md` § Diagnostic: slow payback, five ways to pull cash forward |
| 10% to 20%; 3, 6 or 12 months | discount; prepay term | prepay discounts | general | [M*] | `money-model.md` § Diagnostic: slow payback, five ways to pull cash forward |
| 1/3 or 50% | deposit | layaway or upfront deposit before delivery | general | [M*] | `money-model.md` § Diagnostic: slow payback, five ways to pull cash forward |
| every 4 weeks (13 cycles); bi-weekly | billing | billing cadence to pull cash forward | recurring services | [M*] | `money-model.md` § Diagnostic: slow payback, five ways to pull cash forward |

---

## Rollover and continuity multiples

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| at least 4x the credit; discount 25% or less; $500 deposit into a $2,000+ offer | multiple | rollover upsell price; same in q85, q86, q89 | general | [M*] | `money-model.md` § Money model ratios: rollover and continuity multiples; `upsell-and-downsell.md` § Rollover upsell: credit a past purchase toward a bigger one; `layer-two-sweep.md` § q103 numbers held in other files: where to find them |
| 1.33x → 50%; 2.33x → 80%; 2.66x → 90% (2.67 if from 2 2/3) | standalone price ÷ monthly; take rate | continuity take-rate pricing (q74); q94: "33% higher", against the first month; do not use as rules (L2.4 row 22) | general | [M*] | `money-model.md` § Money model ratios: rollover and continuity multiples; `continuity.md` § Continuity: standalone-to-continuity price multiples |
| $200/month; $466 ($200 x 2.33) | price | q74's worked 80% example | membership | [M*] | `money-model.md` § Money model ratios: rollover and continuity multiples |
| $399, $699, $799 against $199/month | price | the lane-18 worked figures: against $199 they are 2.0x, 3.5x, 4.0x; against $299 they fit (1.33x, 2.34x, 2.67x); do not fit the stated ratio (L2.4 row 22) | membership | [M*] | `continuity.md` § Continuity: standalone-to-continuity price multiples; `money-model.md` § Money model ratios: rollover and continuity multiples |

---

## Money model examples

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| $600 deposit; 6 weeks; 100% back | deposit; time | microgym win-your-money-back challenge (q73); q101 gives $500 down; layer one $500; both kept | gym | [M*] | `money-model.md` § Money model example: the microgym |
| $50/month off a $200/month 12-month membership; nets $150/month; $50 x 12 = $600 | credit | microgym rollover; matches the $600 deposit | gym | [M*] | `money-model.md` § Money model example: the microgym; `attraction-offers.md` § Win Your Money Back: prices and conditions |
| buy 4 months, get 2 free; 6-month supply | months | dog food attraction offer; fewer free than paid, against q79's more-free rule | e-commerce | [M*] | `money-model.md` § Money model example: dog food |
| free DIY against $16,000 | price | Gym Launch decoy | Gym Launch | [M*] | `money-model.md` § Money model example: Gym Launch |
| $42,000/year ($36,000 prepaid) | price | Gym Launch classic upsell (Gym Lords) | Gym Launch | [M*] | `money-model.md` § Money model example: Gym Launch |
| $10,000 down, rest over 52 weeks ($800/week) | payment plan | Gym Launch downsell; $42,000 − $10,000 over 52 weeks is about $615/week, not $800; $800 x 52 = $41,600 before the $10,000 down | Gym Launch | [M*] | `money-model.md` § Money model example: Gym Launch |
| $800/week; $300/week ads; $200/week sales training; $100/week tech support or license | price | Gym Launch menu close plus feature downsell; a ladder by feature, not a three-tier menu | Gym Launch | [M*] | `money-model.md` § Money model example: Gym Launch |
| zero to $476,000 per month in 3 months | revenue | Gym Launch with the decoy offer (q79); his claim, no record | Gym Launch | [M*] | `money-model.md` § Money model example: Gym Launch |
| $297 up front | price | newsletter lifetime rate | info product | [M*] | `money-model.md` § Money model example: the newsletter; `attraction-offers.md` § Pay Less Now or Pay More Later: prices |

---

## Win Your Money Back and giveaways

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| 28 days to 6 weeks | time | goal window in the examples | general | [M*] | `attraction-offers.md` § Win Your Money Back: structure |
| 20 lbs or 10% of body weight (q79); 20 lbs or 5% body fat in 6 weeks (q82) | result | results-based criteria; both kept | gym | [M*] | `attraction-offers.md` § Win Your Money Back: structure |
| $500 or $600, 6 weeks (q79); $600, 6 weeks (q73); $500 or $300, 6 weeks (q82); $500 down, 6 weeks (q101); $500, 8 weeks (q78) | deposit | gym challenge deposits; no deposit or length stated as the rule | gym | [M*] | `attraction-offers.md` § Win Your Money Back: prices and conditions |
| $400 (q78); free, "$0 deposit option" (q82); 28 days | deposit | 28-day blueprint | gym | [M*] | `attraction-offers.md` § Win Your Money Back: prices and conditions |
| $500; 5 days | deposit | B2B lead challenge (q78) | B2B | [M*] | `attraction-offers.md` § Win Your Money Back: prices and conditions |
| $500 to $1,000; $500 with 100 outbound messages a day; 100% back | deposit | consulting version and its conditions (q82) | B2B | [M*] | `attraction-offers.md` § Win Your Money Back: prices and conditions |
| under 5% | refund rate | prerequisite before running it (q78) | general | [M*] | `attraction-offers.md` § Win Your Money Back: prerequisite and results |
| over $1 billion (q78, q79); $1.5 billion across 45,000+ gyms over 7 years (q79) | sales; revenue | total from the offer; "45,000+" is likely a transcription error: layer one has 4,000+ gyms and Capstone Partners (grade A) 4,500+ | Gym Launch | [M*] | `attraction-offers.md` § Win Your Money Back: prerequisite and results |
| 78% to 80%; 2/3; about 10% | share | reach the goal; completers who convert to long-term memberships; ask for cash rather than rollover | Gym Launch | [M*] | `attraction-offers.md` § Win Your Money Back: prerequisite and results |
| $300,000/month to $1.5 million/month | revenue | Gym Launch scaled with rollover upsells and payment plans | Gym Launch | [M*] | `attraction-offers.md` § Win Your Money Back: prerequisite and results |
| $500 initial cash plus $200 to $300 in supplements within 48 hours | cash | ad costs liquidated up front | gym | [M*] | `attraction-offers.md` § Win Your Money Back: prerequisite and results |
| 2 of 4,000 | refunds | early gym unconditional guarantee; confirmed in layer one `[D]` | gym | [D] | `attraction-offers.md` § Win Your Money Back: prerequisite and results |
| 1,000,000 miles | distance | Volvo's free-new-car offer, third party | general | [M*] | `attraction-offers.md` § Win Your Money Back: prerequisite and results |
| 3 to 7 days; 1 winner; within 7 days; 7-day claim deadline | time; count | giveaway countdown, public winner, private offer and deadline | local service | [M*] | `attraction-offers.md` § Giveaways: structure |
| 10% to 30% "off gross margins" | discount | the giveaway scholarship, gift card or voucher only (q79); q103 made it a cap on all promotional discounts (L2.3) | local service | [M*] | `attraction-offers.md` § Giveaways: structure; `layer-two-sweep.md` § Discount cap: 10% to 30%, a scoped rule made general |
| $6,000 and $2,000; $1,000 for one year and $300; $12,000 16-week and $6,000; $5,000 value ($2,000 retail) and $1,800; $50,000 | prize; offer to the rest | dentist; dog food; consulting; another; gym (no offer given) | local service | [M*] | `attraction-offers.md` § Giveaways: prizes, vouchers and results |

---

## Decoy, buy X get Y free, pay less now

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| $0, $1, $5, $6 or $21; free 21-day; $5 VIP tanning; $6 six-week stress release | price | decoy prices | local service | [M*] | `attraction-offers.md` § Decoy offer: prices and The Economist menu |
| $399 6-week intensive; $299 or $399 (q82, gym); $100/month; $16,000 against free DIY | price | premium options beside the decoy | local service; Gym Launch | [M*] | `attraction-offers.md` § Decoy offer: prices and The Economist menu |
| 70% to 80% | take rate | prospects who take the $399 premium over the $5 decoy (q78 ties it to tanning, q79 states it generally); basic decoy against premium | local service | [M*] | `attraction-offers.md` § Decoy offer: prices and The Economist menu; `upsell-and-downsell.md` § Upsell take rates and presentation benchmarks |
| $59 digital; $125 print only (decoy); $125 digital plus print | price a year | The Economist decoy menu, Ariely's study, not his business | magazine | [D] | `attraction-offers.md` § Decoy offer: prices and The Economist menu; `upsell-and-downsell.md` § Decoy menu: The Economist, $59, $125, $125 |
| buy 1 get 2 over buy 2 get 1; buy 6 months get 12 over buy 12 get 6 | ratio | the more-free rule (q79 only) | general | [M*] | `attraction-offers.md` § Buy X Get Y Free: structure and the more-free rule |
| $200 a pair; buy 1 for $600, get 2 free; $200 average | price | Boot Factory, Nashville; a $600 transaction, not $200 | retail | [M*] | `attraction-offers.md` § Buy X Get Y Free: prices and results |
| buy 6 months get 6 free for $1,800 ($150/month); buy 6 get 12 free for $1,800 (q79) or buy 12 get 6 free for $1,800 (q82) | price | service agreement; q82's form is the one q79 says loses; both kept | service | [M*] | `attraction-offers.md` § Buy X Get Y Free: prices and results; `attraction-offers.md` § Buy X Get Y Free: structure and the more-free rule |
| buy 1 for $30 get 2 free (against 3 for $10); buy 1 for $20 get 2 free (against 33% off) | price | T-shirts | retail | [M*] | `attraction-offers.md` § Buy X Get Y Free: prices and results |
| 12 to 18 months | prepaid term | customers locked in instead of month to month; no conversion numbers | service | [M*] | `attraction-offers.md` § Buy X Get Y Free: prices and results |
| buy 12 get 6, buy 6 get 6, buy 6 get 12, all $1,800 | price | q106's three-version menu; 12 and 6 paid months cannot both cost $1,800; do not use (L2.4 row 21) | service | [M*] | `attraction-offers.md` § Buy X Get Y Free: prices and results; `first-customers-layer-two.md` § Layer two on tiers; `upsell-and-downsell.md` § Tiers: no good, better, best menu in layer two |
| 24 hours, 14 days or 30 days; 20% to 50%; under 10% | billing delay; discount; cancellations | pay-later window; pay-now discount; the cancellation ceiling (the sweep: most cancellations or refunds on conditional offers before it signals over-promising) | general | [M*] | `attraction-offers.md` § Pay Less Now or Pay More Later: structure; `layer-two-sweep.md` § q103 numbers held in other files: where to find them |
| $0 down, $297 tomorrow; $97 today (67% off) | price | speed reading course; $97 is 32.7% of $297, so 67.3% off | info product | [M*] | `attraction-offers.md` § Pay Less Now or Pay More Later: prices |
| $0 now, $149 in 14 days; $97 today plus an accessory | price | clothing | e-commerce | [M*] | `attraction-offers.md` § Pay Less Now or Pay More Later: prices |
| $600 after service; $369 today; $199/month upsell | price | lawn care pay later, pay now and recurring maintenance (q82) | local service | [M*] | `attraction-offers.md` § Pay Less Now or Pay More Later: prices |

---

## Free, premium and discount promotions

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| 90% off | discount | "going out of business" as a reason why | general | [M*] | `attraction-offers.md` § Promotions: free, premium and discount are wrappers |
| "five to 10 times higher"; "at least five to 10 times higher" | lead cost; price | a premium offer's lead cost, and the price it needs to match free | paid ads | [D] | `attraction-offers.md` § Free promotion: the penny gap and the split test |
| 1 cent against free; about 9x | demand | the penny gap (Ariely, as he cites it) | general | [M*] | `attraction-offers.md` § Free promotion: the penny gap and the split test |
| 10 gym markets; 5x to 10x (q80), "5x or more" (q78) | lead cost cut | his split test of free front ends; close rates and ticket virtually identical; no record | gym | [M*] | `attraction-offers.md` § Free promotion: the penny gap and the split test |
| $1,000: 500 leads (250 qualified, 250 not) against 200 (160 qualified, 40 not) | leads | free money math; free wins on qualified count; assumes ad spend | paid ads | [M*] | `attraction-offers.md` § Free promotion: the penny gap and the split test |
| 3x to 5x; about 10% | price; volume | premium promotion against cheaper models (q78 only) | high-ticket | [M*] | `attraction-offers.md` § Premium promotion |
| $100 with $50 profit against $10,000 with $9,500; 190 sales against 1; 190 prospects at 5% = 9.5 sales; $90,250; 9.5x; under 10 clients against 190 | cash; count | premium math; checks | high-ticket | [M*] | `attraction-offers.md` § Premium promotion |
| $50,000 burger; $10,000 package against a $100 course | price | premium illustrations, not his businesses | general | [M*] | `attraction-offers.md` § Premium promotion |
| 50% or more; 5% to 25% | discount | a deep discount on one sliver; marginal discounts rarely change behaviour | local service | [M*] | `attraction-offers.md` § Discount promotion: structure and four ways to show it |
| 87% off; $181 off, normally $210; $29 | discount; price | Ultimate Lemonade Bundle; $210 − $181 = $29 is 86.2% off, not 87% | local service | [M*] | `attraction-offers.md` § Discount promotion: structure and four ways to show it |
| 50%+ | discount | seasonal retail clearances | retail | [M*] | `attraction-offers.md` § Discount promotion: structure and four ways to show it |

---

## Two-step sale, presentations, freemium, pick your price

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| $19; $2,100 10-week | price | heavy metals test, then the detox plan; q82 attaches the $2,100 to physical therapy | health clinic | [D] | `attraction-offers.md` § Two-step sale: the $19 diagnostic; `first-customers-layer-two.md` § Layer two on audits: free diagnostic, not a product |
| 85% to 90%+; 90%+ (q80 only) | attendance; upsell | paid appointments attended; attendees upsold | local service | [M*] | `attraction-offers.md` § Two-step sale: the $19 diagnostic |
| $19 or $29 | price | introductory consultations or cleanings at chiropractors, dentists, gyms | local service | [M*] | `attraction-offers.md` § Two-step sale: the $19 diagnostic |
| about 0.9% | ratio | $19 against $2,100; Pass 1's arithmetic, not his rule | health clinic | [M*] | `attraction-offers.md` § Two-step sale: the $19 diagnostic |
| 20 feet; 2 miles | runway | "the bigger the plane, the longer the runway" | general | [M*] | `attraction-offers.md` § Free presentations: why they work |
| 15 minutes to 3 days | length | free presentations | general | [M*] | `attraction-offers.md` § Free presentations: why they work |
| 60 to 90 minutes; 25%; 33% of those; 100 → 25 → 8 | close rate | free dinner presentation; 33% of 25 is 8.25 | local seminar | [M*] | `attraction-offers.md` § Free presentations: formats and close rates; `upsell-and-downsell.md` § Upsell take rates and presentation benchmarks |
| 90 minutes; 10% | close rate | free masterclass, live attendees on the call | online coaching | [M*] | `attraction-offers.md` § Free presentations: formats and close rates; `upsell-and-downsell.md` § Upsell take rates and presentation benchmarks |
| 4 days of 60 to 90 minutes, pitch on day 5; 2% to 5% of signups | close rate | free 5-day challenge; the upsell file gives 10% of attendees on pitch day | online coaching | [M*] | `attraction-offers.md` § Free presentations: formats and close rates; `upsell-and-downsell.md` § Upsell take rates and presentation benchmarks |
| 3 days; pitch on days 2 and 3; 10% | close rate | free virtual summit, final-day attendees | online coaching | [M*] | `attraction-offers.md` § Free presentations: formats and close rates |
| 15 to 60 minutes; 25% | close rate | free strategy call, those who take the second call | general | [M*] | `attraction-offers.md` § Free presentations: formats and close rates; `upsell-and-downsell.md` § Upsell take rates and presentation benchmarks |
| $2,000 after a 60-minute webinar | price | third-party software pitch | software | [M*] | `attraction-offers.md` § Free presentations: formats and close rates |
| 1% to 5%; close to 100% | conversion; margin | freemium free-to-paid (q78 only); incremental gross margin needed | software | [M*] | `attraction-offers.md` § Freemium: criteria and the warning |
| $0.05/month | cost per free user | the freemium warning | software | [M*] | `attraction-offers.md` § Freemium: criteria and the warning; `operating-the-model.md` § Warning: freemium without capital |
| free 21-day; most pay $99 (1-on-1 call); $199 (handbook); $499 (10-lb guarantee; q106 adds "or full service credit") | price rungs | weight-loss pick your price | coaching | [D] | `attraction-offers.md` § Free Pick Your Price: every rung; `first-customers-layer-two.md` § Layer two on tiers; `upsell-and-downsell.md` § Tiers: no good, better, best menu in layer two |
| free; $30+ hand wax; $67+ buff; $99+ interior | price rungs | car wash pick your price | local service | [D] | `attraction-offers.md` § Free Pick Your Price: every rung; `upsell-and-downsell.md` § Tiers: no good, better, best menu in layer two |
| free cup; $5+; $25+; $99+ three months | price rungs | lemonade pick your price | illustrative | [M*] | `attraction-offers.md` § Free Pick Your Price: every rung |
| free cleaning; $99 or $299 | price rungs | dentist | local service | [M*] | `attraction-offers.md` § Free Pick Your Price: every rung |
| free group; $299 video course; $997 6 group calls | price rungs | coaching | coaching | [M*] | `attraction-offers.md` § Free Pick Your Price: every rung |
| $149 to $299 | price range | art gallery; most pay past the midpoint | retail | [M*] | `attraction-offers.md` § Free Pick Your Price: every rung |
| "3-tier"; $0, $99, $199, $499 | count | q81 calls it three tiers; its example has four price points | coaching | [M*] | `attraction-offers.md` § Free Pick Your Price: structure and pitch |

---

## Lifetime discount, setup fee and the $1 trial

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| $400/month at 50% off for life, $200/month | price | founding-member lifetime discount; the only 50% figure in layer two, and it is for life, not a first period | local service | [D] | `attraction-offers.md` § Lifetime discount and founding member offers; `continuity.md` § Lifetime discount: price protection and the founding member; `first-customers-layer-two.md` § Layer two on half-price starts |
| $39 to $19/month for life ($20 off) | price | software early access or beta testers | software | [M*] | `attraction-offers.md` § Lifetime discount and founding member offers; `continuity.md` § Lifetime discount: price protection and the founding member |
| $19.99 to $14.99/month for life | price | supplement flavour tester | e-commerce | [M*] | `attraction-offers.md` § Lifetime discount and founding member offers; `continuity.md` § Lifetime discount: price protection and the founding member |
| $100 initiation fee; dues $18 to $10 for life; or $100 waived for 1 year | price | "John the Tanning King" buy-down | local service | [M*] | `attraction-offers.md` § Lifetime discount and founding member offers; `continuity.md` § Lifetime discount: price protection and the founding member |
| month 4 | drop-off month | the earned lifetime discount: stay past it to earn the rate | general | [M*] | `attraction-offers.md` § Lifetime discount and founding member offers; `continuity.md` § Lifetime discount: price protection and the founding member |
| 14-day trial; 500 trials; 400 billed on day 15 (80%); 400+ members on day 1; profitable in month 1; $200 from $400 | count; rate | "The Opener", a mentor's franchise; a claim with no named business | gym or tanning | [M*] | `attraction-offers.md` § Lifetime discount and founding member offers; `continuity.md` § Lifetime discount: price protection and the founding member |
| $14.99/month for life | price | the uncapped lifetime-rate warning | subscription | [M*] | `attraction-offers.md` § Lifetime discount and founding member offers; `continuity.md` § Lifetime discount: price protection and the founding member; `operating-the-model.md` § Warning: fixed lifetime discounts with no cap |
| $399/month or $200/month lifetime | price | q95's blend of the newsletter and the local service; the $200 belongs to the local service | mixed | [M*] | `continuity.md` § Lifetime discount: price protection and the founding member |
| 95% off; $1,900 off; first month $100; $1,900 setup fee; $2,000 collected | price | recurring service discount plus setup fee | recurring service | [D] | `attraction-offers.md` § Discount plus setup fee: both worked cases; `continuity.md` § Discount plus one-time fee: the setup fee collects the cash; `first-customers-layer-two.md` § Layer two on half-price starts |
| $1,000/month (q104); $2,000/month (q92) | price | the recurring price after month 1; the audio says only "straight into recurring"; both are the answers' figures (L2.4 row 18) | recurring service | [M*] | `attraction-offers.md` § Discount plus setup fee: both worked cases; `continuity.md` § Discount plus one-time fee: the setup fee collects the cash |
| $3,000 12-week; 88% off; $120 first month; $1,000 setup fee; $1,120 month 1; $1,000 each after | price | program discount plus setup fee; $880 off a $1,000 month; total collected $1,120 + $2,000 = $3,120, not the stated $3,000; q95 misstates it as $120/month + $1,000 fee | program | [D] | `attraction-offers.md` § Discount plus setup fee: both worked cases; `continuity.md` § Discount plus one-time fee: the setup fee collects the cash; `first-customers-layer-two.md` § Layer two on half-price starts |
| $100 sign-up on a $10 month; $19 down on a $19 month | fee | "the higher the one-time start fee, the lower the churn"; his tanning-salon mentor | tanning salon | [D] | `attraction-offers.md` § Discount plus setup fee: both worked cases; `continuity.md` § Discount plus one-time fee: the setup fee collects the cash |
| $5,000 startup + $267/month; about 4 months to over 2 years (24+ months) | fee; lifespan | online weight-loss coaching; buyer self-selection not discussed; owner not stated | coaching | [M*] | `continuity.md` § Discount plus one-time fee: the setup fee collects the cash |
| $1 | first month | charged instead of free so a card is on file before month two | subscription | [D] | `attraction-offers.md` § $1 trial: charge a dollar, not zero; `upsell-and-downsell.md` § Trial with penalty: structure and the $1 first month; `first-customers-layer-two.md` § Layer two on half-price starts |

---

## Free with alternative revenue

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| $5/month for 1 year; $300/month supplements (q78) or $400/month (q82); 200+ clinics | price | weight-loss clinic paired offer; "grew 200+ clinics", unnamed business | clinic | [M*] | `attraction-offers.md` § Free with alternative revenue stream |
| $300 x 80% x 80% = $192 | gross profit per free offer | 80% take rate at 80% margin; q78's $300 fits, q82's $400 does not; q85 calls it "net profit", it is gross and ignores the free item's cost | general | [M*] | `attraction-offers.md` § Free with alternative revenue stream; `upsell-and-downsell.md` § Free with alternative revenue: the numbers |
| $30 lock (q85 only); 4 free sessions (q87 only); $200+ orthotics | price; count | storage and physical therapy examples | local service | [M*] | `upsell-and-downsell.md` § Upsell offer: free with alternative revenue stream |
| $7.95 shipping; $27 audiobook; $97 templates; $297 course; $497 financing course | price | real estate free-book sequence | info product | [M*] | `upsell-and-downsell.md` § Upsell offer: free with alternative revenue stream |
| $99 at 30% = 30 buyers = $2,970; free at 100%, 80% x $300 = 80 buyers = $24,000 | revenue per 100 prospects | paid model against free model | general | [M*] | `upsell-and-downsell.md` § Free with alternative revenue: the numbers |
| $200/month; nearly 100% (q87), 100% (q89); 50% more; $300 to $400 | price; rate | No Sale Sale: orientation bookings, supplement spend against members | gym | [M*] | `upsell-and-downsell.md` § Free with alternative revenue: the numbers |
| $5/month (normally $100/month); 95% and 5%; "$300+" (q95) | price; share | 200+ clinic chain: products against medical revenue; q95's $300+ possibly borrowed from the unit math | clinic | [M*] | `upsell-and-downsell.md` § Free with alternative revenue: the numbers |

---

## Front ends for services, agencies and local businesses

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| $1,000 challenge free with $200/month | price | free bribe script | gym | [M*] | `first-customers-layer-two.md` § Service front ends: salty pretzel, sealant, free bribe |
| 4 times a year; about 98% | frequency; margin | internal mini-programs for existing customers | general | [M*] | `first-customers-layer-two.md` § Service front ends: salty pretzel, sealant, free bribe |
| 3 coats | count | free wood sealant: first coat free, coats 2 and 3 sold | home services | [M*] | `first-customers-layer-two.md` § Service front ends: salty pretzel, sealant, free bribe |
| $1,000 down plus $1,000/month | price | the commodity agency retainer that drives comparison and churn | agency | [M*] | `first-customers-layer-two.md` § Consulting and agency front ends |
| $4,000 setup; 20 people in month 1 or next month free | price; guarantee | pay-per-show script | agency | [M*] | `first-customers-layer-two.md` § Consulting and agency front ends |
| $750/hour; 6 months | price; term | agency-to-consulting hybrid | agency | [M*] | `first-customers-layer-two.md` § Consulting and agency front ends |
| 4 months; 21-day launch | free window | free agency window; the 4 months has no worked example, the only case is Gym Launch's 21 days | agency | [M*] | `first-customers-layer-two.md` § Consulting and agency front ends |
| $300 to $500/month; $450/month | price | local SMB Google Maps or review management; website-as-a-service | agency | [M*] | `first-customers-layer-two.md` § Consulting and agency front ends |
| $0; $0 plus about $16 to $17 shipping; $1,000 stack with a 2-hour consultation | price | $100M Scaling Roadmap; free real estate book; book stack | consulting | [M*] | `first-customers-layer-two.md` § Consulting and agency front ends |
| 3 to 5 hours | free help | 1-on-1 consulting to a result, then pitch (q83) | consulting | [M*] | `first-customers-layer-two.md` § Consulting and agency front ends |
| 3-hour workshop; $0 or $29 to $99; 100% to the gym owner; 1 to 2 free adjustments | price; share | chiropractor gym workshop and new-member packets | local service | [M*] | `first-customers-layer-two.md` § Local business plays: hyper-local, partners, affiliates |
| $1,500 to $2,000 off | discount | dentists' kids' braces | local service | [M*] | `first-customers-layer-two.md` § Local business plays: hyper-local, partners, affiliates |
| 100 owners; 3 massages for $500; $30 a massage ($90); CAC $90 | count; price; cost | massage therapist affiliate package; $90 CAC holds only if every package converts; no rate given | local service | [M*] | `first-customers-layer-two.md` § Local business plays: hyper-local, partners, affiliates |

---

## First avatar

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| 5% to 7%; $100,000/month and $40,000/year at 10% = $4,000/year; $10,000,000/month and $4,000,000/month ($48M/year) at 10% = $4,000,000/year | conversion; value; fee | sales page designer example; units mixed: a 40% lift on $100,000/month is $40,000 a month, not a year, and 10% of $48M is $4.8M, not $4M; the ~100x point survives | general | [M*] | `first-customers-layer-two.md` § First avatar: picking the first customer type |
| bottom 80% replaced by the top 20%; "80/20, 5x growth" (sweep) | share | Vista's rule applied to the customer base | general | [M*] | `first-customers-layer-two.md` § First avatar: the four-step survey method; `layer-two-sweep.md` § q103 numbers held in other files: where to find them |
| top 20%; 3 to 5 | share; count | spenders to study; common qualifiers to find | general | [M*] | `first-customers-layer-two.md` § First avatar: the four-step survey method |
| 25 to 45; 1+ employees; $10,000+/month; at least 30 members; $1M+ gym | profile | Gym Launch top-20% avatar | Gym Launch | [M*] | `first-customers-layer-two.md` § First avatar: the Gym Launch case |
| 78%; two long-form pieces | share; count | top customers who consumed two pieces before buying; made a booking rule | Gym Launch | [M*] | `first-customers-layer-two.md` § First avatar: the Gym Launch case |
| $6,000 to $8,000 to over $45,000 | lifetime GP | industry average against his after the avatar change; his figures, no record | Gym Launch | [M*] | `first-customers-layer-two.md` § First avatar: the Gym Launch case |
| 70x | profit | the competitor serving "anyone with a pulse and a credit card", on the same monthly sales; competitor unnamed | Gym Launch | [M*] | `first-customers-layer-two.md` § First avatar: the Gym Launch case; `operating-the-model.md` § Warning: the expensive customer problem, 70x lower profit |

---

## Audits, free work and the free five

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| 1 hour; $25; $250+; $0; 1 in 4; $25 x 4 = $100 | labour; value; CAC | free audit economics, same as layer one; profitable if the core margin exceeds $100 | service | [M*] | `first-customers-layer-two.md` § Layer two on audits: free diagnostic, not a product |
| 3% per second | conversions lost | website load time; unsourced | general | [M*] | `first-customers-layer-two.md` § Layer two on audits: free diagnostic, not a product |
| 5, "The Exact Number" (q107); "Rule of First 5" (q82) | free clients | question-shaped; his Leads part 3 audio: the number "matters less than knowing why" | general | [D] | `first-customers-layer-two.md` § Layer two on free work and the free five |
| 1 to 5 free; 6 to 10 80% off; 11 to 15 60%; 16 to 20 40%; 21 to 25 20%; 26 on full retail | price by client count | the step-up ladder (q107 and q108 agree); matched to Leads part 3 in layer one | new offer | [D] | `first-customers-layer-two.md` § Layer two on free work and the free five; `layer-two-sweep.md` § Price rise: the 5-to-5-to-5 rule, 20% after every 5 sales |
| +20% every 5 sales | price rise | until demand softens or conversion drops; "5-to-5-to-5" is q103's name | new offer | [D] | `first-customers-layer-two.md` § Layer two on free work and the free five; `layer-two-sweep.md` § Price rise: the 5-to-5-to-5 rule, 20% after every 5 sales |
| a year | free training | his workout clients, for donations or testimonials; his claim | his businesses | [M*] | `first-customers-layer-two.md` § Layer two on free work and the free five |
| $0 upfront; 21-day launch; 33 gyms; 18 months | turnarounds | Gym Launch original model; matches layer one `[D]` | Gym Launch | [D] | `first-customers-layer-two.md` § Layer two on free work and the free five; `hormozi-record-layer-two.md` § Record: the free turnarounds, 33 gyms in 18 months |
| 213 members; $112,000 | result | free case-study video title, a small gym in San Diego (q82) | gym | [M*] | `first-customers-layer-two.md` § Layer two on free work and the free five |

---

## No-ad-budget models and referrals

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| 100 a day for 100 days; never below 100 cold attempts | actions | Rule of 100 | no ad budget | [M*] | `first-customers-layer-two.md` § Layer two on no-ad-budget models; `layer-two-sweep.md` § Rule of 100: the forms q103 gives |
| 100 minutes of content; $100/day ads; 100 warm messages; 100 cold outreaches; 100 days | daily input; time | q103's forms; 100 days is the least time to run a channel before judging it | general | [M*] | `layer-two-sweep.md` § Rule of 100: the forms q103 gives; `first-customers-layer-two.md` § Layer two on no-ad-budget models |
| 300 fliers; 0 leads; 1 complaint call; 150,000 | fliers | his flier test against his mentor's; layer one: one call, the mentor ran 5,000 a day for 30 days | his businesses | [M*] | `first-customers-layer-two.md` § Layer two on no-ad-budget models; `hormozi-record-layer-two.md` § Record: first gym, 2013 |
| 100 → 20 (20%) → 4 (20%) → 1; 500 a week = 5 customers; $400 offer; $2,000/week = $104,000/year | funnel; revenue | warm outreach with zero ad spend; 100 → 1 is 1%; 4 → 1 is the free audit's 1 in 4 | no ad budget | [M*] | `first-customers-layer-two.md` § Layer two on no-ad-budget models |
| 1% to 3% | engaged leads | cold contacts that become engaged leads, not customers | general | [M*] | `first-customers-layer-two.md` § Layer two on no-ad-budget models |
| 1 → 2 → 4 → 8 | customers | referrals as exponential growth against linear outreach | general | [M*] | `first-customers-layer-two.md` § Layer two on no-ad-budget models |
| 25% to 30% | sign-ups | added as referrals by asking at checkout | general | [M*] | `first-customers-layer-two.md` § Layer two on no-ad-budget models |
| 3 direct text introductions | count | the bargaining chip for any discount | general | [M*] | `first-customers-layer-two.md` § Layer two on no-ad-budget models; `upsell-and-downsell.md` § Barter downsell: $100 off for reviews and introductions |
| up to max CAC | incentive | two-sided referral reward, split | general | [M*] | `first-customers-layer-two.md` § Layer two on no-ad-budget models |
| "$700/week"; 2 customers a week; $10,000/year or $200/month over 4 years; 100 customers; $1M a year | projection | do not use (L2.4 row 24): $200 x 48 = $9,600; "$700/week" unexplained; $10,000 a year and $10,000 over 4 years cannot both hold; 2 a week reaches 100 in about 50 weeks | high-ticket | [M*] | `first-customers-layer-two.md` § Layer two on no-ad-budget models; `layer-two-sweep.md` § $1 million as 100 clients at $10,000 |
| 100 at $10,000 against 10,000 at $100 | customers | $1M is easier high-ticket (q103 gives $10,000 per client in total) | general | [M*] | `layer-two-sweep.md` § $1 million as 100 clients at $10,000 |

---

## Upsells

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| $2 burger, $0.25; fries +$0.75, $1.00, 4x; meal +$1.75, $2.75, 11x; supersize $1, +$0.25, $3.00, "11.6x" | profit | burger progression; $3.00 / $0.25 is 12x, not 11.6x; 3 to 4 sequential upsells | fast food | [M*] | `upsell-and-downsell.md` § Classic upsell numbers: the burger profit progression |
| 5% to 50%; 10%; 30% | price add-on; take rate | guarantee or insurance upsell; art studio replacement guarantee bought by 30% | general | [M*] | `upsell-and-downsell.md` § Classic upsell: "You can't have X without Y" |
| $30 | price | fur coat ear muffs | retail | [M*] | `upsell-and-downsell.md` § Classic upsell: "You can't have X without Y" |
| 20 consecutive; $5,000 to $10,000 in a day | sales | supplement menu upsell; his gym, unchecked | gym | [M*] | `upsell-and-downsell.md` § Menu upsell: unsell, prescribe, A/B, card on file; `hormozi-record-layer-two.md` § Record: other own-business claims in the offer chapters |
| five to 10 times | anchor ÷ core | the anchor upsell | general | [D] | `upsell-and-downsell.md` § Anchor upsell: premium first at 5x to 10x the core; `first-customers-layer-two.md` § Layer two on tiers |
| $1,000 offer to a $100 budget; $100 offer to a $1,000 budget | price | q85's anchor rule | general | [M*] | `upsell-and-downsell.md` § Anchor upsell: premium first at 5x to 10x the core |
| $500 budget; $16,000 suit; $2,200 bought; 4.4x budget; 7.3x anchor | price; ratio | his suit purchase | his businesses | [M*] | `upsell-and-downsell.md` § Anchor upsell: premium first at 5x to 10x the core; `hormozi-record-layer-two.md` § Record: other own-business claims in the offer chapters |
| $1,000/week against $200/week; 5x; 20-year insurance | price | landscaping anchor (q85) | local service | [M*] | `upsell-and-downsell.md` § Anchor upsell: premium first at 5x to 10x the core |
| $199/month against $19/month; 10.5x; 24-hour early access | price | newsletter anchor; above the stated 10x ceiling | info product | [M*] | `upsell-and-downsell.md` § Anchor upsell: premium first at 5x to 10x the core; `first-customers-layer-two.md` § Layer two on tiers |
| $1,000 against $200; 5x; 20-year against 1-year insurance | price | art studio (q85) or physical product (q106); q85 also gives the pair as landscaping; the answers disagree on the business | retail | [M*] | `upsell-and-downsell.md` § Anchor upsell: premium first at 5x to 10x the core; `first-customers-layer-two.md` § Layer two on tiers |
| $600 deposit; $50/month off $200/month for 12 months; $150/month; $1,800/year | price | gym challenge rollover; the same figures appear as a continuity discount in q92 and q93, likely one example | gym | [M*] | `upsell-and-downsell.md` § Rollover upsell: credit a past purchase toward a bigger one; `continuity.md` § Moving a customer into continuity: the numbers |
| $200 gift card for $20 (90% off); $1,000+ (5x) | price | gift card rollover | general | [M*] | `upsell-and-downsell.md` § Rollover upsell: credit a past purchase toward a bigger one |
| $200 cleaning; "$1,000+" (q85) against "$2,100" whitening (q89) | price | dental rollover; both satisfy the 4x rule | local service | [M*] | `upsell-and-downsell.md` § Rollover upsell: credit a past purchase toward a bigger one |
| 200 past clients; 6+ months inactive; $4,000 credit; 20%; $1.9 million a year (q89: "ARR"); 1 day | count; revenue | win-back by personal video; 20% of 200 is 40, so $47,500 a year each; whose program is not stated | high-ticket | [M*] | `upsell-and-downsell.md` § Rollover upsell: the win-back, 200 past clients and $1.9 million; `hormozi-record-layer-two.md` § Record: other own-business claims in the offer chapters |
| 9 asks; one bundle | count | "make one ask and get nine sales" | general | [M*] | `upsell-and-downsell.md` § Upsell price relative to the first purchase, and how many to make |
| 80% to 90%+; over 90% (q87) | take rate | frictionless alternative-revenue product upsells at orientation | gym | [M*] | `upsell-and-downsell.md` § Upsell take rates and presentation benchmarks |
| 75% (3 of 4) | take rate | free trial upgraded with an A/B close | gym | [M*] | `upsell-and-downsell.md` § Upsell take rates and presentation benchmarks |

---

## Value grid and the offer stack

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| 10 prospects; 8 take a $75 trial; 3 convert; $600; $75 a client; $60 a prospect; $600 to $1,000 of labour | count; revenue | value grid #1; $600 is 8 x $75, the trial revenue alone, so the 3 conversions add nothing to the total | local service | [M*] | `upsell-and-downsell.md` § Value grid #1: the simple trial model, $75 a client |
| $75 to $1,763; "over 23x" (23.5x) | revenue per client | value grid #2; no front-end, downsell or path figures survive | local service | [M*] | `upsell-and-downsell.md` § Value grid #2: the offer-stacked model, $1,763 a client |
| 6 to 12 weeks; half down; quarter down; 24 to 72 hours; 3-month and 1-month supply; 12-pack, 8-pack, bi-weekly; 2 to 3 weeks | time; terms | the 4-sale weight-loss sequence | coaching | [M*] | `upsell-and-downsell.md` § Offer stack example: the 4-sale weight-loss sequence |

---

## Downsells

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| $15 total; $10 prepaid | price | prepay discount against an interest-inclusive anchor (q89 step 1) | general | [M*] | `upsell-and-downsell.md` § Payment plan downsell: the step-down sequence |
| half down; 1/3 down, 1/3 on each of the next two paychecks | split | payment-plan steps | general | [M*] | `upsell-and-downsell.md` § Payment plan downsell: the step-down sequence |
| up to a third (33%) | payments | declined or failed payments recouped by a payment-plan process (q91); "declined" may mean offers or cards | general | [M*] | `upsell-and-downsell.md` § Payment plan downsell: the step-down sequence |
| half down today, half on the 2nd | split | his first sale | his businesses | [M*] | `upsell-and-downsell.md` § Payment plan downsell: the step-down sequence; `hormozi-record-layer-two.md` § Record: other own-business claims in the offer chapters |
| $16,000 16-week; $10,000 down over 52 weeks; $800/week for 52 weeks | price | Gym Launch "downsell"; $800 x 52 = $41,600, far above $16,000, so it is the $42,000 back end, not a downsell | Gym Launch | [M*] | `upsell-and-downsell.md` § Payment plan downsell: the step-down sequence; `hormozi-record-layer-two.md` § Record: Gym Launch prices and the back end |
| $25,000; $9,000 down; 3 instalments ($3,000 each) | price | layaway for high-ticket coaching | high-ticket | [M*] | `upsell-and-downsell.md` § Layaway: fulfilment waits for the threshold |
| $25,000 to $30,000/year or $2,500 to $3,000/month; $9,000 down; 2 getaways a year | price | "Couplepreneurs Accelerator", probably the same layaway example; owner not stated | high-ticket | [M*] | `upsell-and-downsell.md` § Layaway: fulfilment waits for the threshold; `continuity.md` § Service business continuity: delivery rules |
| after two failed downsells; 8 to 10; 7 or below | score | 1-to-10 temperature check: money or structure against fit | general | [M*] | `upsell-and-downsell.md` § 1-to-10 temperature check after two failed downsells |
| $50 per missed action | penalty | chunked trial penalty | general | [M*] | `upsell-and-downsell.md` § Trial with penalty: structure and the $1 first month |
| $500 onboarding + $99/month; three 60-minute calls; $500 penalty | price | HR software trial with penalty | software | [M*] | `upsell-and-downsell.md` § Trial with penalty: structure and the $1 first month |
| 28 days; 5 days; 100 messages a day | terms | fitness and B2B trial penalties; no penalty amounts given | gym; B2B | [M*] | `upsell-and-downsell.md` § Trial with penalty: structure and the $1 first month |
| 3 of 10; 4 of 10; 3 of those 4; 3 to 6 of 10 (q89); another 3 to 4, "6 or 7" of 10 (q91) | close | trial with penalty after an upfront-cash refusal; q91's 7 counts all 4 trial takers, not the 3 that convert | gym | [M*] | `upsell-and-downsell.md` § Trial with penalty: script and conversion numbers |
| 3-month to 1-month; 4 sessions a month to 2 | quantity | feature downsell by quantity | general | [M*] | `upsell-and-downsell.md` § Feature downsell: the five sub-types |
| $3,000 paint job; $19 home massage tools | price | DFY to DIY: painter (spray machine rate not given); chiropractor | local service | [M*] | `upsell-and-downsell.md` § Feature downsell: the five sub-types |
| 25% to 75%; 100 calls; 35 (up from 25) with guarantee; 40 without; $400 cheaper | close | guarantee removal; 35 + 40 = 75 checks; whose business is not stated | high-ticket | [M*] | `upsell-and-downsell.md` § Feature downsell: removing the guarantee, 25% to 75% close |
| $100 off; reviews, video, 3 public posts, 2 friends (q89); 3 friends (q90); 3 introductions (q108) | discount; asks | barter downsell; possibly two examples | general | [M*] | `upsell-and-downsell.md` § Barter downsell: $100 off for reviews and introductions |
| about half (50%) | take rate | free-orientation attendees who buy the DIY or alternative product; not the No Sale Sale's "50% more spend" | gym | [M*] | `upsell-and-downsell.md` § No prospect left behind: the free orientation after every no |

---

## Continuity offers

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| $800 toys with $59/month food | value; price | pet food continuity bonus | e-commerce | [M*] | `continuity.md` § Continuity bonus offer: advertise the bonus, not the membership |
| $1,000 accelerator with $100/month | value; price | service continuity bonus | service | [M*] | `continuity.md` § Continuity bonus offer: advertise the bonus, not the membership |
| 40 past newsletters; $15,880; $399/month; $397 an issue | value; price | digital continuity bonus | info product | [M*] | `continuity.md` § Continuity bonus offer: advertise the bonus, not the membership |
| $100/month; challenge sales 34 to 15; straight to continuity 17 to 40; 8 of 40 (20%) prepaid 6 months; 50% (17 of 34); 40 of 100 leads (q96 only) | count | microgym case; called "tripling", but 17 to 40 is 2.35x | gym | [M*] | `continuity.md` § Continuity bonus offer: advertise the bonus, not the membership; `continuity.md` § Moving a customer into continuity: the numbers |
| 3 months free on 1 year at $200/month = $600; $50/month off; $150/month | price | continuity discount spread over time | general | [M*] | `continuity.md` § Continuity discount offer: five delivery structures |
| 1 year free for 5 years; 15% off after 5 months; after about 3 payments | terms | trash removal; rice company; gift card redemption | general | [M*] | `continuity.md` § Continuity discount offer: five delivery structures |
| equal to the discount ($600) | cancellation fee | breaking a continuity-discount commitment early | general | [M*] | `continuity.md` § Continuity discount offer: five delivery structures |
| $1,000/month; $5,000 setup; $6,000 down; 12 months; $5,000 owed | price | waived fee worked example; the example is exactly 5x | B2B | [M*] | `continuity.md` § Waived fee offer: leaving costs more than staying |
| below 5% | early cancellations | what the waived fee keeps | B2B | [M*] | `continuity.md` § Waived fee offer: leaving costs more than staying |
| 1.5x to 5x (q92, q93); 3x to 5x (q94) | setup fee ÷ monthly | waived fee size; two readings, unchecked | B2B | [M*] | `continuity.md` § Waived fee offer: leaving costs more than staying |
| 4 months; 1 module; every 3,000 miles or 6 months; 3, 6, 12 months; every 14 days or quarterly | trigger | lifetime upgrades: tenure unlock, referral bonus, car lease service, status milestones, bonus schedule (q102) | general | [M*] | `continuity.md` § Lifetime upgrades: a "When" paired with a "What"; `layer-two-sweep.md` § Framework map: where each named item sits in the two books |
| buy 5 months, get 1 free; 1 of 8 (12.5%); +50% | take rate; 30-day GP | bulk prepay upsell; q92 says profits, q86 and q96 gross profit; the 50% depends on unstated margins | general | [M*] | `continuity.md` § Bulk prepay upsell: buy 5 months, get 1 free |

---

## Billing, churn and cancellation

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| 10.7%; 5.0%; 2.0% | monthly cancellation | monthly, quarterly, annual billing across 14,000 businesses; unnamed dataset; not the 158-gym survey's 10.7% | subscription | [M*] | `continuity.md` § Churn: billing cadence, 10.7%, 5%, 2% |
| 13 cycles against 12; +8.3%; +41% on a 20% net margin | billing; revenue; profit | 4-week billing; 13/12 = 1.083 and (20 + 8.3) / 20 = 1.415 check | general | [M*] | `continuity.md` § Billing: every 4 weeks, 13 cycles a year |
| 3% | fee | waived for a backup ACH method; q103: about 3% pure profit to net income | US | [M*] | `continuity.md` § Billing: backup payment method and the 3% fee |
| $120,000 a year; $4,000/month; $700 to $1,000/month | profit; price | pricing to the worst month; the figure set is in q94 only and not in the audio (L2.3); layer one: $3,500/month, competitors $800 to $1,200 keeping clients 36 to 40 months | B2B | [M*] | `continuity.md` § Churn: price a recurring offer to the client's worst month |
| "only using 20%" | usage | the feature-bloat complaint | general | [M*] | `continuity.md` § Churn: feature bloat and the first 48 hours |
| 24 to 48 hours (q94); 48 hours (q103) | onboarding window | small promises kept at once | general | [M*] | `continuity.md` § Churn: feature bloat and the first 48 hours; `layer-two-sweep.md` § q103 numbers held in other files: where to find them |
| 14 days | first cash win | onboarding KPI | service | [M*] | `layer-two-sweep.md` § Onboarding KPI: the 14-day initial cash win |
| 1/3 to 1/2 (33% to 50%) | saved | cancelling clients saved by routine exit interviews | recurring services | [M*] | `continuity.md` § Cancellation: the save sequence and the exit interview |

---

## Moving into continuity and Gym Launch continuity

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| week 3 or 4 of 6 (q96); 2 to 3 weeks after the start (q88) | timing | when to pitch continuity; never the last day | gym | [M*] | `continuity.md` § Moving a customer into continuity: when |
| $500 credit | credit | rollover credit script, against the $600 deposit elsewhere; likely a different example | local health service | [M*] | `continuity.md` § Moving a customer into continuity: the scripts |
| 2/3 (about 66%) | take rate | challenge signups who roll the deposit into a 1-year membership (q96 only) | gym | [M*] | `continuity.md` § Moving a customer into continuity: the numbers |
| $16,000 once; $42,000/year for 3 years; $3,200/month (q95: or $800/week); every 14 days | price; cadence | Gym Launch continuity back end; $3,200 x 12 = $38,400, $42,000 / 12 = $3,500, $800 x 52 = $41,600 (L2.4 row 19); layer one's matched $3,500 | Gym Launch | [M*] | `continuity.md` § Gym Launch continuity: from $16,000 once to $42,000 a year |
| $300,000/month to $4,000,000/month; "more than 13x" (13.3x) | revenue | after adding the back end; q92 calls it revenue, q93 recurring revenue; no outside record | Gym Launch | [M*] | `continuity.md` § Gym Launch continuity: from $16,000 once to $42,000 a year; `hormozi-record-layer-two.md` § Record: Gym Launch revenue, profit and dates |

---

## Service business continuity

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| $1,500 to $3,000/month; "$450/week" (q95, about $1,950/month); 4 to 6 months | price; stick | the SMB dead zone | agency | [M*] | `continuity.md` § Service business continuity: the dead zone and the two paths |
| "$400/month or less" (q94); under $400 to $500 ($299 to $400) and $299 to $450 (q95) | price | path (a), low-ticket automated services | agency | [M*] | `continuity.md` § Service business continuity: the dead zone and the two paths |
| 30 to 40 months (q94); 29 to 40 and 29 to 38 (q95) | stick | path (a) | agency | [M*] | `continuity.md` § Service business continuity: the dead zone and the two paths |
| $25,000+/year | price | path (b), upmarket high ticket | agency | [M*] | `continuity.md` § Service business continuity: the dead zone and the two paths |
| $300 to $400; $10,000+ | price | layer one's down-market and up-market version | agency | [M*] | `continuity.md` § Service business continuity: the dead zone and the two paths |
| quarterly; 2 a year | cadence | strategy calls; live getaways | high-ticket | [M*] | `continuity.md` § Service business continuity: delivery rules |
| $400 to $500 ceiling; $1,500 floor | price | the gap layer two does not cover | agency | [A] | `continuity.md` § Agencies and retainers: what the sources do not hold; `first-customers-layer-two.md` § Not covered: enterprise pilots, legal terms, technical audits, retainers |

---

## Hiring, managing and growth

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| $2M profit; $0 against $10M+ | value | the same business with and without the owner; $10M+ implies 5x profit or more, no multiple stated | general | [M*] | `operating-the-model.md` § Owning versus making: a $2M profit business worth $0 or $10M+ |
| 10 to 1; 1 of 4; 40 interviews per hire | screening | the 40-to-1 bottleneck; company not named | frontline hiring | [M*] | `operating-the-model.md` § Hiring: the 40-to-1 screening bottleneck and group interviews |
| 40 hours for 4; 36 saved; 200 hours for 20; 4 hours for the founder | hours a week | management time math; the 10% ratio is implied | team | [M*] | `operating-the-model.md` § Management time math: 40 hours of work for 4 hours of managing |
| 30 to 45 minutes | weekly one-on-one | management cadence | team | [M*] | `operating-the-model.md` § Management cadence: daily huddles and the weekly one-on-one |
| 30 to 60 minutes; 10 to 20 chunks a day; 5 to 60 minutes | blocks | the manager's schedule | general | [M*] | `operating-the-model.md` § Maker versus manager: the manager's schedule |
| half or full day; 1 to 2 chunks a day; 10 to 14 a week | blocks | the maker's schedule; 1 to 2 a day gives 10 to 14 only over 7 days (5 to 10 over 5) | general | [M*] | `operating-the-model.md` § Maker versus manager: the maker's schedule |
| 45 minutes; 6 months | time | "solving is the work": stuck time, a book's structure | general | [M*] | `operating-the-model.md` § Maker versus manager: the maker's schedule |
| 10x; 10:00 am into 2 hours and 1.5 hours; 2:00 pm | cost; time | a 30-minute meeting's cost to a maker; the split morning; the open loop | general | [M*] | `operating-the-model.md` § Maker versus manager: what a meeting costs a maker |
| first 4 to 6 hours; after 1:00 pm; Mondays | time | his maker and manager hours; layer one says 4 | his businesses | [M*] | `operating-the-model.md` § Maker versus manager: his own calendar |
| 8 | functions | changes needed per growth stage | general | [M*] | `operating-the-model.md` § Growth stages: the eight business functions |
| 0 employees, first 5 customers; 1 to 4 employees; 25%+ from referrals; $100M+ | level markers | the seven levels; 25%+ is the only referral-share threshold in layer two | general | [M*] | `operating-the-model.md` § Growth: the seven levels of advertising and organisation |
| $1M; 20% margin; $200,000; 100% of profit; 6 hours a day; 1 to 3 employees | cash; time | the Swamp's A-player choice; the seven levels give 1 to 4 for first staffing | $1M to $3M | [M*] | `operating-the-model.md` § The Swamp: $1M to $3M with 1 to 3 employees |
| $1,000,000 | revenue | 1-1-1 rule until $1M (q103); the seven levels make it a level-1 focus only | general | [M*] | `layer-two-sweep.md` § 1-1-1 rule to $1 million |

---

## Warnings he illustrates with figures

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| $42,000/year (about $800/week) to about $31,000/year ($600/week); $100,000/month overhead; churn unchanged; revenue −25%; $5,000,000 a year; a third of net income | price; profit | his GymLords price cut; $600 x 52 = $31,200; a third at $5M implies about $15M net; q101 calls the $5M a "Claim / Calculation" | Gym Launch | [M*] | `operating-the-model.md` § Warning: lowering price to cut churn |
| $250,000; $30,000 glass wall; first gym about $30,000 (q100) or $34,000 (q101); "8x worse" (q100), "8x as much" (q101) | cost | ego spending; $250,000 ÷ $34,000 is about 7.35x, ÷ $30,000 about 8.33x; layer one gives $34,000 (L2.4 row 23) | gym | [M*] | `operating-the-model.md` § Warning: ego spending on fulfilment |
| $5,000 down to $400 | price | car insurance add-on discounted until trust was gone | car dealership | [M*] | `operating-the-model.md` § Warning: discounting the same product, the car insurance example |
| $1,500/month at 10:1, $13,500 profit; $15,000/month at 4:1, $45,000; $31,500 missed | ad spend; profit | ROAS over profit (q100); the sums check | gym | [M*] | `operating-the-model.md` § Warning: ROAS percentage over profit dollars |
| 13:1 to 10:1 | ROAS | q101's telling: he stopped ads when ROAS dropped; layer one has 10:1 or 13:1 on $1,500/month | gym | [M*] | `operating-the-model.md` § Warning: ROAS percentage over profit dollars |
| 40 to 50 members; 3,500 sq. ft.; sessions halved; one-third lost | count; share | changing a product customers love (q101 only for the one-third) | gym | [M*] | `operating-the-model.md` § Warning: changing a product customers love |

---

## Sweep rules of thumb

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| 10:1; $10,000 for $1,000 | value ÷ price | the minimum perceived value; probably $100M Offers | general | [M*] | `layer-two-sweep.md` § Value-to-price ratio: 10:1 |
| 3.5:1 or about 70/30; 10:1 over-give (q74) | gives ÷ asks | give-to-ask; 3.5:1 is about 78/22 and 70/30 about 2.33:1, so the two forms disagree | content | [M*] | `layer-two-sweep.md` § Give-to-ask content ratio: 3.5:1 or 70/30 |
| 70/20/10 | effort or budget | core, variations, moonshots | general | [M*] | `layer-two-sweep.md` § Effort allocation: 70/20/10 |
| 70% brand; 30% direct response | ad budget | possibly merged with the give-to-ask 70/30; check before use | paid ads | [M*] | `layer-two-sweep.md` § Ad budget split: 70% brand, 30% direct response |
| square root of headcount; 50%; 10 of 100 | output | Price's Law, not his | team | [M*] | `layer-two-sweep.md` § Square root law of team productivity |
| 60 seconds to 5 minutes; 391% (about 4x to 5x) | response time; conversion lift | speed to lead; 391% is 4.91x the base | inbound leads | [M*] | `layer-two-sweep.md` § Speed to lead: 60 seconds to 5 minutes, 391% |
| 3 to 6 months (90 to 180 days) | wait | before re-contacting an unresponsive list | cold lists | [M*] | `layer-two-sweep.md` § Re-contacting a cold list: wait 3 to 6 months |
| 2x 30-day cash; 1x with no leads | ad spend | ad test budget and kill point | paid ads | [M*] | `layer-two-sweep.md` § Ad test budget: 2x 30-day cash, kill at 1x |
| about 70 | active leads per rep | outbound lead cap; no other home in either layer | outbound team | [M*] | `layer-two-sweep.md` § Lead cap: about 70 active leads per outbound rep |

---

## His record: first gym and the gym prices

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| 2013; age 23 to 24; $50,000 saved; $10,000 mastermind; $34,000 build; $6,000 left; $4,972 rent | cash | the first gym, Huntington Beach; $50,000 − $10,000 − $34,000 = $6,000 checks | his businesses | [M*] | `hormozi-record-layer-two.md` § Record: first gym, 2013 |
| $1,000 Facebook ads; $5,700; 19 members at $299 | cash | first ad campaign; 19 x $299 = $5,681, not $5,700 | his businesses | [M*] | `hormozi-record-layer-two.md` § Record: first gym, 2013 |
| $4,972 first-month cash; $100,000+ first year; 5 to 6 locations over 3 years; sold 2016 | cash; count | first-gym growth; a first month equal to the rent is worth checking against the audio | his businesses | [M*] | `hormozi-record-layer-two.md` § Record: first gym, 2013 |
| 15% to about 80% | share | first-challenge clients hitting goal, before and after simpler plans | his businesses | [M*] | `hormozi-record-layer-two.md` § Record: first gym, 2013 |
| $99 to $299/month; $299 to $500 down (q73: $600 deposit) | price | boot camp membership; 6-week challenge | his businesses | [M*] | `hormozi-record-layer-two.md` § Record: the gym prices he charged |
| $4,000/month for 10 hours a week | price | high-ticket personal training | his businesses | [M*] | `hormozi-record-layer-two.md` § Record: the gym prices he charged |
| $200 to $300 | supplements per customer | sold at onboarding | his businesses | [M*] | `hormozi-record-layer-two.md` § Record: the gym prices he charged |
| $300 for 6 sessions; 30 members; $9,000 | price; revenue | "Big Booty Boot Camp"; 30 x $300 = $9,000 checks | his businesses | [M*] | `hormozi-record-layer-two.md` § Record: the gym prices he charged |

---

## His record: Launch and Go, Gym Launch, Prestige Labs, ALAN, net worth

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| 50/50; $45,700 (also "all funds", $46,000); 4 years of savings; "2016/2017" | cash | the launch-and-go partner fraud | his businesses | [M*] | `hormozi-record-layer-two.md` § Record: Launch and Go, the partner fraud and the refund crisis |
| $150,000; 2 gym launches; March 2017 | refunds | the refund crisis; half-price offerer open (Pass 2 §4 row 11) | Gym Launch | [M*] | `hormozi-record-layer-two.md` § Record: Launch and Go, the partner fraud and the refund crisis |
| 33 gyms; 18 months; 21 days (q101: "21 to 30 days"); $42,000 average; 100% of revenue; 8 gyms a month at peak | count; cash | free turnarounds; 33, 18, 21 days, $42,000 matched `[D]` in layer one; no outside record (ledger L9) | Gym Launch | [D] | `hormozi-record-layer-two.md` § Record: the free turnarounds, 33 gyms in 18 months |
| $16,000 16-week | price | front-end licensing | Gym Launch | [M*] | `hormozi-record-layer-two.md` § Record: Gym Launch prices and the back end |
| $6,000, $8,000 and $10,000; May 2017 | price | relaunch phone sales; citation numbers unlike the rest, may be cross-wired | Gym Launch | [M*] | `hormozi-record-layer-two.md` § Record: Gym Launch prices and the back end |
| $42,000/year ($3,200/month or $36,000 prepaid); $800/week (q106); $126,000 over 3 years | price | GymLords back end; $3,200 x 12 = $38,400, $800 x 52 = $41,600, $126,000 ÷ 3 = $42,000 fits; layer one's matched figure is $3,500/month | Gym Launch | [M*] | `hormozi-record-layer-two.md` § Record: Gym Launch prices and the back end |
| $3,300/day | credit card run | during the launch | Gym Launch | [M*] | `hormozi-record-layer-two.md` § Record: Gym Launch revenue, profit and dates |
| 2017: $6,820,000; 2018: $25.9 million revenue, $17 million take-home | revenue; profit | the answer labels the $17M "First Year Gym Launch Profit (2018)" beside 2017 revenue, so "first year" is wrong or means first full year | Gym Launch | [M*] | `hormozi-record-layer-two.md` § Record: Gym Launch revenue, profit and dates |
| $300,000/month to $4 million/month | revenue | growth tied to the $42,000 back end, "more than 13x" | Gym Launch | [M*] | `hormozi-record-layer-two.md` § Record: Gym Launch revenue, profit and dates |
| $42 million over 4 years; 66% stake; American Pacific Group; 2021; $46.2 million valuation | cash; share | owner distributions and the exit; the exit is on an IMAP/Capstone record, the $46M and 66% on blogs (ledger L2) | his businesses | [M*] | `hormozi-record-layer-two.md` § Record: Gym Launch revenue, profit and dates; `hormozi-record-layer-two.md` § Record: Prestige Labs, supplements from 2018 |
| $100,117 January 2017; $215,000 May to June 2017 | cash; profit | relaunch first month; licensing first-month profit; "from my processing records"; date conflict with the May 2017 phone sales, possibly two launches | Gym Launch | [M*] | `hormozi-record-layer-two.md` § Record: Gym Launch revenue, profit and dates |
| $30,000 in 30 days; $239,000/year topline; $160,000/year recurring | client results | average client gym; differs from the $42,000 in 21 days (different programs); "per month" or "per year" for $239,000 open (Pass 2 §2) | Gym Launch | [M*] | `hormozi-record-layer-two.md` § Record: Gym Launch revenue, profit and dates |
| 2018; $200 average order; 30% discount; 40% commission | price; share | Prestige Labs affiliate model; 70 points of price out in discount and commission combined, worth checking | his businesses | [M*] | `hormozi-record-layer-two.md` § Record: Prestige Labs, supplements from 2018 |
| $1 million software; $3 million inventory | investment | Prestige Labs | his businesses | [M*] | `hormozi-record-layer-two.md` § Record: Prestige Labs, supplements from 2018 |
| $1.5 million/month | revenue | Prestige Labs by the end of year 1 | his businesses | [M*] | `hormozi-record-layer-two.md` § Record: Prestige Labs, supplements from 2018 |
| first 3 weeks $150,000; 5-year break-even pace; week 4 | sales | the slow start before affiliate launch training | his businesses | [M*] | `hormozi-record-layer-two.md` § Record: Prestige Labs, supplements from 2018 |
| "$450,000+ in a single week"; $429k, $383k, $411k, $452k | weekly revenue | after the training; only the last week tops $450,000; ledger L14, no record | his businesses | [M*] | `hormozi-record-layer-two.md` § Record: Prestige Labs, supplements from 2018; `hormozi-record-layer-two.md` § Said against done: layer-two ledger additions (Pass 2 L2.5) |
| 2019; $1.2 million/month by end of year 1; 75% sold in 2021; $12 million trailing revenue | revenue; share | ALAN / LNS; $1.2M a month is $14.4M a year, above the $12M trailing at sale: revenue fell or year 1 was a peak month | his businesses | [M*] | `hormozi-record-layer-two.md` § Record: ALAN / LNS, software from 2019 |
| $100 million at 31, 2021 | net worth | his claim | his businesses | [M*] | `hormozi-record-layer-two.md` § Record: net worth and personal income |
| over $1.2 million a month | profit | peak personal income during Gym Launch; ledger L14, no record | his businesses | [M*] | `hormozi-record-layer-two.md` § Record: net worth and personal income; `hormozi-record-layer-two.md` § Said against done: layer-two ledger additions (Pass 2 L2.5) |
| $250 million+ | annual revenue | Acquisition.com portfolio combined | his businesses | [M*] | `hormozi-record-layer-two.md` § Record: net worth and personal income |
| $100,000 | first deposit | when he felt richest | his businesses | [M*] | `hormozi-record-layer-two.md` § Record: net worth and personal income |
