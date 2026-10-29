# Step 1: Sources

## Grill

- Which existing show or art is the **style target**? Offer the closest match you can find to the client's art, with
  a frame of each.
- Which file is the **identity source**, and which traits does it give (colours, accessories, clothing, marks)?
- What must the character do across the reels (sit at a desk, hold a glass, lie in a lounger)? This fixes which
  poses step 6 builds.
- Which views do the reels need? Front and side only, or more?

## Build

- Download the style target (ask before any download: filename, source, size) into
  `scratchpads/<target>-ref/episode/` and pull a contact sheet every 2 s: `ffmpeg -i ep.mp4 -vf "fps=1/2,scale=320:-1,tile=6x9" -frames:v 1 sheet.jpg`.
- Pick frames where a character of the target stands straight-on, full body, with nothing over its outline. Save
  each one used into `rig/sheets/` under a name that carries its timestamp (`lilpudgys-f30.png`).
- Save the identity source into `rig/sheets/` as well.
- Start the character's brief (`<series>/<CHARACTER>-RIG-BRIEF.md`) with both sources and every grill answer.

## Sheet

The contact sheet with the chosen frames marked, and the identity source beside it.

## Checks

- The identity source never supplies a size. Leon's avatar did for eight passes and every pass drifted.
- Prefer a frame where the character faces the camera square. A 3/4 turn moves the face off-centre and makes every
  horizontal reading unreliable (the pink penguin at 52 s).
