---
type: tool
aliases: ["Video, image and design tools"]
corpus: nate-herk
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-09-29
name: Video, image and design tools
speaker: Nate Herk
provenance: D
sources: [q18, q30, q38, q41]
videos: [claude-just-destroyed-every-video-editing-tool.md, claude-heygen-just-changed-content-creation-forever.md, this-one-gpt-6-astra-skill-replaces-your-higgsfield-subscription.md, build-sell-with-codex-5-hour-course.md, create-anything-with-sora-2-n8n-ai-agents-full-beginner-s-guide.md, build-sell-grok-bots-2-hour-course.md, claude-design-2-hour-course-beginner-to-pro.md, gpt-6-astra-finally-kills-ai-website-slop.md, build-sell-ai-saas-products-2-hour-course.md]
---

# Video, image and design tools

The tools behind Nate Herk's video pipelines and design work, with the prices he states. The pipelines themselves (steps, prompts, QA loops) are in `build-video-editing-pipelines.md`. Caption spellings to expect: "Cedance" or "Cance" for Seedance, "Cling" for Kling, "key.ai" or "Key AI" for a credit marketplace that is probably kie.ai.

## Hyperframes replaced Remotion in April 2026
`[T] · [D] · uploaded 2026-04-18 · claude-just-destroyed-every-video-editing-tool.md · q30 · version-bound`

Hyperframes has the model write HTML, CSS and JS animations, then renders them to MP4 with Puppeteer and FFmpeg. Remotion does the same with React. He switched three days after using Remotion on a HeyGen edit (2026-04-15):

> hyperframes which is kind of like a better version of remotion if you guys have seen that it's a little bit more setup but it's way more powerful (claude-just-destroyed-every-video-editing-tool.md)

His reason, per q30 [M]: models iterate on and visually check HTML faster than React. Remotion's last caption mention is 2026-05-05; Hyperframes runs in 19 captions to 2026-09-25. Rendering is free locally. q30's token cost for a full run (120k to 400k tokens, $7 to $18 via API) is [M].

## HeyGen avatars: Creator plan about $30
`[T] · [D] · uploaded 2026-04-15 · claude-heygen-just-changed-content-creation-forever.md · q30, q38 · version-bound`

> the production stack on a creator plan of hey gen it's going to cost you about 30 bucks a month and that is going to give you only a limited amount of avatar 5 generations (claude-heygen-just-changed-content-creation-forever.md)

He keeps clips to about a minute because longer voice audio drifts:

> once you push past about a minute of audio it starts to degrade and it starts to sound less and less like you (claude-heygen-just-changed-content-creation-forever.md)

q30's API rate (about $4 a generated minute) and per-video total ($40 to $50 for 10 minutes against $300 for a human editor) are [M].

## ElevenLabs voice: $22 for about 100 minutes
`[T] · [D] · uploaded 2026-04-15 · claude-heygen-just-changed-content-creation-forever.md · q30, q38 · version-bound`

> the 11 labs creator plan the 22 bucks a month plan is going to give you roughly 100 minutes of audio (claude-heygen-just-changed-content-creation-forever.md)

He uses it for the voice clone in avatar videos and for word-level transcripts in Hyperframes edits. Whisper is the local alternative. The $5 Starter plan in q38 is [M].

## Higgsfield: Seedance 2.5 locked behind a $60 plan
`[T] · [D] · uploaded 2026-09-18 · this-one-gpt-6-astra-skill-replaces-your-higgsfield-subscription.md · q30, q38 · version-bound`

Higgsfield connects Claude to many video and image models through MCP or CLI, with Marketing Studio templates for UGC ads and product reveals. His complaint is the subscription:

> if you wanted to use cedance 2.5 you had to be on a 60 bucks a month plan and you still had a limited number of c[redits] (this-one-gpt-6-astra-skill-replaces-your-higgsfield-subscription.md)

On 2026-09-18 he replaced it with an Astra skill calling models per clip. His whole test run cost $7.40.

## Per-clip prices: Seedance 2.5 $3.23, Kling 3.0, MiniMax
`[T] · [D] · uploaded 2026-09-18 · this-one-gpt-6-astra-skill-replaces-your-higgsfield-subscription.md · q30 · version-bound`

> so this was cedance 2.5 and it was $3.23 (this-one-gpt-6-astra-skill-replaces-your-higgsfield-subscription.md)

Seedance 2.5 gave the best UGC realism with sound. Kling 3.0 is captioned "60s" and MiniMax "a$110"; the likely values are $0.60 and $1.10 but the captions are garbled, so treat them as unresolved. The sizzle reel's "1755 based on my credits" has unclear units. "Cance costs 5x Cling" is Gemini's arithmetic. Small package text still warps in video models.

## key.ai: Sora 2 at 1.5 cents a second
`[T] · [D] · uploaded 2025-10-22 · create-anything-with-sora-2-n8n-ai-agents-full-beginner-s-guide.md · q30, q38, q41 · version-bound`

A pay-per-credit marketplace for image and video models, free to sign up.

> charging you 10 cents per second of sora 2 video generation whereas keys only charging you 1.5 cents per second so it's six times cheaper (create-anything-with-sora-2-n8n-ai-agents-full-beginner-s-guide.md)

A 10-second Sora 2 clip is about $0.15. He also routes Nano Banana 2, GPT Image 2 and Seedance 2.0 through it. The Seedance 2.0 cost of $0.20 to $0.50 per 10-second clip and Nano Banana's $0.04 to $0.12 per image are [M].

## Seedance 2.0 loops for scroll sites
`[T] · [M] · no transcript · q30 · version-bound`

[M] Gemini's version only; no caption carries this text. Generate a clean 16:9 start frame in Nano Banana 2 or GPT Image 2, give Seedance the same start and end frame for a 10-second loop, extract 100 to 120 WebP frames with FFmpeg, and bind them to scroll. Web backgrounds cap around 15 seconds and 30 to 40 MB; 10-second clips loop tighter.

## GPT Image 2 is the reason to use Codex for visuals
`[T] · [D] · uploaded 2026-08-10 · build-sell-ai-saas-products-2-hour-course.md · q16, q18 · version-bound`

> i'm going to be using codeex for this because it has gpt image 2 (build-sell-ai-saas-products-2-hour-course.md)

Claude Code has no native image model. He also sends Claude Design's brand text spec to GPT Image 2 to render a brand sheet.

## Claude Design: the "Figma killer" and its usage cost
`[T] · [D] · uploaded 2026-04-30 · claude-design-2-hour-course-beginner-to-pro.md · q18 · version-bound`

Anthropic's standalone design surface on Opus 4.7, for design systems, decks, prototypes and launch videos.

> a lot of people when this was released was calling it the figma killer (claude-design-2-hour-course-beginner-to-pro.md)

It draws on your plan's limits:

> on a $200 a month plan for max that design system took about 6% of my session limit already (claude-design-2-hour-course-beginner-to-pro.md)

That was before Anthropic doubled limits on 2026-05-07.

## Claude Design: build the design system first
`[J] · [M] · uploaded 2026-04-30 · claude-design-2-hour-course-beginner-to-pro.md · q18 · stable`

[M] Gemini's version only; no caption carries this text. Feed a site URL, GitHub repo, brand guide or logos, and it writes a `design.md` with type scale, hex palette and component styles. A published system is reused team-wide. q18's six rules: do strategy and outlines in normal chat and paste clean markdown in; reference hex codes and URLs instead of saying "modern"; build the system first; one structural change per prompt; use the Tweaks panel and direct edits for small fixes; start a fresh project when history gets long.

## The 110,000-token prompt is the tool's number
`[R] · [D] · uploaded 2026-04-30 · claude-design-2-hour-course-beginner-to-pro.md · q18 · version-bound`

> it says start a new chat to save 110,000 tokens of context (claude-design-2-hour-course-beginner-to-pro.md)

Claude Design's own interface says this and he reads it out. It is not a threshold he set.

## Hand off from Claude Design to Claude Code
`[B] · [M] · uploaded 2026-04-30 · claude-design-2-hour-course-beginner-to-pro.md · q18 · version-bound`

[M] Gemini's version only; no caption carries this text. Share, then "Hand off to Claude Code", or download a zip with `index.html`, CSS, `design.md` and assets. Paste the handoff command into Claude Code, wire any back end or n8n webhook, then prompt: "Push this project to a private GitHub repository and deploy it to Vercel."

## Design king: GPT-6 Astra, September 4
`[T] · [D] · uploaded 2026-09-04 · gpt-6-astra-finally-kills-ai-website-slop.md · q34 · version-bound`

> we have a new ai design king and it's not even close take a look at some of these outputs i've been getting with astra (gpt-6-astra-finally-kills-ai-website-slop.md)

The crown went to Astra, not Fable 5.1.
