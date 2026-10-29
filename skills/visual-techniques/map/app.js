// Renders map.json against techniques.json. Data only; every decision lives in the two files.
const $ = (id) => document.getElementById(id);
const esc = (s) => String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);
const JOBS = ["differentiate", "group", "sequence", "predict"];
const col = (job) => `--c: var(--${job})`;

async function load() {
  const [vocab, map] = await Promise.all(
    ["techniques.json", "map.json"].map((f) => fetch(f).then((r) => r.json()))
  );
  const byId = Object.fromEntries(vocab.techniques.map((t) => [t.id, t]));
  const order = JOBS.flatMap((j) => vocab.techniques.filter((t) => t.job === j));
  const refs = map.refs || [];
  const uses = (tid) => refs.filter((r) => r.reads.some((x) => x.t === tid));
  const shortIds = new Set((map.shortlist || []).map((s) => s.t));
  return { vocab, map, byId, order, refs, uses, shortIds };
}

function header({ map }) {
  document.title = map.title ? `${map.title} · technique map` : document.title;
  $("title").textContent = map.title || "Visual technique map";
  $("brief").textContent = map.brief || "";
  $("idea").textContent = map.idea ? `Idea: ${map.idea}` : "";
}

function jobs({ vocab, map, refs, byId }) {
  const counts = Object.fromEntries(JOBS.map((j) => [j, 0]));
  refs.forEach((r) => r.reads.forEach((x) => counts[byId[x.t].job]++));
  $("jobs").innerHTML = JOBS.map((j) => `
    <div class="job${map.job === j ? " set" : ""}" style="${col(j)}">
      <b>${counts[j]}</b><span>${j}${map.job === j ? " · the brief's job" : ""}</span>
      <p>${esc(vocab.jobs[j])}</p></div>`).join("");
}

function shortlist(s) {
  const items = s.map.shortlist || [];
  $("shortSec").hidden = !items.length && !s.map.dissent;
  $("short").innerHTML = items.map((x) => {
    const t = s.byId[x.t];
    return `<button class="chip" style="${col(t.job)}" data-t="${t.id}" title="${esc(x.why)}">${esc(t.name)}</button>`;
  }).join("") + (s.map.dissent ? `<span class="chip dissent" title="${esc(s.map.dissent.why)}">Against: ${esc(s.map.dissent.tool)}</span>` : "");
  $("short").onclick = (e) => e.target.dataset.t && showTech(s, e.target.dataset.t);
}

function matrix(s) {
  const head = s.order.map((t) => {
    const cls = ["t", s.uses(t.id).length ? "used" : "", s.shortIds.has(t.id) ? "short" : ""].join(" ");
    return `<th class="${cls}" style="${col(t.job)}" data-t="${t.id}" scope="col" tabindex="0"><div>${esc(t.name)}${t.conf === "low" ? " ?" : ""}</div></th>`;
  }).join("");
  const band = s.order.map((t) => `<th style="${col(t.job)}"></th>`).join("");
  const rows = s.refs.map((r) => {
    const cells = s.order.map((t) => {
      const on = r.reads.some((x) => x.t === t.id);
      return `<td class="${on ? "on" : ""}${r.draft ? " draft" : ""}" style="${col(t.job)}" data-r="${r.id}" data-t="${on ? t.id : ""}"></td>`;
    }).join("");
    return `<tr><th class="r" data-r="${r.id}" scope="row" tabindex="0"><img src="${esc(r.file)}" alt="">${esc(r.title)}${r.draft ? " (draft)" : ""}</th>${cells}</tr>`;
  }).join("");
  $("matrix").innerHTML = `<thead><tr class="jobrow"><th></th>${band}</tr><tr><th></th>${head}</tr></thead><tbody>${rows}</tbody>`;
  const pick = (e) => {
    const el = e.target.closest("[data-r],[data-t]");
    if (!el) return;
    if (el.dataset.r) showRef(s, el.dataset.r, el.dataset.t);
    else showTech(s, el.dataset.t);
  };
  $("matrix").onclick = pick;
  $("matrix").onkeydown = (e) => e.key === "Enter" && pick(e);
}

function mark(attr, id) {
  document.querySelectorAll("#matrix .sel").forEach((n) => n.classList.remove("sel"));
  document.querySelectorAll(`#matrix th[data-${attr}="${id}"]`).forEach((n) => n.classList.add("sel"));
}

function showTech(s, tid) {
  const t = s.byId[tid], users = s.uses(tid), sl = (s.map.shortlist || []).find((x) => x.t === tid);
  mark("t", tid);
  $("detail").style.cssText = col(t.job);
  $("detail").innerHTML = `
    <div><h2>${esc(t.job)} · ${esc(t.menu)}</h2><h3>${esc(t.name)}</h3>
      <p>${t.def_src === "ours" || t.def_src.startsWith("ours") ? esc(t.def) : `“${esc(t.def)}”`}</p>
      <p class="src">${esc(t.def_src)}${t.job_src === "ours" ? " · job placed by us" : ""}${t.conf === "low" ? " · name read at low confidence" : ""}</p></div>
    <div><h2>Look for</h2><p>${esc(t.look)}</p>
      ${sl ? `<h2>Why it is on the shortlist</h2><p>${esc(sl.why)}</p>` : ""}
      <h2>${users.length} reference${users.length === 1 ? "" : "s"} use it</h2>
      <div class="thumbs">${users.map((r) => `<img src="${esc(r.file)}" alt="${esc(r.title)}" title="${esc(r.title)}" data-r="${r.id}">`).join("") || "<p>None of the references in this map.</p>"}</div></div>`;
  $("detail").querySelector(".thumbs").onclick = (e) => e.target.dataset.r && showRef(s, e.target.dataset.r, tid);
}

function showRef(s, rid, tid) {
  const r = s.refs.find((x) => x.id === rid);
  mark("r", rid);
  $("detail").style.cssText = "";
  $("detail").innerHTML = `
    <div><img class="big" src="${esc(r.file)}" alt="${esc(r.title)}"></div>
    <div><h2>${r.draft ? "Draft" : "Reference"} · ${esc(r.source)}</h2><h3>${esc(r.title)}</h3>${r.idea ? `<p class="idea">Idea: ${esc(r.idea)}</p>` : ""}
      <ul>${r.reads.map((x) => { const t = s.byId[x.t]; return `<li style="${col(t.job)}"><b>${esc(t.name)}</b>${x.t === tid ? " ←" : ""}<br>${esc(x.why)}</li>`; }).join("")}</ul></div>`;
}

load().then((s) => {
  header(s); jobs(s); shortlist(s); matrix(s);
  const gaps = s.map.gaps || [];
  $("gapSec").hidden = !gaps.length;
  $("gaps").innerHTML = gaps.map((g) => `<li>${esc(g)}</li>`).join("");
  const first = (s.map.shortlist || [])[0];
  first ? showTech(s, first.t) : s.refs[0] && showRef(s, s.refs[0].id);
}).catch((err) => {
  $("detail").textContent = `The map could not load its data: ${err.message}. Republish with map.json and techniques.json beside the page.`;
});
