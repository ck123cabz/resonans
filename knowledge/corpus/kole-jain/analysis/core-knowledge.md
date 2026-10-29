---
type: corpus
aliases: ["Core Knowledge: Kole Jain"]
corpus: kole-jain
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
---

# Core Knowledge: Kole Jain

**Corpus:** kole-jain
**Generated:** 2026-07-22
**Sources:** 151 signals across 43 NotebookLM extraction files (50-video notebook)
**Provenance:** Everything below is [S] (Gemini synthesis of Kole's spoken video content, Medium confidence) unless marked [I] for inferred. No first-order source exists yet, so nothing here has been confirmed in his own written words. When a concept repeats across many independently-asked questions, that repetition marks importance rather than confidence.

---

## The Mathematical Design System

Kole's core differentiator as a teacher is the claim that the things beginners eyeball are actually computable. Nearly every visual decision has a formula.

**Typography.** The scale starts at a 16px base and multiplies by the golden ratio, 1.62, per heading level. That escalates fast (a fourth-level header can hit 110px), so the system provides gentler multipliers: the square root of the golden ratio, 1.27, for subheadings, and the cube root for dense contexts like dashboards and mobile. The cube root value is never stated in the corpus; computed, it's about 1.17 [I].

Line height moves opposite to size. Paragraphs sit around 150% so text can breathe. Headings tighten to 110-130% as they grow, and whenever he wants the "super pro" look he lands in 110-120%. Kerning follows the same logic: above 70-80px, default letter spacing reads loose, so he tightens by -2% to -4%, staying nearer -2% to -3% when subtle. Treat 110-120% line height and -2% starting kerning as the canonical targets; the wider ranges are tolerance.

Constraints do the rest of the typographic work. One high-quality sans serif covers 90% of projects. Two font weights, two text colors (primary at 100% opacity, secondary at 45-70%), at most six font sizes on a landing page. Dashboard text rarely exceeds 24px because density wins there.

For responsive text he skips breakpoints entirely with a fluid interpolation: `MinFontSize + (MaxFontSize - MinFontSize) * ((CurrentScreenWidth - MinScreenWidth) / (MaxScreenWidth - MinScreenWidth))`, bounded between 320px and 1920px screen widths and wrapped in clamp() so text never leaves its size envelope.

**Spacing.** Everything is a multiple of 4, because multiples of 4 halve cleanly. He changes Figma's nudge from the default 10px to 8px so arrow-key adjustments stay on grid. Dashboards follow the grid strictly; landing pages run a 12-column grid that drops to 8 on tablet and 4 on mobile. The hero has its own named rule, 8-12-32: 8px between heading and subtext, 12px between eyebrow and heading, 32px between the text block and the CTAs. The general principle behind all of it is that distance is meaning. People read closeness as relatedness, so whitespace replaces dividers and containers.

Component-level ratios: button width roughly double its height. Chip vertical padding at a half or a quarter of horizontal (20px across, 10px down). And never nest a card inside a card. "Padding on padding" is his most-repeated spacing sin; group with whitespace instead of another box.

**Radius and depth.** Nested corners follow one formula: inner radius equals outer radius minus the gap between the two corners. A 30px outer with 10px padding gives a 20px inner. Pills are the exception, keeping uniform distance around the curve. For the premium squircle finish, max out iOS Corner Smoothing in Figma. Shadows: blur runs 1.3 to 2 times the Y-offset, X stays at or below Y, and Figma's default 25% opacity drops to 15-20%. Dashboard pop-ups get light gray shadows rather than transparent black.

## Color: The 4-Layer Doctrine

Kole's most explicit contrarian position: the 60-30-10 rule (60% dominant neutral, 30% secondary, 10% accent) is fine for beginner landing pages and "ruins" product design. His evidence is observational. Real products don't follow it; Vercel is roughly 90% black, 8% white, 2% red. Pushing a brand color to 30% coverage creates noise on unimportant elements, fails contrast checks on big saturated areas, and forces semantic errors like a purple delete button.

His replacement has four layers:

**Layer 1, Neutral Foundation.** At least four background layers, two strokes, and three text variants. The follow-up extraction recovered the actual values: main background at 98-100% white (Notion runs 100%, Vercel 98%); sidebar as the anchor at ~96% white with a 2% brand tint (Mercury adds 2% blue); cards pure white against off-white backgrounds, or sidebar-toned when the background is white; interactive elements around 90-95% white. Borders are 85% white, never thin black lines. Text runs 11% white for headings, 15-20% for body, 30-40% for subtext. A landing page only needs three to five neutrals; the full stack is for product UI.

**Layer 2, Functional Accent.** The brand color as a 50-950 ramp rather than one swatch: 500/600 for primary actions, 700 for hover, 400/500 for links.

**Layer 3, Semantic Communication.** Red is destructive, green is success, yellow is warning, blue is trust. Always, even when red isn't a brand color. Icons stay colorless except when color signals status.

**Layer 4, Theming.** A mathematical OKLCH transform: take the neutral hex values into OKLCH, drop lightness 0.03, raise chroma 0.02, shift hue to the brand color. Perceived weight stays constant whether the theme is yellow or blue.

Ramp construction happens in HSB, not hex: each darker step adds ~20 saturation and drops ~10 brightness, with an advanced hue shift toward blue/purple when darkening and yellow/red when lightening, because those hues read naturally darker and lighter. For chart palettes he moves to OKLCH, fixing lightness and chroma and stepping hue 25-30 points per series color so every chart color carries equal visual weight.

**Dark mode gets rebuilt, not inverted.** Dark colors look more alike to the eye, so his "double the distance" rule applies: a 2% layer separation in light mode becomes 4-6% in dark. Elevation flips to lightness. Raised surfaces are always 4-6% lighter than what they sit on, and shadows mostly retire. The base is a very dark version of the accent (a bluish black), never pure #000000. His refinement hack: take the dark background, bump HSB Brightness up 4-6 points and drop Saturation 10-20 points to build the next layer up.

## Progressive Disclosure and Invisible UI

Twelve signals across ten separately-asked questions hit this doctrine, spanning dashboards, mobile, macOS, landing pages, AI products, and motion. Treat it as the anchor.

The core rule: show only what the moment requires, and sequence everything else. Filters hide until requested. Secondary actions (delete, share, copy) live in popovers and hover reveals, never in the permanent UI. Complex forms collapse "Advanced Options" by default. The "spectrum of explicitness" governs the decisions: global, primary actions earn permanent visibility; contextual, secondary actions hide until hover or swipe.

Invisible UI is the craft layer that makes interfaces feel professional without announcing itself:

- **Optimistic UI.** Assume server success and update instantly. Gmail deletes the email from view before the server confirms, so the app feels fast because the interface never waits.
- **Four states minimum** on every interactive element: default, hovered, active/pressed, disabled. Mobile has no hover, so everything needs a slightly darker press state instead.
- **Empty states that invite action** ("Start saving inspiration"), never blank screens. The full-screen empty state pointing at the plus button is the professional version.
- **Signifiers.** Press states, active highlights, tooltips on ambiguous icons: cues that show what the UI affords without instructions.
- **Immediate feedback on everything.** Every scroll, swipe, and click gets an instant state change confirming it registered.

One thing worth knowing here: progressive disclosure is simultaneously his prescribed treatment for AI products and his go-to example of what AI design generators cannot do. The two fit together. The judgment AI lacks is exactly what he sells, and it's where a design agent applying this corpus has to work hardest.

## Data Drives Form

His dashboard doctrine reduces to one sentence: the shape of the data dictates the component. Numbers in tables right-align so digits stack by place value. Long strings truncate to protect breathing room. Categories and statuses render as chips instead of plain text. Time-series data never goes in a table; it becomes a timeline. Tables themselves are tools, not displays, so search, filter, and sort live in view.

Charts stay boring on purpose. Curved trend lines hide where data actually lands, so curvature goes off. Horizontal grid lines, clear axis numbers, legends, and a time-scale selector are the whole kit. Decorative chart styling (rounded bar tops, gradient fills) is a beginner tell.

The sidebar is "the spine of the product": navigation and search, profile management at the top where the logo usually goes, related links grouped, rarely-used items like settings and help at the bottom, collapsible with the active state still visible. A dashboard that shows everything at once looks like someone "emptied a drawer onto the screen." The drawer metaphor is his shorthand for skipped progressive disclosure.

## The Redesign Method

His redesign process, consistent across the Google AI, Spotify Wrapped, skincare, finance dashboard, and Fisker projects, runs in five moves:

1. **Kill list.** Four failure categories: redundancy (duplicate pages and features get merged or deleted), corporate jargon (replaced by ~7-word headers and ~14-word subtext), useless ornamentation (mismatched icons, harsh default shadows, decorative shapes), and friction (interactions that fight the user, like Spotify's click-to-next reel replaced with vertical scroll).
2. **Benchmark.** Steal patterns, not designs, from gold-standard companies like Apple, Tesla, and Chrome. Mood-board with Mobin. The recurring skeleton he finds everywhere is the four-zone landing structure: navbar, main text block, stats, image.
3. **Structural overhaul.** Important content moves higher and further left. Dense repetitive lists become Bento grids or clickable multisections. Layout monotony breaks via "breaking the box": elements overlapping containers or bleeding off-frame, arranged to pull the eye toward page center. On mobile, one screen does one thing, and bottom sheets beat new pages.
4. **Visual refinement.** Neutral backgrounds so content shines, type tightening on large text, and image tracing (cutting out the subject so text can layer behind it).
5. **Invisible UI.** The hover states, loading confirmations, and progressive disclosure that make it feel finished.

For learning, he inverts standard advice: redesigning an app you like is "pretty bad advice." Clone professional designs exactly instead, because cloning forces you to notice the details a creative redesign glosses over: exact padding, nav heights, font sizes. Quantity breeds quality. Taste changes so fast in the first two months that early portfolios get scrapped anyway.

## Design Psychology

The named laws he actually operates with:

- **Hick's Law:** decision time grows with options. His application is the one-CTA rule (below) and TikTok's single-action interface.
- **Fitts's Law:** reach time depends on target size and distance. On mobile that means 44px minimum touch targets near the thumb's rest position, bottom-right for the right-handed majority.
- **Proximity:** closeness reads as relatedness. Whitespace is the separator; lines and containers are usually redundant.
- **Aesthetics-usability effect:** attractive designs are perceived as easier to use, which buys trust, patience with flaws, and time-on-site. He also deploys this one as a sales argument for craft.

His TikTok breakdown is the applied case study: one interaction (swipe up) eliminates decisions, the swipe target is effectively the whole screen at zero thumb travel, right-side icons serve the 70-80% right-handed population, and 37-second average videos beat YouTube's 11.7 minutes on the breadth-over-depth principle. His gamification work (the Duolingo-to-finance-app mapping: currency, streaks, local leaderboards, quiz-gated lessons) carries its own boundary rule: rewards must map to the user's real goals or nobody cares.

There is an unresolved tension here. The gamification material warns that engagement mechanics tip "captivating into chaotic," while the TikTok material celebrates deliberately addictive design and says to apply its lessons. The corpus never draws the ethics line. His implicit boundary appears to be user-goal alignment: mechanics that serve what the user came to do are fine, and he simply never addresses attention-farming beyond admiring its craft [I]. An agent using this corpus should run the user-goal test and set the TikTok admiration aside.

## The Beginner-Tell Diagnostic

The corpus contains at least six overlapping mistake inventories (color mistakes, beginner screams, vibe-code tells, element upgrades, mobile mistakes, case-study tells). Merged, the canonical diagnostic reads as follows, each tell with its fix:

- Emojis used as icons → one professional library (Phosphor, Lucide, or Feather), one stroke weight, sized to the font's line height.
- Harsh default shadows → light gray, high blur, 15-20% opacity.
- Bright uncoordinated palettes, brand color everywhere → neutral foundation, color moved into functional micro-charts and status.
- Pure #000000 / #FFFFFF → functional grays (11% headings, 30-40% subtext).
- Placeholder text as the only label → labels above inputs, examples pre-filled.
- Curved chart lines and rounded bar tops → straight lines, grid lines, legends.
- Padding on padding → whitespace grouping, no nested cards.
- Repeated KPI blocks → layout variety: two-column grids, donut charts, maps.
- Lorem ipsum → real or AI-drafted copy that carries the product's narrative. (Stand-in logos like Logo Ipsum are fine; the ban covers narrative text, not furniture [I].)
- Mismatched icon sets and drifting corner radii → measurement variables, one standard radius.
- Missing states → four states on everything interactive; press states on mobile.
- Navigation arrows on swipeable sections → delete them; show position (dots, timers), never direction.
- Vague corporate copy → ~7 words per header, ~14 per subtext, outcomes over features ("turn data into decisions," not "analyzes data").

## Motion, With Restraint

The full effect specs live in the retrieval index; what belongs in core knowledge is the governor. Animation is justified by purpose (clarity, feedback, or guidance toward an action) and killed by cost: anything that slows load, hijacks scroll, or gates content behind a long preloader goes. Looped ambient effects stay minimal and slow. Easing is never linear, because nothing in the physical world moves linearly; bounce and exponential curves are the default. His signature curve is expo.inOut, cubic-bezier(0.87, 0, 0.13, 1) in CSS.

His captivating-versus-chaotic boundary never gets a numeric threshold. The working heuristic the corpus supports: motion tied to a user action or state change may carry personality (bounce, shimmer); ambient motion the user didn't cause must stay quiet; and when two animated elements compete for attention, one of them is wrong [I]. Direction carries meaning too. Slide up from the bottom signals a temporary surface, slide in from the left signals progress through a flow.

## Identity: Product Designer Over UI Designer

UI design is decorating a room; product design is designing the house, meaning the flow, the function, the wiring. UI is "flavor," a restylable skin over the product's logic. The professional marker is designing every state (empty, loading, error, success) where beginners design only the happy path. This identity claim is the thesis under everything else in the corpus.

His four self-check questions: How did the user get here and what do they need next? What's the minimum UI that lets the content shine? Does this design do anything the previous version didn't? And for portfolios: if I was the one hiring me, would I?

The business framing follows. Designers are problem solvers, and most client problems reduce to needing more customers, so genius design shows up as ROI in sales, sign-ups, or donations. Niche by problem, not industry. Build for the end user rather than the client's taste.

His four non-negotiables, stated as such:

1. **One primary CTA per layout.** A second button loses its background or drops opacity. Apple and Google ship one main action for a reason.
2. **Every action gets immediate feedback.** Hover, press, optimistic updates. No awkward pauses.
3. **No lorem ipsum, ever.** Copy carries the product's narrative even in fake projects.
4. **Presentation is half the design.** Mockups, realistic contexts, and glow treatments build client confidence in work they can't otherwise evaluate.

The last one explains a corpus-wide pattern: he spends as much effort teaching how to present design (device mockups, AI-generated lived-in scenes, exploded screenshots, zoomed crops for dashboards) as how to produce it. "Design looks better when it's presented" is load-bearing. The same artifact reads as amateur or premium depending on its frame.
