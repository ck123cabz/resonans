---
type: tool
aliases: ["Computer use"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: Computer use
provenance: M
lanes: [7]
sources: [q40]
---

# Computer use

Anthropic feature in research preview for Mac users on Pro and Max plans: Claude physically controls the machine — pointing, clicking, navigating browsers, and filling out spreadsheets.

## When to use
The play for legacy enterprise applications with no API. It is slower than direct API integrations, so it's the fallback tier, not the default: if an MCP, CLI, or API path exists, use that instead.

## Worked example
Simon's demo: automatically open a browser, navigate to a private school community, screenshot member posts from the last 24 hours, read them from the screenshots, and generate a prioritized list of who needs help — a workflow impossible via API because the community platform has none.

## Constraints
Mac only, research preview, Pro/Max plans (version-bound — availability and platform support likely to have changed since recording).
