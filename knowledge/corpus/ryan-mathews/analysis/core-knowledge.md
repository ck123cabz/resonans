---
type: corpus
aliases: ["Core Knowledge: Ryan Mathews"]
corpus: ryan-mathews
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-10-07
---

# Core Knowledge: Ryan Mathews

**Layer 1, always in context.** Written 7 Oct 2026 for the `ryan-mathews` lens, headless run, no review gate. It answers funnel and VSL questions the way Ryan Mathews teaches them: which funnel a price calls for, what the video says in what order, how long it runs, what sits above and below it, and what happens after the form. Case numbers, benchmarks, his AI workflows and his vocabulary are in the retrieval index (`analysis/retrieval-index/`).

---

## 0. How to read this file

**What the corpus is.** Ryan Mathews runs the funnel agency Funnel Architecture and the YouTube channel Ryan Mathews (about 20,000 followers on 7 Oct 2026). The corpus holds 73 of the channel's 76 long-form videos, uploaded 28 Nov 2022 to 11 Sep 2026, as auto-caption transcripts (about 215,000 words), plus 44 NotebookLM answers (63,164 words). Pass 1 checked every answer against the transcripts; Pass 2 reconciled the four lane files. Three videos have no transcript: Brunson Linchpin, Dan Koe $4.3M, Whop vs Skool.

**Provenance markers.**

| Marker | Meaning |
|---|---|
| `[D]` | His words, found in a transcript under `.raw/video/`. Captions carry no punctuation and spell VSL "VSSL"; quotes keep that. |
| `[X:Name]` | Someone else's method, number or line that he describes, repeats or reads off their funnel. Most teardown content is this. |
| `[M]` | NotebookLM wording with no transcript line behind it. Never upgrade it without the line. |
| `[A]` | The corpus does not address it. See `gap-register.md`. |

**Confidence ceiling.** Almost every number is one client, one test, often with his own hedge attached ("probably not repeatable", "it's inconclusive"). Keep the hedge. Every number is true for the year he said it. Captions have no speaker labels; five videos carry a second voice (Cole Gordon is 80 to 85% of `scaling-to-1m-isn-t-hard-if-you-copy-this.md`).

**Source short names.** Files under `knowledge/corpus/ryan-mathews/.raw/video/`. Upload date in brackets.

| Short | File |
|---|---|
| FT | `the-only-funnel-training-you-ll-ever-need-1m-funnel.md` (2025-10-07) |
| UF | `the-ultimate-funnel-for-selling-high-ticket-offers.md` (2025-11-19) |
| SCRIPT | `how-to-create-a-1m-video-sales-letter-vsl.md` (2025-12-02) |
| STEVE | `the-only-vsl-funnel-training-you-ll-ever-need-1-3m-vsl.md` (2026-03-05) |
| PSYCH | `the-psychology-of-a-persuasive-video-sales-letter-vsl.md` (2026-05-07) |
| 200X | `i-ran-200-sales-funnel-experiments-here-s-what-converts.md` (2026-06-05) |
| AJS | `repaired-transcript-he-built-a-4-step-10-000-000-funnel-full-breakdown.md` (2025-05-05) |
| MINER | `how-jeremy-miner-built-a-24m-sales-funnel-genius-marketing.md` (2025-01-02) |
| MORGAN | `repaired-transcript-how-charlie-morgan-made-a-803-000-m-skool-communit.md` (2024-09-12) |
| COACH | `this-landing-page-makes-him-116-000-day-copy-it.md` (2026-03-26) |
| TAKI | `this-funnel-generates-1-6m-mo-without-sales-calls.md` (2026-04-16) |
| IMAN | `how-iman-gadzhi-made-100m-online-genius-strategy.md` (2025-03-12) |
| HADV | `alex-hormozi-s-advice-for-sales-funnels.md` (2026-02-03) |
| PREMIUM | `repaired-transcript-the-psychology-of-premium-landing-pages.md` (2026-04-02) |
| 249K | `repaired-transcript-i-made-this-business-owner-249-000-mo-learned-this.md` (2025-09-10) |
| OVENS | `how-sam-oven-s-made-940-000-in-30-days-genius-strategy.md` (2023-09-12) |
| 7RULES | `7-rules-for-sales-funnels-what-the-gurus-don-t-tell-you.md` (2024-04-05) |
| 5VAR | `repaired-transcript-the-5-variables-behind-20-000-successful-sales-fun.md` (2024-05-31) |
| BECKER | `repaired-transcript-4-secrets-behind-alex-beckers-100m-youtube-ads.md` (2023-04-14) |
| YTADS | `repaired-transcript-i-spent-1-000-000-on-youtube-ads-here-s-what-i-lea.md` (2022-11-28) |
| BROWN | `how-william-brown-makes-364-000-m-at-a-91-profit-margin.md` (2024-10-04) |
| RAVI | `how-ravi-abuvala-made-a-25m-sales-funnel-genius-strategy.md` (2024-05-21) |
| SUBY | `i-fixed-sabri-suby-s-7-8b-sales-funnel.md` (2024-11-14) |
| PRICE | `repaired-transcript-how-to-price-your-online-course-proven-7-figure-st.md` (2022-12-14) |
| ALI | `the-real-way-ali-abdaal-makes-5-1m-with-youtube.md` (2024-02-06) |
| HAI | `how-i-automated-alex-hormozi-s-entire-ad-strategy-with-ai.md` (2026-03-19) |
| SCALING | `scaling-to-1m-isn-t-hard-if-you-copy-this.md` (2025-09-30) |
| CODIE | `how-codie-sanchez-built-a-12-000-000-sales-funnel-copy-it.md` (2025-05-23) |
| KARLTON | `repaired-transcript-how-karlton-dennis-made-a-11-5m-sales-funnel-geniu.md` (2025-06-12) |
| H10M | `how-alex-hormozi-made-a-10m-sales-funnel-in-4-months.md` (2024-01-08) |
| FAILING | `i-dissected-a-failing-ad-funnel-losing-250-000.md` (2026-01-07) |
| PRETZEL | `alex-hormozi-s-lead-gen-strategy-but-make-it-ai.md` (2026-04-23) |
| EASIEST | `the-easiest-way-to-double-your-sales-funnel-revenue.md` (2026-09-11) |
| MICRO | `repaired-transcript-how-to-find-optimizations-in-your-sales-funnel-mic.md` (2024-10-23) |
| GYM | `repaired-transcript-how-alex-hormozi-made-a-100m-sales-funnel-genius-s.md` (2023-10-10) |
| PINEDA | `repaired-transcript-how-ryan-pineda-built-a-21-9m-sales-funnel-genius.md` (2024-07-24) |
| DANHENRY | `how-dan-henry-made-a-1m-skool-community-in-3-days.md` (2025-01-27) |
| FHL | `7-marketing-lessons-from-funnel-hacking-live-2025.md` (2025-04-03) |

---

## 1. Funnel architecture by price band

### 1.1 The $2,000 line
`[D]` FT. "there's kind of a line in the sand these rules are always broken but really anything under $2,000 is going to fall into a different funnel than anything above $2,000".

- **Under $2,000:** sales page, then an order form (sometimes embedded on the page), an order bump, one or two one-time offers. The price is on the page; buyers go to checkout "once they see the price". Works best for traffic that is solution aware and up.
- **Over $2,000:** a VSL funnel. VSL page, then a survey or straight to a calendar, then a sales call. Usable "even from problem aware and up". He avoids fully unaware traffic in both.
- No price appears on any page of his over-$2,000 builds (STEVE, UF). That is read off what he builds, not a rule he states. Where the video speaks the price is `[A]`.

### 1.2 The three fits come before any funnel
`[D]` STEVE. Message-market fit wins attention, copy-market fit wins conversion, offer-market fit wins the sale. "if you build an audience you can get a lot of things wrong and still do quite well". He judges offer-market fit with Hormozi's value equation `[X:Hormozi]`.

### 1.3 His own high-ticket funnel
`[D]` UF, STEVE, FT. One video page with the survey on the same page. Qualified leads go to a calendar; the rest go to a "not a great fit" page (some clients send them to a free Skool group). Then a thank-you page. A qualified lead who does not book gets an email about 30 minutes later. "this funnel is also the funnel that I personally use for my business at funnel architecture" (UF). Five videos from 2025 and 2026 describe the same shape.

It replaces the older opt-in, then video, then calendar-with-questions flow that "guys like Sam Evans [Ovens] used to teach" five or six years earlier (UF).

### 1.4 Survey first or calendar first: supply and demand
`[D]` FT, STEVE. "if you have more demand than you have supply we want to add friction to increase quality". Questions inside the booking form get more bookings, but at scale "it becomes kind of an operational problem". Use the survey when demand exceeds what the sales team can take.

### 1.5 What keeps the call, and the no-call model
- `[X:Taki Moore]` TAKI (2026-04-16). Black Belt sells with no call: a long application, a $1,500 refundable deposit, $2,000 for month one, then $2,500 a month, sold out "9 months in a row" as Ryan states it. Taki's reason: "trust has moved upstream in 2026", meaning trust is built in content before the offer. "Content is the new sales call" is Taki's too.
- `[D]` Ryan's limit on it, same file: "if you have a very custom offer if it's done for you it doesn't work quite well". His own agency keeps the call because its work is custom.
- `[D]` TAKI. Start with a name-and-email waitlist until you can sell out; switch to application and deposit once demand passes supply.
- Reading for a buyer: above $2,000 and custom or done for you means the call stays.

### 1.6 Pick the funnel by awareness
`[D]` FT, BECKER. The more aware the traffic, the less video it needs. `[X:Alex Becker]` Hyros runs a very short YouTube ad straight to a booking page: "they took out the vsl and they just go straight to it because again this is a very direct vsl right this is a direct offer" (BECKER, 2023). Unaware traffic gets webinars ("really complicated 3-hour webinars") or a mini offer first.

### 1.7 A mini offer before the VSL for cold traffic
`[X:Hormozi]` PRETZEL (2026-04-23). The "salty pretzel": sell what most of the crowd wants first, so the main offer meets a thirst. Going straight to a VSL and a call is "asking for marriage before the first date". The "300 to 500% increase in lead volume" is Hormozi's expectation, not Ryan's result. Ryan's build of it is an AI audit tool.

`[D]` 249K (2025-09-10). A $1 buyer converts on the call at twice the rate: one client scrapped the low-ticket front end and sent everyone to a VSL-to-call funnel, and calls closed at 30% instead of 60%. "once someone hands you even just $1, they're much more likely to hand you more".

### 1.8 Model a funnel only from the same traffic source
`[D]` SCRIPT. "if somebody's using a VSSL for organic traffic and I'm going to run ads it might not work for me because they're running it to organic traffic there's just less they have to do to that audience". Steve's case runs the other way; see §6.3.

### 1.9 The funnel is not where the magic is
`[D]` OVENS (2023-09-12). Sam Ovens' Google Doc VSL worked because of pent-up demand, very aware buyers, marketers who "like the way they're marketed to", and a million-person list. "the magic wasn't really in the funnel". Ryan copied it after selling his old list and audience and it flopped: "it's kind of expected that it's going to flop".

---

## 2. The VSL: beat orders

Two skeletons sit in the corpus, plus a short form read off other people's funnels. They agree on the order problem, mechanism, proof, objections, call to action. They disagree on where the offer goes. No transcript gives a timing for any beat; every timestamp in NotebookLM's q07 is `[M]`.

### 2.1 First question: does the buyer know your type of solution?
`[X:Hormozi]` framework, `[D]` for his default. PSYCH (2026-05-07). No: run the 5 Ps (educate). Yes: run the 5 Ws. "now if you're unsure I would choose no". This is his shorthand for Schwartz's awareness levels `[X:Schwartz]`. For fully unaware traffic he points to the story lead from *Great Leads* and does not script it.

He credits the whole build on camera: "I want to give credit here to Alex Heroszi because he did come up with these frameworks" (PSYCH). Sections 2.2 to 2.6 are Hormozi's structure in Ryan's wording.

### 2.2 The intro: Promise, Pain, Proof, Plan
`[X:Hormozi]` structure, `[D]` wording. PSYCH.

- **Promise:** outcome plus timeframe plus "without" the thing they dread. His lawn example: "thick green head turning grass ... usually within one growing season ... without you having to ... spend your Saturdays spreading fertilizer".
- **Pain:** "the knife's kind of in now we're going to twist it".
- **Proof:** specific, visual, showing the outcome the buyer wants, never features. "the burden of proof is on us to prove that what we're saying is true".
- **Plan:** a spoken agenda of what the video covers (why the usual fix fails, the steps, the biggest concerns, how to take the next step).

He says this intro is built the same way as his YouTube intros.

### 2.3 The body: Proof, Promise, Pain, Plan, Picture
`[X:Hormozi]`, `[D]` wording. PSYCH. The Pain beat explains why the old way fails, and that explanation builds the unique mechanism ("you're feeding a patient that's actually sick underneath"). The Plan is "the bridge to get from where they are to where they want to go while also explaining the reason why everything they've tried hasn't worked". Picture gets one clause in the transcript; the scripted "Imagine pulling into your driveway" lines in NotebookLM are `[M]`.

### 2.4 Five objections, four steps each
`[X:Hormozi]`. PSYCH. "what are the five most common objections you're going to hear in the sales meeting bring those forward". For each: what they think, the problem with that, what is right, proof that answers that objection. Be "tactful and winsome". He names one objection (DIY at Home Depot); the five categories in q12 are `[M]`.

### 2.5 The call to action
`[D]` PSYCH. Say what to click and what happens next, with risk reversal in the same breath: "there's a button down below you click that there's going to be a short form takes about 60 seconds to fill out". The guarantee follows. Its job is to raise perceived likelihood and lower risk.

### 2.6 The close: testimonial reel after the CTA
`[X:Hormozi]` frame, `[D]` for the reel spec. PSYCH. Hormozi's line, given to a client of Ryan's who paid "$100,000" to sit in a room with him: "Hey this video is over but I'm going to play some testimonials here hey no pressure to stay". Hormozi's claim is "everybody stays". Ryan's spec: "multiple short snippets not ... 2 seconds but like maybe 30 seconds", better than "3 minute long versions that are kind of boring", ending on an on-screen CTA or a return to camera. On 7 May 2026 he had "just started testing" it. No result.

### 2.7 The 5 Ws variant for buyers who know the solution
`[X:Hormozi]`. PSYCH. "who you are what you do where you do it when you do it and then why us over the other guys". It replaces the 5 Ps body; "every other step of the process is actually exactly the same". This is the corpus's answer for warm or reply traffic.

### 2.8 Cialdini on top
`[X:Cialdini]`. PSYCH. Reciprocity, commitment and consistency, social proof, liking ("a little bit self-deprecating"), authority, scarcity: "the tactical level that is going to make a good VSSL turn into a great one".

### 2.9 The long form with money behind it: Steve's VSL
`[D]` STEVE (2026-03-05). Steve, A Life Engineered, an ex-Amazon principal engineer: "141 days ... $1.3 million in revenue and over 1,800 leads". The live VSL is the fourth one tested over four or five months. This is the only skeleton in the corpus with revenue behind it. Order, as Ryan walks it:

1. Credibility intro: nearly a thousand interviews, promotion panels, "Amazon's brutal L6 to L7 gauntlet".
2. Problem with a filter: "stuck at mid senior or above", so juniors drop out.
3. Agitation: companies "quietly managing out the bottom 5 to 20% every year", and AI.
4. Story and dream outcome: "my comp jumped by over 300K per year".
5. Curiosity: "mastering the unspoken rules".
6. Offer as a guarantee per avatar: a promotion or a better review in 12 months "or work with you for free until you do".
7. Proof: "hundreds of engineers across Amazon Google Meta Airbnb".
8. Reviews and testimonials.
9. Objections.
10. Call to action.

"it's not that complicated of a VSSL". No price in the video or on the page; the offer is the guarantee. His own critique: open on the credential, "just cut out that first six words ... that kind of credibility hook might work a little bit better".

### 2.10 The short form: offer first
- `[X:Charlie Morgan]` MORGAN (2024-09-12). "normally the traditional way with vsls and webinars is you you know spend 20 minutes 45 minutes building up to the offer ... whereas he within 20 seconds". Morgan's opening offer: 20 high-ticket clients in 180 days, guaranteed, or a full refund plus "$5,000 of our own pocket", then "the next 10 minutes" agenda.
- `[X:viral coach page]` COACH (2026-03-26). A VSL "only about 5 minutes long" that goes "the guarantee right offer kind of who they are who this has worked for who it doesn't work for how this works why this works and next steps". Order: guarantee and offer, who they are, who it works for, who it does not, how, why, next steps.
- `[D]` SCRIPT (2025-12-02). The Charlie Morgan VSL he modeled for MSP Fuel: "it's 5 minutes". Proven because the ad had run four or five months in the Meta Ad Library.

Read together: the 5-minute VSLs he points to state the offer and guarantee first and build afterwards. Steve's long form states the guarantee in the middle. Both are his examples; neither is stated as a rule over the other.

### 2.11 Other hook devices, all borrowed
- `[X:Alex Becker]` BECKER. The "Uber promise" in the first five seconds: "this simple line of code can increase your ad sale by 50 to 100".
- `[X:Sabri Suby]` SUBY. An on-screen timer and chapter markers on a 7-minute VSL ("I can invest seven minutes here"); a soft CTA "probably 5 to 10 minutes in".
- `[D]` AJS. Normally "you're leading with the promise"; AJ&Smart opens with a self-introduction and returns 2.5 to 3x, so "Don't change".

### 2.12 The script process, five steps
`[D]` SCRIPT (2025-12-02), with the modeling step `[X:Brunson]`.

1. Six inputs: audience, main problem, solution, price or commitment, credibility, guarantee. Probe each pain several layers down. He dictates with Whisper Flow.
2. Pick a proven VSL to model, by structure, never words. Four filters: same traffic source, same audience, same offer type ("sometimes trumps similar audience"), proven in the Meta Ad Library.
3. One prompt: the model's structure ("seven different pieces"), the offer details, a tone guide from 5 to 10 YouTube transcripts. "do not copy the wording learn from and model the structure".
4. Several drafts, combined or used as inspiration. His first draft "is just using too much of Cole's actual language".
5. Revise line by line with the client days later, with fresh eyes, then test and repeat.

He ran this in a ChatGPT custom GPT, not Claude.

### 2.13 A good offer writes the script
`[D]` STEVE. MSP Fuel's first VSL was hard because the offer was wrong: "you're trying to like spice this thing up". The second went fast. On Steve: "you're not trying to put lipstick on a pig". `[D]` HADV: without a real offer "you're really just putting lipstick on a pig".

### 2.14 Copy rules
- `[D]` 7RULES. Never blame the buyer: "hey it's not your fault it's because of this thing".
- `[D]` 7RULES. Real benefits over faux ones: "a faux benefit is the surface level".
- `[D]` `repaired-transcript-exactly-how-to-turn-your-content-into-sales.md` (2025-08-05). Specific numbers: "He's not saying 1,000%. That sounds very generic".
- `[D]` PREMIUM. About a ninth-grade reading level, checked in Hemingway. "technobabble" lost novice buyers for Joel Turner.
- `[D]` DANHENRY. "screenshots are always going to convert better" than typed testimonials. No number.
- `[D]` `repaired-transcript-how-to-boost-your-website-conversion-rate-by-2x.md` (2023-08-17). Answer a question the moment the reader raises it (the elephant, learned from his mentor Spencer Van's webinar).

---

## 3. Format

### 3.1 Length: one stated norm, and it is for cold ads
- `[D]` AJS (2025-05-05). On AJ&Smart's 66-minute Meta VSL: "Normally, this would be about 20 to 30 minutes." Said once. AJ&Smart returns 2.5 to 3x "last I heard", so "it's working right. Don't change it."
- `[D]` SCRIPT (2025-12-02). The script he modeled for MSP Fuel runs 5 minutes.
- `[X]` lengths he reads off other funnels, none tied by him to a traffic source: Morgan offer in 20 seconds and a 10-minute agenda (MORGAN); viral coach 5 minutes (COACH); Suby 7 (SUBY); Gym Launch 15 (GYM); Pineda 27 (PINEDA); AJ&Smart 66 (AJS).
- `[X:Cole Gordon]` SCALING. "a 10 to 15 minute video i mean it's still pretty short and snappy" after an indirect ad; "The long funnels are really tough uh especially in more saturated markets." A guest's line, not Ryan's.
- No transcript pairs a minute count with YouTube, email, warm or retargeting traffic. `[A]`.
- Webinars: the only length he gives is "really complicated 3-hour webinars" for unaware traffic. q04's "VSLs 5 to 20 minutes, webinars 1 to 3 hours" is `[M]`.

### 3.2 Thank-you page video: 60 seconds to 2 minutes
`[D]` AJS. "a video here that just gives them a few pieces of information, it's very short, 60 seconds to 2 minutes". `[X:Ravi Abuvala]` says a shorter thank-you video raises show rate; Ryan: "I tend to agree". The minute count is Ryan's.

### 3.3 On camera, screen-share and production
- `[D]` YTADS (2022). "having good video and audio quality is crucial regardless". His best YouTube ads were shot by Rich Krause (Ridgeline Media) and "engineered ... for retention". About ads.
- `[D]` 249K (2025). A client turned his ad copy into produced skits with props; he had expected selfie videos and "was blown away by how well these things converted on ice cold traffic". The client's organic posts run as ads had struggled to profit. About ads.
- `[X:Charlie Morgan]` MORGAN, `[X:William Brown]` BROWN. Low production for marketers selling to marketers: Morgan in front of a whiteboard with "basically no editing"; Brown's VSL is a walk through his Stripe ("I made 20 grand today"). Ryan: "there's a lot of nuance to organic content".
- `[X:Ravi Abuvala]` RAVI. A VSL "walking through a Google doc". `[X:Sam Ovens]` OVENS: a Google Doc and a Loom.
- The screen-share formats are the nearest thing in the corpus to a faceless VSL, and all are the founder narrating his own screen in his own voice. Faceless, AI voice, avatars and ElevenLabs appear in no transcript. `[A]`. "People can smell it from a mile away" is about AI-written copy, not voice.
- `[X:unnamed FHL 2025 speaker]` FHL. "minimally edit videos with just simple subtitles typically lead to a cheaper CPL". Ads.

### 3.4 Visuals and the first seconds
- `[D]` HAI (2026-03-19). "sometimes what's on the screen as the hook is more important than the words sometimes the words don't even start for 5 seconds". Said about ads and reels.
- `[X:True Classic]`, `[X:Mark Rober]`, `[X:Alex Becker]`: a slap and a beep before the 5-second skip, broken glass, speed changes and sound effects to break the viewer's trance. YouTube ads, not VSLs.
- `[X:Tony Robbins / Sales Humanity]`: an event ad cut "similar to how you would in a movie trailer".

### 3.5 Hosting and the player
- `[D]` UF. Custom HTML embed over the page builder's video block: "it loads faster and slow pages per conversion". A border matching the buttons. Check mobile first; some clients get 96% of traffic on mobile.
- `[D]` HADV, 200X. Vidalytics (affiliate link disclosed each time): rapid engage bar "somewhere around 1.5x", a click-to-unmute box that restarts the video. "averages a 10 to 25% increase", smallest lift 16%, one live test "30 or 40% better", one client +66% applications "at a 100% statistical significance" (KARLTON). It does nothing when "your VSSL sucks".
- `[X:Iman Gadzhi]` IMAN (2025-03-12). The flywheel VSL: a public YouTube video, linked first in the description of his content videos, because "if this vssl is gated behind an optin page ... the distribution is only going to be as much as you send to it". 9.5M views. At its end he links off YouTube to a second, high-production VSL on a sales page. Ryan's guess: the YouTube version converts near 0.2% where a gated funnel might do 1.5%, and volume makes up the gap.
- `[X:Hormozi]` FAILING. Removing the video from a Skool About page cost "something like a 40% drop", told second-hand; "I forget the exact number". He calls a page with no video "mistake number one".

---

## 4. The page flow

The densest and most consistent part of the corpus. Almost every row is `[D]` with a client test behind it.

### 4.1 Above the video
`[D]` UF, STEVE.
- **Eyebrow** naming the audience or credential: "MSP owners only"; "former Amazon principal engineer".
- **Headline** with the promise and, where there is one, the risk reversal. MSP Fuel: "Discover how we can guarantee you 12K in new MR in 12 weeks". Steve's headline ends "or work with you for free until you do"; Ryan would cut it to "get promoted to senior/staff engineer in 12 months".
- **Subheadline** with "without" plus what they already tried: "without ads trade shows or any new employees". It creates curiosity.
- **Message match** with the ad: the headline carries the ad's promise, timeline and mechanism (KARLTON).
- In both of his builds, social proof sits under the button, not above the video.

### 4.2 The first fold: one action
- `[D]` H10M. "two call to action buttons on the initial fold website is going to harm conversions that's because the confused mind doesn't buy". He credits the line to Dan Kennedy `[X:Kennedy]` elsewhere.
- `[X:Hormozi]` HADV. "something like 60% of people never get below" the fold.
- `[D]` PREMIUM. Eyes go headline, hero, CTA. "There's a lot of dead space on this page, and that's okay."

### 4.3 Directly below the video
- `[D]` UF, FT. One button that scrolls to the survey on the same page. Neither tiny nor full width. "10 to 20% more conversions or more applications" (UF, 2025-11-19); "5 to 15% of more applications" (FT, 2025-10-07). Same test, two ranges six weeks apart: quote 5 to 20%.
- `[D]` STEVE. Button copy: a benefit-worded button "slightly lowered conversion rate i think it was probably just too wordy", so "apply now" stayed. "See if I qualify" is a strategist's idea, untested.
- `[D]` STEVE. A logo bar under the button ("we've helped clients get promoted at" plus big-tech logos): "we AB tested we didn't have this at first and it improved conversions by 10%".
- `[D]` UF. MSP Fuel: "trusted by 100 MSP owners" with client photos.
- `[D]` RAVI (2024). A Trustpilot badge under every CTA on one client's long page: +149.2%.

### 4.4 The survey, on the same page
- `[D]` 200X. Embedded on the page, not in a pop-up: "we saw a 31% increase in conversion rate". The pop-up lost answers when people scrolled away to re-read.
- `[D]` UF. A progress bar for sunk cost; click options, not typing; easy yes/no first; "add the most invasive questions last" (revenue, email, phone), each with a reason ("100% confidential").
- `[D]` UF, STEVE. The "lowest common denominator" test at every step: "would they be confused ... is this a quiz like what is this". "Apply now" above the survey came from that test.
- `[D]` STEVE. Disqualifiers for Steve: not in a technical role, junior or intern, under 2 years at level, location; LinkedIn URL required.
- `[D]` CODIE. Every form field costs "5 to 40% I would say"; a phone field on an opt-in costs "30 40%". Opt-in and checkout forms, not application surveys.

### 4.5 The booking page
- `[D]` UF. Copy that tells them they are pre-qualified and ties to the benefit. A bar "Get approved ✓, Pick a time" for sunk cost. MSP Fuel's booking copy softens the headline: "without insinuating that we can guarantee everyone 12K new MR".
- `[D]` 200X. Testimonial cards under the calendar headed "It all started with a call": booking rate 38% to 50%, a 32% relative lift, organic funnel, one client.
- `[D]` AJS. "by not letting people book no more than 3 days out, even more, ideally 2 days out, and show rate like immediately jumps up 25%", from a 50% show rate. Whether 25% is relative or points is unclear. Booking 7 days out: "your show rate just plummets" (COACH).
- `[D]` 200X. Swapping a client's calendar tool for iClosed took booking rate from 35% to 15%.

### 4.6 Disqualified leads
`[D]` UF, FT. A "not a great fit" page. Some clients send them to a free Skool community.

### 4.7 The thank-you page
`[D]` UF (2025). "right now in 2025 one of the hardest metrics to get right especially with paid ads is show rate". His fix:
- Headline: "your call needs to be confirmed".
- A short video (60 seconds to 2 minutes, §3.2): find the invite, "go to your email right now find the calendar invite and hit yes I know the sender", join from a laptop, "please don't show up on your phone". Testimonials inside the video.
- Numbered big steps and a picture of the invite.
- No add-to-calendar button, because it drops the Zoom link.
- `[D]` AJS. An optional second video below that "just sells even more", unless they just watched an hour-long VSL.

### 4.8 Qualified but not booked (QFNB)
`[D]` UF. "if you go and you fill out my form but you do not book a call you'll get an email within about 30 minutes". The email asks if everything is okay. His EA answers replies and books them by hand: "I get clients that way that would have just been completely lost". He has no setter.

### 4.9 Between booking and the call
- `[D]` STEVE. "booking reminders texting people the night before the call free call videos from your sales reps all of those things are are good things to do". Rep videos are named once and never described.
- `[D]` COACH. One client turned each top objection into an email, sent 6 hours apart before the call; "the first one was like 98%" open rate.
- `[D]` COACH. A separate four-email pre-call sequence over 225 booked calls: "we saw show rate go up by 0.2% so literally nothing", close rate "exactly the same".
- `[X:Sabri Suby]` SUBY. A "pinky promise" question in the application; Ryan says it lifts show rate, with no number.

### 4.10 If the VSL is gated: follow-up
`[X:Charlie Morgan]` MORGAN. "I got about nine emails in 4 days from Charlie uh just pushing me back to either book a call or go and watch the vssl". Morgan's thank-you video states "a very strict no ghosting policy".

`[D]` HADV. His own list gets nothing but the weekly test email: "I don't really send out any more emails besides literally just conversion ideas".

### 4.11 Lead pages and application pages pull opposite ways
- `[D]` PREMIUM (2026-04-02). Lead page: removing everything below the fold took one client from 2.32% to 3.51%; another test +52%.
- `[D]` AJS (2025). Application page: extra sections below the fold lowered opt-ins, but "the strategy session booking rate 4xed", 5% to 20%, and cost per booked call went from "close to $1,000 down to like $250". "we'll see again if that sticks"; "it's inconclusive".
- `[D]` PREMIUM. "Premium should equal conversion. It should build trust." Apple-style scroll animations: "for most brands, I've seen it actually hurt conversions". He rebuilt one agency-made site "a lot more boring".
- `[D]` MICRO (2024). Load time: an opt-in pop-up that took 10 seconds to 2 minutes to load, replaced, took conversion "from 10% to over 20%" and lead cost from $41 to $8.

---

## 5. Offer and pricing

- `[D]` FT. The $2,000 line (§1.1). Above it, the price stays off the page.
- `[D]` TAKI. Custom or done-for-you work keeps the call (§1.5).
- `[X:Hormozi]` HADV, FAILING. Value equation: dream outcome times perceived likelihood, over time delay times effort. A weak offer makes funnel work "lipstick on a pig" `[D]`.
- `[X:Hormozi]` line, `[D]` story. PRICE, 7RULES. "It's never the price": a prospect who says no at $10K would find the money in hours for a $200K Ferrari at $10K (the car is $300K in the 7RULES telling). "either you need to lower the price or find a way to increase the value".
- `[D]` ALI. Say "investment": "that word typically resonates better with people rather than cost or price" (describing Ali Abdaal's page).
- `[D]` ALI, 7RULES. Price marinade: Ali's "6 years and $100,000 in courses and coaching" and a $10,000-an-hour Zoom rate before a $995 price. That page sells at checkout with no call.
- `[D]` 249K, quoted at §1.7. A $1 front end doubles close rate for one client.
- `[D]` UF. Guarantee wording on the MSP Fuel headline: "guarantee you 12K in new MR in 12 weeks" or you do not pay, for MSPs with 7+ employees and $70K+ MRR. Ryan reads the "without" line as naming what they already tried.
- `[D]` SCRIPT. The script's six inputs include the price point or commitment level; nothing says the video speaks it.
- `[D]` PRICE (2022). Course pricing by value, not time: one offer raised from $500 to $1,000, $2,000, $3,800, $5,800. Cole Gordon pushed him off $2,000 for his own services `[X:Cole Gordon]`.
- `[D]` 200X, EASIEST (2026-09-11, his newest video). Price tests both ways, low ticket: $149 to $99 gave +112% revenue (Yans Larson); $297 to $197 won, $197 to $147 did nothing. Crossing a round barrier moves volume; moving inside a band does not. Price tests are among the first things his agency runs on a direct checkout.
- `[D]` FT, 200X. An upsell adds about 15% ("a good Otto easy 10 to 15% increase"); start OTOs at $97. Low ticket only.
- `[X:Davie Fogarty]` (2024). A shown price ($1,790 a month against $8,000 of stacked value) and a revenue floor. Ryan praises the revenue disqualifier, not the shown price. The rule "show the price to disqualify" is `[M]`.
- `[X:Taki Moore]`, `[X:Daniel Priestley]` TAKI. "scarcity has to be real"; "people see through evergreen timers and ... only three spots".

---

## 6. Contradictions, both sides with dates

### 6.1 Gating the VSL behind an opt-in
- **For the gate, tested.** `[D]` MINER (2 Jan 2025): "a few years ago we did test it and it seemed pretty consistent and if you skip the optin page you got less calls the calls you got closed at a lower rate". In the same breath: "people might be burned out of opting into things now", so skipping "might now increase the throughput of call[s]". Jeremy Miner, Charlie Morgan and Ravi Abuvala gate paid traffic and leave organic ungated `[X]`.
- **Against the gate, untested.** `[D]` FT (7 Oct 2025): "most of the time I don't like doing this unless you're really good at email marketing and you're really going to use those emails". `[D]` STEVE (5 Mar 2026): "you are murdering your conversions in almost all cases unless you're absolutely amazing with email marketing or SMS marketing".
- **His arithmetic for the newer view.** `[D]` IMAN (12 Mar 2025): paid opt-in pages run "a 20 to 30% optin rate so they're paying typically $10 to $20 to get someone just to start watching their vsl".
- **Reading.** His one test favors the gate and predates January 2025. His stance hardened through 2025 and 2026 with no new test cited. State both. For warm traffic arriving from a link (a YouTube description, a reply to an email), every case he describes runs ungated.

### 6.2 Length
- `[D]` AJS (May 2025): "about 20 to 30 minutes" for a cold-ad VSL.
- `[D]` SCRIPT (Dec 2025): the script he modeled for MSP Fuel is 5 minutes.
- The norm and the model disagree by 15 minutes or more, and nothing pairs length with a surface. Read the 20 to 30 minutes as cold paid traffic only.

### 6.3 One cut for organic and paid, or one per source
- **One cut.** `[D]` STEVE (Mar 2026): "same landing page just duplicate it" and "this VSSL the exact same one is crushing on Meta Ads as well"; first-week cost per booked call $11, 9.5x return on "very low spend". `[D]` UF (Nov 2025): "The traffic sources can be either organic or ads It works great for both".
- **Per source.** `[D]` SCRIPT (Dec 2025), quoted at §1.8. `[D]` 200X (Jun 2026): proof density "you got to test these like per traffic source". `[D]` 249K (Sep 2025): organic sent straight to a VSL halved one client's close rate. `[D]` HAI (Mar 2026): more than half his Hormozi-style organic-as-ads flopped.
- **Reading.** The per-source rule governs borrowing someone else's script. Steve shows one cut crossing over when the offer and credential are strong. The corpus has that one case only.

### 6.4 Social proof
`[D]` 5VAR (May 2024): "It's really hard to overdo social proof." `[D]` 200X (Jun 2026): three to five times more proof cut organic conversion "like 50% lower"; on ads +32%, "not conclusive". Newer and tested wins; keep both with dates.

### 6.5 Benefit CTAs
He praises benefit buttons elsewhere ("yes let's create my pitch", "send me my book"). On Steve's page the benefit wording lost to "apply now" (STEVE). His own test beats his rule.

### 6.6 Production
High production won on his YouTube ads (2022) and on the skits client's cold traffic (2025). Low production wins for marketers selling to marketers (Morgan, Brown, 2024) `[X]`. He calls it niche-specific. All of it is ads or organic video; none is about a VSL.

### 6.7 Booking window
His rule says AJ&Smart's 4-day window is "guaranteed hurting their show rate"; their show rate is "about 80%. Which is decent" (AJS). He leaves it unresolved.

### 6.8 Whose framework
The 5 Ps, 5 Ws, objection drill and testimonial frame are Hormozi's, credited on camera (PSYCH, 2026). The seven beliefs (pain, desire, cost, value, doubt, trust) were "the seven beliefs that I found inside of every single successful seven and 8 figure funnel" in 7RULES (2024), and "Cole Gordon talks about the seven beliefs" in TAKI (2026). He names six of the seven in 2024. Credit Cole Gordon.

---

## 7. What fails

Each item is a test or a case he reports, with its year.

- **Tripling the social proof.** `[D]` 200X (2026). Three to five times more proof on one page: organic conversion "like 50% lower".
- **A benefit-worded CTA.** `[D]` STEVE (2026). "slightly lowered conversion rate"; "apply now" kept.
- **A funnel with no warm audience.** `[D]` OVENS (2023). His copy of Ovens' Google Doc VSL flopped after he sold his list and entered a new market where "no one really knew me".
- **Removing the low-ticket front end.** `[D]` 249K (2025). Close rate 60% to 30%, $30K to $50K of low-ticket revenue gone, worst month of the year.
- **Organic posts as ads, by default.** `[D]` HAI (2026). 8 ads run Hormozi's way: one hit 12.43x, "more than half the ads following his strategy flopped". `[D]` 249K (2025): the client's organic posts as ads were "struggling to make a profit".
- **A pre-call nurture sequence.** `[D]` COACH (2026). Four emails over 225 calls: show rate +0.2%.
- **A slow calendar tool.** `[D]` 200X. iClosed: booking 35% to 15%.
- **A survey in a pop-up.** `[D]` 200X. Answers lost on scroll; the embed won by 31%.
- **Two CTAs on the first fold.** `[D]` H10M (2024).
- **Pretty pages.** `[D]` PREMIUM (2026). Apple-style animation hurt "most brands" he has seen.
- **Booking far out.** `[D]` AJS, COACH. Past 3 days show rate drops; at 7 days it "plummets".
- **Fake scarcity.** `[X:Daniel Priestley]` TAKI.
- **The VSL itself, when it is bad.** `[D]` 200X. A better player does nothing when "your VSSL sucks".
- **His own 3-day split tests.** `[D]` 200X. At his old business he called ClickFunnels splits "for like 3 days". Now: one variable, even split, a significance calculator; the one threshold he states is 99% (HADV).

---

## 8. Benchmarks he quotes, with dates

All `[D]` unless marked. Each is one client or one remark, true for its year. Fuller tables live in the retrieval index.

| Number | Context | File, year |
|---|---|---|
| Close rate 25 to 30% "if you're good" | traditional VSL-to-call | TAKI, 2026 |
| Show rate 50%, plus 25% with a 2 to 3 day cap | one client | AJS, 2025 |
| Show rate about 80% | AJ&Smart, 4 days out | AJS, 2025 |
| Booking rate 38% to 50% | testimonial cards under calendar | 200X, 2026 |
| Opt-in rate 20 to 30% before a VSL | paid traffic, typical | IMAN, 2025 |
| Opt-in to call about 80% | "other clients who have similar funnels" | MICRO, 2024 |
| A traditional VSL "probably converts about 1%" | rule of thumb | IMAN, 2025 |
| $11 per booked call, 9.5x | Steve, first week of Meta | STEVE, 2026 |
| Earnings per visitor 11 cents to $2.80 | one low-ticket client, two years; EPV is "the metric that I think matters really the most" | HADV, 2026 |
| 0.5% to 3.68% over a year | the Frankenfunnel; "optimize before you scale" | 249K, 2025 |

**No watch-time, play-rate or completion figure exists for any VSL in the corpus.** `[A]`. The only percent-watched is an FHL speaker retargeting people who "watched 95% of your ad" `[X]`.

---

## 9. Whose idea is whose

| Hormozi `[X:Hormozi]` | Other people `[X:<name>]` | His own `[D]` |
|---|---|---|
| 5 Ps, 5 Ws, the five-objection drill, the post-CTA testimonial frame; the value equation; "it's never the price"; the salty pretzel and its 300 to 500%; organic posts as ads with a banner; 60% never scroll; the 40% drop without a video | Seven beliefs and "the bridge" (Cole Gordon, by 2026); 10 to 15 minute VSLs (Cole Gordon, as guest); modeling a proven funnel (Brunson); "trust has moved upstream" and "content is the new sales call" (Taki Moore); offer in 20 seconds (Charlie Morgan); the flywheel VSL (Iman Gadzhi); "Uber promise" (Alex Becker); timer and chapters (Sabri Suby); "the confused mind doesn't buy" (Dan Kennedy); awareness levels (Schwartz); Cialdini's six; copy-skill layer 1 (James, the Boring Marketer); crowd copy (Justin Book); the CRO skill (Corey Haines); the conversion heuristic (MECLABS) | The $2,000 line; the three fits; custom work keeps the call; no opt-in gate (stance, untested since); survey first by supply and demand; on-page survey; QFNB; the lowest common denominator test; 2 to 3 day booking cap; the confirm-your-call thank-you page; 20 to 30 minute cold-ad norm; 60 s to 2 min thank-you video; 30-second testimonial snippets; the five-step script process; EPV as north star; the 2023 four pillars (obstruction, resonance, awareness, coherence) |

**How his thinking moved.** 2022 to early 2023: his own info businesses, course pricing, Consulting Label (a revenue-share partner model), $90K to $210K a month by doubling ad spend (YTADS). August 2023: the four pillars, never named again after 2023. Late 2023 to 2025: teardowns, "Genius" in 12 titles, where most `[X]` material comes from. 2025: his own funnel written down, the gate turned against, show rate "really really plummeting". 2026: Claude builds (8 of 21 videos), Steve's $1.3M, Hormozi credited on camera, social proof found to backfire. Read any "his current method" claim by date.

---

## 10. What this corpus is not

Most of these 73 videos are Ryan reading other people's funnels from the outside: Hormozi, Gadzhi, Ovens, Suby, Morgan, Brunson, Abdaal, Saraev, Fogarty. Revenue figures for those creators are their claims as Ryan states them, and the funnel behind each is reverse-engineered from the public pages. The funnels are mostly B2C and creator businesses: courses, Skool communities, coaching, consumer products. The one B2B done-for-you case, MSP Fuel, was still being set up on 19 Nov 2025 and has no results on camera. His own results are client numbers (Steve, Joel Turner, the $7K-to-$450K client) and a vibe-coded side product; his agency's own revenue, booking and close figures are never given, and his newest own-business figure dates from January 2023. It says nothing on faceless or AI-voice VSLs, length by surface, VSL watch time, where a high-ticket VSL speaks the price, or B2B outbound. Those are `[A]` in `gap-register.md`.
