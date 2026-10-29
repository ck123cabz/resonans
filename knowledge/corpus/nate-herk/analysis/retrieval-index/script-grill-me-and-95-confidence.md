---
type: script
aliases: ["Grill Me and the 95% confidence prompt"]
corpus: nate-herk
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-29
name: Grill Me and the 95% confidence prompt
speaker: Nate Herk, relaying Matt Pocock (grill-me) and Sabrina (95% prompt)
provenance: D
sources: [q07, q39]
videos: [the-skill-that-10x-d-my-claude-code-projects.md, build-sell-with-claude-code-10-hour-course.md, 18-claude-code-token-hacks-in-18-minutes.md, how-to-never-hit-your-claude-session-limit-again.md, how-i-d-teach-a-10-year-old-to-build-agentic-workflows-claude-code.md, build-sell-with-codex-5-hour-course.md]
---

# Grill Me and the 95% confidence prompt

The planning prompts Nate uses before any build. Two are other people's words he reads out: Matt Pocock's grill-me prompt and Sabrina's 95% prompt. Two are his: the claude.md 95% rule and the rough-idea-to-PRD ask. He names Grill Me in 14 transcripts, 2026-06-04 to 2026-09-21.

## Grill Me: Matt Pocock's prompt, as Nate reads it
`[S] · [D] (Pocock's words) · uploaded 2026-06-04 · the-skill-that-10x-d-my-claude-code-projects.md · q07, q39 · stable`

He credits the skill to Matt Pocock (captions: "Matt PCO") and reads the whole prompt aloud. He calls it "four to five sentences". Verbatim caption:

> Interview me relentlessly about every aspect of this plan until we reach a shared understanding Walk down each branch of the design tree resolving dependencies between decisions one by one (the-skill-that-10x-d-my-claude-code-projects.md)

> For each question provide your recommended answer Ask questions one at a time If a question can be answered by exploring the codebase explore the codebase instead (the-skill-that-10x-d-my-claude-code-projects.md)

Punctuated for pasting:

```
Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree resolving dependencies between decisions one by one. For each question provide your recommended answer. Ask questions one at a time. If a question can be answered by exploring the codebase, explore the codebase instead.
```

His takeaway from its length:

> it makes you realize that a skill doesn't have to be super complicated automation (the-skill-that-10x-d-my-claude-code-projects.md)

In the Codex course (2026-09-21) he says his own version "was inspired by Matt PCO's Grill Me" and goes in the AIS OS kit.

## Nate's upgrade: checkpoint after every question
`[S] · [D] for the idea; [M] for the file path · uploaded 2026-06-04 · the-skill-that-10x-d-my-claude-code-projects.md · q07, q39 · stable`

The original skill held everything in the conversation. Grilling can run an hour or more, so he added a write-back after each answer to a knowledge doc.

> what I did is I worked in that whole element of checkpointing after every single question because originally the skill doesn't do that (the-skill-that-10x-d-my-claude-code-projects.md)

> it will write everything back to a knowledge dock and it will just keep going over this loop endlessly until the knowledge dock is good enough and there's no gaps or holes (the-skill-that-10x-d-my-claude-code-projects.md)

q07 names the file `/brainstorms/<topic>.md` with a running summary, locked decisions, Q&A log and open flags. The path and section names are Gemini's.

## The grill-me skill file as q39 gives it
`[S] · [M] · no transcript quote · q39 · stable`

[M] Gemini's version only; no caption carries this text.

```
---
name: grill-me
description: Relentlessly interviews the user about a plan, design, or business process until reaching 100% shared understanding. Use when planning a project, extracting domain context, or stress-testing a spec.
---

# Operational Steps
1. Create a capture file immediately at `./brainstorms/[topic]-discovery.md` so no context is lost during the session.
2. Interview the user relentlessly ONE question at a time about every aspect of their plan, target audience, technical stack, edge cases, and failure modes.
3. For every question asked, provide your own recommended answer so the user can simply confirm or tweak.
4. Walk down each branch of the decision tree, resolving dependencies between choices one by one.
5. Checkpoint every answer into `./brainstorms/[topic]-discovery.md` after every single turn.
6. Stop only when there are zero remaining ambiguities or open questions.
```

Steps 3 and 4 match Pocock's text. Step 5 matches Nate's spoken upgrade. The rest is Gemini's layout.

## Sabrina's 95% confidence prompt
`[S] · [D] (Sabrina's words) · uploaded 2026-03-12 · build-sell-with-claude-code-10-hour-course.md · q07, q39 · stable`

He ends a content-repurposing request with it and credits Sabrina, the student turned head of AI. The closing sentence is verbatim:

> "Ask me clarifying questions one at a time until you are 95% confident that you can complete the task successfully." And I kind of use this templated prompt from Sabrina (build-sell-with-claude-code-10-hour-course.md)

```
Ask me clarifying questions one at a time until you are 95% confident that you can complete the task successfully.
```

q39's longer wrapper ("Help me build out a new automation flow for [Describe workflow/goal]. Build this as a reusable skill.") is Gemini's framing around the verbatim sentence.

## The 95% rule for claude.md
`[S] · [D] · uploaded 2026-04-02 · 18-claude-code-token-hacks-in-18-minutes.md · q01, q39 · stable`

His own line, which he says goes into all his claude.md files when Claude helps him build. He names it "the 95% confidence rule" in the same video.

> do not make any changes until you have 95% confidence in what you need to build ask me follow-up questions until you reach that confidence level (18-claude-code-token-hacks-in-18-minutes.md)

```
Do not make any changes until you have 95% confidence in what you need to build. Ask me follow-up questions until you reach that confidence level.
```

The reason he gives: a wrong build has to be scrapped and redone, "a huge waste of time and tokens".

## Rough idea to PRD in plan mode
`[S] · [D] · uploaded 2026-02-07; 2026-03-12 · how-i-d-teach-a-10-year-old-to-build-agentic-workflows-claude-code.md; build-sell-with-claude-code-10-hour-course.md · q07 · stable`

Put the agent in plan mode, then hand it the rough idea. The same passage appears in both videos (the course reuses it).

> put the agent in plan mode and say something like "Hey here's a rough idea of what I want help me turn this into an actual solid PRD or project requirement doc (how-i-d-teach-a-10-year-old-to-build-agentic-workflows-claude-code.md)

q07's version is longer and [M]: "Put yourself in Plan Mode and act as a senior Product Manager... Do initial research, analyze potential technical bottlenecks, and ask me clarifying questions one at a time until we have a complete spec." The senior-PM role and the bottleneck line are not in the captions.

## Plan mode first: Boris Cherny's habit
`[J] · [D] · uploaded 2026-04-20 · how-to-never-hit-your-claude-session-limit-again.md · q07 · stable`

He relays that Boris Cherny, who created Claude Code (captions: "Churnney"), starts every session in plan mode, and says he does the same. His reason is tokens spent up front save corrections later.

> boris Churnney the creator of Claude Code starts every single session in plan mode i do the same thing (how-to-never-hit-your-claude-session-limit-again.md)

## Order of use
`[J] · [I] · no transcript quote · q07 · stable`

Across q07 the sequence is: plan mode, grill-me or the 95% line to pull out context, a PRD, then the roast council (`script-roast-council.md`), then build. No single video states all five steps in this order; treat the sequence as a pattern across videos.
