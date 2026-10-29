---
name: immerse
description: >
  Build insider fluency in a field the way a person gets it by living inside the field's culture,
  done by AI and faster: its map and history, the same events read by every role, its words and
  rituals, its critical incidents and how they felt, its live fights, its judgment calls, and what
  text cannot give. Writes a seven-section immersion pack and keeps the run open until a real
  insider accepts something built from it. Every SOP is written from a pack. Triggers: "/immerse",
  "immerse in <field>", "immersion run", "build an immersion pack", "I lack immersion in <topic>",
  "before writing an SOP for <field>".
---

# immerse

Christian, 27 Jul 2026: "competence comes from immersing into the culture, norms, habits, routines
of the whole universe of the specific domain." On 15 Aug he added: "Don't presume the 'syllabus', it
will surface itself during the immersion process." This skill is that process. The design, with
every source cited, is `docs/superpowers/specs/2026-10-20-immersion-layer-design.md`; the sources are
`research/2026-10-20-immersion-expertise-sources.md`.

**The target is interactional expertise** (Collins and Evans 2007): talking the field's talk from
several of its roles, well enough that an insider accepts it. Doing the field's practice is out of
reach for an AI, so the pack hands that part to Christian by name.

## The rule that ends a run

A run is done when a real insider accepts something built from the pack. Machine checks run first,
and passing them does not finish the run. Christian set this on 20 Oct 2026. The record behind it:
on 29 Jul a writing note asked for a corpus, a lens and a wiki before one creator was named, and the
reading never met anyone. Whether a pack is done is read from `checks.md`, never from a field.

## Where a pack lives

`knowledge/learning/<field-slug>/`, beside the mathematics lore that was the first one
(`knowledge/learning/lore/mathematics.md`, 13 Aug). Raw sweeps go under `.raw/` so Obsidian never
indexes them (`.claude/rules/knowledge-corpus.md`). Section formats: `references/pack-format.md`.

```
knowledge/learning/<field-slug>/
  README.md     field, roles, judge, the order to read in
  map.md  roles.md  culture.md  incidents.md  fights.md  judgment.md  gaps.md
  checks.md     machine checks and the insider gate, appended as they happen
  .raw/         sweep outputs, one file per agent
```

## Steps

1. **Intake.** Write `README.md` with four facts: the field in one line, why now (the project or SOP
   it feeds), the roles to cover (at least a beginner, a pro, someone the field serves, a critic,
   someone who left), and the judge: a named person or a named community where an answer can be
   accepted. If no judge can be named, stop and ask Christian, since a run with no judge cannot finish.
2. **Sweep, in parallel.** One agent per section group, launched together, each writing to `.raw/`:
   - map and history: how the field formed and changed, crisis by crisis;
   - culture and roles: where insiders gather, their words, what each role sees;
   - incidents and judgment: critical moments told first-hand, with cues and the call made;
   - fights: the live disagreements and the old wars behind them.
   Each agent ranks material by `references/material-ranking.md` and cites every claim.
3. **Reuse before you collect.** Before sweeping a voice, check `skills/lens/lenses/` and
   `knowledge/corpus/` for it; a lens on the field is a voice already ingested. One voice worth deep
   provenance goes through corpus-ingestion. Several voices on one question go through
   corpus-synthesis. research-router `--brief` is the quick sweep when a field is new.
4. **Roles from first-person material.** A role is read from that role's own long first-person
   writing or talk: forum posts, interviews, postmortems. Never from a persona prompt. Simulated
   people sound like outsiders describing the group and lose its spread (Wang et al. 2025); grounding
   in interviews narrows that gap and does not close it (Park et al. 2024).
5. **Assemble the seven sections** per `references/pack-format.md`. Every claim carries a marker:
   `[D]` said by a practitioner in the source, `[M]` reported by someone else, `[I]` inferred by the
   pack, `[A]` the sources are silent. Fights stay open; the pack never picks a side.
6. **Machine checks**, written into `checks.md` (protocol: `references/checks.md`):
   - name, tone and fight tests, ten items each;
   - three incident stops: a recorded case cut at a decision point, the pack predicts the call;
   - the "where would I fail" list.
   A failed check sends the run back to the sweep for that section.
7. **The insider gate.** Build one thing a member of the field would judge: an answer to a real
   question in the field's community, a review the judge reads, or an SOP the judge uses. Record who
   judged, when, and what they said, word for word, in `checks.md`. Nothing posts or sends without
   Christian's go-ahead on that exact text.
8. **Hand-off.** `gaps.md` ends with his part: the spaces to join, the reps only a body can do, and
   the witness for them. Report the pack to him with the gate's state in one line.

## What this skill never does

- Writes into a vault folder. The pack is linked from the note that needed it.
- Posts, replies or messages anyone. Step 7 drafts; Christian sends.
- Calls a pack done on machine checks.
- Presumes the syllabus: section contents come from the sweep, not from a list written in advance.
