---
type: corpus
aliases: ["Motion Kit -- Kole Jain"]
corpus: kole-jain
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
---

# Motion Kit -- Kole Jain

**Corpus:** kole-jain
**Generated:** 2026-07-22

---

Consolidated motion reference. Each signature effect appears 3-4 times across the corpus (Figma spec, build recipe, code port, deployment guidance); merged here into one canonical spec each. Single NotebookLM source, all provenance [S].

## The Custom Exponential Curve (shared foundation)

The curve behind the signature entrance effects. In Figma he selects a custom bezier in the prototyping panel and hand-drags the handles, "dragging out these handles... to give us more of an exponential curve." No numeric handle coordinates appear in the source. The motion starts very slowly, accelerates rapidly in the middle, and decelerates hard at the end. In code he always uses GSAP `expo.inOut`. The CSS mapping is `cubic-bezier(0.87, 0, 0.13, 1)` -- note this is the canonical easeInOutExpo value and may be NotebookLM supplying the standard mapping rather than an on-screen number. Confirmed durations on this curve: 800ms loading slide-up, 400ms navbar bar expansion, 700ms text wipe. Springs (636/24, 550/40) are a separate category, never interchangeable with this curve.

**Provenance:** [S]

## Loading Slide-Up

Full-screen black preloader that slides up to reveal the page. Figma build: black rectangle with logo placed directly over the dashboard content; nudge the content underneath down slightly in frame one, so when the preloader exits upward the content slides up into final position with it. Settings: trigger after-delay 1000ms, Smart Animate, 800ms duration, custom bezier exponential. A nav bar fade-in follows: delay 100ms, 200ms duration, Ease In and Out.

Code port: preloader at `position: fixed` with a high z-index. Fade the logo container to `opacity: 1`, then move the whole loading section to `y%: -100%`. Use the GSAP `"<"` position parameter so the content slide-up starts concurrently with the preloader exit.

Deploy when large background videos or 3D effects genuinely need an extra second to load. Keep it short; the restraint rules below cap preloaders.

**Provenance:** [S]

## Expanding Navbar

Dot-to-circle-to-bar entrance in three steps. Step 1: a 1x1px transparent dot expands into a 53x53px circle (after-delay 1ms, Smart Animate, Ease In/Out, 300ms). Step 2: the circle stretches into a full bar, roughly 500px wide (after-delay 1ms, Smart Animate, custom bezier exponential, 400ms). Step 3: icons and logo fade in (after-delay 1ms, Smart Animate, Ease In/Out, 200ms per element).

Code port: `stagger: 0.2` animates the nav links one by one in place of the per-element fades. Use `gsap.getProperty()` to read the container height in pixels and set the starting `max-width` from it, so the element begins as a perfect circle at any screen size.

Deploy primarily as a landing-page entrance. Also works as progressive disclosure inside apps, like a search icon that expands into a full search bar only when clicked, keeping the UI minimal until needed.

**Provenance:** [S]

## Text Wipe

A thin rectangle sweeps across text so it appears drawn or revealed. Figma build: 1px-wide rectangle as tall as the text, with the text used as a mask. Slide the rectangle across; when it covers the text, toggle the text to 100% opacity. Reveal wipe and exit wipe are both after-delay 1ms, Smart Animate, custom bezier exponential, 700ms each.

Code port: absolutely-positioned "text-wipe" container over the text at `width: 0%`. Animate to 100%, toggle text opacity, then flip the wipe's CSS to `right: 0` / `left: auto` before animating width back to 0% so it exits the opposite side.

Deploy on landing to make a site feel premium immediately, or as a spacer/interlude between two text-heavy sections, paired with a thin cropped photo.

**Provenance:** [S]

## Spring Interactions Table

Springs are the interactive-feedback category, distinct from the exponential bezier used for entrances.

| Interaction | Trigger | Duration/Delay | Spring or curve |
|---|---|---|---|
| Name tag pop-up (also cited as success message/toast) | Hover | 500ms | Stiffness 636, dampening 24 |
| Spinning loader ("connecting" states) | After-delay 300ms | -- | Stiffness 550, dampening 40 |
| Success checkmark slide-in | After-delay 300ms | -- | Ease Out |
| Delayed tooltips | Mouse enter / mouse leave | 1000ms delay | Custom easing, high bounce |

Build notes. Name tag: nudged down at 0% opacity in frame one, up at 100% on hover, Smart Animate with custom easing. Spinner: four frames rotating the icon 180 degrees incrementally on the custom spring. The tooltip delay is the point of the pattern; 1000ms keeps tooltips off casual hovers.

**Provenance:** [S]

## Micro-Interaction Inventory

- **Button hover mask:** text mask so the label slides up and a second label replaces it. Click is a While Pressing scale-down for tactile feedback, no color change.
- **Search bar expansion:** magnifying-glass icon expands into a full input field on click.
- **Progress bar:** a stroke masked to a sliding rectangle, so the bar "draws" in as the rectangle moves along the path.
- **Card swipe:** rotate the top card out of frame to 0% opacity while the cards behind scale up and shift down to fill the space. Used in notification centers.
- **Shimmer stroke:** build the outline as a subtract boolean of two rectangles, then rotate a circle carrying an angular gradient continuously behind it for a shimmering border.
- **Highlight-on-scroll:** stack a two-color gradient closely, use the text as a mask, animate a colored rectangle across based on scroll position. Right for scrollytelling and portfolios where you want attention on specific phrases without chaotic movement.
- **Optimistic UI deletion:** Gmail-style, item vanishes instantly assuming server success.
- **AI-product set:** skeleton loading with shimmer placeholders, a "research trail" of status lines ("searching docs," "extracting quotes") fading in one by one, and word-by-word streaming that turns server delay into anticipation.

In his redesign process this inventory is the final "invisible UI" layer: micro-animations confirming actions, progressive disclosure protecting the happy path, optimistic UI for perceived speed.

**Provenance:** [S]

## Swipe Taxonomy

The source splits mobile swipes into three categories.

**Within-page navigation** (carousels): linear easing feels rigid, so use easing curves with bounce for natural momentum. Advanced moves: skew cards toward the screen edges for a 3D ring / "spool of data" illusion; treat the display edge as a horizon that shrinks approaching elements, paired with circular swipe motion; magnetic-feeling page indicators that react to the swipe instead of static dots.

**Between-page navigation:** the core rule is directional continuity -- new content and background must follow the swipe direction. Patterns: a card expands to full-screen while background and new content fade in, finished with an elastic snap at the top (recipe app example); onboarding circle expansion, one circle growing huge to push old content out, a new circle shrinking down to bring the next content in; image zooming, a list image zooming in to become the next page's hero.

**Functional gestures:** swipe down dismisses sheets, popovers, and modals; sell it by zooming out and moving the background down slightly when the popover opens, reversing on dismiss. Swipe-to-confirm replaces buttons with a horizontal slider for irreversible actions (sending email, buying crypto). iOS back gesture: current screen slides right while the background moves left by 35%. Swipe left on a list item reveals Delete/Share actions that would otherwise clutter the UI. Long-press is mobile's right-click: blur the screen, slightly zoom the element, reveal a contextual menu.

The "One Direction" rule governs all of it: a section scrolls either vertically or horizontally, never both. Swipe animations always carry bounce and momentum, never linear easing.

**Provenance:** [S]

## Scroll and Ambient Effects

- **Morphing:** an image or video transforms as the user scrolls; a small side asset morphs into a large background element or the next section. Use it when raw assets are weak ("kind of ass") and need to look premium, or as an entrance sequence, like a video reel morphing into large display text.
- **Margin parallax:** doodles or illustrations in spacious margins moving at a different rate than the scroll. Gives a lifelike 3D feel without complex layered backgrounds.
- **Preloader justification:** the slide-up entrance earns its place only when large background videos or 3D effects need the extra load second. Otherwise it is dead weight.

**Provenance:** [S]

## Figma Mechanics

- **Matching Names Rule:** Smart Animate only animates a property change when the layer names are identical between Before and After frames. Different names just cross-fade.
- **Layer opacity, not fill opacity:** hide elements with the layer opacity control (top-right panel), not fill opacity (bottom-right); transitions come out more consistent.
- **8px nudge:** change Figma's default nudge from 10 to 8 pixels so every animation move stays on the 4-point grid.

**Provenance:** [S]

## GSAP Technique Kit

The workflow: prototype the happy path in Figma first to lock the motion, then build the static final-state HTML/CSS, define starting states with CSS or `gsap.set()` (e.g. `opacity: 0`, `y%: 100`), create `gsap.timeline({ paused: true })`, chain with `.to()`/`.fromTo()`, fire with `.play()`.

- **`expo.inOut`** is the code equivalent of the Figma custom exponential bezier.
- **`"<"` position parameter** on a `.to()` call starts it concurrently with the previous tween (content slides up while the preloader exits).
- **`stagger: 0.2`** animates lists like navbar links one by one.
- **`gsap.getProperty()`** reads container height in pixels to set a starting `max-width`, so an expanding navbar begins as a perfect circle at any screen size.
- **Percentage transforms** (`y%`/`x%`) over pixel values, so motion scales across viewports.
- For layout scaffolding he occasionally uses Matter (by JetBrains) or Dualite to generate base front-end code from Figma links or screenshots. AI covers the skeleton; the GSAP motion work stays manual.

**Provenance:** [S]

## Restraint Constraints

When not to animate, and the rules that keep motion tasteful. Usability is the heart of design; motion supports clarity or it goes.

- **Performance:** if an animation makes the site load slower or navigation harder, it is not worth the visual payoff. Cut it.
- **Purposeless motion:** no clarity, no functionality, no guidance toward an action means it should be removed. Big or flashy animation is a beginner tell.
- **Long preloaders:** they buy asset-load time but users are impatient; intricate preloaders that gate real content are counterproductive.
- **Scrolljacking:** anything interfering with natural scroll gets used very sparingly, if at all.
- **Looped effects:** vertical marquees and similar loops stay minimal and slow so content remains readable.
- **Situational motion:** direction carries meaning. Slide up from the bottom signals a temporary action; slide in from the left signals progress in a flow.
- **Never linear easing:** real things speed up and slow down, so use bounce curves for a lifelike feel. This applies everywhere, from carousels to functional gestures.
- **Captivating vs chaotic:** captivating design guides the eye with restraint, simple grids, and motion that rewards interaction (an expanding modal, a subtle hover). Chaos is complex shapes, too many components, and complexity for its own sake; it competes for attention and lands as uninspiring or sterile.
- **Immediate feedback and progressive disclosure** apply as motion principles too: every interaction gets an instant state change, and animation reveals functionality only when the moment requires it (the search bar that expands on trigger).

**Provenance:** [S]
