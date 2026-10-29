---
type: tool
aliases: ["Ralph Loop"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: Ralph Loop
provenance: M
lanes: [2, 5]
sources: [q13, q30, q31]
---

# Ralph Loop

Open-source headless autonomous loop: a plugin built from just three files, including a headless bash script whose while-loop feeds the exact same prompt back into Claude every iteration until done.

## How it works
- State carries through edited files, not conversation history — each iteration gets a fresh prompt plus the updated files, saving massive tokens versus dragging the whole transcript along.
- The loop breaks on exactly two conditions: the predefined "done" completion state, or a maximum iteration count.
- Mechanically the same as the loop-until-done multi-agent pattern from Anthropic's docs.

## Setup
Clone the Ralph Code GitHub repo or `/plugin install`. `Ralph enable` (or `Ralph setup my project`) scaffolds prompt.md, a fix plan, and a specs file. Write a `prd.json` with user stories and exact acceptance criteria defining done. Trigger with `/Ralph loop`. The plugin name is rendered phonetically in the transcript ("raw" for Ralph) — command/key name garbled in transcript — verify against the tool's real docs before use.

## When to use
Well-defined batch tasks with easily verifiable output and tight guardrails: six LinkedIn posts with strict rules and acceptance criteria, rule-based codebase refactoring, overnight content pipelines. Users ship whole projects overnight with it.

## Risks
Always set a max iteration count before running — relying on the done condition alone means a stuck bug loops indefinitely and burns tokens without bound. Vague acceptance criteria or poor inputs make the model veer completely off course and build the wrong thing; the no-oversight strength is the risk.

## Vs /loop + /goal
That pair schedules against a time interval and stops when the interval's goal is met. Ralph is an immediate continuous cycle that hammers one intensive build to completion in a single sitting.
