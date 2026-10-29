---
type: corpus
aliases: ["Claude and AI workflows"]
corpus: ryan-mathews
layer: retrieval-index
tags: [machine]
source: skills/corpus-ingestion
created: 2026-10-08
generated: 2026-10-07
source_data: analysis/pass-1/lanes-5-7-offer-metrics-ai.md, inventory-tools.tsv, lane-8-sweep.md
---

# Claude and AI workflows

How Ryan uses Claude and other AI tools in his funnel work, with the prompts as he reads them on camera. 8 of his 21 videos from 2026 are about Claude or AI. Captions write Claude as "Cloud" or "Clawude" and Hormozi as "Ramoszi"; quotes keep the captions.

Two limits to carry into any use: his worked VSL-script example runs in a ChatGPT custom GPT, not Claude, and no transcript shows Claude writing a VSL script or building a static VSL page from scratch. [A]

Dates are YouTube upload dates. File paths are relative to `knowledge/corpus/ryan-mathews/.raw/`.

## Copy: the three-layer Claude skill stack

- **Type:** [AI]
- **Provenance:** [D]; the layer-1 idea [X:James, the Boring Marketer]
- **Date:** 2026-01-20
- **Source:** `video/how-i-built-claude-skills-that-write-perfect-sales-copy-step-by-step-t.md`
- Setup: Claude on the $20 plan, Anthropic's skill-creator skill, Wispr Flow dictation.
- Layer 1, foundation: an "elevated direct response copywriting" skill modeled on Hormozi, Codie Sanchez and Justin Welsh, with no fixed frameworks.
- Layer 2, tone: a tone profile built from about 50 pages of a client's transcripts, or a client questionnaire when they have no content.
- Layer 3, asset skills: e.g. a "sales page copy generator" trained on real pages. Frameworks (PAS and the like) live only here, so they never override layer 1.
- One generation prompt calls all three. Output is "80% 90% of the way there"; he edits it. He used it to redraft "20 something emails" for a client.
- Why: AI copy people "can smell it from a mile away it doesn't sound human".

## Layer 1 prompt: the elevated direct-response skill

- **Type:** [AI]
- **Provenance:** [D]
- **Date:** 2026-01-20
- **Source:** `video/how-i-built-claude-skills-that-write-perfect-sales-copy-step-by-step-t.md`
- Opening, as captioned: "hey Claude I just added the skill creator skill can you help me make an elevated direct response copyrightiting skill i want to model people like Alex Ramoszi Cody Sanchez Justin Welsh and other direct response goats".
- Continuation: "while avoiding a hypy fluff of some of the direct response people the skill should be able to use to write headlines VSSLs emails body copy etc".
- Constraint: "it should focus on the core principles of writing but avoid learning any concrete frameworks for writing".
- He then has Claude research the three writers' real copy. The principles that came back: specific outcomes, no hype or manipulation, authentic proof.

## Layer 2 prompt: the tone guide

- **Type:** [AI]
- **Provenance:** [D]
- **Date:** 2026-01-20
- **Source:** `video/how-i-built-claude-skills-that-write-perfect-sales-copy-step-by-step-t.md`
- He asks the finished layer-1 skill for its best prompt. It gave: "analyze this content and create a a refined tone guide for client name" then "extract their authentic voice but elevate it using the elevated direct response principles".
- Plus: if the tone is too corporate or boring, suggest how to make it more engaging while keeping its essence.
- Output: voice summary, dimensions (formality, energy, directness), dos, don'ts, forbidden words, real quotes. For himself he would make a Ryan tone profile skill.

## Layer 3 prompt: the sales page generator

- **Type:** [AI]
- **Provenance:** [D]
- **Date:** 2026-01-20
- **Source:** `video/how-i-built-claude-skills-that-write-perfect-sales-copy-step-by-step-t.md`
- Build prompt ends: "you're not going to add any elements you're not going to remove any elements you're going to learn the specific elements what do you need for me to get started".
- Feed it real pages through an HTML-to-text converter (Shot IQ, George Gammon). Add elements they lack (FAQ, guarantee, closing CTA).
- Inputs each run: tone profile, guarantee, testimonials, credibility markers, bonuses, full offer.
- Run prompt: "generate sales page copy for client name using the sales page generator copy skill read the skill and the elevator direct response style skill before writing" ("elevator" is the caption's "elevated").

## VSL script prompt (ChatGPT custom GPT)

- **Type:** [AI] / [VSL]
- **Provenance:** [D]
- **Date:** 2025-12-02
- **Source:** `video/how-to-create-a-1m-video-sales-letter-vsl.md`
- Shape: "Write a VSSL script using the model VSSL" + the model's structure + your business + "follow this exact framework" + "do not copy the wording learn from and model the structure and the principles behind why they are saying what they are saying" + offer details + the structure ("seven different pieces" from the model) + tone requirements + "generate a complete VSSL script following the structure exactly".
- Tone input: 5–10 YouTube transcripts in a TXT file. A client's self-described tone made the copy worse. It works best when the transcripts already contain good sales copy.
- Worked example: MSP Fuel, with Cole Gordon's transcribed VSL pasted in. The first draft "is just using too much of Cole's actual language", so he rewrote from scratch using the drafts as inspiration.
- The five-step process around it is in `vsl-scripts-and-beats.md`.

## Crowd copy: synthetic avatars review the copy

- **Type:** [AI]
- **Provenance:** [X:Justin Book], demoed at Greg Isenberg's January 2026 event on MindStudio; [D] for Ryan's Claude Code build
- **Date:** 2026-05-22
- **Source:** `video/this-agent-writes-ads-so-good-they-trigger-people-to-buy.md`
- Pick the buyers you want first; fill them in from won sales calls, surveys, reviews, testimonials and forum threads. Count: "i think somewhere around 8 to 12 is what the where the best results are going to come from"; more blows up the context window. Justin suggested 500.
- Each avatar answers: would you open, keep reading, click; your number-one remaining question; what keeps you from clicking; what would make you click faster. It scores the copy. A copywriter agent rewrites. Real results go back in.
- Cited support: Columbia Business School digital twins at "up to 88% accuracy" (2,000 people, 500 questions each).
- Result: Daniel (guitar, 159,000 subscribers) says his crowd-copy emails beat the one he wrote himself; "I actually get less hate mail". No revenue figure.

## Landing page audit: Claude Desktop + Microsoft Clarity

- **Type:** [AI]
- **Provenance:** [D]
- **Date:** 2026-05-01
- **Source:** `video/claude-just-changed-landing-pages-forever.md`
- Claude Desktop ($20 plan) → Customize → connect apps → Microsoft Clarity → paste the API token. Prompt: audit all pages with "/become-a-member" for things hurting conversion; then have it scope priority number two as a test.
- Claude split traffic by affiliate slug and read bounce, scroll depth, dead clicks and rage clicks.
- Before AI he watched about 100 recordings over lunch; that is how he once found a broken mobile Apple Pay that had cut a client's sales by two-thirds.

## Landing page audit: the page CRO skill in Claude Cowork

- **Type:** [AI]
- **Provenance:** [D]; the skill pack [X:Corey Haines] (captioned "Corey Haynes 31", GitHub user likely coreyhaines31, not confirmed in the corpus)
- **Date:** 2026-05-29
- **Source:** `video/claude-clarity-new-skill-insane-conversion-rates.md`
- Claude Cowork + the Clarity plugin + the free "marketing skills" GitHub pack. Prompt: "can you audit this is a client's website with the page CRO skill and Microsoft clarity plugin to find optimizations".
- Findings he liked: no risk reversal on a $239.88-a-year plan; anchor annual as $19.99 a month against $29.99 with a struck price; a "97.2% of members win more games" claim repeated five times; enlarge the yearly card.

## Where the Claude audit fails

- **Type:** [AI]
- **Provenance:** [D]
- **Date:** 2026-05-01; 2026-05-29
- **Source:** `video/claude-just-changed-landing-pages-forever.md`; `video/claude-clarity-new-skill-insane-conversion-rates.md`
- It reads code, not the render: it called a bright blue button dark, and reported placeholder cards no visitor sees. It over-indexed one PayPal rage-click session. It picked click-through to checkout as the main metric ("what matters is the stinking conversion rate"). It changed four things in one variant. It knows nothing of the business, past tests, ads or emails: "supplemental not a replacement yet". He suggests Playwright or screenshots for the visual problem.

## Vibe-coded funnel: $24K ARR, 12% of visitors bought

- **Type:** [AI] / [CASE]
- **Provenance:** [D]
- **Date:** 2026-07-23
- **Source:** `video/i-vibe-coded-a-sales-funnel-to-25k-arr-in-30-days.md`
- "in the first 30 days of launching I did about $24,000 in ARR and about half of that was upfront revenue". "12% of unique visitors into customers", a rate he has seen once before.
- Why: visitors try the product (a Duolingo-like speaking test) before paying; a plain sales page "would probably be converting half".
- Built entirely by Claude Code, kept on GitHub with skills and a CLAUDE.md. PostHog found the biggest drop-off step; Claude wired the Meta pixel and Conversions API. SEO posts came from James the Boring Marketer's skills.
- Three cons: 1 a steep learning curve, and for a plain sales-page-to-order-form info product "I don't think it's really worth it"; 2 you cannot see mistakes (the Resend email bug in `experiments-and-failures.md`); 3 security is on you: Anthropic's code-review and security-review skills set in CLAUDE.md to run before every push, plus Codex reviewing each push.
- He keeps old sites on GoHighLevel and builds new ones in Claude Code. Learning source he names: Nick Saraev's free 4-hour Claude Code course.

## AI audit lead magnet: Antigravity + Claude Code + Vercel + HighLevel

- **Type:** [AI]
- **Provenance:** [D]; the mini-offer idea [X:Hormozi]
- **Date:** 2026-03-11; 2026-04-23
- **Source:** `video/claude-code-antigravity-creates-insane-lead-magnets.md`; `video/alex-hormozi-s-lead-gen-strategy-but-make-it-ai.md`
- Google Antigravity with the Claude Code extension, Wispr Flow, plan mode. First prompt: "i want to build an airbnb audit tool the idea is people can come they can add their airbnb link to their listing and it will audit the pictures and description".
- Working prototype in about 20 minutes. Expertise goes in a skill (a markdown file).
- Security prompt: "can you audit the code for security risks so i don't know exactly what questions to ask but just think through ways that we could have security vulnerabilities extra costs".
- Ship: Vercel CLI → iframe on a HighLevel page → report link and an "audit ready" tag back into HighLevel → about five emails to the booking page.
- Model: "sonnet 4.6 cuz it's fast". Cost "10 to 30 cents" per funnel audit, 15–50 cents per Airbnb audit. He caps the API key at $20–30 and rate-limits the endpoint.
- Pricing choice: give it away if a service sits behind it, or charge $50–100 to filter tire kickers.

## Hormozi's ad strategy, automated

- **Type:** [AI]
- **Provenance:** [X:Hormozi] for the strategy; [D] for the pipeline and results
- **Date:** 2026-03-19
- **Source:** `video/how-i-automated-alex-hormozi-s-entire-ad-strategy-with-ai.md`
- Strategy: run top organic posts as ads with a banner, "just put a banner that says like click to to grab a thing".
- Pipeline: Instagram and Meta APIs → Hyros attribution → Gemini annotates video and on-screen text (because "sometimes the words don't even start for 5 seconds") → Claude Code builds a skill from winners vs losers → 10 ICP avatars review new scripts → 3 bodies × 10 hooks = 30 variations per shoot, up from 3 × 3.
- The avatars review newly written scripts, not organic posts.

## 2023: the all-AI course funnel with ChatGPT and Midjourney

- **Type:** [AI]
- **Provenance:** [D]
- **Date:** 2023-02-22; 2023-02-08
- **Source:** `video/repaired-transcript-i-built-an-entire-sales-funnel-using-chatgpt-midjo.md`; `video/how-to-use-chatgpt-to-build-a-1-000-000-online-course-step-by-step.md`
- ChatGPT outlined a course and wrote its sales page; Midjourney made images; built in 24 hours. His verdict: "Will this sales page work honestly probably not". AI copy was usable but lacked the context to pick the funnel type.
- Read this by date: the 2023 ChatGPT videos and the 2026 Claude builds are three years apart.

## Tools in the AI stack

- **Type:** [REF] / [AI]
- **Provenance:** [D]
- **Date:** 2026 videos as above
- **Source:** `analysis/pass-1/inventory-tools.tsv` (Pass 1 inventory)
- Claude Desktop and Cowork (he is on the $100 plan; Cowork needs at least $20), Claude Code, Google Antigravity, Gemini (video reading), Wispr Flow (captioned "Whisper Flow"), Vercel, GitHub, PostHog, Resend, Stripe, Microsoft Clarity, Hyros, MindStudio (Justin Book's build), the marketing-skills pack. Full entries in `people-and-tools.md`.
