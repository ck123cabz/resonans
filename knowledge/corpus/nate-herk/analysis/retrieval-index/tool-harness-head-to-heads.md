---
type: tool
aliases: ["Harness and model head-to-head tests"]
corpus: nate-herk
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-29
name: Harness and model head-to-head tests
speaker: Nate Herk
provenance: D
sources: [q14, q19, q34]
videos: [100-hours-testing-claude-code-vs-chatgpt-codex-honest-results.md, i-made-codex-and-claude-code-build-the-same-app-one-clearly-won.md, i-tested-claude-code-vs-codex-on-design-it-wasn-t-even-close.md, 100-hours-testing-claude-code-vs-antigravity-honest-results.md, 100-hours-testing-deepseek-harness-vs-claude-code-what-you-need-to-kno.md, 100-hours-testing-clawdbot-vs-claude-code-honest-results.md, i-battle-tested-sakana-fugu-s-fable-killer.md, i-tested-gpt-5-6-sol-vs-fable-5-what-you-need-to-know.md, i-tested-gpt-6-astra-vs-fable-5-1-on-15-real-use-cases.md]
---

# Harness and model head-to-head tests

Every side-by-side test Nate Herk ran with numbers, January to September 2026. Each result is dated by upload, because the models under the harnesses changed every few weeks. His method for judging a release (real tasks, time and dollars side by side, no vendor charts) is in `tool-models-and-prices.md`.

## Claude Code vs Codex: marketing dashboard, 283k vs 1.64M tokens
`[T] · [D][G] · uploaded 2026-05-26 · 100-hours-testing-claude-code-vs-chatgpt-codex-honest-results.md · q14 · version-bound`

One dashboard prompt in both harnesses. Claude Code took about 2 minutes, Codex about 8. Claude's version was dark-mode and polished; he called Codex's "cheaper" looking.

> claude used about 283,000 tokens total where codex used about 1.64 million so almost six times more tokens (100-hours-testing-claude-code-vs-chatgpt-codex-honest-results.md)

## Claude Code vs Codex: research PDF, Codex wins at 2.8M vs 4.7M
`[T] · [D][G] · uploaded 2026-05-26 · 100-hours-testing-claude-code-vs-chatgpt-codex-honest-results.md · q14 · version-bound`

A branded research report as a PDF. Codex produced cleaner spacing and tables, and both took about 8 minutes (8 minutes against 8 minutes 15 seconds).

> codeex used about 2.8 million tokens versus claude's 4.7 million (100-hours-testing-claude-code-vs-chatgpt-codex-honest-results.md)

## Codex writes 2 to 5x fewer output tokens
`[T] · [D] · uploaded 2026-05-26 · 100-hours-testing-claude-code-vs-chatgpt-codex-honest-results.md · q14 · version-bound`

> on every single build codex wrote about 2 to 5x fewer output tokens than claude (100-hours-testing-claude-code-vs-chatgpt-codex-honest-results.md)

This is output tokens per build. The dashboard's 1.64M is total tokens. The two figures measure different things in the same video, so they do not cancel. Later tests (below) cut against the 2 to 5x claim; see the last section.

## Claude Code vs Codex: Typeform clone, 5.5 hours vs 61.5 hours
`[T] · [D][G] · uploaded 2026-08-14 · i-made-codex-and-claude-code-build-the-same-app-one-clearly-won.md · q14 · version-bound`

A three-phase Typeform clone. Claude Code finished in 5.5 hours, Codex in 61.5. Codex over-built the back end and shipped a worse user experience. Codex wrote about 11.5M output tokens to Claude's 2M.

> claude code did this with one orchestrator 35 sub aents and about 2,800 tool calls whereas codex did this with one orchestrator 126 sub aents and 32.5k tool calls (i-made-codex-and-claude-code-build-the-same-app-one-clearly-won.md)

Cost: Codex about $3,000 API-equivalent. For Claude he first said about $832, then corrected himself on camera to "roughly $447 ... there was a mismatch somewhere". Cite both, and his own flag.

## Claude Code vs Codex: design test, $65 vs $20
`[T] · [D] · uploaded 2026-08-26 · i-tested-claude-code-vs-codex-on-design-it-wasn-t-even-close.md · q34 · version-bound`

> took an hour and 12 minutes whereas cloud code took two and a half hours it only cost 100,000 tokens and 20 bucks (i-tested-claude-code-vs-codex-on-design-it-wasn-t-even-close.md)

Codex: 1 hour 12 minutes, 100,000 tokens, $20. Claude Code: 2.5 hours, about 500,000 tokens, $65.

## Claude Code vs Antigravity: three builds and SWE-bench
`[T] · [D] · uploaded 2026-04-13 · 100-hours-testing-claude-code-vs-antigravity-honest-results.md · q14 · version-bound`

Claude Code on Opus 4.6 and 4.7, Antigravity on Gemini 3 Pro and 3.1 Pro. Habit tracker: Antigravity faster and prettier, Claude richer logic with streak tracking. Plan-mode research report: Claude won with styled tables and cited sources; Antigravity cited none. Landing page: Antigravity more visual, Claude better copy and structure.

The SWE-bench scores are published numbers he read out, not his test:

> claude opus 4.6 inside of cloud code scored an 80.9% gemini 3 pro inside of anti-gravity came in at around 76.2% (100-hours-testing-claude-code-vs-antigravity-honest-results.md)

## Claude Code vs DeepSeek harness: 50 seconds vs 5 minutes
`[T] · [D][G] · uploaded 2026-08-23 · 100-hours-testing-deepseek-harness-vs-claude-code-what-you-need-to-kno.md · q14 · version-bound`

Local wiki search: DeepSeek found a transcript and summarized it in about 50 seconds; Claude Code took over 5 minutes. Formatted Excel sheet:

> this one came back in about 3 minutes whereas the other one from cloud code took i think it was 17 minutes (100-hours-testing-deepseek-harness-vs-claude-code-what-you-need-to-kno.md)

DeepSeek V4 has no vision, so its UI output had overlapping text that Claude's screenshot loop would catch. q14's STORM report counts (Claude 5,000 words and 26 sources, DeepSeek 4,400 and 14) are [M]; the source counts were not found in the captions.

## Claude Code vs Clawdbot: 51.5 to 49
`[T] · [D] · uploaded 2026-01-28 · 100-hours-testing-clawdbot-vs-claude-code-honest-results.md · q14 · version-bound`

Scored on eight metrics; the rubric and per-metric scores are in `tool-harnesses.md`. Totals he spoke: Claude Code 51.5, Clawdbot 49. His Clawdbot bill on Telegram:

> my bill today with that 8 million tokens was about 80 bucks (100-hours-testing-clawdbot-vs-claude-code-honest-results.md)

Gemini's q14 filed this whole test under Grok Bot. It is Clawdbot.

## Sakana Fugu Ultra vs Opus 4.8: 36 ties in 38
`[T] · [D][G] · uploaded 2026-06-23 · i-battle-tested-sakana-fugu-s-fable-killer.md · q19, q34 · version-bound`

Marketed as a "Fable killer", tested inside Claude Code against Opus 4.8.

> we had 36 of the 38 tasks end in a tie we had fugu being 4.5 times slower overall and five times more expensive (i-battle-tested-sakana-fugu-s-fable-killer.md)

Wait time 357 minutes vs 80. Cost $50 vs $10. Opus won the other 2. Verdict: Fugu is a routing wrapper over frontier models; running Claude Code or Codex directly is faster and cheaper at equal quality. q15's line that he keeps Fugu for second-family checks was not found.

## GPT-5.6 Sol vs Fable 5: 24 to 3, $16 vs $63
`[T] · [D][G] · uploaded 2026-07-10 · i-tested-gpt-5-6-sol-vs-fable-5-what-you-need-to-know.md · q34 · version-bound`

27 quick one-off tasks. Fable also refused several.

> soul won 24 to3 for these kind of quick one-off tasks and soul costed 16 bucks while fable costed 63 bucks (i-tested-gpt-5-6-sol-vs-fable-5-what-you-need-to-know.md)

Timing example from the same video: Fable 23 minutes, Sol almost 7.

## GPT-6 Astra vs Fable 5.1: 10 of 15
`[T] · [D][G] · uploaded 2026-09-06 · i-tested-gpt-6-astra-vs-fable-5-1-on-15-real-use-cases.md · q34 · version-bound`

> astra won 10 of them and fable won five of them (i-tested-gpt-6-astra-vs-fable-5-1-on-15-real-use-cases.md)

Per-task costs only, such as $12 for Astra vs $26 for Fable on one run. q34's "45% faster and 38% cheaper overall" has no caption hit. Do not cite it.

## Open: which harness is token-lean
`[T] · [D] · uploaded 2026-05-26; 2026-08-14; 2026-08-26 · three files above · q14 · version-bound`

Contradiction B-C03 stays open. On 2026-05-26 Codex wrote 2 to 5x fewer output tokens. On 2026-08-14 Codex wrote about 11.5M output tokens to Claude's 2M on the Typeform clone. On 2026-08-26 Codex used 100,000 tokens to Claude's 500,000 on design. Per-test results go both ways, and model versions changed between each date.
