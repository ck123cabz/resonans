# Rig layout

One folder per character, beside the series' reels (`<series>/rig/`), because every reel shares it. Leon's
(`video-projects/cryptoleon/survived-rugs/rig/`) is the example to copy and adapt. A shared library waits until a
third character needs the same code.

| File | Job |
|---|---|
| `spec.js` | every number and colour token, each with its pixel source |
| `shape.js` | the outlines (front, side, the face-and-belly patch) built from `spec.js` only |
| `arm.js` | the tapered limb, its pose table and how it mounts on the body |
| `parts.js` | accessories and the mouth (Leon: visor, beak states, crown) |
| `expr.js` | the expression table and the face parts it adds |
| `front.js`, `side.js` | the views, assembled from the files above |
| `paint.js` | shared filters, gradients and small drawing helpers |
| `sheets/*.html`, `*.js` | one check sheet per step |
| `sheets/render.sh` | headless Chrome to PNG: `./render.sh <sheet> <width> <height>` |
