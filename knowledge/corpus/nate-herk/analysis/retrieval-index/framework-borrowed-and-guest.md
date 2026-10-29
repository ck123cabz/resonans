---
type: framework
aliases: ["Borrowed and guest frameworks"]
corpus: nate-herk
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-29
name: Borrowed and guest frameworks
speaker: various; each heading names the owner
provenance: D
sources: [q35, q37, q43]
videos: [gpt-6-astra-finally-solves-ai-video-editing-full-guide.md, the-skill-that-10x-d-my-claude-code-projects.md, 18-months-of-pricing-ai-automations-in-21-mins.md, the-playbook-for-a-100m-ai-agency.md, stanford-s-method-turns-claude-into-a-phd-level-research-team.md, anthropic-engineer-explains-what-to-build-instead-of-ai-agents.md, claude-code-skills-just-got-even-better.md, how-to-actually-choose-the-right-ai-agent.md, i-deleted-all-my-claude-skills-and-claude-got-smarter.md, why-your-ai-offer-isn-t-selling-and-how-to-fix-that.md, finally-agent-loops-clearly-explained.md, this-one-plugin-just-10x-d-claude-code.md]
---

# Borrowed and guest frameworks

Frameworks Nate Herk teaches or hosts but did not create. Each heading names the true owner. Where Nate reads someone else's words on camera, the reading is `[D]` and the author is named. Guest speech carries `[D:guest:<name>]` and stays out of Nate's own positions.

## Andrej Karpathy: three layers (spec, verifier, environment)
`[F] · [D] · uploaded 2026-09-08 to 2026-09-23 · gpt-6-astra-finally-solves-ai-video-editing-full-guide.md; build-sell-with-codex-5-hour-course.md · q43, q50 · stable`

Karpathy's method, read in a one-minute reel that Nate edits as demo footage on 2026-09-08. Whose voice reads the reel is open (I-6). Layer 1, the spec: work with Claude to write a detailed spec before the task. Layer 2, the verifier: define a good result first, then give Claude a way to check itself (another model, real data, tests). Layer 3, the environment: a workspace preloaded with instructions, knowledge, skills and rules. Gemini credited it to Cole Medin; the Cole interview never mentions Karpathy.

> andre karpathy thinks there's a much better way to work with ai and his method has three layers layer one is the spec (gpt-6-astra-finally-solves-ai-video-editing-full-guide.md)

> layer two is the verifier before claude does anything define exactly what a good result looks like then give it ways to actually check its own work (gpt-6-astra-finally-solves-ai-video-editing-full-guide.md)

> layer three is the environment build a workspace where claude already has your instructions your knowledge your skills and your rules every single time you use it (gpt-6-astra-finally-solves-ai-video-editing-full-guide.md)

## Matt Pocock: Grill Me (pointer)
`[S] · [D] · uploaded 2026-06-04 to 2026-09-21 · the-skill-that-10x-d-my-claude-code-projects.md; build-sell-with-codex-5-hour-course.md · q07, q39 · stable`

Pocock's skill, named in 14 files. Nate says his version "was inspired by Matt PCO's Grill Me" (captions spell Pocock "PCO"). Prompt text and Nate's checkpoint upgrade are in `script-grill-me-and-95-confidence.md`.

## Jonathan Stark: cost, value, price and the landscaper
`[F] · [D] · uploaded 2026-08-01; 2026-08-25 · 18-months-of-pricing-ai-automations-in-21-mins.md; the-3-step-system-behind-my-20k-month-ai-agency-retainers.md · q20, q35 · stable`

Stark spoke at AIS Live, and Nate relays him with credit on 2026-08-01. Hourly billing "pays you more to be slow". Cost doesn't justify price. The landscaper who mows for $100, buys a new truck and asks $200 loses the customer. On 2026-08-25 Nate says the line his own way, "value justifies price". Both forms are his (X-09).

> a pricing guy named jonathan stark came and spoke at ais live ... the problem with hourly is that it pays you more to be slow (18-months-of-pricing-ai-automations-in-21-mins.md)

> cost doesn't justify price price justifies cost and jonathan made a really great example of a landscaper (18-months-of-pricing-ai-automations-in-21-mins.md)

Nate's own exception: hourly is fine "for your first two or three projects when you've got you know nothing to point at". Whether his why-this, why-now, why-me buckets also came from Stark is open (R44-12).

## [D:guest:Devin Karns] Custom AI Studio escalator
`[F] · [D:guest:Devin Karns] · uploaded 2026-05-25 · the-playbook-for-a-100m-ai-agency.md · q24, q35 · version-bound`

Devin Karns runs Custom AI Studio. His four steps: a one-hour fixed-price AI workshop, a paid discovery blueprint at "15 to 35k", a fixed build of the blueprint, then a managed partnership where he takes "15% of the topline revenue". No dollar figure is spoken for the workshop or the build. He also prefers mid-market clients over small businesses; that view is his, not Nate's (B-C11).

> we charge around 15 to 35k for this right now (the-playbook-for-a-100m-ai-agency.md)

> i'm going to take 15% of the topline revenue (the-playbook-for-a-100m-ai-agency.md)

## [D:guest:Devin Karns] M&A rerating at scale
`[J] · [D:guest:Devin Karns] · uploaded 2026-05-25 · the-playbook-for-a-100m-ai-agency.md · q24 · stable`

A $2 million a year consultancy sells for about $2 million. At $6 million a year with systematic delivery, he says a buyer pays about 5x, "30 million". The "1x to 2x EBITDA" line in q24 is not in the captions.

> if you're making six million a year then it's like "oh now i can sell this business for like 5x right i can sell it for 30 million." (the-playbook-for-a-100m-ai-agency.md)

## Stanford STORM: five research perspectives
`[F] · [D] · uploaded 2026-06-29 · stanford-s-method-turns-claude-into-a-phd-level-research-team.md · q04, q05 · stable`

Stanford's research method, built by Nate as a `storm-research` skill. Five lenses run in parallel.

> storm utilizes these five perspectives we've got a practitioner an academic a skeptic an economist and a historian (stanford-s-method-turns-claude-into-a-phd-level-research-team.md)

## Anthropic: progressive disclosure, DRY, "a tool for its future self"
`[F] · [D] · uploaded 2026-09-13 · anthropic-engineer-explains-what-to-build-instead-of-ai-agents.md · q43 · stable`

He relays an Anthropic engineers' talk. Progressive disclosure: at start Claude reads only skill names and descriptions, the body loads on match. His mechanic line: hundreds of tools owned, a few on the bench. DRY: save a proven script in the skill and reuse it. Anthropic's example is presentation styling Claude rewrote every run until it saved the script as "a tool for its future self".

> skills work in a very similar way because of something that enthropic calls progressive disclosure so when claude starts it doesn't read the full instructions (anthropic-engineer-explains-what-to-build-instead-of-ai-agents.md)

> they had claude save that script inside the skill as in their own words a tool for its future self (anthropic-engineer-explains-what-to-build-instead-of-ai-agents.md)

## Anthropic: capability uplift versus encoded preference
`[F] · [D] · uploaded 2026-03-05 · claude-code-skills-just-got-even-better.md · q04 · stable`

Anthropic's two skill types, read by Nate. Details and quotes in `framework-6-step-skill-method-and-bike-method.md`.

## Boris Cherny: delete all skills every 6 months
`[J] · [D] · uploaded 2026-09-11; 2026-08-12 · how-to-actually-choose-the-right-ai-agent.md; i-deleted-all-my-claude-skills-and-claude-got-smarter.md · q35, q47 · version-bound`

Cherny, who created Claude Code, tweeted that you should delete all your skills every 6 months. The line sits in a cold-open teaser in the Mark Kashef interview, and captions cannot say whether Nate or Mark speaks it (I-5, open). Nate's own position, from 2026-08-12: he did not sweep-delete his setup, and he warns against applying anyone's advice wholesale.

> boris churnney dropped a tweet saying you should delete all of your skills every six months (how-to-actually-choose-the-right-ai-agent.md)

> the reason why i didn't actually go out and sweep delete all of my stuff is because based on my findings and my testings that wouldn't be as v[aluable] (i-deleted-all-my-claude-skills-and-claude-got-smarter.md)

## [D:guest:Nate B. Jones] The last mile
`[J] · [D:guest:Nate B. Jones] · uploaded 2026-07-20 · why-your-ai-offer-isn-t-selling-and-how-to-fix-that.md · q35, q47 · stable`

Nate B. Jones's claim on Nate Herk's podcast: builders add value by connecting models to real workflows. Gemini gave the line to Nate Herk.

> reality is surprisingly detailed nate right like going the last mile is how we deliver value as builders (why-your-ai-offer-isn-t-selling-and-how-to-fix-that.md)

## Reason-act-observe: how "some people" describe loops
`[F] · [D] · uploaded 2026-06-19 · finally-agent-loops-clearly-explained.md · q37 · stable`

Not his framework. He mentions think-act-see and reason-act-observe as other people's framing. His own two pillars for a loop are a goal and verification.

> there's really two most important pillars of that in my mind which are the goal what is the actual objective ... and then verification how does the agent know what that stop condition is (finally-agent-loops-clearly-explained.md)

## Superpowers plugin: TDD for skills
`[F] · [D] · uploaded 2026-04-12 · this-one-plugin-just-10x-d-claude-code.md · q43 · stable`

The Superpowers plugin's writing-skills meta-skill: write a failing test scenario, then the skill that passes it. Nate reads it off the plugin's docs; he never teaches TDD in his own voice.

> write a failing test scenario first then write a skill to make it pass (this-one-plugin-just-10x-d-claude-code.md)
