// The labelled shots of the current point, and the saved points of a whole-match clip.
import { api } from "./api.js";
import { parseShots } from "./form.js";

export function drawShots(S, video) {
  const p = S.point, box = document.getElementById("shots");
  box.replaceChildren();
  p.shots.forEach((s, n) => {
    if (n) box.append(Object.assign(document.createElement("span"), { className: "sep", textContent: "›" }));
    const d = document.createElement("span");
    d.className = "shot" + (s.t.toFixed(2) === p.turn ? " turn" : "");
    if (S.vocab.tips?.[s.shot]) d.dataset.tip = S.vocab.tips[s.shot];
    d.textContent = `${s.shot} ${(s.t - p.in_s).toFixed(1)}s`;
    d.onclick = () => (video.currentTime = s.t);
    box.append(d);
  });
}

export function drawPoints(S, c, { load, remove }) {
  const box = document.getElementById("points");
  box.replaceChildren();
  if (!c.rallies.length) return;
  S.tags.filter(r => r.file === c.file).forEach(r => {
    const d = document.createElement("span");
    d.className = "pt" + (r.key === S.point.replace ? " on" : "");
    d.textContent = `${fmt(+r.in_s)} · ${plural(parseShots(r.shots).length, "shot")} · ${r.outcome || "no outcome"}`;
    const x = Object.assign(document.createElement("button"), { type: "button", textContent: "×", title: "Delete point" });
    x.setAttribute("aria-label", "Delete point");
    x.onclick = async e => { e.stopPropagation(); await remove(r.key); };
    d.append(x);
    d.onclick = () => load(r);
    box.append(d);
  });
}

export const plural = (n, word) => `${n} ${word}${n === 1 ? "" : "s"}`;

export const fmt = t => `${Math.floor(t / 60)}:${String(Math.floor(t % 60)).padStart(2, "0")}`;

// The bar that stops a save while a guessed field is still unchecked.
export function confirmBar(S, next) {
  const bar = document.getElementById("confirm");
  S.pending = next === null ? null : { next };
  bar.hidden = !S.pending;
  if (!S.pending) return;
  const p = S.point, m = S.matches.find(x => String(x.id) === String(p.match));
  const show = { match: m ? `#${m.id} ${m.stage}` : p.match, outcome: p.outcome, placement: p.placement };
  bar.innerHTML = "Not checked: " + [...p.guess].map(k => `${k} <b>${show[k]}</b>`).join(", ") +
    ". Enter saves them as yours · Esc to check them";
}

// Deleting a point adds a delete event; the history in tags.db still holds the point.
export async function removePoint(S, key) {
  await api("/api/tags/delete", { key });
  S.tags = S.tags.filter(r => r.key !== key);
  if (S.point.replace === key) S.point.replace = null;
}
