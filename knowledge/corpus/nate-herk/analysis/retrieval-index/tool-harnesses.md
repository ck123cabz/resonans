---
type: tool
aliases: ["Agent harnesses"]
corpus: nate-herk
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-29
name: Agent harnesses
speaker: Nate Herk
provenance: D
sources: [q14, q16, q38]
videos: [hermes-agent-zero-to-personal-ai-assistant-1-hour-course.md, build-sell-with-codex-5-hour-course.md, build-sell-ai-saas-products-2-hour-course.md, 100-hours-testing-claude-code-vs-antigravity-honest-results.md, 100-hours-testing-deepseek-harness-vs-claude-code-what-you-need-to-kno.md, 100-hours-testing-clawdbot-vs-claude-code-honest-results.md, grok-bot-is-for-real-what-you-need-to-know.md, build-sell-grok-bots-2-hour-course.md, how-to-actually-choose-the-right-ai-agent.md, 100-hours-testing-claude-code-vs-chatgpt-codex-honest-results.md]
---

# Agent harnesses

The harnesses Nate Herk runs or tested between January and September 2026: Claude Code, Codex, Antigravity, the DeepSeek harness, Grok Bot, Hermes, OpenClaw (first called Clawdbot) and Cursor. Each section gives price, plan, limits and his verdict with the upload date. Test numbers live in `tool-harness-head-to-heads.md`; model prices live in `tool-models-and-prices.md`.

## Claude Code: plans and the "daily driver" verdict
`[T] · [D] · uploaded 2026-05-10 · hermes-agent-zero-to-personal-ai-assistant-1-hour-course.md; 100-hours-testing-claude-code-vs-chatgpt-codex-honest-results.md · q38 · version-bound`

Plans he names: Pro at $20 a month, Max 5x at $100, Max 20x at $200. On 2026-05-10, inside the Hermes course, he still calls Claude Code the tool where most of his day happens.

> claude code is still my daily driver that's where I do 90% of my knowledge work throughout the day (hermes-agent-zero-to-personal-ai-assistant-1-hour-course.md)

> claude pro at 20 bucks a month ... claude max 5x at 100 bucks a month (100-hours-testing-claude-code-vs-chatgpt-codex-honest-results.md)

q38's "S-tier" and "most valuable subscription" labels are Gemini's wording. Limits: 5-hour rolling windows plus weekly quotas. Anthropic doubled the 5-hour limits on 2026-05-07 (see `tool-claude-code-features-and-tokens.md`).

## Codex: plans and the $14,000 inference line
`[T] · [D] · uploaded 2026-09-21 · build-sell-with-codex-5-hour-course.md; build-sell-ai-saas-products-2-hour-course.md · q16 · version-bound`

Codex comes with a ChatGPT plan at $20, $100 or $200 a month. He says the $200 plan buys far more compute than it costs. In the SaaS course (2026-08-10) he puts either lab's $200 plan at "$8,000 to $14,000 of inference".

> the subscription of codeex actually gets you about $14,000 of inference if you use the entire subscription (build-sell-with-codex-5-hour-course.md)

What Codex has that Claude Code lacks, per q16 [M]: native git worktrees in the desktop app, an in-app browser for visual QA, native image generation with GPT Image 2, and a voice mode. It needs an explicit instruction or `/goal` to spawn subagents. The 400,000-token context figure in q38 was not found in the captions and stays [M].

## Antigravity: looks better, thinks worse
`[T] · [D] · uploaded 2026-04-13 · 100-hours-testing-claude-code-vs-antigravity-honest-results.md · q14 · version-bound`

Google's harness, running Gemini 3 Pro and 3.1 Pro in his test. His one-line verdict came after three builds:

> i think that claude code thinks better but i think that anti-gravity makes things look better and gemini is also noticeably faster (100-hours-testing-claude-code-vs-antigravity-honest-results.md)

Use it for fast front-end prototypes and its free tier. Keep Claude Code for production logic, long sessions, skills and MCP. The "rule drift by day 3" claim in q14 is [M]; no caption check was run.

## DeepSeek harness: free and open, no vision
`[T] · [D] · uploaded 2026-08-23 · 100-hours-testing-deepseek-harness-vs-claude-code-what-you-need-to-kno.md · q14 · version-bound`

An open-source harness from DeepSeek. The harness costs nothing; inference on DeepSeek V4 Flash or Pro is cheap but paid.

> the harness is completely free you could run this harness 24/7 with a free model and you would never get charged but for inference that's not free (100-hours-testing-deepseek-harness-vs-claude-code-what-you-need-to-kno.md)

Why he would pick it: you can change the harness itself. He compares Claude Code to a car where you can only swap the engine, and the DeepSeek harness to one where you can move the seats and the wheel. Against it: DeepSeek V4 has no vision, so it cannot screenshot-check its own UI. He also warns to have Claude Code or Codex review any open-source plugin before installing it.

## Grok Bot: $200 at launch, $30 by August 31
`[T] · [D] · uploaded 2026-08-12; 2026-08-31 · grok-bot-is-for-real-what-you-need-to-know.md; build-sell-grok-bots-2-hour-course.md · q17, q38 · version-bound`

Access changed twice in 19 days. On 2026-08-12 you needed Cursor's Ultra plan. By 2026-08-31 it was $30 a month through Super Grok.

> in order to try this out you are going to have to be on the cursor ultra plan (grok-bot-is-for-real-what-you-need-to-know.md)

> you can get access to grockbot for just 30 bucks a month so it used to be when it first came out it was just the 200 bucks a month (build-sell-grok-bots-2-hour-course.md)

Verdict [M]: good for phone-first inbox and social tasks, less organized than Claude Code or Codex for software. Who owns the product is unsettled; Cursor and xAI branding both appear. The "$80 in one day" bill belongs to Clawdbot, not Grok Bot.

## Hermes: free harness on a $6 host, ChatGPT login
`[T] · [D] · uploaded 2026-05-10; 2026-08-27 · hermes-agent-zero-to-personal-ai-assistant-1-hour-course.md; set-up-a-personal-hermes-in-14-mins-no-vps-or-mac-mini.md · q17, q38 · version-bound`

Nous Research's open-source agent, 140,000 GitHub stars when he filmed the course on 2026-05-10. It runs 24/7 on a VPS or Hostinger's managed Hermes app. He powers it with a ChatGPT subscription through the Codex login instead of an API key.

> the managed hermes is starting off at about six bucks a month (set-up-a-personal-hermes-in-14-mins-no-vps-or-mac-mini.md)

> use your chat gpt subscription because you're going to get way more inference it's going to be way cheaper (set-up-a-personal-hermes-in-14-mins-no-vps-or-mac-mini.md)

Role split he gives: Hermes is the always-on phone assistant, Claude Code the desk tool. The full Hermes build is in `build-hermes-assistant.md`.

## OpenClaw and Clawdbot: 900 exposed servers
`[T] · [D] · uploaded 2026-01-28 · 100-hours-testing-clawdbot-vs-claude-code-honest-results.md · q33, q38 · version-bound`

Clawdbot (later OpenClaw) is free and open source, hosted on a Hostinger KVM 2 for "six bucks a month n[ine] bucks a month". On 2026-01-28 he read out a security report:

> there were over 900 servers that have been exposed with no password protection leaking api keys and months of private chat history (100-hours-testing-clawdbot-vs-claude-code-honest-results.md)

He ran it on Telegram and paid about $80 for 8 million tokens in one day. By 2026-09-28 he refers to OpenClaw as an experiment he already ran. q38's "graduated" label is Gemini's word for that.

## Claude Code vs Clawdbot: the 8-metric scorecard
`[T] · [D] · uploaded 2026-01-28 · 100-hours-testing-clawdbot-vs-claude-code-honest-results.md · q14 · version-bound`

The rubric he used on 2026-01-28, reusable for any new harness:

> the categories that we're going to be looking at today are out of the box ability setup friction and risk cost power and access security everyday usability actual roi and the icp (100-hours-testing-clawdbot-vs-claude-code-honest-results.md)

Scores spoken on camera: out of the box, Claude Code 7, Clawdbot 9. Setup friction, Claude Code 8. Security, Claude Code 7, Clawdbot 3. Everyday usability, Claude Code 6, Clawdbot 9. ROI, Claude Code 8.5, Clawdbot 6, weighted higher. Final total 51.5 to 49. ICP got no number. Gemini's q14 relabelled all of this "Grok Bot vs Claude Code"; the product was Clawdbot.

## Cursor
`[T] · [M] · no transcript · q38 · version-bound`

[M] Gemini's version only; no caption carries this text. q38 lists Cursor Pro at $20 a month and says he moved to terminal harnesses. The only caption-backed Cursor fact is the Ultra plan that Grok Bot required on 2026-08-12.

## Owl and Rottweiler: which harness feels like what
`[J] · [D] · uploaded 2026-08-10; 2026-09-11 · build-sell-ai-saas-products-2-hour-course.md; how-to-actually-choose-the-right-ai-agent.md · q14, q15 · version-bound`

The owl is Claude Code, or Fable inside it. The Rottweiler is Codex. No model called Opus 4.8 is the owl, and "surgeon" has zero caption hits.

> it feels like it has more of that wise old owl sort of perspective whereas when i jump over here to codeex this thing feels like a rottweiler (build-sell-ai-saas-products-2-hour-course.md)

## Loyal to the harness and assets (speaker open)
`[J] · [D] · uploaded 2026-09-11 · how-to-actually-choose-the-right-ai-agent.md · q15 · stable`

> my number one goal is to never be loyal to a provider only be loyal to my harness and my assets and i will switch the brain interchangeably (how-to-actually-choose-the-right-ai-agent.md)

The line sits in the cold-open teaser of the Mark Kashef interview. Captions carry no speaker tags, so whether Nate or Mark says it is open. The "skills and context files" wording in q15 is Gemini's.

## Anthropic's third-party login rule
`[R] · [D] · uploaded 2026-05-26 · 100-hours-testing-claude-code-vs-chatgpt-codex-honest-results.md · q16, q33 · version-bound`

OpenAI lets a ChatGPT login drive Hermes, OpenClaw or Grok Bot. Anthropic does not allow a Claude subscription in those harnesses without approval, which is why his Hermes runs on Codex.

> using your cloud subscription inside of a third party tool like openclaw or hermes isn't allowed unless anthropic specifically approves you (100-hours-testing-claude-code-vs-chatgpt-codex-honest-results.md)
