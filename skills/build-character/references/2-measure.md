# Step 2: Measure

## Grill

- Which part of the target goes on the identity's character where they differ (Leon: the show's arms and body, his
  visor and crown)?
- Any trait that must keep its own size against the show, and why (Leon's beak became 0.18 W, larger than the show's
  0.12 W, because with the eyes hidden it is his only mouth)?

## Build

- The unit is the head's widest width, W, set to 600 rig units. The origin is the eye line's centre.
- Crop each part with a pixel grid and read edges by hand at 3x zoom. At 640x360 an automatic dark-pixel scan
  returned noise.
- Read the outline as half-widths every 0.08 W from the top of the head to the base.
- Write every number into `rig/spec.js` with the frame and pixels it came from in the comment beside it.

## Sheet

The grid crops with the readings written on them.

## Checks

- Name the part before measuring it. At 47 s two "arms" were backpacks; zoom in and confirm the part first.
- Measure each part on two characters or two frames before trusting it (the arm at 52 s: pink 0.47 W, blue 0.49 W).
- Never state a ratio before measuring it. The head-to-body split was guessed at 60% in the grill; the frames said 44%.
- A part hidden behind something (the shoulder dip under backpack straps) is an estimate read from the edges above
  and below; label it so in `spec.js` and on every sheet.
