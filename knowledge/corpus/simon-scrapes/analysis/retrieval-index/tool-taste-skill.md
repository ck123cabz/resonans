---
type: tool
aliases: ["Taste skill"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: Taste skill
provenance: M
lanes: [2, 6]
sources: [q13, q36]
---

# Taste skill

Design skill by Leon that improves how AI writes front-end code: applies named aesthetics (brutalist, minimalist) and strips forbidden "AI tell" patterns.

## How it works
- Carries a "forbidden patterns"/"AI tells" list that explicitly bans the Inter font, Roboto, generic gradients, and the color teal.
- Its `redesign` sub-skill is the final 10% polish: fixes weak hierarchy and spacing, introduces natural inconsistencies (varied font weights), and swaps out stock AI layouts like zigzag reverse patterns and traditional accordions for more modern components.
- Without guardrails like this, Claude defaults to recognizable styling tells — cream and off-white backgrounds among them (version-bound).

## Setup
Install via `npx skills add` (the transcript renders it as "npx skills add the taste skill"). Run the redesign on a specific file: "reformat using the brutalist skill on this landing page.html". Command/key name garbled in transcript — verify against the tool's real docs before use.

## When to use
When a project or UI already exists and needs the last 10% of design polish — fixing weak layouts and removing generic AI aesthetics. In the landing-page build it runs as the final filter after Claude Design has produced a token-constrained page.

## Verdict
Good for applying specific aesthetic styles, but it struggles with elements like logos and images; sometimes stock Claude Design output is preferred.
