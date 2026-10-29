---
type: build
aliases: ["Landing page from an extracted design system"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: Landing page from an extracted design system
provenance: M
lanes: [6]
sources: [q36]
---

# Landing page from an extracted design system

Build that produces a responsive landing page avoiding the generic AI look, by feeding Claude Design a real site's extracted design system and constraining it with hard tokens.

## Pipeline
1. Extract: run Skill UI against a target site (the demo emulates stackai.com). Ultra mode uses Playwright to crawl the URL, capturing scroll behaviors, hover interactions, component layouts, and animations. Output folder: `skill.md`, `colors.json`, `spacing.json`. Skill UI's install/run commands are phonetic in the source — command/key name garbled in transcript — verify against the tool's real docs before use.
2. Constrain: the design tokens act as hard guardrails — a `tokens.json` plus `design.md` defining typography rules, spacing, CSS variable tokens, and color palettes. Forcing Claude Design to abide by them removes random visual variability between generations.
3. Generate: Claude Design builds the page against the extracted system.
4. Polish: pass the result through the Taste skill's brutalist/minimalist filters — the final 10%: fixes weak hierarchy and spacing, introduces natural inconsistencies (varied font weights), strips stock AI layouts (zigzag reverse patterns, traditional accordions), and bans the AI-tell defaults (Inter, Roboto, generic gradients, teal).

## Why the guardrails matter
Without them Claude defaults to recognizable styling tells — cream and off-white backgrounds among them. Codifying a single source of truth for the visual identity is what makes generations consistent instead of vibes-dependent.
