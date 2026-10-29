---
type: framework
aliases: ["6-step skill method and the bike method"]
corpus: nate-herk
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-29
name: 6-step skill method and the bike method
speaker: Nate Herk
provenance: D
sources: [q04, q16, q37, q50]
videos: [master-95-of-claude-code-skills-in-28-minutes.md, build-sell-claude-code-operating-systems-2-hour-course.md, how-to-build-codex-skills-better-than-99-of-people.md, claude-video-editing-just-became-unrecognizable.md, build-sell-grok-bots-2-hour-course.md, claude-code-skills-just-got-even-better.md, agentic-workflows-just-changed-ai-automation-forever-claude-code.md]
---

# 6-step skill method and the bike method

Nate Herk's recipe for writing a `skill.md`. He first teaches it on 2026-02-27 as "the six-step skill building framework" and repeats it in the AIOS course (2026-05-01). Step 6 is the bike method, an analogy he uses in 5 files through 2026-09-21. On 2026-09-19 he teaches a different six-item list for Codex skills.

## The six steps, Claude Code version
`[F] · [D] · uploaded 2026-02-27; 2026-05-01 · master-95-of-claude-code-skills-in-28-minutes.md; build-sell-claude-code-operating-systems-2-hour-course.md · q04, q37, q50 · stable`

1. Name and trigger.
2. Goal: in one sentence, what the skill produces.
3. Step-by-step process: what you do by hand, in what order, with which decisions.
4. Reference files: images, current projects, priorities, style guides.
5. Rules: what could go wrong, turned into guardrails.
6. Self-improvement loop.

> the six-step skill building framework so number one is the name and the trigger (master-95-of-claude-code-skills-in-28-minutes.md)

> number three is the actual meat of it that's the step-by-step process if you had to do something manually exactly what do you do in what order what do you look at and what decisions do you make (master-95-of-claude-code-skills-in-28-minutes.md)

> number five is the rules think about what could go wrong and then the agent can help you build in guardrails and constraints around that (master-95-of-claude-code-skills-in-28-minutes.md)

## Skill size: 500-line ceiling, 1,000 to 2,000 token body
`[R] · [D] · uploaded 2026-02-27 · master-95-of-claude-code-skills-in-28-minutes.md · q04 · version-bound`

He quotes the Claude Code docs for a ceiling of 500 lines on `skill.md`. Separately he estimates a typical skill body at 1,000 to 2,000 tokens, and the front matter at about 100 tokens. Pass 2 (A-C09) resolved these as a ceiling and a typical size.

> keep the skill.md under 500 lines (master-95-of-claude-code-skills-in-28-minutes.md)

> that might be anywhere from a thousand to a couple thousand tokens (master-95-of-claude-code-skills-in-28-minutes.md)

## Reference files: option A nested, option B alongside
`[F] · [D] · uploaded 2026-02-27 · master-95-of-claude-code-skills-in-28-minutes.md · q04 · stable`

He teaches two layouts for step 4. Option A keeps references and scripts inside the skill's folder. Option B keeps them elsewhere in the project, not nested under the skill, with his `.claude/skill/infographic` example.

> first option is to have it self-contained ... or option b is that they're not directly nested right under that skill (master-95-of-claude-code-skills-in-28-minutes.md)

## Codex version: six items, reverse-engineer first
`[F] · [D] · uploaded 2026-09-19 · how-to-build-codex-skills-better-than-99-of-people.md · q16 · stable`

His Codex skills video (2026-09-19) teaches a different list: 1 reverse engineer, 2 one specific job and one specific trigger, 3 freedom level, 4 verification, 5 walk it down, 6 the bike method. Reverse engineering means starting from the output, the definition of done, then turning a manual run into a skill. Freedom level asks whether the job is deterministic or not. He calls verification "probably the most important piece". Walk it down means testing cheaper models once quality is set (see `framework-other-named-methods.md`). Pass 1's Codex list (B036) is Gemini's paraphrase; this caption order replaces it.

> the whole idea with reverse engineering your skills is basically that you want to start with an output you want to start with what is the definition of done (how-to-build-codex-skills-better-than-99-of-people.md)

> number three we have thinking about the freedom level (how-to-build-codex-skills-better-than-99-of-people.md)

> number four we have verification and this is probably the most important piece of building skills (how-to-build-codex-skills-better-than-99-of-people.md)

## The bike method: your skill is never done
`[F] · [D] · uploaded 2026-04-23 to 2026-09-21 · how-to-build-codex-skills-better-than-99-of-people.md; build-sell-grok-bots-2-hour-course.md · q04, q37 · stable`

Step 6 in both lists. Every run, say what you liked and what you didn't, and have the agent update the skill. The picture is teaching a kid to ride: hand on the handlebars, then let go by degrees. He applies it to prompts, skills and automations alike. Files: 2026-04-23, 2026-05-29, 2026-08-31, 2026-09-19, 2026-09-21.

> we have the bike method which is ... just the idea to me that your skill is never done every single time you run the skill you're going to improve it (how-to-build-codex-skills-better-than-99-of-people.md)

> the feedback loop which i actually call this um riding the bike or the bike method (build-sell-grok-bots-2-hour-course.md)

## Bike to motorcycle: a separate analogy
`[J] · [D] · uploaded 2026-01-25 · agentic-workflows-just-changed-ai-automation-forever-claude-code.md · q47 · stable`

On 2026-01-25 he compares tools. n8n taught balance, steering and pedalling; Claude Code is the motorcycle. There are no training wheels in it; those belong to the bike method. He adds that n8n "wasn't a detour".

> learning to ride a bike i've got balance i know how to steer i know how to pedal but now we're going to be hopping on to like a motorcycle where we don't have to pedal (agentic-workflows-just-changed-ai-automation-forever-claude-code.md)

## Anthropic's two skill types: capability uplift, encoded preference
`[F] · [D] · uploaded 2026-03-05 · claude-code-skills-just-got-even-better.md · q04 · stable`

He reads this split from Anthropic, not his own. A capability uplift skill teaches Claude to do something better, like front-end design. An encoded preference skill holds steps Claude already knows but must run in a set order, closer to a workflow.

> there are two different types of skills we have a capability uplift skill which basically is a prompt so it teaches claude how to do something better (claude-code-skills-just-got-even-better.md)

> we also have encoded preference skills which means that claude already understands each of these pieces but it needs to follow them in a specific order (claude-code-skills-just-got-even-better.md)

## Warnings
`[A] · [M] · no transcript · q50 · stable`

- q50's step-6 quote ("update the skill manifest") is a paraphrase.
- TDD for skills (failing test first) is the Superpowers plugin's method, which he reads out on 2026-04-12. See `framework-borrowed-and-guest.md`.
