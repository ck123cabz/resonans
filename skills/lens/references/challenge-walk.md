# Challenge walk: testing a claim through the framework

The challenge mode tests a claim by letting the framework attack it from its own angles, one per pass, with each critique pulled from the lens's files. It aims the framework's internal tensions at the claim; it does not turn generic doubt up louder each round.

Each lens supplies its own angles. Every lens's `## Mode overrides` has a **challenge** line that lists its steps in order: xandros walks adjacent stages, the opposite pole and the stage's pathology; jason-murray walks the Big Idea Pyramid, the Idea Sizing Chart, the menu and the lineage. Until 20 Oct this file hard-coded the xandros steps, and on 17 Sep a dashboard-copy session read it, found no stages in Kole Jain or Josh Braun, and ran none of it.

Two ways to run it:

- **Quick walk**: one turn, every pass in sequence. Good for a fast check.
- **Deep loop**: the ralph-loop plugin runs one pass per iteration and deepens each time. Use it when the user wants the idea worked over at length.

Both use the same passes and differ only in how they are run.

---

## The passes

Ground every critique in retrieved content: the core knowledge, the retrieval index, the wiki when there is one. Never write in the framework's voice from memory.

### Pass 0: Restate and place

Restate the claim in one sentence. Then say where it sits in the framework: the stage for xandros, the pyramid tier for jason-murray, the part of the system the lens's categories name. Record why.

### Pass 1 to N: The lens's own steps

One pass per step of the lens's challenge override, in its order. Each pass pulls the files that step needs and states the critique that step makes of the claim. A claim is usually weakest against its own category's known failure, so give that step its full weight when the lens has one.

### Gap check

Read the `gap_register`. Where the claim leans on ground the author never covered, say the framework has no standing to support or attack it there. This keeps the walk from pretending to a position the source does not hold.

### Synthesis

Say which critiques held, which the claim survived, and what would have to be true for the claim to stand. The useful result is a sharper claim or a named open tension; skip the tidy verdict.

---

## Quick walk

Run every pass in one turn, a few sentences each. Cite the files each critique came from. End with the synthesis.

---

## Deep loop (ralph-loop)

The ralph-loop plugin feeds the same prompt back each iteration and relies on files to carry state, so the loop keeps its state in a session file and advances one pass per iteration.

### Setup

1. Pick a slug for the claim and create `scratchpads/lens-challenge-<slug>.md`, with one heading per pass: Pass 0, then one per step of the lens's challenge override, then Gap check and Synthesis. Put `<!-- TODO -->` under each heading, and `Lens: <name> | Started: <date>` under the title.

2. Launch the loop, with N as the number of headings:

   ```
   /ralph-loop "Read skills/lens/references/challenge-walk.md and the session file scratchpads/lens-challenge-<slug>.md. Load the <name> lens (skills/lens/lenses/<name>.md) and its core knowledge. Find the first pass still marked TODO and complete ONLY that pass: replace its TODO with the critique, grounded in retrieved content and citing the files. If a later pass deepens an earlier one, add a dated sub-note to the earlier pass. When Synthesis is written and every pass is filled, output the completion promise. Honor every hard constraint in the lens file." --max-iterations N --completion-promise "CHALLENGE WALK COMPLETE: all passes and synthesis written to the session file"
   ```

   - Raise `--max-iterations` past N to let the loop keep deepening after the first full pass.
   - The completion promise is a hard gate. Output it only when every pass is filled and the synthesis is real; never early to escape the loop.

3. When the loop completes, read the session file back and present the synthesis. Offer to keep the file or delete it.

The session file is the prior work ralph-loop shows each iteration. Without it each iteration starts cold and repeats Pass 0. It also leaves the user a record of how the idea was worked over.
