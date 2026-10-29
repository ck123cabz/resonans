---
type: corpus
aliases: ["Money Model"]
corpus: alex-hormozi
layer: retrieval
tags: [cac, corpus, ltgp, machine, money-model, payback, unit-economics]
source: skills/corpus-ingestion
created: 2026-10-16
file: money-model
sources: q73, q74, q75, q76, q77, q97, q99, Q100, q102, q103, q108
---

# Money Model

Layer 2 retrieval index, layer two ($100M Money Models and $100M Lost Chapters). One
framework, formula or number set per `##` heading, each section self-contained. Built from Pass
1 blocks G and I and the Pass 2 "Layer two" section (L2.1 to L2.6), which overrides Pass 1.

**Provenance key.** `[D]` the words were matched to his own audio (Pass 2 §2 or L2.1 lists each
match). `[M*]` NotebookLM transcribed the audio and chose the words: his idea, someone else's
phrasing. `[A]` the sources are silent. **Type:** FRM framework, NUM number set, SCR script, PRN
principle, MEC mechanism, WRN warning, CLM claim about a result, BIO what he did. Prices are US
dollars.

**Standing caution.** The NotebookLM notebook holds both layers (Offers, Leads, 29 videos, Money
Models, Lost Chapters). An answer can pull from any of them and cites by number, not by book, so
a layer-two answer is not proof that the idea is in a layer-two book. None of the formulas or
worked examples below was matched to the audio; L2.1 matched offer structures, not this lane.
Where two answer files give different values, both are printed with their files.

---

## Money model: definition

**Type:** FRM · **Prov:** [M*] · **Scale:** general · **Signals:** S-73.1 · **Files:** q73, q77

A money model is a deliberate sequence of offers that solves a customer's problems step by step.
Each offer that solves a problem reveals a new problem, and the next offer solves that one.

At the business level it is built to raise three things: how many customers you get, how much
they pay, and how fast they pay it.

A "$100M money model" makes enough gross profit in the first 30 days (30-day gross profit well
above CAC) that one customer pays to acquire multiple new customers. That removes cash as the
limit on scaling. q77 words it as one customer paying to acquire "and service" multiple new
customers.

---

## Money model: four offer types in three stages

**Type:** FRM · **Prov:** [M*] · **Scale:** general · **Signals:** S-73.2, S-99.5 · **Files:** q73, q77, q99

Four offer types, grouped in three stages, built in this order:

1. **Stage 1, Get Cash: attraction offers.** Turn strangers into customers at low cost and make
   gross profit in the first 30 days to cover or offset acquisition costs (q77 adds delivery
   costs). q99: start with a low-friction hook, such as free, win your money back, or deep
   discount promotions.
2. **Stage 2, Get More Cash: upsells and downsells.**
   - Upsell offers solve the new problem the first offer created and raise 30-day gross profit
     per customer. q99 names classic, menu, anchor and rollover upsells.
   - Downsell offers capture revenue from people who say no, by changing payment terms (payment
     plans), the trial structure (trial with penalty), or the features (remove features to lower
     the price).
   - q99 sets the stage target at 30-day gross profit ≥ 2x CAC.
3. **Stage 3, Get the Most Cash: continuity offers.** Ongoing value for a recurring payment
   (subscriptions, memberships, rollover contracts, waived-fee agreements) until the customer
   cancels, to maximise lifetime gross profit.

Each named offer type sits in Money Models as follows (q102): money model, Parts 1 and 2; four
offer types, Part 2; win your money back and giveaways, Part 3; decoy, buy X get Y free, pay less
now or pay more later, Part 4; classic, menu, anchor and rollover upsells, Part 5; payment plan,
trial with penalty and feature downsells, Part 6; continuity bonus, continuity discount and
waived fee, Part 7; building a money model, Parts 8 and 9. Pass 2 L2.1 confirms from the audio
that four upsell types are named (classic, menu, anchor, rollover) and three downsell families
(payment plan, feature, trial with penalty) `[D]`.

---

## Money model: rental car example

**Type:** FRM · **Prov:** [M*] · **Scale:** large consumer business · **Signals:** S-73.3 · **Files:** q73

Sequential offers at a car rental counter:
1. Offer 1, the rental booking (attraction).
2. Offer 2, a vehicle upgrade (upsell).
3. Offer 3, late return, gas prepay or insurance (upsell or downsell).

---

## Money model: where it sits among the books

**Type:** BIO · **Prov:** [M*] · **Scale:** general · **Signals:** S-77.1, S-102.3 · **Files:** q77, q102

- $100M Offers answers "What should I sell?"
- $100M Leads answers "How do I find these people?"
- $100M Money Models answers "How do we get them to buy it?"

Money Models Part 8 is "Make Your Money Model". Part 9 is "Ten Years in Ten Minutes".

Lost Chapters map as q102 gives it: Section B holds the unit economics. CFA, chapters 7 and 13.
CAC, chapters 8 and 10. LTGP, chapters 8 and 11. Payback period, chapters 8 and 12. OPM, chapter
12. The three levers, chapters 8 and 9. CFA levels, chapter 13. Section D: cost per engaged lead,
chapter 24. Chapter numbers are NotebookLM's and were not checked against the 26 Lost Chapters
items.

---

## Customer financed acquisition: the three levels

**Type:** FRM · **Prov:** [M*] · **Scale:** general · **Signals:** S-74.1, S-74.3, S-99.2 · **Files:** q74, q75, q76, q99

Customer Financed Acquisition (CFA): customers' own payments fund the acquisition of the next
customers. Measured on the first 30 days.

**30-day gross profit = 30-day revenue minus 30-day direct fulfilment costs.**

| Level | Test | What it means |
|---|---|---|
| 1 | 30-day GP < CAC | You may come out ahead over the lifetime, but it takes months or years. You float the business on savings, credit lines, loans or venture capital. |
| 2 | 30-day GP = CAC (q74: ≥ 1x CAC) | Every customer pays for themselves. Fund ads on a business credit card with 30-day interest-free terms and pay it off from gross profit. The credit limit becomes the maximum ad budget: a $5,000 limit caps acquisition at what $5,000 of CAC buys. |
| 3 | 30-day GP ≥ 2x CAC | Each customer pays for their own acquisition plus at least one more. Removes the cash constraint. |

- q76 labels Level 2 "Good" and Level 3 "Ideal / Minimum Standard".
- Making 2x CAC in 30 days is his minimum standard for scaling a bootstrapped business (q75,
  q76).
- q99 sets the baseline as 30-day GP > CAC at minimum, ideally ≥ 2x CAC.

Wording differences, kept: q75 defines CFA itself as "30-day GP > CAC" and then sets Level 2 at
"=". q75 says Level 3 funds "two (or more)" new customers. At exactly 2x CAC the surplus funds
one, as q74 says.

---

## Customer financed acquisition: worked Level 3 example

**Type:** NUM · **Prov:** [M*] · **Scale:** general · **Signals:** S-74.2 · **Files:** q74

- CAC: $1,000.
- Upfront program price: $2,500.
- Direct fulfilment (materials, coaching labour): $500.
- 30-day GP: $2,500 − $500 = $2,000.
- $2,000 ≥ 2 x $1,000, so Level 3.
- The $2,000 clears the $1,000 CAC and leaves $1,000 to fund new customers next month.

Error in the answer: it says the leftover $1,000 funds "2 new customers" at a $1,000 CAC. It funds
one.

---

## Customer financed acquisition: the compounding series

**Type:** NUM · **Prov:** [M*] · **Scale:** general · **Signals:** S-75.1, S-75.2 · **Files:** q75

Level 3, starting with 1 customer and reinvesting all extra profit, total customers over 12
months as q75 gives them: 1, 3, 7, 15, 31, 63, 127, 256, 511, 1,023, 2,047, 4,095.

The series is 2^n − 1, so the eighth term should be 255, not 256. Likely an answer or
transcription error.

His claim (CLM): in his first year at Gym Launch he made $100 in gross profit within 30 days for
every $1 spent on advertising. A 100:1 thirty-day return. No outside record.

---

## Customer financed acquisition: the three levers

**Type:** FRM · **Prov:** [M*] · **Scale:** general · **Signals:** S-75.3, S-99.1, S-102.2 · **Files:** q75, q76, q99, q102

1. **Lever 1, get more customers:** lower CAC.
2. **Lever 2, make them worth more:** raise LTGP.
3. **Lever 3, do it fast:** shorten the payback period (PPD).

q99's definitions under each lever:
- CAC = total marketing, sales and support spend ÷ customers acquired, counting ad spend, sales
  commissions and salaries, marketing software, media buyers and creative production. q99 puts
  "support" spend in CAC; q102 does not.
- LTGP = gross profit per transaction × average number of transactions, where gross profit =
  price paid minus direct fulfilment costs.
- Payback period: the time until a customer's gross profit covers their acquisition cost (GP ≥
  CAC).

OPM, "Other People's Money" (Lost Chapters Section B, ch. 12 per q102): here it means using
customers' gross profit to fund growth, instead of debt or outside investors.

"CAC can only approach zero, but LTGP can go to infinity" (q74, q99).

---

## Customer financed acquisition: the order to pull the levers

**Type:** PRN · **Prov:** [M*] · **Scale:** general · **Signals:** S-75.4, S-99.5 · **Files:** q75, q77, q99

The pull order is not the lever numbering. q75:
1. Lower CAC with attraction offers to create flow.
2. Shorten payback with upsells and downsells right after the first purchase, until 30-day GP ≥
   CAC (or ≥ 2x CAC).
3. Raise LTGP with continuity offers on the back end.

The maxim, in two wordings: "Create flow, monetize flow, then add friction" (q75) and "Generate
flow, monetize flow, then add friction" (q99). Pass 2 L2.4 row 20: same maxim.

q77's operational order:
1. Get customers reliably.
2. Make sure they pay for themselves reliably.
3. Make sure they pay for other customers reliably.
4. Maximise each customer's lifetime value.
5. Spend as many ad dollars as possible.

In an existing business the 3x industry CAC test (see "Diagnostic: CAC against 3x the industry
average") can override this order. Layer one holds the same maxim for the front end: see
`free-work-trials-and-first-customers.md` § Front end: create flow, monetise flow, then add
friction.

---

## CAC: formula and what to count

**Type:** FRM · **Prov:** [M*] · **Scale:** general · **Signals:** S-74.6, S-99.1, S-100.5 · **Files:** q74, q75, q76, q99, Q100

**CAC = total marketing and sales costs ÷ new customers acquired.**

Count: ad spend, sales and media payroll, commissions, software, creative overhead. q99 adds
support spend and media buyers.

Warning (Q100): counting only ad spend, and leaving out media buyer payroll, creative production,
tracking software and sales commissions. Example: an owner thought a $1,000 sale cost $200 in ad
spend; true CAC with software, commissions and payroll was $500. Cost: large profit shortfalls at
month end. In scaling companies this mistake can decide between making $1M a month, making $10M
a month, or going out of business.

---

## CAC: worked examples by channel

**Type:** NUM · **Prov:** [M*] · **Scale:** small outreach, content and paid-ads businesses · **Signals:** S-75.5 · **Files:** q75, q76

Identical in both files. Arithmetic checks.

| Channel | Costs | Customers | CAC |
|---|---|---|---|
| Outreach | $200/month software + $3,000/month cold email manager + $800 commission ($100 x 8 sales) = $4,000 | 8 | $500 |
| Content | 2 media staff at $5,000/month ($10,000) + $1,000 commission ($100 x 10) = $11,000 | 10 | $1,100 |
| Paid ads | $4,000 media buyer + $20,000 ad spend + $1,000 tracking software + $10,000 commission ($1,000 x 10) = $35,000 | 10 | $3,500 |

---

## CAC from payroll: cost per engaged lead

**Type:** FRM · **Prov:** [M*] · **Scale:** business with paid lead-getting staff · **Signals:** S-97.14, S-97.15 · **Files:** q97, q102

**Cost Per Engaged Lead (CPEL) = Total Payroll ÷ Total Engaged Leads Generated.** q102 words the
numerator "Total Marketing & Sales Employee Payroll" (Lost Chapters Section D, ch. 24).

Worked example:
- $100,000 payroll ÷ 1,000 engaged leads = $100 CPEL.
- 1 in 10 engaged leads becomes a customer: CAC = $100 × 10 = $1,000.
- LTGP $4,000: LTGP:CAC = 4:1.

His benchmark (CLM): an Acquisition.com content team costing $100,000/month that produces 30,000
engaged leads a month comes to $3.33 per engaged lead in payroll.

This is the only formula in the layer-two set that makes labour the acquisition cost. Layer one's
lead-magnet version (a $25 hard cost plus $75 of ads per engaged lead call) is in
`free-work-trials-and-first-customers.md` § Lead magnet economics: cost per engaged lead.

---

## Gross profit: formula and worked examples

**Type:** NUM · **Prov:** [M*] · **Scale:** product and service · **Signals:** S-74.6, S-75.6 · **Files:** q74, q75, q76

**Gross profit = price minus direct cost of fulfilment.**

- Widget: sold for $100, $20 fulfilment and shipping, GP $80 (80% margin). If the average
  customer buys 4 times, LTGP = $320 (the "4 times, $320" part is in q76 only).
- Service: 10 packages at $1,000 ($10,000), fulfilled by 1 employee paid $2,000, GP $8,000, which
  is $800 per customer.

---

## LTGP: formulas for recurring and product businesses

**Type:** FRM · **Prov:** [M*] · **Scale:** general · **Signals:** S-74.6, S-74.12, S-99.1 · **Files:** q74, q75, q76, q99

- **Recurring business:** LTGP = monthly gross profit per client ÷ monthly churn (as a decimal).
- **Product business:** LTGP = average gross profit per transaction × number of transactions per
  customer.
- **Monthly churn** = clients lost in the period ÷ clients at the start of the period.
- **Average lifespan in months** = 1 ÷ monthly churn.

q102 prints the acronym as "LTGP / LDGP / LCGP / LZGP". The three extra forms look like
transcription errors, not separate terms.

---

## LTGP: worked examples

**Type:** NUM · **Prov:** [M*] · **Scale:** subscription, agency-style service, illustrative · **Signals:** S-74.7, S-75.7, S-75.8 · **Files:** q74, q75, q76

**Subscription (q74).** $300/month price, $60/month fulfilment, monthly GP $240. Churn 5%. LTGP =
$240 ÷ 0.05 = $4,800. $15,000 monthly sales and marketing spend brings 10 customers: CAC $1,500.
LTGP:CAC = 3.2:1, above the 3:1 threshold, so paid marketing can scale. Arithmetic checks; the
tidy figures may be the model's own construction around the formula.

**Agency-style service (q76).** Client pays $3,000/month. One account rep costs $6,000/month and
serves 10 clients. Revenue per rep $30,000/month, GP per rep $24,000/month (80% margin), GP per
client $2,400/month. At 5% monthly churn, LTGP = $2,400 ÷ 0.05 = $48,000. Arithmetic checks. The
closest example in the set to a retainer.

**Lemonade stand (q75).** $400,000 sales and marketing spend over 12 months acquires 10,000
customers: CAC $40. $10/month subscription, $2/month fulfilment (powder, water), monthly GP $8
(80% margin). Average retention 5 months: LTGP $40. At CAC $40 and LTGP $40, LTGP:CAC is 1:1.
The same stand has CAC $20 in the payback example (see "Payback period: worked examples"); the
answer does not say whether these are two stages of one story.

---

## LTGP to CAC: benchmarks

**Type:** NUM · **Prov:** [M*] · **Scale:** general · **Signals:** S-74.4, S-74.5 · **Files:** q74, q76

| Ratio | Reading |
|---|---|
| Below 3:1 | Advertising is inefficient or the model is under-monetised |
| 3:1 | Minimum healthy |
| 5:1 to 10:1+ | World class |

q76 example: $3,000 LTGP for a $1,000 CAC. Layer one ($100M Leads) holds the same 3:1 floor; the
answer may blend the two books.

His claim (CLM): his personal portfolio's lifetime average LTGP:CAC is 36:1. No record.

---

## Payback period: formula and target

**Type:** NUM · **Prov:** [M*] · **Scale:** general · **Signals:** S-74.8 · **Files:** q74, q76

**Payback period = time for cumulative gross profit to equal CAC.** q76 writes it as CAC ÷ gross
profit collected per month or per day.

- Target: 30 days or less (q76: "under 30 days").
- Ideally 0 to 14 days (q74 only).
- Longer than 30 days ties cash up in working capital and slows reinvestment cycles by 4x or more
  compared with a 30-day turnaround (q74).

---

## Payback period: worked examples

**Type:** NUM · **Prov:** [M*] · **Scale:** service, subscription, illustrative · **Signals:** S-74.9, S-75.9, S-75.10, S-75.11 · **Files:** q74, q75, q76

**30 days (q74).** CAC $800. $500/month service, $100/month fulfilment, GP $400/month. Month 1
payment leaves $400 unrecovered. Month 2 payment (day 30) brings cumulative GP to $800. Payback =
30 days.

**31 days (q75, q76).** CAC $100. Customer brings $50/month GP. Day 1 payment collects $50, day 31
payment collects the remaining $50. Payback 31 days. Same two-payment pattern as the 30-day case,
counted differently.

**Slow against fast, lemonade stand (q75, q76).**
- Slow: CAC $20, GP $8/month. Day 0 −$20. Day 30 +$8 (net −$12). Day 60 +$8 (net −$4). Day 90 +$8
  (net +$4). q75 states the slow payback as 75 to 90 days, q76 as 60 to 90 days. By the
  day-by-day figures, payback comes at the day-90 payment.
- Fast (CFA-optimised): CAC $1 on day 0. Day 7 the customer pays $10 ($8 GP); the $1 CAC is
  recovered with $7 left. Day 8, reinvest $7 to get 7 new customers. Day 14, those 7 bring $56
  GP. By day 60 the account holds $225+ from the original $1 (the $225+ is in q75 only). Payback 7
  days.

**Upsell fix (q75).** $15/month subscription, $5 fulfilment, $10/month GP. Retention 10 months,
LTGP $100. CAC $30. Month 1 GP is $10, a −$20 gap, payback 3 months. Add a $100 upsell at 100%
margin that 1 in 5 new customers buy: $20 average GP per customer. New 30-day GP = $10 + $20 =
$30, equal to CAC. Payback 30 days, "free customers for life". Arithmetic checks. This reaches
Level 2, not Level 3.

---

## Churn and lifespan: the 5% target and net organic growth

**Type:** NUM · **Prov:** [M*] · **Scale:** subscription business · **Signals:** S-74.12, S-108.3 · **Files:** q74, q108

- Monthly churn target: 5% or less. 5% monthly churn = 20-month average lifespan (1 ÷ 0.05).
- **Net organic growth (q74), the referral growth equation (q108):** monthly compounding growth %
  = % of clients referring each month − % of clients churning each month. If referrals exceed
  churn, the business compounds with $0 ad spend.
- Worked example (q74): 200 clients. 8 cancel: churn 4%, lifespan 25 months. 12 referred: 6%. Net
  organic growth +2% a month. Arithmetic checks.

---

## Diagnostic: CAC against 3x the industry average

**Type:** FRM · **Prov:** [M*] · **Scale:** business with an industry CAC benchmark · **Signals:** S-74.10, S-99.3, S-99.4 · **Files:** q74, q75, q76, q99, q103

Compare your CAC with the industry average first.

- **More than 3x the industry average:** an advertising or sales problem. Fix targeting, ad
  creative or closing. Ask the question in "Diagnostic: high CAC, advertising or sales".
- **Within 3x:** advertising is adequate. Stop pushing CAC down and work the business model to
  raise LTGP (pricing, upsells, retention, continuity), because "CAC can only approach zero, but
  LTGP can go to infinity".

Worked example (q74): industry CAC $300.
- Your CAC $600 (2x): the bottleneck is LTGP. If LTGP is $500, LTGP:CAC is under 1:1.
- Your CAC $1,200 (4x): targeting or closing is broken.

Limit noted in Pass 1: the test needs a published industry CAC to compare against.

---

## Diagnostic: high CAC, advertising or sales

**Type:** FRM · **Prov:** [M*] · **Scale:** general · **Signals:** S-76.1, S-97.16, S-76.2 · **Files:** q76, q97, q99

The one question: **"Do my engaged leads have the problem I solve and the money to spend?"**

| Answer | Problem | Fix |
|---|---|---|
| No | Advertising: wrong people | Targeting, lead magnets, messaging or avatar |
| Yes, but not enough leads | Advertising: volume | More volume, better creative, more split-testing |
| Yes, leads exist but do not buy | Sales | Scripts, close rate or reps. Do not fire the ad team for a sales problem |

If CAC is within 3x the industry average, stop working on CAC and raise LTGP.

Figure he gives (q76, unsourced as given): the top 0.1% of advertisers split-test 11x more creative
than average. Layer one holds it too.

---

## Diagnostic: low LTGP, the seven levers

**Type:** FRM · **Prov:** [M*] · **Scale:** general · **Signals:** S-76.3 · **Files:** q76

When LTGP is too low ("the arms race of business"), pull these levers:

1. **Raise prices**, the strongest lever. At 20% margins a 20% price rise doubles profit ($100
   price, $20 profit; $120 price, $40 profit).
2. **Cut fulfilment cost:** vendor pricing, one-to-many delivery, streamlining.
3. **Resells and subscriptions:** turn one-off sales into continuity.
4. **Upsells:** classic, menu, anchor, rollover.
5. **Cross-sells:** for example supplements with workout programs.
6. **Downsells:** payment plans, feature downsells, trials with penalties.
7. **Reduce churn:** higher-quality prospects churn less; deliver value fast; continuity retention
   bonuses and upgrades.

Aim for 80%+ gross margins on services and digital offers, so there is margin left to outspend
competitors on ads.

The answer introduces "six primary levers" and lists seven. All seven are kept.

---

## Diagnostic: slow payback, five ways to pull cash forward

**Type:** FRM · **Prov:** [M*] · **Scale:** general; recurring services · **Signals:** S-76.4 · **Files:** q76

When payback is too long (60, 90 or 180+ days locks capital):

1. **Upfront upsells at checkout:** high-margin digital products, onboarding fees, physical
   products.
2. **Prepay discounts** of 10% to 20%, or bonuses, for prepaying 3, 6 or 12 months.
3. **Layaway or an upfront deposit** of 1/3 or 50% before delivery starts.
4. **One-time setup or initiation fees** on top of monthly fees.
5. **Bill every 4 weeks** (13 cycles a year) or bi-weekly on paydays instead of monthly.

This confirms layer one's "change terms" as delayed payment and layaway: see `pricing-and-tiers.md`
§ Discounting: add value, change terms, fence the offer, and `free-work-trials-and-first-customers.md`
§ First payment: large down payment and layaway. The setup-fee structure is worked in full in
`attraction-offers.md` § Discount plus setup fee: both worked cases.

---

## Money model ratios: rollover and continuity multiples

**Type:** NUM · **Prov:** [M*] · **Scale:** general; membership business · **Signals:** S-74.13, S-74.14, S-86.6 · **Files:** q74, q86, q92 to q96

**Rollover upsell ratio (q74).** The backend offer price must be at least 4x the credit or
discount given, which keeps the discount at 25% or less. Example: roll a $500 challenge deposit
into a backend offer priced at least $2,000.

**Continuity take-rate pricing (q74).** Set the standalone one-time price as a multiple of the
monthly continuity price:

| Standalone price | Share choosing continuity |
|---|---|
| 1.33x monthly | 50% |
| 2.33x monthly | 80% |
| 2.66x monthly | 90% |

q74 example: $200/month membership; for 80% to choose recurring, price the one-time option at
$466 ($200 x 2.33). "2.66x" is kept as given (2.67 if rounded from 2 2/3).

Do not use these ratios as rules. Pass 2 L2.4 row 22: in the lane-18 answers the worked figures
($399, $699, $799 against $199/month) fit a $299 monthly price, not $199. How the multiples map to
take rates is not explained in any answer.

---

## Making your own money model: the four steps

**Type:** FRM · **Prov:** [M*] · **Scale:** general · **Signals:** S-77.2 · **Files:** q77

1. **Start with an attraction offer.** Figure out what you sell, pick the best way to present it,
   advertise it. His favourites: Win Your Money Back, Giveaways, Decoy Offer, Buy X Get Y Free,
   Pay Less Now or Pay More Later. Each is in `attraction-offers.md`.
2. **Pick an upsell** to drive 30-day profit well above acquisition and delivery cost.
   - Classic Upsell: "You can't have X without Y."
   - Menu Upsell: prescribe what they need, unsell what they don't.
   - Anchor Upsell: most expensive option first.
   - Rollover Upsell: credit past purchases toward the next offer.
3. **Pick a downsell** to turn a no into a yes.
   - To keep the price, change how they pay: Payment Plan Downsell, Trial with Penalty.
   - To charge less, change what they get: Feature Downsell.
   - Alternate payment plans and feature downsells in the sales conversation.
4. **Pick a continuity offer** to get one last sale inside the 30-day window and stack recurring
   cash.
   - Continuity Bonus: a bonus if they sign today.
   - Continuity Discount: free time for signing today.
   - Waived Fee: waive a setup fee in exchange for a commitment.

---

## Making your own money model: one offer at a time, and the rules

**Type:** PRN · **Prov:** [M*] · **Scale:** general; new offer · **Signals:** S-77.3, S-77.4, S-77.5 · **Files:** q77

- **Perfect one offer at a time.** Implementing the whole money model at once "will break your
  business". Pick one offer, test it until it works reliably, make it automatic, then move to the
  next stage.
- **Measure in quarters, not weeks.** "Build it right or build it again and again."
- **Simple scales, fancy fails.** Have 100 ways to offer one product rather than 100 products. 1,
  2, 3 or 4 training sessions a week turns one product into four offers.
- **Affiliate products** can fill any stage without adding operations.
- **No rigid rules.** Offers can be mixed and inverted: a continuity offer as an attraction offer,
  a rollover upsell on a 12-month commitment.
- **Price new offers low** enough to get a flood of yeses, use customer feedback to refine
  delivery, then raise prices until profit peaks. This matches layer one's free-then-step-up
  ladder: `free-work-trials-and-first-customers.md` § Price step-up after the free five:
  80/60/40/20.

The question asked for a worksheet or checklist. The answer gives these rules, not a worksheet.

---

## Money model example: the microgym

**Type:** FRM · **Prov:** [M*] · **Scale:** local gym · **Signals:** S-73.4, S-101.3 · **Files:** q73, q77, q79, q101

| Stage | Offer | Detail |
|---|---|---|
| 1, attraction | Win Your Money Back challenge | $600 deposit for a 6-week fitness challenge; 100% back as cash or store credit if the client hits the goal |
| 1, downsell | Payment plan | For those who cannot pay $600 up front. q77 adds trial with penalty |
| 2, upsell | Menu upsell | Personalised supplement bundles or done-for-you nutrition |
| 2, downsell | Feature downsell | A smaller supplement package. q77: big bundle against small bundle against monthly subscription |
| 3, continuity | Rollover upsell plus lifetime discount | Roll the $600 deposit into a 12-month membership at $50 off a month |

Rollover arithmetic (q79): $50/month credit for 12 months against a $200/month membership; the
client nets $150/month. $50 x 12 = $600, which matches the deposit.

Deposit readings: q73 gives $600; q101 gives his own challenge as $500 down; layer one gives $500
(see `free-work-trials-and-first-customers.md` § Free with deposit: the $500 challenge and refund
versus credit). Both kept.

---

## Money model example: dog food

**Type:** FRM · **Prov:** [M*] · **Scale:** e-commerce, physical product · **Signals:** S-73.5 · **Files:** q73, q77, q78

- **Attraction:** Buy X Get Y Free. Buy 4 months of food, get 2 months free.
- **Upsell:** classic upsell of dog toys, treats or health vitamins at checkout (q77: monthly toys
  or vitamins).
- **Downsell:** feature downsell. Strip the add-ons and sell just the premium food.
- **Continuity:** automatic month-to-month renewal after the initial 6-month supply runs out.

Stage label differs: q73 puts the downsell in Stage 3, q77 in Stage 2. The three-stage frame puts
downsells in Stage 2.

This example gives fewer free months than paid ones (buy 4, get 2), against the rule in q79 that
the free part should be larger. See `attraction-offers.md` § Buy X Get Y Free: structure and the
more-free rule.

---

## Money model example: Gym Launch

**Type:** FRM · **Prov:** [M*] · **Scale:** Gym Launch, B2B services · **Signals:** S-77.6, S-77.7 · **Files:** q77, q79

| Stage | Offer | Detail |
|---|---|---|
| Attraction | Decoy offer | Free DIY materials against $16,000 done-with-you licensing |
| Upsell | Classic upsell | $42,000/year ($36,000 prepaid) for advanced business services (Gym Lords) |
| Downsell | Payment plan | $10,000 down, the rest over 52 weeks ($800/week) |
| Continuity | Menu close plus feature downsell | Full package at $800/week down to single features: done-for-you ads $300/week, sales training $200/week, tech support/license $100/week minimum package |

Arithmetic problems, kept as given: $42,000 less $10,000 down over 52 weeks is about $615/week, not
$800; $800 x 52 = $41,600 before the $10,000 down. The answer may have joined two price points.
Calling a menu close plus feature downsell "continuity" mixes stage types. This is a downsell
ladder by feature, not a three-tier menu.

His claim (CLM, q79): Gym Launch went from zero to $476,000 per month in 3 months using the decoy
offer. No record.

Layer one holds the [D] figures for the $16,000 intensive and the 35% upsold to $42,000 a year:
`pricing-and-tiers.md` § Pricing case: Gym Launch $16,000 intensive and the $42,000 upsell.

---

## Money model example: the newsletter

**Type:** FRM · **Prov:** [M*] · **Scale:** digital product · **Signals:** S-77.8 · **Files:** q77, q79

- **Attraction:** free trial.
- **Upsell and continuity:** Pay Less Now or Pay More Later plus a lifetime discount. Pay $297 up
  front to lock that rate for life.

---

## The ten-year view

**Type:** PRN · **Prov:** [M*] · **Scale:** general; personal · **Signals:** S-77.9, S-77.10 · **Files:** q77

Money Models Part 9, "Ten Years in Ten Minutes":

- "The bigger your goals, the longer time horizons need to be. You want to play games where if you
  wait, you win."
- Most entrepreneurs take about 5 years to figure out "which way is North" (a model that works)
  and another 5 to build generational wealth.
- **The Doom Loop:** jumping to new opportunities in hard phases resets the clock to year 0
  instead of compounding into years 5 to 10.
- Never interrupt compounding (Charlie Munger: the eighth wonder of the world).
- Business is an infinite game. The goal is to stay in business and keep improving.

His own statement (BIO): crossing $100M in net worth took him and his wife over a decade of
continuous effort.

---

## Money model with no ad budget

**Type:** FRM · **Prov:** [A] · **Scale:** $0 ad budget · **Signals:** S-108.12, Pass 2 L2.2 · **Files:** q108

Not covered. The sources hold rules for getting customers with no ad budget, but nothing says how
the attraction, upsell, downsell and continuity stages, or the 30-day GP ≥ CAC target, change when
the acquisition cost is labour instead of ad spend. The nearest formula is cost per engaged lead,
where payroll stands in as the acquisition cost (see "CAC from payroll: cost per engaged lead").
The zero-budget customer-getting rules are in `first-customers-layer-two.md` § Layer two on
no-ad-budget models.
