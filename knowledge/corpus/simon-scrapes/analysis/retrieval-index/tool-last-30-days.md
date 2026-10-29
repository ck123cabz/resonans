---
type: tool
aliases: ["Last 30 Days"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: Last 30 Days
provenance: M
lanes: [2]
sources: [q13]
---

# Last 30 Days

Research skill by Ronny Nutrition that scans X and Reddit for discussions over the last 30 days and synthesizes the trending patterns into a research deliverable.

## Setup
Add OpenAI and X API keys, then run `/last 30 days [topic]`. Install commands in the source file are phonetic transcript renderings — command/key name garbled in transcript — verify against the tool's real docs before use.

## When to use
Two cases: trending-topic research for content angles, and as a workaround for Claude's paywall and site blocks — Claude Code is often blocked from fetching Reddit and X directly, and this skill routes around that. (The other workaround in the corpus is the Gemini CLI fallback skill.)

## Verdict
"30 days of research in 30 seconds" — Simon calls it a complete gamechanger for trend research. Feeds naturally into the trending-research step of the content pipelines (repurposing engine, social content creator).
