---
type: corpus
aliases: ["AI Workflow -- Kole Jain"]
corpus: kole-jain
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
---

# AI Workflow -- Kole Jain

**Corpus:** kole-jain
**Generated:** 2026-07-22

---

## The Vibe-Coding Chain

Five stages, each tool with one job:

1. **Claude** is the core engine. Multipurpose LLM, but recent updates made it exceptionally good at writing code for UI components.
2. **21st.dev** is a library of UI components built for or by AI. Copy exact code or prompt snippets from it straight into Claude.
3. **HTML to Design** (Figma plugin) is the bridge, converting Claude's code into an editable Figma design.
4. **Figma refinement** is the human stage: fixing fonts, alignment, color contrast, rebuilding weak sections by hand.
5. **Production bridges** take the refined design back to code. Builder.io acts as an AI front-end engineer that understands existing codebases and design systems, iterating on Figma designs visually inside the code. Matter (by JetBrains) prototypes Figma designs into live, sharable previews for web and native Mac apps. Dualite Alpha turns a Figma link into a functional web app in under two minutes.

One boundary he keeps: AI covers the layout skeleton, GSAP motion work stays manual.

**When to use:** Any time a working UI is needed fast without hand-coding it.

**Provenance:** [S] (S118, S61, S126)

## The Four-Part Prompt Structure for UI Generation

Kole's prompting structure for Claude, in order:

1. **Define output format.** Explicitly request HTML and CSS. Mandatory if the result is going to Figma later.
2. **State purpose and context.** Give the intended use so the AI understands the functional logic, e.g. "a project management dashboard to track ongoing projects."
3. **Request specific elements.** List exactly what you need: a sidebar with icons, a Gantt chart with colorful bars.
4. **Enforce a professional icon library.** Name Lucide or Phosphor outright so the AI doesn't default to emojis, a major beginner tell.

The benchmark trick: upload a screenshot of a high-end site like Linear along with the prompt, giving Claude a stylistic benchmark to emulate.

**When to use:** Every Claude UI generation. Skipping part 1 breaks the Figma export; skipping part 4 guarantees emoji icons.

**Provenance:** [S] (S119)

## The Claude-to-Figma Import Procedure

1. Download the generated code from Claude as an HTML file.
2. Open the HTML to Design plugin in Figma and go to the "File" tab.
3. Toggle the "hover effects" setting on before running, which yields a more interactive imported design.
4. Drag and drop the HTML file into the plugin.

Manual fixes after import are essentially guaranteed: fonts, alignment, and color contrast almost always need hand-fixing.

**When to use:** After any Claude UI generation that needs to become an editable design rather than throwaway code.

**Provenance:** [S] (S120)

## Known Breakdown Points

Where the workflow fails and what he does about it.

**Detail dropping.** Claude struggles to see small, nuanced details in complex reference images (Dribbble shots especially) and simply excludes them from the generated code.

**The five vibe-code tells, each with its fix:**

| Tell | Fix |
|---|---|
| Emojis as icons | Swap for Phosphor or Lucide; consistent stroke width reads as production-ready |
| Bright, uncoordinated palettes (fail accessibility, look cheap) | Neutral grays, dark greens, or purple-grays for backgrounds; move color into micro-charts and data viz |
| Same four KPIs repeated across a small app | Vary layout: two-column grids, maps or shaded regions instead of bar charts; collapse redundant links into a triple-dot menu or popover |
| Sparse input fields crammed into flyouts | Use a modal for complex tasks; collapse "Advanced Options" by default so the layout scales |
| Disorganized billing pages (too many plans, e.g. five, confusing pricing) | Cut to 3 or 4 plans, enlarge the cost figure, doughnut charts for usage, show the actual discount or what the next plan adds |

**No progressive disclosure.** AI layouts come out sterile, showing every button at once instead of tucking secondary actions into a popover or hover state.

**Vague verbose copy.** His targets are roughly 7-word headers and roughly 14-word subtext.

**Sections he nukes and rebuilds.** Billing plans and boring bar charts get deleted entirely and rebuilt with doughnut charts or maps. Not worth salvaging.

The underlying rule: AI sets up logic well but lacks craft. Alignment, fonts, and hierarchy get fixed by hand or the design feels sterile.

**When to use:** As a review checklist on any AI-generated UI before it ships or reaches a client.

**Provenance:** [S] (S121, S122, S123, S124, S77)

## The 7 Unicorn AI Startup Components

Kole's framework for the modern AI-product interface, each with its design treatment:

1. **Giant prompt box.** A control panel rather than a plain input field. Context-taking chips for modes (brainstorm, data, email), deep-integration buttons for Google Drive, GitHub, or Figma, an advanced-mode toggle with real-time token cost estimates, and input compression that collapses large pastes like code blocks into clean viewable blocks.
2. **Generation history.** A record of what happened, built for retrievability. Vertical list by session (ChatGPT-style) or tied to the original document blocks (Notion AI style), with search and short previews. Should work as a workspace instead of a waste basket.
3. **Memory panel.** A record of what matters, as distinct from history. Persistent and accessible rather than buried in settings; exposes the AI's "brain" with visible storage space, bulk delete, and manual addition of key facts.
4. **Inline AI editing.** Compact selectors directly under paragraphs or on text highlight. Contextual buttons like "improve writing" and "fix spelling," plus keyboard shortcuts so refinement feels like real-time revision instead of full regeneration.
5. **Research trails.** Animated steps ("searching docs," "extracting quotes," "drafting answer") fading in one by one, plus retrieved documents and cited sources. Makes the product read as a collaborator instead of a black box.
6. **Real-time feedback.** Word-by-word streaming (the "trickle" effect), skeleton loading with shimmer showing exactly where images or text will land, and fluid loading indicators like Notion's three bouncing dots or Claude's rotating star.
7. **Confidence indicators.** A pill-shaped bar directly below the response, labeled "high confidence" or "unverified." Clicking reveals the model's numeric confidence value, e.g. 97%.

**When to use:** Designing or auditing any AI-product interface; this is the component vocabulary for the category.

**Provenance:** [S] (S113, S114, S115, S116, S50)

## AI-Product Micro-Patterns

The small moves that make generation feel collaborative rather than static:

- **Skeleton shimmer:** placeholder blocks with a shimmer animation so the layout feels alive while content generates.
- **Research trails:** small status animations fading in one by one, exposing the thought process mid-generation.
- **Streaming:** word-by-word output converts server delay into anticipation.
- **Confidence pills:** the pill bar with a percentage score ("97% confident") as lightweight trust signaling.
- **Dark soft glass recipe:** dark backgrounds, striking gradients, a one-pixel border carrying a soft inner shadow, background blur, and a gentle shimmer animation on top. The named signature that separates the high-end AI look from a plain dark theme.

**When to use:** Pull individually when an AI product feels static or untrustworthy during generation states.

**Provenance:** [S] (S54, S116, S117, S50)

## AI Mockup Generation

He calls AI the gold standard for high-end custom product mockups and "lived-in" lifestyle environments; they build client confidence. Roughly 30-word prompts, fed to an AI image generator. The green screen gets punched out in Figma and the UI skewed into the frame.

The two verbatim prompts:

> "MacBook Air green screen on screen on an orange faux leather padded chair notebook and stool in background background blurred soft shadows moody lighting natural lived in"

> "minimal concrete cylinders with small cracks beige living room with water stain"

The six-part prompt structure behind them:

1. **Core product:** a modern Apple device (MacBook Air, iPad, Apple Watch).
2. **Screen state:** the phrase "green screen on screen," enabling the Figma punch-out.
3. **Surface and setting:** exactly what the device sits on ("orange faux leather padded chair").
4. **Lived-in background elements:** grounding details ("notebook and stool in background").
5. **Lighting and depth:** "background blurred," "soft shadows," "moody lighting."
6. **Imperfections:** water stains, small cracks. The flaws sell the authenticity.

**When to use:** Presenting UI work to clients; any time a design needs a realistic scene instead of a flat frame.

**Provenance:** [S] (S150, S151, S126)

## Where AI Helps vs Where Craft Wins

Core position: AI is an accelerant for technical execution and prototyping. It handles the heavy lifting of building layouts, but it can't "design the entire house" (the flow, the function, how every part of the system connects, grounded in user intent and business outcomes).

**AI genuinely helps in five lanes:** rapid prototyping via vibe coding (functional UI code from prompts or screenshots); visual assets (the mockup workflow above); research via Mobin, searching thousands of real-world UI patterns and auto-generating mood boards; production bridges (Builder.io, Matter) that respect an existing design system; and drafting realistic copy, research trails, and docs instead of Lorem Ipsum.

**Human craft still wins on four fronts:** intricate detail and refinement (AI excludes details that are too complex; humans fix fonts, alignment, spacing); detecting beginner tells like emoji icons, repeated KPIs, and sterile "corporate AI mush"; progressive disclosure, since AI shows every feature at once and can't sequence functionality; and strategic problem solving that ties design decisions to user intent and business outcomes.

**When to use:** Deciding what to delegate to AI on a given project, and framing AI's role for clients or stakeholders.

**Provenance:** [S] (S125, S126, S127)

## What Designers Must Learn

His forward-looking prescription, four items:

1. Work in "AI adjacent fields," treating AI as a collaborator instead of a black box.
2. Master the LLM-to-Figma bridge: generate code in an LLM, pull it back through HTML to Design, refine manually.
3. Learn advanced prompting, specifically the 30-word prompt method for mockups.
4. As AI cheapens the aesthetic/UI side, double down on Product Design: hidden UI, state changes (loading, error, success), meaningful flows, and the invisible UI AI typically omits (tooltips, optimistic feedback, contextual hover states).

**When to use:** Career-direction questions, or prioritizing which skills to build next.

**Provenance:** [S] (S128)
