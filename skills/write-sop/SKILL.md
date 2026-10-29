---
name: write-sop
description: >
  Write an SOP that a person and an agent can both follow cold, to Christian's standard: from an
  immersion pack, one primed callout per pause point, a value-seen check on every step, a gate on
  every never-rule, and a runs log that says whether it has been tested. Triggers: "/write-sop",
  "write an SOP for <task>", "make this a procedure", "turn this into an SOP", "SOP for <task>".
---

# write-sop

**The procedure is a vault note, not this file:** `04-resources/sops/writing-an-sop.md`. Sai follows
that note by hand and an agent follows it through this skill, so the two can never drift (Christian,
20 Oct 2026). Read it first and follow it step by step. This file holds only what a person never
needs.

## Before the note's first pause point

- Check the task is not already covered: `grep -ril "<task words>" 04-resources/sops/`. Extend a near
  match, since two SOPs for one task drift apart.
- Decide the kind. A ladder method note (a project blocked at a rung) follows the ladder rule in
  `.claude/rules/project-ladders.md` and is `kind: method`. Everything else is `kind: field` and
  needs a pack.
- Find the pack: `ls knowledge/learning/`. If the field has none, stop and tell Christian, who
  decides whether to run `/immerse`. Do not write a field SOP without one.

## While following the note

- **Draft from a real run.** The second pause point needs the person who does the task. An agent
  never drafts from nothing: it drafts from a recording, a transcript, a session log, or a person
  walking through it in chat, and names the source in the Source callout.
- **Christian's own rules come first.** Where his memory or a project note states a rule for this
  task (in video work: never time-stretch the voice; blind-read a visual before recommending it),
  it goes in as a step or a never-rule, cited to where he said it.
- **Every Why cites.** A pack section, a named practitioner, or "my own rule, untested". A Why with
  no source does not ship.
- Lint the prose: `python3 scripts/ai_slop_lint.py <file>`, and fix every TIER1 and over-cap line.
- Check the structure: `.venv/bin/python scripts/sop_check.py <file>` must print no problem lines.

## The cold run

The agent never runs the cold test and never writes a Runs line for someone else. It hands the SOP to
Christian with the name of a follower who has never done the task, and records the Runs line only
from what Christian or the follower reports.

## Never

- Post, send or share the SOP outside the repo.
- Write into a note Christian wrote. A new SOP is a new file in `04-resources/sops/`.
- Mark an SOP tested. Tested is read from its Runs callout by `sop_check.py`.
