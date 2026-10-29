---
type: tool
aliases: ["Gemini CLI fallback"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: Gemini CLI fallback
provenance: M
lanes: [7]
sources: [q40]
---

# Gemini CLI fallback

A research workaround pattern: Claude Code is often blocked from fetching Reddit, X, and paywalled content, while the Gemini CLI has broader web access. Install Gemini CLI as the fallback fetcher.

## How it works
Write a dedicated fetch skill instructing Claude that when it's asked to pull from blocked sites, it should:
1. Start a teamwork session.
2. Pass the prompt to the Gemini CLI to fetch and summarize the target URLs.
3. Capture the results back into the Claude Code workflow.

## When to use
Whenever a research or scraping step hits Claude's site blocks — Reddit and X are the common cases in the content pipelines (trending research for the repurposing engine and social content creator). The alternative workaround in the corpus is the Last 30 Days skill, which reaches X and Reddit through their APIs (OpenAI and X API keys required) instead of through a second CLI.

## When to skip
For sites Claude fetches fine natively, the hand-off adds a hop and a summarization layer for no gain.
