---
type: tool
aliases: ["Skill UI"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: Skill UI
provenance: M
lanes: [2, 6]
sources: [q13, q36]
---

# Skill UI

Open-source CLI that reverse-engineers any live website's design system — colors, typography, spacing, scroll journeys — into a Claude-ready skill folder.

## How it works
- "Ultra mode" uses Playwright to crawl the target URL, capturing scroll behaviors, hover interactions, component layouts, and animations.
- Output is a dedicated folder containing `skill.md` plus `colors.json` and `spacing.json`.
- Claude then reads that folder to emulate the scraped site's layout and design patterns when generating new interfaces.

## Setup
Needs an npm global install plus Playwright and Chromium. Run: `skill UI -URL [website.com] mode ultra`. The transcript renders the name phonetically ("scale UI") — command/key name garbled in transcript — verify against the tool's real docs before use.

## When to use
When you want to emulate an existing site's design system as hard input to Claude Design instead of prompting visuals vaguely — the landing-page build feeds Claude a Skill UI extraction of stackai.com and forces it to abide by the tokens. Pairs with the Taste skill, which handles the final polish after generation.

## Verdict
Highly impressive out of the box and effective at avoiding the generic AI look; still requires some manual iteration to perfect.
