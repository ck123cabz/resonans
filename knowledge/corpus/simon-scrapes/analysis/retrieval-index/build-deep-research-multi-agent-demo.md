---
type: build
aliases: ["Deep research multi-agent demo (Ultra Code)"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: Deep research multi-agent demo (Ultra Code)
provenance: G
lanes: [5]
sources: [q30]
---

# Deep research multi-agent demo (Ultra Code)

Demonstrated Ultra Code run: deep research on Claude Code's latest desktop app features, executed as a fan-out-and-synthesize workflow with hard numbers attached.

## Pipeline
1. Fan-out: 5 initial "scout" agents deployed across sources — one news scout alone cost 45,000 tokens.
2. Deep read: 8 more agents spawned to read specific sources in depth.
3. Adversarial verification: a checker pass actively tried to break or disprove 12 key claims from the drafts.
4. Final synthesis into one report.

## Totals
13 minutes, 26 agents, 670,000 tokens for the complete run.

## When this shape applies
Ultra Code writes its own workflow harness and gives each sub-agent a clean context slate and a single job — use it where a single context window degrades (premature stopping, self-favoring verification, objective loss to context rot). Fan-out-and-synthesize is the right pattern for research across multiple sources; adversarial verification is the fact-checking layer.

## Cost lesson
The token totals are the point of the demo: multi-agent research is powerful and expensive. Budget accordingly, and force sub-agents onto a cheap model where the work allows (the corpus's settings advice: background workers on Haiku). Companion demo in the same session: the inbox skill builder (rubric agent, two parallel build agents, integration, adversarial review) that produced the newsletter digest skills.
