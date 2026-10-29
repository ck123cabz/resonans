---
type: corpus
aliases: ["Gap Register: Alex Hormozi (layer one)"]
corpus: alex-hormozi
layer: analysis
tags: [corpus, machine, offers, pricing]
source: skills/corpus-ingestion
created: 2026-10-16
---

# Gap Register: Alex Hormozi (layer one)

**Date:** 16 Oct 2026. **Layer 3 of 3.** Consolidates the `[A]` signals in Pass 1, the gap table in Pass 2 §7 and the profile's known gaps. It tells the consumer what the corpus does not hold and tells Christian what collecting more would fix.

Read with `core-knowledge.md` (Layer 1) and `retrieval-index/` (Layer 2).

---

## 1. What is in and what is not

| Part | State on 16 Oct 2026 |
|---|---|
| $100M Offers audiobook, 7 parts | In. Transcribed locally and checked. |
| $100M Leads audiobook, 11 parts | In. Parts 2, 3, 4, 9 checked against local transcripts; 1, 5 to 8, 10, 11 are NotebookLM only. |
| YouTube: 28 videos on offers, pricing, guarantees, leads, closing | In. Not transcribed locally; every signal from them is `[M*]`. |
| $100M Money Models audiobook (9 parts) and $100M Lost Chapters audiobook (26 items) | **In (layer two, 16 Oct 2026).** Same podcast feed (items dated 19 Aug 2025 and 14 Nov 2025). All 35 items transcribed locally (85,586 words) and added to the notebook as text. The seven free-offer types and the attraction names that layer-one answers cited without a source are Money Models material; they are now sourced. |
| The rest of his channel and The Game back catalogue (1,157 episodes) | Not in. |
| Independent record | Eight items, grades A to D, `.raw/research/independent-record-2026-10-16.md`. |
| Lens | Created and registered: `skills/lens/lenses/alex-hormozi.md`; `scripts/tests/test_lens_registry.py` passes (6). |

---

## 2. Boundaries the lens must state aloud

| Boundary | Detail |
|---|---|
| **No half-price first month** | Layer one said so (q71). Layer two found the nearest: a 95% or 88% first-month discount with a setup fee, a $1 first month, 50% off for life, and the 80/60/40/20 ladder by client number (`[D]`, Pass 2 L2.2). No 50% first month exists. |
| **No priced stand-alone audit** | Every audit example is free, or a $19 diagnostic before a $2,100 program (q70, q105; `[D]`). |
| **No good-better-best menu for one core offer** | Four fresh queries find none (q68, q106 and the layer-one q15). What exists: the anchor upsell at 5 to 10 times the core, the decoy menu, and pick-your-price rungs above a free base (`[D]`). The earlier pyramid came from the question. |
| **No price-rise letter to existing clients** | Pipeline notices exist; the letter does not (q16, q17). |
| **No sample size or pass mark for testing an offer** | q33, q34. |
| **No rule that a name carries result and time** | MAGIC components are optional (Offers part 7). |
| **No single launch with dates** | One example that combines scarcity, urgency, bonuses, guarantee and name does not appear (q25). |
| **No Philippine market, no service business under ₱100,000 a month, no non-fitness local trade** | q72. The dead-zone prices and the weekly wage figures are US dollars. |
| **No agency retainer price or scope between $400 and $1,500 a month, no two-person or non-US agency** | q94, q95 (S-94.3). Layer two's agency examples are performance and pay-on-show offers. |
| **No money model with a labour cost instead of an ad budget** | q108 (S-108.12). The no-ad-budget rules are Leads material. |
| **No firing-a-client protocol, no legal or licensing guidance** | q72. |
| **No cost per lead** | Only $25 of fulfilment plus $75 of ads, or $100 per engaged call (q39, q44). |
| **Upload dates for the videos** | Absent. A book-versus-video change cannot be ordered (q55). |
| **The "exactly five" free clients** | His book says the number "matters less than knowing why". |

---

## 3. Evidence gaps

1. **Results are his own words.** Revenue ($120M in 24 months, $17M profit, $1.6M a week), client outcomes (the 158-gym survey, $30,000 in 30 days, $42,000 per launch) and the weight-loss and agency case studies have no outside record. The survey was voluntary and of his own clients.
2. **Layer two added no outside source.** The outside record is still eight items.
3. **The customer record is thin and low-grade.** Review sites and one lawyer's anecdote. No court filing, regulator action or refund rate was found or read.
4. **Book versus video origin is unresolved** for the $19 to $1,997 time-management ladder, the 99.6% figure, the toilet-paper price, Jason Fladlien's $25,000 buy-back, Lloyd's newspaper software, the small-business dead zone, and the 20-people-or-next-month-free guarantee. None was found in the transcripts of Offers, Money Models, Lost Chapters or Leads parts 2, 3, 4 and 9, so they come from the other Leads parts or the videos.
5. **About 40 sums in the answers do not add up** (Pass 1 flags them in place). Pass 2 resolves the ones it could: 3.1× is his rounding, the $4,351 total is his slip, $5.4M is about $54,000 a head, 33 gyms and "8 a month at peak" are both his. The others stay flagged.
6. **Topline growth for the 158-gym survey** is heard as "$239,000 per month" in the audio and "per year" in the answers.
7. **The half-price poacher** is a client gym owner in two answers and a competitor in a third. Needs the Offers part 1 audio at that passage.
8. **NotebookLM chat bleed.** Q1 to Q35 and Q48 to Q64 ran in one conversation and several answers open with the previous one. Signals were attributed to the question they answer. Q67 to Q72 and Q36 to Q47, Q65 and Q66 ran in fresh conversations. `scripts/nlm_extract.py` now passes `--new-conversation`, which affects any later run on any corpus.
9. **q39 was cut off** on its first run and was re-run in full. Pass 1 block F holds the cut version; Pass 2 §4 row 12 and `core-knowledge.md` §6 hold the rest.

---

## 4. Collection decisions

| Gap | Fix | Cost | Priority |
|---|---|---|---|
| Agency and retainer pricing; a money model with a labour cost | Other lenses (adam-erhart, nick-abraham, eric-nowoslawski hold local-business and agency material); Christian's batch | Reading plus the trial | High |
| Customer-outcome record | Read the IMAP page in full, search court records for "Gym Launch", read BBB complaints, find 2017 to 2019 sales pages on the Wayback Machine | Separate research task | High |
| Local transcripts for Leads 1, 5 to 8, 10, 11 and the videos | whisper.cpp on the Leads audio already downloaded; videos need audio pulled | About an hour of machine time for Leads | Medium |
| Video upload dates | `yt-dlp --flat-playlist` with dates, added to the manifest by video id | Small | Medium |
| Free work for Dumaguete B2B and B2C small businesses | Test with the batch of five; compare with the free-first material in josh-braun, adam-erhart, christian-bonnier, eric-nowoslawski | The trial itself | High |
| The 20-people guarantee and the dead zone: book or video | Transcribe the videos the dead zone came from | Medium | Low |

---

## 5. Consumers

1. `skills/lens/lenses/alex-hormozi.md`, registered in `skills/lens/SKILL.md`. Done.
2. The Resonans offer draft (due Fri 23 Oct 2026) reads `core-knowledge.md` §9. The link goes in `02-projects/resonans.md`; this run did not edit that note, which is Christian's.
3. Tier prices on the Resonans site (live by Sat 25 Oct) read §9.2.
