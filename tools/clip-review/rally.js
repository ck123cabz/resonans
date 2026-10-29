// Whole-match clips: say which rally the form is on, and keep the form on the rally
// under the playhead. Leaving a rally saves it first (autosave.js).
import { readRow } from "./form.js";
import { fmt } from "./points.js";

const bar = document.getElementById("rallybar");
const PAD = 1.5;

export const snapshot = S => (S.saved = JSON.stringify(readRow(S, true)));
export const dirty = S => !!S.point && S.saved !== JSON.stringify(readRow(S, true));
export const rallyOf = (c, t) => c.rallies.findIndex(r => t >= r.in - PAD && t <= r.out);

// A saved point belongs to a rally when its in-time falls inside it, even after
// Christian moved the in-time with `i`.
export const savedIn = (S, c, r) => S.tags.find(x => x.file === c.file && +x.in_s >= r.in - PAD && +x.in_s <= r.out);

export function rallyBar(S, c) {
  bar.hidden = !c.rallies.length;
  if (!c.rallies.length) return;
  const p = S.point, n = rallyOf(c, p.in_s) + 1;
  const state = S.failed ? "not saved, server not answering" : dirty(S) ? "saving"
    : p.replace ? "saved as a point" : "not tagged";
  bar.textContent = `Rally ${n || "?"} of ${c.rallies.length} · ${fmt(p.in_s)}–${fmt(p.out_s)} · ${state}`;
  bar.classList.toggle("warn", !!S.failed);
}

export function watchRallies(S, clip, video, pick) {
  video.addEventListener("timeupdate", () => {
    const c = clip(), p = S.point, t = video.currentTime;
    if (!c?.rallies.length || !p) return;
    if (t >= p.in_s - PAD && t <= p.out_s) return;
    const r = c.rallies[rallyOf(c, t)];
    if (r) pick(r, false, true);
  });
}
