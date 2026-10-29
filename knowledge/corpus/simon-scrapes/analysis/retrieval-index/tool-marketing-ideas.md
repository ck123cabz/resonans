---
type: tool
aliases: ["Marketing Ideas"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: Marketing Ideas
provenance: M
lanes: [2]
sources: [q13]
---

# Marketing Ideas

Skill by Cory Haynes packaging 139 proven marketing approaches organized by category, for marketing and growth inspiration.

## Setup
Install via `npx skills add ... -skill marketing-ideas -local`. Command/key name garbled in transcript — verify against the tool's real docs before use.

## The mandatory refactor
It ships as one massive single file, so installing it as-is instantly bloats the context window — the exact mega-skill antipattern. It must be refactored with the Skill Creator (progressive disclosure: lean skill.md, detail pushed to references/) before use. Simon notes the same author's AI SEO skill requires the identical refactor.

## Verdict
Great content and business logic, bad packaging. Worth having once refactored; a context tax if installed raw. A concrete instance of the general rule that marketplace skills get refactored before they enter a curated 20-30 skill library.
