---
type: corpus
aliases: ["Gap Register — Rian Doris (Flow Research Collective)"]
corpus: rian-doris
layer: analysis
tags: [corpus, machine, psychology]
source: skills/corpus-ingestion
created: 2026-07-28
---

# Gap Register — Rian Doris (Flow Research Collective)

**Date:** 2026-07-28
**Layer 3 of 3.** Consolidates the 31 `[A]` signals from Pass 1 with the gap analysis in Pass 2
§4 and the profile's known gaps. This is the collection decision input: what the corpus does not
hold, what that costs a lens, and what would fix it.

Read alongside `core-knowledge.md` (Layer 1) and `retrieval-index/` (Layer 2).

---

## 1. Boundaries the lens must state aloud

Things a reader will assume the corpus covers, and it does not. The lens says so rather than
improvising.

| Boundary | Detail |
|---|---|
| **No upload dates** | Not one of the 55 videos carries a publish date in the corpus. Consequence: 18 internal contradictions are permanently ambiguous between "he changed his mind" and "he is inconsistent". No evolution analysis is possible. |
| **Four protocols are named for a number that is not in them** | "56 Secs" (content: 60–90 seconds), "58 Secs" (resolves to the 45/5 cycle), "8 Minutes" (nothing timed), "11 Minutes" (**verified by re-query 2026-07-28: the transcript never states 11 minutes**). The lens never quotes these as durations. |
| **No "Massively Transformative Purpose"** | q01 records that the sources never use the phrase. They define an "infinite purpose" doing the same job. Do not import the MTP vocabulary. |
| **No counter-indications, anywhere** | 44,047 words contain no medical disclaimer, no contraindication, and no population caveat against 48-hour fasts twice monthly, 300mg caffeine ceilings, 1mg nicotine, or 15°C sleeping. This is an absence in the source, not an endorsement by it. The lens supplies the boundary. |
| **No timeline for Attention Recovery** | The protocol is pitched as replacing 23 minutes 15 seconds with 3 seconds. How long the training takes to work is never stated. |
| **No terminating condition for the Salience Swap** | And no fallback for when pull work is unavailable. |
| **No test for which procrastination treatment applies** | The corpus gives two mutually exclusive responses (force engagement, or abandon the task as a signal of ambivalence or burnout) and no way to tell which case you are in. The highest-cost gap in the corpus, because it is the question readers actually bring. |
| **No integration rule between competing protocols** | The 45/5 cycle, a 10–30 minute certainty window and "the first 3 hours on the scaling blocker" all claim the same block of the day. |
| **No prices or model numbers** | q20 names workspace equipment by category and brand but never by price or model. |
| **Tier 2 and Tier 3 of the minimalism system are never distinguished** | q21 names three tiers and defines two. |
| **Chronotype taxonomy does not sum to 100%** | q42's population shares total 85–90%. A reader may not find themselves in it. |
| **"Round" is undefined in the Flow State Breath** | "3 rounds (or 9 total breaths)" admits two readings; both are carried in the numbers index. |
| **Part-lists cited by count but not enumerated** | van den Hout's 7 team-flow triggers (only 2 named), Maslach's 6 burnout triggers, and Kotler's trigger list are referenced by number without being listed in full. |

---

## 2. Evidence gaps

The corpus's claims outrun its evidence in a specific, patterned way.

**Seven figures carry a protocol and are attributed to nobody anywhere in 44,047 words:**
the 4% challenge-skills stretch (which carries the entire tuning practice), the 4:1 chronotype
return, the 50–70% dopaminergic firing drop, the 40% context-switching cost, the 50/25/25
standing ratio, "cutting 3 hours of sitting adds 2 years of life expectancy", and the carnivore
flow-meal claim.

**Two of those seven Doris flags himself.** He states the 4:1 return is not peer-reviewed
("in our experience having worked with thousands and thousands of clients") and marks the
carnivore meal as a sample of one. This is the corpus's only counter-evidence, and it corrects
the pre-ingestion assumption that none exists.

**Citation quality, measured.** Of 56 named authorities in q59: 9 carry a date, 3 name a
journal, 0 name a paper title. The headline percentages (500% McKinsey, 490–500% DARPA, 430%
University of Sydney) arrive with no design, sample, or link. The corpus supports "he cites X".
It does not support asserting X.

**The grounding is asymmetric, and the asymmetry runs one way.** Where the corpus grounds a
claim it grounds a **cost** from his own life: the hypomania spiral and what it destroyed, the
water-slide head injury at 13, the Long Covid year. Those are specific and self-reported against
interest. The **benefit** claims rest on borrowed statistics or on Flow Research Collective
revenue, and the revenue is confounded because the company sells flow training. Its 8-figure run
rate evidences demand for the claims, not efficacy of the protocols.

**No independent replication, no critic, no failed adopter** appears anywhere in the corpus.

---

## 3. Population validity

The protocols assume a reader the corpus never names. Evidence, not suspicion, after Pass 1:

- "Stop dating or stay married" and a leased office (q07)
- Outsource laundry; 24 hours fully offline (q09)
- Eliminate the chore "using cash or creativity" — every remedy in q36 costs money
- "Kids at school or asleep" as the precondition for the deep block (q11)
- A $500K/month payroll and 60+ staff make the People Leverage vector explicit (q52, q58)
- The morning fix presumes nobody depends on your morning, while q15's own examples include
  "getting your kids to school"

The single acknowledgement of household obligation (q21's possession tiers) covers objects, not
time. **The lens must not prescribe People Leverage to a reader with nobody to leverage**, and
should name the assumed conditions when prescribing anything that presumes schedule control or
discretionary cash.

---

## 4. Coverage gaps

| Gap | Cost | Fix | Effort |
|---|---|---|---|
| 55 videos of a larger channel; long-form podcast appearances absent | Coverage is partial and unversioned; no way to know what is missing | Add remaining videos and podcast transcripts to the notebook, re-extract | Medium |
| No upload dates | See §1 | Resolve each title to its video and scrape the publish date (yt-dlp), attach to the manifest | Medium — the notebook API does not expose source URLs, so the 55 titles must be resolved first |
| Underlying studies unread | Cannot verify any borrowed claim | Trace citations individually | Separate research task, outside this corpus |
| Michael Fox credited to UBC for the DMN/TPN anti-correlation | Attribution looks wrong against outside knowledge | Verify | Low |

---

## 5. Errors carried from the source

Recorded so nothing downstream republishes them.

| Error | Where | Handling |
|---|---|---|
| **Adenosine described as "a wakefulness neurochemical suppressed by darkness"** | q45, Step 3 | **Factually wrong.** The same file describes it correctly elsewhere as the sleep-pressure signal that builds during waking. Only the correct version reaches Layers 1 and 2. |
| "VUKA" for VUCA | q38 | Spelling artifact |
| "Ivita" for Edita Navratilova; "Baros" for Barros | q55 against q59 | q59 spellings preferred |
| "Gotlieb" and "Gottlieb" in one sentence | q50 | Both carried, neither verified |
| "8:00 AM: Reboot routine" inside an otherwise PM-ordered evening sequence | q35 | Near-certain typo for 8:00 PM; preserved verbatim with the flag |
| Chronotype shares total 85–90% | q42 | See §1 |

---

## 6. What Layer 1 supplies that the corpus does not

Marked `[I]` in `core-knowledge.md`, listed here so the boundary between corpus and synthesis
stays visible:

1. The distinction between threat-locked rumination and deliberate incubation. The corpus uses
   the default mode network as both villain and supercomputer and never separates them.
2. One reconciled account of dopamine across the five incompatible jobs it carries.
3. Cognitive load, life-maintenance load and allostatic load presented as one family at three
   timescales. The corpus names them separately and never relates them.
4. The named assumed reader, and the gate on People Leverage.
5. The counter-indication boundary on doses, fasts and stimulants.
6. The distinction between what the corpus grounds and what it asserts.

---

## 7. Resolved before delivery

- **q41's missing 11-minute protocol** — re-queried 2026-07-28. Confirmed absent from the
  transcript. Moved from "possible extraction failure" to a stated boundary in §1.
- **Corrupt sources** — none. All 55 imports are readable, unlike the escaping-ordinary notebook
  which lost two to broken imports.
- **Consumer surface** — `skills/lens/lenses/rian-doris.md` was the first entry in this register
  until Pass 3 wired it. Now live.

## Related

- [[04-resources/thinking-tools/flow.md|Flow]] — This lists the flow numbers Doris cites with nobody attached, including the challenge-skills stretch the flow note is built on.
- [[01-inbox/fully-leverage-notebooklm-workflow.md|Fully leverage NotebookLM workflow]] — His NotebookLM plan hits the limits written down here, like the notebook API not giving back source URLs.
