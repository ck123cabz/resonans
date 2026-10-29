---
type: corpus
aliases: ["Page flow and booking"]
corpus: ryan-mathews
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-10-08
generated: 2026-10-07
source_data: analysis/pass-1/lanes-1-2-funnel-vsl.md, lanes-3-4-format-page.md, lanes-5-7-offer-metrics-ai.md
---

# Page flow and booking

The page around a high-ticket VSL and everything after the click: what sits above and below the video, the opt-in question, the survey, the calendar, the thank-you page, and what happens to people who qualify but never book. Ordered the way a visitor moves through the funnel.

Dates are YouTube upload dates. File paths are relative to `knowledge/corpus/ryan-mathews/.raw/`.

## The high-ticket VSL funnel, end to end

- **Type:** [FUNNEL] / [PAGE]
- **Provenance:** [D]
- **Date:** 2025-11-19; 2025-10-07
- **Source:** `video/the-ultimate-funnel-for-selling-high-ticket-offers.md`; `video/the-only-funnel-training-you-ll-ever-need-1m-funnel.md`
- Video page with the survey on the same page → qualified to the calendar, disqualified to a "not a great fit" page (some clients send them to a free Skool group) → thank-you page.
- It replaces the opt-in → video → calendar-with-questions flow "guys like Sam Evans used to teach 5 six years ago". He uses it for his own agency, Funnel Architecture.
- When to use it: offers above $2,000, "even from problemaware and up" (as captioned). Below $2,000 he uses a sales page and order form instead (see `offer-and-pricing.md`).

## Opt-in before the VSL: his current stance

- **Type:** [PAGE]
- **Provenance:** [D]
- **Date:** 2026-03-05; 2025-10-07
- **Source:** `video/the-only-vsl-funnel-training-you-ll-ever-need-1-3m-vsl.md`; `video/the-only-funnel-training-you-ll-ever-need-1m-funnel.md`
- "you could still probably do quite well but you are murdering your conversions in almost all cases unless you're absolutely amazing with email marketing or SMS marketing".
- "most of the time I don't like doing this unless you're really good at email marketing and you're really going to use those emails".

## Opt-in before the VSL: his older test, and the split by platform

- **Type:** [PAGE] / [METRIC]
- **Provenance:** [D]; Miner's and Morgan's splits [X:Miner], [X:Morgan]
- **Date:** 2025-01-02; 2024-09-12
- **Source:** `video/how-jeremy-miner-built-a-24m-sales-funnel-genius-marketing.md`; `video/repaired-transcript-how-charlie-morgan-made-a-803-000-m-skool-communit.md`
- "a few years ago we did test it and it seemed pretty consistent and if you skip the optin page you got less calls the calls you got closed at a lower rate". Now "People might be burned out of opting into things", so skipping may win.
- Jeremy Miner: YouTube straight to the video, Facebook to an opt-in: "there's almost never something that's true in all instances".
- Charlie Morgan: organic ungated, paid gated with a different video. The corpus pattern: organic ungated, paid often gated, test per platform.

## Above the video: eyebrow, promise headline, "without" sub-headline

- **Type:** [PAGE]
- **Provenance:** [D]
- **Date:** 2025-11-19; 2026-03-05
- **Source:** `video/the-ultimate-funnel-for-selling-high-ticket-offers.md`; `video/the-only-vsl-funnel-training-you-ll-ever-need-1-3m-vsl.md`
- MSP Fuel: eyebrow "MSP owners only" → promise headline → sub-headline "without ads trade shows or any new employees", naming what they already tried → video.
- Steve: eyebrow "former Amazon principal engineer" ("we're trying to immediately back up whatever claim we're going to make") → headline with offer and risk reversal → video.
- In both builds the proof sits below the button, not above the video.
- Message match: the page headline carries the ad's promise, timeline and mechanism (Karlton Dennis rewrite, `video/repaired-transcript-how-karlton-dennis-made-a-11-5m-sales-funnel-geniu.md`).

## The video player: Vidalytics, custom embed, mobile first

- **Type:** [FORMAT] / [PAGE]
- **Provenance:** [D]; affiliate link disclosed in every video that recommends Vidalytics
- **Date:** 2025-11-19; 2026-02-03
- **Source:** `video/the-ultimate-funnel-for-selling-high-ticket-offers.md`; `video/alex-hormozi-s-advice-for-sales-funnels.md`
- "The reason we use custom HTML is typically it loads faster and slow pages per conversion".
- "make sure you set the rapid engage bar depending on how long your video is I tend to do it somewhere around 1.5x". Lift figures in `benchmarks-and-numbers.md`.
- Check mobile first; some clients get 96% of traffic on mobile.

## Directly below the video: one button that scrolls to the survey

- **Type:** [PAGE]
- **Provenance:** [D]
- **Date:** 2025-11-19; 2025-10-07
- **Source:** `video/the-ultimate-funnel-for-selling-high-ticket-offers.md`; `video/the-only-funnel-training-you-ll-ever-need-1m-funnel.md`
- The button anchors to the on-page survey; neither tiny nor full width. Lift: 10–20% in one video, 5–15% in the other.
- "Apply now" above the survey came out of the lowest-common-denominator test: "would they be confused ... is this a quiz like what is this".
- Button wording: on Steve's page a benefit-worded button "slightly lowered conversion rate i think it was probably just too wordy", so "apply now" stayed. "See if I qualify" is a strategist's idea, untested.
- One action above the fold: "two call to action buttons on the initial fold website is going to harm conversions that's because the confused mind doesn't buy" (`video/how-alex-hormozi-made-a-10m-sales-funnel-in-4-months.md`).

## Below the button: logos, proof line, testimonials

- **Type:** [PAGE]
- **Provenance:** [D]
- **Date:** 2026-03-05; 2024-05-21; 2025-01-27
- **Source:** `video/the-only-vsl-funnel-training-you-ll-ever-need-1-3m-vsl.md`; `video/how-ravi-abuvala-made-a-25m-sales-funnel-genius-strategy.md`; `video/how-dan-henry-made-a-1m-skool-community-in-3-days.md`
- Steve: a big-tech logo bar under the button, A/B tested at +10%. MSP Fuel: "trusted by 100 MSP owners" with client photos. Then the application, then testimonials led by company, title and result, then a second CTA.
- Long pages: a Trustpilot badge "below every single call to action" gave +149.2% for one client.
- Format: "screenshots are always going to convert better" than typed testimonials.
- Caution: tripling to quintupling proof cut one client's organic conversion in half (see `experiments-and-failures.md`).

## The survey: supply and demand decide survey-first or calendar-first

- **Type:** [PAGE]
- **Provenance:** [D]
- **Date:** 2025-10-07
- **Source:** `video/the-only-funnel-training-you-ll-ever-need-1m-funnel.md`
- "if you have more demand than you have supply we want to add friction to increase quality". Conditional logic qualifies or disqualifies.
- Questions inside the booking form get more bookings, "but it becomes kind of an operational problem at scale" because the calendar fills with bad calls.

## The survey: how to build it

- **Type:** [PAGE]
- **Provenance:** [D]
- **Date:** 2025-11-19; 2026-06-05
- **Source:** `video/the-ultimate-funnel-for-selling-high-ticket-offers.md`; `video/i-ran-200-sales-funnel-experiments-here-s-what-converts.md`
- A custom progress bar (sunk cost), click options instead of typing, easy yes/no first, "add the most invasive questions last", each with a reason ("so that we can send you your action plan", "100% confidential").
- On the page, not in a pop-up: a pop-up lost answers when people scrolled away to re-read; embedding gave +31%.
- Steve's disqualifiers: not technical, junior or intern, under 2 years at level, location; LinkedIn URL required.
- Suby adds a pinky-promise question ("do you pinky promise that if you qualify for a phone call you will show up at the selected time") in `video/i-fixed-sabri-suby-s-7-8b-sales-funnel.md`. Ryan says it raises show rate; no number.

## The booking page: "you're pre-qualified" and "It all started with a call"

- **Type:** [PAGE]
- **Provenance:** [D]
- **Date:** 2025-11-19; 2026-06-05
- **Source:** `video/the-ultimate-funnel-for-selling-high-ticket-offers.md`; `video/i-ran-200-sales-funnel-experiments-here-s-what-converts.md`; `video/repaired-transcript-he-built-a-4-step-10-000-000-funnel-full-breakdown.md`
- Header: "want the copy to speak again to the fact that they're pre-qualified", then the benefit. A progress bar reading get approved ✓, pick a time, for sunk cost. MSP Fuel books a 30-minute discovery call.
- Testimonial cards under the calendar headed "It all started with a call": booking rate 38% → 50% on an organic funnel.
- Calendar inside the form: Calendly at the end of a Typeform gave "above 20%" more calls ("like 32% or something like that"), a tip he credits to Jeremy Haynes.
- A calendar tool swap can hurt: iClosed took one client's booking rate from 35% to about 15%.

## Booking window: no more than 2 to 3 days out

- **Type:** [PAGE] / [METRIC]
- **Provenance:** [D]
- **Date:** 2025-05-05; 2026-03-26
- **Source:** `video/repaired-transcript-he-built-a-4-step-10-000-000-funnel-full-breakdown.md`; `video/this-landing-page-makes-him-116-000-day-copy-it.md`
- "We've seen show rate be at 50%. And you change nothing else by not letting people book no more than 3 days out, even more, ideally 2 days out, and show rate like immediately jumps up 25%."
- AJ&Smart books 4 days out: "That's guaranteed hurting their show rate", though their show rate is about 80%. Seven days out: "your show rate just plummets".
- Whether +25% is relative or points is not said.

## Thank-you page: "your call needs to be confirmed"

- **Type:** [PAGE]
- **Provenance:** [D]
- **Date:** 2025-11-19; 2025-05-05
- **Source:** `video/the-ultimate-funnel-for-selling-high-ticket-offers.md`; `video/repaired-transcript-he-built-a-4-step-10-000-000-funnel-full-breakdown.md`
- Why: "right now in 2025 one of the hardest metrics to get right especially with paid ads is show rate", partly from Google Calendar updates.
- Build: headline "your call needs to be confirmed"; a short video ("60 seconds to 2 minutes") covering "go to your email right now find the calendar invite and hit yes I know the sender", Zoom, and joining from a laptop not a phone; testimonials inside the video; big numbered steps; a picture of the invite. No add-to-calendar button, because it drops the Zoom link.
- Ravi Abuvala says shorter thank-you videos raise show rate; Ryan: "I tend to agree". The 60-second-to-2-minute length is Ryan's.
- A second selling video below it is optional: "If they just watched an hourong video, they probably don't need that."

## QFNB: qualified, not booked

- **Type:** [PAGE]
- **Provenance:** [D]
- **Date:** 2025-11-19
- **Source:** `video/the-ultimate-funnel-for-selling-high-ticket-offers.md`
- "if you go and you fill out my form but you do not book a call you'll get an email within about 30 minutes". The email: "Is everything okay i saw you made it to the ... booking page but you didn't grab a time".
- His EA answers replies and books them: "I get clients that way that would have just been completely lost". He skips the second automation (alerting setters to dial) because he is capacity-capped.

## Between booking and the call: reminders and pre-call emails

- **Type:** [PAGE] / [METRIC]
- **Provenance:** [D]; Viral Coach cadence [X:Daniel]
- **Date:** 2026-03-05; 2026-03-26
- **Source:** `video/the-only-vsl-funnel-training-you-ll-ever-need-1-3m-vsl.md`; `video/this-landing-page-makes-him-116-000-day-copy-it.md`
- "booking reminders texting people the night before the call free call videos from your sales reps all of those things are are good things to do".
- Test result: each top objection as an email, four emails 6 hours apart, over 225 booked calls: "we saw show rate go up by 0.2% so literally nothing", close rate "exactly the same". The first email opened at about 98%.
- Viral Coach's reminder ladder (24 hours email, 3 hours text, 1 hour email, 15 minutes text, morning-of text) is the only full cadence in the corpus, and it is theirs.

## The call: current situation → desired situation → offer as the bridge

- **Type:** [FUNNEL]
- **Provenance:** [D]; the same image from [X:Cole Gordon]
- **Date:** 2026-03-05; 2025-04-03
- **Source:** `video/the-only-vsl-funnel-training-you-ll-ever-need-1-3m-vsl.md`; `video/7-marketing-lessons-from-funnel-hacking-live-2025.md`
- The call walks current situation, desired situation, then the offer as the bridge between them. Cole Gordon uses the same bridge for phone pitches.

## Follow-up when the VSL is gated

- **Type:** [PAGE]
- **Provenance:** [X:Charlie Morgan]
- **Date:** 2024-09-12
- **Source:** `video/repaired-transcript-how-charlie-morgan-made-a-803-000-m-skool-communit.md`
- "I got about nine emails in 4 days from Charlie uh just pushing me back to either book a call or go and watch the vssl". Charlie's thank-you video states a no-ghosting policy: miss it and you cannot reschedule.
- Ryan's own list gets one email a week: "I don't really send out any more emails besides literally just conversion ideas" (`video/alex-hormozi-s-advice-for-sales-funnels.md`).

## Application pages: more content, fewer but better leads

- **Type:** [PAGE] / [METRIC]
- **Provenance:** [D]
- **Date:** 2025-05-05; 2026-04-02
- **Source:** `video/repaired-transcript-he-built-a-4-step-10-000-000-funnel-full-breakdown.md`; `video/repaired-transcript-the-psychology-of-premium-landing-pages.md`
- Extra sections below the fold on a call-booking page: "optin rate decreased. However, the strategy session booking rate 4xed", 5% to 20%, cost per call from "close to $1,000 down to like $250". He calls it inconclusive.
- For lead-magnet pages the opposite holds: cut everything below the fold (see `benchmarks-and-numbers.md`).
- Premium design: "Premium should equal conversion. It should build trust." Apple-style scroll animations "for most brands, I've seen it actually hurt conversions".
