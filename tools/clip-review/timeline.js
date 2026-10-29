// The two bars under the video. The overview spans a whole-match clip and shows its
// rally candidates; the timeline spans the current point and shows detected hits
// (grey ticks) and the shots Christian labelled (yellow, the turn in ember).

const overview = document.getElementById("overview");
const timeline = document.getElementById("timeline");
const video = document.getElementById("video");
const PAD = 1.5;

export function view(S, c) {
  const p = S.point;
  return c.rallies.length ? [Math.max(0, p.in_s - PAD), Math.min(c.duration, p.out_s + PAD)]
                          : [0, c.duration || video.duration || 1];
}

const at = (t, [a, b]) => `${((t - a) / (b - a)) * 100}%`;

function put(bar, cls, css, text) {
  const d = document.createElement("div");
  d.className = cls;
  Object.assign(d.style, css);
  if (text) d.textContent = text;
  bar.append(d);
  return d;
}

export function drawTimeline(S, c, pickRally) {
  const p = S.point, v = view(S, c), whole = [0, c.duration];
  overview.replaceChildren();
  if (c.rallies.length) {
    const saved = S.tags.filter(r => r.file === c.file).map(r => +r.in_s);
    c.rallies.forEach(r => {
      const on = saved.some(s => s >= r.in - PAD && s <= r.out);
      const d = put(overview, "rally" + (on ? " saved" : ""),
        { left: at(r.in, whole), width: at(whole[0] + r.out - r.in, whole) });
      d.onclick = e => { e.stopPropagation(); pickRally(r); };
    });
    put(overview, "range", { left: at(p.in_s, whole), width: at(p.out_s - p.in_s, whole) });
    put(overview, "head", {});
  }
  timeline.replaceChildren();
  put(timeline, "range", { left: at(p.in_s, v), width: at(v[0] + p.out_s - p.in_s, v) });
  c.hits.filter(t => t >= v[0] && t <= v[1]).forEach(t => put(timeline, "tick", { left: at(t, v) }));
  const letter = Object.fromEntries(S.vocab.shots.map(s => [s.name, s.key]));
  p.shots.forEach(s => put(timeline, "mark" + (s.t.toFixed(2) === p.turn ? " turn" : ""),
    { left: at(s.t, v) }, letter[s.shot] || s.shot[0]));
  put(timeline, "head", {});
  overview.onclick = e => seek(e, overview, whole);
  timeline.onclick = e => seek(e, timeline, v);
}

function seek(e, bar, [a, b]) {
  const r = bar.getBoundingClientRect();
  video.currentTime = a + ((e.clientX - r.left) / r.width) * (b - a);
}

// Playhead positions follow the video on every frame.
export function follow(S, clip) {
  const step = () => {
    const c = clip();
    if (c && S.point) {
      const t = video.currentTime;
      const h1 = timeline.querySelector(".head"), h2 = overview.querySelector(".head");
      if (h1) h1.style.left = at(t, view(S, c));
      if (h2) h2.style.left = at(t, [0, c.duration]);
    }
    requestAnimationFrame(step);
  };
  requestAnimationFrame(step);
}

// Jump to the previous or next hit: detected ticks plus any shot added by hand.
export function hop(S, c, d) {
  const t = video.currentTime, stops = [...c.hits, ...S.point.shots.map(s => s.t)];
  const ahead = stops.filter(h => (d > 0 ? h > t + 0.05 : h < t - 0.05));
  if (!ahead.length) return;
  video.pause();
  video.currentTime = d > 0 ? Math.min(...ahead) : Math.max(...ahead);
}
