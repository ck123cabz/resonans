---
type: build
aliases: ["Invoice processing and other ROI worked cases"]
corpus: nate-herk
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-29
name: Invoice processing and other ROI worked cases
speaker: Nate Herk
provenance: D
sources: [q20, q44, q51]
videos: [i-ve-built-500-ai-workflows-this-is-what-businesses-want-in-2026.md, 18-months-of-pricing-ai-automations-in-21-mins.md, stop-selling-ai-agents-sell-ai-solutions-instead.md, build-sell-with-claude-code-10-hour-course.md]
---

# Invoice processing and other ROI worked cases

Four small builds Nate uses to show how he turns a process into an annual dollar figure. Only the onboarding case carries a build price; the invoice case is a value ceiling with no fee attached. The appointment setter has its own file (build-appointment-setting-agent.md).

## Invoice processing for a small accounting firm
`[B] · [D][G] · uploaded 2026-03-30 · i-ve-built-500-ai-workflows-this-is-what-businesses-want-in-2026.md · q51 · stable`

He frames it as an accountant facing 200 invoices on a Monday morning: open each, read it, pull vendor, amount, date and line items, type them into other software, categorize. For a small accounting firm he has worked with, that came to 50 hours a week, one full-time job. At $30 an hour: 50 x 30 x 52 = $78,000 a year.

The workflow: invoices arrive by email, the system extracts vendor, amount and date, checks against a chart of accounts, flags anything unusual, and pushes clean data where it needs to go. He keeps a human review step at the end, which is why the target time is 2 minutes, not zero. He adds that many document-processing automations need no AI at all.

> 50 hours a week basically a full-time employees entire job just moving numbers from pdfs into spreadsheets so at $30 an hour let's say that's $78,000 a year (i-ve-built-500-ai-workflows-this-is-what-businesses-want-in-2026.md)

> this will cut processing times down from 15 minutes per invoice let's just say to something like 2 minutes (i-ve-built-500-ai-workflows-this-is-what-businesses-want-in-2026.md)

## Invoice processing: the 45-hour rounding slip
`[R] · [D] · uploaded 2026-03-30 · i-ve-built-500-ai-workflows-this-is-what-businesses-want-in-2026.md · q51 · stable`

He says the change frees about 45 hours a week, "over $70,000" a year. 45 x 30 x 52 = $70,200, which matches. But 200 invoices x 13 minutes saved = 2,600 minutes = 43.3 hours, which gives about $67,600. The 45 is his rounding. No build fee is given, so this is a ceiling for pricing, not a priced deal.

> that would free up about 45 hours a week which is over $70,000 in direct labor savings per year before you even factor in things like human errors (i-ve-built-500-ai-workflows-this-is-what-businesses-want-in-2026.md)

## Construction phone orders: price against hard dollars
`[B] · [D] · uploaded 2026-08-01 · 18-months-of-pricing-ai-automations-in-21-mins.md · q20, q51 · stable`

He calls this one of the most profitable automations he has seen, and one of the simplest. It took a construction crew's daily phone orders and turned them into the text format the crew already used. It saved only about 45 minutes a day, but it stopped around $12,000 a month in scheduling errors. He separates freed hours from hard dollars lost to errors, and says the hard dollars are why a 45-minute saving was worth so much. The x12 = $144,000 a year figure is Gemini's arithmetic; he gives only the monthly number.

> it only saved like 45 minutes a day but it helped them avoid around $12,000 a month in scheduling errors and that second number isn't freed up hours ... it's hard dollars (18-months-of-pricing-ai-automations-in-21-mins.md)

The sizing question that surfaces numbers like this is "what happens when it goes wrong" (see script-discovery-call.md).

## Client onboarding: 60% automated for $3,000
`[B] · [D] · uploaded 2025-09-24 · stop-selling-ai-agents-sell-ai-solutions-instead.md; build-sell-with-claude-code-10-hour-course.md · q44, q51 · stable`

A team spends 10 hours a week on client onboarding at $25 an hour: $250 a week. He multiplies by 4 weeks to get about $1,000 a month, $12,000 a year. Automating only 60% saves $600 a month, "more than $7,000" a year (600 x 12 = 7,200). He prices it at $3,000, which pays back in 5 months (3,000 / 600). That is about 2.4x in year one, well under his 10x rule; he uses it to show a price reads as an investment once the return is visible. The 10-hour course (2026-03-12) repeats the passage word for word, so it is one origin.

> if the average employee is paid $25 an hour that's $250 a week multiply that by 4 weeks to get a month and suddenly the process is costing the business around $1,000 a month or $12,000 annually (stop-selling-ai-agents-sell-ai-solutions-instead.md)

> i'm only going to charge you $3,000 for the solution ... it's an investment that has a very clear measurable return that already pays for itself in 5 months (stop-selling-ai-agents-sell-ai-solutions-instead.md)

He annualizes with 4-week months here (48 weeks), and with 52 weeks in the appointment-setter telling of 2026-08-01. His method is not consistent across examples. Gemini labels this case "10 Hours to 10 Seconds"; that is the name of his AIS Plus n8n course, not of this example.

## Customer support: 1 hour a day, $12,000, $1,200 build
`[S] · [D] · uploaded 2026-08-01 · 18-months-of-pricing-ai-automations-in-21-mins.md · q20, q44, q51 · stable`

This is the answer he scripts for "Can you walk me through how you got to that price?". A rep spends an hour a day on a task, the hour costs about $50, the business loses about $12,000 a year, 10% of that is a $1,200 build, and the client 10xes it in year one.

> it takes a rep an hour a day manually and an hour of that rep's time is about 50 bucks ... that equals about $12,000 to the business so 10% of that $12,000 is $1,200 (18-months-of-pricing-ai-automations-in-21-mins.md)

He never shows a days-per-year step. Gemini's q44 and q51 add "$50 x 5 days x 52 weeks = $12,000", which is wrong: that product is $13,000. $12,000 implies about 240 working days (50 x 240). A 365-day year would give $18,250. Gemini's q22 version of this script, at $18,000 and $1,800, exists in no caption. Only $12,000 and $1,200 are his.
