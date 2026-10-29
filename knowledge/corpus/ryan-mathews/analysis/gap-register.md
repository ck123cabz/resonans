---
type: corpus
aliases: ["Gap register: Ryan Mathews corpus (Layer 3)"]
corpus: ryan-mathews
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-10-08
---

# Gap register: Ryan Mathews corpus (Layer 3)

Written 7 Oct 2026 from the 30 `[A]` gaps in the four Pass 1 lane files and the gap table in `analysis/pass-2-reconciliation.md`. Duplicates are merged; each row names the lane files that raised it. Paths are relative to `knowledge/corpus/ryan-mathews/` unless they start with `skills/`, `docs/` or `research/`.

"Lens" means `skills/lens/lenses/ryan-mathews.md`, which does not exist yet. "The brief" means a client's VSL brief: a B2B M&A deal-flow platform, done for you, sold on a call, with the VSL on YouTube and in a cold-email follow-up.

Priority: High blocks a correct answer for the lens or a decision in the brief. Medium weakens one. Low is background.

## 1. Consumer wiring

| Gap | Why it matters | What would resolve it | Extraction method | Priority |
|---|---|---|---|---|
| The lens file does not exist. The brief answered A1 and A2 straight from the Pass 1 files; challenge C1 waits on the lens. | A corpus nothing reads is not done. Without the lens, every later VSL question means re-reading 2,700 lines of Pass 1. | Pass 3 core knowledge and retrieval index, then the lens entry registered in `skills/lens/SKILL.md` | Write from Pass 3, modes ask, classify, challenge, per the profile | High |

## 2. The VSL itself: length, timing, format

| Gap | Why it matters | What would resolve it | Extraction method | Priority |
|---|---|---|---|---|
| **No length rule per surface.** His one norm is "about 20 to 30 minutes" for a cold-ad VSL (AJ&Smart teardown, 2025-05-05). He modeled MSP Fuel's script on a 5-minute Charlie Morgan VSL. No transcript pairs a length with YouTube, email, warm or retargeting traffic. Raised in lanes 1 and 2, 3 and 4. | The brief's 3 to 4 minutes cannot cite him. The lens would invent a rule if asked "how long for YouTube?" | His own statement, or two cuts of one script compared on one source | Check the 3 missing videos; scrape his Conversion Ideas newsletter archive; search his Shorts captions for "minutes long" | High |
| **No beat timings.** Every timestamp NotebookLM gave in q07 is its own. The Picture beat gets one clause. Lanes 1 and 2. | VSL 1's section lengths are guesswork | One VSL timed beat by beat | Time Steve's live VSL (A Life Engineered) and the Charlie Morgan VSL he modeled, by hand from the page, and mark the result `[I]` | Medium |
| **Nothing on faceless or AI-voice VSLs.** No transcript mentions synthetic voice, ElevenLabs, avatars or "faceless". The nearest formats are founders narrating their own screens: William Brown's Stripe, Ravi Abuvala's Google Doc, Sam Ovens' Loom. Lanes 3 and 4. | The client asked for "eleven labs voice on it". This corpus can neither back nor block it, and the lens must say so rather than guess. | Another corpus, or a the client test | Not fillable from this channel. Use `research/2026-10-07-elevenlabs-voice-plan-for-vsl.md`; run a voice A/B on VSL 1 | High |
| Production quality evidence is about ads, not VSLs (his $1M of YouTube ads, the skits client) | The lens could carry an ad rule onto a VSL | His own VSL production comparison | Conversion Ideas archive | Low |
| No email-only cut of a VSL; captions on the VSL itself are never discussed; pre-call rep videos are named once and not described. Lanes 3 and 4. | The cold-email follow-up surface has no model in this corpus | A described email VSL flow | Charlie Morgan's opt-in emails (nine in four days, per Ryan) if captured elsewhere | Low |

## 3. Numbers he never gives

| Gap | Why it matters | What would resolve it | Extraction method | Priority |
|---|---|---|---|---|
| **No watch-time, play-rate or completion figure for any VSL.** Searched all 73 transcripts. The only percent-watched is an FHL speaker retargeting "95%" ad viewers. Lanes 1 and 2, 5 to 7. | Nothing to set a target for VSL 1 or judge it by after it ships | Any retention curve he shows | Vidalytics case studies (he is an affiliate); otherwise measure the client's own YouTube analytics after VSL 1 and treat that as the baseline | High |
| No show-rate baseline for his own funnels; only others' (AJ&Smart about 80%, a 50% client) and a 2025 decline with no number. Lane 5 to 7, lane 8. | The confirm-your-call page has no before and after | His own numbers | Conversion Ideas archive | Medium |
| No booking rate for Steve or MSP Fuel; cost per booked call only for Steve's first week of ads ($11). Lanes 5 to 7. | The two closest cases have no funnel numbers past the headline | Later updates on either client | His videos after 11 Sep 2026 | Medium |
| No conversion, booking or close figures for his own Funnel Architecture funnel. Lane 8. | The funnel he recommends most has no numbers of his own | Same | Same | Medium |
| No tested result for the post-CTA testimonial frame or any hook variant on Steve's VSL. Lanes 1 and 2. | The one dated VSL-ending move (May 2026) is untested | His follow-up | His videos after 7 May 2026 | Medium |

## 4. Offer and price

| Gap | Why it matters | What would resolve it | Extraction method | Priority |
|---|---|---|---|---|
| **Where the price is spoken in a high-ticket VSL.** His over-$2,000 funnels show no price on any page; the word "price" does not occur in the Steve teardown. Nothing says whether, or at what minute, the video names it. Lanes 1 and 2, 5 to 7. | the client keeps the call. The brief says no price in the video, and that rests on what he omits, not on a rule he states. | His statement, or a high-ticket VSL transcript that names a price | The Brunson Linchpin video (missing, may cover a VSL offer); Ali Abdaal's page, which he reads with a $995 price, is a low-ticket counterexample | Medium |
| **No B2B outbound-agency example beyond MSP Fuel**, and MSP Fuel had no results on camera. Lanes 5 to 7. | The nearest analog to the client is unproven | A later MSP Fuel update, or another B2B case | His videos after 11 Sep 2026; Conversion Ideas | Medium |

## 5. AI in the VSL build

| Gap | Why it matters | What would resolve it | Extraction method | Priority |
|---|---|---|---|---|
| No Claude VSL skill. His copy-skill video (2026-01-20) covers sales pages and emails; his VSL script example (2025-12-02) runs in a ChatGPT custom GPT. Lanes 5 to 7. | Tier 1 of the brief plans his three-skill setup for the VSL script; he never showed it on a VSL | His own Claude VSL build | His videos after 11 Sep 2026; otherwise build it and log the result | Medium |
| No Claude-built static VSL page. He builds pages in GoHighLevel or vibe-codes an app. Lanes 5 to 7. | The the client page build has no model from him | Same | Same | Low |

## 6. Missing sources

| Gap | Why it matters | What would resolve it | Extraction method | Priority |
|---|---|---|---|---|
| **Three videos with no transcript:** 2Q-S3uFBNoM Brunson $265M Linchpin (2024-08-20), fZjUTHNlgfw Dan Koe $4.3M (2024-03-22), g9bpQDAGdC0 Whop vs Skool (2025-06-03). Exa returned nothing for them. Lanes 1 and 2, lane 8. | The q05 Dan Koe flywheel and the Whop claims in q41 and q42 cannot be checked. The corpus is otherwise the whole long-form channel. | Their transcripts | yt-dlp auto-captions; a Whisper transcription of the audio; the Exa contents API again | Medium |
| **40 bare-URL sources at error status** in notebook `dbdbda41`. Per the manifest, 28 also failed in notebook A and about 12 duplicate sources copied from A. Lane 8 matched 73 of 76 long-form videos, so these 40 likely add no video beyond the 3 above. | They inflate the notebook's source count and NotebookLM may cite them as empty | Confirm each id is a duplicate, then remove them | Compare their video ids with the 73 files and the 3 missing ids; deleting them from the notebook needs Christian's yes | Low |
| His Shorts, community posts and the Conversion Ideas newsletter are not in the corpus | The newsletter is where he says he sends one tested idea a week; it may hold the numbers sections 3 and 4 lack | A scrape | The newsletter archive; yt-dlp on the Shorts tab | Medium |

## 7. Attribution and his own record

| Gap | Why it matters | What would resolve it | Extraction method | Priority |
|---|---|---|---|---|
| The seven beliefs: claimed as his find in April 2024, credited to Cole Gordon in April 2026. He names six in 2024. | The lens could credit Cole's framework to Ryan, or the reverse | Cole Gordon's own source for the seven beliefs | Cole Gordon's material, outside this corpus | Low |
| Captions have no speaker labels. Five videos carry a second voice (Cole Gordon is 80 to 85% of one). Lane 8. | A guest's line can enter the lens as his; q15 already did this with Cole's 10 to 15 minutes | Diarised transcripts | Whisper with diarisation on the five files lane 8 lists | Low |
| His revenue today, Funnel Architecture's size and client count, the 2.6x exit (no name, year or price), what became of Consulting Label, his ad spend after 2022, the unnamed vibe-coded product, his age, location and team. Lane 8. | Background for the lens's voice; no bearing on the brief | His own statements | None needed now | Low |
| A full reminder cadence between booking and call, beyond objection emails 6 hours apart. Lanes 3 and 4. | the client's Nudge to Book flow has no full model here; the only test (four emails over 225 calls) moved show rate 0.2% | His cadence | Conversion Ideas archive | Low |
| A paid vs organic VSL difference, stated as a rule. He says they differ and tests per source, but gives none. Lanes 1 and 2. | Contradiction 3 in Pass 2 stays open | Same | Same | Low |
