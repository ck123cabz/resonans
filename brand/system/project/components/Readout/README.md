One result as a number. Wrap `rs-readout` items, each with a `dt`, a `dd` and a `small`, in a `dl` with class `rs-readouts`.

**You provide** the label, the number, and the line that says what it is counted against.

- Resonans sells results, so the number is the largest thing in the block: `readout`, mono, tabular figures.
- The label is `label` in `ink-soft`. The third line is never empty: "of 10 by 26 Oct", "312 on last week".
- Add `rs-readout--root` to one readout per row, the one the client is paying for. Its number takes `root-ink`.
- A change line uses a triangle and a word of direction: class `up` in `third-ink`, class `down` in `clip-ink`.
- Up to 4 readouts in a row, divided by a `line` hairline. More than 4 is a table.
