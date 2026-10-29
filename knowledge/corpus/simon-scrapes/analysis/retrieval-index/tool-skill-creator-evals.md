---
type: tool
aliases: ["Skill Creator / Skills 2.0 evals"]
corpus: simon-scrapes
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
name: Skill Creator / Skills 2.0 evals
provenance: M
lanes: [2]
sources: [q11, q13]
---

# Skill Creator / Skills 2.0 evals

Anthropic's meta-skill for creating, refactoring, and measuring skills, with adapted versions by Tash (Glitter Cowboy) and Simon. Enforces proper progressive disclosure: lean YAML frontmatter and skill.md, detailed instructions pushed to references/. Skills 2.0 adds structured evaluation — test, benchmark, and score skills against defined criteria instead of vibes-based judging.

## Eval mechanics
- Give it a task ("write landing page copy") plus explicit criteria ("does it use curiosity gaps", "does it include an author bio", "does it follow the persuasion toolkit reference file").
- It spawns parallel agents to run the skill multiple times (e.g. 5 runs) and grades with binary true/false assertions.
- Test only 1-3 criteria at a time so the evaluation isn't overwhelmed by moving parts.
- Output: a structured HTML report/dashboard — pass/fail per assertion across runs, execution time and exact token usage per run, and qualitative failure explanations ("the copy lacks genuine curiosity gaps").
- A/B testing: run the task 5x with a reference file and 5x without; compare scores, tokens, and time to prove whether the file improves quality or just wastes tokens and should be cut.

## Iteration workflow
Build v1.0 via skill-creator (description, tools, references, step process) → run eval on 1-3 criteria → review report → give failure-specific feedback ("place more emphasis on founder-led stories", "always check for internal links") → the system auto-edits skill.md and reruns → stop when the skill reliably hits 9 out of 10.

## Setup
`npx skills add anthropics/skills-skill-creator`, or the Glitter Cowboy variant via `npx skills add ... -local`. Command/key name garbled in transcript — verify against the tool's real docs before use.

## Verdict
Essential — never write skills from scratch. Also the mandatory refactor tool for bloated marketplace downloads (e.g. Marketing Ideas).
