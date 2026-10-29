# Step 6: Poses

## Grill

- For each action the reels need, which pose and which body pose (stand, at a desk, reclined, sitting up)?

## Build

- Front poses come from `arm.js`; side poses are their own table in `side.js`. Body poses turn the whole figure
  about a point on its base: a Lil Pudgys character sits and lies on its body.
- `sheets/posesheet.js`: every front pose, every side pose and every body pose at one scale.

## Sheet

The pose sheet. Then the fresh reader.

## Checks

- Side arms are not clipped to the body: a forward reach must pass the belly. Hide the root under a body-colour pad
  placed where the body is that one colour.
- A pose that hangs (rest, slump) keeps gravity when the body turns: take the body's rotation off the shoulder angle.
- A held object stays in front of the face at chest height; Leon's lift first put his flipper into his visor.
- Poses that differ only slightly read as the same pose. Push them apart until the reader can tell them apart.
