A labelled text input with one line of help. Wrap a `label`, an `input` and a `small` in `rs-field`.

**You provide** the label, the input's `id`, and help text that says what a good answer looks like.

- The label sits above the input in `body-strong`. Never use the placeholder as the label: placeholder text is `ink-faint`, 3 to 1, and vanishes on typing.
- Border is `stroke-hair` in `line-strong`; radius `radius-2`; height 48px, the same as a Button, so a field and its button line up.
- On an error add `rs-field--clip`, set `aria-invalid="true"`, and replace the help with what to fix: "Add the full link, starting with https://". The border goes to `clip` at `stroke-firm`.
- One field per line on phones. Gap between fields is `space-4`.
