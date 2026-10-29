// Clip review page. The machine finds when each paddle hit happened; Christian says
// what each hit was. A shot key snaps to the detected hit just before the playhead,
// or makes a new one at the playhead when detection missed it.
import { renderList } from "./list.js";
import { drawTimeline, follow, hop } from "./timeline.js";
import { fillOptions, showPoint, fromRow, newPoint, toggle } from "./form.js";
import { bindKeys, help } from "./keys.js";
import { drawShots, drawPoints, removePoint, fmt, plural, confirmBar } from "./points.js";
import { startPresence } from "./presence.js";
import { snapshot, rallyBar, watchRallies, rallyOf, savedIn as savedInClip } from "./rally.js";
import { makeSaver } from "./autosave.js";
import { api } from "./api.js";
import { drawMissing, holdForReminder } from "./check.js";
import { writeUrl, readUrl } from "./url.js";

const video = document.getElementById("video");
const status = msg => (document.getElementById("status").textContent = msg);
const S = { clips: [], vocab: null, matches: [], tags: [], i: 0, point: null, untagged: false };
const clip = () => S.clips[S.i];
const SNAP_BEFORE = 0.6, SNAP_AFTER = 0.2;
const savedIn = r => savedInClip(S, clip(), r);
const saver = makeSaver(S, api, status, p => {
  if (p) status(`saved ${fmt(p.in_s)} · ${plural(p.shots.length, "shot")} · ${plural(S.tags.length, "point")} tagged`);
  rallyBar(S, clip());
});
S.onEdit = () => { saver.soon(); rallyBar(S, clip()); drawMissing(S, clip()); };

function render() {
  const c = clip();
  renderList(S, open);
  document.getElementById("title").textContent = c.label;
  document.getElementById("tier").textContent = c.tier;
  showPoint(S, render);
  drawTimeline(S, c, pickRally);
  drawShots(S, video);
  const load = async r => {
    if (!(await saver.save()) || holdForReminder(S, c, false)) return;
    S.point = fromRow(r, c); snapshot(S); video.currentTime = r.in_s; render();
  };
  drawPoints(S, c, { load, remove: key => removePoint(S, key).then(render) });
  rallyBar(S, c);
  drawMissing(S, c);
  writeUrl(S);
  saver.soon();
}

async function open(i, at = null) {
  if (!(await saver.save()) || (S.point && holdForReminder(S, clip(), false))) return;
  confirmBar(S, null);
  S.point = null;
  S.i = Math.max(0, Math.min(S.clips.length - 1, i));
  const c = clip(), rows = S.tags.filter(r => r.file === c.file);
  video.src = `/media/${encodeURIComponent(c.proxy)}`;
  video.playbackRate = c.tier === "groups" ? 1 : 0.5;
  const there = at === null ? null : c.rallies[rallyOf(c, at)];
  if (c.rallies.length) return pickRally(there || c.rallies.find(r => !savedIn(r)) || c.rallies[0]);
  S.point = rows.length ? fromRow(rows[0], c) : newPoint(c, 0, c.duration);
  snapshot(S);
  render();
}

// The point being left is saved before the form moves to rally r.
async function pickRally(r, seek = true, auto = false) {
  if (!(await saver.save())) return;
  const c = clip(), row = savedIn(r), p = S.point;
  if (p && p.file === c.file && p.in_s >= r.in - 1.5 && p.in_s <= r.out) {
    if (seek) video.currentTime = r.in;  // already on this rally
    return;
  }
  if (p && holdForReminder(S, c, auto)) return;
  S.point = row ? fromRow(row, c) : newPoint(c, r.in, r.out);
  snapshot(S);
  if (seek) video.currentTime = r.in;
  render();
}

const act = {
  label(shot) {
    const p = S.point, t = video.currentTime;
    const near = clip().hits.filter(h => h >= t - SNAP_BEFORE && h <= t + SNAP_AFTER);
    const at = near.length ? near.reduce((a, b) => (Math.abs(b - t) < Math.abs(a - t) ? b : a)) : t;
    const old = p.shots.find(s => Math.abs(s.t - at) <= 0.05);  // relabelling a shot
    p.shots = p.shots.filter(s => s !== old);
    if (old && p.turn === old.t.toFixed(2)) p.turn = at.toFixed(2);
    p.shots.push({ t: at, shot });
    p.shots.sort((a, b) => a.t - b.t);
    render();
  },
  unlabel() {
    const p = S.point, t = video.currentTime;
    if (!p.shots.length) return;
    const s = p.shots.reduce((a, b) => (Math.abs(b.t - t) < Math.abs(a.t - t) ? b : a));
    p.shots.splice(p.shots.indexOf(s), 1);
    if (p.turn === s.t.toFixed(2)) p.turn = "";
    render();
  },
  turn() {
    const p = S.point, t = video.currentTime + SNAP_AFTER;
    const s = [...p.shots].reverse().find(x => x.t <= t);
    if (s) p.turn = p.turn === s.t.toFixed(2) ? "" : s.t.toFixed(2);
    render();
  },
  bound(k) {  // i and o in either order: the earlier time is always the start
    const p = S.point;
    p[k] = video.currentTime;
    if (p.in_s > p.out_s) [p.in_s, p.out_s] = [p.out_s, p.in_s];
    render();
  },
  set(k, v) { S.point[k] = v; S.point.guess.delete(k); render(); },
  role(v) {
    toggle(S.point.roles, v);
    if (clip().tier === "groups") return act.save(true, "drop");
    render();
  },
  // Enter. Auto-save already stores everything but guesses; Enter is how they get in.
  // mode "ask": name any unchecked guess first; "accept": store them as his;
  // "drop": store them blank (one-key group tagging), so they stay guesses.
  async save(next, mode = "ask") {
    if (S.pending && mode === "ask") return act.save(S.pending.next || next, "accept");
    if (mode === "ask" && S.point.guess.size) return confirmBar(S, next);
    confirmBar(S, null);
    if (!(await saver.save(mode === "drop" ? "drop" : "accept"))) return;
    if (next) return clip().rallies.length ? act.rally(1) : open(S.i + 1);
    render();
  },
  hop: d => hop(S, clip(), d),
  cancel: () => confirmBar(S, null),
  move: d => open(S.i + d),
  rally(d) {
    const c = clip(), i = c.rallies.findIndex(r => r.in >= S.point.in_s - 0.01);
    const r = c.rallies[(i < 0 ? 0 : i) + d];
    return r ? pickRally(r) : open(S.i + d);
  },
};

document.getElementById("untagged").onchange = e => { S.untagged = e.target.checked; render(); };

[S.clips, S.vocab, S.matches, S.tags] = await Promise.all(
  ["/api/clips", "/api/vocab", "/api/matches", "/api/tags"].map(p => api(p)));
fillOptions(S);
bindKeys(S, act);
help(S);
follow(S, clip);
const { i: startAt, at } = readUrl(S);
open(startAt, at);
startPresence(S, clip, api, () => renderList(S, open));
watchRallies(S, clip, video, pickRally);
status(`${plural(S.clips.length, "clip")} · ${plural(S.tags.length, "point")} tagged`);
