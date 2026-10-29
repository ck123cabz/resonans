// The fields under the timeline: filled from the current point, read back on save.
// A value the page guessed carries the `guess` class until Christian touches it, and is
// saved blank unless he accepts it, so tags.csv never holds an unchecked guess.

const $ = id => document.getElementById(id);
const SELECTS = ["match", "outcome", "placement", "won_by", "difficulty", "camera", "crowd"];
const TEXTS = ["score", "note"];
const CHIPS = ["build", "roles"];
const GUESSED = ["match", "outcome", "placement"];

function options(sel, values, labels = values) {
  sel.replaceChildren(...["", ...values].map((v, i) => {
    const o = document.createElement("option");
    o.value = v;
    o.textContent = i ? labels[i - 1] : "–";
    return o;
  }));
}

export function fillOptions(S) {
  const m = S.matches;
  options($("f-match"), m.map(x => String(x.id)),
    m.map(x => `#${x.id} ${x.stage} · ${x.a} vs ${x.b} · ${x.score}`));
  ["outcome", "placement", "camera", "crowd"].forEach(k => options($(`f-${k}`), S.vocab[k]));
  options($("f-difficulty"), ["1", "2", "3", "4", "5"],
    ["1 routine", "2", "3 good rally", "4", "5 a 4.0 player rewinds it"]);
  [...SELECTS, ...TEXTS].forEach(k => $(`f-${k}`).addEventListener("input", () => {
    S.point[k] = $(`f-${k}`).value;
    S.point.guess.delete(k);
    $(`f-${k}`).classList.remove("guess");
    if (k === "match") wonBy(S);
    S.onEdit?.();
  }));
  // A dropdown gives focus back after a pick, so the next key is a shortcut again
  // and a letter can never change the pick by type-ahead.
  SELECTS.forEach(k => $(`f-${k}`).addEventListener("change", () => $(`f-${k}`).blur()));
}

function wonBy(S) {
  const m = S.matches.find(x => String(x.id) === String(S.point.match));
  options($("f-won_by"), m ? [m.a, m.b] : []);
  if (!(m && [m.a, m.b].includes(S.point.won_by))) S.point.won_by = "";  // winner must be in the match
  $("f-won_by").value = S.point.won_by;
}

export function showPoint(S, onChange) {
  const p = S.point;
  [...SELECTS, ...TEXTS].forEach(k => {
    if (k === "won_by") wonBy(S);
    $(`f-${k}`).value = p[k] ?? "";
    $(`f-${k}`).classList.toggle("guess", p.guess.has(k));
  });
  CHIPS.forEach(k => {
    const box = $(`f-${k}`);
    box.replaceChildren(...S.vocab[k].map(v => {
      const c = document.createElement("button");
      c.type = "button";
      c.className = "chip" + (p[k].includes(v) ? " on" : "");
      c.setAttribute("aria-pressed", p[k].includes(v));
      c.textContent = v;
      if (S.vocab.tips?.[v]) c.dataset.tip = S.vocab.tips[v];
      c.onclick = e => { toggle(p[k], v); onChange(); if (e.detail) e.currentTarget.blur(); };
      return c;
    }));
  });
}

export function toggle(list, v) {
  const i = list.indexOf(v);
  i < 0 ? list.push(v) : list.splice(i, 1);
}

export function readRow(S, accept) {
  const p = { ...S.point };
  if (!accept) p.guess.forEach(k => (p[k] = ""));
  return {
    file: p.file, in_s: p.in_s.toFixed(2), out_s: p.out_s.toFixed(2),
    match: p.match, score: p.score, turn: p.turn, outcome: p.outcome,
    shots: p.shots.map(s => `${s.t.toFixed(2)}:${s.shot}`).join(" "),
    placement: p.placement, won_by: p.won_by, build: p.build.join("|"),
    difficulty: p.difficulty, camera: p.camera, crowd: p.crowd,
    roles: p.roles.join("|"), note: p.note,
  };
}

// `shots` is "<t>:<name> <t>:<name>"; a name can hold spaces ("twoey drive"), so a
// pair runs until the next "<number>:", never just to the next space.
const SHOT = /(\d+(?:\.\d+)?):(.+?)(?=\s+\d+(?:\.\d+)?:|$)/g;
export const parseShots = s => [...(s || "").matchAll(SHOT)].map(m => ({ t: +m[1], shot: m[2].trim() }));

export function fromRow(r, c) {
  const blank = GUESSED.filter(k => !r[k] && c[k]);
  return {
    ...r, replace: r.key, in_s: +r.in_s, out_s: +r.out_s, guess: new Set(blank),
    ...Object.fromEntries(blank.map(k => [k, String(c[k])])),
    shots: parseShots(r.shots),
    build: r.build ? r.build.split("|") : [], roles: r.roles ? r.roles.split("|") : [],
  };
}

export function newPoint(c, in_s, out_s) {
  const guess = new Set(GUESSED.filter(k => c[k]));
  return {
    replace: null, file: c.file, in_s, out_s, shots: [], turn: "", score: "",
    match: c.match ? String(c.match) : "", outcome: c.outcome, placement: c.placement,
    won_by: "", build: [], roles: [], difficulty: "", camera: "", crowd: "", note: "", guess,
  };
}
