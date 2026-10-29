---
type: corpus
aliases: ["Numbers Index"]
corpus: alex-hormozi
layer: retrieval
tags: [corpus, leads, machine, numbers, offers, pricing]
source: skills/corpus-ingestion
created: 2026-10-16
file: numbers-index
---

# Numbers Index

Every figure in the Alex Hormozi corpus that carries a rule or a claim, with its unit, what it
governs, the scale it was stated at, its provenance and its home. Grep the figure or the thing it
measures. Compiled from the eleven domain files in this folder, with `pass-2-reconciliation.md`
§2 to §4 applied where they override Pass 1. Named frameworks are indexed in
`frameworks-index.md`.

Rules this file obeys:

- Nothing is rounded or dropped. Ranges stay ranges. A figure given two ways keeps both.
- Where two answer files read the same figure differently, both readings sit in one row with the
  file each comes from.
- Where Pass 2 says a figure is his own rounding or his own arithmetic slip, the row says so. Where
  an answer's own sum does not add up, the row gives the real sum.
- A row marked `origin [A]` is one Pass 2 did not find in the transcribed audio; it may sit in an
  untranscribed Leads part or a YouTube video.

**Columns.** *Scale:* gym, agency, general or US, the scale the figure was stated at; a few rows
use info-product, local B2C, SMB or his businesses where none of the four fits. *Marker:* `[D]`
matched to his own audio (Pass 2 §2); `[M*]` NotebookLM's transcription and wording; `[A]` not in
the sources; `record` an outside source graded in Pass 2 §5. *Home:* file § heading, exact.

**Standing caution.** These are his figures and NotebookLM's renderings of them, not measured
results. About 40 sums in the answers do not add up (Pass 2 §4); the ones below are flagged where
they sit. A figure repeated across files is one retelling, not independent confirmation.

---

## Value equation and its drivers

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| 0 to 1 per driver; Meditation 1.5/4, Xanax 4/4 | score | Meditation against Xanax; scores are summed, not run through the division | general | [M*] | `value-equation.md` § Value equation: Meditation versus Xanax scoring |
| 15 minutes | time to effect | Xanax's time delay, scored 1 | general | [M*] | `value-equation.md` § Value equation: Meditation versus Xanax scoring |
| $123 billion; $62 billion | industry size | supplements (Grand View Research) against health clubs (IHRSA); q07 calls it "double"; no year | US | [M*] | `value-equation.md` § Value equation: supplements against health clubs |
| $200; $29/month | price | what people pay for supplements against the gym fee they hesitate at | US | [M*] | `value-equation.md` § Value equation: supplements against health clubs |
| "a few million"; "billions" | cost | London Underground arrival map against faster trains; imprecise in both files | general | [M*] | `value-equation.md` § Value equation: psychological solutions over logical ones |
| $300 to $1,500 (5x) | average ticket | photography company after removing friction; whose business is not given | general | [M*] | `value-equation.md` § Value equation: portfolio photography company result; `pricing-and-tiers.md` § Pricing case: photography business 5x ticket |
| $1,000/week to $38,000/week (38x) | weekly profit | same company; how 5x price became 38x profit is not said | general | [M*] | `value-equation.md` § Value equation: portfolio photography company result; `hormozi-record.md` § Results he reports for clients and others |
| almost $1,000,000 (q01); over $1,000,000 (q12 onward) | donations | same company, to children's charities; two readings | general | [M*] | `value-equation.md` § Value equation: portfolio photography company result; `pricing-and-tiers.md` § Pricing case: photography business 5x ticket |
| 40 yards | drive distance | golf club status script | general | [M*] | `value-equation.md` § Dream outcome: status and the viewpoint of others |
| 20 lbs in 6 weeks | dream outcome | the strong form, against "$99/month boot camp" | gym | [M*] | `value-equation.md` § Dream outcome: weak against strong examples; `offer-construction.md` § Offer creation: the full process in order |
| 10,000th against 1st | patient | surgeon test: track record raises perceived likelihood | general | [M*] | `value-equation.md` § Perceived likelihood: definition and the surgeon test; `closing-vetting-and-operating.md` § Trust: proof beats promise |
| 11 months; first $2,000 sale within 7 days | time; cash | Gym Launch: the long result took 11 months (q05), so clients got ads live and a first sale in 7 days | gym | [M*] | `value-equation.md` § Time delay: long-term outcome and short-term wins; `hormozi-record.md` § Gym Launch client results and the 158-gym survey |
| 12 to 24 months | time delay | body change in a weight-loss programme | general | [M*] | `value-equation.md` § Time delay: long-term outcome and short-term wins; `value-equation.md` § Effort and sacrifice: fitness against liposuction |
| 1 to 2 hours earlier; 5 to 10 hours per week | effort | what fitness costs the client | general | [M*] | `value-equation.md` § Effort and sacrifice: fitness against liposuction |
| $100/month; 1/10th or 1/100th | price | what fitness sellers "arm wrestle" for, against the surgery price | US | [M*] | `value-equation.md` § Effort and sacrifice: fitness against liposuction |
| $25,000 up front; 2 to 4 weeks | price; recovery | liposuction with tummy tuck, done in an afternoon | US | [M*] | `value-equation.md` § Effort and sacrifice: fitness against liposuction; `pricing-and-tiers.md` § Price examples: surgery, consulting days, a fundraiser |
| $100/month; $99/month; $29/month | price | three fitness prices for three products: boot camp (effort), boot camp (dream outcome), big-box gym; keep apart | gym, US | [M*] | `value-equation.md` § Effort and sacrifice: fitness against liposuction |
| $50 | fee | private MVD skip-the-line against the free DMV; the "fast beats free" line is `[D]`, the example is not | US | [M*] | `value-equation.md` § Time delay: fast beats free |
| 100 hours; 100 custom meal plans; 15 minutes per plan; 4,000+ gyms | build time; output; reuse | Excel macro sheet; whether "100 custom" means 100 variants is not said; reused by 4,000+ gyms (q34) | gym | [M*] | `value-equation.md` § Time delay and effort: techniques to cut them; `offer-construction.md` § Delivery vehicles: create flow, monetize flow, add friction; `bonuses-and-naming.md` § Bonus: what a bonus should be; `hormozi-record.md` § Weight-loss challenge: deposit, supplements, success rate and the stack |

---

## Market and niche

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| 2 AM | time | when bars close, one telling of the starving crowd (q09) | general | [M*] | `offer-construction.md` § Market: the starving crowd |
| "$100 or more" (q07, q09); "$100/roll" (q08) | price | COVID toilet paper; per roll or per pack unclear; origin `[A]` | US | [M*] | `offer-construction.md` § Market: the starving crowd |
| 25% a year | contraction | newspapers in the Lloyd story; nothing overcomes it; origin `[A]` | general | [M*] | `offer-construction.md` § Market: dying market, the Lloyd story; `guarantees.md` § Performance pricing case: Lloyd's newspaper revenue share; `guarantees.md` § Performance pricing: the risks; `closing-vetting-and-operating.md` § Service business: picking a niche and staying in it |
| "millions of dollars per month within 5 months" (q06, q07); "a multi-million dollar business in 5 months" (q08) | revenue | Lloyd's mask pivot; a monthly rate against a total size; origin `[A]` | general | [M*] | `offer-construction.md` § Market: dying market, the Lloyd story; `guarantees.md` § Performance pricing case: Lloyd's newspaper revenue share |
| 99.6% | share | of entrepreneurs (q06) or of businesses (q07, q08) under $10M a year, for whom a tight niche pays more; origin `[A]` | general | [M*] | `offer-construction.md` § Market: the $10 million rule and micro-niching |
| $10 million a year | revenue | stay niched below it | general | [M*] | `offer-construction.md` § Market: the $10 million rule and micro-niching |
| $10 million to $30+ million a year | revenue | where the TAM usually caps out; q08 "after crossing $10 million per year or when it exhausts its TAM"; q06, q07 tie it to the TAM only | general | [M*] | `offer-construction.md` § Market: the $10 million rule and micro-niching |
| 100 members, may be "at least 100" (q06); at least 30 members (q72) | gym size | Gym Launch qualifier, with a signed lease and at least 1 employee; two readings | gym | [M*] | `offer-construction.md` § Market: the $10 million rule and micro-niching; `closing-vetting-and-operating.md` § Vetting: qualifier scripts; `hormozi-record.md` § Gym Launch offer: programme sequence, guarantee, bonuses, scarcity |
| $19; $99; $499; $1,997 | course price | niche ladder: generic, sales professionals, outbound B2B reps, power tools and gardening reps; credited to Kennedy; $1,997/$19 = 105x, labelled "up to 100x"; origin `[A]` | info-product | [M*] | `pricing-and-tiers.md` § Niche price ladder: time management $19 to $1,997; `value-equation.md` § Dream outcome: weak against strong examples; `closing-vetting-and-operating.md` § Service business: picking a niche and staying in it |
| $19; $1,997 | programme price | generic weight loss against a programme for shift nurses | info-product | [M*] | `pricing-and-tiers.md` § Niche price ladder: time management $19 to $1,997; `value-equation.md` § Dream outcome: weak against strong examples |
| up to 100x | price multiple | niching's pricing power for the same deliverable (q12, q51); q03's "100x more" is value to the avatar | general | [M*] | `pricing-and-tiers.md` § Niche price ladder: time management $19 to $1,997; `offer-construction.md` § Offer creation: the full process in order; `closing-vetting-and-operating.md` § Service business: picking a niche and staying in it |
| $300 | fee | the resume service unemployed buyers could not pay (q72); q08 calls the builder "a consultant" | general | [M*] | `closing-vetting-and-operating.md` § Vetting: four market qualifications; `offer-construction.md` § Market: the four criteria |

---

## Offer construction and the stack

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| $10,000 for $100,000 | price against value | irresistible-price example; may be NotebookLM's illustration | general | [M*] | `offer-construction.md` § Offer: definition and the grand slam offer; `pricing-and-tiers.md` § Premium pricing: the 10x value-to-price gap |
| 10x ($100,000); 1/10th | price multiple | delivery test; $100,000 implies a $10,000 base, which neither answer states | general | [M*] | `offer-construction.md` § Delivery vehicles: the 10x and 1/10th test |
| 24/7; 9-to-5; 5 minutes; 1 hour; 24 hours | response speed | the delivery cube's speed lever | general | [M*] | `offer-construction.md` § Delivery vehicles: the delivery cube |
| $4,351 for $599 | stack value; price | "Total value $4,351, all for only $599"; the seven values he reads add to $4,347, his own sum is off by $4 (Pass 2 §4 row 5); 7.26x, q27 "more than 7x"; q13 calls it a 10x example, which it is not | gym | [D] | `offer-construction.md` § Weight-loss stack: every item and value; `bonuses-and-naming.md` § Bonus stack: the weight-loss offer, $4,351 for $599; `pricing-and-tiers.md` § Premium pricing: the 10x value-to-price gap; `hormozi-record.md` § Weight-loss challenge: deposit, supplements, success rate and the stack |
| $1,000; $600; $500; $699; $199; $1,000; $349 | item value | Bargain Grocery System; Ready in 5 Minute Cooking Guide; "Lick Your Fingers Good" Meal Plan; Fat Burning Workouts; Tone Up While You Travel Blueprint; Never Fall Off Accountability System; Live It Up While Slimming Down Eating Out System | gym | [D] | `offer-construction.md` § Weight-loss stack: every item and value; `bonuses-and-naming.md` § Bonus stack: the weight-loss offer, $4,351 for $599 |
| $2,400 to $5,200 | price | later longer-term versions of the same bundle | gym | [D] | `offer-construction.md` § Weight-loss stack: every item and value; `bonuses-and-naming.md` § Bonus stack: the weight-loss offer, $4,351 for $599 |
| $100s a month | savings | the grocery system's claim | gym | [M*] | `offer-construction.md` § Weight-loss stack: every item and value |

---

## Pricing and tiers

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| $500/month; $5,000 | competitor price | lowest and highest competitors to Gym Launch | gym, US | [D] | `pricing-and-tiers.md` § Pricing case: Gym Launch $16,000 intensive and the $42,000 upsell |
| $16,000; 16 weeks | price; term | Gym Launch DWY intensive, "three times the highest price player and 32 times more than the lowest"; $16,000/$5,000 = 3.2x; the 32x is his wording, a one-off fee against a monthly fee, not like for like (Pass 2 §4 row 1) | gym | [D] | `pricing-and-tiers.md` § Pricing case: Gym Launch $16,000 intensive and the $42,000 upsell; `hormozi-record.md` § Gym Launch pricing: $16,000 front end and the $42,000 back end |
| $18,000 | up-front price | a review blog's figure for Gym Launch (ledger L5, grade C); open | gym | record | `pricing-and-tiers.md` § Pricing case: Gym Launch $16,000 intensive and the $42,000 upsell; `hormozi-record.md` § Said against done: the ledger (Pass 2 §5) |
| 35% | upsell rate | to the 3-year back end; q16 "35% of graduating clients"; q17 "35% of clients upgraded" | gym | [D] | `pricing-and-tiers.md` § Pricing case: Gym Launch $16,000 intensive and the $42,000 upsell; `pricing-and-tiers.md` § Tiers: ascension and the tier-upgrade bonus; `hormozi-record.md` § Gym Launch pricing: $16,000 front end and the $42,000 back end |
| $42,000 a year; $3,500/month; $800/week; $126,000 | price | Gym Lords 3-year back end; q48's $800/week is $41,600; $126,000 over 3 years ("$126,000+ LTV") | gym | [D] for $42,000; [M*] rest | `pricing-and-tiers.md` § Pricing case: Gym Launch $16,000 intensive and the $42,000 upsell; `hormozi-record.md` § Gym Launch pricing: $16,000 front end and the $42,000 back end |
| $35,280 a year | income | average gym owner; other readings $29,500 to $35,280 (q60) and $30,000 to $36,000 (q49); clients committed half or more of it | gym, US | [D] for $35,280 | `pricing-and-tiers.md` § Pricing case: Gym Launch $16,000 intensive and the $42,000 upsell; `pricing-and-tiers.md` § Pricing case: $99 boot camp against $29 gym; `hormozi-record.md` § Gym Launch pricing: $16,000 front end and the $42,000 back end |
| 1,000 clients at $42,000/year | count; price | the event his father saw; implies $42M a year from that tier, set it against the 35% upsell rate | gym | [M*] | `pricing-and-tiers.md` § Pricing script: "If I made you $239,000 extra" |
| $239,000; $42,000; 17.6%; about 5.7:1 | gain; fee | ROI script and rule; the fee is 17.6% of the gain, under the 10x rule | gym | [M*] | `pricing-and-tiers.md` § Pricing script: "If I made you $239,000 extra"; `pricing-and-tiers.md` § Premium pricing: the 10x value-to-price gap |
| 10x; $100,000 for $10,000 | value-to-price | the target gap; raise price only after raising value | general | [M*] | `pricing-and-tiers.md` § Premium pricing: the 10x value-to-price gap |
| up to 100x | price over cost | charge up to 100x fulfilment cost, never more than worth | general | [M*] | `pricing-and-tiers.md` § Premium pricing: the 10x value-to-price gap |
| 100-hour weeks | hours | what copycat pricing leaves owners working | general | [M*] | `pricing-and-tiers.md` § Premium pricing: copycat pricing and the commodity trap |
| $1,000 down + $1,000/month | price | commodity agency retainer; readings: "$1,000 retainer" (q13), "$1,000/mo" (q15), "$1,000 down + $1,000/month" (q17, q20, q33) | agency | [M*] | `pricing-and-tiers.md` § Agency offer math: $10,000 ad spend, commodity against grand slam; `pricing-and-tiers.md` § Agency offer: the standard retainer is a commodity; `pricing-and-tiers.md` § Premium pricing: copycat pricing and the commodity trap |
| $1.2 million a month | personal profit | premium pricing "in his late 20s" (q12, q13) or "in his 20s" (q14); more than the CEOs of Ford, McDonald's, Motorola and Yahoo combined; no record | his businesses | [M*] | `pricing-and-tiers.md` § Pricing claim: $1.2 million a month personal profit; `hormozi-record.md` § Gym Launch revenue and profit |
| $99/month; $29/month | price | his boot camp refused against "You Fitness" (q35), "Gym B" (q32), Planet Fitness (q02, q03) | gym, US | [M*] | `pricing-and-tiers.md` § Pricing case: $99 boot camp against $29 gym; `hormozi-record.md` § First gym: savings, build cost and expansion |
| 20% of prospects; 5x to 10x | share; price multiple | fractal 80/20: one in five pays 5x to 10x for access, speed or DFY | general | [M*] | `pricing-and-tiers.md` § Tiers: 20% will pay 5x to 10x |
| 10 × $500 = $5,000; 2 × $5,000 = $10,000; 8 prospects | revenue | demand math; leaves 8 with pent-up demand; assumes 2 of 10 pay 10x, a premise | general | [M*] | `pricing-and-tiers.md` § Tiers: 20% will pay 5x to 10x; `scarcity-and-urgency.md` § Scarcity: fractal 80/20 demand math |
| $99 to $299 | software price | entry tier in q14's pyramid; appears nowhere else; the pyramid is question-shaped | general | [A] | `pricing-and-tiers.md` § Tiers: the three-tier pyramid is not his |
| $599 to $2,400 to $5,200; $19 up to $499 to $1,997 | price | q14's middle and entry tiers, assembled by NotebookLM from separate examples | general | [M*] | `pricing-and-tiers.md` § Tiers: the three-tier pyramid is not his |
| $50,000 a day | consulting fee | specialists on $10M+ problems, where the supply of solvers equals 1 | general | [M*] | `pricing-and-tiers.md` § Price examples: surgery, consulting days, a fundraiser; `scarcity-and-urgency.md` § Scarcity: the $50,000 consulting day; `value-equation.md` § Perceived likelihood: tools to raise it |
| $50,000 offered; $1 million a month; $1 million a week; over $50,000 a day | fee; revenue; profit | two entrepreneurs at $1M a month offered him $50,000 for a day while he did $1M a week; he refused, making over $50,000 a day in profit; Pass 2 §4 row 10: q68 turned the refused offer into a price | his businesses | [M*] | `pricing-and-tiers.md` § Price examples: surgery, consulting days, a fundraiser; `scarcity-and-urgency.md` § Scarcity: the $50,000 consulting day; `hormozi-record.md` § Gym Launch revenue and profit |
| $50,000 to $250,000 | offered day fee | DMs he regularly turns down | his businesses | [M*] | `hormozi-record.md` § Acquisition.com: the giving flywheel and the refused consulting days |
| $1,000,000 = 100 × $10,000, against 10,000 × $100; $200/month over 4 years | revenue | start high-touch; $200 × 48 = $9,600, not $10,000 | general | [M*] | `closing-vetting-and-operating.md` § Tiers: no three-tier menu, enter at the top |
| $120,000 | price | Tesla Model S, the enter-at-the-top example | US | [M*] | `closing-vetting-and-operating.md` § Tiers: no three-tier menu, enter at the top |
| $21 for 20 days; $99/month; $299/month; $500; $16,000; $3,997 / $4,000 | front-end price | q68's front-end list mixes his and competitors' ($21 for 20 days is the competitor offer he argues against) | gym, agency | [M*] | `closing-vetting-and-operating.md` § Tiers: no three-tier menu, enter at the top |

---

## Agency offer math (one $10,000 test)

Whose agency, and whether it was a real test or an illustration, is not stated. q48's general
multipliers are probably drawn from this one case.

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| $10,000; 300,000 impressions | ad spend | the same spend for both offers; only the offer changed | agency | [M*] | `pricing-and-tiers.md` § Agency offer math: $10,000 ad spend, commodity against grand slam; `closing-vetting-and-operating.md` § Offer as the main lever: the agency split test |
| $3,997 | one-time fee | grand slam: pay one time, performance guarantee, bundle of sales assets | agency | [M*] | `pricing-and-tiers.md` § Agency offer math: $10,000 ad spend, commodity against grand slam; `pricing-and-tiers.md` § Agency offer: the pay-for-performance script |
| 0.13% against 0.33% | response rate | 0.33/0.13 = 2.54, given as 2.5x | agency | [M*] | `pricing-and-tiers.md` § Agency offer math: $10,000 ad spend, commodity against grand slam; `bonuses-and-naming.md` § Enhancing: funnel metrics to watch |
| 40 against 100 | booked calls | q14 in the pricing file; q48 in the closing file | agency | [M*] | `pricing-and-tiers.md` § Agency offer math: $10,000 ad spend, commodity against grand slam; `closing-vetting-and-operating.md` § Offer as the main lever: the agency split test |
| 30 against 75 | shows | q48 only | agency | [M*] | `closing-vetting-and-operating.md` § Offer as the main lever: the agency split test |
| 5 against 28 | closes | | agency | [M*] | `pricing-and-tiers.md` § Agency offer math: $10,000 ad spend, commodity against grand slam |
| 16% against 37% (q33); 16.7% against 37.3% (q48, of shows); 12.5% against 28% (of booked calls) | close rate | three readings: 2.31x, 2.23x and 2.24x; q13 and q14 state 2.3x | agency | [M*] | `pricing-and-tiers.md` § Agency offer math: $10,000 ad spend, commodity against grand slam; `closing-vetting-and-operating.md` § Offer as the main lever: the agency split test |
| 2x to 3x (q32); 2.3x to 2.5x (q33) | close-rate lift | moving from a commodity to a grand slam offer; likely generalised from this case | agency | [M*] | `bonuses-and-naming.md` § Enhancing: funnel metrics to watch; `pricing-and-tiers.md` § Agency offer math: $10,000 ad spend, commodity against grand slam |
| $5,000 against $112,000 | cash up front | 28 × $3,997 = $111,916, given as $112,000 | agency | [M*] | `pricing-and-tiers.md` § Agency offer math: $10,000 ad spend, commodity against grand slam; `leads-content-ads-referrals.md` § Paid ads: his reported returns |
| 0.5:1 against 11.2:1 | ROAS | the commodity offer lost $5,000 up front | agency | [M*] | `pricing-and-tiers.md` § Agency offer math: $10,000 ad spend, commodity against grand slam; `leads-content-ads-referrals.md` § Paid ads: his reported returns |
| 22.4x | cash multiple | $112,000/$5,000 | agency | [M*] | `pricing-and-tiers.md` § Agency offer math: $10,000 ad spend, commodity against grand slam |
| 4x | price | q48's "price often 4x" | agency | [M*] | `closing-vetting-and-operating.md` § Offer as the main lever: the agency split test |

---

## Discounting, payment terms and price rises

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| every 4 weeks or so | cadence | "we change them every 4 weeks or so", the in-person urgency script | gym | [M*] | `pricing-and-tiers.md` § Discounting: promotional discount as the marketing hook; `scarcity-and-urgency.md` § Urgency script: fast-action bonus |
| $1,000 | bonus value | action-taker bonus "that normally costs $1,000" | general | [M*] | `pricing-and-tiers.md` § Discounting: promotional discount as the marketing hook; `scarcity-and-urgency.md` § Urgency script: fast-action bonus |
| 5 lbs | trigger | "We won't bill your second installment until you lose your first 5 lbs [or close your first sale]" | gym | [M*] | `pricing-and-tiers.md` § Discounting: add value, change terms, fence the offer; `guarantees.md` § Guarantee: conditional sub-types |
| Jan 30th; 5 spots | deadline; cap | "New Year special ends Jan 30th", "limited to 5 spots" | gym | [M*] | `pricing-and-tiers.md` § Discounting: add value, change terms, fence the offer; `scarcity-and-urgency.md` § Urgency script: rolling seasonal promotions |
| 100% of the time | eating out | the one-thing objection script | gym | [M*] | `pricing-and-tiers.md` § Discounting script: the bonus close |
| end of the week or month (q16); 2 weeks (q53, q61) | notice period | pipeline price-rise deadline; two readings | general | [M*] | `pricing-and-tiers.md` § Raising prices: clean the pipeline first; `scarcity-and-urgency.md` § Urgency: pricing deadline, the pipeline clean-out; `closing-vetting-and-operating.md` § Raising prices: anchoring and the pipeline notice |
| 25 clients max; 10% to 20% | capacity; expansion | capacity cap (q16) and periodic expansion; 25 may be NotebookLM's | agency | [M*] | `pricing-and-tiers.md` § Raising prices: capacity cap and account squeeze; `scarcity-and-urgency.md` § Scarcity script: total business cap, 25 clients |
| $38.95; 37 tools | price; count | the "but wait, there's more" knife; knife and stack `[D]` (Offers p6), the 37 only in q29 | general, US | [D] | `pricing-and-tiers.md` § Anchoring: what the sources hold; `bonuses-and-naming.md` § Bonus: why bonuses work, "but wait, there's more" |
| 50% or more; 10% | discount size | threshold to change behaviour; 10% rarely does (q66, q71) | general | [M*] | `free-work-trials-and-first-customers.md` § Half-price start and discounted first period; `leads-content-ads-referrals.md` § Sweep: numbers q66 gives as rules |
| $100 off for 3 referrals or reviews | discount | q71's example; itself a discount traded for terms | general | [M*] | `free-work-trials-and-first-customers.md` § Half-price start and discounted first period |
| 3 friends | introductions | 3-way text in exchange for a cut initiation fee | gym | [M*] | `free-work-trials-and-first-customers.md` § Half-price start and discounted first period; `leads-content-ads-referrals.md` § Customer referrals: goodwill, incentives and scripts |
| 50% off | discount | the one "half the price" in the sources: a gym owner offering members 50% off in the refund story | gym | [M*] | `free-work-trials-and-first-customers.md` § Half-price start and discounted first period; `hormozi-record.md` § Launch & Go: the partnership collapse and $150,000 in refunds |
| 1/3 of total fee or $9,000 | down payment | before high-touch work starts (q57); q58 "Couplepreneurs Scaling" $9,000 layaway | general | [M*] | `free-work-trials-and-first-customers.md` § First payment: large down payment and layaway |
| $25,000 to $30,000; $9,000 down; $2,500 to $3,000/month; 3-month layaway | price; terms | annual consulting (q71); $9,000 + 12 × $2,500 = $39,000, above $30,000; term not given | general | [M*] | `free-work-trials-and-first-customers.md` § First payment: large down payment and layaway |
| "$5,000 or $25,000" | programme price | q68 attaches the $9,000 layaway to these; $9,000 cannot apply to $5,000 | general | [M*] | `free-work-trials-and-first-customers.md` § First payment: large down payment and layaway |
| $2,000 to $12,000 | price band | the sales team the jump anchor is sized for | general | [M*] | `closing-vetting-and-operating.md` § Jump anchor: raising price without losing sales |
| $2,000 to $3,000; anchor $4,000 = $2,000 + $2,000 in 30 days, or $3,000 today | price | jump anchor, first example | general | [M*] | `closing-vetting-and-operating.md` § Jump anchor: raising price without losing sales |
| $4,000 to $5,000; anchor $6,000 = $4,000 + $2,000 in 30 days, or $5,000 today | price | jump anchor, second example | general | [M*] | `closing-vetting-and-operating.md` § Jump anchor: raising price without losing sales |
| $10,000 to $12,000; $6,000 + $3,000 + $3,000 or 3 × $4,000 | price | third example (q68); installments equal the target; no prepay figure | general | [M*] | `closing-vetting-and-operating.md` § Jump anchor: raising price without losing sales |
| $99 to $299/month; 33% cancelled; 67% stayed; 2.01x revenue; fulfilment costs down 33% | price; churn | tripling on existing gym members; which gym and when not given | gym | [M*] | `closing-vetting-and-operating.md` § Raising prices: tripling on existing members and pricing to the worst month |
| $3,500/month ($800/week); $120,000 a year; $800 to $1,200/month; 36 to 40 months (q49), 36 to 40+ months (q53, q59) | price; retention | worst-month rule: Gym Launch clients cancelled in bad months despite +$120,000 a year; cheaper competitors kept clients longer | gym | [M*] | `closing-vetting-and-operating.md` § Raising prices: tripling on existing members and pricing to the worst month |

---

## Guarantees

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| 30 days | window | generic "30-Day No-Questions-Asked Money-Back Guarantee"; Club a Baby Seal; shark-infested waters | general | [M*] | `guarantees.md` § Guarantee type: unconditional; `guarantees.md` § Guarantee naming: vivid imagery |
| 29 minutes or 29 days | window | Fladlien's "fully informed decision" script | info-product | [M*] | `guarantees.md` § Guarantee script: Fladlien's "fully informed decision" |
| 3x/week; 10 sales calls; $X on ads | condition | activation metrics to tie a conditional guarantee to (q18 and q19 merged) | general | [M*] | `guarantees.md` § Guarantee type: conditional |
| 90 days + 90 days | term | modified service guarantee: miss the target in 90 days, get 90 more free | general | [M*] | `guarantees.md` § Guarantee: conditional sub-types |
| 30 days; 5 minutes | term; response | "We will fill your gym in 30 days"; answer lead calls within 5 minutes (q18 only) | gym | [M*] | `guarantees.md` § Guarantee: conditional service guarantee, Gym Launch |
| 30-day unconditional + 90-day triple money back | terms | stacking two guarantees | general | [M*] | `guarantees.md` § Guarantee: stacking two guarantees |
| 100 against 130 sales at $1,000; 5% (5) against 10% (13) refunds; $95,000 against $117,000; 23% | sales; refunds; net | guarantee math; 117/95 = 1.23x; net sales, not profit; no fulfilment cost on refunded buyers; the 30% lift is assumed; the $1,000 price is q19 only | general | [M*] | `guarantees.md` § Guarantee math: 100 sales against 130 |
| 5% against 5% | break-even | for a stronger guarantee to lose, refunds must offset every new sale (q21) | general | [M*] | `guarantees.md` § Guarantee math: 100 sales against 130 |
| 2x to 4x | conversion lift | changing only guarantee quality (q19, q21); does not match the 30% in the worked math | general | [M*] | `guarantees.md` § Guarantee math: 100 sales against 130 |
| $500 worth of value; 2 refunds in 4,000 sales; 3.5 years; 0.05% | guarantee; refunds | boot-camp unconditional guarantee, his words; the figure is the consumer boot camp; outside record grade C and D, open (L4) | gym | [D] | `guarantees.md` § Guarantee case: boot camp "$500 worth of value", 2 refunds in 4,000; `hormozi-record.md` § Weight-loss boot camp: the $500 guarantee and 2 refunds in 4,000 |
| 6-week (q18, q61); 5-week (q56, videos) | programme length | the guarantee period; "5-week" against a 6-week challenge is a different programme or a slip | gym | [M*] | `hormozi-record.md` § Weight-loss boot camp: the $500 guarantee and 2 refunds in 4,000; `closing-vetting-and-operating.md` § Service business: no unconditional refunds on heavy fulfilment |
| 6 weeks of free training | worst case | best-case, worst-case close as q16 words it; the close itself is `[D]` | gym | [M*] | `guarantees.md` § Guarantee script: best-case, worst-case close |
| 100% of your money back | worst case | q50's template; assumes an unconditional refund | general | [M*] | `closing-vetting-and-operating.md` § Best-case, worst-case close |
| $2,997; $25,000; $3,000,000; 10 refunds; $250,000; $2.75 million | price; buyback; sales | Fladlien's store buyback; counts gross extra sales as profit; ad threshold X missing; origin `[A]` | info-product | [M*] | `guarantees.md` § Guarantee case: Fladlien's $25,000 store buyback; `hormozi-record.md` § Results he reports for clients and others |
| 11 | variations | named guarantee variations in the book, against four types in the videos | general | [M*] | `hormozi-record.md` § What changed between the books and the videos |

---

## Performance pricing

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| 10% of gross revenue growth (q18, q21); 10% of topline revenue (q19, q20) | share | revenue share; very different bases, both kept | general | [M*] | `guarantees.md` § Performance pricing: share percentages, ratchets and floor fees |
| 20% of net profit | share | profit share | general | [M*] | `guarantees.md` § Performance pricing: share percentages, ratchets and floor fees |
| 25% of revenue growth above a baseline | share | q19, q20, q21; not q18 | general | [M*] | `guarantees.md` § Performance pricing: share percentages, ratchets and floor fees |
| 10% up to $50k, 20% over $50k (q18); 10%, 20%, 30% over $X, $Y, $Z (q20); 10% over $50k, 20% over $100k, 30% over $150k (q21) | ratchet | three readings; only the 10/20/30% steps are shared; the q18 and q21 thresholds look filled in by NotebookLM | general | [M*] | `guarantees.md` § Performance pricing: share percentages, ratchets and floor fees |
| greater of $1,000 or 10% of revenue generated (q19, q20, q21); greater of $1,000/month or 10% of revenue growth (q18) | floor fee | hybrid; two readings | general | [M*] | `guarantees.md` § Performance pricing: share percentages, ratchets and floor fees |
| $1,000/month for the first 3 months, then 100% performance | floor fee | q20, q21 | general | [M*] | `guarantees.md` § Performance pricing: share percentages, ratchets and floor fees |
| $1,000/month | base retainer | add one during a long, labour-heavy ramp-up | general | [M*] | `guarantees.md` § Performance pricing: when to avoid or modify it |
| 100% of the revenue; first 6 weeks of membership fees | fee | "my fee was 100% of the revenue I would bring in" | gym | [D] | `guarantees.md` § Performance pricing case: Gym Launch's first turnaround model; `hormozi-record.md` § DFY gym launches: 33 gyms, 21 days, paid from the members' cash |
| $500 refundable deposit; $0 up front | owner cost | DFY launch; refunded (book) or credited (later video), Pass 2 §4 row 17, open | gym | [M*] | `guarantees.md` § Performance pricing case: Gym Launch's first turnaround model; `hormozi-record.md` § DFY gym launches: 33 gyms, 21 days, paid from the members' cash |
| 33 gyms in 18 months; 21 days each; 8 a month at peak | count | DFY turnarounds; all his words; under 2 a month on average, 8 the peak; the Pass 1 flag is withdrawn (Pass 2 §4 row 3) | gym | [D] | `guarantees.md` § Performance pricing case: Gym Launch's first turnaround model; `offer-construction.md` § Delivery vehicles: create flow, monetize flow, add friction; `value-equation.md` § Perceived likelihood: Gym Launch proof numbers; `hormozi-record.md` § DFY gym launches: 33 gyms, 21 days, paid from the members' cash |
| $42,000 | sales per gym | "$42,000 additional sales on average" per DFY launch | gym | [D] | `guarantees.md` § Performance pricing case: Gym Launch's first turnaround model; `hormozi-record.md` § DFY gym launches: 33 gyms, 21 days, paid from the members' cash |
| $40,000 to $100,000 | cash per launch | q61 only; fits a $42,000 average only if most sat near the bottom | gym | [M*] | `hormozi-record.md` § DFY gym launches: 33 gyms, 21 days, paid from the members' cash |
| $100,000/month | cash flow | the point at which he turned DFY into licensing and scaled to 4,000+ locations | gym | [M*] | `offer-construction.md` § Delivery vehicles: create flow, monetize flow, add friction; `hormozi-record.md` § DFY gym launches: 33 gyms, 21 days, paid from the members' cash |
| $20,000/month to $200,000/month | agency revenue | agencies using his software, "in a matter of months"; software not named | agency | [M*] | `guarantees.md` § Performance pricing case: agencies from $20,000 to $200,000 a month; `hormozi-record.md` § Results he reports for clients and others |
| 20 people (or 20 showed appointments) in the first month, or next month free | guarantee | the agency pay-on-show script; origin `[A]` | agency | [M*] | `guarantees.md` § Performance pricing script: pay one time, 20 people or next month free; `pricing-and-tiers.md` § Agency offer: the pay-for-performance script; `hormozi-record.md` § Gym Launch offer: programme sequence, guarantee, bonuses, scarcity |

---

## Scarcity

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| 100 boxes; 100 hoodies; once a month | drop size; cadence | physical limited drops; q24 "100 boxes of a specialty protein-bar flavour once a month" | general | [M*] | `scarcity-and-urgency.md` § Scarcity: physical limited drops |
| 1 to 2 pieces | per item per store | Chanel; his telling, unchecked | general | [M*] | `scarcity-and-urgency.md` § Scarcity: physical limited drops |
| 25 total clients; 10% to 20% | cap; expansion | total business cap script, waitlist once full; 25 may be NotebookLM's | agency | [M*] | `scarcity-and-urgency.md` § Scarcity script: total business cap, 25 clients |
| 5 new clients a week; 3 spots taken; 6 more calls | cap | weekly growth cap script (q22 fullest; q11 marked "e.g.") | general | [M*] | `scarcity-and-urgency.md` § Scarcity script: weekly growth cap, 5 new clients a week; `offer-construction.md` § Offer creation: the five enhancers |
| 100 clients 4 times a year | cohort | cohort cap, 400 a year | general | [M*] | `scarcity-and-urgency.md` § Scarcity: cohort cap |
| 3 tickets; $5,000 | count; event price | bonus scarcity line | info-product | [M*] | `scarcity-and-urgency.md` § Scarcity script: bonus scarcity |
| 20 downloads a week | cap | lead-magnet scarcity on a free checklist | general | [M*] | `scarcity-and-urgency.md` § Scarcity: lead-magnet scarcity |
| 5, 10 or 25 per week (q25, q26); per week or month (q22) | capacity | honest onboarding capacity examples | general | [M*] | `scarcity-and-urgency.md` § Scarcity: honest capacity number and the four rules |
| 81% | capacity | "81% of capacity in your total business"; q24's "We are at 81% capacity" is `[M*]` | general | [D] | `scarcity-and-urgency.md` § Scarcity: honest capacity number and the four rules; `scarcity-and-urgency.md` § Honest scarcity and honest urgency: the rules |
| $15,000 to $25,000; 150 to 100 (q24), uncapped to 100 (q26); "a hundred people"; $5.4 million; about $54,000 a head | ticket; guests; total | Schwarzenegger fundraiser; $54,000 a head includes auction items (Pass 2 §4 row 4 resolves the 100 × $25,000 = $2.5M flag; q22's "before the auction" is overridden) | general | [D] for 100 and $54,000; [M*] rest | `scarcity-and-urgency.md` § Scarcity case: the Schwarzenegger fundraiser; `pricing-and-tiers.md` § Price examples: surgery, consulting days, a fundraiser |
| $700,000; $100k, $500k, $2M+ | donated items | George's watches (q22); a $700,000 total cannot hold a $2M+ watch, so the item values are garbled | general | [M*] | `scarcity-and-urgency.md` § Scarcity case: the Schwarzenegger fundraiser |
| 30 days; quarterly; top 5 in each of 10 categories; $100 a month | challenge terms | Skool Games: time-boxed and real (L7, grade B); entry capped at $100 a month (L6) | general | record | `scarcity-and-urgency.md` § Honest scarcity and honest urgency: the rules; `hormozi-record.md` § Skool: investment and platform claims |

---

## Urgency and launch

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| weekly, bi-weekly, monthly or quarterly | cadence | rolling cohort start dates | general | [M*] | `scarcity-and-urgency.md` § Urgency script: rolling cohorts |
| January 30th; February 28th; March 31st; April 30th | end date | New Year; Valentine's Day Lover; Sexy by Spring; Fools in Love (q24, q25, q26, not q23) | gym | [M*] | `scarcity-and-urgency.md` § Urgency script: rolling seasonal promotions |
| up to 50 to 60 percent; last four hours of the last day; "the last three percent" | share of sales | his words; four of 168 hours is 2.4%, so the 3% is his rounding (Pass 2 §4 row 6); q23 says "up to", q24 and q25 state it flat for week-long launches | general | [D] | `scarcity-and-urgency.md` § Urgency: 50% to 60% of sales in the last four hours |
| 2-day workshop; 1 week out | launch | whisper, tease, shout; "1 week out" is q25 only | general | [M*] | `scarcity-and-urgency.md` § Launch: the whisper, tease, shout sequence |

---

## Bonuses, naming and testing

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| $600 for 200 hours a year | bonus value | price-tag justification example; $3 an hour, as given | general | [M*] | `bonuses-and-naming.md` § Bonus: naming and the price tag |
| $400; 1 to 2 massages; 2 adjustments ($100 value); orthotics $150 savings; training session and 1-month pool pass ($100 value) | price; bonus value | pain-clinic OPS stack; bonus value exceeds the price | local B2C, US | [M*] | `bonuses-and-naming.md` § Bonus stack: the pain-clinic OPS stack on a $400 offer |
| $100 per visit; $100 per referral; $50/mo per signup; $100 per referral; $350 | affiliate fee | chiropractor, orthotics, gym, pharmacy; the $350 sum works but mixes one-time and monthly fees | local B2C, US | [M*] | `bonuses-and-naming.md` § Bonus stack: the pain-clinic OPS stack on a $400 offer |
| orthotics $150, pharmacy $100/mo (q27); together $150 to $200, "$350 pure profit" (q28); orthotics $150, foods and pharmaceuticals $150+ monthly, "$350+" (q29) | savings | three readings of the same stack | local B2C, US | [M*] | `bonuses-and-naming.md` § Bonus stack: the pain-clinic OPS stack on a $400 offer |
| 30% discount; 40% commission | split | Prestige Labs: members' discount and the gym's commission (q61: recurring); who got the 30% is unclear | gym | [M*] | `bonuses-and-naming.md` § Bonus case: Prestige Labs supplement affiliate; `hormozi-record.md` § Prestige Labs: the supplement affiliate model |
| 1 month | trial | tier-upgrade bonus of VIP 1-on-1 access | general | [M*] | `bonuses-and-naming.md` § Bonus: the tier-upgrade bonus; `pricing-and-tiers.md` § Tiers: ascension and the tier-upgrade bonus |
| 3 to 5 | components | MAGIC: "not all these components are mandatory… typically three to five" | general | [D] | `bonuses-and-naming.md` § MAGIC naming: the five components; `bonuses-and-naming.md` § MAGIC naming: steps to build a name; `bonuses-and-naming.md` § MAGIC naming: result plus time is not a rule |
| "$10,000 in 10 days" against "Make your first sale in 10 days" | name | ad-platform compliance: claim plus time reads as an implied guarantee | US | [M*] | `bonuses-and-naming.md` § MAGIC naming: result plus time is not a rule |
| 2 to 3 | wrappers | contenders run at once against a control | general | [M*] | `bonuses-and-naming.md` § Testing: wrappers against a control, and 100 offers; `bonuses-and-naming.md` § MAGIC naming: steps to build a name |
| 100 offers | attempts | "If you try 100 offers, I promise you will succeed"; a persistence line, not a test size | general | [M*] | `bonuses-and-naming.md` § Testing: wrappers against a control, and 100 offers |
| 6 weeks to 28 days or 8 weeks | duration | the fourth thing to vary on a fatigued offer | general | [M*] | `bonuses-and-naming.md` § Enhancing: order to vary a fatigued offer |
| $20 per 1,000; 200,000 people; around $10,000 | reach cost | local market reached once across platforms; at $20 per 1,000, 200,000 people is $4,000, so $10,000 assumes repeats or several platforms, or is misheard | US | [M*] | `bonuses-and-naming.md` § Testing: local market reach cost, $20 per 1,000 |

---

## Free work and the first five

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| 5 | free clients | "make the first five free. The exact number matters less"; q69's "exactly five" is question-shaped; a beginner cannot handle more (q52) | general | [D] | `free-work-trials-and-first-customers.md` § First five free: the number and why |
| 3 | terms | use it, give feedback, leave a killer review | general | [D] | `free-work-trials-and-first-customers.md` § First five free: the three terms of exchange |
| 3,000 messages to 5 free case studies (q52, q69); 100 reach outs to 20 replies to 4 free to 1 paying (q40) | yield | 0.17% against 4%, 24 times apart; one is probably not his figure | general | [M*] | `free-work-trials-and-first-customers.md` § First five free: how many messages it takes; `leads-and-outreach.md` § Warm outreach: volume and pipeline numbers |
| clients 1–5 free; 6–10 80% off; 11–15 60% off; 16–20 40% off; 21–25 20% off; 26 on full price | price step | his words "80% off for the next five, then 60%... then 40% off… and so forth"; the 80/60/40 steps all sit above his 50% discount threshold | general | [D] | `free-work-trials-and-first-customers.md` § Price step-up after the free five: 80/60/40/20 |
| other readings of the ladder | price step | q38 and q40 stop at 40% then full price; q71 "80% off for the first 5" drops the free five; q69 ends "20% to 40% above retail"; q58 "Full Retail Price ($1,000+ or $10,000)", uncited | general | [M*] | `free-work-trials-and-first-customers.md` § Price step-up after the free five: 80/60/40/20; `leads-and-outreach.md` § Warm outreach: the 10 steps (two versions) |
| 20% every 5 sales | price rise | "raise it by 20% every five until you find your sweet spot"; stop when conversion drops; Pass 2 §4 row 7: both rules are in the book | general | [D] | `free-work-trials-and-first-customers.md` § Price step-up: raise 20% every five sales |
| 213 members; $112,000 | result | San Diego free case-study headline; his offer was paid off the sales | gym | [D] | `free-work-trials-and-first-customers.md` § Free case study paid on results: his San Diego offer; `hormozi-record.md` § San Diego free case study: 213 members and $112,000 |
| 13 minutes | video | the raw screen recording that filled his calendar (q38) | gym | [M*] | `free-work-trials-and-first-customers.md` § Free case study paid on results: his San Diego offer; `hormozi-record.md` § San Diego free case study: 213 members and $112,000 |
| 99% | share of market | never buys, but judges you on your free content | general | [M*] | `free-work-trials-and-first-customers.md` § Free content quality: the 99% rule and give until they ask |
| 5-minute video | content | a free video that solves a real problem now (q54) | general | [M*] | `free-work-trials-and-first-customers.md` § Free content quality: the 99% rule and give until they ask |
| a full year | free training | his early free fitness clients; far outside his own five cap; unchecked | gym | [M*] | `hormozi-record.md` § First clients free: a year of free training and a charity donation |

---

## Free-offer models and trials

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| $12,000 of courses; $397/month | value; price | Free Bribe, Frank Kern's newsletter | info-product | [M*] | `free-work-trials-and-first-customers.md` § Seven free-offer models |
| $1,000 challenge; $200/month | value; price | Free Bribe at a gym (re-run q39) | gym | [M*] | `free-work-trials-and-first-customers.md` § Seven free-offer models |
| 28-day trial, 1 workout a week; 3 of 4 (75%); $199 to $299 | trial; upsell rate; price | Limited Free Offer (A/B close); q58 adds 3x/week coaching | gym | [M*] | `free-work-trials-and-first-customers.md` § Seven free-offer models; `free-work-trials-and-first-customers.md` § Free trials: the warning against unconditioned trials; `free-work-trials-and-first-customers.md` § First offer to a new customer: five structures |
| $50 | penalty | Free Trial + Penalty, per missed session or no-show | gym | [M*] | `free-work-trials-and-first-customers.md` § Seven free-offer models; `free-work-trials-and-first-customers.md` § Free trials: the warning against unconditioned trials |
| 95% | revenue share | weight-loss clinics' revenue from required supplements (Free Forever) | general | [M*] | `free-work-trials-and-first-customers.md` § Seven free-offer models |
| $25,000; $300 entry fee | prize; fee | Free Giveaway transformation challenge; the fee is q49's | gym | [M*] | `free-work-trials-and-first-customers.md` § Seven free-offer models |
| first month or 28 days; 9 or 12 months | free period; contract | Free with Commitment | gym | [M*] | `free-work-trials-and-first-customers.md` § Seven free-offer models |
| $199/month to $397/month | contract | q58's price for Free Bribe and Free with Commitment; the $199 floor appears only there | gym | [M*] | `free-work-trials-and-first-customers.md` § Seven free-offer models; `free-work-trials-and-first-customers.md` § First offer to a new customer: five structures |
| $21 for 20 days; 3 weeks; $99 to $199/month; 3 months | trial; delay; price; payback | the competitor gym trial he argues against: little cash, pitch after 3 weeks, 3 months to recoup ads | gym, US | [M*] | `free-work-trials-and-first-customers.md` § Free trials: the warning against unconditioned trials; `free-work-trials-and-first-customers.md` § Free with deposit: the $500 challenge and refund versus credit; `hormozi-record.md` § Weight-loss challenge: deposit, supplements, success rate and the stack |
| 7-day | trial | "try before you buy", like Amazon Prime; q56 mislabels it "Layaway" | general | [M*] | `free-work-trials-and-first-customers.md` § Free trials: the warning against unconditioned trials |
| 22.4x; 11.2:1 against 0.5:1 | cash; ROAS | q56 attaches the agency figures to the gym trial comparison; a blend of two sources | agency | [M*] | `free-work-trials-and-first-customers.md` § Free trials: the warning against unconditioned trials |
| 4 months | free lead generation | deprivation: then a monthly retainer to keep the leads coming | agency | [M*] | `free-work-trials-and-first-customers.md` § Deprivation: four months of free lead generation; `free-work-trials-and-first-customers.md` § Lead magnet: never solve the core problem |
| week 5 of 6; 15 to 20 lbs; 12-month | timing; result; membership | B2C deprivation; q58 only, uncited | gym | [M*] | `free-work-trials-and-first-customers.md` § Deprivation: four months of free lead generation |

---

## Lead magnets and audits

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| 3-second delay, 18% (re-run q39); 9 against 3 seconds, 3% per second, 18% (q70) | conversion loss | website speed audit; whether 3% a second is his or an industry figure is not stated | general | [M*] | `free-work-trials-and-first-customers.md` § Lead magnet: definition and the three types; `free-work-trials-and-first-customers.md` § Audit or problem reveal: the CAC math |
| 7-day (q38); 14-day (re-run q39) | trial | software trial as a lead magnet | general | [M*] | `free-work-trials-and-first-customers.md` § Lead magnet: definition and the three types |
| 1 of 3 coats; 1 of 6 to 8 sessions | step | garage sealant; laser hair removal; one-step lead magnets | general | [M*] | `free-work-trials-and-first-customers.md` § Lead magnet: definition and the three types |
| 2 video modules | free content | first 2 modules of a programme given free | gym | [M*] | `free-work-trials-and-first-customers.md` § Lead magnet: the four delivery methods |
| $25 hard cost; 3x to 10x returns (q38) | cost; return | a hard-cost magnet can still cut CAC; q38's range may blend q39's two figures | general | [M*] | `free-work-trials-and-first-customers.md` § Lead magnet economics: cost per engaged lead |
| 3x to 5x more engaged leads; 10x engagement; $25 + $75 = $100 per engaged lead call; CAC down up to 3x | leads; cost | q39; 3x to 5x and 10x sit in neighbouring bullets; the only cost-per-lead figure in the set | general | [M*] | `free-work-trials-and-first-customers.md` § Lead magnet economics: cost per engaged lead; `leads-content-ads-referrals.md` § Paid ads: his reported returns |
| $25 an hour; $250; 1 in 4; $100 CAC (q56); $25 hard cost, $250+ retail, 4 qualified leads, $100 (q70) | cost; value; CAC | free audit math, two renderings | general | [M*] | `free-work-trials-and-first-customers.md` § Audit or problem reveal: the CAC math |
| $2,000 off | discount | chiropractic diagnostic wrapper "$2,000 off / free initial examination" | general | [M*] | `free-work-trials-and-first-customers.md` § Audit or problem reveal: the CAC math |

---

## First payment and the front end

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| $500 deposit; 6 weeks; 20 lbs or 10% of body weight; 100% refunded or credited | deposit; goal | 6-Week Challenge; refund in the book, credit in a later video (Pass 2 §4 row 17, open) | gym | [M*] | `free-work-trials-and-first-customers.md` § Free with deposit: the $500 challenge and refund versus credit; `free-work-trials-and-first-customers.md` § Seven free-offer models; `hormozi-record.md` § Weight-loss challenge: deposit, supplements, success rate and the stack; `hormozi-record.md` § What changed between the books and the videos |
| $200 to $300 within 48 hours; $700 to $800 | supplements; day-one cash | per challenge customer | gym | [M*] | `free-work-trials-and-first-customers.md` § Free with deposit: the $500 challenge and refund versus credit; `hormozi-record.md` § Weight-loss challenge: deposit, supplements, success rate and the stack |
| $199/month or $200/month (q49); $199 to $299/month (q59); $199/month and $2,388/year (q58) | back-end price | membership after the challenge; the $2,388 is $199 × 12, computed by NotebookLM | gym | [M*] | `free-work-trials-and-first-customers.md` § Free with deposit: the $500 challenge and refund versus credit |
| 78% to 80% (q57, q71); about 80% (q64) | goal achievement | the deposit as skin in the game and a vetting tool | gym | [M*] | `free-work-trials-and-first-customers.md` § Free with deposit: the $500 challenge and refund versus credit; `closing-vetting-and-operating.md` § Vetting inside the funnel and at events; `hormozi-record.md` § Weight-loss challenge: deposit, supplements, success rate and the stack |
| 3 massages for $300 to $500; about $90; 1 in 3; $2,000 | price; labour; conversion; core price | 100% affiliate revenue-share start | local B2C | [M*] | `free-work-trials-and-first-customers.md` § Small paid starts: revenue share, penny offers, quantity downsell |
| 10 CDs for 1 penny | price | low-barrier paid trial; q71 says Sony, the classic offer is usually credited to Columbia House | US | [M*] | `free-work-trials-and-first-customers.md` § Small paid starts: revenue share, penny offers, quantity downsell |
| $7 to $21 | tripwire price | what he breaks from for service businesses (q58, uncited) | general | [M*] | `free-work-trials-and-first-customers.md` § Small paid starts: revenue share, penny offers, quantity downsell |
| $1,500 to $3,997 | deposit | q58's structure A for B2B and agency; joins the dead-zone range with the $3,997 offer, not a stated rule | agency | [M*] | `free-work-trials-and-first-customers.md` § First offer to a new customer: five structures |
| $2,000 to $16,000; $9,000 | price; layaway | q58's structure B; "paid pilot" is the question's label `[A]` | general | [M*] | `free-work-trials-and-first-customers.md` § First offer to a new customer: five structures |
| 15 lbs; 1,000 subscribers; week 4 | activation point | milestones that earn the continuity invite | gym, general | [M*] | `free-work-trials-and-first-customers.md` § Free or cheap to recurring: activation points and the continuity pitch |
| 15 lbs in 6 weeks (q49, q59); 15 lbs in the first 4 weeks (q58); week 4 or 5 of 6 (q58); midway (q59) | result; timing | the continuity pitch, three renderings | gym | [M*] | `free-work-trials-and-first-customers.md` § Free or cheap to recurring: activation points and the continuity pitch |
| $2,000; 30:1; $15,000 a year; 12:1 | price; LTV:CAC | hairdresser-education course ascending to coaching | general | [M*] | `free-work-trials-and-first-customers.md` § Free or cheap to recurring: activation points and the continuity pitch; `hormozi-record.md` § Results he reports for clients and others |
| $99/month or $999/year; $10,000+ | price | low-ticket community ascending to a programme (q59) | general | [M*] | `free-work-trials-and-first-customers.md` § Free or cheap to recurring: activation points and the continuity pitch |
| "Lose 20 lbs in 6 weeks"; "Fill your gym in 30 days"; "$29/month gym pass"; "$1,000/month ad management" | offer | attraction offers against commoditised access | gym, agency | [M*] | `free-work-trials-and-first-customers.md` § Front end: create flow, monetise flow, then add friction |

---

## Core Four, Rule of 100 and allocation

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| $0 | ad spend | warm outreach and content | general | [M*] | `leads-and-outreach.md` § Core Four: trade-offs and which to start with |
| under $1M; first 5 customers | revenue; customers | "more time than money": start with warm outreach | general | [M*] | `leads-and-outreach.md` § Core Four: trade-offs and which to start with |
| $1,000,000 | threshold | 1-1-1: "$1,000,000 in revenue/profit" (q36); "$1 Million in revenue (and up to $3 Million)" (q42); revenue (q51); "$1 million to $10 million" (q62); "1-1-1-1" (q66); revenue against profit unchecked | general | [M*] | `leads-and-outreach.md` § 1-1-1 rule: one offer, one avatar, one channel; `closing-vetting-and-operating.md` § Service business: 1-1-1 and the two ways to grow |
| 6 gyms, a chiropractor agency, a dental agency, a supplement line | count | what he ran at once while building Gym Launch; revenue slowed in all | gym | [M*] | `closing-vetting-and-operating.md` § Service business: 1-1-1 and the two ways to grow |
| 100 a day for 100 days | actions | Rule of 100: 100 warm reach outs; 100 minutes of content, at least 1 piece a day (q43: per platform); 100 cold reach outs; 100 minutes on ads | general | [M*] | `leads-and-outreach.md` § Rule of 100; `leads-content-ads-referrals.md` § Content: posting volume |
| first 4 hours | time | one channel exclusively under $1M (q44, q66) | general | [M*] | `leads-and-outreach.md` § First 4 hours and the 444 split |
| 4 + 4 + 4 | hours | 444 split: promotion, delivery, building; a 12-hour day (q65) | general | [M*] | `leads-and-outreach.md` § First 4 hours and the 444 split |
| 70% / 20% / 10% | allocation | proven, adjacent, new: marketing effort, ad creative, resources (q66) | general | [M*] | `leads-and-outreach.md` § 70/20/10 allocation; `closing-vetting-and-operating.md` § Service business: 70/20/10 and don't break what works |
| 1 brings 2, 2 bring 4 | referral loop | channel roadmap step 4 | general | [M*] | `leads-and-outreach.md` § Channel roadmap for a new business, seven steps |
| $100M+ | lead machine | channel roadmap step 7 | general | [M*] | `leads-and-outreach.md` § Channel roadmap for a new business, seven steps |

---

## Warm outreach

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| 1,000+ | contacts | typical combined warm list (q40) | general | [M*] | `leads-and-outreach.md` § Warm outreach: building the list |
| 100 a day; 3,000 in about 30 days | reach | working a 3,000-contact list (q52) | general | [M*] | `leads-and-outreach.md` § Warm outreach: building the list; `leads-and-outreach.md` § Warm outreach: the 10 steps (two versions) |
| 30 seconds | per profile | personalisation research | general | [M*] | `leads-and-outreach.md` § Warm outreach: the 10 steps (two versions) |
| up to 3 times; once a day for 3 days | follow-up | each non-responsive warm contact | general | [M*] | `leads-and-outreach.md` § Warm outreach: the 10 steps (two versions); `leads-and-outreach.md` § Warm outreach: volume and pipeline numbers |
| 500 a week (5 days) | reach | warm volume | general | [M*] | `leads-and-outreach.md` § Warm outreach: volume and pipeline numbers |
| 1 paying per 100 | benchmark | warm reach outs to paying customers (q40) | general | [M*] | `leads-and-outreach.md` § Warm outreach: volume and pipeline numbers |
| 1% at $400; 5 a week; $2,000 a week; $104,000 a year | conversion; revenue | q40's path to $100,000 a year with no ads, "more than double the median US household income"; a 1,000-contact list lasts 2 weeks at 500 a week | US | [M*] | `leads-and-outreach.md` § Warm outreach: volume and pipeline numbers |

---

## Cold outreach and follow-up

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| 1 to 3 | personal details | per cold message | general | [M*] | `leads-and-outreach.md` § Cold outreach: three problems and their fixes |
| 1 to 3 sentences | opener | cold email | general | [M*] | `leads-and-outreach.md` § Cold outreach: calls, DMs and email |
| below 3rd grade; 50% | reading level; response lift | cold email through a reading-level app; no source or sample; content at 3rd to 5th grade | general | [M*] | `leads-and-outreach.md` § Cold outreach: calls, DMs and email |
| 100 dials; ~20% pickup; ~25% take the magnet; ~4 engaged; ~1 an hour | cold calls | per 100 dials (q41); 20 × 25% = 5, not 4 | general | [M*] | `leads-and-outreach.md` § Cold outreach: benchmarks per 100 |
| ~30% open; ~10% reply; ~3 engaged (~3%) | cold email | per 100 | general | [M*] | `leads-and-outreach.md` § Cold outreach: benchmarks per 100 |
| up to 20% reply (~20 per 100) | cold DMs with voice or video | counts replies as engaged leads, which the email line does not | general | [M*] | `leads-and-outreach.md` § Cold outreach: benchmarks per 100 |
| 1% to 3%; 20% | engagement; pickup | q66's readings, lower than q41's ~4% and ~20% | general | [M*] | `leads-and-outreach.md` § Cold outreach: benchmarks per 100 |
| 1 in 10 (q41); 10% of lead-magnet users (q66) | conversion | engaged leads to customers; the same 10% on two bases; warm runs 4 free to 1 paying (25%) | general | [M*] | `leads-and-outreach.md` § Cold outreach: benchmarks per 100 |
| 5 booked calls; 4 engaged leads; 5 appointments a day; 50 or 5,000 touches | daily goal | open to goal | general | [M*] | `leads-and-outreach.md` § Open to goal |
| 2 to 3 (q41); 1 to 2, or one call (q72) | conversations to close | higher-ticket against local B2C | general | [M*] | `leads-and-outreach.md` § Follow-up: multi-touch, multi-channel, and the cadence; `closing-vetting-and-operating.md` § Speed to lead and close-rate numbers |
| up to 3 a day for 3 days, up to 9 touches (q45); once a day for 3 days, 3 touches (q40, q66) | cadence | initial follow-up; two readings, unchecked against the audio | general | [M*] | `leads-and-outreach.md` § Follow-up: multi-touch, multi-channel, and the cadence |
| once a week | cadence | direct-mail follow-up (q45) | general | [M*] | `leads-and-outreach.md` § Follow-up: multi-touch, multi-channel, and the cadence |
| 3 to 6 months | wait | before re-contacting a worked list (q41, q45, q66) | general | [M*] | `leads-and-outreach.md` § Follow-up: multi-touch, multi-channel, and the cadence |
| month 1: 0 ($0); month 2: 2 ($32,000); month 3: 4 ($64,000); month 4: 6 ($96,000); month 9: 30 ($480,000/month) | sales | Gym Launch cold outbound ramp; $16,000 a sale throughout | gym | [M*] | `leads-and-outreach.md` § Gym Launch cold outbound ramp; `hormozi-record.md` § Gym Launch revenue and profit |

---

## Speed to lead, closing and trust

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| 60 seconds; 391% (4.91x, "nearly 5x"); 4x to 5x (q47) | sales lift | contacting a lead within a minute of opt-in; likely an industry statistic, no study named | general | [M*] | `leads-and-outreach.md` § Engaging leads: speed to lead and the "maniac" caller; `closing-vetting-and-operating.md` § Speed to lead and close-rate numbers |
| 50% to 80% (1.6x); 5x | close rate; throughput | speed often moves revenue more than the script (q50) | general | [M*] | `leads-and-outreach.md` § Engaging leads: speed to lead and the "maniac" caller; `closing-vetting-and-operating.md` § Speed to lead and close-rate numbers |
| 24 to 48 hours (q45); 48 hours (q66) | onboarding window | when satisfaction and retention are mostly set; CLOSER's reinforce step | general | [M*] | `leads-and-outreach.md` § Engaging leads: speed to lead and the "maniac" caller; `closing-vetting-and-operating.md` § CLOSER: the six-step sales conversation |
| 1 in 3 (33%) | close rate | target on qualified calls (q66) | general | [M*] | `closing-vetting-and-operating.md` § Speed to lead and close-rate numbers; `leads-content-ads-referrals.md` § Sweep: numbers q66 gives as rules |
| 11,000 (q55: 11,000+) | 5-star reviews | proof beats promise: one result with 11,000 reviews beats four results with one | general | [M*] | `closing-vetting-and-operating.md` § Trust: proof beats promise |
| $1 | frame | dollar-store frames for review screenshots | general | [M*] | `closing-vetting-and-operating.md` § Trust: damaging admissions, the flash roll and proof walls |
| 1 or 0 | need-to-believes | the limit per offer, learned from Prestige Labs' slow calls | general | [M*] | `hormozi-record.md` § Prestige Labs: the supplement affiliate model |

---

## Vetting

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| 33% to 50% | lead volume | given up to raise ticket size and avatar tier | general | [M*] | `closing-vetting-and-operating.md` § Vetting: when to add qualification |
| 10 steps, not 1 | funnel steps | filters tire-kickers before a call | general | [M*] | `closing-vetting-and-operating.md` § Vetting: five levers for lead quality |
| 5-minute | video | value-first gate before booking | general | [M*] | `closing-vetting-and-operating.md` § Vetting: five levers for lead quality |
| $500 for a $1,000 programme | minimum spend | the qualifier question | general | [M*] | `closing-vetting-and-operating.md` § Vetting: qualifier scripts |
| 80%+ | close rate | in a vetted event room | general | [M*] | `closing-vetting-and-operating.md` § Vetting inside the funnel and at events |
| 1,000 subscribers | milestone | before a higher-tier call in communities | general | [M*] | `closing-vetting-and-operating.md` § Vetting inside the funnel and at events |
| 70x; $5,000 against $42,000 LTV | profit; LTV | what vetting earned him against a generic-ad consultant; $42,000/$5,000 = 8.4x, so the 70x is not derivable; Gym Launch LTV elsewhere is $126,000+ | gym | [M*] | `closing-vetting-and-operating.md` § Vetting: four market qualifications |

---

## Unit economics and paid ads

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| 3:1 minimum; 10:1+ (q41, cold); 4:1 or 5:1+ (q44); 5:1 to 10:1+ (q66); 3:1 or higher (q65) | LTGP:CAC | the minimum is agreed everywhere; upper targets differ; below 3:1 the model, not the ads, is usually at fault (q44) | general | [M*] | `leads-and-outreach.md` § LTGP to CAC: the ratio targets |
| 2x first-30-day cash; $100 to $200 | testing budget | spend on a new ad before judging; q44 states the base as gross cash, the example as cash profit | general | [M*] | `leads-content-ads-referrals.md` § Paid ads: testing and scaling budgets |
| 1x ($100), zero leads | kill rule | shut the ad off | general | [M*] | `leads-content-ads-referrals.md` § Paid ads: testing and scaling budgets |
| × 1.20 | padding | Target Monthly Spend = (Desired Customers × CAC) × 1.20 | general | [M*] | `leads-content-ads-referrals.md` § Paid ads: testing and scaling budgets |
| 30 days; 100%+ of CAC (q66) | payback | client-financed acquisition | general | [M*] | `leads-content-ads-referrals.md` § Paid ads: testing and scaling budgets |
| 11 times | creatives tested | top 0.1% of digital advertisers (q66); no source for the cohort | general | [M*] | `leads-content-ads-referrals.md` § Paid ads: testing and scaling budgets |
| 36:1 | lifetime ROAS | average across portfolio companies | his businesses | [M*] | `leads-content-ads-referrals.md` § Paid ads: his reported returns; `hormozi-record.md` § Acquisition.com: portfolio numbers and ad returns |
| $1,000; 19 sales at $299; $5,700; about 5.7:1 | first campaign | his first gym ad; 19 × $299 = $5,681 | gym | [M*] | `leads-content-ads-referrals.md` § Paid ads: his reported returns; `hormozi-record.md` § First gym: marketing mistakes and early ad results |
| 10:1 or 13:1 on $1,500/month, net $13,500; competitor $15,000/month at 4:1, net $45,000 | ROAS; profit | his early bragging; $13,500 fits 10:1, 13:1 would net $18,000; lesson: absolute profit over ROAS | gym | [M*] | `hormozi-record.md` § First gym: marketing mistakes and early ad results |
| up to 78% | share of clients | consume long-form content before booking or buying; no base | general | [M*] | `leads-content-ads-referrals.md` § Content: give-to-ask ratio and the path to a customer |

---

## Content

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| at least 100 minutes a day; 1 primary piece a day per platform | volume | Rule of 100 for content | general | [M*] | `leads-content-ads-referrals.md` § Content: posting volume |
| up to 10 short-form a day per platform; long-form up to 5 days a week | volume | platform maxima at scale | general | [M*] | `leads-content-ads-referrals.md` § Content: posting volume |
| twice a month; 30 clips | batch | recording sessions; per session or per month is unclear | general | [M*] | `leads-content-ads-referrals.md` § Content: posting volume |
| 450 a week | pieces | Acquisition.com's media team (q63); q66 calls it the benchmark for a global brand, not a small-business rule | his businesses | [M*] | `leads-content-ads-referrals.md` § Content: posting volume; `hormozi-record.md` § Acquisition.com: the giving flywheel and the refused consulting days |
| 1 to 5 seconds | hook | the opening seconds or the headline | general | [M*] | `leads-content-ads-referrals.md` § Content: hooks, headlines and callouts |
| at least 2 of 7 | headline elements | Recency, Relevancy, Celebrity/Authority, Proximity, Conflict, Unusual, Ongoing | general | [M*] | `leads-content-ads-referrals.md` § Content: hooks, headlines and callouts |
| 3 seconds; 40,000 to 780,000 views; "a 19x lift" (19.5x) | views | cutting preamble so the hook hit at once (q64) | his businesses | [M*] | `leads-content-ads-referrals.md` § Content: hooks, headlines and callouts; `hormozi-record.md` § His media: audience drift and the hook cut |
| 3.5:1; 3.5 minutes of TV per 1 minute of ads; 3 organic posts per 1 ad (3:1); 70% value, 30% pitch (2.33:1) | give-to-ask | three readings disagree: 3.5:1 is about 78/22, so one is wrong; the book gave no ratio | general | [M*] | `leads-content-ads-referrals.md` § Content: give-to-ask ratio and the path to a customer; `hormozi-record.md` § What changed between the books and the videos |
| $100 for a month | challenge | manufactured content example, "I lived on $100 for a month" | general | [M*] | `leads-content-ads-referrals.md` § Content: topics, framing and the pillar |
| 3 to 6 months | drift | his lifestyle-content period, which lost part of his core audience | his businesses | [M*] | `hormozi-record.md` § His media: audience drift and the hook cut |

---

## Referrals and affiliates

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| 1 to 4 weeks | event length | referral events (Bring-a-Friend, Spouse Challenge) | general | [M*] | `leads-content-ads-referrals.md` § Customer referrals: goodwill, incentives and scripts |
| "Sell 3, get it free" | incentive | non-cash referral reward | general | [M*] | `leads-content-ads-referrals.md` § Customer referrals: goodwill, incentives and scripts |
| "3 times the results" | claim | inside the "Not IF, but WHO" script, not a study | general | [M*] | `leads-content-ads-referrals.md` § Customer referrals: goodwill, incentives and scripts |
| 25% to 30% | sign-up lift | asking for referrals at the point of sale; q66 uses the same range for opt-ins and show-ups | general | [M*] | `leads-content-ads-referrals.md` § Customer referrals: goodwill, incentives and scripts; `leads-content-ads-referrals.md` § Sweep: numbers q66 gives as rules |
| 2 referrals each; 4:1 to 12:1 | LTGP:CAC | what referrals do to the ratio | general | [M*] | `leads-content-ads-referrals.md` § Customer referrals: goodwill, incentives and scripts |
| 39x in 15 months; 100M users; $10 give / $10 get | growth | Dropbox and PayPal, third-party cases he cites | US | [M*] | `leads-content-ads-referrals.md` § Customer referrals: goodwill, incentives and scripts |
| 10% to 20% of year-1 earnings | affiliate buy-in | skin in the game for affiliates | general | [M*] | `leads-content-ads-referrals.md` § Affiliates: qualifying, payout tiers and offers |
| 25%, 50%, 100% of CAC; 5 active clients | payout | 3-tier affiliate payout by stage | general | [M*] | `leads-content-ads-referrals.md` § Affiliates: qualifying, payout tiers and offers |
| sell 3; over $300; 100% | affiliate offer | "Peel off a piece": the affiliate keeps all of it | general | [M*] | `leads-content-ads-referrals.md` § Affiliates: qualifying, payout tiers and offers |
| $4,000 to acquire; $120,000 sales; $90,000 gross profit; $54,000 net; 13.5:1 | affiliate economics | worked example; implies $36,000 in payouts | general | [M*] | `leads-content-ads-referrals.md` § Affiliates: qualifying, payout tiers and offers |
| 1 super-affiliate; 10 agencies a month; 50 local businesses a month; 2,500 leads a month; $12,500 a month; $1.7M a month in 6 months | chain | "Allan Software" (possibly ALAN); the chain mixes units | agency | [M*] | `leads-content-ads-referrals.md` § Affiliates: his reported cases; `hormozi-record.md` § Results he reports for clients and others |
| 4,000 affiliates; 14 packages a month; $200 average order; tens of millions | supplements | Prestige Labs; 4,000 × 14 × $200 = $11.2M a month if every affiliate sold 14 | gym | [M*] | `leads-content-ads-referrals.md` § Affiliates: his reported cases; `hormozi-record.md` § Prestige Labs: the supplement affiliate model |

---

## Staff, delegation and operating

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| 10x to 100x | output | one A-player marketer against a B or C player | general | [M*] | `leads-content-ads-referrals.md` § Employees for lead generation |
| 20% to 40% | share of schedule | tasks grouped into one full-time hire after a week's time audit | general | [M*] | `leads-content-ads-referrals.md` § Employees for lead generation |
| 3 to 6 months | deadline | hire an agency to learn, then replace it | general | [M*] | `leads-content-ads-referrals.md` § Agencies: the trap and hire-to-learn |
| 100% of a monthly payment up to $500 (q51); $500 or $1,000 (q72); $1,000 (q66) | discretionary spend | to fix a complaint without sign-off; three readings | general | [M*] | `closing-vetting-and-operating.md` § Delegation: 3 Ds and authority to match responsibility; `leads-content-ads-referrals.md` § Sweep: numbers q66 gives as rules |
| $150k OTE; 50% base ($75k); 10% to 12.5% of location profit | operator pay | location manager (q72) | gym | [M*] | `closing-vetting-and-operating.md` § Delegation: 3 Ds and authority to match responsibility |
| 80%+ | gross margin | target for service and digital products | general | [M*] | `leads-content-ads-referrals.md` § Sweep: numbers q66 gives as rules |
| 20%+; a 20% price rise doubles net profit | net margin | baseline; the doubling holds if volume and costs hold | general | [M*] | `leads-content-ads-referrals.md` § Sweep: numbers q66 gives as rules |
| 14 days | cash collected | the key onboarding KPI | general | [M*] | `leads-content-ads-referrals.md` § Sweep: numbers q66 gives as rules |
| 6-week or 90-day | cycle | front-end transformation offer length | general | [M*] | `leads-content-ads-referrals.md` § Sweep: numbers q66 gives as rules |
| square root of headcount; 50% | output | Price's Law (Derek de Solla Price) | general | [M*] | `leads-content-ads-referrals.md` § Sweep: numbers q66 gives as rules |
| 3 to 5 years; 10 years | horizon | scale location models; build $100M+ enterprise value (the split is Pass 1's reading) | general | [M*] | `leads-content-ads-referrals.md` § Sweep: numbers q66 gives as rules |
| $1M to $3M; $3M to $10M | revenue band | the Swamp; then growth from LTV, retention and ascension | general | [M*] | `closing-vetting-and-operating.md` § Service business: the Swamp and scaling bands |
| $1,500 to $3,000/month ($450/week); 4 to 6 months | price; stick | SMB dead zone; $450 × 52 / 12 = $1,950/month, inside the range; origin `[A]` | SMB, US | [M*] | `closing-vetting-and-operating.md` § Service business: the SMB dead zone; `leads-content-ads-referrals.md` § Sweep: numbers q66 gives as rules |
| $300 to $400/month (q53 under $400; q66 $400 or less); 29 to 38 months (q51), 30 to 40 months (q66) | price; stick | down-market exit from the dead zone | SMB, US | [M*] | `closing-vetting-and-operating.md` § Service business: the SMB dead zone; `leads-content-ads-referrals.md` § Sweep: numbers q66 gives as rules |
| $10,000+ or performance-based | price | up-market exit (q53) | SMB, US | [M*] | `closing-vetting-and-operating.md` § Service business: the SMB dead zone |
| 25 to 60 clients | cap | 1-on-1 founder labour | general | [M*] | `closing-vetting-and-operating.md` § Offer as the main lever: the $10K versus $10M offer |
| about $100 against $2 million; $5 million a year | value | the same advice to a beginner and to a founder (q48 added value; q57 added gross profit) | general | [M*] | `closing-vetting-and-operating.md` § Offer as the main lever: the $10K versus $10M offer |
| 1 to 3 months | pre-sell | before delivery exists | general | [M*] | `closing-vetting-and-operating.md` § Service business: do it by hand, pre-sell, then productise |
| 100% | exposure | never carry all of a partnership's financial risk | general | [M*] | `closing-vetting-and-operating.md` § Partners: TEAM and never carry 100% of the risk |
| 6 consecutive months; 30 days (q51), 1 month (q72) | growth; vacation test | before a second location | local B2C | [M*] | `closing-vetting-and-operating.md` § Local business: location rules and the pre-sale test |
| $500 to $1,000; 5 to 10 zip codes; 5-year lease; $500k buildout | test spend | pre-sale market test before committing | local B2C, US | [M*] | `closing-vetting-and-operating.md` § Local business: location rules and the pre-sale test |
| 200 members; 1,000,000 people; "0.002%" | market share | stated as 0.002%; it is 0.02% | gym | [M*] | `closing-vetting-and-operating.md` § Local business: location rules and the pre-sale test |

---

## His record: first gyms and early years

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| 2013/2014; age 24; $50,000; $10,000; $34,000; 6 locations over 3 years | savings; spend | first gym; $10,000 + $34,000 = $44,000, leaving $6,000 unaccounted for | gym | [M*] | `hormozi-record.md` § First gym: savings, build cost and expansion |
| $250,000 | build cost | ego-driven second gym; made the same money as the $34,000 gym | gym | [M*] | `hormozi-record.md` § First gym: savings, build cost and expansion |
| 300 flyers; 1 call; 5,000; 5,000 a day for 30 days (150,000) | flyers | his sample against his mentor's | gym | [M*] | `hormozi-record.md` § First gym: marketing mistakes and early ad results |
| 80+ hours a week; under $30,000 a year; two years | hours; pay | sole operator while equity partners took no salary | gym | [M*] | `hormozi-record.md` § First gym: marketing mistakes and early ad results |
| 50/50; $45,700; $150,000 overnight; four years of savings | partnership; loss | Launch & Go: the partner embezzled $45,700; refunds after gym owners' stunts; client or competitor poacher is open (Pass 2 §4 row 11) | gym | [M*] | `hormozi-record.md` § Launch & Go: the partnership collapse and $150,000 in refunds |
| May/June 2017 | date | move to the licensing model | gym | [M*] | `hormozi-record.md` § Launch & Go: the partnership collapse and $150,000 in refunds |
| Christmas Eve 2016; "120 grand"; six months | hold | the processor hold, his words | gym | [D] | `hormozi-record.md` § Christmas Eve: the payment processor hold |
| $22,000; $23,000; "-$22,000 / $1.36" | commissions; bank | NotebookLM's balance is garbled; $23,000 − $22,000 is about $1,000 | gym | [M*] | `hormozi-record.md` § Christmas Eve: the payment processor hold |
| $6,000; $8,000; $10,000; $60,000 in one day; 48 hours; $150,000 | price; cash; debt | phone licensing day after the refund debt; number of sales behind the $60,000 not given | gym | [M*] | `hormozi-record.md` § Phone licensing day: $6,000, $8,000, $10,000 and $60,000 in a day; `pricing-and-tiers.md` § Pricing case: early licensing at $6,000, $8,000 and $10,000; `offer-construction.md` § Delivery vehicles: create flow, monetize flow, add friction |
| $6,000; almost $44,000 in 30 days; 4x | price; cash | the Boise, Idaho gym owner who bought the licence (q64) | gym | [M*] | `hormozi-record.md` § Phone licensing day: $6,000, $8,000, $10,000 and $60,000 in a day |

---

## His record: Gym Launch

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| 158 gyms; 11 months | survey | voluntary survey of his own clients; self-selected by construction (L11) | gym | [D] | `pricing-and-tiers.md` § Pricing case: the 158-gym survey; `value-equation.md` § Perceived likelihood: Gym Launch proof numbers; `hormozi-record.md` § Gym Launch client results and the 158-gym survey |
| 10.7% to 6.8% | monthly churn | survey result | gym | [D] | `pricing-and-tiers.md` § Pricing case: the 158-gym survey; `hormozi-record.md` § Gym Launch client results and the 158-gym survey |
| $2,943 to $8,940 a month; "that's 3.1x" | profit | the ratio is 3.04x, so 3.1x is his rounding (Pass 2 §4 row 2); $2,943 × 12 = $35,316, near the $35,280 average | gym | [D] | `pricing-and-tiers.md` § Pricing case: the 158-gym survey; `value-equation.md` § Perceived likelihood: Gym Launch proof numbers; `hormozi-record.md` § Gym Launch client results and the 158-gym survey |
| $239,000 per month (audio); per year (NotebookLM) | topline growth | open: against a $6,000 a month profit gain the monthly reading is implausible, so the audio is probably misheard or misspoken | gym | [D] audio, open | `pricing-and-tiers.md` § Pricing case: the 158-gym survey; `value-equation.md` § Perceived likelihood: Gym Launch proof numbers; `value-equation.md` § Time delay: long-term outcome and short-term wins |
| +$160,000 a year; +67 members; +$4,400 a month; $129 to $167 a month | revenue; members; retail; price | other survey figures | gym | [M*] | `pricing-and-tiers.md` § Pricing case: the 158-gym survey; `hormozi-record.md` § Gym Launch client results and the 158-gym survey |
| $30,000 in the first 30 days; $15,500 in the first 14 days | cash | the average gym owner on the launch system; no sample size for either | gym | [M*] | `value-equation.md` § Perceived likelihood: Gym Launch proof numbers; `hormozi-record.md` § Gym Launch client results and the 158-gym survey |
| $120,000 a year | extra net profit | client claim; the survey gives ($8,940 − $2,943) × 12 = $71,964 | gym | [M*] | `hormozi-record.md` § Gym Launch client results and the 158-gym survey; `closing-vetting-and-operating.md` § Raising prices: tripling on existing members and pricing to the worst month |
| 4,000+ to 4,500+ | locations | gyms served; the record lists 4,500+ (Capstone, grade A) | gym | [M*] | `hormozi-record.md` § Gym Launch client results and the 158-gym survey; `hormozi-record.md` § The exit: Gym Launch and Prestige Labs, 2021 |
| $6,820,000 (2017); $25.9 million revenue and $17 million take-home (2018) | revenue; profit | Gym Launch | gym | [M*] | `hormozi-record.md` § Gym Launch revenue and profit |
| $1.2 million a month profit; $2 million a month revenue | pace | end of year one; $17M a year is $1.42M a month; $2M a month is $24M a year | gym | [M*] | `hormozi-record.md` § Gym Launch revenue and profit |
| $500,000 to $28,000,000 a year in 18 months; under $1,000,000 ad spend; $3M to $17M | revenue; profit | q61 (a run rate); q48 also gives $3M to $17M | gym | [M*] | `hormozi-record.md` § Gym Launch revenue and profit |
| $120 million in 24 to 36 months (q60); in 24 months (book claim) | sales | total; no record found (L3) | gym | [M*] | `hormozi-record.md` § Gym Launch revenue and profit; `hormozi-record.md` § Said against done: the ledger (Pass 2 §5) |
| $30,000+ in 30 days | guarantee | DWY guarantee as q61 gives it; no quote, unsourced | gym | [M*] | `hormozi-record.md` § Gym Launch offer: programme sequence, guarantee, bonuses, scarcity |
| 60 minutes daily; 100+ meal plans; 4 months | bonus | daily Zoom with him; nutrition assets; free lead-nurture software (q61 blends offers) | gym | [M*] | `hormozi-record.md` § Gym Launch offer: programme sequence, guarantee, bonuses, scarcity |
| $800/week ($42,000/year) to $600/week ($31,000/year; $31,200); $100,000 a month overhead; topline down 25%; overhead up $1.2M a year; $5,000,000 a year profit lost | price cut | churn stayed the same; q71: he expected it to halve churn | gym | [M*] | `hormozi-record.md` § Gym Launch price cut: $800 to $600 a week and $5 million lost; `free-work-trials-and-first-customers.md` § When free works and when it fails |

---

## His record: Prestige Labs, the exit, Acquisition.com, books, Skool

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| 2018; $1.5 million a month | revenue | Prestige Labs by the end of its first year | gym | [M*] | `hormozi-record.md` § Prestige Labs: the supplement affiliate model |
| 2021; 66%; $46.2 million; $42 million over 4 years | stake; valuation; owner pay | sale to American Pacific Group; the deal is grade A (Capstone), the price and the 66% grade C (L2) | his businesses | [M*] | `hormozi-record.md` § The exit: Gym Launch and Prestige Labs, 2021 |
| 2020; $100 million at age 32 (2022) | net worth | Acquisition.com founded; personal net worth | his businesses | [M*] | `hormozi-record.md` § Acquisition.com: founding, criteria and what it charges |
| $3M to $10M revenue (q55: "or up to $50M") to $1M EBITDA | investment criteria | the Leads author's note dates the change | his businesses | [M*] | `hormozi-record.md` § Acquisition.com: founding, criteria and what it charges; `hormozi-record.md` § What changed between the books and the videos |
| $0 | charge | for courses, training or advice | his businesses | [M*] | `hormozi-record.md` § Acquisition.com: founding, criteria and what it charges |
| top 1%; $1 million+ EBITDA | filter | the giving flywheel monetises through equity past this line | his businesses | [M*] | `hormozi-record.md` § Acquisition.com: the giving flywheel and the refused consulting days |
| 200+ hours; 14 hours; 10 stages; 8 functions | build; length | the free $100M Scaling Roadmap | his businesses | [M*] | `hormozi-record.md` § Acquisition.com: the giving flywheel and the refused consulting days |
| $250 million+ a year; $1.6 million a week; 20,000+ leads a day | portfolio | $1.6M a week is $83.2M a year; Pass 2 §4 row 16 reads the two as different dates | his businesses | [M*] | `hormozi-record.md` § Acquisition.com: portfolio numbers and ad returns |
| 1.8x revenue, 3.01x profit (first 12 months); 2.3x revenue, 4.7x profit (months 12 to 24) | growth | average portfolio company; "verified", with no sample or method | his businesses | [M*] | `hormozi-record.md` § Acquisition.com: portfolio numbers and ad returns |
| 2021; 19 August 2023 | date | $100M Offers published; $100M Leads launched | his businesses | [M*] | `hormozi-record.md` § Books: prices, sales and copies given away |
| $0.99 or $0; $16 to $17 | price; shipping | ebook; free hardback "Business Backpack", buyer pays shipping | his businesses | [M*] | `hormozi-record.md` § Books: prices, sales and copies given away |
| 1 million+ copies; 25,000+ 5-star reviews; 1,000 a day with $0 on ads; 3.6 million donated | sales | donated exceeds sold: different counts or dates; free audiobooks checked (L1, done) | his businesses | [M*] | `hormozi-record.md` § Books: prices, sales and copies given away |
| $99/month; 30-day free trial | price | Skool per community; trial in book bundles | his businesses | [M*] | `hormozi-record.md` § Skool: investment and platform claims |
| 1 in 2; $1,360 a month; $50,000 a month | earnings | paid communities making at least $1; the average; the top Skool Games winner; a part-owner's claims about others | his businesses | [M*] | `hormozi-record.md` § Skool: investment and platform claims |
| $9 and $99 | tiers | Skool's listed monthly tiers against "never discount the core" (L6, "different scale") | his businesses | record | `hormozi-record.md` § Skool: investment and platform claims; `pricing-and-tiers.md` § Discounting: never discount the core offer |

---

## Other results he reports

| Figure | Unit | What it governs | Scale | Marker | Home |
|---|---|---|---|---|---|
| $450,000 a month; 5:1; 30% close; $150,000 profit; one 50% price rise; 8 weeks; $1,000,000 a month; 10:1; profit nearly tripled | revenue; ROAS; profit | a weight-loss brand; a 50% rise alone gives $675,000, the rest is unexplained | general | [M*] | `hormozi-record.md` § Results he reports for clients and others |
| 5-day challenge to one 2 to 4 hour event; 50%+ drop-off | format | the video's replacement for multi-day challenges, doubling the number pitched; the book's 6-week challenge is a paid front end | general | [M*] | `hormozi-record.md` § What changed between the books and the videos |
