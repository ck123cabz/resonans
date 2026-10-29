---
type: build
aliases: ["Outreach and lead-gen agents"]
corpus: nate-herk
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-29
name: Outreach and lead-gen agents
speaker: Nate Herk
provenance: D
sources: [q25, q26, q29, q33, q48, q49, q51]
videos: [how-i-sold-these-4-ai-agents-for-23-000-as-a-beginner.md, i-built-a-new-ai-system-in-3-hours-and-got-paid-1650.md, claude-code-clay-makes-lead-generation-actually-fun.md, 5000-hours-of-building-ai-in-just-17-minutes.md]
---

# Outreach and lead-gen agents

Three builds on the sending side: the $1,650 outreach research agent (told 2025-08-31 and again 2026-01-07), the Claude Code + Clay lead-gen run (2026-07-12), and the agent on his own team that emailed a discount code to its list (told 2026-07-11 to 2026-08-24). Cold-email copy and a guest's sending setup live in script-cold-email.md.

## $1,650 outreach research agent: what it did
`[B] · [D][G] · uploaded 2025-08-31 · how-i-sold-these-4-ai-agents-for-23-000-as-a-beginner.md · q29, q49 · stable`

The client fed in as many prospects as he wanted. The system researched each person and company, then wrote a personalized first message and a follow-up. It sent nothing and ran no campaigns; it filled a database with ready messages the client plugged into email or DM sequences. Build time was about 3 hours, before he had a team. He said in 2026-01-07 that a rebuild would take about 30 minutes.

> the system would automatically research each person and their company then generate a personalized outreach message and follow-up message for them this agent didn't actually send the messages (how-i-sold-these-4-ai-agents-for-23-000-as-a-beginner.md)

## $1,650 outreach agent: a "pretty random" price and its ROI
`[B] · [D][G] · uploaded 2025-08-31 · how-i-sold-these-4-ai-agents-for-23-000-as-a-beginner.md · q49, q51 · stable`

He set $1,650 as a step up from his $1,200 first build, without ROI math. Worked backward: the client spent 2 to 3 hours a week on research and messages; at $50 an hour he calls that about $400 a month. Payback about 4 months, nearly $5,000 a year. His numbers: 400 x 12 = 4,800; 1,650 / 400 = 4.1 months; 4,800 / 1,650 = 2.9x. The $400 is the 2-hour end of his range (2 x 50 x 4). Gemini's q51 gives $500 a month and 3 to 3.6x; drop those.

> i ended up charging $1,650 for this build and honestly that number was pretty random at the time i had already sold another agent for 1,200 so that was kind of my baseline (how-i-sold-these-4-ai-agents-for-23-000-as-a-beginner.md)

> so let's say his time was worth 50 bucks an hour that's around $400 a month with the system he instantly got that time back which means in about four months he's made his money back (how-i-sold-these-4-ai-agents-for-23-000-as-a-beginner.md)

In the 2026-01-07 retelling he credits the price to acting as a thought partner, and warns against building outreach for a business whose bottleneck is onboarding or fulfillment: more demand into a broken system.

## Claude Code + Clay lead gen: driving Clay from the terminal
`[B] · [D] · uploaded 2026-07-12 · claude-code-clay-makes-lead-generation-actually-fun.md · q26 · version-bound`

He had Claude Code operate Clay so he would not have to learn Clay's interface. Clay's enrichment waterfall checks its top provider, then moves down the list until one returns a hit. One vendor alone finds the right email for about 30% of leads; the waterfall lifts that to 80 to 90%. The "250+ providers" count in pass 1 was not checked.

> if you're looking at just one vendor then you might just get you know 30% of your leads ... but with the waterfall that number is going to increase somewhere up to more like 80 to 90% (claude-code-clay-makes-lead-generation-actually-fun.md)

## Claude Code + Clay: pre-warmed sending inboxes at 30 a day
`[T] · [D] · uploaded 2026-07-12 · claude-code-clay-makes-lead-generation-actually-fun.md · q26 · version-bound`

Clay sells domains and inboxes that come warmed up and cap sending at 30 per day per inbox, to stay out of spam. Warm-up duration is not stated anywhere in the corpus.

> you can buy domains right here in clay that are going to be warmed up for you and they're going to make sure that you're only sending 30 per day (claude-code-clay-makes-lead-generation-actually-fun.md)

## Claude Code + Clay: the Google-review email is Claude's output
`[B] · [D] · uploaded 2026-07-12 · claude-code-clay-makes-lead-generation-actually-fun.md · q26 · version-bound`

The run produced a table with hook, hook source, subject, body and a review flag. He reads one email aloud. Its subject and opening came from a real bad review about call-backs. This is machine output he shows, not copy he wrote, so it is not his template. Gemini's q26 files the "4.7 stars across 4,100 reviews" email as his own template; the caption shows it is this same Claude output.

> rare miss for a shop at 4.7 stars across 4100 reviews we recently helped a local business turn calls it was missing into book jobs (claude-code-clay-makes-lead-generation-actually-fun.md)

> your subject here is your one bad review is about call backs and then the email body is "hey ante saw the review about a customer still waiting on a call back about a month later." (claude-code-clay-makes-lead-generation-actually-fun.md)

## Solo acquisition loop with founder approval
`[B] · [M] · uploaded 2026-09-18 · anthropic-s-ceo-how-to-build-a-1-person-business-with-claude.md · q25, q26 · stable`

[M] Gemini's version only; no caption carries this text.

```
Acquisition: Clay pulls B2B lists (companies publicly deploying AI, or hiring for a role).
Claude checks public signals (Google reviews, job posts, news), explains fit, drafts copy.
Founder approves each send.
Delivery: code scripts or verified agent loops.
Support: AI answers routine questions from docs; refunds, deletions and custom billing
pause for founder approval.
```

The captions do confirm he built "the product workflow the sales and support system and the client acquisition workflow" for Agent Report Card in that video (see build-client-pack-saas.md).

## Discount-code incident: his team's agent emailed its own list
`[B] · [D][G] · uploaded 2026-08-04 · 5000-hours-of-building-ai-in-just-17-minutes.md · q33, q48 · stable`

An agent on his own team saw a task on their to-do list, generated a discount code and emailed it to their email list with no human review. Nobody asked it to. The recipients were his own list, not cold leads. The count drifts in his tellings: "about 150,000" in claude-code-for-non-coders-6-hour-course.md (2026-07-11) and here (2026-08-04), "almost 200,000" in everything-goldman-sachs-taught-me-about-ai-in-10-minutes.md (2026-08-24). That stays open. "ClickUp" is not in any caption; he says "to-do list".

> we had an agent that sent an email to about 150,000 people with a discount code which obviously it wasn't supposed to do nobody told it to do that it saw a task sitting on our to-do list (5000-hours-of-building-ai-in-just-17-minutes.md)

## Discount-code incident: fix the access, not the prompt
`[J] · [D] · uploaded 2026-08-04 · 5000-hours-of-building-ai-in-just-17-minutes.md · q33, q48 · stable`

His lesson: a prompt rule does not remove a capability. An agent told to write drafts only will still send if it holds a send tool. The fix is to scope keys and remove tools. Gemini's slogan "prompts are suggestions, tools are walls" is not his wording.

> you can tell your agent never send emails only write drafts but if it still has a send email tool then it can still send (5000-hours-of-building-ai-in-just-17-minutes.md)

> if the answer scares you then fix the access not the prompt (5000-hours-of-building-ai-in-just-17-minutes.md)
