---
type: build
aliases: ["Client Pack SaaS build"]
corpus: nate-herk
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-29
name: Client Pack SaaS build
speaker: Nate Herk
provenance: D
sources: [q13, q21, q25, q26, q42, q43]
videos: [build-sell-ai-saas-products-2-hour-course.md, anthropic-s-ceo-how-to-build-a-1-person-business-with-claude.md]
---

# Client Pack SaaS build

Client Pack turns a discovery-call transcript into a branded 10-slide proposal deck for AI agency owners. Nate built it end to end in "Build & Sell AI SaaS Products (2 HOUR COURSE)", uploaded 2026-08-10. A second SaaS, Agent Report Card, comes from a video uploaded 2026-09-18 and sits at the bottom of this file.

## Client Pack idea research: what the subagents scraped
`[B] · [D][G] · uploaded 2026-08-10 · build-sell-ai-saas-products-2-hour-course.md · q13 · stable`

He dictated the goal with Glido into both Codex and Claude Code, which worked out of one shared folder. Subagents scraped his own audience first, then Reddit and X, for agency pain points. The target buyer, AI agency owners, is his own audience.

> it looked through about 16,000 youtube comments it looked through about 8,000 comments and you know within posts inside of my plus community it looked at about 4,000 tweets (build-sell-ai-saas-products-2-hour-course.md)

Glido is the voice layer he dictates with. It is linked in the description; nothing on camera says he owns it.

## Client Pack names tested and the editorial fold design
`[B] · [D][G] · uploaded 2026-08-10 · build-sell-ai-saas-products-2-hour-course.md · q13 · stable`

Claude checked the name space and proposed three, then rendered each visually. He picked Client Pack in the "editorial fold" look because it read as trusted rather than AI.

> the three cleanest literal territories are client pack scope pack and proposal ready (build-sell-ai-saas-products-2-hour-course.md)

## Client Pack promise line and 3 Ps
`[S] · [D] · uploaded 2026-08-10 · build-sell-ai-saas-products-2-hour-course.md · q13 · stable`

Pain: agency owners rebuild proposals, statements of work and ROI math by hand after every discovery call. Person: AI agency owners and consultants. Promise: the line below, which is Claude's positioning output that he read out and accepted.

> without rebuilding every document from scratch so it hits on that pain point and then the short brand line is discovery in client ready out (build-sell-ai-saas-products-2-hour-course.md)

## Client Pack price: $39 a month, $390 a year, band $29 to $49
`[R] · [D][G] · uploaded 2026-08-10 · build-sell-ai-saas-products-2-hour-course.md · q13 · version-bound`

He first guessed $5 to $25 a month. The research said that was too low. The band is $29 to $49; Gemini's q13 widens it to $29–$50, which no caption supports. The "50 bucks" remark is about single-job tools in general.

> reddit surfaced 835 price sentences with a consistent band (build-sell-ai-saas-products-2-hour-course.md)

> final price point config currently says 39 bucks a month and 390 for the year research band is saying 29 to 49 (build-sell-ai-saas-products-2-hour-course.md)

The free tier is one watermarked deck. Afterward he said he would launch differently, with about five free deck generations and a conversation about how many decks a user needs.

## Value in one sitting
`[J] · [D] · uploaded 2026-08-10 · build-sell-ai-saas-products-2-hour-course.md · q13 · stable`

A SaaS user should reach the payoff in the first session, around 5 minutes. For Client Pack that moment is the first finished deck.

> maybe they get value in one sitting in 5 minutes they can get value (build-sell-ai-saas-products-2-hour-course.md)

## Client Pack stack
`[B] · [D][G] · uploaded 2026-08-10 · build-sell-ai-saas-products-2-hour-course.md · q13 · version-bound`

Next.js App Router, Supabase on the back end, Stripe checkout, deployed on Vercel. Codex runs the image work because it has GPT Image 2, and Sol in Codex runs the testing. The back-end model is "probably like opus 5". He switched the Claude session to Fable for planning.

> it's going to be a next.js app router we're going to have superbase on the back end we're going to have a stripe checkout (build-sell-ai-saas-products-2-hour-course.md)

Gemini's q13 lists GPT-6 and Astra in the stack; neither is in this video.

## Client Pack parallel build: two Opus workers in worktrees
`[B] · [D][G] · uploaded 2026-08-10 · build-sell-ai-saas-products-2-hour-course.md · q13 · version-bound`

He told Claude to split the build plan by dependency and run what it could in parallel, writing progress back to a shared file. The count he names is two Opus workers. Gemini's "9 parallel subagents" with named roles has no caption behind it; the UI, data layer, API routes, PDFs, extraction spikes and Puppeteer are review areas Sol checked.

> we have two opus workers that are now building each in an isolated work tree so that the codeex testing stays untouched (build-sell-ai-saas-products-2-hour-course.md)

## Client Pack two-call split and cost per deck
`[B] · [D][G] · uploaded 2026-08-10 · build-sell-ai-saas-products-2-hour-course.md · q13 · version-bound`

Call 1 analyzes the transcript: current state, constraints, what is in and out, ROI math, three investment options. Call 2 builds the deck. The smoke test cost 13 cents. After QA he put a pack at 16 to 20 cents, and every AI call logs tokens and dollars to the admin panel.

> it analyzed it for 4 cents generated the deck for 9 cents ... all of that happened with 13 cents for a full deck (build-sell-ai-saas-products-2-hour-course.md)

The slide names Gemini gives (Cover, Current Constraint, The Plan, What Moves the Math, Scope, Investment, Next Steps) are [M]; they were likely on screen.

## Client Pack PDF check: five defects and the geometry fit script
`[B] · [D][G] · uploaded 2026-08-10 · build-sell-ai-saas-products-2-hour-course.md · q13 · version-bound`

Puppeteer screenshotted every generated PDF, the agent looked at each image, found five layout defects, fixed them and re-proved on a fresh run. A script now checks all 10 slides every time. The captions do not name the five defects.

> i screenshotted every generated pdf and looked five layout defects found and fixed then reproven on a fresh generation a geometry fit check script now guards all 10 slides (build-sell-ai-saas-products-2-hour-course.md)

## Client Pack end-to-end test: 85 checks and the user journey
`[B] · [D][G] · uploaded 2026-08-10 · build-sell-ai-saas-products-2-hour-course.md · q13 · version-bound`

Sol in Codex tested the app for over 20 minutes. The journey it walked: sign in, brand kit and case study, create project, analyze, deck, Stripe checkout webhook, watermark removed.

> it signed in it did a brand kit and case study it created a project it analyzed it ... did a stripe checkout web hook ... watermark was removed (build-sell-ai-saas-products-2-hour-course.md)

> it ran 85 checks and said "okay cool this stuff is now good to go." (build-sell-ai-saas-products-2-hour-course.md)

## Client Pack security review: OWASP ASVS 5.0
`[B] · [D] · uploaded 2026-08-10 · build-sell-ai-saas-products-2-hour-course.md · q13 · version-bound`

Before deploy he ran his own security-review prompt against "OWSP 5.0", which he calls a GitHub repo. That matches OWASP ASVS 5.0. Gemini's "OWASP Top 10" and the Row Level Security detail are not in the captions.

> this is going to say to audit against the owsp 5.0 and that is actually a github repo (build-sell-ai-saas-products-2-hour-course.md)

## Client Pack moat: the back-end prompt
`[J] · [D] · uploaded 2026-08-10 · build-sell-ai-saas-products-2-hour-course.md · q13 · stable`

He says anyone could rebuild the app in a day, so the defensible part is the prompt behind the analyze step, fed by a grill-me interview of the expert. Gemini's list of what sits in that prompt (ROI calculators, LRP, objection handling) is [M].

> the real moat ... is that the prompt that powers this on the back end is what matters because anyone could come in here and rebuild this entire th[ing] (build-sell-ai-saas-products-2-hour-course.md)

No revenue, subscriber or conversion figures exist for Client Pack.

## Agent Report Card: QA software for support agents
`[B] · [D] · uploaded 2026-09-18 · anthropic-s-ceo-how-to-build-a-1-person-business-with-claude.md · q25, q26, q42, q43 · version-bound`

Agent Report Card tests customer-support agents that AI agencies deploy for clients. It runs 16 mystery-shopper tests, saves the evidence, and writes a client-ready report. His first run scored 88: 14 passed, 2 failed. He approved a tighter billing-dispute instruction, reran, and scored 88 again because a different test failed. Gemini's "12–16 tests on a receptionist" is wrong: it is 16 tests on a support agent.

> the app runs that agent through 16 tests think of them like mystery shoppers some ask normal questions while others try to get the agent to take a risky action (anthropic-s-ceo-how-to-build-a-1-person-business-with-claude.md)

## Agent Report Card 3 Ps and the $499 x 168 math
`[R] · [D] · uploaded 2026-09-18 · anthropic-s-ceo-how-to-build-a-1-person-business-with-claude.md · q25, q42 · stable`

He named the 3 Ps as the "AI monetization readiness assessment", ordered pain, person, promise. Person: an AI agency deploying support agents for clients. At $499 a month, 168 customers pass $1M ARR (168 x 499 x 12 = $1,005,984). The "$39 needs 2,136 users" line is Gemini's arithmetic. His first milestone is five agencies paying.

> the person is an ai automation agency who is deploying customer support agents for their clients and the promise is that agent report card runs your agents through 16 or more high-risisk scenarios (anthropic-s-ceo-how-to-build-a-1-person-business-with-claude.md)

> at $499 bucks per month agent report card would need 168 active customers monthly to pass $1 million in annual recurring revenue (anthropic-s-ceo-how-to-build-a-1-person-business-with-claude.md)
