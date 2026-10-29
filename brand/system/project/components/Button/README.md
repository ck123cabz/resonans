The one way to start an action. Use class `rs-button` on a `button` or an `a`.

**You provide** the label, as a verb and its object: "Send the brief", "Open the calendar". 2 to 3 words.

| Variant | Class | When |
|---|---|---|
| Ink | `rs-button` | The main action of a view. Fill `ink`, label `ground`. |
| Root | `rs-button rs-button--root` | Once per layout at most, for the action the page exists for. Fill `root`, label `on-root`. |
| Quiet | `rs-button rs-button--quiet` | Every other action. Border `line-strong`. |

- Height is 48px (`space-12`) and the ends are `radius-round`, because the wordmark's stroke ends in a half circle.
- Padding is `space-3` by `space-6`. Leave `space-4` between two buttons.
- Press scales to 97% over `time-1` on `ease-settle`. Focus shows a 2px `focus` outline, 2px away.
- A disabled button keeps its label and says why nearby. Do not hide it.
- Do not put two Root buttons in one view. Do not use Root for delete; errors use `clip`.
