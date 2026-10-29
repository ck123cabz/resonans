---
type: corpus
aliases: ["Continuity"]
corpus: alex-hormozi
layer: retrieval
tags: [agencies, billing, churn, continuity, corpus, machine, offers]
source: skills/corpus-ingestion
created: 2026-10-16
file: continuity
sources: q86, q88, q89, q92 to q96, q100, q102 to q104, q107 (layer two, $100M Money Models and $100M Lost Chapters)
---

# Continuity

Layer 2 retrieval index for the Alex Hormozi corpus, layer two: the six continuity offer types, pricing and churn, billing cadence, moving a customer into continuity, and the service and agency answers. One framework, rule, script or number set per `##` heading. Each section stands alone, so context repeats rather than cross-references. Upsells, the value grid and downsells are in `upsell-and-downsell.md`.

**Provenance key.** `[D]` the words were matched to his own audio (Pass 2 L2.1). `[M*]` NotebookLM transcribed the audio and chose the words; not yet matched. `[A]` a gap: the sources do not hold it. Pass 2 corrections (L2.1 to L2.6) override Pass 1 wherever they disagree.

**Standing caution.** Layer-two answers ran in fresh NotebookLM conversations, so none opens with a previous answer. The same example often appears in several answer files; that is one retelling, not independent confirmation. Pass 2 has not passed Christian's review gate.

**Layer-one files that overlap.** The SMB dead zone and the worst-month rule: `closing-vetting-and-operating.md`. Gym Launch prices: `hormozi-record.md`. First payments, half-price starts and activation points: `free-work-trials-and-first-customers.md`. Agency offers: `pricing-and-tiers.md`.

---

## Continuity offers: the six types

**Type:** FRM · **Prov:** [D] for the three Money Models families; [M*] for chapter names · **Scale:** general · **Signals:** S-92.1, S-102.3 · **Files:** q92, q93, q102, Money Models p7

Each uses bonuses, discounts or fees to get customers to start and stay on recurring payments.
- $100M Money Models part 7: **Continuity Bonus Offer, Continuity Discount Offer, Waived Fee Offer.**
- $100M Lost Chapters: **Lifetime Upgrades** (ch. 21, "Get Them To Stick"), **Lifetime Discounts** (ch. 22), **Discount + One-Time Fee** (ch. 23). Pass 2 L2.1 matched ch. 22 and ch. 23 content to the audio.

q92 found these six without the question naming them; q93's question named them. The list holds on independent recovery. q102 defines continuity offers as ongoing value in exchange for recurring payments until the customer cancels.

---

## Continuity bonus offer: advertise the bonus, not the membership

**Type:** FRM, NUM, SCR · **Prov:** [M*] · **Scale:** subscriptions and memberships; a microgym · **Signals:** S-92.2, S-92.3, S-96.6 · **Files:** q92, q93, q96

- A high-value bonus (free product, service, onboarding package, premium feature, accelerator, digital vault, physical goods) free or steeply discounted if the customer signs up for recurring continuity today.
- Anchor the bonus at a higher value than the first continuity payment. "Join my membership" is a weak pitch; advertise the bonus they get by joining.
- **Pet food:** $800 of dog toys free with $59/month food shipments, plus a new toy each month.
- **Service:** a $1,000 short-term accelerator free with a $100/month membership.
- **Digital:** all 40 past newsletters ($15,880 value) free with a $399/month membership. $15,880 / 40 = $397 per issue, about one month each.
- **Script:** "Become a VIP member today and you'll get [the $1,000 program/bonus] as a free gift for joining. Or you can just buy it standalone for [large price]. Which would you prefer?"
- **Microgym case:** the owner moved from selling a standalone 6-week challenge to giving it free to those who joined member-only continuity at $100/month with exclusive perks. Standalone challenge sales fell from 34 to 15; clients going straight into continuity rose from 17 to 40; 8 of the 40 (20%) prepaid a 6-month membership up front. Described as tripling total membership sales with immediate cash; 17 to 40 is 2.35x. q96: before, 50% of challenge completers converted (17 of 34); after, "40 out of 100 total leads" went straight to continuity (the 100 base is in q96 only).

---

## Continuity: standalone-to-continuity price multiples

**Type:** NUM · **Prov:** [M*] · **Scale:** general; membership examples · **Signals:** S-86.6 · **Files:** q86, q92, q93, q94, q96

Price the one-time standalone option as a multiple of the monthly continuity price to steer buyers into continuity. q94 says the multiple is against "the first month of continuity".

| Standalone multiple | Share choosing continuity | Worked figure as given |
|---|---|---|
| 1.33x (q94: "33% higher") | about 50% | $399 standalone vs $199/month |
| 2.33x | about 80% | $699 vs $199/month |
| 2.66x | about 90% | $799 vs $199/month |

**The worked examples do not fit the multiples.** Against $199: $399 is 2.0x, $699 is 3.5x, $799 is 4.0x. Against $299 they fit: 1.33x, 2.34x, 2.67x. Pass 2 L2.4 #22: the examples fit a $299 monthly price, not $199. Do not use the ratio until it is checked against the audio.

---

## Continuity discount offer: five delivery structures

**Type:** FRM, NUM · **Prov:** [M*] · **Scale:** general; phones, storage, trash removal, landscaping, SaaS, food · **Signals:** S-93.1, S-93.2, S-85.16, S-104.4 · **Files:** q92, q93, q104

Products or services free or discounted if the customer commits to a recurring schedule. The condition is a longer commitment, not a simple first-month promotion (q104).
1. **Upfront:** applied at once, pushing out the contract start. Best where enforcement or collateral is strong (cell phones, storage).
2. **At the end:** free time earned at the end of the term if every payment is on time.
3. **Spread over time:** the discount divided across every cycle. 3 months free on a 1-year commitment at $200/month = $600, spread as $50/month off, so $150/month.
4. **After the 1st or 2nd payment:** the customer pays first and last month (or an activation fee) before bonus time, to confirm a valid payment method.
5. **Gift card:** a physical card redeemable after about 3 payments, or given to a friend as a referral magnet.

The five-structure list is in q93 only. Examples: trash removal, 1 year free for signing a 5-year paid contract; landscaping, pool cleaning, SaaS; a rice company giving 15% off after 5 months.

**Cancellation fee:** equal to the exact dollar amount of the discount received (example: $600). Breaking the commitment early reverts the customer to the standard month-to-month rate.

---

## Waived fee offer: leaving costs more than staying

**Type:** FRM, NUM · **Prov:** [M*] · **Scale:** high-ticket B2B services; the example is a solo high-ticket sales rep with zero employees · **Signals:** S-92.6 · **Files:** q89, q92, q93, q94, q95

Two options:
- **A:** month-to-month with a large upfront setup fee that covers onboarding risk, cancel anytime.
- **B:** commit to a long term (example 12 months) and the setup fee is waived. Cancel early and the waived fee is owed.

Example: $1,000/month with a $5,000 setup fee. Option A: $5,000 + $1,000 first month = $6,000 down. Option B: fee waived on a 12-month commitment at $1,000/month; $5,000 owed if broken early.

Keeps early cancellations below 5%. **Setup fee size, two readings:** 1.5x to 5x the monthly rate (q92, q93); 3x to 5x (q94). The worked example is exactly 5x. Not checked against the audio.

---

## Lifetime upgrades: a "When" paired with a "What"

**Type:** FRM, MEC, PRN · **Prov:** [M*] · **Scale:** general; subscriptions, car leases · **Signals:** S-92.7, S-92.9, S-94.6 · **Files:** q92, q93, q94, q96, q102

Pair a **When** (a delay or a milestone) with a **What** (a one-time bonus, a variable bonus, or a permanent feature or status upgrade), given after the customer joins, to raise the stick rate ($100M Lost Chapters ch. 21). q102: variable or recurring bonuses on a schedule, "every 14 days or quarterly".
- Stay 4 months in a row, unlock "Advanced Member" status and access to a customer appreciation event (delayed one-time bonus).
- Refer a friend, get 1 extra module (milestone bonus).
- ButcherBox: lifetime free bacon in every box while the subscription is active, forfeited forever on cancelling.
- Car leases: free vehicle service every 3,000 miles or 6 months.

**Status labels** (VIP, Advanced, Lifer, Gold, Elite) at tenure milestones (3, 6, 12 months), with transitions celebrated publicly. Customers fear losing the status and often value keeping their level more than the perks.

**Surprise rule:** variable or recurring bonuses drop on a schedule (monthly or quarterly). Tease what is coming but keep the exact bonus a surprise, so clients always have something to look forward to.

---

## Lifetime discount: price protection and the founding member

**Type:** FRM, NUM, WRN · **Prov:** [D] for the $400 to $200 local service; rest [M*] · **Scale:** local service, software, supplements, tanning, a gym franchise · **Signals:** S-92.10, S-92.11, S-92.12, S-104.5, S-100.7 · **Files:** q92, q93, q94, q100, q104, Lost Chapters ch. 22

A discounted recurring rate locked in for as long as payments continue uninterrupted. Cancel and the discount is gone forever; returning means full retail. Frame it as "Price Protection". Use it as a "Founding Member" attraction offer or as a rollover upsell.

**Earned version:** find the month the average customer drops off (example: month 4) and let clients earn a lifetime lower rate if they stay past it.

**Matched to audio (Lost Chapters ch. 22):** a $400 a month local service at 50% off for life, $200 a month; reason "new location", urgency "until we open"; "make sure you make a profit after the discount."

Other prices `[M*]`:
- Digital product or software: retail $39/month, $19/month for life ($20 off) for early access or beta testers giving feedback.
- Supplement flavour tester: retail $19.99/month, $14.99/month for life.
- Initiation-fee buy-down ("John the Tanning King"): pay a $100 initiation fee to lower monthly dues from $18 to $10 for life; or the $100 fee waived for a 1-year commitment.
- q95's "$399/month (or $200/month lifetime locked-in discount)" blends the newsletter and the local service; the $200 belongs to the local service.

**"The Opener" (a mentor's gym franchise, not his):** a 14-day trial into a Founding Member lifetime discount before grand opening. Every new location opened with 400+ recurring members: 500 trials, 400 billed on day 15 (80% stick). Profitable in month 1. q92 says "Gym Franchise", q93 "a gym/tanning franchise mentor".

**Warning (q100):** a fixed lifetime rate (e.g. $14.99/month for life) with no term limit and no room to adjust for inflation or fulfilment cost leaves the business serving those customers at a permanent loss if costs rise above the locked rate.

This 50% is the only 50% figure in layer two, and it is for life, not a first period.

---

## Discount plus one-time fee: the setup fee collects the cash

**Type:** FRM, NUM, MEC · **Prov:** [D] for the examples and the churn rule; [M*] for the $5,000 coaching case · **Scale:** gyms, coaching, agencies, tanning · **Signals:** S-92.14, S-104.2, S-92.13, S-92.15 · **Files:** q92, q93, q95, q104, Lost Chapters ch. 23

Advertise a large discount on the first month or term to lower lead friction, and charge one or more upfront setup, enrolment or startup fees to liquidate ad and sales-commission costs up front. The sunk cost cuts churn.

His words (Lost Chapters ch. 23):
- "Any recurring service offer: 95% off the first month, $1,900 off the first month, first month for $100… they still get charged a $1,900 setup fee. All in all they get charged $2,000 and go straight into recurring."
- "Any defined end service or program offer: 88% off first month, selling a 12-week program for $3,000… you get 88% off your first month, which would be 120 bucks… then we have a $1,000 setup fee, they end up paying $1,120 for the first month and then can then pay their next few payments at $1,000 each."
- "The higher the one-time start fee, the lower the churn." His tanning-salon mentor: a $100 sign-up fee on a $10 month membership produced next to no churn; members who paid $19 down on a $19 month churned more.

**The recurring price after month 1 (Pass 2 L2.4 #18):** in the audio he does not state it for the recurring service. The "$1,000/month" (q104) and "$2,000/month" (Pass 1 from q92/q93) are the answers' figures. Read only what he says: $2,000 collected, then recurring.

The 12-week total collected is $1,120 + $2,000 = $3,120, slightly above the stated $3,000. q95 misstates it as "$3,000 12-week program billed as $120/month + $1,000 setup fee".

**"The bigger the head, the longer the tail":** larger upfront initiation or setup fees lead to longer stick rates through sunk cost; clients who commit a lot of money up front pay closer attention and quit less.

**Online weight-loss coaching `[M*]`:** $5,000 startup fee + $267/month after. Average client lifespan in fitness is about 4 months; with the $5,000 fee it rose to over 2 years (24+ months). Whose business is not stated; the self-selection of buyers willing to pay $5,000 is not discussed.

---

## First-month discount: what the sources hold

**Type:** PRN · **Prov:** [D] for the precedents; a 50% first month is [A] · **Scale:** recurring services · **Signals:** S-104.1, S-104.2, S-104.3, S-104.5 · **Files:** q104

Not in the sources: a half-price (50% off) first month or first period. Layer one found none either (S-71.11). What they hold (Pass 2 L2.2):
- 95% or 88% off the first month, paired with a setup fee that collects the cash up front (§ Discount plus one-time fee, above).
- A $1 first month with a card on file (`upsell-and-downsell.md` § Trial with penalty: structure and the $1 first month).
- A front-loaded continuity discount conditioned on a longer commitment, with no figure in q104.
- 50% off appears only as a lifetime rate ($400 to $200 a month).

Layer one: `free-work-trials-and-first-customers.md` § Half-price start and discounted first period.

---

## Bulk prepay upsell: buy 5 months, get 1 free

**Type:** NUM · **Prov:** [M*] · **Scale:** general · **Signals:** S-86.11 · **Files:** q86, q92, q96

"Buy 5 months, get 1 month free." If 1 of 8 customers (12.5%) takes it, 30-day gross profit rises 50%. q92 says "30-day profits"; q86 and q96 say gross profit. The 50% depends on margin and price assumptions the answers don't give.

---

## Churn: billing cadence, 10.7%, 5%, 2%

**Type:** NUM · **Prov:** [M*] · **Scale:** subscription data across 14,000 businesses · **Signals:** S-89.4 · **Files:** q89, q94, q103

| Billing | Monthly cancellation rate |
|---|---|
| Monthly | 10.7% |
| Quarterly | 5.0% |
| Annual | 2.0% |

A third-party dataset; its source is not named in the answers. Not the same thing as the 10.7% churn in the 158-gym survey (`hormozi-record.md` § Gym Launch client results and the 158-gym survey), which is a before figure for his clients.

---

## Billing: every 4 weeks, 13 cycles a year

**Type:** NUM · **Prov:** [M*] · **Scale:** general; a 20% net margin business · **Signals:** S-92.4 · **Files:** q92, q93, q94, q95, q103

Bill every 4 weeks (13 cycles a year) instead of monthly (12). Same price: +8.3% annual top-line revenue, +41% annual profit on a 20% net margin, with no extra fulfilment. 13/12 = 1.083; (20 + 8.3) / 20 = 1.415. Consistent across four files.

---

## Billing: backup payment method and the 3% fee

**Type:** NUM · **Prov:** [M*] · **Scale:** general; US payment rails · **Signals:** S-92.5 · **Files:** q92, q94, q95, q103

Waive a 3% processing fee (or give a 3% discount) in exchange for a second payment method on file, specifically ACH (bank transfer). Card expirations and declines are a primary driver of churn; the backup removes that risk. q103 adds that charging or waiving the 3% fee adds about 3% pure profit to net income. ACH is a US payment rail.

---

## Churn: price a recurring offer to the client's worst month

**Type:** PRN · **Prov:** [M*] · **Scale:** B2B service sold to business owners · **Signals:** S-94.1 · **Files:** q94

Price a recurring offer to the customer's worst month, not their average or best. Even if the program adds $120,000 net profit a year on average, a client cancels in a bad month if the $4,000/month price exceeds what they take home that month. Pricing lower (example $700 to $1,000/month) keeps them paying through the bad months, cuts churn and raises LTV.

Question-shaped (Pass 2 L2.3): q94's question named a "worst month" rule. The $120,000 / $4,000 figure set appears in this one answer and was not found in the audio. Layer one's version is the only other source: `closing-vetting-and-operating.md` § Raising prices: tripling on existing members and pricing to the worst month ($3,500/month, competitors at $800 to $1,200/month keeping clients 36 to 40 months).

---

## Churn: feature bloat and the first 48 hours

**Type:** WRN, PRN · **Prov:** [M*] · **Scale:** services and memberships · **Signals:** S-94.4, S-94.5 · **Files:** q94, q95

- **Feature bloat backfires.** Adding features, calls or modules (example: weekly group coaching calls) makes customers who use only a fraction feel they are wasting money ("Look at all the stuff I'm not using"; "I'm only using 20% of what I pay for") and cancel. Strip the bloat; deliver 100% of the single core thing they want.
- **First 24 to 48 hours** after purchase: make as many small promises as possible and keep them at once, to confirm the buying decision. q103 words it as a 48-hour onboarding window.

---

## Cancellation: the save sequence and the exit interview

**Type:** FRM, PRN · **Prov:** [M*] · **Scale:** recurring services · **Signals:** S-94.7, S-94.8 · **Files:** q94, q95

When a customer wants to cancel:
1. **Make cancelling obvious and internal;** never hide it. If they can't complain to you, they complain in public reviews.
2. **Exit interview:** waive any cancellation fee if they agree to an exit interview (q95: a 1-on-1). Listen and get more upset about their problem than they are; if it is fixable, fix it on the spot or upgrade them. Done routinely, this saves 1/3 to 1/2 (33% to 50%) of cancelling clients.
3. **Remind them of what they lose:** perks, price protection, locked rates, status.
4. **Rollover for a do-over:** credit past payments toward a higher-tier or restructured service before refunding.
5. **Feature downsell:** a cheaper package with optional features or support tiers removed, not a discount on the core.
6. **"Blood money" rule:** if they still want to leave after a save attempt, process the cancellation or refund cleanly. If a customer doesn't want you to have their money, you should want it even less.

---

## Moving a customer into continuity: when

**Type:** FRM · **Prov:** [M*] · **Scale:** gym challenge or short program · **Signals:** S-96.1, S-86.1, S-88.8 · **Files:** q88, q96

- At the point of greatest need, not after a milestone when the client feels "stuffed".
- Around **week 3 or 4 of a 6-week program**, or at progress check-ins and feedback meetings; never the last day (q96).
- At a "client feedback meeting" **2 to 3 weeks after the start** (q88). The two windows roughly agree.
- Or right at signup or checkout, with a continuity or bulk-prepay option, using peak enthusiasm.

Layer one's activation points: `free-work-trials-and-first-customers.md` § Free or cheap to recurring: activation points and the continuity pitch.

---

## Moving a customer into continuity: the scripts

**Type:** SCR · **Prov:** [M*] · **Scale:** gym challenge; local health service; trials · **Signals:** S-96.2, S-96.3, S-96.4, S-96.5, S-107.6 · **Files:** q96, q107

- **"Make everyone a winner"** (active or successful clients): "To show you how much I want you to hit your long-term goal, I'll credit this program towards the next one, whether you hit the short-term goal or not. How's that sound?"
- **"Loser wins"** (clients who missed the short-term goal): "Don't worry about it. You started. That's the biggest victory of all. And even though you didn't hit your short-term goal, you met ours, which was finishing what you started. To show you that we're in this for the long haul, we'll credit your entire deposit towards staying with us long-term. That way you get your money back and you can still hit your goal. How does that sound?"
- **Rollover credit:** "As a way of saying thank you, I want to give you $500 of your money back as credit towards staying [pain-free / in the program] for good." $500 here against the $600 challenge deposit elsewhere; likely a different example (physical therapy or chiropractic).
- **Setting expectations at the start (q96):** "I don't want you to just try it. I want you to get results... You're not going to hit your long-term goals during this 6-week trial, but you will establish the habits. If you want to get your long-term results, you're going to have to stay on after." (cut with an ellipsis)
- **Before a free trial starts (q107):** ask "If this program got you the result, will you stay long-term?" If they ask why or hesitate: "I don't want you to just try it; I want you to get results. You're not going to hit your long-term goals during this trial alone, but you will establish the habits. We're going to help you do that for free, but if you want to get your long-term results, you're going to have to stay on after. I just want to make sure you're not looking for a quick fix."

---

## Moving a customer into continuity: the numbers

**Type:** NUM · **Prov:** [M*] · **Scale:** gym challenge · **Signals:** S-96.7, S-92.3, S-85.16 · **Files:** q85, q93, q96

- Rollover credit strategy: 2/3 (about 66%) of front-end challenge signups accept rolling their deposit into a 1-year recurring membership (q96 only).
- Unstructured baseline: 50% of challenge completers converted to membership (17 of 34) before the continuity-bonus change.
- The $600 challenge deposit rolled as $50/month off a $200/month 12-month membership: $1,800/year members.

---

## Gym Launch continuity: from $16,000 once to $42,000 a year

**Type:** CLM · **Prov:** [M*] · **Scale:** Gym Launch, B2B licensing · **Signals:** S-92.8, S-89.6 · **Files:** q89, q92, q93, q95

He first sold a $16,000 one-time licensing deal and could monetise each client only once. He added a back-end continuity offer at $42,000/year for 3 years ($3,200/month; q95: or $800/week), releasing a new money-making play every 14 days. Recurring revenue went from $300,000/month to $4,000,000/month, "more than 13x" ($4M / $300K = 13.3x). q92 calls the figure revenue; q93 recurring revenue.

The billing figures do not reconcile: $3,200 x 12 = $38,400; $42,000 / 12 = $3,500; $800 x 52 = $41,600 (Pass 2 L2.4 #19: his rounding or the model's). Layer one's $42,000 and $3,500/month are matched to Offers part 2: `hormozi-record.md` § Gym Launch pricing: $16,000 front end and the $42,000 back end. No outside record of the revenue figures.

---

## Service business continuity: the dead zone and the two paths

**Type:** NUM · **Prov:** [M*] · **Scale:** SMB services and agencies, US figures · **Signals:** S-94.2 · **Files:** q94, q95

- **Dead zone:** $1,500 to $3,000/month (q95 adds "$450/week", about $1,950/month). Average customer stick only 4 to 6 months; SMB volatility becomes the agency's volatility.
- **Path (a), low ticket:** automated or low-fulfilment services (local SEO, map ranking, review management, websites-as-a-service). Price: "$400/month or less" (q94); "under $400–$500/month (e.g., $299–$400/mo)" and "$299–$450/month" (q95). Stick: "30 to 40 months" (q94); "29–40 months" and "29 to 38-month" (q95).
- **Path (b), high ticket:** upmarket, $25,000+/year, to mature clients with proven sales metrics and existing infrastructure, using proven high-touch systems.

Question-shaped (Pass 2 L2.3): q95's question used the word "retainer" and its answer calls the dead zone "traditional mid-priced agency retainers"; q94, asked without the word, calls it SMB pricing. Layer one's version (down-market $300 to $400, up-market $10,000+): `closing-vetting-and-operating.md` § Service business: the SMB dead zone. Pass 2 did not find the dead zone in the transcribed layer-one audio.

---

## Service business continuity: delivery rules

**Type:** WRN, PRN, NUM · **Prov:** [M*] · **Scale:** agencies and high-ticket services · **Signals:** S-95.1, S-95.2, S-95.3, S-95.4 · **Files:** q95

- Never give clients unlimited daily access to founders or team members through Slack or messaging. It caps capacity, interrupts constantly and makes scaling impossible.
- Change the delivery cadence (example: quarterly strategy calls, 2 live getaways a year), not the execution ratios; cadence is far easier to adjust. "Execution ratios" is not explained.
- For high-ticket continuity, re-pitch and close annual renewals live, at in-person events or retreats, where emotional connection and perceived value are highest.
- **"Couplepreneurs Accelerator":** $25,000 to $30,000/year (or $2,500 to $3,000/month with $9,000 down via layaway). Includes a 1-on-1 deep-dive onboarding, quarterly strategy sessions and 2 in-person getaways a year. Whose business is not stated.
- Also in the agency answers: waived setup fees, 4-week billing, backup payments and exit interviews (sections above).

---

## Agencies and retainers: what the sources do not hold

**Type:** PRN · **Prov:** [A] · **Scale:** agencies · **Signals:** S-94.3 · **Files:** q94, q95

Not covered in layer two (Pass 2 L2.2, L2.6):
1. Any rule or example for a service priced between the low-ticket ceiling ($400 to $500/month) and the dead-zone floor ($1,500/month).
2. A monthly management retainer (ads, content or account management) with a price and scope.
3. A two-person agency, or any market outside the US.

q95 was told to say plainly if the sources give nothing; it gave rules instead. The agency material is limited to the automated low-ticket path, the $25,000+ upmarket path, waived setup fees, 4-week billing, backup payments, exit interviews and delivery rules. Layer two's agency examples are performance and pay-on-show offers. Layer one's agency offers: `pricing-and-tiers.md` § Agency offer: the standard retainer is a commodity.
