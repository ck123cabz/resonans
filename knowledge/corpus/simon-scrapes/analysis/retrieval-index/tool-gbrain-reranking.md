---
type: tool
aliases: ["GBrain reranking pattern"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: GBrain reranking pattern
provenance: M
lanes: [3]
sources: [q15, q19]
---

# GBrain reranking pattern

Gary Tan's pattern for the last step of a memory stack: instead of handing the agent raw retrieved chunks, add a reranker second pass that returns a written, cited answer.

## How it works
Vector-DB systems like MemSearch return the top 5-10 chunks and leave interpretation to the agent. GBrain layers a second pass on top: it reranks the retrieved material, synthesizes a written answer with citations back to the source memories, and — the distinctive behavior — admits when it can't find the information rather than improvising.

## When to use
Decision-tree routing question 4: raw chunks vs synthesized answer. If you want the memory system itself to produce a finished, cited answer (and to say "not found" honestly), layer GBrain on top of a retrieval base. In Simon's map of fixes for Claude Code's native memory, the stack reads: MemSearch for semantic search over embedded transcripts, Mem Palace for zero-loss verbatim storage, GBrain on top for reranked, synthesized, cited answers.

## When to skip
If the consuming agent is happy interpreting top-k chunks itself (the MemSearch default), the extra pass is unnecessary machinery.
