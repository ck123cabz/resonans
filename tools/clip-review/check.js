// Reminders for the parts a point usually needs, listed under "required" in
// tags.vocab.json. Leaving an incomplete point on purpose (], [, arrows, Shift+Enter,
// a click) asks once; the second try goes through. Playing into the next rally never
// stops, but says what the rally just left was missing.

const line = document.getElementById("missing");
const NAMES = { shots: "shots", turn: "turn (t)", won_by: "won by", difficulty: "difficulty (1–5)",
                camera: "camera", score: "score", outcome: "outcome", build: "build" };

const id = p => `${p.file}#${p.in_s.toFixed(2)}`;
const empty = v => !v || (Array.isArray(v) && !v.length);

export function missing(S, c) {
  const p = S.point;
  if (!p || c.tier === "groups" || (!p.shots.length && !p.replace)) return [];
  return (S.vocab.required || []).filter(k => empty(p[k]));
}

export function drawMissing(S, c) {
  const m = missing(S, c);
  const asked = S.asked === (S.point && id(S.point));
  line.hidden = !m.length && !S.leftOpen;
  line.classList.toggle("warn", asked || !!S.leftOpen);
  line.textContent = m.length
    ? `Still missing: ${m.map(k => NAMES[k] || k).join(" · ")}${asked ? ". Press again to move on anyway" : ""}`
    : S.leftOpen || "";
}

// True when the move should stop here so Christian sees the reminder first.
export function holdForReminder(S, c, auto) {
  const m = missing(S, c), p = S.point;
  S.leftOpen = "";
  if (!m.length) return false;
  if (auto) {
    S.leftOpen = `The rally you just left is missing ${m.map(k => NAMES[k] || k).join(" · ")}. [ goes back`;
    return false;
  }
  if (S.asked === id(p)) return false;
  S.asked = id(p);
  drawMissing(S, c);
  return true;
}
