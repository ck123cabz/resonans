A message about something that happened. Use class `rs-notice` with a `b` heading and a `span` of one sentence.

**You provide** a heading that states the event, and one sentence with the next step.

| Class | When | Role |
|---|---|---|
| `rs-notice--third` | a result arrived | `status` |
| `rs-notice--fifth` | something to know | `status` |
| `rs-notice--offkey` | something is drifting and can still be fixed | `status` |
| `rs-notice--clip` | something failed | `alert` |

- The heading names what happened in the reader's words: "Thursday's post did not go out".
- The sentence says what to do, and what happens when they do it.
- Round mark for good news and information, square for a warning, diamond for a failure.
- Stack notices with `space-4` between them. Newest first.
