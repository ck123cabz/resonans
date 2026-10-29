---
type: tool
aliases: ["/rewind + checkpoints"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: /rewind + checkpoints
provenance: M
lanes: [4]
sources: [q23]
---

# /rewind + checkpoints

Claude Code's native rollback system, and the mechanism that makes the slot-machine principle executable: when output is bad, never manually correct — restart from a clean state ("pull the lever again").

## How it works
- Claude Code automatically takes a session-level snapshot of the codebase right before any file edit — checkpoints exist without setup.
- /rewind (or /re) opens a list of every prompt in the session. Select the clean checkpoint just before the mistake, then choose to roll back code only, conversation only, or both. Re-prompt with slightly more specific instructions and let it retry from the clean state.

## Why restart beats correction
Each fix forces Claude to hold the original broken code, the failed attempt, AND the correction in one window; corrections compound pollution, the model drifts further, and quality worsens the more you try to fix. As retold from Anthropic's data science team: save state, let Claude run autonomously 30 minutes, then a binary choice — accept the result or throw it away and start fresh, no middle path. Anthropic engineering (also retold) runs constant checkpoints for seconds-fast rollback; Claude nails a task on the first try only about a third of the time.

## The adoption blocker
The sunk-cost trap: invested session time makes restarting feel like waste, but a clean restart has a significantly higher success rate than arguing with an already-drifting model.

Note: the "treat Claude like a slot machine" phrase and Anthropic-practice claims are Simon's retelling, not first-hand.
