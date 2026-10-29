A count on its way to a target. Wrap a label row and a `progress` element in `rs-meter`.

**You provide** the label, the count as "7 of 10", and matching `value` and `max` on the `progress`.

- Always print the count in words beside the bar. The bar alone is not the information.
- The bar is `ink` on `ground-sunken`, 12px tall (`space-3`), with round ends.
- Add `rs-meter--third` only when the target is met. The bar turns `third`.
- The fill grows over `time-4` on `ease-settle`, so it passes the mark by a hair and comes back.
- Use a Meter for a count with an agreed target. A number with no target is a Readout.
