---
type: corpus
aliases: ["Frameworks Index"]
corpus: alex-hormozi
layer: retrieval
tags: [corpus, frameworks, leads, machine, offers]
source: skills/corpus-ingestion
created: 2026-10-16
file: frameworks-index
---

# Frameworks Index

Every named framework, formula, acronym, list and script family in the Alex Hormozi corpus, one
line each. Grep the name here, then open the home file at the heading given. Compiled from the
eleven domain files in this folder, with `pass-2-reconciliation.md` §2 to §4 applied where they
override Pass 1. Every figure is indexed by value in `numbers-index.md`.

**Columns.** *Type:* FRM framework, SCR script, PRN principle, MEC mechanism, WRN warning, NUM
number set, CLM claim about a result, BIO what he did. *Prov:* `[D]` the words were matched to his
own audio (Pass 2 §2); `[M*]` NotebookLM transcribed the audio and chose the words; `[A]` the
sources do not hold it. Where a construct belongs to someone else, its line says whose it is.
*Home:* file § heading, exact, so `grep -n '^## Heading' file` finds it.

**Home files:** `value-equation.md` · `offer-construction.md` · `pricing-and-tiers.md` ·
`guarantees.md` · `scarcity-and-urgency.md` · `bonuses-and-naming.md` ·
`free-work-trials-and-first-customers.md` · `leads-and-outreach.md` ·
`leads-content-ads-referrals.md` · `closing-vetting-and-operating.md` · `hormozi-record.md`.

**Standing caution.** Q1 to Q35 ran in one NotebookLM chat, so a framework repeated across answer
files is one retelling, not independent confirmation. Pass 2 has not passed Christian's review
gate.

---

## Names that are not his, or not in the sources

These names show up in questions or answer headings. Indexing them as his frameworks would have a
reader cite a construct the sources do not hold. Each home section says so in its first line.

| Name | What the sources hold instead | Prov | Home |
|---|---|---|---|
| "Gasp" test for price | "stings a little" and the Kennedy "without cracking a smile" epigraph | [A] | `pricing-and-tiers.md` § Premium pricing: the "gasp" test |
| Three-tier pyramid (premium anchor, middle, entry) | one offer, buyers ascended; q68 and q15 find no menu (Pass 2 §4 row 8) | [A] | `pricing-and-tiers.md` § Tiers: the three-tier pyramid is not his; `closing-vetting-and-operating.md` § Tiers: no three-tier menu, enter at the top |
| "Magnetic middle" tier | nothing | [A] | `pricing-and-tiers.md` § Tiers: the three-tier pyramid is not his |
| Add value, change terms, fence the offer | adding a bonus is his; terms appear as delayed payment and layaway; fencing as deadline promotions | [A] | `pricing-and-tiers.md` § Discounting: add value, change terms, fence the offer |
| Price-rise letter to existing customers | the pipeline notice to prospects | [A] | `pricing-and-tiers.md` § Raising prices: a letter to existing customers |
| Rule that a name states result and time | MAGIC components are optional, pick 3 to 5 | [A] | `bonuses-and-naming.md` § MAGIC naming: result plus time is not a rule |
| "Exactly five" free clients | "The exact number matters less" | [A] | `free-work-trials-and-first-customers.md` § First five free: the number and why |
| Half-price start or half-price first month | the step-up ladder and free with commitment | [A] | `free-work-trials-and-first-customers.md` § Half-price start and discounted first period |
| Price for a paid audit | only free or discounted diagnostics | [A] | `free-work-trials-and-first-customers.md` § Paid audit: what he says |
| "Paid pilot" | the question's label; no source uses it | [A] | `free-work-trials-and-first-customers.md` § First offer to a new customer: five structures |
| Sample size and pass mark for testing an offer | the 100-offers line and 2 to 3 wrappers per campaign | [A] | `bonuses-and-naming.md` § Testing: sample size and pass mark |
| "You don't need a new offer, you need trust" | a heading in q54 and q55, never quoted as his | [A] | `closing-vetting-and-operating.md` § Trust: proof beats promise |
| Delivery vehicle by price table | two loose rules only | [A] | `offer-construction.md` § Delivery vehicles: which vehicle for which price |
| Free bonuses given before purchase | the sales-call moment against the after-sign-up reveal | [A] | `bonuses-and-naming.md` § Bonus: free bonuses given before purchase |
| A full launch with dates and numbers | separate pieces only; Money Models may hold one | [A] | `scarcity-and-urgency.md` § Launch: a full launch with dates and numbers |
| Free work for local B2B services | B2C fitness and B2B to gym owners only | [A] | `free-work-trials-and-first-customers.md` § Free work for local B2B services |
| Selling a guarantee as a paid item | outsized guarantees carry an explicit dollar value | [A] | `guarantees.md` § Guarantee: why it works |
| Speed of closing inside a call | speed to lead instead | [A] | `closing-vetting-and-operating.md` § Speed to lead and close-rate numbers |

---

## Value equation

| Name | What it is | Type | Prov | Home |
|---|---|---|---|---|
| Value equation | Value = (Dream Outcome × Perceived Likelihood of Achievement) / (Time Delay × Effort and Sacrifice) | FRM | [D] | `value-equation.md` § Value equation: the formula and its four drivers |
| Father's four questions | "What will I make?", "How will I know it's going to happen?", "How long will it take?", "What is expected of me?"; one per driver | BIO | [M*] | `value-equation.md` § Value equation: his father's four questions |
| Lazy top side, winning bottom side | bigger claims are lazy; world-class firms cut time delay and effort | PRN | [M*] | `value-equation.md` § Value equation: lazy top side, winning bottom side |
| Psychological over logical solutions | London Underground map, elevator mirrors, train hosts | MEC | [M*] | `value-equation.md` § Value equation: psychological solutions over logical ones |
| Meditation versus Xanax scoring | score each driver 0 to 1, then sum | NUM | [M*] | `value-equation.md` § Value equation: Meditation versus Xanax scoring |
| Three core markets: Health, Wealth, Relationships | every enduring market hooks into one | FRM | [M*] | `value-equation.md` § Dream outcome: how to choose it; `offer-construction.md` § Market: niche slapping |
| Dream outcome: four rules | channel existing desire; sell the destination, not the plane flight; anchor in a core market; aim at universal desires | FRM | [M*] | `value-equation.md` § Dream outcome: how to choose it |
| Status and the viewpoint of others | frame benefits as other people will see them; golf club script | FRM | [M*] | `value-equation.md` § Dream outcome: status and the viewpoint of others |
| Weak against strong dream outcome | "Lose 20 lbs in 6 weeks" over "$99/month boot camp" | NUM | [M*] | `value-equation.md` § Dream outcome: weak against strong examples |
| Surgeon test | the 10,000th patient pays more for identical work | PRN | [M*] | `value-equation.md` § Perceived likelihood: definition and the surgeon test |
| Perceived likelihood tools | q04 five tools; q01 six items | FRM | [M*] | `value-equation.md` § Perceived likelihood: tools to raise it |
| DIY, DWY, DFY | effort levels; moving toward DFY raises likelihood and cuts effort | FRM | [M*] | `value-equation.md` § Perceived likelihood: tools to raise it; `value-equation.md` § Time delay and effort: techniques to cut them; `offer-construction.md` § Delivery vehicles: the delivery cube |
| Long-term outcome and short-term wins | buy the dream, stay for early wins | FRM | [M*] | `value-equation.md` § Time delay: long-term outcome and short-term wins |
| Fast beats free | only speed beats free | PRN | [D] | `value-equation.md` § Time delay: fast beats free |
| Four techniques to cut delay and effort | vehicle shift; psychological levers; one-to-many assets; remove one-thing objections | FRM | [M*] | `value-equation.md` § Time delay and effort: techniques to cut them |
| Eating Out Guide | one lost sale turned into a permanent bonus | BIO | [M*] | `value-equation.md` § Time delay and effort: techniques to cut them; `hormozi-record.md` § Weight-loss programme: the eating-out objection |
| Bonuses move three drivers | effort and delay toward 0, likelihood up | MEC | [M*] | `bonuses-and-naming.md` § Bonus: how bonuses change the value equation |

---

## Market and niche

| Name | What it is | Type | Prov | Home |
|---|---|---|---|---|
| Starving crowd | demand beats offer quality, price and location | MEC | [M*] | `offer-construction.md` § Market: the starving crowd |
| Market over offer over persuasion | Great overpowers lower, Normal passes on, Bad halts | FRM | [M*] | `offer-construction.md` § Market: ranking market over offer over persuasion; `bonuses-and-naming.md` § Enhancing: is it the offer, the traffic or the sales process |
| Four market criteria | Massive pain, Purchasing power, Easy to target, Growing; "the pain is the pitch" | FRM | [M*] | `offer-construction.md` § Market: the four criteria; `closing-vetting-and-operating.md` § Vetting: four market qualifications |
| Dying market (Lloyd) | contraction beats product, zero-risk offer and sales; origin `[A]` | WRN | [M*] | `offer-construction.md` § Market: dying market, the Lloyd story |
| Niche slapping | switching markets after one failure resets learning to zero | WRN | [M*] | `offer-construction.md` § Market: niche slapping; `closing-vetting-and-operating.md` § Service business: picking a niche and staying in it |
| $10 million rule, micro-niching | stay tight until the TAM caps out | NUM | [M*] | `offer-construction.md` § Market: the $10 million rule and micro-niching |
| Niche price ladder | $19 to $1,997 for the same content; credited to Dan Kennedy; origin `[A]` | NUM | [M*] | `pricing-and-tiers.md` § Niche price ladder: time management $19 to $1,997 |
| 3Ps of niche selection | a Pain you overcame, a Passion, a Profession | FRM | [M*] | `closing-vetting-and-operating.md` § Service business: picking a niche and staying in it; `leads-content-ads-referrals.md` § Sweep: frameworks q65 names that sit outside the offer lanes |

---

## Offer construction

| Name | What it is | Type | Prov | Home |
|---|---|---|---|---|
| Grand Slam Offer | promotion, unmatchable value, premium price, unbeatable guarantee, money model | FRM | [M*] | `offer-construction.md` § Offer: definition and the grand slam offer |
| Irresistible price | a premium price far below perceived value, not a discount | PRN | [M*] | `offer-construction.md` § Offer: definition and the grand slam offer; `pricing-and-tiers.md` § Premium pricing: the 10x value-to-price gap |
| "So good they feel stupid saying no" | his mentor TJ's line | SCR | [D] | `offer-construction.md` § Offer: "so good they feel stupid saying no"; `closing-vetting-and-operating.md` § Offer as the main lever: the $10K versus $10M offer |
| Listing every problem | dream outcome, every obstacle in time order, "How to..." reversal, name each solution | FRM | [M*] | `offer-construction.md` § Problems: listing every problem |
| Four-driver filter | each obstacle phrased as the buyer's doubt per driver | FRM | [M*] | `offer-construction.md` § Problems: the four-driver filter |
| Problem-to-solution conversions | seven weight-loss stages turned into "How to..." lines | SCR | [M*] | `offer-construction.md` § Problems: weight-loss problem-to-solution conversions |
| Delivery cube | attention ratio, effort level, live medium, recorded format, speed, 10x test | FRM | [M*] | `offer-construction.md` § Delivery vehicles: the delivery cube |
| 10x and 1/10th test | what you would deliver at 10x the price, and at 1/10th | FRM | [M*] | `offer-construction.md` § Delivery vehicles: the 10x and 1/10th test |
| Sales-to-fulfillment continuum | easy to sell is hard to fulfil, and the reverse | MEC | [M*] | `offer-construction.md` § Delivery vehicles: sales-to-fulfillment continuum |
| Create flow, monetize flow, add friction | q33's "friction flow threshold"; the 33 gyms and 8 a month are `[D]` | PRN | [M*] | `offer-construction.md` § Delivery vehicles: create flow, monetize flow, add friction; `free-work-trials-and-first-customers.md` § Front end: create flow, monetise flow, then add friction |
| Trim and stack: four buckets | cost to you against value to them; drop, keep, convert, double down | FRM | [M*] | `offer-construction.md` § Trim and stack: the four cost-value buckets |
| Trim and stack: building the stack | bundle, name, price each item, sum; valuation method `[A]` | FRM | [M*] | `offer-construction.md` § Trim and stack: building the stack |
| Weight-loss stack | seven named items, "Total value $4,351, all for only $599" | NUM | [D] | `offer-construction.md` § Weight-loss stack: every item and value; `bonuses-and-naming.md` § Bonus stack: the weight-loss offer, $4,351 for $599 |
| Offer creation process | four tellings: q11 six steps, q02 four, q12 eight, q25 launch order | FRM | [M*] | `offer-construction.md` § Offer creation: the full process in order |
| Five enhancers | scarcity, urgency, bonuses, guarantees, MAGIC naming | FRM | [M*] | `offer-construction.md` § Offer creation: the five enhancers |
| 10/10 offer checklist | video version: add scarcity, urgency, bonuses, guarantees | FRM | [M*] | `hormozi-record.md` § What changed between the books and the videos |
| $10K versus $10M offer | six differences (q48; its diagram shows four) | FRM | [M*] | `closing-vetting-and-operating.md` § Offer as the main lever: the $10K versus $10M offer |
| Need-to-believes | limit the beliefs a buyer must hold to 1 or 0 | PRN | [M*] | `hormozi-record.md` § Prestige Labs: the supplement affiliate model; `closing-vetting-and-operating.md` § Offer as the main lever: the $10K versus $10M offer |
| Four product criteria | Unique, Expensive, Sticky, Air | FRM | [M*] | `leads-content-ads-referrals.md` § Sweep: frameworks q65 names that sit outside the offer lanes |

---

## Pricing and tiers

| Name | What it is | Type | Prov | Home |
|---|---|---|---|---|
| Profit, not customers | race to the bottom; Kennedy's "no strategic benefit to being the second cheapest" | PRN | [M*] | `pricing-and-tiers.md` § Premium pricing: profit, not customers |
| Vicious cycle of lowering prices | five steps from less investment to destroyed margins | MEC | [M*] | `pricing-and-tiers.md` § Premium pricing: the vicious cycle of lowering prices |
| Virtuous cycle of raising prices | five steps, the mirror | MEC | [M*] | `pricing-and-tiers.md` § Premium pricing: the virtuous cycle of raising prices; `closing-vetting-and-operating.md` § Raising prices: the virtuous cycle and the wine study |
| "Those who pay the most pay the most attention" | price forces adherence where the client does the work | MEC | [M*] | `pricing-and-tiers.md` § Premium pricing: those who pay the most pay the most attention |
| Wine study | three identical wines, prices visible, not blind | MEC | [D] | `pricing-and-tiers.md` § Premium pricing: the wine study; `closing-vetting-and-operating.md` § Raising prices: the virtuous cycle and the wine study |
| Customer at each price level | low-price buyer against high-price buyer | PRN | [M*] | `pricing-and-tiers.md` § Premium pricing: the customer at each price level |
| 10x value-to-price gap | Buffett's "Price is what you pay, value is what you get" | PRN | [M*] | `pricing-and-tiers.md` § Premium pricing: the 10x value-to-price gap |
| Quantifiable ROI rule | charge a fraction of the return produced | PRN | [M*] | `pricing-and-tiers.md` § Premium pricing: the 10x value-to-price gap |
| "If I made you $239,000 extra" | his answer to his father | SCR | [M*] | `pricing-and-tiers.md` § Pricing script: "If I made you $239,000 extra" |
| Say it out loud, it stings a little | Kennedy epigraph in Offers p2, not his instruction | PRN | [M*] | `pricing-and-tiers.md` § Premium pricing: say it out loud, it stings a little |
| Copycat pricing, commodity trap | "a little more for a little less" | WRN | [M*] | `pricing-and-tiers.md` § Premium pricing: copycat pricing and the commodity trap |
| Category of one | priced far above market, cannot be compared | PRN | [M*] | `pricing-and-tiers.md` § Premium pricing: conviction and the category of one |
| Anchoring | anchor the core then stack; an elite tier as anchor | MEC | [M*] | `pricing-and-tiers.md` § Anchoring: what the sources hold |
| Fractal 80/20 | 20% will pay 5x to 10x | MEC | [M*] | `pricing-and-tiers.md` § Tiers: 20% will pay 5x to 10x; `scarcity-and-urgency.md` § Scarcity: fractal 80/20 demand math |
| Ascension | enter on a front end, climb to the back end; 35% upsell `[D]` | FRM | [M*] | `pricing-and-tiers.md` § Tiers: ascension and the tier-upgrade bonus |
| Enter at the top, start high-touch | Tesla Roadster first; 100 clients at $10,000 | PRN | [M*] | `closing-vetting-and-operating.md` § Tiers: no three-tier menu, enter at the top |
| Gym Lords | the 3-year back-end tier | CLM | [D] | `pricing-and-tiers.md` § Pricing case: Gym Launch $16,000 intensive and the $42,000 upsell; `hormozi-record.md` § Gym Launch pricing: $16,000 front end and the $42,000 back end |
| Commodity agency retainer | "Pay us to work. We do work. Maybe you get results" | WRN | [M*] | `pricing-and-tiers.md` § Agency offer: the standard retainer is a commodity |
| Pay-for-performance agency script | "Pay one time, no recurring fee..."; the 20-people guarantee origin `[A]` | SCR | [M*] | `pricing-and-tiers.md` § Agency offer: the pay-for-performance script; `guarantees.md` § Performance pricing script: pay one time, 20 people or next month free |
| Agency offer math | one $10,000 ad spend, commodity against grand slam | NUM | [M*] | `pricing-and-tiers.md` § Agency offer math: $10,000 ad spend, commodity against grand slam; `closing-vetting-and-operating.md` § Offer as the main lever: the agency split test |
| Jump anchor | anchor above the target, split it, offer a prepay | FRM | [M*] | `closing-vetting-and-operating.md` § Jump anchor: raising price without losing sales |
| Van Westendorp's four price questions | a standard research method he teaches | SCR | [M*] | `closing-vetting-and-operating.md` § Van Westendorp: four price questions |
| Worst-month pricing | price recurring offers to the client's worst month | CLM | [M*] | `closing-vetting-and-operating.md` § Raising prices: tripling on existing members and pricing to the worst month |
| SMB dead zone | $1,500 to $3,000/month churns fast; origin `[A]` | WRN | [M*] | `closing-vetting-and-operating.md` § Service business: the SMB dead zone; `leads-content-ads-referrals.md` § Sweep: numbers q66 gives as rules |

---

## Discounting, payment terms and price rises

| Name | What it is | Type | Prov | Home |
|---|---|---|---|---|
| Never discount the core offer | keep price fixed, stack bonuses or change terms | PRN | [M*] | `pricing-and-tiers.md` § Discounting: never discount the core offer; `bonuses-and-naming.md` § Bonus: never discount the core instead; `closing-vetting-and-operating.md` § Objections about price: add a bonus, never discount |
| 1-on-1 sequence instead of a discount | full price first, reveal bonuses after yes, add a bonus on hesitation | FRM | [M*] | `pricing-and-tiers.md` § Discounting: the 1-on-1 sequence used instead of a discount |
| Bonus close, the matching close | "Tell you what... Sound fair enough?" | SCR | [M*] | `pricing-and-tiers.md` § Discounting script: the bonus close; `bonuses-and-naming.md` § Bonus script: the matching close |
| Promotional discount as the hook | discount in the name, never at close; action-taker scripts | SCR | [M*] | `pricing-and-tiers.md` § Discounting: promotional discount as the marketing hook |
| Pipeline notice | tell every lead the price rises on a date | FRM | [M*] | `pricing-and-tiers.md` § Raising prices: clean the pipeline first; `scarcity-and-urgency.md` § Urgency: pricing deadline, the pipeline clean-out; `closing-vetting-and-operating.md` § Raising prices: anchoring and the pipeline notice |
| Capacity cap and account squeeze | raise price on each opening, replace low-margin accounts | FRM | [M*] | `pricing-and-tiers.md` § Raising prices: capacity cap and account squeeze |
| Tripling on existing members | $99 to $299/month, revenue doubled | CLM | [M*] | `closing-vetting-and-operating.md` § Raising prices: tripling on existing members and pricing to the worst month |
| 50% discount threshold | below 50% a discount rarely changes behaviour | NUM | [M*] | `free-work-trials-and-first-customers.md` § Half-price start and discounted first period; `leads-content-ads-referrals.md` § Sweep: numbers q66 gives as rules |
| Large down payment and layaway | a third down or $9,000 before delivery; layaway if they cannot pay | NUM | [M*] | `free-work-trials-and-first-customers.md` § First payment: large down payment and layaway |

---

## Guarantees

| Name | What it is | Type | Prov | Home |
|---|---|---|---|---|
| Guarantee formula | "If you do not achieve [X result] in [Y timeframe], we will [Z remedy]" | FRM | [M*] | `guarantees.md` § Guarantee: the formula |
| Why a guarantee works | moves risk to the seller; reverse what they desperately do not want | MEC | [M*] | `guarantees.md` § Guarantee: why it works |
| Four guarantee types | unconditional, conditional, anti, implied | FRM | [D] | `guarantees.md` § Guarantee: the four types |
| Unconditional guarantee | money back for any reason in a set period | FRM | [M*] | `guarantees.md` § Guarantee type: unconditional |
| Conditional guarantee | remedy depends on actions the client completes | FRM | [M*] | `guarantees.md` § Guarantee type: conditional |
| Conditional sub-types, a to h | buyback, service, modified service, credit, personal 1-on-1, delayed second payment, ancillary cost, wage | FRM | [M*] | `guarantees.md` § Guarantee: conditional sub-types |
| Conditional service guarantee | "We will fill your gym in 30 days..." or keep working free | SCR | [M*] | `guarantees.md` § Guarantee: conditional service guarantee, Gym Launch |
| Anti-guarantee | all sales final, with a reason why | FRM | [M*] | `guarantees.md` § Guarantee type: anti-guarantee |
| Implied guarantee | the pay structure is the guarantee | FRM | [M*] | `guarantees.md` § Guarantee type: implied (performance pricing) |
| Eleven named variations | book list; the videos group them into the four types | CLM | [M*] | `hormozi-record.md` § What changed between the books and the videos |
| Vivid-imagery names | "Club a Baby Seal Guarantee"; shark-infested waters | SCR | [M*] | `guarantees.md` § Guarantee naming: vivid imagery |
| "Fully informed decision" | Jason Fladlien's words, not his | SCR | [M*] | `guarantees.md` § Guarantee script: Fladlien's "fully informed decision" |
| Stacking two guarantees | unconditional 30-day plus conditional 90-day | FRM | [M*] | `guarantees.md` § Guarantee: stacking two guarantees |
| Matching type to offer level | low-ticket B2C unconditional; high-ticket B2B conditional or anti | PRN | [M*] | `guarantees.md` § Guarantee: matching the type to the offer level |
| Guarantee math | 100 sales against 130 | NUM | [M*] | `guarantees.md` § Guarantee math: 100 sales against 130 |
| Boot camp "$500 worth of value" | his unconditional guarantee, 2 refunds in 4,000 | CLM | [D] | `guarantees.md` § Guarantee case: boot camp "$500 worth of value", 2 refunds in 4,000; `hormozi-record.md` § Weight-loss boot camp: the $500 guarantee and 2 refunds in 4,000 |
| Best-case, worst-case close | close `[D]`; template wording `[M*]` | SCR | [D] | `guarantees.md` § Guarantee script: best-case, worst-case close; `closing-vetting-and-operating.md` § Best-case, worst-case close |
| $25,000 store buyback | Fladlien's case; origin `[A]` | CLM | [M*] | `guarantees.md` § Guarantee case: Fladlien's $25,000 store buyback |
| When not to use a guarantee | heavy fulfilment, stealable IP, filtering, weak product | WRN | [M*] | `guarantees.md` § Guarantee: when not to use one; `closing-vetting-and-operating.md` § Service business: no unconditional refunds on heavy fulfilment |

---

## Performance pricing

| Name | What it is | Type | Prov | Home |
|---|---|---|---|---|
| Five performance structures | pay-per-result, revenue share, profit share, ratchets and triggers, hybrid | FRM | [M*] | `guarantees.md` § Performance pricing: the five structures |
| Shares, ratchets, floor fees | percentages and three ratchet readings | NUM | [M*] | `guarantees.md` § Performance pricing: share percentages, ratchets and floor fees |
| Gym Launch first turnaround model | "my fee was 100% of the revenue I would bring in" | BIO | [D] | `guarantees.md` § Performance pricing case: Gym Launch's first turnaround model; `hormozi-record.md` § DFY gym launches: 33 gyms, 21 days, paid from the members' cash |
| Performance pricing risks | tracking, dishonesty, dying markets, burnout, no control of the close | WRN | [M*] | `guarantees.md` § Performance pricing: the risks |
| When to avoid or modify it | five conditions | WRN | [M*] | `guarantees.md` § Performance pricing: when to avoid or modify it |

---

## Scarcity

| Name | What it is | Type | Prov | Home |
|---|---|---|---|---|
| Scarcity against urgency | quantity against time; Naval Ravikant's "desire is a contract" | MEC | [M*] | `scarcity-and-urgency.md` § Scarcity and urgency: definitions and why they work |
| Three core scarcity types | seats or slots, bonuses, never available again | FRM | [M*] | `scarcity-and-urgency.md` § Scarcity: the three core types |
| Seven ways to limit supply | q24's seven; q22 groups into five | FRM | [M*] | `scarcity-and-urgency.md` § Scarcity: seven ways to limit supply |
| "Once you're out, never return" | a churn lever filed under scarcity | FRM | [M*] | `scarcity-and-urgency.md` § Scarcity: seven ways to limit supply |
| Physical limited drops | fixed quantity, once a month | NUM | [M*] | `scarcity-and-urgency.md` § Scarcity: physical limited drops |
| Total business cap | "Our agency only services 25 total clients" | SCR | [M*] | `scarcity-and-urgency.md` § Scarcity script: total business cap, 25 clients |
| Weekly growth cap | "We only accept 5 new clients per week" | SCR | [M*] | `scarcity-and-urgency.md` § Scarcity script: weekly growth cap, 5 new clients a week |
| Cohort cap | 100 clients 4 times a year | NUM | [M*] | `scarcity-and-urgency.md` § Scarcity: cohort cap |
| Bonus scarcity | program-exclusive, quantity-capped, first X buyers | SCR | [M*] | `scarcity-and-urgency.md` § Scarcity script: bonus scarcity |
| Lead-magnet scarcity | cap free downloads per week | NUM | [M*] | `scarcity-and-urgency.md` § Scarcity: lead-magnet scarcity |
| Honest capacity, four rules | honest number, always sell out, announce it, resist satisfying all demand; the 81% line `[D]` | FRM | [M*] | `scarcity-and-urgency.md` § Scarcity: honest capacity number and the four rules |
| Fake scarcity and urgency | reset timers, false stock; the "zero-fucks-given vibe" | WRN | [M*] | `scarcity-and-urgency.md` § Fake scarcity and fake urgency: the warning |
| Honest scarcity and urgency rules | deadlines from real events, published real capacity | PRN | [M*] | `scarcity-and-urgency.md` § Honest scarcity and honest urgency: the rules |

---

## Urgency and launch

| Name | What it is | Type | Prov | Home |
|---|---|---|---|---|
| Four urgency types | q23 and q24 both give four, split differently | FRM | [M*] | `scarcity-and-urgency.md` § Urgency: the four types |
| Rolling cohorts | "Our next group starts Monday" | SCR | [M*] | `scarcity-and-urgency.md` § Urgency script: rolling cohorts |
| Rolling seasonal promotions | holiday wrappers with end dates | SCR | [M*] | `scarcity-and-urgency.md` § Urgency script: rolling seasonal promotions |
| Fast-action bonus | "If you buy today... I reward action-takers" | SCR | [M*] | `scarcity-and-urgency.md` § Urgency script: fast-action bonus |
| Exploding opportunity | a time-decaying return | FRM | [M*] | `scarcity-and-urgency.md` § Urgency: exploding opportunity |
| Year-round services rule | tie urgency to the promotion, not to access | PRN | [M*] | `scarcity-and-urgency.md` § Urgency: year-round services tie the deadline to the promotion |
| Last four hours | 50% to 60% of sales at the deadline | NUM | [D] | `scarcity-and-urgency.md` § Urgency: 50% to 60% of sales in the last four hours |
| Launch order of the enhancers | likely the book's chapter order | FRM | [M*] | `scarcity-and-urgency.md` § Launch: order of the enhancers |
| Whisper, tease, shout | three or four steps to a launch date | FRM | [M*] | `scarcity-and-urgency.md` § Launch: the whisper, tease, shout sequence |

---

## Bonuses

| Name | What it is | Type | Prov | Home |
|---|---|---|---|---|
| "But wait, there's more" | anchor the core, stack bonuses until the "rubber band" snaps | MEC | [D] | `bonuses-and-naming.md` § Bonus: why bonuses work, "but wait, there's more"; `pricing-and-tiers.md` § Anchoring: what the sources hold |
| What a bonus should be | low-cost high-value assets; tools over trainings | FRM | [M*] | `bonuses-and-naming.md` § Bonus: what a bonus should be |
| "The One Thing" | one bonus per objection | PRN | [M*] | `bonuses-and-naming.md` § Bonus: one objection per bonus, "the one thing" |
| Total-value rule | stacked bonuses should eclipse the core's value | PRN | [M*] | `bonuses-and-naming.md` § Bonus: how many, and the total-value rule |
| Bonus naming and price tag | benefit title plus a justified dollar value | PRN | [M*] | `bonuses-and-naming.md` § Bonus: naming and the price tag |
| Six-step reveal checklist | title, relate, value impact, proof, future picture, price tag | FRM | [M*] | `bonuses-and-naming.md` § Bonus: the six-step reveal checklist |
| 1-on-1 against group presentation | reveal after the yes; or stack live one by one | FRM | [M*] | `bonuses-and-naming.md` § Bonus: presenting bonuses, 1-on-1 against group |
| OPS and the "Jedi" strategy | partners' products as bonuses, plus a referral commission | FRM | [M*] | `bonuses-and-naming.md` § Bonus: other people's products and services (OPS) |
| Pain-clinic OPS stack | partner bonuses on a $400 offer | NUM | [M*] | `bonuses-and-naming.md` § Bonus stack: the pain-clinic OPS stack on a $400 offer |
| Prestige Labs affiliate bonus | a discount for members, a commission for the gym | BIO | [M*] | `bonuses-and-naming.md` § Bonus case: Prestige Labs supplement affiliate |
| Tier-upgrade bonus | a fixed trial of a higher tier | FRM | [M*] | `bonuses-and-naming.md` § Bonus: the tier-upgrade bonus |

---

## Naming

| Name | What it is | Type | Prov | Home |
|---|---|---|---|---|
| MAGIC | Magnet, Avatar, Goal, Interval, Container; "not all these components are mandatory… typically three to five" | FRM | [D] | `bonuses-and-naming.md` § MAGIC naming: the five components |
| MAGIC: steps to build a name | pick 3 to 5, order for flow, polish, apply to bonuses, test | FRM | [M*] | `bonuses-and-naming.md` § MAGIC naming: steps to build a name |
| Result plus time on ad platforms | a compliance caveat, not a rule | WRN | [M*] | `bonuses-and-naming.md` § MAGIC naming: result plus time is not a rule |
| Rhyme and alliteration names | Six-Pack Fasttrack, Debt Detox | SCR | [M*] | `bonuses-and-naming.md` § Naming examples: rhyme and alliteration |
| Local and wellness names | Free 21-Day Mommy Makeover and others | SCR | [M*] | `bonuses-and-naming.md` § Naming examples: local and wellness businesses |
| Coaching, agency, gym, e-commerce names | Fill Your Gym in 30 Days Free and others | SCR | [M*] | `bonuses-and-naming.md` § Naming examples: coaching, agency, gym, e-commerce |
| Wrapper and container | the name changes response, not fulfilment | MEC | [M*] | `bonuses-and-naming.md` § Naming: the wrapper and the container |
| Before-and-after names, fatigue refreshes | Float Tank Session to Free 6-Week Stress Release Challenge | SCR | [M*] | `bonuses-and-naming.md` § Naming: before-and-after names and fatigue refreshes |

---

## Enhancing and testing an offer

| Name | What it is | Type | Prov | Home |
|---|---|---|---|---|
| Offer, traffic or sales process | three-way diagnosis; "It means your offer sucks" | FRM | [M*] | `bonuses-and-naming.md` § Enhancing: is it the offer, the traffic or the sales process |
| Funnel metrics to watch | response, booking and show, close, upfront cash and ROAS | FRM | [M*] | `bonuses-and-naming.md` § Enhancing: funnel metrics to watch |
| Order to vary a fatigued offer | creative, body copy, wrapper, duration, enhancers, monetisation last | FRM | [M*] | `bonuses-and-naming.md` § Enhancing: order to vary a fatigued offer; `closing-vetting-and-operating.md` § Service business: offer fatigue, change the lightest thing first |
| Wrappers against a control, 100 offers | 2 to 3 contenders, beat the control; a persistence line | FRM | [M*] | `bonuses-and-naming.md` § Testing: wrappers against a control, and 100 offers |
| Local market reach cost | $20 per 1,000 people | NUM | [M*] | `bonuses-and-naming.md` § Testing: local market reach cost, $20 per 1,000 |

---

## Free work and the first five

| Name | What it is | Type | Prov | Home |
|---|---|---|---|---|
| Free work: four reasons | reps, forgiveness, hidden costs, proof | PRN | [M*] | `free-work-trials-and-first-customers.md` § Free work: when he recommends it |
| First five free | "The exact number matters less than knowing why you benefit from it" | PRN | [D] | `free-work-trials-and-first-customers.md` § First five free: the number and why |
| Three terms of exchange | use it, give feedback, leave a killer review | SCR | [D] | `free-work-trials-and-first-customers.md` § First five free: the three terms of exchange |
| 80/60/40/20 step-up | 20 points less discount per batch of five | FRM | [D] | `free-work-trials-and-first-customers.md` § Price step-up after the free five: 80/60/40/20 |
| Raise 20% every five | q53's 5-to-5-to-5 rule; stop when conversion drops | FRM | [D] | `free-work-trials-and-first-customers.md` § Price step-up: raise 20% every five sales |
| Free-to-paid transition script | "Are you comfortable with that?"; if not, ask for the review | SCR | [M*] | `free-work-trials-and-first-customers.md` § Free to paid: the transition script |
| Charity-donation first sale | free work for a donation to the client's charity | BIO | [D] | `free-work-trials-and-first-customers.md` § His first sale: free work for a charity donation; `hormozi-record.md` § First clients free: a year of free training and a charity donation |
| Hidden costs | "Your free stuff is too expensive" | PRN | [D] | `free-work-trials-and-first-customers.md` § Hidden costs: "your free stuff is too expensive" |
| San Diego free case study | free, paid off the sales | CLM | [D] | `free-work-trials-and-first-customers.md` § Free case study paid on results: his San Diego offer; `hormozi-record.md` § San Diego free case study: 213 members and $112,000 |
| Give away what competitors charge for | five steps from competitor price to backend buyers | FRM | [M*] | `free-work-trials-and-first-customers.md` § Giving away what competitors charge for: the 5-step formula |
| 99% rule, give until they ask, legal drug dealer | free must beat competitors' paid | PRN | [M*] | `free-work-trials-and-first-customers.md` § Free content quality: the 99% rule and give until they ask |

---

## Free-offer models, trials and front ends

| Name | What it is | Type | Prov | Home |
|---|---|---|---|---|
| Seven free-offer models | the seven below; names match the Money Models list, not in this layer | FRM | [M*] | `free-work-trials-and-first-customers.md` § Seven free-offer models |
| Free Bribe | a free program for joining a recurring membership | FRM | [M*] | `free-work-trials-and-first-customers.md` § Seven free-offer models |
| Limited Free Offer (A/B close) | a restricted trial upsold at onboarding | FRM | [M*] | `free-work-trials-and-first-customers.md` § Seven free-offer models |
| Free Trial + Penalty (downsell) | card down, penalty for no-shows | FRM | [M*] | `free-work-trials-and-first-customers.md` § Seven free-offer models |
| Free with Deposit (challenge model) | deposit refunded or credited on hitting the goal | FRM | [M*] | `free-work-trials-and-first-customers.md` § Seven free-offer models; `free-work-trials-and-first-customers.md` § Free with deposit: the $500 challenge and refund versus credit |
| Free Forever | free core, required high-margin product | FRM | [M*] | `free-work-trials-and-first-customers.md` § Seven free-offer models |
| Free Giveaway | a contest whose entrants self-identify | FRM | [M*] | `free-work-trials-and-first-customers.md` § Seven free-offer models |
| Free with Commitment | first month free on a long contract | FRM | [M*] | `free-work-trials-and-first-customers.md` § Seven free-offer models |
| When free works and when it fails | five areas; Pass 2 §4 row 12 | WRN | [M*] | `free-work-trials-and-first-customers.md` § When free works and when it fails |
| Against unconditioned free trials | freebie seekers, no skin, slow cash | WRN | [M*] | `free-work-trials-and-first-customers.md` § Free trials: the warning against unconditioned trials |
| Deprivation | give the result free until they depend on it, then stop | MEC | [M*] | `free-work-trials-and-first-customers.md` § Deprivation: four months of free lead generation |
| Small paid starts | 100% affiliate revenue share, "CDs for a penny", quantity downsell, against tripwires | FRM | [M*] | `free-work-trials-and-first-customers.md` § Small paid starts: revenue share, penny offers, quantity downsell |
| First offer: five structures | challenge, DWY intensive, bribe or commitment, A/B close, 5-by-5 escalation | FRM | [M*] | `free-work-trials-and-first-customers.md` § First offer to a new customer: five structures |
| Front-end cash liquidators | the first offer recovers ad cost on day one | PRN | [M*] | `free-work-trials-and-first-customers.md` § Front end: create flow, monetise flow, then add friction; `leads-content-ads-referrals.md` § Paid ads: when to start and what to sell on them |
| Activation points, continuity pitch | upsell at the point of greatest need, not greatest satisfaction | SCR | [M*] | `free-work-trials-and-first-customers.md` § Free or cheap to recurring: activation points and the continuity pitch |

---

## Lead magnets and audits

| Name | What it is | Type | Prov | Home |
|---|---|---|---|---|
| Lead magnet: three types | reveal a problem, samples and trials, one step of a multi-step process | FRM | [M*] | `free-work-trials-and-first-customers.md` § Lead magnet: definition and the three types |
| Lead magnet: four delivery methods | software, information, services, physical products | FRM | [M*] | `free-work-trials-and-first-customers.md` § Lead magnet: the four delivery methods |
| Never solve the core problem | salty pretzel, Costco sampler, legal drug dealer | WRN | [M*] | `free-work-trials-and-first-customers.md` § Lead magnet: never solve the core problem |
| Lead magnet economics | a hard-cost magnet can still cut CAC | NUM | [M*] | `free-work-trials-and-first-customers.md` § Lead magnet economics: cost per engaged lead |
| Audit or problem reveal | a diagnostic for qualified leads; the CAC math | NUM | [M*] | `free-work-trials-and-first-customers.md` § Audit or problem reveal: the CAC math |
| Big Fast Value | lead cold prospects with a narrow problem solved | FRM | [M*] | `leads-and-outreach.md` § Cold outreach: three problems and their fixes |

---

## Core Four and channel order

| Name | What it is | Type | Prov | Home |
|---|---|---|---|---|
| Core Four | warm outreach, free content, cold outreach, paid ads; a 2x2 of audience by path | FRM | [M*] | `leads-and-outreach.md` § Core Four: the four ways to make an offer known |
| Core Four trade-offs | time against money decides the start | MEC | [M*] | `leads-and-outreach.md` § Core Four: trade-offs and which to start with |
| 1-1-1 rule | one offer, one avatar, one channel to $1M; q66 calls it "1-1-1-1" | FRM | [M*] | `leads-and-outreach.md` § 1-1-1 rule: one offer, one avatar, one channel; `closing-vetting-and-operating.md` § Service business: 1-1-1 and the two ways to grow |
| Shiny object syndrome | adding channels before the first works | WRN | [M*] | `leads-and-outreach.md` § 1-1-1 rule: one offer, one avatar, one channel |
| Lead-getting framework | make an offer, pick a channel, scale | FRM | [M*] | `leads-and-outreach.md` § Lead-getting framework: three steps |
| Seven-step channel roadmap | warm first, executives last | FRM | [M*] | `leads-and-outreach.md` § Channel roadmap for a new business, seven steps |
| More, Better, New | scale volume, then conversion, then new placements | FRM | [M*] | `leads-and-outreach.md` § More, Better, New: the scaling order |
| Rule of 100 | 100 advertising actions a day for 100 days | FRM | [M*] | `leads-and-outreach.md` § Rule of 100 |
| First 4 hours and the 444 split | one channel first each day; 4 promote, 4 deliver, 4 build | NUM | [M*] | `leads-and-outreach.md` § First 4 hours and the 444 split |
| 70/20/10 | proven, adjacent, new | FRM | [M*] | `leads-and-outreach.md` § 70/20/10 allocation; `closing-vetting-and-operating.md` § Service business: 70/20/10 and don't break what works |
| Open to goal | work until the outcome count, not the input count | FRM | [M*] | `leads-and-outreach.md` § Open to goal |
| Lead Getters | customers, employees, agencies, affiliates | FRM | [M*] | `leads-content-ads-referrals.md` § Lead Getters: customers, employees, agencies, affiliates |

---

## Warm and cold outreach

| Name | What it is | Type | Prov | Home |
|---|---|---|---|---|
| Warm list building | email, social and phone contacts | FRM | [M*] | `leads-and-outreach.md` § Warm outreach: building the list |
| Warm outreach 10 steps | two versions, q40 and q52 | FRM | [M*] | `leads-and-outreach.md` § Warm outreach: the 10 steps (two versions) |
| Warm opener | "Hey [Name], saw you just..." | SCR | [M*] | `leads-and-outreach.md` § Warm outreach: the opener |
| ACA | Acknowledge, Compliment, Ask | FRM | [M*] | `leads-and-outreach.md` § ACA: Acknowledge, Compliment, Ask |
| Referral-framed offer | "Does anyone you like come to mind?"; "does anyone you hate come to mind?" | SCR | [M*] | `leads-and-outreach.md` § Warm outreach: the referral-framed offer ("does anyone you hate come to mind") |
| Cold outreach: three problems | no contact info, ignored, not trusted | FRM | [M*] | `leads-and-outreach.md` § Cold outreach: three problems and their fixes |
| Cold calls, DMs, email | reading level "clear, not clever" | FRM | [M*] | `leads-and-outreach.md` § Cold outreach: calls, DMs and email |
| Cold email or DM template | opener, body, offer, ask; possibly NotebookLM's assembly | SCR | [M*] | `leads-and-outreach.md` § Cold outreach: email or DM template |
| Follow-up cadence, 3x3 | multi-touch, multi-channel | NUM | [M*] | `leads-and-outreach.md` § Follow-up: multi-touch, multi-channel, and the cadence |
| LTGP to CAC | lifetime gross profit over acquisition cost | NUM | [M*] | `leads-and-outreach.md` § LTGP to CAC: the ratio targets |
| Speed to lead, the "maniac" | call within 60 seconds; a rep who only calls new leads | NUM | [M*] | `leads-and-outreach.md` § Engaging leads: speed to lead and the "maniac" caller; `closing-vetting-and-operating.md` § Speed to lead and close-rate numbers |

---

## Content, ads, referrals, affiliates and staff

| Name | What it is | Type | Prov | Home |
|---|---|---|---|---|
| Content pillar, five topic categories | far past, recent past, present, trending, manufactured | FRM | [M*] | `leads-content-ads-referrals.md` § Content: topics, framing and the pillar |
| Document, don't manufacture; "How I", not "How To" | talk about what you did | PRN | [M*] | `leads-content-ads-referrals.md` § Content: topics, framing and the pillar |
| Hook formula | Proof + Promise + Plan, sometimes Picture + Pain | FRM | [M*] | `leads-content-ads-referrals.md` § Content: hooks, headlines and callouts |
| Seven headline elements | Recency, Relevancy, Celebrity/Authority, Proximity, Conflict, Unusual, Ongoing | FRM | [M*] | `leads-content-ads-referrals.md` § Content: hooks, headlines and callouts |
| Callouts | labels, yes questions, if-then, ridiculous results; contrast, likeness | FRM | [M*] | `leads-content-ads-referrals.md` § Content: hooks, headlines and callouts |
| Hook, Retain, Reward | the content unit | FRM | [M*] | `leads-content-ads-referrals.md` § Content: hooks, headlines and callouts |
| Give-to-ask ratio | 3.5:1; three readings | NUM | [M*] | `leads-content-ads-referrals.md` § Content: give-to-ask ratio and the path to a customer |
| Integrated and Intermittent Asks | CTAs inside long-form or after a run of value posts | FRM | [M*] | `leads-content-ads-referrals.md` § Content: give-to-ask ratio and the path to a customer |
| Ad testing budget and kill rule | spend to 2x 30-day cash; kill at 1x with zero leads | NUM | [M*] | `leads-content-ads-referrals.md` § Paid ads: testing and scaling budgets |
| Target monthly spend | (Desired Customers × CAC) × 1.20 | NUM | [M*] | `leads-content-ads-referrals.md` § Paid ads: testing and scaling budgets |
| Client-financed acquisition | 30-day payback recycles ad spend | NUM | [M*] | `leads-content-ads-referrals.md` § Paid ads: testing and scaling budgets |
| Goodwill | Value − Price = Goodwill | FRM | [M*] | `leads-content-ads-referrals.md` § Customer referrals: goodwill, incentives and scripts |
| "Not IF, but WHO" | the checkout referral ask | SCR | [M*] | `leads-content-ads-referrals.md` § Customer referrals: goodwill, incentives and scripts |
| Hinge method | a 3-way text introduction | SCR | [M*] | `leads-content-ads-referrals.md` § Customer referrals: goodwill, incentives and scripts |
| Referral growth equation | % monthly referrals − % monthly churn = % monthly compounding growth | FRM | [M*] | `leads-content-ads-referrals.md` § Customer referrals: goodwill, incentives and scripts |
| Affiliate 3-tier payout | 25%, 50%, 100% of CAC by stage | FRM | [M*] | `leads-content-ads-referrals.md` § Affiliates: qualifying, payout tiers and offers |
| "Peel off a piece"; minimum order line | affiliate offer scripts | SCR | [M*] | `leads-content-ads-referrals.md` § Affiliates: qualifying, payout tiers and offers |
| Three affiliate integration strategies | give the magnet, sell the magnet, sell the core | FRM | [M*] | `leads-content-ads-referrals.md` § Affiliates: qualifying, payout tiers and offers |
| 3Ds | Document, Demonstrate, Duplicate | FRM | [M*] | `leads-content-ads-referrals.md` § Employees for lead generation; `closing-vetting-and-operating.md` § Delegation: 3 Ds and authority to match responsibility |
| Fewer, better; mindset swaps; time audit | hiring for lead generation | FRM | [M*] | `leads-content-ads-referrals.md` § Employees for lead generation |
| Agency trap, hire to learn | pay to learn, then replace | WRN | [M*] | `leads-content-ads-referrals.md` § Agencies: the trap and hire-to-learn |

---

## Closing and objections

| Name | What it is | Type | Prov | Home |
|---|---|---|---|---|
| CLOSER | Clarify, Label, Overview past pain, Sell the vacation, Explain away concerns, Reinforce | FRM | [M*] | `closing-vetting-and-operating.md` § CLOSER: the six-step sales conversation |
| BAMFAM | Book A Meeting From A Meeting | FRM | [M*] | `closing-vetting-and-operating.md` § CLOSER: the six-step sales conversation |
| Pain cycle, rubber band | poking past pain stretches deprivation | MEC | [M*] | `closing-vetting-and-operating.md` § CLOSER: the six-step sales conversation |
| 3A | Acknowledge, Associate, Ask; q65 says "Attack", same meaning | FRM | [M*] | `closing-vetting-and-operating.md` § 3A: Acknowledge, Associate, Ask |
| Be like smoke, third party, universal probe | never argue; "What are you most afraid of having happen?" | SCR | [M*] | `closing-vetting-and-operating.md` § Objections: never argue, use a third party, probe the fear |
| Price objection bonus | add a bonus, never discount | SCR | [M*] | `closing-vetting-and-operating.md` § Objections about price: add a bonus, never discount |

---

## Trust and vetting

| Name | What it is | Type | Prov | Home |
|---|---|---|---|---|
| Proof beats promise | one result with 11,000 reviews beats four with one | PRN | [M*] | `closing-vetting-and-operating.md` § Trust: proof beats promise |
| Damaging admission | [Bad Thing] + But + [Good Thing] | FRM | [M*] | `closing-vetting-and-operating.md` § Trust: damaging admissions, the flash roll and proof walls |
| Flash roll | name problems they have not met and how you solved them | FRM | [M*] | `closing-vetting-and-operating.md` § Trust: damaging admissions, the flash roll and proof walls |
| Proof up to your eyeballs | proof walls in $1 frames | FRM | [M*] | `closing-vetting-and-operating.md` § Trust: damaging admissions, the flash roll and proof walls |
| When to add qualification | only when capacity is maxed or ticket size is the goal | PRN | [M*] | `closing-vetting-and-operating.md` § Vetting: when to add qualification |
| Five levers for lead quality | targeting, steps, offer, application, value first | FRM | [M*] | `closing-vetting-and-operating.md` § Vetting: five levers for lead quality |
| Qualifier scripts | the Gym Launch ad line; the minimum-spend question | SCR | [M*] | `closing-vetting-and-operating.md` § Vetting: qualifier scripts |
| Vetting inside the funnel | remove bonuses freebie seekers love; dropdowns; event segments | FRM | [M*] | `closing-vetting-and-operating.md` § Vetting inside the funnel and at events |

---

## Service business and operating

| Name | What it is | Type | Prov | Home |
|---|---|---|---|---|
| Two ways to grow; three ways | more customers or higher LTV; q65 gives three | FRM | [M*] | `closing-vetting-and-operating.md` § Service business: 1-1-1 and the two ways to grow |
| Do it by hand, pre-sell, productise | learn friction by hand, sell before building | PRN | [M*] | `closing-vetting-and-operating.md` § Service business: do it by hand, pre-sell, then productise |
| Gatorade or shot glass | keep the founder's concentrate, serve small groups | PRN | [M*] | `closing-vetting-and-operating.md` § Service business: do it by hand, pre-sell, then productise |
| The Swamp | $1M to $3M margin squeeze | NUM | [M*] | `closing-vetting-and-operating.md` § Service business: the Swamp and scaling bands |
| Discretionary budget | staff may spend to fix a customer issue without sign-off | NUM | [M*] | `closing-vetting-and-operating.md` § Delegation: 3 Ds and authority to match responsibility |
| TEAM | a partner brings Time, Expertise, Assets or Money | WRN | [M*] | `closing-vetting-and-operating.md` § Partners: TEAM and never carry 100% of the risk; `leads-content-ads-referrals.md` § Sweep: frameworks q65 names that sit outside the offer lanes |
| Nail it before you scale it, vacation test | location #1 runs without you first | FRM | [M*] | `closing-vetting-and-operating.md` § Local business: location rules and the pre-sale test |
| Pre-sale market test | ads across candidate zip codes before a lease | FRM | [M*] | `closing-vetting-and-operating.md` § Local business: location rules and the pre-sale test |
| Three pillars of a business | Acquisition, Delivery, Operations | FRM | [M*] | `leads-content-ads-referrals.md` § Sweep: frameworks q65 names that sit outside the offer lanes |
| Management diamond | Knowledge, Skill, Timeline, Motivation, External blockers | FRM | [M*] | `leads-content-ads-referrals.md` § Sweep: frameworks q65 names that sit outside the offer lanes |
| Four Rs of customer success | Retain, Review, Refer, Resell, in order | FRM | [M*] | `leads-content-ads-referrals.md` § Sweep: frameworks q65 names that sit outside the offer lanes |
| What, Who, When | ad copy: value and hidden costs, status, time frames | FRM | [M*] | `leads-content-ads-referrals.md` § Sweep: frameworks q65 names that sit outside the offer lanes |
| Four elements of equity | Control, Risk, Profits, Sale or Enterprise Value | FRM | [M*] | `leads-content-ads-referrals.md` § Sweep: frameworks q65 names that sit outside the offer lanes |
| Three buckets for reinvesting profit | more customers, higher LTV, less risk | FRM | [M*] | `leads-content-ads-referrals.md` § Sweep: frameworks q65 names that sit outside the offer lanes |
| Giving flywheel | give free, earn trust, monetise the top 1% through equity | BIO | [M*] | `hormozi-record.md` § Acquisition.com: the giving flywheel and the refused consulting days |
| Processor as a single point of failure | keep buffers, split processing | BIO | [D] | `hormozi-record.md` § Christmas Eve: the payment processor hold |

---

## Constructs that belong to someone else

He cites or teaches these. The source names the owner, and the provenance column still carries the corpus marker.

| Name | Owner | Prov | Home |
|---|---|---|---|
| "No strategic benefit to being the second cheapest" | Dan Kennedy | [M*] | `pricing-and-tiers.md` § Premium pricing: profit, not customers |
| "Charge as high a price as you can say out loud without cracking a smile" | Dan Kennedy, an epigraph | [M*] | `pricing-and-tiers.md` § Premium pricing: say it out loud, it stings a little |
| Niche price ladder | credited to Dan Kennedy | [M*] | `pricing-and-tiers.md` § Niche price ladder: time management $19 to $1,997 |
| "Make people an offer so good they would feel stupid saying no" | TJ, his mentor | [D] | `offer-construction.md` § Offer: "so good they feel stupid saying no" |
| "Price is what you pay, value is what you get" | Warren Buffett | [M*] | `pricing-and-tiers.md` § Premium pricing: the 10x value-to-price gap |
| "Desire is a contract you make with yourself to be unhappy" | Naval Ravikant | [M*] | `scarcity-and-urgency.md` § Scarcity and urgency: definitions and why they work |
| "Fully informed decision" script and the $25,000 store buyback | Jason Fladlien | [M*] | `guarantees.md` § Guarantee script: Fladlien's "fully informed decision"; `guarantees.md` § Guarantee case: Fladlien's $25,000 store buyback |
| Free Bribe example ($12,000 of courses for a $397/month newsletter) | Frank Kern | [M*] | `free-work-trials-and-first-customers.md` § Seven free-offer models |
| Four price questions | Van Westendorp | [M*] | `closing-vetting-and-operating.md` § Van Westendorp: four price questions |
| Five levels of awareness | Eugene Schwartz | [M*] | `leads-content-ads-referrals.md` § Sweep: frameworks q65 names that sit outside the offer lanes |
| Maker versus manager | Paul Graham | [M*] | `leads-content-ads-referrals.md` § Sweep: frameworks q65 names that sit outside the offer lanes |
| Entrepreneur life cycle | Kelley and Conner | [M*] | `leads-content-ads-referrals.md` § Sweep: frameworks q65 names that sit outside the offer lanes |
| Price's Law | Derek de Solla Price | [M*] | `leads-content-ads-referrals.md` § Sweep: numbers q66 gives as rules |
| Wine study | an outside study, not named | [D] | `pricing-and-tiers.md` § Premium pricing: the wine study |
| Speed-to-lead 391% | likely an industry statistic, no source | [M*] | `leads-and-outreach.md` § Engaging leads: speed to lead and the "maniac" caller |

---

## Lists whose count differs by file

A reader who quotes "the N steps" should check which file's N. None of these counts is matched to
audio except the four guarantee types and MAGIC's optional components.

| List | Counts by file | Home |
|---|---|---|
| Perceived likelihood tools | q04 five tools; q01 six items | `value-equation.md` § Perceived likelihood: tools to raise it |
| Techniques to cut delay and effort | q05 four; q07 four with different members | `value-equation.md` § Time delay and effort: techniques to cut them |
| Delivery cube | q09 six levers; q11 four plus the 10x test; q07 three axes | `offer-construction.md` § Delivery vehicles: the delivery cube |
| Market-offer-persuasion cases | three in most files; q08 adds a fourth (Lloyd) | `offer-construction.md` § Market: ranking market over offer over persuasion |
| Offer creation process | q11 six; q02 four; q12 eight; q25 six | `offer-construction.md` § Offer creation: the full process in order |
| Guarantee types | four in the book `[D]`; three in q02 and q11; eleven named variations in the book; eight sub-types (a to h) in q18 and q19 | `guarantees.md` § Guarantee: the four types; `hormozi-record.md` § What changed between the books and the videos |
| Scarcity types | three (q22, q24); seven ways (q24); five offer types (q22) | `scarcity-and-urgency.md` § Scarcity: seven ways to limit supply |
| Urgency types | four in q23 and four in q24, split differently | `scarcity-and-urgency.md` § Urgency: the four types |
| Whisper, tease, shout | three steps (q25); four (q26) | `scarcity-and-urgency.md` § Launch: the whisper, tease, shout sequence |
| MAGIC build steps | five (q29, Gemini's numbering); three execution rules (q30) | `bonuses-and-naming.md` § MAGIC naming: steps to build a name |
| CLOSER objection categories | six (q50); four (q45) | `closing-vetting-and-operating.md` § CLOSER: the six-step sales conversation |
| $10K versus $10M differences | six (q48 text); four (q48 diagram) | `closing-vetting-and-operating.md` § Offer as the main lever: the $10K versus $10M offer |
| Ways to grow | two (q51); three (q65) | `closing-vetting-and-operating.md` § Service business: 1-1-1 and the two ways to grow |
| 1-1-1 rule | three ones; q66's "1-1-1-1" | `leads-and-outreach.md` § 1-1-1 rule: one offer, one avatar, one channel |
| Warm outreach steps | ten in q40 and ten in q52, different steps | `leads-and-outreach.md` § Warm outreach: the 10 steps (two versions) |
