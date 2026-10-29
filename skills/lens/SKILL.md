---
name: lens
description: >
  Apply a framework "lens" to understand minds and ideas. A lens is a body of
  knowledge on disk (a corpus analysis, sometimes a wiki) plus a personality that
  reasons strictly within that framework. Modes are declared per lens: ask (query
  the framework), classify (read a person or a piece of work), reflect (turn the
  lens on your own thinking), challenge (an adversarial walk that tests an idea
  through the framework), select (shortlist the entries that fit a situation).
  16 lenses are registered, from cold email to art direction. Triggers: "/lens", "view through <framework>", "what stage is this", "classify
  this person", "challenge this idea through <lens>", "reflect on this through",
  "which thinking tool fits this".
---

# lens: pluggable framework lenses for understanding minds

## What a lens is

A lens is an externalized way of seeing. It bundles:

- a **wiki**, when one exists: human-written synthesis, the first place to look
- a **corpus**: the source material, for grounding and fallback
- a **core knowledge** file small enough to hold in context
- a `gap-register.md`: what the source never covers, which is where honest claims stop
- a **persona and constraints**: how the lens speaks, and what it refuses to do

The lens does not invent a worldview. It reasons inside one that already exists on disk, cites it, and keeps to the limits its own files state.

Lenses live in `skills/lens/lenses/<name>.md`. Paths in this skill are relative to the repo root, except the Definition column of the table below, which is relative to `skills/lens/`.

## Invocation

```
/lens <lens-name> <mode> [input]
```

- `<lens-name>`: e.g. `jason-murray`. If omitted, pick from the user's words and each lens's Framework column in the table below. Several may fit. The first line of the output names the lenses that ran and any plausible ones that were skipped, with the reason. Ask only when nothing in the input points to a lens.
- `<mode>`: one of `ask`, `classify`, `reflect`, `challenge`, `select`, narrowed to the ones the lens names in its `modes:` key. If omitted, infer from the input (a question → ask; a third party's text or work → classify; the user's own writing → reflect; a claim to stress-test → challenge; a situation the user is about to act inside → select). One mode per lens per run, named in the output. A question about the world is ask even when the user is part of that world; reflect only when the input is his own thinking. On 28 Sep a question about Filipino politics came back with "What the MBTI reading says about you", and he answered "I didn't want this to be about me".
- `[input]`: the question, the text to read, the claim to challenge, or a file path.

Conversational invocation works too: "view this tweet through jason-murray", "what would the framework say about X", "challenge my thinking on Y."

## How the skill runs

1. **Resolve the lens.** Read `skills/lens/lenses/<name>.md` in full. Its frontmatter holds the paths to the wiki, corpus, core knowledge, retrieval index and `gap_register`; its body holds the persona, the mode overrides and the hard constraints.
2. **Load the core knowledge.** Read the `core_knowledge` file in full before any output. A grep, a word count or a 60-line head is not a load. In the review of 20 Oct (`docs/reviews/2026-10-20-lens-self-review.md`), four of six sessions answered in a lens's name without reading it.
3. **Check the domain.** Compare the input with what the lens says it is strong and weak on (the lens file's opening, usually) and with its `gap_register`. When the input sits outside, the output's first line says so, and the lens then answers as marked outside commentary or not at all. On 17 Sep Josh Braun's cold-email rule went onto dashboard copy, on 19 Sep Adam Erhart onto a brand essence, and on 6 Oct Jason Murray onto a logo, each with no warning.
4. **Retrieve specifics on demand.** For anything past the core knowledge, go to the files, never a guess:

   ```bash
   grep -rn "<term>" <wiki_dir>                    # the wiki first
   grep -rn "<term>" <corpus_dir>/analysis         # then the corpus analysis
   ```

   Grep to locate, then read the matched file whole; an analysis file runs 10,000 to 25,000 words and the full section beats a fragment. Heading greps (`grep -rn "^#.*<term>"`) usually find the right article first. Never cite `.raw/notebooklm/` answers as the author's words: they are Gemini's summary, and pass 2 corrected 125 of nate-herk's.
5. **Enter the mode.** Follow `skills/lens/references/modes.md`, where the lens's own Mode overrides replace the generic template wherever they differ. For `challenge`, follow `skills/lens/references/challenge-walk.md`.
6. **Show the lens before acting on it.** The lens's output is advice, shown as its own block. When the input is the user's own work (his docs, a brand, copy, a drawing), the lens asks for his references first (a moodboard, earlier drafts) and puts its questions and recommendations to him through the `grilling` skill, one question per call with the recommended answer first; files change only after he answers. Never a merged review document: on 23 Oct he asked for grilling in place of reviews, because a round gets his feedback faster. On 19 Sep a session made 13 edits under ask mode and he answered "i havent really approved of it yet". On 6 Oct four wordmarks were drawn before the session had seen his Eden moodboard.

## Provenance

A lens is worth using only when each claim can be traced to its owner and its silences are stated.

- **Every claim names its owner**: the source author, the wiki author, or you. Three voices, never blurred.
- **Mark what is not the author's own words.** A claim the source states outright needs only its owner and its file. Anything inferred, borrowed from a guest, summarized by Gemini, or absent carries the lens's own marker from its `provenance_markers` frontmatter. With several lenses in one answer, each claim carries its own lens's markers: on 17 Sep a session tagged Kole Jain claims `[D]`, a marker his lens does not have.
- **Never upgrade an inferred marker to a direct one.** If the framework only implies something, say so.
- **A rule keeps its domain.** When a rule is used outside the field its author taught it in, say so next to the claim.
- **Honor the `gap_register`.** Where it marks a topic absent, do not put words in the author's mouth. Say the framework has no position, or give outside commentary under the lens's `demarcation` line.
- **End with one Sources line** naming the files read. In chat, wikilinks print raw; give file names, and keep wikilinks for output written into the vault.

## The modes (summary; full templates in `references/modes.md`)

- **ask**: answer a question from inside the framework, with sources. When the answer touches a gap, say the framework is silent and stop.
- **classify**: read a person or a piece of work against the framework's categories, with a confidence band. Show the signals that matched and the ones that did not, and report a contradiction as found.
- **reflect**: the lens turned on the user's own thinking. It raises questions and assigns no verdict.
- **challenge**: walk a claim through the lens's own challenge override, one critique at a time, each grounded in retrieved content. See `references/challenge-walk.md`.
- **select**: given a situation, shortlist the entries that fit, plus one that argues against them. What counts as an entry (a thinking tool, a menu line, a technique) is set by the lens's select override. One match, or none, is a real answer.

**Modes are declared per lens.** A lens's frontmatter carries `modes: [...]`, and the skill offers only those. A lens with no `modes:` line is a registration bug, caught by `scripts/tests/test_lens_registry.py`.

## Registered lenses

| Lens | Framework | Definition |
|---|---|---|
| `rian-doris` | The Flow Research Collective system: ~40 named protocols for protecting and restoring attention, authored by Rian Doris on cited flow and cognitive science | `lenses/rian-doris.md` |
| `dan-koe` | The one-person business and digital writing system, packaged inside borrowed developmental philosophy (Wilber, Cook-Greuter, Csikszentmihalyi, Naval) | `lenses/dan-koe.md` |
| `josh-braun` | Sales by detachment and question-led self-persuasion, from 6,009 of his own LinkedIn posts | `lenses/josh-braun.md` |
| `eric-nowoslawski` | Cold email where the offer is 70% of the result, with infrastructure rules treated as physics | `lenses/eric-nowoslawski.md` |
| `christian-bonnier` | Cold email copywriting driven by a four-level diagnosis of what demand the market already has | `lenses/christian-bonnier.md` |
| `nick-abraham` | Cold email and agency operations at volume, organised as Methodology / Operations / Craft / Infrastructure | `lenses/nick-abraham.md` |
| `alex-vacca` | ColdIQ's revenue system: outbound joined to ads and content in one compounding loop | `lenses/alex-vacca.md` |
| `michel-lieben` | Content-led growth and employee advocacy, with outbound run against an audience that already knows the name | `lenses/michel-lieben.md` |
| `nicolas-gromer` | Behaviour-based segmentation and multi-channel sequences. The smallest corpus here, 7 files | `lenses/nicolas-gromer.md` |
| `simon-scrapes` | Agents in production: context as the scarce resource, filesystem as the operating system, restart over correct | `lenses/simon-scrapes.md` |
| `kole-jain` | Product design as arithmetic — spacing, a 4-layer colour doctrine, and a named beginner-tell diagnostic | `lenses/kole-jain.md` |
| `adam-erhart` | Local-business marketing where order is the method: Model, Market, Message, Media, Machine. Gemini synthesis of 300 videos, Medium confidence | `lenses/adam-erhart.md` |
| `nate-herk` | Building and selling AI automation: agents as workflows, agents and tools (WAT), services priced on a four-rung ladder. 299 transcripts checked against 51 Gemini answers | `lenses/nate-herk.md` |
| `jason-murray` | Art direction as insight, idea, then two or three standout visual ingredients from a menu of 61, plus 28 named visual techniques. 75 transcripts, his slides read off video, 44 campaigns checked against trade press | `lenses/jason-murray.md` |
| `ryan-mathews` | Sales funnels by price band and the VSL inside them: under $2,000 a sales page, over it an ungated VSL, survey, then a call; long and short beat orders; the page around the video. 73 of his 76 long-form videos, 44 Gemini answers checked, 91 corrections | `lenses/ryan-mathews.md` |
| `alex-hormozi` | The offer system from $100M Offers, $100M Leads and his YouTube talks: value equation, grand slam offer, premium pricing, guarantees, scarcity, bonuses and naming, with each piece of advice set against what his businesses visibly did | `lenses/alex-hormozi.md` |

## Adding a lens

1. Copy `lenses/_template.md` to `lenses/<name>.md` and fill it in. (`lenses/jason-murray.md` is the worked example.) The frontmatter carries the paths (wiki, corpus, core-knowledge, retrieval-index, gap-register), provenance markers, and citation pattern; the body carries the persona overlay, the category reference, mode overrides, and hard constraints. Declare the modes the lens supports in the `modes:` frontmatter key; every declared mode needs a matching `## <mode>` section in `references/modes.md`.
2. If the lens has a wiki repo, put its path in the lens frontmatter (`wiki:`). Nothing to index — the
   skill greps and reads it directly. Note when a wiki lives outside this repo, so the dependency is visible.
3. Add a row to the Registered lenses table above.

A lens with an empty or absent corpus still loads — it just has nothing to retrieve. That is the expected state for a freshly scaffolded lens.
