---
type: build
aliases: ["Content Repurposing Engine"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: Content Repurposing Engine
provenance: M
lanes: [6]
sources: [q32]
---

# Content Repurposing Engine

One source in, platform-ready drafts out: a YouTube URL, raw transcript, blog post, podcast notes, or social post fans out to LinkedIn (posts/carousels), X (threads), and email newsletters, saved as .md files in `/drafts/date/platform/`.

## Pipeline
A chain of specialized modular skills, not one mega-skill:
1. Transcript extraction — word-level timestamps from a video URL.
2. Trending research — Reddit + X angles on the topic.
3. The orchestrating repurposer.
4. A humanizer editor — scans generated drafts and strips "AI slop": robotic transitions, forbidden words, em-dashes.

## Orchestrator SOP
Read the source without summarizing it back (token save), extract 3-5 strong standalone ideas, draft multiple variations per idea (e.g. two thread variants), route everything through the humanizer.

## Brand voice via progressive disclosure
The skill reads a central "business brain" folder (voice profile, positioning, ICP, best past content) and loads `platform-formatting.md` (character limits, hook structures, spacing) only while drafting that platform, offloading it before the next one to prevent context rot.

## Triggers
Three modes: explicit slash command with a file argument (`/repurpose transcript.txt`); natural-language invocation matched via the skill's specific YAML description; or scheduled automation (cron: every Monday 9 a.m., check YouTube for new videos, grab the transcript, run the skill).

## Guardrail
Nothing auto-posts. Drafts land in the local folder and a human reviews, selects, and publishes.
