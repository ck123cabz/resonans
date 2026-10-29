---
type: corpus
aliases: ["Attraction Offers"]
corpus: alex-hormozi
layer: retrieval
tags: [attraction-offers, corpus, free-offers, machine, money-model, promotions]
source: skills/corpus-ingestion
created: 2026-10-16
file: attraction-offers
sources: q73, q77, q78, q79, q80, q81, q82, q83, q85, q87, q92, q93, Q100, q102, q104, q105, q106
---

# Attraction Offers

Layer 2 retrieval index, layer two ($100M Money Models and $100M Lost Chapters). One offer type,
script or number set per `##` heading, each section self-contained. Built from Pass 1 blocks G
and I and the Pass 2 "Layer two" section (L2.1 to L2.6), which overrides Pass 1. The front ends
for services, agencies, consultants and local businesses, the first avatar, and what layer two
adds on audits, free work, half-price starts, tiers and no-ad-budget models are in
`first-customers-layer-two.md`.

**Provenance key.** `[D]` the words were matched to his own audio (Pass 2 §2 or L2.1 lists each
match). `[M*]` NotebookLM transcribed the audio and chose the words: his idea, someone else's
phrasing. `[A]` the sources are silent. **Type:** FRM framework, NUM number set, SCR script, PRN
principle, MEC mechanism, WRN warning, CLM claim about a result, BIO what he did. Prices are US
dollars.

**Standing caution.** The NotebookLM notebook holds both layers. An answer can pull from Offers,
Leads or the videos, and cites by number, not by book. Where two answer files give different
values, both are printed with their files. Layer one's seven free-offer models (free bribe,
limited free offer, free trial plus penalty, free with deposit, free forever, free giveaway, free
with commitment) are the same family seen through the layer-one books: see
`free-work-trials-and-first-customers.md` § Seven free-offer models.

---

## Attraction offers: the full list by book

**Type:** FRM · **Prov:** [M*] · **Scale:** general · **Signals:** S-78.1, S-102.3 · **Files:** q78, q79, q102

An attraction offer is Stage 1 of the money model (Get Cash): it turns strangers into customers at
low cost and makes gross profit in the first 30 days to cover or offset acquisition. The money
model itself is in `money-model.md`.

**$100M Money Models, Section 2 (the five core):**
1. Win Your Money Back (Part 3)
2. Giveaways (Part 3)
3. Decoy Offer (Part 4)
4. Buy X Get Y Free (Part 4)
5. Pay Less Now or Pay More Later (Part 4)

**$100M Lost Chapters, Section A "Attract" and Section C "Advanced Offer Stacking":**
6. Free Presentations, ch. 17
7. Freemium, ch. 18
8. Free Pick Your Price, ch. 19
9. Premium Promotions, ch. 4
10. Free Promotions, ch. 5
11. Discount Promotions, ch. 6
12. Founding Member / Lifetime Discount, ch. 22
13. Free with Alternative Revenue Stream, ch. 20

Chapter numbers are NotebookLM's. q102 also lists Discount + One-Time Fee (ch. 23) and Lifetime
Upgrades (ch. 21); q92 files those three chapters (21 to 23) as continuity offers. q102 files Free
with Alternative Revenue Stream as an upsell. q80 calls free, premium and discount "promotional
wrappers" around the Grand Slam Offer rather than offers in their own right. q84 adds "Your First
Avatar" as Lost Chapters ch. 2.

---

## Win Your Money Back: structure

**Type:** FRM · **Prov:** [M*] · **Scale:** local gym, B2B consulting · **Signals:** S-78.2 · **Files:** q78, q79, q82

1. The customer pays a deposit.
2. If they hit a set goal or complete set actions within a set time (28 days to 6 weeks in the
   examples), they get the deposit back as cash or as credit toward a long-term backend offer.
3. Three criteria types:
   - **Results-based:** for example lose 20 lbs or 10% of body weight (q79); "20 lbs lost or 5%
     body fat down in 6 weeks" (q82). Both kept.
   - **Action-based:** attend all sessions, log daily, post weekly, attend check-ins.
   - **Action plus results.**
4. Mandatory check-ins (orientation, mid-point, final session) are required to qualify. They also
   create natural points to present the backend offer.
5. Winnings are rolled over as monthly credit toward a long-term contract, for example $50/month
   off a 12-month membership.

---

## Win Your Money Back: prices and conditions

**Type:** NUM · **Prov:** [M*] · **Scale:** local gym, B2B consulting · **Signals:** S-78.3, S-73.4, S-101.3 · **Files:** q73, q78, q79, q82, q101

| Example | Deposit | Length | File |
|---|---|---|---|
| Gym challenge | $500 or $600 | 6 weeks | q79 |
| Gym challenge | $600 | 6 weeks | q73 |
| Gym challenge | $500, or $300 | 6 weeks | q82 |
| His own challenge | $500 down | 6 weeks | q101 |
| Challenge | $500 | 8 weeks | q78 |
| 28-day blueprint | $400 (q78); "free ($0 deposit option)" (q82) | 28 days | q78, q82 |
| B2B lead challenge | $500 | 5 days | q78 |
| Consulting | $500 to $1,000 | not given | q82 |

Consulting conditions (q82): deposit $500, send 100 outbound messages a day, attend trainings, do
homework, attend a graduation call, get 100% back as cash or as credit toward higher-level
consulting.

Rollover arithmetic (q79): $50/month credit for 12 months against a $200/month membership; the
client nets $150/month; $50 x 12 = $600, the deposit.

No length or deposit is stated as the rule. Layer one's version (a $500 deposit, refund in the
book, credit in a later video) is in `free-work-trials-and-first-customers.md` § Free with
deposit: the $500 challenge and refund versus credit.

---

## Win Your Money Back: prerequisite and results

**Type:** CLM · **Prov:** [M*] · **Scale:** Gym Launch and its clients · **Signals:** S-78.4, S-78.5, S-78.6, S-78.7 · **Files:** q78, q79, q82

**Prerequisite (WRN, q78):** your product's standard refund rate should be under 5% before you run
it.

Results he reports, all his own figures with no outside record:
- Over $1 billion in total sales across his businesses and clients (q78, q79).
- $1.5 billion in total revenue across 45,000+ gyms over 7 years (q79). "45,000+" is likely a
  transcription error: layer one has him at 4,000+ gyms, and the independent record (Capstone
  Partners, grade A) gives 4,500+. The $1 billion and $1.5 billion are for the same offer.
- 78% to 80% of participants reach the goal.
- 2/3 of challenge completers convert into long-term memberships.
- About 10% of customers ask for the cash back rather than rolling over.
- With rollover upsells and payment plans, Gym Launch scaled from $300,000/month to $1.5
  million/month.
- Ad costs liquidated up front from $500 initial cash plus $200 to $300 in supplement upsells
  within 48 hours.

Separate offer, confirmed in layer one `[D]`: in his early gym days 2 of 4,000 clients asked for a
refund under the unconditional guarantee (q79).

Third-party example (q78, q82): Volvo. Drive a car 1,000,000 miles with dealer servicing and get a
free new car.

---

## Giveaways: structure

**Type:** FRM · **Prov:** [M*] · **Scale:** local services, consulting · **Signals:** S-78.8 · **Files:** q78, q79

1. Advertise a chance to win a high-value grand prize in exchange for contact details and survey
   answers (for example "Why should we pick you?").
2. Run a 3- to 7-day countdown.
3. Pick 1 public grand prize winner.
4. Contact everyone else privately within 7 days with a promotional offer (partial scholarship,
   gift card or voucher), because their application was compelling. The discount is justified as
   a reward for applying.
5. Put a 7-day deadline on claiming the promotional offer.

**Two-prize viral play:** if a friend an entrant refers wins, the entrant wins a second grand prize
too. Doubles lead volume.

The promotional discount: q79 calls it "a 10%–30% discount off gross margins", a phrase that does
not parse cleanly. Pass 2 L2.3: q103 turned this 10% to 30% into a cap on all promotional
discounts, which goes beyond the source. It applies to the giveaway scholarship, gift card or
voucher only.

---

## Giveaways: prizes, vouchers and results

**Type:** NUM · **Prov:** [M*] · **Scale:** local services, consulting · **Signals:** S-78.9, S-78.10 · **Files:** q78, q79, q82

| Business | Grand prize | Offer to everyone else |
|---|---|---|
| Dentist | $6,000 (invisible braces) | $2,000 gift voucher |
| Dog food | $1,000, one year | $300 voucher |
| Consulting | $12,000 16-week turnaround | $6,000 partial scholarship |
| Another | $5,000 value ($2,000 retail) | $1,800 promotional price |
| Gym | $50,000 equipment bundle | not given |

Results (CLM, q79): a compelling prize ($50,000 equipment bundle rather than low-value event
tickets) floods leads and "explains itself". Fitness certification case: a large volume of
qualified leads, and nearly all applicants who took the call bought on the spot because of the
anchor value of the full scholarship. No numbers given for the case.

---

## Decoy offer: structure

**Type:** FRM · **Prov:** [M*] · **Scale:** local services, B2B · **Signals:** S-78.11 · **Files:** q78, q79, q82

1. Advertise a stripped-down, free or very cheap version (the decoy) for volume.
2. When leads engage, show the decoy and a premium option side by side, or present the premium
   first by asking "Are you here for free stuff or lasting results?"
3. Decoy: minimal features. DIY Facebook group workouts, 1 session a month, a general meal plan,
   no support, no guarantee.
4. Premium: unlimited access, personalised plans, 1-on-1 coaching, a results guarantee.
5. The contrast makes the premium look far better.

A two-option comparison, not a three-tier menu.

Two definitions of "decoy", Pass 2 L2.3: q102 describes the cheap basic option as the decoy (as
above); q106 describes the middle-priced option as the decoy (The Economist, next section). The
Economist example uses the second.

---

## Decoy offer: prices and The Economist menu

**Type:** NUM · **Prov:** [D] for The Economist; rest [M*] · **Scale:** local services; magazine · **Signals:** S-78.12, S-106.3 · **Files:** q78, q79, q82, q106, Money Models p5

Decoy prices: $0, $1, $5, $6 or $21. Named decoys: free 21-day transformation; $5 VIP tanning pass;
$6 six-week stress release.

Premium prices: $399 (6-week intensive with 1-on-1 coaching and a guarantee); $299 or $399 (q82,
gym); $100/month; $16,000 (16-week done-with-you licensing against free DIY, Gym Launch).

Tanning: 70% to 80% of prospects take the $399 premium over the $5 decoy. q78 ties the figure to
tanning; q79 states it generally.

**The Economist** `[D]`, matched to Money Models part 5: $59 digital, $125 digital plus print, then
a print-only $125 decoy added. As q106 lays it out:
- A, digital: $59/year.
- B, the decoy, print only: $125/year.
- C, the target, digital plus print: $125/year.

B costs the same as C and gives less, so buyers mostly choose C. A third-party study (Ariely's),
not his business.

---

## Buy X Get Y Free: structure and the more-free rule

**Type:** FRM · **Prov:** [M*] · **Scale:** retail, services · **Signals:** S-79.1 · **Files:** q78, q79

1. Instead of a percentage discount, require a baseline quantity or commitment (X).
2. Give extra units or time (Y) free. Selling several units at once lets the free part be large.
3. **Rule:** always give away more free items than paid items. "Buy 1, Get 2 Free" beats "Buy 2,
   Get 1 Free". "Buy 6 months, Get 12 months free" beats "Buy 12 months, Get 6 months free".
4. Permanently raise the single-item retail price before launching, to protect margins.

The rule appears in q79 only, and other answers break it: q82 lists "Buy 12 months, get 6 months
free for $1,800", the form q79 says loses; the dog food money model is buy 4, get 2 free.

---

## Buy X Get Y Free: prices and results

**Type:** NUM · **Prov:** [M*] · **Scale:** retail, service contracts · **Signals:** S-79.2, S-79.3, S-106.4 · **Files:** q78, q79, q82, q106

- **Boot Factory, Nashville:** one pair normally $200. Offer: buy 1 pair for $600, get 2 pairs free
  ($600 up front, $200 a pair average).
- **Service agreement:** buy 6 months, get 6 months free for $1,800 ($150/month average). Second
  variant: "buy 6 months, get 12 months free for $1,800" (q79) or "buy 12 months, get 6 months
  free for $1,800" (q82). Both kept.
- **T-shirts:** buy 1 for $30, get 2 free (against 3 for $10 each); or buy 1 for $20, get 2 free
  (against 33% off).

Results (CLM, q79): large upfront cash and customers locked in 12 to 18 months prepaid instead of
month to month. The Nashville boot store dominated its strip because tourists made a $600
transaction, not $200. It out-converts percentage discounts because people understand
"free" better than percentages. No conversion numbers.

Do not use (Pass 2 L2.4 row 21): q106's three-version menu, all at $1,800 (buy 12 get 6, buy 6 get
6, buy 6 get 12). 12 paid months and 6 paid months cannot both cost $1,800; the figures are
garbled.

---

## Pay Less Now or Pay More Later: structure

**Type:** FRM · **Prov:** [M*] · **Scale:** local services, info product, e-commerce · **Signals:** S-78.13 · **Files:** q78, q79, q82

Offer a choice:
- **Pay Later:** $0 down today. Full price billed in 24 hours, 14 days or 30 days, only if
  satisfied or a clear result is reached. Carries a conditional guarantee: the buyer must attend
  or complete steps to qualify to cancel.
- **Pay Now:** pay today at a 20% to 50% discount with extra bonuses, giving up the pay-later
  guarantee.

Because the card is already captured for Pay Later, the Pay Now discount converts many to cash at
once. Keep cancellations under 10% by making the promised outcome clear, measurable and tied to
strict execution criteria.

---

## Pay Less Now or Pay More Later: prices

**Type:** NUM · **Prov:** [M*] · **Scale:** local services, info product, e-commerce · **Signals:** S-78.14 · **Files:** q78, q79, q82

| Example | Pay later | Pay now |
|---|---|---|
| Speed reading course | $0 down, $297 tomorrow; email to cancel if speed does not double | $97 today (67% off) plus bonus recordings |
| Clothing | $0 now, $149 in 14 days | $97 today plus a free accessory |
| Lawn care | $0 down, full cut plus hedges, $600 after service if satisfied | $369 today (cut, hedges and treatment) |
| Newsletter | not given | $297 today for a lifetime rate |

Lawn care upsell (q82): $199/month recurring maintenance. The closest local service in the set.

---

## Promotions: free, premium and discount are wrappers

**Type:** MEC · **Prov:** [M*] · **Scale:** general · **Signals:** S-80.1, S-80.3 · **Files:** q80, q82

Free, premium and discount promotions are not changes to the core offer. They are promotional
wrappers ("wrapping paper") placed around the Grand Slam Offer to make it more attractive to cold
markets and create demand flow. Never discount the core offer directly.

**Reason why.** Every free or deeply discounted offer needs a believable reason: grand opening,
inventory clearance, anniversary, beta testing, getting first testimonials, case-study selection,
launching a location, going out of business at 90% off. Without one, prospects assume a scam or
low quality.

Layer one's discounting rules are in `pricing-and-tiers.md` § Discounting: never discount the core
offer and § Discounting: promotional discount as the marketing hook.

---

## Free promotion: the penny gap and the split test

**Type:** CLM · **Prov:** [D] for the lead-cost line; rest [M*] · **Scale:** paid ads; 10 gym markets · **Signals:** S-80.2, S-80.4, S-80.5, S-80.7 · **Files:** q78, q80, q82, Lost Chapters ch. 5

**Matched to Lost Chapters ch. 5** `[D]`: the lead cost on a premium offer is "five to 10 times
higher", so the price has to be "at least five to 10 times higher"; "free makes more money".

**Penny gap (Dan Ariely, as he cites it):** dropping a price from 1 cent to free raises demand
sharply. About 9x more people take a free item than one priced at 1 cent (free Hershey's Kiss
against a 1-cent Kiss).

**His split test (CLM):** across 10 gym markets, free front-end offers cut lead costs by 5x to 10x
(q80; q78 says "5x or more"), with close rates and average ticket virtually identical between
free-offer and non-free-offer leads. No record.

**Free money math (q80, illustrative):**
- $1,000 of ads on a free offer: 500 leads (250 qualified, 250 unqualified).
- $1,000 on a non-free offer: 200 leads (160 qualified, 40 unqualified).
- Free yields 250 qualified prospects against 160, so it wins on dollars even though its
  qualified share is lower. Assumes ad spend, not outreach.

His line (SCR, mediated): "If I only had one offer to make to convert or my family would be
killed, it would be a free offer."

---

## Free promotion: when it fits

**Type:** PRN · **Prov:** [M*] · **Scale:** local, new business · **Signals:** S-80.6 · **Files:** q80

- Entering cold markets where prospects do not know you.
- The goal is maximum lead volume at the lowest CAC.
- Small local markets with few buyers, where you need every hand-raiser.
- Starting out: no social proof, needing fast testimonials, lacking sales conviction, or wanting
  referral flow.

When free fails, from layer one's re-run q39: `free-work-trials-and-first-customers.md` § When free
works and when it fails.

---

## Premium promotion

**Type:** FRM · **Prov:** [M*] · **Scale:** high-ticket · **Signals:** S-80.8, S-80.9, S-80.10, S-80.11 · **Files:** q78, q80

**Structure.** Present the Grand Slam Offer on its own at full price, with no discount or free
wrapper. Compete on value, perceived outcome, bonuses and creative guarantees. It skims the most
qualified, price-insensitive buyers. q78 only: it enables 3x to 5x higher price points without
changing the core service, at about 10% of the customer volume of cheaper models, with much
higher margins.

**Premium math (q80).** Business A sells a $100 product with $50 profit. Business B sells a $10,000
package with $9,500 profit. To make $9,500, A needs 190 sales; B needs 1. Show the $10,000 offer to
190 prospects and close 5% (9.5 sales): $90,250 profit (9.5 x $9,500), 9.5x more profitable
advertising, with under 10 clients against 190. Arithmetic checks.

**Examples (illustrations, not his businesses):** a luxury restaurant's $50,000 burger with caviar
and gold flakes; a $10,000 done-with-you package in place of a $100 course; high-alkalinity organic
lemonade from specific orchards sold to health nuts. q78 lists high-ticket consulting and
executive coaching without citations; they may be the model's additions.

**When it fits (WRN).** You already have a proven high-value product and a sales process that shows
the value, and want fewer, easier, higher-margin customers. Do not start with a standalone
premium offer if you are brand new, lack conviction, have unproven results, or have acquisition
costs you cannot bear. Start with a free or discount promotion for traction, then upgrade
customers into premium.

Layer one's premium-pricing material: `pricing-and-tiers.md` § Premium pricing: profit, not
customers.

---

## Discount promotion: structure and four ways to show it

**Type:** FRM · **Prov:** [M*] · **Scale:** local services, two-step sales, regulated markets · **Signals:** S-80.12, S-80.15 · **Files:** q78, q80

**Structure.** A deep discount (50% or more) on one component or "sliver" of the offer, not a
permanent cut to the core business. Marginal discounts (5% to 25%) rarely change buyer behaviour
and only eat margin.

**Four ways to show a discount:**
1. Percentage off: "87% off first visit".
2. Absolute amount off: "$181 off first visit, normally $210".
3. Relative equivalent: "Save the cost of a steak dinner", "Less than going out to lunch".
4. The discounted price alone: "$29 New Client Special".

The plain discounted price works best for well-understood services where buyers know the usual
price. The $210 to $29 example is the "Ultimate Lemonade Bundle" ($210 one-week bundle cut to
$29). $210 − $181 = $29, called 87% off (86.2% exactly).

**When discounts fit:**
- Heavily regulated industries or countries where ads cannot carry free offers with conditions.
- Well-understood markets with known price baselines: dentists, chiropractors, gyms, haircuts.
- Two-step sales processes where no-shows are the problem.
- Retail clothing stores run seasonal 50%+ clearances.

---

## Two-step sale: the $19 diagnostic

**Type:** MEC · **Prov:** [D] for the $19 and $2,100; rest [M*] · **Scale:** health clinic, local services · **Signals:** S-80.14, S-105.2 · **Files:** q78, q80, q82, q83, q105, Lost Chapters ch. 6

**Matched to Lost Chapters ch. 6** `[D]`: "heavy metals test consultations for $19 and then
upselling… a $2,100 10 week detox plan." Flow: ad, opt-in, phone call for $19, appointment,
follow-up for $2,100.

**How it works.** Charge a small front-end fee ($19) for a first consultation or test, get the card
on file, then upsell the core service. People attend 85% to 90%+ of appointments they paid for, so
the fee removes no-shows, starts trust, and makes the backend upsell frictionless.

- Upsell rate: 90%+ of attendees (q80 only).
- Chiropractors, dentists and gyms use $19 or $29 introductory consultations or cleanings.
- q82 attaches the "$2,100 10-week" plan to physical therapy, not the detox; likely the same
  figure moved to another example.

q105 frames it: when he charges for an assessment, it is a discounted two-step offer, not a profit
centre. Structure: (1) advertise a narrow diagnostic or test at a low price; (2) do the test and
set up the follow-up proposal; (3) pitch the full-price core offer during or right after it. The
$19 is about 0.9% of the $2,100 core (Pass 1's arithmetic, not his rule).

---

## Free presentations: why they work

**Type:** MEC · **Prov:** [M*] · **Scale:** high-ticket, complex offers · **Signals:** S-81.1, S-81.2, S-81.5 · **Files:** q78, q81, q82

Free presentations educate prospects to close the information gap before a sale, for complex or
high-ticket offers that need education and trust. They hold a captive audience, take a time
investment from attendees, and give a big offer the runway it needs.

- "The bigger the plane, the longer the runway": a toy plane needs 20 feet, a 747 Dreamlifter 2
  miles.
- "The more time they spend with you, the more they'll spend with you."
- Length: 15 minutes to 3 days.
- A presentation breaks three core limiting beliefs before the pitch, as q78 and q81 give them:
  (1) results must come easy, (2) results must be the best possible, (3) results must lead to
  attention and approval. They read oddly; possibly garbled in transcription or summary.

WRN (q81): selling high-ticket offers to cold traffic is one of the hardest things in business; it
needs a long content game or maximum exposure inside a short presentation window. He cut this
chapter from Money Models because it gets too close to sales-script coaching rather than offer
structure.

---

## Free presentations: formats and close rates

**Type:** NUM · **Prov:** [M*] · **Scale:** local seminars, online coaching · **Signals:** S-81.3, S-81.4 · **Files:** q78, q81, q82, q83

| Format | Shape | Close rate |
|---|---|---|
| Free dinner presentation | 60 to 90 minutes over a meal | 25% of the room buy a lower-ticket offer; 33% of those buy the high-ticket offer (100 attendees, 25 low, 8 high; 33% of 25 is 8.25) |
| Free 90-minute masterclass | Remote | 10% of live attendees buy on the call |
| Free 5-day challenge | 4 days of 60 to 90 minute live training, pitch on day 5 (Friday) | 2% to 5% of total signups |
| Free 3-day virtual summit | Multi-speaker, pitch on days 2 and 3 | 10% of attendees on the final day |
| Free strategy call | 15 to 60 minutes, two-step triage on BANT (budget, authority, need, timing) | 25% of those who take the second call |

Examples (third-party): free neuropathy dinner and free diabetic dinner (medical clinics); a $2,000
software pitch after a 60-minute webinar. 5-day challenges: "Find Your Niche Entrepreneurship
Challenge", "Find Your First Real Estate Deal", "Buy a Business with $0 Down", "Make Your First
High Ticket Sale", "Plateau Buster Weight Loss Challenge", "5 Days to Freedom Addiction
Challenge", "Pain Release Challenge"; q82 adds "Free 5-Day High-Ticket Sales Challenge" and "Free
5-Day Get Unstuck Challenge".

---

## Freemium: criteria and the warning

**Type:** FRM · **Prov:** [M*] · **Scale:** venture-funded software, media · **Signals:** S-81.6, S-81.7, S-100.6 · **Files:** q78, q81, Q100

**Structure.** Give the core software or digital product away free to build user volume with $0 ad
spend, then upsell users into paid tiers by sales or automation.

Three criteria:
1. Near-zero incremental cost per extra user.
2. Continuous value, not a one-time download.
3. A built-in hole or cap (storage, feature locks, branding overlays, seats, ads) that pushes
   power users to upgrade.

Free-to-paid conversion is typically low, 1% to 5% (q78 only). Needs close to 100% incremental
gross margin. "This isn't a business model. It's an acquisition strategy." Examples: Dropbox,
Gmail, Facebook, YouTube, Spotify, Slack, Canva. q81 also files Uber (free first ride), Netflix
(30-day trial) and European Wax Center (free first wax) under freemium; q78 files them under free
promotions. They are free trials.

**Warning.** "If you do not have investors or large amounts of capital, I would not recommend this
structure." Three roadblocks:
1. Conversion: too few free users pay.
2. Value or virality: not viral enough, so you pay for ads to get free users.
3. Cost: serving free users costs more than paid users bring. "Now you're just running a business
   that loses money servicing customers for free. No bueno."

Q100 example: a free tier where each free user costs a hard $0.05/month to serve, with low
conversion to paid, drains cash fast in a bootstrapped business. Know your unit economics.

---

## Free Pick Your Price: structure and pitch

**Type:** FRM · **Prov:** [M*] · **Scale:** local services, coaching · **Signals:** S-81.8, S-81.10 · **Files:** q78, q81

1. Market the offer as free.
2. At checkout or in the pitch, let the customer pick their price on a sliding scale with no
   ceiling, with bonuses at set rungs to encourage paying above zero.
3. Frame payment as supporting coaches, employees or families rather than the company, and higher
   prices as investing in their own commitment and results.
4. Pitch sequence: ask commitment questions first ("Are you willing to change X?", "Will you keep
   showing up if life gets busy?"); lay out what each rung gets; ask "Which would you prefer?";
   then stay quiet while they pull out their card.

Result: very high conversion, lower average ticket. It works in low-trust settings by giving the
buyer full control over the entry price.

**Warning (q81).** Cut from Money Models because inexperienced owners can lose money if they cannot
close the backend upsells. The $0 option must carry minimal operating cost so non-payers do not
burn out staff; reserve high-labour fulfilment for higher-paying rungs.

q81 calls it a "3-tier incentive scale", but its own example has four price points ($0, $99,
$199, $499). It is a sliding scale inside one free offer.

---

## Free Pick Your Price: every rung

**Type:** NUM · **Prov:** [D] for weight loss and car wash; rest [M*] · **Scale:** local services, coaching · **Signals:** S-81.9, S-106.5 · **Files:** q78, q81, q82, q106, Lost Chapters ch. 19

**Matched to Lost Chapters ch. 19** `[D]`: "Free 21-day weight loss. Upsell. Pick your price. Most
people pay $99… If you pick $99, we'll give you an extra one-on-one call. If you pay over $199,
we'll also provide our entire supplement handbook. If you pay $499, we'll guarantee that you lose
10 pounds." Car wash: free, then over $30 hand wax, $67 buff, $99 interior.

| Business | $0 rung | Rungs above |
|---|---|---|
| Weight loss, free 21-day program | Basic group access | $99 (most popular): 1-on-1 call. $199: supplement handbook. $499: 10-lb results guarantee (q106 adds "or full service credit") |
| Car wash | Machine wash with water and soap | $30+: hand wax. $67+: hand buff. $99+: full interior detailing |
| Lemonade | Free cup | $5+: hand-squeezed. $25+: a pitcher plus photo. $99+: three months of shipments |
| Dentist | Free cleaning | $99 or $299 tiers with extra treatments |
| Coaching | Free group access | $299: video course. $997: 6 group calls |
| Art gallery | n/a | Paintings on a $149 to $299 range; most buyers pay past the midpoint so they do not look cheap or unsupportive |

q106 alone calls the weight-loss and car-wash rungs good, better, best. Pass 2 L2.2: these rungs
are the nearest thing to tiers in the sources; see `first-customers-layer-two.md` § Layer two on
tiers.

---

## Lifetime discount and founding member offers

**Type:** FRM · **Prov:** [D] for the $400 example; rest [M*] · **Scale:** local recurring service, grand openings, SaaS beta · **Signals:** S-78.15, S-104.5, S-92.10, S-92.11, S-92.12, S-100.7 · **Files:** q78, q82, q92, q93, q104, Q100, Lost Chapters ch. 22

**Matched to Lost Chapters ch. 22** `[D]`: a $400 a month local service at 50% off for life, $200 a
month; reason "new location"; urgency "until we open"; "make sure you make a profit after the
discount."

**Structure.** A discounted recurring rate locked in for as long as payments continue
uninterrupted. Cancel and the discount is gone forever; returning means full retail. Frame it as
"Price Protection". Use it as a "Founding Member" attraction offer for a grand opening or new
location, or as a rollover upsell.

**Earned version (q92 to q94).** Find the month the average customer drops off (example: month 4)
and let clients earn a lifetime lower rate if they stay past it.

**Prices (q92, q93):**
- Local service: retail $400/month, Founding Member $200/month for life (50% off).
- Digital product or software: retail $39/month, $19/month for life ($20 off), for early access or
  beta testers giving feedback.
- Supplement flavour tester: retail $19.99/month, $14.99/month for life.
- Initiation-fee buy-down ("John the Tanning King"): pay a $100 initiation fee to lower monthly
  dues from $18 to $10 for life; or the $100 initiation fee waived for a 1-year commitment.

**"The Opener" (q78, q82, q92, q93).** A 14-day trial converting into a 50% lifetime discount ($200
a month, down from $400) before grand opening. 500 trials, 400 billed on day 15: an 80% stick rate
after the trial. Every new location opened with 400+ recurring members on day 1. Profitable in
month 1. q92 calls it a gym franchise, q93 a gym or tanning franchise mentor; whether The Opener
is a person or a business is unclear. A result claim with no named business.

**Warning (Q100).** A fixed lifetime rate with no cap (for example $14.99/month for life), no term
limit and no room to adjust for inflation or fulfilment cost. If fulfilment or marketing costs
rise above the locked rate, the business serves those customers at a permanent loss.

This 50% is a lifetime rate, not a first-period discount. See `first-customers-layer-two.md` §
Layer two on half-price starts.

---

## Free with alternative revenue stream

**Type:** FRM · **Prov:** [M*] · **Scale:** clinics, local services · **Signals:** S-78.16, S-87.1, S-87.4 · **Files:** q78, q82, q85, q87

**Structure.** Give the main service free (or $5/month) and earn from a required high-margin item:
supplements, physical products, software, setup fees. Requirements (q87): the business has more
than one revenue stream; the free item has low incremental fulfilment cost; the paid item carries
enough gross margin to cover fulfilment of both. Two variations: paired (Thing A free in exchange
for buying Thing B) and independent (Thing A free, Thing B recommended for the best result).

**Examples:**
- Weight loss: $5/month service for 1 year if the client buys $300/month of supplements (q78) or
  $400/month of supplements, bars and shakes (q82). "Grew 200+ clinics", a result claim about an
  unnamed business.
- Storage units: free storage, required proprietary lock.
- Physical therapy: free treatments, required orthotics or tape.

**Unit math.** 80% take rate on the $300 backend at 80% margin: $300 x 80% x 80% = $192 gross profit
per free offer given. q78's $300 fits its own arithmetic; q82's $400 does not. q85 calls the $192
"net profit"; it is gross, since it ignores the cost of the free item.

Layer one's "free forever" model (clinic supplements making 95% of revenue) is in
`free-work-trials-and-first-customers.md` § Seven free-offer models.

---

## Discount plus setup fee: both worked cases

**Type:** NUM · **Prov:** [D] · **Scale:** recurring service; 12-week program; tanning salon · **Signals:** S-104.2, S-92.14, S-80.13, Pass 2 L2.1, L2.4 row 18 · **Files:** q80, q92, q93, q104, Lost Chapters ch. 23

**Matched to Lost Chapters ch. 23** `[D]`:

> "Any recurring service offer: 95% off the first month, $1,900 off the first month, first month
> for $100… they still get charged a $1,900 setup fee. All in all they get charged $2,000 and go
> straight into recurring."

> "Any defined end service or program offer: 88% off first month, selling a 12-week program for
> $3,000… you get 88% off your first month, which would be 120 bucks… then we have a $1,000 setup
> fee, they end up paying $1,120 for the first month and then can then pay their next few payments
> at $1,000 each."

**Case 1, recurring service.**
- List first month: $2,000. 95% off = $1,900 off. First month: $100.
- Setup fee: $1,900.
- Paid up front: $100 + $1,900 = $2,000.
- After that: the audio says only "straight into recurring"; the recurring price is not stated.
  q104 gives $1,000/month; q92 gives $2,000/month. Pass 2 L2.4 row 18: the $1,000 is NotebookLM's.

**Case 2, 12-week program at $3,000.**
- Monthly payment: $1,000. 88% off the first month = $880 off. First month: $120.
- Setup fee: $1,000.
- Month 1: $120 + $1,000 = $1,120. Months 2 and 3: $1,000 each.
- Total collected: $1,120 + $2,000 = $3,120, slightly above the stated $3,000 (Pass 1 arithmetic).

**Why it works.** Advertise a large discount on the first month or term to lower lead friction, and
charge one or more upfront setup, enrolment or startup fees to liquidate ad and sales-commission
costs up front (q92). The sunk cost cuts churn.

**Setup fee and churn** `[D]`, Lost Chapters ch. 23: "The higher the one-time start fee, the lower
the churn." His tanning-salon mentor: a $100 sign-up fee on a $10 month membership produced next
to no churn; members who paid $19 down on a $19 month churned more.

Businesses named (q92): personal training gyms, online weight-loss coaching, tanning salons,
service agencies.

---

## $1 trial: charge a dollar, not zero

**Type:** NUM · **Prov:** [D] · **Scale:** subscription · **Signals:** S-104.3, S-82.3 · **Files:** q82, q104, Money Models p6

**Matched to Money Models part 6** `[D]`: charge **$1 for the first month** instead of a free one, so
a card is on file; "people get weird when you offer free stuff and ask for a card."

It sits under trial with penalty, one of the three downsell families. The working credit card is
on file before automatic billing starts in month two.

**Trial with penalty as a first offer (q82).** Provide the service for $0 up front, but the client
must follow set accountability actions (attend all sessions, log metrics). If they fail, they pay
a pre-agreed penalty fee. Layer one's $50 penalty version: `free-work-trials-and-first-customers.md`
§ Free trials: the warning against unconditioned trials.
