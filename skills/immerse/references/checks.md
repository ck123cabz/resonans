# Checks and the insider gate

`checks.md` in the pack is append-only. Each entry is dated and records what was asked, what the pack
answered, and the result. A pack is done when `checks.md` holds an insider acceptance entry; that is
read at the time, never stored as a flag.

## Machine checks

Run all three before the gate. A fresh agent that has read only the pack answers each check,
because the session that wrote the pack would pass on memory.

1. **Name, tone, fight.** From the mathematics lore (13 Aug 2026). Ten items each, drawn from the raw
   sweep and held back from the pack:
   - Name: a person from the field is named; say who they are and what they stand for.
   - Tone: an insider term in a real sentence; say whether it is praise, insult or warning.
   - Fight: a position someone takes; say which fight it belongs to and what the other side says.
   Pass at 8 of 10 in each. Score against the raw source, not against the pack.
   Tone and fight items come from sources the pack does not cite, with sentences the pack does not
   hold. On 20 Oct 2026 the SOP-craft tone items reused culture.md's own sentences, and 9 of 10
   answers were read off its table. An answer whose basis is outside the pack scores 0.
2. **Incident stops.** Three recorded incidents from `.raw/`, each cut just before a decision. The
   agent names the cues it reads and the call it would make. Compare with what the person did and
   the cues they named (Klein 1998). Record a match, a partial match with the miss named, or a miss.
   Two of three must match or partially match. Use obscure cases only: a freelancer's forum post, a
   small team's postmortem. On 20 Oct 2026 all three SOP-craft stops (United 232, Qantas 32, GitHub
   2018) were void, because the test agent knew them from training and never needed the pack.
   The same goes for names: avoid the people every model knows.
3. **Where would I fail.** The agent lists the questions about this field it could not answer from
   the pack. Each becomes a sweep target or a `gaps.md` line (Collins and Evans 2015). The pack's
   own sense of confidence counts for nothing (Kahneman and Klein 2009).

## The insider gate

Collins's imitation game, cut down to what one person can run (Collins et al. 2006). The form
depends on the judge named in `README.md`:

- **A named practitioner.** They read one section, or the artefact built from the pack, and say what
  is wrong in it. Accepted when they name nothing wrong that the pack treats as settled.
- **A community.** An answer to a real open question in that community, written from the pack and
  posted by Christian. Accepted when a member engages with it as an insider answer: a reply that
  builds on it, an upvote from a practitioner, a follow-up question. Rejected when it is corrected
  on a point the pack held as `[D]`.
- **An SOP user.** Someone other than Christian follows an SOP built from the pack, cold. Accepted
  when they finish it without asking a question the SOP should have answered.

Record the judge, the date, the artefact, and what they said in their own words. A rejection goes
back to the section it exposed, and that section is re-swept before the gate runs again.

Nothing is posted or sent by the skill. It drafts the artefact; Christian sends it.
