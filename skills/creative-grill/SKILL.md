---
name: creative-grill
description: >
  Grill a content piece, campaign, reel, key visual or series before it gets made, with Jason
  Murray's art direction questions in his order: insight, idea, size, who carries the message,
  ingredients, references, ship. Each answer is graded against his test before the next gate.
  Use when Christian says "/creative-grill", "grill this idea", "grill the art direction",
  "before I make this", or starts making content with no settled idea. Enter at any gate.
---

# creative-grill

Christian is not an art director. Left alone he can iterate on execution forever while the
idea above it is missing. Murray's rule: "execution doesn't matter if you're executing a dumb
idea" (`core-knowledge.md` §9, rule 11). This skill borrows his questions, his order and his
tests, so the grill asks what an art director would ask and grades the answer the way he would.

The engine is the `grilling` skill: rounds through AskUserQuestion, recommendation first. This
skill adds the tree and a test for every node. Paths are from the repo root. Murray's corpus is
`knowledge/corpus/jason-murray/analysis/`; `core-knowledge.md` there is cited as "core".

## The gates

| Gate | Question | File |
|---|---|---|
| 0 | Is this inside Murray's domain? | below |
| 1 | Insight: "People think X, but the reality is Y" | `references/gates-concept.md` |
| 2 | Idea: "So let's ___", a verb and a name | `references/gates-concept.md` |
| 3 | Size: platform, campaign, execution, one-off | `references/gates-concept.md` |
| 4 | Who carries the message: the copy or the picture | `references/gates-craft.md` |
| 5 | Ingredients: two or three, each with a reason | `references/gates-craft.md` |
| 6 | References: his saves read at three levels | `references/gates-craft.md` |
| 7 | Ship: hook and finish line | `references/gates-ship.md` |
| W | Words, borrowed from Dan Koe and writing-video-scripts | `references/gates-ship.md` |
| E | Edit, borrowed from short-form-edit | `references/gates-ship.md` |

W and E run only when the piece has a script or footage. Run them after gate 7's hook.

## Gate 0: domain check

Murray's method is strongest on ads, campaigns, key visuals, content series, mood boards and
spec work. Route the rest in the first line:

- Logos and marks: the `logo-design` skill. The grill can still ask whether a mark carries an idea.
- Product UI: `/lens kole-jain classify`.
- Pure script writing with the idea already settled: `writing-video-scripts` from its step 3.

## Steps

1. **Read the project before asking anything.** Find its notes, scripts, Linear project and
   earlier drafts. Draft a candidate answer for every gate from them, each tagged with its
   source or marked a guess. Finding facts is your job; only the decisions go to Christian.
   When a render or draft exists, read frames of it (`ffmpeg -ss <t> -frames:v 1`, a contact
   sheet) and describe what is on screen. A script describes what was planned. On 20 Oct a
   candidate named "coin towers" from the script; the render opened on a dot chart.
2. **Pick the entry gate.** Default is gate 1. When he names a later gate, ask for every earlier
   gate in one line each first. A gate with no answer pulls the grill back to it.
3. **Grill one gate at a time.** Open its file. Put the candidate answer to him as the
   recommended option, with the gate's question. Grade his answer against the gate's **test**.
   An answer that reads like the gate's **weak** example gets the gate's **drill** and the same
   gate again. The gate is passed when the answer meets the test, quoted back to him in one line.
   On a failing pick, say which test it failed in one sentence with Murray's words, then ask
   again with his pick kept and the missing part added as the recommended option. On 20 Oct he
   chose plain 1960 towers as a key visual; it failed rule 20, and the retry kept the towers and
   added a bar stopping the PH one, which he took.
4. **Hold the gate.** Nothing is drawn, generated, edited or scripted while gates 1 and 2 are
   open. A mockup made before the idea passes is the iteration loop this skill exists to stop.
5. **Write the brief** to `scratchpads/creative-grill/<slug>.md` after every passed gate: his
   answer in his words, the test it met, the source line. The brief holds answers only; which
   gates are open is read from which sections are empty.
6. **Hand off.** Gate 5's named techniques go to `visual-techniques brief`. A script goes to
   `writing-video-scripts`, with gates 1 and 2 as its block 01 table. Footage goes to
   `short-form-edit` or `edit-video`, with gate E's answers as the brief.

The grill is done when gate 7 has an answer in the brief and he confirms the brief.

## Provenance

- Murray's own words carry `[D]` and the core section. Guests are labelled by name: Garrett
  King on photo direction, Jason Gold, Edward Sun. Core §10 lists what is borrowed.
- Gates W and E sit under the line `> NOT FROM MURRAY`. Name their source in every question.
- NotebookLM phrases ("visual pantry", "Centipede Test", "Ask Why Drill") are not his. Use his
  wording: "legs", "ask why", "filling a pantry".
- Where his corpus has no answer (photography against illustration, how many images on a
  board), say the framework is silent and give the nearest rule.

## Restraint

One question per gate per round, two at most. Two or three ingredients, never ten. The point
of the tree is that most questions wait until the gate above is passed.
