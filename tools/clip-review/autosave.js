// Auto-save. A change is written about half a second after the last edit, and leaving
// a point (another rally, another clip, closing the tab) writes it first. Auto-saves
// store unchecked guesses blank; only Enter accepts them (app.js).
import { readRow } from "./form.js";
import { snapshot, dirty } from "./rally.js";

const QUIET_MS = 600;

export function makeSaver(S, api, status, onSaved) {
  let timer = null, chain = Promise.resolve();

  async function write(mode) {
    const p = S.point;
    const body = { replace: p.replace, row: readRow(S, mode === "accept"), who: S.me };
    const row = await api("/api/tags", body);
    S.tags = S.tags.filter(r => r.key !== p.replace && r.key !== row.key).concat(row);
    p.replace = row.key;
    if (mode === "accept") p.guess.clear();
    snapshot(S);
    S.failed = false;
    onSaved(p);
  }

  // Writes queue behind each other, and each reads the point as it stands when it runs.
  // Resolves false when the write failed, so a caller can stay put instead of moving on.
  function save(mode = "drop") {
    clearTimeout(timer);
    chain = chain
      .then(() => (S.point && (mode === "accept" || dirty(S)) ? write(mode) : null))
      .then(() => true)
      .catch(err => {
        S.failed = true;
        status("not saved: server not answering, retrying on your next change");
        onSaved(null);
        console.error(err);
        return false;
      });
    return chain;
  }

  function soon() {
    clearTimeout(timer);
    if (dirty(S)) timer = setTimeout(save, QUIET_MS);
  }

  window.addEventListener("beforeunload", e => {
    if (!dirty(S)) return;
    navigator.sendBeacon("/api/tags",
      JSON.stringify({ replace: S.point.replace, row: readRow(S, false), who: S.me }));
    if (S.failed) e.preventDefault();  // the server was down: let the browser ask
  });

  return { save, soon };
}
