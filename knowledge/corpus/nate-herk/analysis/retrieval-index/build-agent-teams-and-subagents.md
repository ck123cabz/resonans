---
type: build
aliases: ["Agent teams and subagents"]
corpus: nate-herk
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-29
name: Agent teams and subagents
speaker: Nate Herk
provenance: D
sources: [q05, q19]
videos: [how-to-build-claude-agent-teams-better-than-99-of-people.md, how-to-build-claude-subagents-better-than-99-of-people.md, claude-code-dynamic-workflows-clearly-explained.md, stanford-s-method-turns-claude-into-a-phd-level-research-team.md, finally-agent-loops-clearly-explained.md, claude-code-for-non-coders-6-hour-course.md, 5000-hours-of-building-ai-in-just-17-minutes.md]
---

# Agent teams and subagents

Nate's builds with more than one Claude Code agent, from the Neuroflow agent team on 2026-03-23 to the loops video on 2026-06-19. Subagents take one-way orders and return a summary. Agent teams message each other. Dynamic workflows fan out many subagents from code.

## Neuroflow: a three-teammate agent team
`[B] · [D][G] · uploaded 2026-03-23 · how-to-build-claude-agent-teams-better-than-99-of-people.md · q05 · version-bound`

He prompts Claude Code to create a team called Neuroflow with three Sonnet teammates: a front-end developer, a back-end developer and a QA agent. The prompt fires a tool called team create. Per q05 the QA agent files bug reports, the developers fix them, and the lead shuts the team down.

> create a team called Neuroflow of three teammates using sonnet the first one is a front-end developer the second one is a backend developer and the third one is a QA agent (how-to-build-claude-agent-teams-better-than-99-of-people.md)

## Turning agent teams on: the environment flag
`[T] · [D] · uploaded 2026-07-11 · claude-code-for-non-coders-6-hour-course.md · q05 · version-bound`

Agent teams were off by default when he recorded. He adds `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` to the project settings.

> you have to add this environment variable cloud code experimental agent teams equals 1 (claude-code-for-non-coders-6-hour-course.md)

## Team size: two to five, because cost scales per teammate
`[R] · [D] · uploaded 2026-03-23 · how-to-build-claude-agent-teams-better-than-99-of-people.md · q05 · stable`

Each teammate is a full session, so three teammates cost three times one session. His cap is two to five.

> if you have three sessions running that's basically going to be three times the cost so if you have five it'll be five times the cost which means I like to stay around maybe two to five agents max (how-to-build-claude-agent-teams-better-than-99-of-people.md)

Warning line: q05 speaks of swarms of 40 to 200 agents and a `max_turns=10` fix. No caption has 40 to 200. His own large runs are 41 and 210, below.

## Max turns on a subagent
`[T] · [D] · uploaded 2026-06-09 · how-to-build-claude-subagents-better-than-99-of-people.md · q05 · version-bound`

A subagent can carry a max-turns cap to stop research or review loops. He gives 10 as the example and says he rarely uses it.

> you can say "Hey max turns equals 10." Honestly I don't use this very often because most of my sub agent delegation is research or very specific workflows (how-to-build-claude-subagents-better-than-99-of-people.md)

## Graceful shutdown of a team
`[B] · [D] · uploaded 2026-03-23 · how-to-build-claude-agent-teams-better-than-99-of-people.md · q05 · version-bound`

When a researcher, strategist and critic team finished, the lead messaged each teammate to wrap up before closing.

> the main agent said "Cool let me shut down the teammates and finalize." (how-to-build-claude-agent-teams-better-than-99-of-people.md)

## AI trend hunter: a subagent with project memory
`[B] · [M] · uploaded 2026-06-09 · how-to-build-claude-subagents-better-than-99-of-people.md · q05 · version-bound`

He shows his project-level subagents: an AI trend hunter and a carousel planner, all on Sonnet, some with project memory. q05 gives the memory path `.claude/agent-memory/ai-trend-hunter.md` and says it runs web scans on Sonnet or Haiku. The path is Gemini's; the caption only says some agents "have different project memory".

> we could look at you know the AI trend hunter we can look at carousel planner you'll notice that some of these have different models like all of these are sonnet (how-to-build-claude-subagents-better-than-99-of-people.md)

## storm-research: five expert lenses in parallel
`[B] · [D] · uploaded 2026-06-29 · stanford-s-method-turns-claude-into-a-phd-level-research-team.md · q04, q05 · stable`

A skill built on Stanford's STORM method. Five agents each take one angle, and the report merges them. The method is Stanford's; the skill build is his.

> Storm utilizes these five perspectives we've got a practitioner an academic a skeptic an economist and a historian and each angle finds a hole that the other angles miss (stanford-s-method-turns-claude-into-a-phd-level-research-team.md)

## Dynamic workflow: 41 Haiku scorers and one Opus synthesis
`[B] · [D][G] · uploaded 2026-05-30 · claude-code-dynamic-workflows-clearly-explained.md · q19 · version-bound`

He ran a dynamic workflow over his own skill library. It spun up one Haiku scoring agent per skill, 41 in all, and fed the scores to an Opus synthesis agent. In the subagents video he adds that a test run once spun up about 210 subagents.

> it spun up 41 Haiku scoring agents because I have 41 skills here and then it's feeding all of that analysis into an opus synthesis agent (claude-code-dynamic-workflows-clearly-explained.md)

His rule for keeping the fan-out cheap:

> bound the scope name the deliverable and then all your sub aents can be put on haiku (claude-code-dynamic-workflows-clearly-explained.md)

## Four fleet models
`[F] · [M] · no transcript quote · q19 · stable`

q19 sorts his multi-agent setups into four models. (1) Subagents: one-way, fresh context, return a summary, cannot talk to each other. (2) Agent teams: a lead plus teammates with a shared task list and peer messages. (3) Dynamic workflows: code fans out parallel subagents, as in the 41-agent run. (4) Fusion routers such as Sakana Fugu Ultra, one API routing across model families. The four-part taxonomy is Gemini's arrangement. His Fugu test (36 of 38 ties, 4.5 times slower, $50 vs $10) is in `tool-harness-head-to-heads.md`.

## Width vs depth: fan-out vs /goal
`[J] · [M] · no transcript quote · q19 · stable`

q19 says workflows go wide across many small tasks and `/goal` loops go deep on one problem until a stop condition passes. No caption states the pair this way.

## Worker vs judge: goal plus verification
`[F] · [D] · uploaded 2026-06-19 · finally-agent-loops-clearly-explained.md · q19 · stable`

His two pillars of a loop are a goal and a way to verify it. Reason-act-observe is how "some people" describe loops; it is not his framing. q19's rule that the worker never declares itself done, and an independent test suite judges each turn, is Gemini's summary of this.

> there's really two most important pillars of that in my mind which are the goal what is the actual objective something typically that's objective not subjective and then verification (finally-agent-loops-clearly-explained.md)

## Five guardrails for fleets
`[R] · [D] for 1 and 3; [M] for 2, 4 and 5 · uploaded 2026-08-04 · 5000-hours-of-building-ai-in-just-17-minutes.md · q19 · stable`

q19's five, with the numbers the captions support:
1. Fix the access, not the prompt. Remove the tool or scope the key.
2. File territory: each agent owns its files, or runs in its own git worktree. [M]
3. Caps: max turns (10 is his example) and a team of two to five.
4. Graceful shutdown: the lead tells teammates to save state before closing.
5. A human approves money, deletions and mass sends. [M]

> if the answer scares you then fix the access not the prompt (5000-hours-of-building-ai-in-just-17-minutes.md)

The incident behind rule 1 is his own team's agent emailing a discount code to "about 150,000 people" on their list (5000-hours video; one later video says "almost 200,000", still open). Pass 1's "200,000 leads" is wrong on both counts.

## Where to look
- Teams: how-to-build-claude-agent-teams-better-than-99-of-people.md (2026-03-23)
- Subagents, max turns, roast subagent: how-to-build-claude-subagents-better-than-99-of-people.md (2026-06-09)
- Dynamic workflows: claude-code-dynamic-workflows-clearly-explained.md (2026-05-30)
- Loops: finally-agent-loops-clearly-explained.md (2026-06-19)
