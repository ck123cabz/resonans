// Keyboard map. Shot keys come from tags.vocab.json, so a new shot needs no code.
// While a text field has focus every key types; Escape leaves the field.

const video = document.getElementById("video");
const FRAME = 1 / 30;

const FIXED = [
  ["Space", "play / pause"], ["← →", "1 s (shift 5 s)"], [", .", "one frame"],
  ["q", "speed 0.5 / 1"], ["Backspace", "remove shot at playhead"], ["t", "turn = shot at playhead"],
  ["i o", "point in / out"], ["1–5", "difficulty"], ["m", "role: montage"], ["j", "role: skip"],
  ["Enter", "accept guesses (asks first)"], ["Shift+Enter", "accept guesses, next"], ["Esc", "back to check guesses"], ["↑ ↓", "prev / next clip"],
  ["[ ]", "prev / next rally"], ["; '", "prev / next hit, paused on it"],
];

// An uppercase key in the vocab means Shift plus that letter.
const shown = k => (/^[A-Z]$/.test(k) ? `⇧${k.toLowerCase()}` : k);

export function help(S) {
  const tips = S.vocab.tips || {};
  const rows = [...S.vocab.shots.map(s => [shown(s.key), s.name, tips[s.name] || ""]), ...FIXED];
  document.getElementById("help").innerHTML = rows
    .map(([k, v, tip]) => `<div${tip ? ` data-tip="${tip}"` : ""}><kbd>${k}</kbd> ${v}</div>`).join("");
}

export function bindKeys(S, act) {
  const shot = Object.fromEntries(S.vocab.shots.map(s => [s.key, s.name]));
  document.addEventListener("keydown", e => {
    const typing = document.activeElement.matches("textarea, select, input:not([type=checkbox])");
    if (typing) {
      if (e.key === "Escape") document.activeElement.blur();
      return;
    }
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    if (document.activeElement.matches("button") && (e.key === "Enter" || e.key === " ")) return;
    // Shift decides the variant, not the letter's case, so Caps Lock changes nothing.
    const k = e.key.length === 1 ? (e.shiftKey ? e.key.toUpperCase() : e.key.toLowerCase()) : e.key;
    const run = {
      " ": () => (video.paused ? video.play() : video.pause()),
      ArrowLeft: () => (video.currentTime -= e.shiftKey ? 5 : 1),
      ArrowRight: () => (video.currentTime += e.shiftKey ? 5 : 1),
      ",": () => { video.pause(); video.currentTime -= FRAME; },
      ".": () => { video.pause(); video.currentTime += FRAME; },
      q: () => (video.playbackRate = video.playbackRate === 1 ? 0.5 : 1),
      Backspace: act.unlabel, t: act.turn,
      i: () => act.bound("in_s"), o: () => act.bound("out_s"),
      m: () => act.role("montage"), j: () => act.role("skip"),
      Enter: () => act.save(e.shiftKey),
      Escape: act.cancel,
      ArrowUp: () => act.move(-1), ArrowDown: () => act.move(1),
      "[": () => act.rally(-1), "]": () => act.rally(1),
      ";": () => act.hop(-1), "'": () => act.hop(1),
    }[k];
    if (run) run();
    else if (/^[1-5]$/.test(k)) act.set("difficulty", k);
    else if (shot[k] || shot[k.toLowerCase()]) act.label(shot[k] || shot[k.toLowerCase()]);
    else return;
    e.preventDefault();
  });
}
