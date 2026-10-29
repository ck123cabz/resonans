---
type: build
aliases: ["Social Content Creator (18-skill system)"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: Social Content Creator (18-skill system)
provenance: M
lanes: [2, 6]
sources: [q10, q33]
---

# Social Content Creator (18-skill system)

Modular Claude Code skill chain that turns an idea (custom topic, YouTube URL, local audio file, or blog post) into a fully formatted, brand-consistent LinkedIn carousel plus post copy. Built from 18 distinct Lego-block skills; only ~8 are named in the corpus (full roster is a registered gap).

## Named components
- Input/scraping: LinkedIn feed scraping for inspiration; Trending Research skill scraping Reddit and X for viral discussions.
- Brand Voice skill: if no voice profile exists, quizzes you and extracts writing patterns from samples so post bodies sound like you.
- Visual Identity skill: codifies exact color palette, typography, logo placement, and design tokens for cross-slide consistency.
- Template Builder skill: dynamically generates slide layouts (hero, body, call-to-action) from the visual identity plus reference materials.
- Designer sub-agent as art director: audits the visual inventory (logos/photos), chooses a narrative arc, writes a slide-by-slide plan mapping text to visuals, including the post caption.
- Image generation in a fully isolated sub-agent (Nano Banana Pro / Gemini 3 Pro) so heavy image scripts don't pollute the main conversation's context.

## Pipeline order
Onboarding checks (build voice/identity if missing) → inspiration/research → designer planning → human review → isolated image generation → HTML mock-up preview of the post as it would appear in a LinkedIn feed.

The human review gate sits BEFORE image generation: slide plan and copy get approved first, so no render spend on content that isn't valuable.

## Visual style template phase
Supply 3-5 screenshots of carousels you admire; the system extracts their layout and composition, strips the original content, and applies your own visual identity to produce custom hero/body/CTA templates.

## Tail steps
Canva Magic Layers converts flat renders into editable layers for the final 5% manual polish; Zernio API uploads and schedules the finished carousel to LinkedIn.

## Reuse proof
The same visual identity and brand voice blocks detach and drive entirely different assets (formal slide decks) with no rewritten instructions.
