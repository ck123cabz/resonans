// The current clip and point live in the URL hash (#<file>@<in_s>), so a reload or a
// shared link lands where you were instead of back on the first clip.
export function writeUrl(S) {
  const p = S.point;
  if (!p) return;
  const hash = `#${encodeURIComponent(p.file)}@${p.in_s.toFixed(2)}`;
  if (location.hash !== hash) history.replaceState(null, "", hash);
}

export function readUrl(S) {
  const m = decodeURIComponent(location.hash.slice(1)).match(/^(.+)@([\d.]+)$/);
  const i = m ? S.clips.findIndex(c => c.file === m[1]) : -1;
  return i < 0 ? { i: 0, at: null } : { i, at: +m[2] };
}
