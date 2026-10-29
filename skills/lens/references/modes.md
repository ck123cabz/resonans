# Lens modes: prompt templates

These templates are framework-agnostic. The active lens (`skills/lens/lenses/<name>.md`) supplies the markers, the categories, the persona and the constraints, and its Mode overrides replace a template wherever the two differ. Read the lens file and its core-knowledge file in full before running any mode.

Retrieval, in every mode: when you need a specific the core knowledge does not cover, grep the wiki first and the
corpus analysis second (`grep -rn "<term>" <wiki_dir>`), then read the matched file. Cite what comes back.
Never fill a gap with a guess.

---

## ask

Answer a question from inside the framework.

1. Check whether the core knowledge already answers it, and retrieve when it does not.
2. Answer in the framework's own terms, quoting iconic phrasing verbatim where it carries meaning.
3. Attach provenance markers and citations to every claim (wiki page or corpus q-file).
4. If the question falls on a gap-register `[A]` topic, say the framework is silent and stop, or offer clearly-demarcated outside commentary. Do not improvise a position and attribute it to the source.

Output: a direct answer, then a short "Sources" line listing the pages/q-files cited.

When the question is about the user's own work (his docs, his brand, his copy), the answer is the questions the framework would ask of it and what it recommends. No file changes until he answers. On 19 Sep this is what worked: Erhart's rules sent to him as questions got long answers on docs 01 and 02.

---

## classify

Read a person (or a group, or a piece of writing) through the framework, from a sample of their text.

1. **Intake.** Take the supplied text (transcript, posts, a description, a file path). If the sample is thin, say so; confidence scales with evidence.
2. **Signal extraction.** Pull concrete signals: vocabulary, what they value, how they reason about cause and effect, what they treat as obviously true, what they dismiss. Quote the actual phrases.
3. **Match.** Map signals to the framework's categories. For each candidate category, list the signals FOR it and the signals AGAINST it.
4. **Assess with a confidence band.** Give a primary read and a confidence level (low / medium / high) tied to how much the signals converge. State what would raise or lower confidence.
5. **Report contradictions, don't resolve them by force.** If the surface says one category and the substructure says another, name both. Mixed/uneven development is a real finding, not a failure to decide.

Hard rule: classification is for understanding, never for ranking-and-dismissing. If the request is to pull rank on someone, invoke the lens's misuse constraint and decline that framing.

Output: Primary read + confidence → Signals for → Signals against → Contradictions / open questions.

---

## reflect

The lens turned on the user's own thinking. Same machinery as classify, different posture.

1. **Intake** the user's own writing, decision, or stated belief.
2. **Extract signals** as in classify.
3. **Reframe toward questions.** Skip "you are at category X"; surface "this reasoning has the shape of X; the thing X tends to be blind to is Y — does that land?" The goal is a better question, not a verdict.
4. **Apply the lens's self-assessment caveats.** For frameworks that warn about self-placement bias, apply the correction explicitly (xandros: the +2 bias: people read themselves ~2 stages high; the stage just above tends to feel "crazy").
5. **Honor anti-self-ranking caveats.** Don't hand the user a flattering label. Don't hand them a damning one either. Offer the lens as a mirror, not a scoreboard.

Output: What the lens notices → What that vantage tends to miss → Questions worth sitting with.

---

## challenge

Tests a claim by walking it through the lens's own challenge override, one step at a time, each critique pulled from the lens's files and none improvised. Full procedure in `challenge-walk.md`. It ends with a synthesis of which critiques held and which the claim survived.

---

## select

Given a situation, a workflow, or a decision, return the entries that fit it. The lens's select
override says what an entry is (a thinking tool, a menu line, a technique) and where its
examples come from. The retrieval steps below are thinking-tools'; other lenses follow their override.

**Input:** a description of what the user is about to do or is stuck inside.

**Retrieve:** load the lens's `core_knowledge` (the index). Match the situation against each
entry's trigger list. Where fewer than two match, widen on `domain`, which the index has no
column for: read the entry notes under `retrieval_index` and match the situation against the
`domain` field in each one's frontmatter.

**Output:**

1. **Two entries by default, four at most**, and only when they do not overlap. Each as: the
   entry name, one line on what it would have the user do here, and the specific hook in their
   situation it grabs. The name is a wikilink only when the output is written into the vault;
   in chat a wikilink prints raw.
2. **One entry that argues against the others.** If the shortlist has no opposing
   member, say so and do not manufacture one.
3. **What the inventory does not cover here**, read from the `gap_register`. Silence beats
   improvising.

**A short list is an answer.** One match and no match are both ordinary, and neither is fixed
by padding:

- **One entry matches.** Return it alone and say the inventory holds nothing that argues with
  it. Part 2 is skipped, not filled.
- **Nothing matches.** Return no entries. Name the closest one and why it misses, then say what
  the inventory would need in order to answer this: a trigger slug it does not carry, or a tool
  it has no note for. That belongs in `GAPS.md`, and it is worth more than a padded shortlist.

**Never:** collapse two conflicting entries into one recommendation, quote the user's own
`> [!note] My take` callout back to them as though the framework said it, or return an entry
whose researched block is listed as thin in the `gap_register` without flagging it as thin.
