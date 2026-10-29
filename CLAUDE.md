# Resonans

Resonans is a marketing agency run from this repo: Christian Cabaluna and Sai, serving small
businesses abroad, video first. `business/offer.md` holds the offer, the packages and the
dates. Read it before any client-facing work.

## How work runs

Every job is a stage of the pipeline in `README.md`, and every stage has a skill. Name the
stage, load its skill, and follow it. When no skill covers a stage, do the work by hand once,
then write the SOP with `write-sop` so the next run is a skill or an SOP.

Resonans is client zero: a stage runs on Resonans's own brand and channels before it runs
for a client.

## Rules that hold everywhere

- Prose a client or prospect reads goes through `python3 scripts/ai_slop_lint.py <file>`
  before it is called done. Fix every tier 1 line.
- Resonans names what AI builds and who decides. AI builds from named frameworks, and
  people make the calls. Never a bare "AI" or "proven frameworks" in copy.
- No paid generation (Kie.ai, Higgsfield, Wavespeed) without quoting the model, inputs and
  credit cost and getting a yes first. Build from real footage, screenshots and site
  captures.
- Never put one client's material, names or numbers into another client's work or into
  this repo.
- Times a person reads are 12-hour with am/pm: `3:00 pm`, never `15:00`.

## Frameworks

`skills/lens/` reasons inside one framework at a time. Its 16 lenses sit over the corpora
in `knowledge/corpus/<name>/analysis/`. Pick the lens by the job:

| Job | Lenses |
|---|---|
| Offer and pricing | alex-hormozi, nate-herk, dan-koe |
| Cold outreach | josh-braun, eric-nowoslawski, christian-bonnier, nick-abraham, nicolas-gromer, alex-vacca, michel-lieben |
| Local-business marketing | adam-erhart |
| Sales video and funnel | ryan-mathews |
| Art direction | jason-murray, kole-jain |
| Running agents | simon-scrapes, rian-doris |

A lens cites its corpus and stops where its `gap-register.md` says the source is silent.

## Video

The video toolchain is Nate Herk's HyperFrames student kit. Setup is in `docs/SETUP.md`,
a full edit in `docs/WORKFLOW.md`. Before a creative session read `MOTION_PHILOSOPHY.md`
and the project's `DESIGN.md`; the project brief decides pacing, palette and type.
Per-project lessons live in `docs/learnings/`, and a finished project adds its file there.

| Need | Skill |
|---|---|
| New motion-graphics video from a brief | `make-a-video` |
| Full raw-video edit | `edit-video` |
| Reels, Shorts, short ads | `short-form-edit` |
| Brand reel cut to music | `motion-showreel` |
| A client's recurring drawn character | `build-character` |
| Silence removal, retakes | `cut-silences`, `cut-mistakes` |
| Narrative arc and callbacks | `video-storytelling` |
| Overlay beats and cards | `hyperframes-video-beats` |
| Styles and templates | `style-library` |
| Compositions, preview, render, animation | `hyperframes`, `hyperframes-cli`, `gsap` |
| Review a cut, then revise it | `review-video`, `revise-video` |

Video projects live in `video-projects/<client>/<video>/`, which git ignores along with all
media and renders.

## Where files come from

Most of this repo is exported from Christian's private system by a script, and the export
overwrites it. Change a skill, corpus, SOP or the brand there, never here. `README.md`,
`CLAUDE.md`, `business/` and `LICENSE` are written in this repo.
