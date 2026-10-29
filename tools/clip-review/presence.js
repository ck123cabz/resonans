// Who else has the page open, and their saves, checked every few seconds.
// The name lives in this browser only; the page works the same without one.

const EVERY_MS = 3000;
const me = document.getElementById("me");
const who = document.getElementById("who");

function stored() {
  try { return localStorage.getItem("clip-review-name") || ""; } catch { return ""; }
}

export function startPresence(S, clip, api, relist) {
  S.me = me.value = stored();
  me.addEventListener("change", () => {
    S.me = me.value.trim();
    try { localStorage.setItem("clip-review-name", S.me); } catch { /* private window */ }
  });
  let tagsAt = null;
  const tick = async () => {
    if (S.me) {
      try {
        const res = await api("/api/presence", { name: S.me, file: clip().file, in_s: S.point?.in_s ?? 0 });
        S.here = res.here;
        const others = res.here.filter(h => h.name !== S.me);
        who.textContent = who.title = others.length
          ? "Here: " + others.map(h => `${h.name} · ${h.file.replace(/\.[^.]+$/, "")}`).join(", ") : "";
        if (tagsAt !== null && res.tags_at !== tagsAt) S.tags = await api("/api/tags");
        tagsAt = res.tags_at;
        relist();
      } catch (err) {
        who.textContent = "Server not answering";
        console.error(err);
      }
    }
    setTimeout(tick, EVERY_MS);
  };
  tick();
}
