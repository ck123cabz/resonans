---
type: corpus
aliases: ["Gap Register — Simon Scrapes"]
corpus: simon-scrapes
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-23
---

# Gap Register — Simon Scrapes

Living document. Consolidated from Pass 2 (2026-07-22). Update when a gap is filled or a new one surfaces.

## High priority

### G1 — Exact key names and install commands are transcript-garbled
Every settings.json key, env var, and plugin install command in this corpus is a phonetic rendering of something that was shown on screen ("memarch" marketplace heard as "zillastte mem search", Ralph as "raw", the subagent-model key as "full code sub aent model"). Applying a corpus spelling verbatim will fail or misconfigure.
- **Fill by:** verifying each key/command against Claude Code docs or the tool's GitHub repo at the moment of use. Never lift from this corpus directly.
- **Affects:** q13, q16, q25, q31, q39 and every retrieval-index chunk carrying the warning.

### G2 — Routines billing contradiction
q27 says cloud Routines draw from Pro/Max plan usage; q28 says scheduled cloud work still bills via API with only interactive chat riding the subscription. No video dates available to order the two claims. This is a real cost decision for any scheduled-autonomy design.
- **Fill by:** current Anthropic pricing/docs at decision time.

## Medium priority

### G3 — No per-claim video dates
Contradictions can't be ordered and staleness can't be judged; Claude Code moves monthly and this corpus is an undated 2026 snapshot.
- **Fill by:** a yt-dlp metadata pass over sources.tsv adding upload dates; optionally tag claims to source videos via NotebookLM citations in the raw q-files.

### G4 — On-screen content systematically lost
The transcript extraction captured spoken architecture but lost everything demonstrated visually: exact file contents, JSON keys, dashboards, config screens. The most directly actionable artifacts are the ones missing.
- **Fill by:** targeted yt-dlp transcript + frame pulls for named high-value videos (settings video for q39, Memarch install video for q16).

## Low priority

### G5 — n8n era (~109 of 159 videos) unextracted
Only Q37 (comparison) and Q40 (sweep, which surfaced nothing) touch it. Matters only if n8n work enters scope.
- **Fill by:** a dedicated n8n question lane against the same notebook (quota permitting).

### G6 — 18-skill social pipeline roster incomplete
Only ~8 of the 18 skills are named in-corpus; the build can't be fully reproduced from this extraction.
- **Fill by:** follow-up notebook query or transcript pull.

### G7 — Mermaid compression asserted, never demonstrated
The token-savings claim has no worked example in the corpus.
- **Fill by:** any external benchmark or a five-minute local test.

## Structural (inherent to the corpus, not fillable by more extraction)

- **No first-order source:** all content is NotebookLM-mediated; [M]→[D] provenance confirmation would require raw transcripts, which is G4's method applied broadly.
- **Anthropic-practice claims are retellings:** the slot-machine phrase, team workflows, and first-try success rates are Simon retelling Anthropic sources, not the sources themselves.
