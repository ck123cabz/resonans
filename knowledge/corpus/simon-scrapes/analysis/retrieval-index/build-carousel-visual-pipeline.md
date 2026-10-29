---
type: build
aliases: ["Carousel visual pipeline (design-token flow)"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: Carousel visual pipeline (design-token flow)
provenance: M
lanes: [6]
sources: [q33, q36]
---

# Carousel visual pipeline (design-token flow)

The visual-consistency mechanics behind LinkedIn carousels: how brand identity flows from token files into every generated slide. (The full 18-skill orchestration is in build-social-content-creator; this chunk covers the design layer.)

## Token flow
1. The Visual Identity skill codifies the single source of truth: exact color palette, typography, logo placement, and design tokens.
2. The Template Builder generates hero, body, and call-to-action slide layouts from the visual identity plus reference materials.
3. Template phase: supply 3-5 screenshots of carousels you admire; the system extracts their layout and composition, strips the original content, and applies your own visual identity to produce custom hero/body/CTA templates.
4. At render time, the brand's exact colors, typography, and visual philosophy are fed to the image generator (Nano Banana Pro) for every single slide.

## The consistency-vs-attention balance
All 6-10 slides in a carousel share the same aesthetic and brand markers, while layout varies slide-to-slide to keep the viewer engaged — consistency from the tokens, variation from the templates.

## Isolation and gating
Image generation runs in a fully isolated sub-agent so heavy image scripts don't pollute the main conversation's context, and the human review gate sits before generation so no render spend goes to unapproved content.

## Finishing
Flat renders import into Canva Magic Layers, which converts them into editable layers for the final 5% manual polish (typos, text sizing, logo position) instead of token-expensive reprompting; Zernio's API then uploads and schedules the finished carousel.
