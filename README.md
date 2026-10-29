# Resonans

Resonans is a small marketing agency run from Claude Code. Christian Cabaluna and Sai started it in
October 2026 to act as the marketing department for small businesses in the US, Australia,
Canada and the UK, video first. This repo is the agency itself: the skills that do the work,
the frameworks they reason from, the brand system and the video toolchain.

There is no app yet. You open the repo in Claude Code and run a stage of the pipeline as a
skill.

## The pipeline

Each client moves through the same stages. Resonans runs every stage on itself first, as
client zero, and writes the SOP while doing it.

| Stage | What happens | Skill |
|---|---|---|
| Offer | Which package, for whom, at what promise | `lens` (alex-hormozi, nate-herk) |
| Outreach | Cold message with a public audit, content strategy and keyword research; follow-ups on days 1, 4 and 8 | `lens` (josh-braun, eric-nowoslawski, christian-bonnier, nick-abraham) |
| Brief | Insight, idea, then two or three visual ingredients | `creative-grill`, `visual-techniques` |
| Script | Sales video, explainer or reel script with screen directions | `writing-video-scripts` |
| Character | A client's recurring drawn character, rigged to a style target | `build-character` |
| Production | Edit, cut, motion graphics and render in HyperFrames | `make-a-video`, `edit-video`, `short-form-edit`, `motion-showreel` and the kit skills |
| Review | Timestamped review of a cut, then the revision pass | `review-video`, `revise-video` |
| Operations | Turn a finished stage into an SOP someone else can run cold | `write-sop` |
| Learning | Get fluent in a new tool before a client needs it | `immerse` |

The audit skill, the monthly client report and lead capture are not built yet; they come
after Christian and Sai read the first send run on 8 Nov 2026.

## What's in here

```
skills/            every skill, linked into .claude/skills/ so Claude Code finds them
knowledge/corpus/  16 analysed marketing corpora (core knowledge, retrieval index, gap register)
04-resources/sops/ the SOP standard and the SOPs written so far
brand/             the Resonans logo work and design tokens (Python builds)
business/          the offer and the plan
scripts/           video kit scripts, the writing linter, the SOP checker
docs/              video kit setup, workflow and per-project learnings
style-library/     motion styles the video skills pick from
```

The `lens` skill reasons inside one framework at a time and cites it. Each corpus was built
from a creator's own videos and posts in three passes, and this repo holds the final layer
of each.

Every piece of prose the skills write goes through `scripts/ai_slop_lint.py`, a linter
for phrases and sentence shapes that read as machine-written. Run it on any file:

```
python3 scripts/ai_slop_lint.py <file>
```

## Setup

1. Node 22 or later, Python 3.11 or later, FFmpeg.
2. `npm install`, then `npm run setup` and `npm run preflight`.
3. Copy `.env.example` to `.env` and fill only the keys your workflow needs
   (`docs/TOOLS-AND-API-KEYS.md`).
4. Open the folder in Claude Code and name a stage, for example `/creative-grill`.

## Where it comes from

Christian runs a private Claude Code system for his own work. Resonans is exported from it
by a script that copies the business layer, rewrites private names and refuses to finish
if any leak is left. Files here are regenerated on each export; `README.md`, `CLAUDE.md`,
`business/` and `LICENSE` are written here.

The video toolchain is Nate Herk's HyperFrames student kit (MIT, `licenses/video-kit-LICENSE`).
The HyperFrames skills come from `heygen-com/hyperframes` (`skills-lock.json`). Third-party
notices are in `THIRD_PARTY_NOTICES.md`.
