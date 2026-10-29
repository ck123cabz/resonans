---
type: framework
aliases: ["WAT framework"]
corpus: nate-herk
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-29
name: WAT framework
speaker: Nate Herk
provenance: D
sources: [q03, q37, q43, q50]
videos: [master-95-of-claude-code-in-36-mins-as-a-beginner.md, agentic-workflows-just-changed-ai-automation-forever-claude-code.md, build-sell-with-claude-code-10-hour-course.md, how-i-d-teach-a-10-year-old-to-build-agentic-workflows-claude-code.md, from-zero-to-your-first-agentic-ai-workflow-in-26-minutes-claude-code.md]
---

# WAT framework

WAT stands for Workflows, Agent, Tools. Nate Herk uses it to build agentic workflows in Claude Code. It first appears on 2026-01-21 and runs through 15 transcripts to 2026-07-11. It is the flagship of his Claude Code era, the stretch from 2026-01-14 to 2026-04-30.

## WAT: the three layers and what each holds
`[F] · [D] · uploaded 2026-01-25; 2026-03-12 · agentic-workflows-just-changed-ai-automation-forever-claude-code.md; build-sell-with-claude-code-10-hour-course.md · q03, q50 · stable`

Workflows are markdown SOPs in a `/workflows/` folder. The agent is the model inside the harness; it reads the SOP, picks tools and passes data between them. Tools are single-purpose Python scripts in `/tools/`, with API keys loaded from a root `.env`. The claude.md file he drops into each project states the layers in one line.

> we're going to be using a framework called the wat framework which basically just stands for workflows agent and tools (agentic-workflows-just-changed-ai-automation-forever-claude-code.md)

> layer 1 is the instructions layer two is you layer three are the tools (build-sell-with-claude-code-10-hour-course.md)

The second line is the claude.md speaking to the agent, so "you" is the model. The same passage sits in from-zero-to-your-first-agentic-ai-workflow-in-26-minutes-claude-code.md (2026-02-23); the 10-hour course repeats that video, so the two count as one origin.

## WAT: why he separates reasoning from execution
`[F] · [D] · uploaded 2026-01-21 · master-95-of-claude-code-in-36-mins-as-a-beginner.md · q03, q43 · stable`

His reason is reliability. The model decides; scripts do the work the same way every run.

> this is a three-layer framework and it basically separates concerns so that the probabistic AI handles reasoning while deterministic code actually handles the execution (master-95-of-claude-code-in-36-mins-as-a-beginner.md)

## WAT: the 90% per step, 59% after five steps math
`[R] · [D] · uploaded 2026-02-07 · how-i-d-teach-a-10-year-old-to-build-agentic-workflows-claude-code.md · q03 · stable`

He justifies the split with compounding error. The line is inside the claude.md he hands out, and he reads it on camera.

> if each step is 90% accurate then you're down to 59% success after just five steps (how-i-d-teach-a-10-year-old-to-build-agentic-workflows-claude-code.md)

0.9 to the fifth power is 0.59, so the arithmetic holds.

## WAT: the chef, recipe and ingredients analogy
`[F] · [D] · uploaded 2026-03-12 · build-sell-with-claude-code-10-hour-course.md · q03 · stable`

The agent is the chef, a workflow is the recipe, the tools are the ingredients. A chef with no recipe writes one; a pile of ingredients with no order is useless.

> basically the agent is a chef and the chef needs to make a cake the chef is going to either read a pre-existing workflow which is a recipe to how to make the cake or the chef is going to build its own recipe (build-sell-with-claude-code-10-hour-course.md)

> the tools are all of the ingredients but without the structure of the workflow saying use tool one then tool 5 then tool 7 then tool 10 without the order and the structure the tools are useless (build-sell-with-claude-code-10-hour-course.md)

## WAT: self-healing while building, no agent once deployed
`[J] · [D] · uploaded 2026-01-25; 2026-03-12 · agentic-workflows-just-changed-ai-automation-forever-claude-code.md; build-sell-with-claude-code-10-hour-course.md · q03 · stable`

While he builds, the agent reads an error, fixes the script or the SOP, and tests again. He calls this self-healing and ranks it first among the things to understand. When the automation ships to a schedule or webhook, only the W and the T go to the cloud. The agent stays home, so each run costs no reasoning tokens and behaves the same way.

> once you deploy that workflow to run on its own on a schedule or triggered by a web hook or something like that that is when you're deploying the code you're deploying the tools not the actual agent itself (build-sell-with-claude-code-10-hour-course.md)

> we are basically deploying the W workflows and the T tools but not the A agent (build-sell-with-claude-code-10-hour-course.md)

Hosting targets for the deployed half (Modal, Trigger.dev, Cloud Routines) sit in `tool-hosting-and-scheduling.md`.

## WAT: rules of placement (claude.md, workflow, tool, .env)
`[F] · [M] · no transcript · q03 · stable`

[M] Gemini's table only; no caption lists these rules as a table. Project rules and the folder map go in `claude.md`. The SOP, inputs, outputs and edge cases go in `/workflows/<name>.md`. One action per script goes in `/tools/<action>.py`. Keys go in `.env` and nowhere else. The claude.md he reads out does say "look in your existing tools" first, then learn and adapt when things fail (build-sell-with-claude-code-10-hour-course.md, 2026-03-12).

## WAT builds he shows
`[B] · [D][G] · uploaded 2026-02-07; 2026-03-12 · how-i-d-teach-a-10-year-old-to-build-agentic-workflows-claude-code.md; build-sell-with-claude-code-10-hour-course.md · q03 · version-bound`

Two builds carry caption proof. The first scrapes remote job listings: he searched "social media" and got 622 jobs across 21 pages. It is a job scraper; Gemini's q03 calls it lead scraping, and pass 2 corrected that. The second is a YouTube weekly report with seven Python tools. A competitor-analysis report is [M] with no script names. Full detail sits in `build-wat-workflows.md`.

> list of remote jobs so I searched for social media there's 622 remote jobs (how-i-d-teach-a-10-year-old-to-build-agentic-workflows-claude-code.md)

## Warning: "Visual Agentic Workflow Framework" is not his name
`[F] · [M] · no transcript · q36, q50 · stable`

Gemini's q50 labels WAT the "Visual Agentic Workflow Framework". The phrase "visual agentic" has zero hits in 299 transcripts. His name is "the WAT framework". Use only that name.

## Where WAT went next
`[J] · [D] · uploaded 2026-01-25 · agentic-workflows-just-changed-ai-automation-forever-claude-code.md · q36 · stable`

WAT came in as the bridge out of n8n: he frames n8n as the bicycle and Claude Code as the motorcycle, and says "naden wasn't a detour" on 2026-01-25. From 2026-05-01 the AIOS and its 4 C's take over as the flagship (`framework-aios-and-4-cs.md`). Skills later fill the workflows slot; a skill file is the recipe in his 2026-05-01 course, so the chef analogy carries over.
