// Sidebar: clips grouped by tier, a dot on any clip with at least one saved point.

const el = document.getElementById("list");
const HEAD = 15, TAIL = 22;

// Cut the middle, not the end: the end ("10 - John Serve POV") is what tells clips apart.
const short = s => (s.length > HEAD + TAIL + 1 ? `${s.slice(0, HEAD).trimEnd()}…${s.slice(-TAIL).trimStart()}` : s);

export function renderList(S, open) {
  const done = new Set(S.tags.map(r => r.file));
  const others = (S.here || []).filter(h => h.name !== S.me);
  el.replaceChildren();
  let tier = null;
  S.clips.forEach((c, i) => {
    if (S.untagged && done.has(c.file) && i !== S.i) return;
    if (c.tier !== tier) {
      tier = c.tier;
      const all = S.clips.filter(x => x.tier === tier);
      const head = document.createElement("div");
      head.className = "tier-head";
      head.textContent = `${tier} · ${all.filter(x => done.has(x.file)).length}/${all.length}`;
      el.append(head);
    }
    const row = document.createElement("div");
    row.className = "clip" + (done.has(c.file) ? " done" : "") + (i === S.i ? " on" : "");
    row.textContent = short(c.label);
    row.title = c.label;
    others.filter(h => h.file === c.file).forEach(h =>
      row.append(Object.assign(document.createElement("span"), { className: "by", textContent: h.name })));
    row.onclick = () => open(i);
    el.append(row);
    if (i === S.i && S.listedAt !== S.i) row.scrollIntoView({ block: "nearest" });
  });
  S.listedAt = S.i;  // scroll only when the clip changes, not on every presence check
}
