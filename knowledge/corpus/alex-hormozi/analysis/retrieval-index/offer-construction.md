---
type: corpus
aliases: ["Offer Construction"]
corpus: alex-hormozi
layer: retrieval
tags: [corpus, machine, market, offers]
source: skills/corpus-ingestion
created: 2026-10-16
file: offer-construction
sources: q02, q06–q12, q13–q15, q17, q25, q27, q29–q35
---

# Offer Construction

Layer 2 retrieval index for the Alex Hormozi corpus. One framework, rule, script or number set per `##` heading. Each section stands alone, so context repeats rather than cross-references.

**Provenance key.** `[D]` the words were matched to his own audio (Pass 2 §2). `[M*]` NotebookLM transcribed the audio and chose the words; not yet matched. `[A]` a gap: the sources do not hold it. Pass 2 corrections override Pass 1 wherever they disagree.

**Scope.** Offer definition, market selection, problems and solutions, delivery vehicles, trim and stack, the weight-loss stack and the creation order. The value equation and its four drivers are in value-equation.md.

**Standing caution.** Q1 to Q35 ran in one NotebookLM chat, so several answers carry the previous answer's material. A figure repeated across files is one retelling, not independent confirmation. Pass 2 has not passed Christian's review gate.

---

## Offer: definition and the grand slam offer

**Type:** FRM · **Prov:** [M*] · **Scale:** general · **Signals:** S-02.1, S-02.2, S-02.3 · **Files:** q02, q10

**Offer:** the starting point of any conversation to start a transaction; what you provide in exchange for money. It covers the goods and services, how payment is accepted, and the terms of the agreement.

**Grand Slam Offer:** an offer presented to the marketplace that cannot be compared to any other product or service available. Five elements:
1. an attractive promotion;
2. an unmatchable value proposition;
3. a premium price;
4. an unbeatable guarantee;
5. a money model (payment terms) that lets you get paid to acquire new customers.

It lets you sell in a "category of one", where the choice is your product or nothing, so the purchase is value-driven, not a price comparison. "Money model" is also the title of his later book, not in this layer.

**Irresistible price:** not a discount or bargain price. A premium price where perceived value far exceeds the price. People buy when value received is worth much more than price paid. Example given: $10,000 for $100,000 worth of value (may be NotebookLM's illustration).

---

## Offer: "so good they feel stupid saying no"

**Type:** SCR · **Prov:** [D] · **Scale:** general · **Signals:** S-02.5, S-48.2 · **Files:** q02

> "Make people an offer so good they would feel stupid saying no."

From his mentor TJ (Pass 1 reads the name as Travis Jones). Pass 2 matched the line to Offers parts 1 and 4.

q02's reading of what it means (NotebookLM's, not his): every friction point pre-solved; risk moved to the seller by strong guarantees; bonuses stacked until the price-to-value gap is irrationally large; refusing means walking away from a guaranteed result at zero risk.

---

## Market: the starving crowd

**Type:** MEC · **Prov:** [M*] · **Scale:** general · **Signals:** S-07.1, S-07.2 · **Files:** q06, q07, q08, q09

A marketing professor asks: if you open a hot dog stand and can have one advantage (location, quality, low prices, best taste), which? Answer: a starving crowd. With one, you can have bad hot dogs, high prices and a bad location and still sell out. Entrepreneurs do not create demand; they channel existing demand.

The scene differs by file: "a mob of starving people coming out of a stadium" (q06); "when the local college football game breaks out (or when bars close at 2 AM)" (q09); "when a college football game breaks out and crowds ... pour onto the street at 2 a.m." (q08, merging the two).

**COVID-19 toilet paper:** no offer, bad pricing, no sales pitch, yet rolls sold for "$100 or more" (q07, q09) or "$100/roll" (q08) because the crowd was starving. Unit unclear (per roll or per pack). Pass 2 did not find the toilet-paper price in the transcribed audio; its origin is `[A]`.

---

## Market: ranking market over offer over persuasion

**Type:** FRM · **Prov:** [M*] · **Scale:** general · **Signals:** S-07.3, S-32.1 · **Files:** q07, q08, q09, q32

Ranking: Starving Crowd (market) > Offer Strength > Persuasion Skills.

- A Great rating on a higher component overpowers anything lower.
- A Normal rating passes success to the next lever.
- A Bad rating halts success unless a higher component overrides it.

Cases:
1. Great market, bad offer, bad persuasion: hot dogs at 2 a.m. to drunk crowds leaving bars; sells out.
2. Normal market, grand slam offer, bad persuasion: brick-and-mortar gyms, chiropractors, agencies (agencies named in q09 only). You make a lot of money even if bad at persuasion; where most successful businesses operate.
3. Normal market, normal offer, great persuasion: a commodity offer sold on persuasion alone; the hardest, highest-effort path. q08 says this case can "still build an empire".

q08 adds a fourth: bad market, great offer, great persuasion = Lloyd's newspaper business, which declines. The other files give three cases; the fourth may be NotebookLM mapping the Lloyd story onto the grid.

---

## Market: the four criteria

**Type:** FRM · **Prov:** [M*] · **Scale:** general · **Signals:** S-06.1, S-06.2, S-06.3, S-06.4 · **Files:** q02, q06, q07, q08

1. **Massive pain:** they must desperately need, not merely want, a solution. Pain can be financial, physical, emotional or social.
2. **Purchasing power:** they must have the money, or access to it, to pay what you need to charge.
3. **Easy to target:** gathered in identifiable places such as associations, mailing lists, social media groups, submarkets, media channels. q08: hard-to-find buyers make marketing "unnecessarily difficult and expensive" (needles in a haystack).
4. **Growing:** a tailwind. A shrinking market is a headwind.

"The pain is the pitch." The degree of pain is directly proportional to the price you can charge. If you articulate their pain accurately, prospects will almost always buy.

**Purchasing-power failure:** a friend (q08: "a consultant") built a strong system to help unemployed people improve their resumes. Massive pain and easy targeting, but it failed because the market was unemployed and could not pay.

**Targeting failure:** if you serve rich doctors but your ads show to nursing students, the offer falls on deaf ears regardless of quality. q07 adds that nursing students lack purchasing power.

---

## Market: dying market, the Lloyd story

**Type:** WRN · **Prov:** [M*] · **Scale:** a friend's software company, then manufacturing · **Signals:** S-06.5, S-35.4, S-20.7 · **Files:** q06, q07, q08, q20, q35

Lloyd ran a software company serving newspapers: a zero-risk revenue-share offer setting up digital ad services on newspaper websites for a percentage of added revenue. If the newspapers made nothing, Lloyd made nothing. He had strong sales skills and good software. Revenue shrank every year because newspapers were contracting 25% a year.

When COVID hit he pivoted to automated face-mask manufacturing and, with the same skill set, did:
- "millions of dollars per month within 5 months" (q06, q07); or
- "a multi-million dollar business in 5 months" (q08).

These are different claims (monthly rate against total size). Lloyd's surname is not given. Pass 2 did not find the Lloyd story in the transcribed audio; its origin is `[A]`.

Lesson as given: market contraction overrides great products, zero-risk offers and elite sales. It sits in tension with "the market is rarely the problem" (niche slapping): the market is rarely the problem, except when it is shrinking.

---

## Market: niche slapping

**Type:** WRN · **Prov:** [M*] · **Scale:** general · **Signals:** S-06.7, S-33.5 · **Files:** q06, q07, q33, q34, q35

"Niche slapping" (q06) / "niche slap" or "niche hopping" (q07) / "niche slapped" (q33): switching markets after one failed attempt, for example dentists to chiropractors. Changing markets resets trial and error to zero each time. People call a market bad when they have not yet built a grand slam offer for it. Most normal markets hold billions of dollars of opportunity; the market is rarely the problem, the offer is.

Rule: pick one normal or growing market (Health, Wealth or Relationships), commit to one avatar, stay long enough to iterate, and iterate the offer, wrapper and bonuses until it works.

---

## Market: the $10 million rule and micro-niching

**Type:** NUM · **Prov:** [M*] · **Scale:** general, under $10M/year; Gym Launch · **Signals:** S-06.8, S-06.9 · **Files:** q06, q07, q08

For 99.6% of entrepreneurs (q06) or "of businesses" (q07, q08), meaning anyone under $10 million a year in revenue, a tight niche makes far more money and is easier to run. Broaden (up-market, down-market or adjacent markets) only after you cap out your Total Addressable Market, which usually does not happen until $10 million to $30+ million a year. q08 says broaden "after crossing $10 million per year or when it exhausts its TAM", which reads as either condition; q06 and q07 tie broadening to exhausting the TAM.

Pass 2 did not find the 99.6% figure in the transcribed audio; its origin is `[A]`.

**Gym Launch micro-niche:** brick-and-mortar gym owners with 100 members (may be "at least 100"), a signed lease and at least one employee. He turned away personal trainers and online coaches to keep product and messaging focused.

For the niche price ladder ($19 to $1,997), see pricing-and-tiers.md, "Niche price ladder".

---

## Problems: listing every problem

**Type:** FRM · **Prov:** [M*] · **Scale:** general · **Signals:** S-08.1 · **Files:** q02, q08, q09, q11

Divergent problem-solving:
1. Identify the dream outcome (for example lose 20 lbs in 6 weeks).
2. List every obstacle, friction point and limiting belief the prospect meets before, during and after using the product, in chronological order, at granular detail (what happens immediately before and after each action).
3. Reverse each problem into solution language with "How to..." in front.
4. Name each solution with a distinct, benefit-driven title.

Then delivery vehicles, then trim and stack. q09 shows step 4 as its own step; q08 and q11 fold naming into trim and stack. Where naming sits in the order is unclear.

---

## Problems: the four-driver filter

**Type:** FRM · **Prov:** [M*] · **Scale:** general · **Signals:** S-08.2 · **Files:** q08, q09, q11

Run each obstacle through the four value drivers to find sub-problems, phrased as the buyer's doubt:

| Driver | Buyer's doubt |
|---|---|
| Dream Outcome (q09: "Financial worth / Value") | "This won't be worth it financially." |
| Perceived Likelihood | "It won't work for me specifically; my family or travel schedule will get in the way." |
| Effort and Sacrifice | "This will be too hard, confusing, or unpleasant." |
| Time Delay | "This will take too long; I'm too busy." |

---

## Problems: weight-loss problem-to-solution conversions

**Type:** SCR · **Prov:** [M*] · **Scale:** local fitness, weight loss · **Signals:** S-08.3 · **Files:** q08, q09, q11

| Stage | Problem | Solution statement |
|---|---|---|
| Buying food | hard, confusing, expensive, takes too much time | "How to make buying healthy food easy, fast, and cheap so anyone can do it." |
| Cooking | takes too much time; family needs get in the way | "How to cook delicious, healthy meals in under 5 minutes" (despite family constraints) |
| Eating | boring, hard to stick to, tastes bland | "How to eat delicious food without following complicated systems." |
| Exercising | intimidating, risk of injury, slow results | "easy-to-follow exercise system everyone enjoys" |
| Traveling | will ruin diet and routine | "How to travel and stay healthy with no equipment." |
| Dining out | going out with friends or colleagues ruins progress | "How to eat out at restaurants and still reach goals." |
| Consistency | losing motivation and dropping out | "How to stick with the program effortlessly." |

q08 gives the consistency solution as "Unbeatable system to keep you consistent without permission", which looks garbled. Wording varies across the three files.

---

## Delivery vehicles: the delivery cube

**Type:** FRM · **Prov:** [M*] · **Scale:** general · **Signals:** S-09.1 · **Files:** q07, q08, q09, q11

q09's six levers for brainstorming formats:
1. Personal attention ratio: 1-on-1, small group, one-to-many.
2. Level of effort: DIY, DWY, DFY.
3. Medium if live: in-person, phone, email, text, Zoom, chat groups.
4. Consumption format if recorded: audio, video, written (checklists, templates, software calculators).
5. Speed and responsiveness: 24/7, 9-to-5, reply within 5 minutes, 1 hour or 24 hours.
6. The 10x / 1/10th test.

Brainstorm without cost limits first (divergent thinking).

The count differs by file: q09 six; q11 four plus the 10x test; q07 three axes (group size, effort, live against recorded). The cube name implies three axes; the six-lever list may be NotebookLM's expansion.

---

## Delivery vehicles: the 10x and 1/10th test

**Type:** FRM · **Prov:** [M*] · **Scale:** general · **Signals:** S-09.2 · **Files:** q09, q11

- **10x:** if a client paid you 10x ($100,000), what high-touch value would you deliver?
- **1/10th:** how would you make sure they succeed if they paid 1/10th the price? This forces low-cost automation.

q11 words the second half as "How could I deliver 10x value for 1/10th the price at scale?" The $100,000 figure implies a $10,000 base price; neither answer states the base.

---

## Delivery vehicles: sales-to-fulfillment continuum

**Type:** MEC · **Prov:** [M*] · **Scale:** general · **Signals:** S-09.3, S-34.1 · **Files:** q09, q10, q34

- Easy to sell (DFY, 1-on-1, do everything, taking all the risk) = hard to fulfill. It makes the offer irresistible to early clients.
- Easy to fulfill (thin DIY, recorded one-to-many, software, done-with-you) = hard to sell unless heavily bundled, because perceived value is low.
- The goal is an offer that is easy to sell and easy to fulfill. Build the systemised assets with cash flow once demand exists, to bring fulfillment toward near-zero marginal effort.

---

## Delivery vehicles: create flow, monetize flow, add friction

**Type:** PRN · **Prov:** [M*] for the rule, [D] for the 33 gyms and 8 a month · **Scale:** general; his Gym Launch start · **Signals:** S-09.4, S-17.3, S-33.6, S-34.2, S-34.3, S-34.4 · **Files:** q09, q10, q17, q33, q34

"Create flow, monetize flow, then add friction." (q33 calls it the "friction flow threshold".)
1. **Create flow:** manual, high-touch work to generate demand and close sales. Over-deliver, take on all the risk, do done-for-you fulfillment or work on site if needed (for example flying out to clients).
2. **Monetize flow:** collect upfront cash and confirm people want it.
3. **Add friction:** use the cash flow to build software, templates, recorded trainings, DWY assets and automated systems that cut fulfillment effort without lowering perceived value, or raise prices.

When getting first customers, over-deliver even if fulfillment is heavy manual labour; do not optimise or automate before demand is proven. As a pricing rule for a new business (q17), it says start by carrying the risk, not by charging the most.

**Gym Launch case:** he flew to 33 gyms in 18 months [D], lived in cheap motels for 21 days per gym [D for 21 days], paid his own travel and ad spend upfront, worked every lead by hand, ran sales meetings and did the initial onboarding. "At our peak we were turning around eight gyms a month" [D]. Both figures are his words (Offers p2, Leads p9); 33 in 18 months averages under 2 a month and 8 was the peak, so the Pass 1 contradiction flag is withdrawn. Once he collected $100,000/month in cash flow he converted the process into a done-with-you licensing curriculum and software, taught gym owners remotely, and scaled to over 4,000 gym locations from home [M*].

**Macro sheet:** 100 hours coding an Excel application that calculated macronutrients and generated 100 customised meal plans and grocery lists; after that, 15 minutes per personalised plan [M*].

**Cardboard-box sale:** facing $150,000 in sudden refund debt, he phoned gym owners directly, wrote their card details on the flap of a cardboard box, and sold the system verbally for $6,000, $8,000 and $10,000. He collected $60,000 in a single day by phone, then spent 48 hours packaging his lead and sales system into a digital asset package delivered to buyers on Monday morning [M*]. Sold before the product existed.

---

## Delivery vehicles: which vehicle for which price

**Type:** FRM · **Prov:** [A] · **Scale:** general · **Signals:** S-09.5 · **Files:** q09, q10

Not covered: the answers give no price-to-vehicle table. The closest rules: high-cost, high-value vehicles (1-on-1 consulting, bespoke setup) are reserved for premium high-ticket prices; low-cost, high-value one-to-many assets go in at any price.

---

## Trim and stack: the four cost-value buckets

**Type:** FRM · **Prov:** [M*] · **Scale:** general · **Signals:** S-10.1, S-10.2 · **Files:** q08, q09, q10, q11

Trim by cost to you against perceived value to the client. Judge value through the value equation: does it raise the dream outcome or financial value, raise perceived likelihood, cut effort and sacrifice, cut time delay?

| Bucket | Action |
|---|---|
| High cost, low value | drop first |
| Low cost, low value | drop second, to keep the offer clean |
| High cost, high value | keep selectively; reserve for high-ticket tiers or convert to a lower-cost one-to-many version |
| Low cost, high value | keep and double down |

Low-cost, high-value items are one-to-many assets: high one-time effort to create, near-zero cost to deliver again. Examples: recorded trainings, software tools, automated calculators, swipe files, templates, pre-made Instacart carts, fast cooking guides, recorded orientations.

---

## Trim and stack: building the stack

**Type:** FRM · **Prov:** [M*] · **Scale:** general · **Signals:** S-10.3, S-10.5 · **Files:** q08, q10, q11

Stack: combine the remaining deliverables into one bundle; give each element a benefit-driven name and an explicit dollar value; sum the values into a large total; sell the bundle for a fraction of it.

How the dollar value of each element is set is not explained in any of the three answers: `[A]` on the valuation method. (The bonus lane gives one justification rule: price each item by the time or money it saves; see bonuses-and-naming.md.)

Why the stack wins (q10, NotebookLM's summary): it removes every perceived problem before, during and after purchase; $4,351 of value against $599 makes saying no feel illogical; the prospect can no longer compare it to a generic $29/month gym, so the decision moves from price comparison to a category-of-one purchase.

---

## Weight-loss stack: every item and value

**Type:** NUM · **Prov:** [D] · **Scale:** his local fitness and weight-loss offer · **Signals:** S-10.4, S-13.7, S-27.2 · **Files:** q08, q09, q10, q11, q13, q14, q15, q27, q29, q30, q31

| # | Before (plain deliverable) | Named item | Problem it solves | Contents | Value |
|---|---|---|---|---|---|
| 1 | grocery shopping tips | Foolproof Bargain Grocery System | shopping confusing, expensive, time-consuming | 1-on-1 nutrition orientation, recorded grocery store tour, DIY grocery calculator, weekly grocery lists, bargain shopping training, buddy system, pre-made Instacart carts, weekly text check-ins; saves $100s a month and takes less time than the current shopping routine | $1,000 |
| 2 | quick cooking instructions | Ready in 5 Minute Busy Parent Cooking Guide | no time to cook | meal prep instructions, DIY meal prep calculator, healthy snacks under 5 minutes guide, meal prep buddy system | $600 |
| 3 | custom meal plan | Personalized "Lick Your Fingers Good" Meal Plan (q29: "Personalized Meal Plan") | healthy food bland, hard to stick to | personalized meal plan, 5-minute morning shake guide, budget lunches and dinners, family-sized meals | $500 |
| 4 | workout routines | Fat Burning Workouts | plateau, inefficiency, injury | adjusted to avoid injury and plateaus | $699 |
| 5 | travel nutrition plan | Ultimate "Tone Up While You Travel" Blueprint | travel ruins routine | no-equipment workouts and eating guide | $199 |
| 6 | weekly check-in meetings | Never Fall Off Accountability System | discipline, motivation, dropping out | | $1,000 |
| 7 | dining out tips | "Live It Up While Slimming Down" Eating Out System | missing out when dining with friends | | $349 |

- His words: "Total value $4,351, all for only $599" [D, Offers p4].
- The seven values he reads add to $4,347. His own sum is off by $4.
- $4,351 / $599 = 7.26; q27 says "more than 7x". q13 offers it as an example of a 10x gap, which it is not.
- Longer-term versions of the bundle later sold for $2,400 to $5,200 [D].
- Item order is the same in q08 and q10 (Accountability 6th, Eating Out 7th).
- Item 7 began as a one-off restaurant guide written to save one executive's sale (see value-equation.md, "Time delay and effort: techniques to cut them").

---

## Offer creation: the full process in order

**Type:** FRM · **Prov:** [M*] · **Scale:** general · **Signals:** S-11.1, S-02.4, S-12.14, S-25.1 · **Files:** q02, q08, q11, q12, q25

Four tellings exist. None is matched to audio; each is kept whole.

**q11 (six steps, starts at the dream outcome, no market step):**
1. Identify the dream outcome: destination, not vehicle; "Lose 20 lbs in 6 weeks" over "$99/month boot camp membership".
2. List the problems: every obstacle before, during, after; granular timeline; filter through the four drivers.
3. Convert problems to "How to..." solution statements.
4. Create delivery vehicles: divergent brainstorm, no cost limits; delivery cube; 10x / 1/10th test.
5. Trim and stack. 5A trim: drop high-cost low-value, then low-cost low-value; keep high-cost high-value for high-ticket; double down on low-cost high-value. 5B stack: bundle, name, assign dollar values, sum (for example $4,351 value for $599).
6. Add enhancers: scarcity, urgency, bonuses, guarantees, MAGIC naming.

**q02 (market and price first):**
1. Find a starving crowd (pain, purchasing power, easy to target, growing).
2. Charge premium prices so you can invest heavily in client success.
3. Run the 5-step value creation: identify dream outcome; list every problem before, during and after; turn each problem into a "How to..." solution; brainstorm delivery vehicles (1-on-1, small group, 1-to-many; DIY, DWY, DFY); trim high-cost low-value items and stack the rest.
4. Add offer enhancers: scarcity, urgency, bonuses, guarantees (conditional, unconditional, service), MAGIC naming (Magnet, Avatar, Goal, Interval, Container).

**q12 (eight steps, appended unasked):**
1. Select market and niche: verify 4 criteria (Massive Pain, Purchasing Power, Easy to Target, Growing); commit to a narrow avatar; niching lets you charge up to 100x more for the same core service.
2. Identify the dream outcome: sell the destination ("Lose 20 lbs in 6 weeks"); define the feelings and status gain.
3. List every problem and obstacle before, during and after purchase across the 4 value drivers.
4. Reverse each problem into a "How to..." solution statement.
5. Brainstorm delivery vehicles with the Delivery Cube: 1-on-1 vs small group vs 1-to-many; DIY vs DWY vs DFY; mediums (Zoom, text, in-person); formats (audio, video, written/tools).
6. Trim and stack: drop high-cost/low-value, keep low-cost/high-value assets (calculators, templates, 1-to-many trainings), give each a benefit name and a dollar value.
7. Layer enhancers: scarcity (limited spots), urgency (deadlines or rolling cohort start dates), bonuses (instead of discounts), guarantees (conditional, unconditional or service).
8. Name it with MAGIC: Magnet (reason why), Avatar, Goal, Interval, Container.

**q25 (launch order, likely the book's chapter order presented as an order of operations):**
1. Core value offer: dream outcome, map obstacles, turn them into solutions, trim and stack into the core bundle.
2. Scarcity: total cap, weekly cap, cohort limit.
3. Urgency: rolling cohorts, promotional deadlines, countdowns.
4. Bonuses: stack deliverables one by one to widen the price-to-value gap.
5. Guarantees: conditional or unconditional.
6. Naming: MAGIC formula.

Open: whether the book's ordered process includes market selection. Whether he says to apply the enhancers in this order at launch is not shown.

---

## Offer creation: the five enhancers

**Type:** FRM · **Prov:** [M*] · **Scale:** general; examples local fitness and cohort service · **Signals:** S-11.2, S-11.3, S-11.4 · **Files:** q02, q11

Applied after the core bundle:
1. **Scarcity:** cap supply (seats, slots, cohorts).
2. **Urgency:** cap time (deadlines, cohort start dates).
3. **Bonuses:** address specific remaining objections or future problems, instead of discounting.
4. **Guarantees:** conditional, unconditional or service (q02 lists only these three).
5. **MAGIC naming:** Magnet, Avatar, Goal, Interval, Container.

Examples in q11, all marked "e.g." and possibly NotebookLM's, not his lines:
- scarcity: "Only accepting 5 new clients per week"
- urgency: "Next cohort starts Monday"
- service guarantee: "We work for free until you hit your goal"
- MAGIC name: "Free 6-Week Lean-Down Challenge"

Warning attached (q02, q11): avoid the race to the bottom; charge premium prices so you can invest heavily in client success; use bonuses instead of discounts.

Detail for each enhancer: guarantees.md, scarcity-and-urgency.md and bonuses-and-naming.md.
