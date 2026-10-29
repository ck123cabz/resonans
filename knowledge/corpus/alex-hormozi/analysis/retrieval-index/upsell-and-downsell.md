---
type: corpus
aliases: ["Upsell and Downsell"]
corpus: alex-hormozi
layer: retrieval
tags: [corpus, downsell, machine, offer-stacking, offers, upsell]
source: skills/corpus-ingestion
created: 2026-10-16
file: upsell-and-downsell
sources: q85 to q91, q104, q106, q108 (layer two, $100M Money Models and $100M Lost Chapters)
---

# Upsell and Downsell

Layer 2 retrieval index for the Alex Hormozi corpus, layer two: upsell offers, advanced offer stacking and the value grid, and downsell offers. One framework, rule, script or number set per `##` heading. Each section stands alone, so context repeats rather than cross-references. Continuity offers, billing and churn are in `continuity.md`.

**Provenance key.** `[D]` the words were matched to his own audio (Pass 2 L2.1). `[M*]` NotebookLM transcribed the audio and chose the words; not yet matched. `[A]` a gap: the sources do not hold it. Pass 2 corrections (L2.1 to L2.6) override Pass 1 wherever they disagree.

**Standing caution.** Layer-two answers ran in fresh NotebookLM conversations, so none opens with a previous answer. The same example often appears in several answer files; that is one retelling, not independent confirmation. q89 carries citation numbers far outside its own range, so its payment-plan, feature-downsell, guarantee-removal, rollover and waived-fee figures may come from a wider index. Pass 2 has not passed Christian's review gate.

**Layer-one files that overlap.** Anchoring, tiers and discounting: `pricing-and-tiers.md`. Layaway and first payments: `free-work-trials-and-first-customers.md`. Guarantees: `guarantees.md`. ACA: `leads-and-outreach.md`.

---

## Upsell types: the five named upsells

**Type:** FRM · **Prov:** [D] for the four Money Models names; [M*] for the fifth · **Scale:** general · **Signals:** S-85.1, S-89.1, S-102.3 · **Files:** q85, q87, q89, q102, Money Models p5

- $100M Money Models, part 5: **Classic Upsell, Menu Upsell, Anchor Upsell, Rollover Upsell.** Pass 2 L2.1 matched the four names to his audio.
- $100M Lost Chapters, chapter 20: **Upsell Offer: Free with Alternative Revenue Stream.** The chapter number is the answer's; not yet checked.
- q89 files rollover and free-with-alternative-revenue as downsells; q94 uses rollover as a cancellation save. Pass 1 keeps each under its home type.
- An upsell, as q102 defines it: an offer made immediately after a previous purchase to solve the next natural problem revealed, maximising 30-day gross profit per customer.

---

## Upsell timing: point of greatest need, not greatest satisfaction

**Type:** PRN · **Prov:** [M*] · **Scale:** general · **Signals:** S-86.1, S-86.2, S-86.4 · **Files:** q86, q88, q96

- Make the upsell while the customer is feeling the problem, not right after the current need is met. A steak offered right after a meal gets a "no"; offered when starving it gets a "yes". Repeated in three files.
- For continuity: pitching right after a milestone, when the client feels "stuffed", leads to higher churn. Open-loop what comes next while they are engaged.
- **Hyper-buying cycles:** a short window of high excitement when a customer commits to starting something new (launching a business, starting a fitness program). Customers spend the most money in the shortest period then.
- Scheduled check-ins, orientation calls and progress reviews (1-on-1 onboarding, a 14-day progress check) are the windows for complementary upsells.

---

## BAMFAM: Book A Meeting From A Meeting

**Type:** FRM · **Prov:** [M*] · **Scale:** general · **Signals:** S-86.3, S-85.2 · **Files:** q85, q86, q94, q102

Never leave a customer in "no man's land". End every touchpoint by scheduling the next, so they always know when they will see you next and why. Used to cut churn so clients never feel abandoned. q102 places it in Money Models part 5. q85 ties the classic upsell to BAMFAM ("at purchase or during onboarding"); the link may be the answer's.

---

## Classic upsell: "You can't have X without Y"

**Type:** FRM, SCR · **Prov:** [M*] · **Scale:** general; car rental, fast food, fur coats, gyms, an art studio · **Signals:** S-85.2, S-85.3, S-85.5 · **Files:** q85, q86

- Every offer that solves a problem reveals a new problem. Make the upsell at the exact moment the customer becomes aware of the next problem: right after the first purchase or during onboarding.
- Examples: rental car (insurance, gas, late checkout); fast food (fries and a drink with the burger); fur coat dealer ($30 ear muffs, annual cold storage); Gym Launch (optional supplement suggestions inside customised meal plans).
- **Un-selling line**, agreement through a "no". Two wordings, one per file: "You don't want anything else, do you?" (q85) / "You don't want anything else besides this, do you?" (q86).
- **Guarantee, warranty or insurance upsell:** add 5% to 50% to the price in exchange for a guarantee. An art studio charged an extra 10% for a portrait replacement guarantee; 30% of customers bought it, pure profit on something previously given free.

---

## Classic upsell numbers: the burger profit progression

**Type:** NUM · **Prov:** [M*] · **Scale:** fast-food chain · **Signals:** S-85.4 · **Files:** q85, q86

| Step | Added profit | Total profit | Multiple as stated |
|---|---|---|---|
| $2 burger | $0.25 | $0.25 | 1x |
| Add fries | +$0.75 | $1.00 | 4x |
| Make it a meal | +$1.75 | $2.75 | 11x |
| Supersize for $1 | +$0.25 | $3.00 | "11.6x total profit increase" |

Both files say 11.6x; $3.00 / $0.25 is 12x. Either the source base figures differ or NotebookLM computed it wrongly. q86 describes it as 3 to 4 sequential upsells (burger, fries, drink or meal, supersize).

---

## Menu upsell: unsell, prescribe, A/B, card on file

**Type:** FRM, SCR, CLM · **Prov:** [M*] · **Scale:** gym supplement counter · **Signals:** S-85.6, S-85.7, S-85.8 · **Files:** q85, q86

Up to four tactics (q86 presents them as general upsell wording rules, not only the menu upsell):
1. **Unselling:** tell them, or cross off, what they don't need, to build trust.
2. **Prescription upselling:** exact, personalised instructions on what they do need and how to use it, as if they already own it. Line: "To get the best result from what you just bought, you take two of these in the morning and one at night..." (cut off in the answer).
3. **A/B upselling:** ask a preference between option A and option B, never yes or no to buying, so either choice is an upsell. Lines: "Do you prefer flavor A or flavor B?" / "Would you prefer starting today or Monday?"
4. **Card on file:** remove payment friction. Line: "Do you want to just use the card we have on file?"

Example: a female challenger at a gym. Unsell weight gainer and testosterone boosters, prescribe fat burners and vitamins, ask start today or Monday, charge the card on file.

**CLM:** this supplement prescription closed 20 consecutive customers, $5,000 to $10,000 in supplement sales in a single day. Reads as his own gym; who ran it is not checked.

---

## Anchor upsell: premium first at 5x to 10x the core

**Type:** FRM, NUM, BIO · **Prov:** [D] for the 5x to 10x rule; examples [M*] · **Scale:** general; landscaping, newsletter, art studio, a suit shop · **Signals:** S-85.10, S-85.11, S-85.12, S-106.2 · **Files:** q85, q86, q106, Money Models p5

- His words (Money Models part 5): "if you present a premium version that's five to 10 times the price first, lots of people will say no. Then when you present your main offer, it looks like a much better deal."
- Rule as q85 gives it: "The only thing worse than making a $1,000 offer to a $100 budget is making a $100 offer to a $1,000 budget." Show the super-premium version first, get the reaction ("the gasp"), and if they decline, "come to the rescue" with the core offer, which delivers the same primary features for a fraction of the cost.
- "The gasp" is a reaction here, not a named price test. Layer one found no "gasp test" (`pricing-and-tiers.md` § Premium pricing: the "gasp" test).
- **BIO, the suit:** he walked into a suit shop with a $500 budget. The tailor had him try a $16,000 custom suit first, then showed a $2,200 suit. He bought the $2,200 suit, over 4x his budget ($2,200 / $500 = 4.4x), and felt he got a deal. Anchor to core: $16,000 / $2,200 = 7.3x.

| Business | Anchor | Core | Ratio |
|---|---|---|---|
| Landscaping (q85) | $1,000/week super-productive package with 20-year insurance | $200/week normal yard maintenance | 5x |
| Newsletter (q85, q106) | $199/month: all past issues, new issues, 24-hour early access | $19/month: new issues only, standard release | 10.5x, above the stated ceiling |
| Art studio or physical product (q85, q106) | $1,000: product, extra-protective packaging, 20-year insurance, gift wrap | $200: product, normal packaging, 1-year insurance | 5x |

q85 gives the $1,000 / $200 pair with 20-year insurance both as landscaping (per week) and as an art studio; q106 gives it as a physical product. The two answers disagree on the business.

---

## Decoy menu: The Economist, $59, $125, $125

**Type:** NUM · **Prov:** [D] · **Scale:** large publisher, third-party study · **Signals:** S-85.9, S-106.3 · **Files:** q85, q106, Money Models p5

| Option | Price |
|---|---|
| A: digital only | $59/year |
| B: print only (the decoy) | $125/year |
| C: digital + print | $125/year |

Buyers flock to C because it matches B's price and includes A. Pass 2 L2.1 matched the example to Money Models part 5. Not his business.

**Two definitions of "decoy offer"** (Pass 2 L2.3, question-shaped): q102 calls the decoy a stripped-down basic option set beside a premium one, the cheap option as the decoy. q106 calls it the middle-priced option. The Economist example uses the second. q102 places the decoy offer among attraction offers, Money Models part 4.

---

## Rollover upsell: credit a past purchase toward a bigger one

**Type:** FRM, NUM · **Prov:** [M*] · **Scale:** general; dental, B2B software, local gym, local service · **Signals:** S-85.13, S-85.14, S-85.16, S-85.17, S-85.18 · **Files:** q85, q86, q89, q92, q93, q94

Credit some or all of a past purchase, deposit or challenge fee toward a new, larger offer. Four uses:
1. Re-engage past or inactive customers (win-back).
2. Rescue an upset customer before refunding ("rollover for a do-over").
3. Rescue a competitor's unhappy customers by crediting what they paid or owe the competitor (B2B software: credit the balance a prospect owes a competitor if they cancel and switch).
4. Upsell current customers, such as rolling a short-term program fee into a long-term commitment.

**4x rule:** price the rollover offer at least 4x the credit, so the effective discount never exceeds 25% even if 100% of the earlier spend is credited. Same in q85, q86 and q89.

Worked numbers:
- **Challenge rollover (gym):** a $600 6-week challenge deposit rolled over as $50/month off a $200/month 12-month membership ($600 credit over 12 months): $150/month, turning trialers into $1,800/year members. The same figures appear as a continuity discount "spread over time" in q92 and q93; likely one source example used twice.
- **Gift card rollover:** sell $200 gift cards for $20 (90% off), then roll the $200 value toward a $1,000+ offer (5x).
- **Dentistry:** a $200 teeth cleaning fee credited toward a multi-session whitening package: "$1,000+" (q85) against a "$2,100 teeth whitening package" (q89). Both satisfy the 4x rule; not checked against the audio.

---

## Rollover upsell: the win-back, 200 past clients and $1.9 million

**Type:** CLM · **Prov:** [M*] · **Scale:** high-ticket "advanced program" · **Signals:** S-85.15 · **Files:** q85, q86, q89, q96

Personalised videos to 200 past clients, inactive 6+ months, each offered $4,000 of credit toward returning to an advanced program. 20% converted. $1.9 million in annual revenue (q89: "$1.9M in ARR") from 1 day of recording. 20% of 200 is 40 clients; $1.9M / 40 is $47,500 a year each. Whose program it was is not stated.

---

## Upsell offer: free with alternative revenue stream

**Type:** FRM, MEC · **Prov:** [M*] · **Scale:** general; storage, physical therapy, info products, software · **Signals:** S-87.1, S-87.5, S-87.6 · **Files:** q85, q87, q89, q91, q95

Give one product or service free (or heavily discounted) and make money on a complementary offer from another revenue stream ($100M Lost Chapters, chapter 20).

Requirements: the business has multiple monetisation streams; the free item has low incremental fulfilment cost; the paid item carries high gross margin, enough to cover fulfilment of both.

Two variations:
- **Paired upsell:** Thing A free in exchange for buying Thing B (free software coaching as long as you pay for the software).
- **Independent upsell:** Thing A free, and you recommend Thing B for the best result (free weight-loss program, supplement stack encouraged).

The free item creates flow and reveals the need for the paid item. Use it as a front-end offer, or as a downsell for prospects who refused the main offer ("no prospect left behind").

Examples:
- Storage facility: a free month of storage, paired with a required $30 lock that only fits their doors ($30 in q85 only).
- Physical therapist: 4 free treatment sessions ("4" in q87 only), independent upsell of orthotics, braces, bands and athletic tape ($200+).
- Real estate info product: free book (buyer covers shipping), then shipping $7.95, audiobook $27, contract templates $97, deal finder course $297, financing course $497.
- Software or B2B agency: free agency coaching indefinitely, paid through software subscriptions (q95 names the person "Allen").

**Mechanism:** buyers often pay more readily for tangible products (supplements, locks, orthotics) than for intangible service hours, even from certified professionals.

---

## Free with alternative revenue: the numbers

**Type:** NUM · **Prov:** [M*] · **Scale:** local gym; a 200+ clinic chain; general model · **Signals:** S-87.2, S-87.3, S-87.4 · **Files:** q85, q87, q89, q95

- **Unit math:** $0 revenue on the free item; 80% take a $300 upsell at 80% gross margin: $300 x 80% x 80% = **$192 gross profit per free offer handed out.** q85 calls it "net profit per free customer"; the formula computes gross and ignores the cost of the free item.
- **Over 100 prospects:** paid model, a $99 item at 30% conversion = 30 buyers = $2,970 revenue. Free model, 100% take the free item, 80% take the $300 upsell = 80 buyers = $24,000 revenue, plus better retention and referrals.
- **"No Sale Sale" (a gym owner, not him):** a prospect says no to a $200/month membership; the owner gives a free workout USB and a free nutrition orientation. Nearly 100% of non-buyers booked the orientation (q87; q89 says 100%). Those who refused membership spent 50% more on supplements than regular members; upsold $300 to $400 in supplements.
- **Weight-loss clinic chain, 200+ clinics:** service at $5/month (normally $100/month) for a year, if and only if clients bought its supplements, shakes and meal plans. Despite employing doctors and nurses, 95% of total revenue came from consumer products and 5% from medical or clinical services. q95 adds "$300+ in supplements or meals", possibly borrowed from the unit-math example.

---

## Upsell price relative to the first purchase, and how many to make

**Type:** PRN · **Prov:** [M*]; the price ratio is [A] · **Scale:** general · **Signals:** S-86.7, S-86.8, S-86.9 · **Files:** q86

- **How many:** no hard cap, as long as each solves a legitimate problem ("offer as many solutions as problems"). The McDonald's sequence of 3 to 4 upsells is an illustration, not a limit.
- **Price relative to the first purchase:** Not covered. The answer gives no general ratio for a classic or menu upsell. Every ratio it offers belongs to another type: rollover (at least 4x the credit), anchor (5x to 10x the core), continuity standalone (1.33x / 2.33x / 2.66x, which do not fit their own examples).
- **Bundle and name:** don't make 9 separate asks. Bundle complementary upsell items into one named package (example name: "Fastest Results Bundle") to "make one ask and get nine sales".

---

## Upsell take rates and presentation benchmarks

**Type:** NUM, PRN · **Prov:** [M*] · **Scale:** gym and supplement examples; events and sales teams · **Signals:** S-86.10, S-86.12, S-87.7 · **Files:** q86, q87

- Basic decoy against an ultimate or premium option: 70% to 80% take the premium.
- Frictionless alternative-revenue product upsells at orientation (supplements or products paired with a service): 80% to 90%+. q87: can exceed 90% when the upsell is seen as essential to the outcome and the purchase is frictionless. Same rate, not a conflict.
- Free trial upgraded to a paid, feature-rich version with an A/B close: 75% (3 of 4).
- Free dinners or seminars: convert 25% of the room to a lower-tier offer, and 33% of those buyers into a high-ticket offer. 90-minute masterclasses and 5-day challenges: 10% of attendees on pitch day. 2-step strategy calls: 25% of candidates who reach the second call. Likely from the attraction or sales chapters.
- With cold traffic, closing a credit card for the trial up front reduces no-shows. Whether a customer buys the first upsell is "the single greatest predictor" of long-term retention and LTV; stated without data.

---

## Tiers: no good, better, best menu in layer two

**Type:** PRN · **Prov:** [A] for a three-price menu; rungs [D] · **Scale:** general · **Signals:** S-106.1, S-106.4, S-106.5 · **Files:** q106, Lost Chapters ch. 19

Question-shaped: q106 answered yes under a "good, better, best" heading, then listed other things. The sources do not hold a menu of three prices for one core offer, and "The Magnetic Middle" carries no quote from him. What they hold:
- The anchor upsell at 5x to 10x the core (above).
- Decoy menus (The Economist, above).
- **Pick-your-price rungs above a free base** (Lost Chapters ch. 19, [D]): "Free 21-day weight loss. Upsell. Pick your price. Most people pay $99… If you pick $99, we'll give you an extra one-on-one call. If you pay over $199, we'll also provide our entire supplement handbook. If you pay $499, we'll guarantee that you lose 10 pounds." Car wash: free machine wash, then over $30 hand wax, $67 buff, $99 interior.
- A three-version "buy X, get Y free" menu at $1,800 each (12 paid get 6 free; 6 paid get 6 free; 6 paid get 12 free). Pass 2 L2.4 #21: garbled, do not use.

Layer one reaches the same answer: `pricing-and-tiers.md` § Tiers: the three-tier pyramid is not his.

---

## Advanced offer stacking: a series of grand slam offers

**Type:** FRM, WRN · **Prov:** [M*] · **Scale:** general · **Signals:** S-88.1, S-88.2 · **Files:** q88, q102

A series of Grand Slam offers in a row across the customer's journey instead of one front-end offer ($100M Lost Chapters, Section C, chapters 14 and 16). Three purposes:
1. Acquire customers profitably on the front end.
2. Maximise 30-day gross profit by letting high-budget buyers ("whales") spend big while downsells keep lower-budget buyers ("minnows").
3. Build predictable cash flow by moving customers into continuity.

**Warning:** every added offer adds operational complexity. Only add offers that deliver high profit with minimal added cost, time or friction.

---

## Picking the next offer: right stage, right problem, right way, right time

**Type:** FRM · **Prov:** [M*] · **Scale:** general · **Signals:** S-88.3 · **Files:** q88, q102

Four steps ($100M Lost Chapters, chapter 16):
1. **Right stage:** attraction offers lower CAC and get new buyers; upsell and downsell offers maximise 30-day gross profit; continuity offers maximise lifetime gross profit.
2. **Right problem:** one that makes sense for the business, can be solved with existing resources, and creates big perceived value.
3. **Right way:** the customer's preferred delivery. Two people want to lose weight; one prefers changing workouts, the other meal prep.
4. **Right time:** the moment of greatest need or deprivation (the steak: no after a meal, yes when starving).

---

## Value grid: why a grid, not a ladder

**Type:** FRM · **Prov:** [M*] · **Scale:** general · **Signals:** S-88.4 · **Files:** q88, q102

Owners picture lifetime value as a stair-step: every customer buys offer 1, then 2, then 3. He uses a grid ($100M Lost Chapters, chapter 15) because:
1. Buying is non-linear: not every customer buys in sequence or takes every offer.
2. The grid shows every prospect, the conversion rates, revenue per client and total 30-day cash across every branch.

---

## Value grid #1: the simple trial model, $75 a client

**Type:** NUM · **Prov:** [M*] · **Scale:** small local service, gym-like · **Signals:** S-88.5 · **Files:** q88

- **Rows:** 10 prospects down the left side.
- **Columns:** Trial Offer; Conversion to Membership; Total Conversions / Revenue.
- **Numbers:** 8 of 10 take a $75 trial. 3 convert to a paid membership on the back end. Total revenue $600. 30-day cash per client $75 ($600 / 8 trials), or $60 per prospect.
- **Outcome:** after the labour of working and closing 10 leads ($600 to $1,000), the business barely breaks even or loses money.
- **Flag:** $600 equals 8 x $75, the trial revenue alone, so the 3 membership conversions add nothing to the stated total. Either membership revenue falls outside the 30-day window or the figures are blended.

---

## Value grid #2: the offer-stacked model, $1,763 a client

**Type:** NUM · **Prov:** [M*]; row figures [A] · **Scale:** same business as grid #1 · **Signals:** S-88.6, S-88.7 · **Files:** q88

- **Rows:** the same 10 prospects.
- **Columns:** High-Ticket Front-End Offer (with Downsells); Series of 30-Day Upsells/Downsells; Continuity Conversion; Total Revenue per Client.
- Prospects take different paths: some buy the high-ticket front end, some take downsells, some buy more upsells in the first 30 days. Those who say no to the first offer still produce revenue through low-barrier or alternative offers (free orientations, supplements).
- **Average revenue per client rises from $75 to $1,763**, "over 23x" ($1,763 / $75 = 23.5x), for the same type of business, which lets it outspend competitors on marketing.
- Not covered: no front-end price, no downsell prices, no count of prospects on each path, no continuity conversion count. Only the $1,763 average survives. The grid may be a visual in the print book that the audiobook does not read out.

---

## Offer stack example: the 4-sale weight-loss sequence

**Type:** FRM · **Prov:** [M*] · **Scale:** weight-loss or fitness business · **Signals:** S-88.8 · **Files:** q88

Four sales over 6 to 12 weeks.

**Sale 1, service (upfront cash):**
1. High-ticket goal program first.
2. If no, downsell 1: half-down payment plan.
3. If no, downsell 2: quarter-down payment plan.
4. If no, downsell 3: quarter-down, shorter duration, "no plan" (unclear; may mean no meal plan).
5. If no, downsell 4: free trial with card on file and adherence penalties.
6. If no, downsell 5: free 1-on-1 nutrition orientation within 24 to 72 hours.

**Sale 2, physical product at the orientation:**
1. Full 3-month supplement bundle.
2. If no, a 1-month supply on recurring subscription.
3. If no, cross off non-essentials and offer the essential stack.
4. If no, 1 or 2 standalone essentials.
5. Follow-up: pre-made meal prep, 12-pack, then 8-pack, then bi-weekly.

**Sale 3, continuity:** at a "client feedback meeting" 2 to 3 weeks later. If they are getting results, pitch long-term membership, starting with a high-ticket prepayment discount and downselling to standard monthly.

**Sale 4, prepayment discount:** before the program or trial ends, offer a discount to prepay the remaining continuity term in full, pulling cash forward and locking in retention.

---

## Downsell: definition and the three types

**Type:** FRM · **Prov:** [D] for the three families; rest [M*] · **Scale:** general · **Signals:** S-89.1 · **Files:** q89, q90, q91, Money Models p6

- A downsell is any offer made after a prospect says no.
- A true downsell never lowers the price of the exact same offer without changing terms; that is discounting and it damages trust. It changes either **how the customer pays** or **what the customer gets**.
- The three named types ($100M Money Models part 6, matched to audio): **payment plan, trial with penalty, feature downsell.**
- q89 also lists free-with-alternative-revenue, rollover, layaway and waived fee as downsells, following its question's "anything similar". q85 files rollover as an upsell, q87 files free-with-alternative-revenue as an upsell, q92 files waived fee as continuity, and q90 treats layaway as a payment-plan step.

---

## Downsell rules: when to present and how to frame it

**Type:** PRN · **Prov:** [M*] · **Scale:** general · **Signals:** S-90.1, S-90.2, S-90.3 · **Files:** q90, q91

- Present a downsell immediately after the prospect says no to the core offer or an upsell. "No" means no to this thing at this moment, not no to everything and not a rejection of you. A no is feedback on what they want and can afford.
- Downsells are trades: give something, get something. Never lower the price without taking something away or changing the terms.
- Personalise, don't pressure: find which features they value or dislike and adjust the package.
- Offer the same thing in new ways (different payment or feature structures) rather than building many new products.
- Stay a helpful guide; frame each downsell as finding the best fit for budget and goals.
- Never negotiate or drop the price for the exact same product; it devalues the offer, destroys trust and trains customers to demand discounts. Never negotiate with "price terrorists".
- **Which downsell:** want to pay less overall, change what they get (feature downsell). Want to pay less now, change how they pay (payment plan). Demand a discount, change the terms so you get equal or greater value in marketing (barter).

Layer one's no-discount rule: `pricing-and-tiers.md` § Discounting: never discount the core offer.

---

## Payment plan downsell: the step-down sequence

**Type:** FRM, NUM, BIO, CLM · **Prov:** [M*] · **Scale:** general; his first sale; Gym Launch · **Signals:** S-89.2, S-89.3, S-89.5, S-89.6, S-91.1 · **Files:** q89, q90, q91

Same product at full price; the billing is split into an upfront payment plus instalments.

q89's seven steps:
1. Prepayment discount against an interest-inclusive price anchor (example: $15 total, $10 if prepaid).
2. Third-party financing, credit card or layaway.
3. Half down now, half later.
4. 1-to-10 desire scale check.
5. Three-part split: 1/3 down, 1/3 on each of the next two paychecks or months.
6. Payments spread evenly across the full term.
7. Free trial.

q90's step-down after the full-price-with-prepay-discount offer: third-party financing / credit card / layaway; half down now, half next paycheck; one-third down, rest over the next two paychecks or months; evenly spread across the service length. Same order; q90 treats the 1-to-10 check and the free trial separately.

- Aligning payments with paycheck cycles (every two weeks) "significantly" increases 30-day collected cash. No number.
- A payment-plan downsell process lets a business recoup up to a third (33%) of declined or failed payments (q91; "declined" may mean declined offers or declined cards).
- **BIO, his first sale:** the prospect couldn't afford the upfront fee. He asked "When do you get paid?" and set the deal as "half down today, half on the 2nd when you get paid" (or full payment scheduled for the 2nd).
- **CLM, Gym Launch:** a $16,000 16-week program downsold to $10,000 down with the rest spread over 52 weeks, or further to $800 per week for 52 weeks. $800 x 52 = $41,600, far above $16,000, so the second option cannot be a downsell of the $16,000 program; it matches the $42,000/year back end. The answer likely blended two offers.

---

## Payment plan scripts: see-saw, paycheck, most you can put down

**Type:** SCR · **Prov:** [M*] · **Scale:** general · **Signals:** S-90.7 · **Files:** q90

- **See-saw frame:** "Normally it costs [Price]. If you prepay today, you get a huge discount and zero monthly payments. Would you rather have giant monthly payments or tiny ones?"
- **Paycheck alignment:** "Got it, so money's tight right now. When's the next time you get paid? Want to just put half down today and the rest when you get paid? Fair enough?"
- **Cash-available step-down:** "What's the most you can put down today? Great, we'll put that down today and schedule the rest when you get paid."

---

## Layaway: fulfilment waits for the threshold

**Type:** FRM, NUM · **Prov:** [M*] · **Scale:** high-ticket coaching · **Signals:** S-89.13, S-95.4 · **Files:** q89, q90, q95

The client pays in flexible instalments, and fulfilment waits until a threshold is reached (example thresholds: 1/3 down, or paid in full). Example: a $25,000 high-ticket coaching program downsold to a $9,000 down payment by layaway across 3 instalments before the deep-dive strategy session starts. q95's "Couplepreneurs Accelerator" at $25,000 to $30,000/year (or $2,500 to $3,000/month) with $9,000 down via layaway is probably the same example; $9,000 across 3 instalments is $3,000 each.

Layer one's layaway: `free-work-trials-and-first-customers.md` § First payment: large down payment and layaway.

---

## 1-to-10 temperature check after two failed downsells

**Type:** FRM, SCR · **Prov:** [M*] · **Scale:** general · **Signals:** S-90.4 · **Files:** q89, q90, q91

After two downsell adjustments in a row without a sale, pause and ask: "Real quick, on a scale from 1 to 10, how bad do you want this?"
- **8 to 10:** the problem is money or structure. Keep working payment plans and say: "Awesome, don't worry, we're going to figure out a way to make this happen for you."
- **7 or below:** ask "Why not?" or "What would a 10 look like?", then recombine or remove features, or pivot to another product or a do-it-yourself option.

q89 puts the check as step 4 of the payment-plan sequence.

---

## Trial with penalty: structure and the $1 first month

**Type:** FRM, NUM · **Prov:** [D] for the $1 first month; rest [M*] · **Scale:** general; HR software, fitness, B2B · **Signals:** S-89.7, S-89.9, S-104.3 · **Files:** q89, q90, q104, Money Models p6

- The prospect gets the product free (or $1) on condition of completing required actions: attend onboarding calls, log progress, submit homework. Break the terms or miss check-ins and they pay a pre-disclosed penalty fee. Comply and the trial stays free and rolls into recurring paid billing.
- Penalties can be chunked (example: $50 per missed action or check-in) or a lump sum.
- **$1 first month** (Money Models part 6, matched to audio): charge $1 for the first month instead of a free one, so a working card is on file before automatic billing starts in month two; "people get weird when you offer free stuff and ask for a card."
- **HR software:** normal offer $500 onboarding + $99/month. Downsell: $0 onboarding provided the client attends three 60-minute Zoom onboarding calls and activates employee profiles by the end of call 3. Miss calls or homework and they are billed the $500 penalty fee.
- **Fitness:** free 28-day blueprint; missed daily app logs or required check-in calls trigger a fee. **B2B:** a 5-day challenge; failing to send 100 outbound messages a day triggers the fee. Neither penalty amount is given.

---

## Trial with penalty: script and conversion numbers

**Type:** SCR, NUM · **Prov:** [M*] · **Scale:** gym or local service · **Signals:** S-90.8, S-89.8 · **Files:** q89, q90, q91

Pitch: "Hmm, that sure is a pickle. I'll tell you what—how about we just get you started for free? We can just help you out, and if you like it, you can stay. Let me grab your ID—what card do you want to use?"

Penalty: "We will do our part so long as you do yours. That's fair, right? So now I just ask that you bet on yourself. If you miss or skip any steps, your results will suffer. We charge a little fee to keep you on track. If you follow through, then you get all of this for free. Fair enough?"

Numbers after an upfront-cash refusal: close 3 of 10 on upfront cash, sell 4 of 10 on the trial, 3 of those 4 become long-term paying clients, so paid clients go from 3 to 6 of 10 (q89). q91: payment-plan or trial-with-penalty downsells typically convert another 3 to 4 of every 10, doubling acquisitions from 3 of 10 to "6 or 7" of 10. q91's 7 seems to count all 4 trial takers rather than the 3 that convert.

---

## Feature downsell: the five sub-types

**Type:** FRM, SCR · **Prov:** [M*] · **Scale:** general; painter, chiropractor, software support tiers · **Signals:** S-89.10, S-90.5 · **Files:** q89, q90

Lower the price only by removing features, duration, quantity, quality, guarantees or service level. The prospect weighs money saved against value lost and often re-upsells themselves to the full offer.
1. **Quantity:** shorter duration, fewer sessions, less volume (3-month supply to 1-month; 4 sessions a month to 2).
2. **Quality:** lower-grade materials, older versions, junior staff or slower support (vinyl seats instead of leather).
3. **Remove whole features or the guarantee** (priority phone calls; the money-back guarantee).
4. **Done-for-you to do-it-yourself:** a tool, course, self-serve product or workshop instead of the service. Painter: instead of a $3,000 paint job, sell the paint and lease a spray machine at a daily rate (rate not given). Chiropractor: instead of in-office adjustments, $19 home massage tools and foam rollers plus a free orientation.
5. **Barter:** lower price in exchange for marketing actions (next sections).

"Take away and ask" script: "Instead of priority chat, email support, and weekly calls, why don't we just keep chat and email support to save you some money? You'll still get your answers, but it saves us time and we pass those savings on to you. How about now?"

---

## Feature downsell: removing the guarantee, 25% to 75% close

**Type:** NUM, SCR · **Prov:** [M*] · **Scale:** high-ticket sales team, 100 calls · **Signals:** S-89.11, S-90.6 · **Files:** q89, q90, q91

- Close rate went from 25% to 75% overall (tripled). Of 100 sales calls, 35 bought the full-price package with the guarantee (up from 25, because removing it showed the guarantee's value and prospects re-upsold themselves) and 40 took the downsell without the guarantee, $400 cheaper. 35 + 40 = 75. q90 calls guarantee removal "the ultimate feature downsell"; q91 places it in Money Models. Whose business is not stated.
- Script: "If you don't want the option to get your money back, you can pay [Lower Price], or you can keep your money-back guarantee at [Full Price]. Which would you prefer?"

Layer one's guarantee types: `guarantees.md`.

---

## Barter downsell: $100 off for reviews and introductions

**Type:** NUM, SCR, PRN · **Prov:** [M*] · **Scale:** general · **Signals:** S-89.12, S-90.9, S-108.6 · **Files:** q89, q90, q108

- q89: $100 off if the client leaves reviews on all platforms, records a video testimonial, makes 3 public progress posts and introduces 2 friends.
- q90 script: "I can't discount the price for nothing, but I can knock $100 off if you leave us a review, give us a video testimonial, and introduce me to 3 friends who would want to do this with you right now. Deal?" q90's rule text says "3-way referral introductions".
- 2 friends against 3; q89's 3 public posts are missing from q90's script. Possibly two different examples.
- q108: give a price cut only in exchange for 3 direct text introductions to qualified friends.

---

## No prospect left behind: the free orientation after every no

**Type:** FRM, SCR, NUM · **Prov:** [M*] · **Scale:** gym and local service · **Signals:** S-91.2, S-87.2 · **Files:** q87, q89, q91

If the prospect refuses every done-for-you offer and downsell, move them to a free orientation or a free DIY resource to keep goodwill.

Line: "Even though we're not going to work together on X, I still want to help. How about you come in for a free orientation tomorrow?" (or hand over a free guide or USB).

At the orientation, offer a lower-cost DIY product or an alternative product that solves the problem another way (nutrition supplements or meal plans for someone who refused workout services). About half (50%) of those who show up buy the DIY or alternative product. The "50% more spend" in the No Sale Sale is a different measure.
