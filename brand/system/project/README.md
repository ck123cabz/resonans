Resonans is a demand generation agency run by Christian Cabaluna and Sai. It takes what a business means, builds the brand kit and the assets that say it, and posts them until buyers answer. This system is how Resonans itself looks and sounds.

## The idea every value comes from

An orchestra tunes to one note before it plays: A at 440 Hz. Resonans does the same job for a business and its buyers, so the whole system is built from that note and the chord on top of it.

- The A major chord is three pitches in the ratio 4 : 5 : 6. Those ratios set the type sizes, the spacing, the line heights and the durations.
- Raise a pitch 40 octaves and it becomes visible light. 440 Hz becomes 620 nm, 550 Hz becomes 496 nm and 660 Hz becomes 413 nm. Those 3 wavelengths are the 3 hues.
- The mark is the figure sand makes on a square plate ringing in mode 1, 5.

If a new value is needed, derive it from one of those 3 sources. Do not add a value that has no source.

| Decision | Value | Where it comes from |
|---|---|---|
| Brand hue | `root`, 620 nm | A, 440 Hz, raised 40 octaves |
| Success hue | `third`, 496 nm | C sharp, 550 Hz, the chord's third |
| Link and focus hue | `fifth`, 413 nm | E, 660 Hz, the chord's fifth |
| Warning hue | `offkey`, 581 nm | B flat, 469 Hz, a minor second above A: the harshest interval against the root |
| Error hue | `clip` | the root hue at lower lightness: the root note driven too hard |
| Neutrals | `ground` to `ink` | the root hue at a chroma of 0.02 or less |
| Type sizes | 16px times 5/4 per step | the major third, 5 : 4 |
| Body line height | 1.5 | the perfect fifth, 3 : 2 |
| Spacing | 4px times 1, 2, 3, 4, 6, 8, 12, 16, 24 | partials built from 2 and 3 only, so neighbours are an octave, a fifth or a fourth apart |
| Durations | 120, 180, 270, 405 ms | each a fifth longer, times 3/2 |
| Easing | `ease-settle` | passes the target by 4% and returns, like a struck plate settling |
| Stroke of mark and letters | 16 units on an x-height of 100 | one weight for both |
| Round button ends | `radius-round` | the letters' stroke ends in a half circle |

## Voice

Write as a person who has run the numbers and is on the client's side. Christian's own lines set the rules.

- **Sell the result.** On 30 Sep 2026 he put it as "selling the process versus selling the results". Lead with the count and the date: "7 of 10 pairs registered by 26 Oct". Mention a tool only when a client asks how.
- **State the offer as a count.** "3 posts a day and 2 videos a week", never "social media management".
- **Say the free offer in his words.** "Free until we get you your first customer."
- **Use the buyer's words.** Lift phrases from reviews, comments and calls, and write the post in those phrases. That match is the resonance the name refers to.
- **Be the thinking partner.** His 3 Oct note says "we would be their thinking partner, we would help care for their company". Write "we" for Resonans and "you" for the client.
- **No generic AI pictures.** The same note records people boycotting restaurants that post "the generic AI poster". Every image shows the client's real place, product or people.

Three contrast pairs hold the tone:

1. Plain, and still exact. Give the number.
2. Warm, and still brief. Open with 1 sentence of care and follow it with the next step.
3. Confident about the method, modest about the forecast. Promise the work and the count of posts; report the customers as they arrive.

Generate the voice from 1 belief: automating a message nobody answers only sends it faster. Get the message answered first, then automate it.

Write in sentence case. Use digits for every number, ₱10,000 for pesos and 26 Oct 2026 for dates. Use no emoji and no exclamation marks. English by default; a client's own Bisaya or Tagalog phrase stays as they said it.

The tuning words (`root`, `third`, `offkey`, `clip`) are names for tokens. Do not show them to a client. A client reads "Posted", "Needs a photo" and "Failed".

## Colour

Two themes: **Air** is the light theme and the default. **Still** is the dark theme, for screens and decks.

- Set the page in `ground`. Raise cards and fields to `ground-raised`. Sink wells and table heads to `ground-sunken`.
- Set copy in `ink` and captions in `ink-soft`. Use `ink-faint` only for placeholders and disabled labels.
- Use `root` once per layout: the mark, the key number, or the one action the page exists for. A layout with 2 `root` elements has no emphasis.
- Main actions are `ink`, with `ground` text. Links and the focus ring are `fifth`.
- Status is always a word first. `third` repeats "done", `offkey` repeats "needs attention", `clip` repeats "failed". Each also has its own mark: round, square, diamond.
- For coloured text use the `-ink` token (`root-ink`, `third-ink`). For text on a fill use the `on-` token. For a tinted background use the `-wash` token with its `-ink`.
- Every text pair holds 4.5 to 1 in both themes and `ink` holds 7 to 1. Fills and control borders hold 3 to 1.
- Use no gradients: every colour is one flat field.

## Type

Three families, each with one job.

- **Jost** for display: `display`, `headline`, `title`, `subtitle`, at weight 500. Its letters are built from a circle and a stem, the same parts as the wordmark.
- **Atkinson Hyperlegible Next** for reading: `lead`, `body`, `body-strong`, `small`. The Braille Institute drew it so each letter is hard to mistake for another.
- **Atkinson Hyperlegible Mono** for numbers and labels: `readout`, `data`, `label`.

Sizes step by a major third from 16px: 12.8, 16, 20, 25, 31.25, 48.83, 76.29. Do not set a size between steps. Line height is 1.5 for reading, 1.25 for titles, 1.125 for `headline` and 1 for `display` and `readout`. Keep running copy near 65 characters a line. Set labels in uppercase with 0.08em tracking; set nothing else in uppercase.

## Space, shape and stroke

- Space comes from `space-1` to `space-24` only. Inside a component use `space-1` to `space-6`. Between sections use `space-12` to `space-24`.
- Controls are 48px tall (`space-12`), so a field and a button line up.
- Buttons and pills take `radius-round`. Fields and notices take `radius-2`. Cards take `radius-3`. Tags take `radius-1`.
- Lines are `stroke-hair`. Focus and emphasis are `stroke-firm`.
- There are no drop shadows. Show height with `ground-raised` and a `line` hairline.

## Motion

Use `ease-settle` for every transition, with `time-1` for a press, `time-2` for a field, `time-3` for a card or notice and `time-4` for a page-level move. Things arrive, pass their place by 4% and come back. Nothing loops and nothing bounces twice. Under reduced motion, skip the move and show the end state.

## Logo

The files are in `assets/Logos/`. Read the note there before placing one.

- Use `lockup-horizontal` first. Use `lockup-stacked` in square spaces and `mark` alone at 48px and above.
- At 32px and under use `mark-small`, which has a stroke of 24 units where `mark` has 16.
- Keep clear space of half the mark's width on every side.
- The `-ink` files go on `ground` and on light photos. The `-air` files go on `ink`, on `root` and on dark photos. `mark-root` goes on `ground` or `ink` only.
- Do not stretch, outline, recolour or redraw the mark. Do not set the word "resonans" in Jost in place of the wordmark.

## Pattern

`assets/Patterns/` holds 6 figures of the same plate: modes 1, 3 up to 5, 7. Mode 1, 5 is the mark's own figure. Use one pattern per piece, cropped large, in `ink` at 8% to 12% on `ground`, or in `ground-raised` on `ink`. Never place type over the dense middle of a pattern.

## Iconography

Resonans has no icon set yet. Status uses 3 drawn shapes: a round dot, a square and a diamond. Arrows in copy are the text characters ▲ and ▼ with a word beside them. If a layout needs an icon, use a text label until a set is chosen.

## Layout

Lay pages on a 12-column grid with `space-6` gutters, 4 columns on phones. Align everything left; centre only a cover or a title slide. Put the result first: a page opens with its Readouts, then the explanation.
