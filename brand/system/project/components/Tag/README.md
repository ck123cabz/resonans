A short status word with a dot. Use class `rs-tag` on a `span`.

**You provide** one or two plain words: "Posted", "Needs a photo".

| Class | Hue | Means | Dot |
|---|---|---|---|
| `rs-tag` | neutral | not started, draft | round |
| `rs-tag--fifth` | `fifth` | planned, information | round |
| `rs-tag--third` | `third` | done, arrived | round |
| `rs-tag--offkey` | `offkey` | needs attention | square |
| `rs-tag--clip` | `clip` | failed | diamond |

- The word carries the meaning. The hue and the dot's shape repeat it, so a tag still reads without colour.
- Set in `label`: uppercase mono with 0.08em tracking. Text is the `-ink` token on the `-wash` token.
- Never write the token's name to a client. A client reads "Failed", not "Clip".
