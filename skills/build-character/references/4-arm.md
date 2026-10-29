# Step 4: Arm

## Grill

- Which poses do the reels need (from the step 1 answer)? Name each one and its action.
- Do arms reaching toward the camera foreshorten? Leon: yes for hold, clasp and chin (Christian, 24 Oct).

## Build

- `rig/arm.js`: one tapered limb, wide at the root and narrowing to a rounded tip (Lil Pudgys: 0.32 W to 0.15 W over
  0.6 W). The top edge runs straight, the underside bulges a little.
- It pivots at the body side under the shoulder dip. A pose is a shoulder angle, a bend, a foreshortening and a layer.
  Every pose yields the same path commands, so poses morph without a pop.
- Back-layer poses draw behind the body, so the body outline hides the join. Front-layer poses pivot at the body
  edge, draw clipped to the body, and get the body outline redrawn round the shoulder.

## Sheet

Every pose in grey on the body, the taper alone with its widths, and one pose in red over a target frame that shows it.

## Checks

- Report the pivot-to-tip reach of every pose in numbers. Leon's side arm was drawn at 72% once; Christian caught
  it by eye. One arm length in every view; only foreshortened poses read shorter.
- A patch of body colour over a buried root paints a disc wherever the body under it is not one colour (it covered
  the bib corner). Clip and redraw the outline instead.
- A rounded ellipse reads wrong; the show's arm tapers from shoulder to tip.
