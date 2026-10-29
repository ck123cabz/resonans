---
type: tool
aliases: ["LLM Wiki pattern / Recall"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: LLM Wiki pattern / Recall
provenance: M
lanes: [2, 3]
sources: [q13, q15]
---

# LLM Wiki pattern / Recall

Two versions of the same idea: a living wiki where an LLM maintains an interconnected knowledge graph of your raw inputs (articles, videos, podcasts). One self-hosted pattern, one hosted product.

## LLM Wiki (Karpathy pattern)
A living-wiki pattern built in Obsidian where Claude manages an interconnected knowledge graph of raw inputs. Attributed in the source to "Andre Karpathy" — almost certainly a transcript garble of Andrej Karpathy. Use for deep research on interconnected topics and for connecting content you consume.

## Recall
Hosted browser-extension version of the LLM Wiki that auto-tags and summarizes saved content. Zero setup, good for non-technical users. Trade-off: the data lives rented on their servers rather than owned by you.

## When to use
Decision-tree routing question 6 — operationalizing memory vs consuming content. If the goal is connecting articles/videos/podcasts into a knowledge graph, use the LLM Wiki pattern (Obsidian) or Recall.

## When to skip
Neither is operational business memory. For decisions, client context, and session recall, route to MemSearch, Mem Palace, or Open Brain instead. Simon's verdict: better for research and content consumption than running a business.
