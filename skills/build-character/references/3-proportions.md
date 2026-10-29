# Step 3: Proportions

## Grill

- The grey diagram first: does any proportion look wrong to the user against the target, before any colour?

## Build

- `rig/shape.js` draws the outline as one smooth curve through the measured points, mirrored for a straight-on front.
  The side view takes the same heights; its depth comes from a profile frame, or is an estimate (SKILL.md, missing view).
- `sheets/diagram.html`: the identity source, the style target, the grey front and the grey side at one head width,
  with dashed guide lines for top, eye line, shoulder dip, bib or waist, belly, base and feet.
- `sheets/overlay.html`: the onion skin, the outline in red over the target frame at its scale.

## Sheet

The diagram and the onion skin.

## Checks

- Zoom the onion skin on the head. Leon's first outline sat on the frame at belly and base but drew a rounded box
  where the show draws a round dome; re-reading the head edge every 0.08 W fixed it.
- Every guide line must hit the same feature on the target frame. If one misses, the reading is wrong, not the line.
