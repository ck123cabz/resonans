---
job: tell
---
# Resonans reel, 8 October 2026

Project: `video-projects/resonans-reel/`. A 20.6 s 16:9 brand reel at 60 fps, 44 beats at 128 BPM, built from the Resonans design system and the motion-showreel grammar. Christian watched it build in the live studio.

- The brand's own rules cut into the showreel skill. No gradients or shadows, so the bloom, vignette and fringe were dropped; grain stayed. Sentence case except labels. One easing curve, `ease-settle`, written into `core.js` as a bisection of its cubic-bezier.
- Sand on the plate: 8,000 grains, paths built once at load (about a second) as Newton steps toward each grain's own small offset from f = 0, then every frame interpolates a table. For the lockup the grains were sampled from the rasterised mark path, so the sand forms the real mark.
- Hole wipes: `clip-path: path(evenodd, "M0 0H1920V1080H0Z M... a r r 0 1 0 ...")` opens a circle in the outgoing scene and renders in headless Chrome. The S3 to S4 wipe opens from the root colour chip.
- `hyperframes snapshot --at` takes seconds. I passed beat numbers twice and got the wrong chapters; beat n is n * 0.46875 s here.
- `hyperframes validate` flagged a mid-wipe frame as 1.08:1 contrast. A snapshot pixel sample showed the HUD was correct; sample the pixel before changing colours.
- The background studio was not running after the first render and validate; `preview --status <dir>` said so. It came back on port 3004. Check `--status` after renders when he is watching.
