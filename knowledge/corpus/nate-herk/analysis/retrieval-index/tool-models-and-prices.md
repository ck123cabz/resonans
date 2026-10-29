---
type: tool
aliases: ["Models and prices"]
corpus: nate-herk
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-29
name: Models and prices
speaker: Nate Herk
provenance: D
sources: [q15, q16, q34, q38]
videos: [claude-code-for-non-coders-6-hour-course.md, how-anthropic-engineers-actually-prompt-fable-5.md, build-sell-with-codex-5-hour-course.md, glm-5-2-in-claude-code-is-blowing-my-mind.md, i-tested-jev-on-12-real-use-cases-my-honest-thoughts.md, ollama-claude-code-99-cheaper.md, claude-just-told-us-to-stop-using-their-best-model.md, claude-opus-4-7-just-dropped-or-did-it-really.md, opus-4-8-just-dropped-here-s-how-to-actually-use-it.md, fable-5-1-just-dropped-it-looks-unreal.md, gpt-6-astra-finally-kills-ai-website-slop.md, claude-fable-5-made-this-entire-video-by-itself.md, build-sell-with-claude-code-10-hour-course.md, claude-just-solved-session-limits.md, how-to-build-codex-skills-better-than-99-of-people.md]
---

# Models and prices

Per-token prices Nate Herk states on camera, which model he gives which job, and the release dates that video titles fix. Everything here is version-bound: prices and rankings moved every month from April to September 2026. Head-to-head results are in `tool-harness-head-to-heads.md`.

## Anthropic prices: Haiku, Sonnet, Opus, Fable
`[T] · [D] · uploaded 2026-07-11; 2026-07-01 · claude-code-for-non-coders-6-hour-course.md; how-anthropic-engineers-actually-prompt-fable-5.md · q15 · version-bound`

Per million tokens, input then output: Haiku $1 / $5, Sonnet $3 / $15, Opus $5 / $25, Fable $10 / $50.

> it's $1 for a million input tokens and it's $5 for a million output tokens sonnet 5 is $3 for a million input tokens and $15 for a million output (claude-code-for-non-coders-6-hour-course.md)

> it costs double opus at $10 per million input tokens and $50 per million output tokens (how-anthropic-engineers-actually-prompt-fable-5.md)

Opus at $5 / $25 is also spoken in claude-just-told-us-to-stop-using-their-best-model.md (2026-04-09).

## OpenAI prices: Astra stated, Sol, Terra and Luna not
`[T] · [D] · uploaded 2026-09-21 · build-sell-with-codex-5-hour-course.md · q15, q16 · version-bound`

> on astra for every 1 million input tokens it will cost you $10 and for every 1 million output tokens it will cost you 50 bucks (build-sell-with-codex-5-hour-course.md)

No caption gives a per-token price for GPT-5.6 Sol, Terra or Luna. q15's "Sol $2 / $10, half the cost of Fable" is Gemini's; the only "half the cost" line is an Astra vs Fable run, $12 vs $26. Look up Sol pricing on OpenAI's page, not here.

## Subscriptions are worth more than their price
`[R] · [D] · uploaded 2026-08-10; 2026-09-21 · build-sell-ai-saas-products-2-hour-course.md; build-sell-with-codex-5-hour-course.md · q16 · version-bound`

He puts a $200 plan from either lab at "$8,000 to $14,000 of inference", and the Codex $200 plan at about $14,000. His reading: labs are subsidizing usage now and may raise prices later.

## GLM 5.2: $1.40 / $4.40 and three plans
`[T] · [D] · uploaded 2026-06-19 · glm-5-2-in-claude-code-is-blowing-my-mind.md · q15, q34 · version-bound`

A 753B open-weights model he routed into Claude Code. About five times cheaper than Opus on input.

> gm 5.2 is $1.40 40 cents on the input and $4.40 on the output so this is where i got the numbers where i said it's about five times cheaper (glm-5-2-in-claude-code-is-blowing-my-mind.md)

Plans: $16, $64 or $144 a month. What he claims for it is scoped to your workload, not to Opus's ability:

> you could probably handle 80% or more of your knowledge work with something like glm 5.2 (glm-5-2-in-claude-code-is-blowing-my-mind.md)

He adds that you need Opus for "maybe 10 to 20%" of the day's tasks. q34's "80% of Opus 4.8's capability" misreads this.

## Jev: a hosted decision classifier from TypeSafe
`[T] · [D] · uploaded 2026-09-19 · i-tested-jev-on-12-real-use-cases-my-honest-thoughts.md · q15 · version-bound`

Jev is TypeSafe's decision model, trained with RLCD:

> rlcd and you can see what that stands for is reinforcement learning for calibrated decisions and this is on typesafe's blog (i-tested-jev-on-12-real-use-cases-my-honest-thoughts.md)

It returns a decision as JSON, and he tested it on 12 use cases for speed and cost, including a Chrome extension that labels tweets. q15's table lists Jev next to Ollama as a local privacy option. That is wrong: Jev is hosted.

## Ollama and free local models
`[T] · [D] · uploaded 2026-04-04 · ollama-claude-code-99-cheaper.md · q15 · version-bound`

Two ways to run Claude Code for free: a local model through Ollama, or free models on OpenRouter. His analogy: Claude Code is the car, the model is the engine you swap.

> sometimes you do have to play around with the models to see if they can do the proper tool calling that cloud code or your car actually expects (ollama-claude-code-99-cheaper.md)

The video was prompted by Google's Gemma 4 release. q15's job list for local models (pre-summarizing files, log grepping, backup when limits hit) is [M].

## Model by job, and walking it down
`[J] · [D] · uploaded 2026-03-12; 2026-09-21 · build-sell-with-claude-code-10-hour-course.md; build-sell-with-codex-5-hour-course.md · q15 · version-bound`

In the 200k-window era he set Sonnet as the default:

> use sonic for 80% of work switch to opus for complex architecture decisions or tricky bugs (build-sell-with-claude-code-10-hour-course.md)

After Anthropic doubled limits on 2026-05-07 he told viewers who had pushed work down to Haiku or Sonnet only to save limits that they could "start to ... give yourself" more. By June, Fable 5 and Opus orchestrate while Sonnet and Haiku work under them. The method that picks the cheapest model per job is "walk it down": set quality on a top model, then step down the model list and the effort levels until quality drops. It has its own entry in `framework-other-named-methods.md`.

> when i say walk it down i mean walking it down the model list (build-sell-with-codex-5-hour-course.md)

## Advisor strategy: Opus advises a cheaper executor
`[J] · [D] · uploaded 2026-04-09 · claude-just-told-us-to-stop-using-their-best-model.md · q15 · version-bound`

Anthropic's pattern: Sonnet or Haiku executes and calls Opus only when it needs advisor-level help. The numbers he read are Anthropic's evaluation, not his:

> sonnet with opus as an adviser showed a 2.7 percentage point increase on the swe bench ... and it also reduced the cost per agentic task by almost 12% (claude-just-told-us-to-stop-using-their-best-model.md)

q15's "cuts cost 50% to 90%" has no caption source. Use 12%.

## Release dates fixed by video titles
`[T] · [D] · uploaded 2026-04-16 to 2026-09-23 · titles in sources.tsv · q34 · version-bound`

Opus 4.7 video 2026-04-16. Opus 4.8 on 2026-05-28 ("it is may 28th 2026 and opus 4.8 has dropped"). Fable 5 on 2026-06-12, read from Anthropic's post as the first "mythos class model" on a paid plan. GPT-5.6 Sol on 2026-07-09. Fable 5.1 on 2026-09-01. GPT-6 Astra on 2026-09-03. Opus 5.5 on 2026-09-23.

## Opus 4.6 lost 73% of its thinking depth
`[T] · [D] · uploaded 2026-04-16 · claude-opus-4-7-just-dropped-or-did-it-really.md · q34 · version-bound`

> a senior director at amd published an analysis of almost 7,000 coding sessions using claude code she found that the thinking depth collapsed 73% (claude-opus-4-7-just-dropped-or-did-it-really.md)

Reasoning fell from about 2,200 characters to 600 after Anthropic lowered the default effort to medium. The same video warns Opus 4.7's new tokenizer means "the same input might actually cost you more just like 1 to 1.3" times.

## Fable 5.1: vendor claims, and the design crown that went to Astra
`[T] · [D] · uploaded 2026-09-01; 2026-09-04 · fable-5-1-just-dropped-it-looks-unreal.md; gpt-6-astra-finally-kills-ai-website-slop.md · q34 · version-bound`

He read two claims off Anthropic's launch material: Fable 5.1 on low effort beats Fable 5 on max, at an estimated 25% less. Both are vendor claims, not his test.

> fable 5.1 on low is better than the strongest fable 5 on max or high or x high (fable-5-1-just-dropped-it-looks-unreal.md)

Three days later he gave the design title to a different model:

> we have a new ai design king and it's not even close take a look at some of these outputs i've been getting with astra (gpt-6-astra-finally-kills-ai-website-slop.md)

q34's "Fable 5.1 is the design king" and "Fable burns 10x tokens" have no caption support.

## Fugu Ultra pricing
`[T] · [M] · uploaded 2026-06-23 · i-battle-tested-sakana-fugu-s-fable-killer.md · q38 · version-bound`

[M] Gemini's version only; no caption carries this text. q38 lists Fugu at $100 to $200 a month or API. His test cost $50 against Opus's $10 for the same 38 tasks (verified; see `tool-harness-head-to-heads.md`). Verdict: not worth it.
