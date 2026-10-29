---
type: corpus
aliases: ["Component Patterns -- Kole Jain"]
corpus: kole-jain
layer: analysis
tags: [machine]
source: skills/corpus-ingestion
created: 2026-07-28
---

# Component Patterns -- Kole Jain

**Corpus:** kole-jain
**Generated:** 2026-07-22

---

## Dashboard Ruleset

**When to use:** Any data-dense app screen: admin panels, analytics views, internal tools.

### Data formatting

- Right-align every number in a table or list so digits stack by place value; left-aligned table numbers are a beginner tell.
- Truncate long text strings to protect breathing room.
- Categories and statuses render as chips (pill containers), never plain text.
- A table is a tool, not a display: give users search, filter, and sort in-view.
- Event-sequence data gets a timeline, not a sorted table.

### Sidebar as the spine

The sidebar holds the persistent, globally relevant elements: navigation and search. Profile management goes at the top instead of the customary logo, so user identity is immediately clear. Nav links pair a recognizable icon with a short title; group related links, push rarely used items (settings, help) to the bottom. Collapsible, with the active state still visible when collapsed (colored rectangle or icon highlight).

### The 3 flaws that expose inexperience

1. Data doesn't drive the form; the layout reads like someone emptied a drawer onto the screen.
2. No progressive disclosure. Secondary actions (delete user, copy cell) belong in popovers or hover reveals, not on-screen at once.
3. Missing invisible UI: tooltips on ambiguous icons, hover-state indicators, empty states that guide users when no data exists.

### Six-step build

1. Establish the sidebar to anchor navigation.
2. Define a text scale smaller and tighter than landing-page type; dashboard text rarely exceeds 24px.
3. Lay out a strict, simple grid (two-column, two-row works), most important info at top.
4. Charts get horizontal grid lines, clear axis numbers, and date selectors; curved trend lines off, they hide where points land.
5. Modals for complex blocking tasks, popovers for non-blocking settings. Follow a modal with a confirming toast.
6. Toast notifications plus Optimistic UI (remove a deleted item before the server confirms) for snappiness.

**Provenance:** [S] (NotebookLM synthesis)

## Mobile UI Ruleset

**When to use:** Phone-first screens and mobile breakpoints; mobile is its own environment, not shrunken desktop.

### Navigation conventions

- Bottom bar: maximum five links, three or four ideal.
- When high-level links won't fit, the sidebar becomes a dedicated homepage listing them as a vertical menu.
- Navigation is contextual; the bottom bar can disappear inside a note editor to make room for task tools.
- Bottom sheets instead of new pages for temporary tasks (template or filter selection). Keeps the user in context, one-handed.

### Touch ergonomics

Every interactive element gets at least a 44-pixel touch target. Fitts's Law: make targets large and put them near the thumb's resting position, bottom-right for right-handed users. Screens are narrow, so increase vertical spacing between stacked content more than feels natural. Type runs larger on mobile: iOS base font is 17px versus 13px on macOS.

### Gestures

- Swipe right from the left edge for back; swipe down dismisses popovers, modals, and bottom sheets.
- Irreversible actions (buying crypto, high-value email) get a swipe-to-confirm slider, not a button.
- Long-press is mobile's right-click: blur the screen, slightly zoom the held element, reveal a contextual menu.
- One Direction rule: a section scrolls vertically or horizontally, never both.
- Swipe animations need bounce and momentum, never linear easing.

### Mistakes that scream beginner

Double-nested cards ("padding on padding" wastes width). Desktop type scales. Cramming a dashboard into one view; one screen does one thing, new features get a new page or bottom sheet. Arrows left on swipeable sections (the gesture is understood). No press states: without hover, every element needs a slightly darker-gray press state. Skipping the full-screen empty state pointing to the plus button.

**Provenance:** [S] (NotebookLM synthesis)

## Landing Page: The 4 Levels Ladder

**When to use:** Scoping or pricing a SaaS landing page, or diagnosing a page's tier and its next upgrade.

- **Level 1, "The Template," $500, 2/10.** Markers: repetitive text-left/image-right alternation, generic stock images, long vague text blocks with weak hierarchy, flat menus with identical links and no standout CTA.
- **Upgrade 1 to 2:** modern stacked hero, actual product screenshots instead of stock, shorter headlines, outlined or highlighted CTAs, centered menu, simple load animations.
- **Level 2, "The Visual Identity," $2,000, 6/10.** Cohesive brand, real screenshots, stacked hero.
- **Upgrade 2 to 3 (UI design to product design):** add social proof (badges, logos), Bento grids for varied information density, interactive multi-sections with clickable tabs or sliders.
- **Level 3, "The Crafted Experience," $6,000-$10,000, 8/10.** Markers: zoomed-in product shots curating what the user sees, not whole screens; vertical lines framing content (helps responsiveness); a mega menu that reveals depth; fluid slider transitions; subtle hover effects.
- **Upgrade 3 to 4 (mostly copy and motion detail):** shift messaging from what the product does to how it helps. Outcome-value copy like "turn data into decisions" instead of "analyzing data."
- **Level 4, "The Masterpiece," above $10,000, 10/10.** Markers: expertly curated images and color threaded through the page, mega menu content that bumps out smoothly sideways, blur during transitions, CTAs that appear only on hover.

**Provenance:** [S] (NotebookLM synthesis)

## Landing Section Patterns

**When to use:** Composing individual landing sections, hero first.

### The 4-zone hero

Almost every high-end landing page reduces to four zones: navbar, main text block, image, stats/social proof. Copy: exactly 7 words in the header, 14 in the subtext. Never obstruct the image's focal point; image center or right, text left or below in its dead space.

The 8-12-32 rule: 8px heading to subtext (tightest association), 12px eyebrow to heading, 32px text block to CTA buttons. Large hero type: letter spacing -2% to -3%, line height 110-120%.

### Section inventory

- Logo marquee: on 41 of 50 top software sites; the high-end version is a marquee animation with progressive blur fading the edges.
- Clickable multisection with tabs or sliders for complex products (Miro, MongoDB).
- Bento layout (Apple): varied box sizes with room to breathe.
- Straight line grid with visible grid lines (Vercel) for a technical feel.
- Images inside large nav dropdowns, a 2025 trend.
- Text wipe/interlude: a thin cropped photo plus one line of text as a spacer between text-heavy areas.
- Stacked rounded cards on a contrasting dark background.

**Provenance:** [S] (NotebookLM synthesis)

## Layout Systems

**When to use:** Choosing overall page structure before designing sections.

### The 7 modern layouts

From 50 top software landing pages: 1) logo marquee/section (41 of 50 sites); 2) big text and big image, punchy headline over a large product screenshot with heavy whitespace; 3) clickable multisection tabs; 4) simple, tasteful animations, hover and scroll over complex 3D that slows the site; 5) Bento; 6) straight line grid with visible lines; 7) images in the nav.

### Bento rules

Reach for Bento when information density is high and features would get lost in a standard list. Keep the grid simple so it stays responsive and easy to build. Box sizes are driven by the content plan, not decided first.

### Breaking the box

Elements that overlap sections or extend outside the frame make static layouts feel dynamic and 3D. Shift cards slightly up or down to suggest movement, let card sections bleed off the screen edge, trace or mask an image subject so text sits behind the focal point. Arrange overlaps to pull the eye toward page center.

Also worth holding: one-column vertical stacking (Apple's move, one feature in focus at a time) and ultrawide split-screen halves (image left, text right, common on beauty and luxury sites).

**Provenance:** [S] (NotebookLM synthesis)

## macOS Native Design

**When to use:** Desktop apps meant to feel Apple-native; the app acts as a seamless part of the system, not a destination.

### Architecture

Three-part layout following Apple's utility apps (Finder, Notes, Reminders): top bar for global actions, sidebar as the navigation spine, center content area. Traffic lights integrate into the top bar or sidebar.

### Measurements and conventions

- Keep the top 50 pixels of the window largely free of interactive elements so users can drag it.
- macOS base font size is 13px; iOS is 17px. Mobile-adjacent Apple designs keep the 44px minimum touch target.
- Native feel depends on standard shortcuts: Command+Space (search), Command+Tab (switching), Command+W (closing), Command+Shift+S (quick actions/saving).

### Materials and interaction

Native background blur ("vibrancy") makes the window feel integrated with the desktop. Dark mode is not an inversion of light mode; dark colors read as more similar to the eye, so it needs greater differentiation between colors. Empty states invite action ("Start saving inspiration"), never a blank screen. Optimistic UI throughout: Apple Mail trashes an email before the server deletes it. Progressive disclosure hides advanced features until useful. Every interaction gets immediate feedback via micro-animations or state changes (a window collapsing into a toast). Support drag-and-drop in and out (Figma, Finder), and keep search prominent.

**Provenance:** [S] (NotebookLM synthesis)

## Core Component Rules

**When to use:** Any individual control; the per-element defaults.

### Buttons

Width roughly double the height. Four states minimum: default, hovered, active/pressed, disabled. Primary actions get the brand color; secondary actions are ghost buttons (border only, or no background until hover). Destructive actions are always red, even if red isn't a brand color. High-end hover feel comes from small effects, text sliding up or a circle scaling behind the label.

### Forms and inputs

Placeholder text is never the only label; labels sit above inputs so they stay visible while typing. Inputs need a focus state on click and error states (red border plus message) on failed validation. Pre-fill empty fields with real examples of the expected data. For complex forms, collapse advanced options by default.

### Cards and chips

Chip vertical padding is 1/2 to 1/4 of horizontal (e.g. 20px horizontal, 10px vertical); enforce with Auto Layout. Never nest a card inside a card. Depth differs by mode: light mode uses shadows at 15-20% opacity with high blur; dark mode raises a card by making it slightly lighter than the background, no shadow. Within a card, group by importance, name and location above secondary details like ratings.

### The 9 crucial upgrades

1. Mobile tab bar: align icons, label obscure ones, drop protruding "add" buttons into the bar.
2. Charts: curved data lines off (they obscure values); add horizontal grid lines and a legend.
3. UI cards: overlay smooth gradients on images so white text reads.
4. Pricing cards: CTA at top without a background, checkmarks not bullets.
5. Stickers: 12-point stars, quirky display fonts, full-opacity offset shadows.
6. Signup modals: example states plus labels above fields.
7. Footers: centered 3-5 links for small sites, not a multi-column grid.
8. Chips: hold the vertical-to-horizontal padding ratio.
9. Carousels: navigation dots plus an extended circle timer showing when the image changes.

**Provenance:** [S] (NotebookLM synthesis)
