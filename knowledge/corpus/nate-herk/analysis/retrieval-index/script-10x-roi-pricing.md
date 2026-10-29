---
type: script
aliases: ["10x ROI pricing walkthrough"]
corpus: nate-herk
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-29
name: 10x ROI pricing walkthrough
speaker: Nate Herk (case against hourly relayed from Jonathan Stark)
provenance: D
sources: [q20, q22, q39, q44, q45, q51]
videos: [18-months-of-pricing-ai-automations-in-21-mins.md, how-to-price-ai-workflows-without-losing-clients.md, build-sell-with-claude-code-10-hour-course.md, stop-selling-ai-agents-sell-ai-solutions-instead.md, build-sell-with-codex-5-hour-course.md]
---

# 10x ROI pricing walkthrough

The math Nate uses to set a build price and the words he uses to explain it when a client asks "how did you get to that number". Rules span 2025-11-30 (the PRICE video) to 2026-08-01 (the pricing retrospective). The framework wrapper is in framework-price.md; worked client cases are in build-appointment-setting-agent.md and build-invoice-processing-and-roi-cases.md.

## The $12,000 / $1,200 explanation, verbatim
`[S] · [D] · uploaded 2026-08-01 · 18-months-of-pricing-ai-automations-in-21-mins.md · q20, q39, q44 · stable`

A support task takes a rep an hour a day. That hour costs about $50. He calls the yearly cost about $12,000, takes 10% as the build price, and says the client 10xes it in year one. He gives this as the way to explain it to a client.

> it takes a rep an hour a day manually and an hour of that rep's time is about 50 bucks right like that's how much it's costing the business over a year that equals about $12,000 (18-months-of-pricing-ai-automations-in-21-mins.md)

> so 10% of that $12,000 is $1,200 so the build is $1,200 bucks so conservatively you will be 10xing your investment of that $1,200 just in the first year (18-months-of-pricing-ai-automations-in-21-mins.md)

The same $12,000 → $1,200 line appears in the PRICE video (2025-11-30).

> if the workflow is going to save them $12,000 10% of that would be $1,200 and that's your starting point for pricing (how-to-price-ai-workflows-without-losing-clients.md)

Warnings on Gemini's versions. q22 runs this script to $18,000 and a $1,800 build; no caption has either number. q44 and q51 derive the $12,000 as $50 × 5 days × 52 weeks. That product is $13,000. His $12,000 fits about 240 working days, and he never shows the day count.

## Annualize: weekly hours × hourly rate × 52
`[R] · [D] · uploaded 2026-08-01 · 18-months-of-pricing-ai-automations-in-21-mins.md · q20, q45, q51 · stable`

His worked number: 20 hours a week at $40 is $800 a week, × 52 = $41,600. The name "cost of inaction" is Gemini's and appears in no transcript; he says "annualized" and "ceiling".

> 20 hours a week at $40 an hour is about $800 bucks a week and if you multiply that by 52 which is 52 weeks in the year that's $41,600 annualized (18-months-of-pricing-ai-automations-in-21-mins.md)

He is not consistent across videos. The PRICE video (2025-11-30) uses 4-week months: $800 × 4 = $3,200 a month, "about $38,000" a year. The onboarding example (2025-09-24) also uses × 4.

## Anchor: 10% to 20% of first-year value
`[R] · [D] · uploaded 2026-08-01 · 18-months-of-pricing-ai-automations-in-21-mins.md · q20, q44, q45, q51 · stable`

> what I like to do is pick somewhere between 10% and 20% of that number as my starting point (18-months-of-pricing-ai-automations-in-21-mins.md)

The PRICE video of 2025-11-30 anchors at 10%. q42's "10% to 15%" is Gemini's narrowing.

## The 10x golden rule and his 7.5x admission
`[R] · [D] · uploaded 2025-11-30; 2026-08-01 · how-to-price-ai-workflows-without-losing-clients.md; 18-months-of-pricing-ai-automations-in-21-mins.md · q20, q51 · stable`

The client should see about 10x in year one. On his own $5,500 appointment-setter build he admits the multiple is about 7.5, and covers the gap with projected lead growth.

> remember the 10 times investment kind of golden rule they should roughly see 10 times the return on whatever they pay you within the first year (how-to-price-ai-workflows-without-losing-clients.md)

> which comes out to about a 7.5 multiple on their initial investment now typically I like to say the golden rule is that you need to be able to show the client that their investment is going to 10x (18-months-of-pricing-ai-automations-in-21-mins.md)

## Hard dollars beat freed hours
`[J] · [D] · uploaded 2026-08-01 · 18-months-of-pricing-ai-automations-in-21-mins.md · q20, q51 · stable`

A construction client's automation saved only 45 minutes a day but avoided about $12,000 a month in scheduling errors. He prices against the $12,000 a month, which he calls hard dollars.

> it only saved like 45 minutes a day but it helped them avoid around $12,000 a month in scheduling errors and that second number isn't freed up hours ... it's hard dollars (18-months-of-pricing-ai-automations-in-21-mins.md)

## Onboarding example: 60% automated, $3,000 price
`[B] · [D] · uploaded 2025-09-24; 2026-03-12 · stop-selling-ai-agents-sell-ai-solutions-instead.md; build-sell-with-claude-code-10-hour-course.md · q44, q51 · stable`

10 hours a week at $25 is $250 a week, × 4 = $1,000 a month, $12,000 a year. Automating 60% saves $600 a month, "more than $7,000" a year, against a $3,000 price that pays back in 5 months. This one is about 2.4x.

> if the average employee is paid $25 an hour that's $250 a week multiply that by 4 weeks to get a month and suddenly the process is costing the business around $1,000 a month or $12,000 annually (build-sell-with-claude-code-10-hour-course.md)

## Maintenance: $400 flat, or $200 to $1,500 per system
`[R] · [D] · uploaded 2026-08-01; 2025-11-30 · 18-months-of-pricing-ai-automations-in-21-mins.md; how-to-price-ai-workflows-without-losing-clients.md · q20, q51 · version-bound`

On 2026-08-01 his standard plan was $400 a month across all projects. It keeps the agreed build running through API and model changes; new features are a separate talk. He warns that a $30,000 system may cost more than $400 to maintain. In 2025-11-30 he gave a range per system and, for one client, $550 at about 10% of the fee. Gemini's "10% to 25% of build" has no 25% in any caption, and "$400 to $20,000" joins his maintenance plan to his agency's retainer minimum.

> at this point in my career our maintenance package was 400 bucks a month (18-months-of-pricing-ai-automations-in-21-mins.md)

> it's a light retainer that covers reliability and support now this could be a flat monthly fee something like 200 to 1,500 bucks per month per system (how-to-price-ai-workflows-without-losing-clients.md)

## Retainer margin: cost $5,000, price $10,000
`[R] · [D] · uploaded 2025-11-30 · how-to-price-ai-workflows-without-losing-clients.md · q20, q51 · stable`

He names 50% to 70% as the target band and 50% as the floor. Gemini's "$10,000 to $15,000" upper figure is not in the captions.

> the general target margin for this type of work is 50 to 70% 50% is a good baseline (how-to-price-ai-workflows-without-losing-clients.md)

> if it costs you $5,000 per month to deliver you might want to price the retainer at $10,000 per month (how-to-price-ai-workflows-without-losing-clients.md)

## Hourly as an on-ramp for the first two or three projects
`[J] · [D] · uploaded 2026-08-01 · 18-months-of-pricing-ai-automations-in-21-mins.md · q20, q45 · stable`

> I'm not saying hourly is never okay i think for your first two or three projects when you've got you know nothing to point at ... billing hourly is a safer ask (18-months-of-pricing-ai-automations-in-21-mins.md)

The "$100 an hour" in q20 and q45 is an illustration from the Grok Bots course ("let's just say 100 bucks an hour"), not a rate he set.

## The case against hourly, relayed from Jonathan Stark
`[F] · [D] · uploaded 2026-08-01 · 18-months-of-pricing-ai-automations-in-21-mins.md · q20, q45 · stable`

Stark spoke at AIS Live; Nate credits him on camera. Two developers billed at $150 an hour: the fast one bills one day, the slow one bills three. Nate adds his own line that getting good at the job cut your income. The "price justifies cost" and landscaper lines are in framework-borrowed-and-guest.md.

> a pricing guy named Jonathan Stark came and spoke at AIS Live ... the problem with hourly is that it pays you more to be slow (18-months-of-pricing-ai-automations-in-21-mins.md)
