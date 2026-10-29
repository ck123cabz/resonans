// Anchor check: lists every scene animation and sound effect whose word is no longer in SCRIPT.md, before the
// voice run spends credits on it. Reads SCRIPT.md through the project's own tools/narrate.mjs (its exported
// `scenes`), so a line's text here is exactly what timing.json will hold, delivery cues and {caption|spoken}
// tokens resolved. Anchors read: literal W('scene', n, 'phrase') and L('scene', n) calls in src/ and tools/,
// per-file wrappers such as `l = (i) => L('ph', i)` and `W8 = (i, w) => W('ph', i, w)`, and
// [scene, line, phrase, offset] arrays in data/*.json.
// Run from content-studio/: node scripts/check-anchors.mjs video-projects/<slug>
// Exit 0 every anchor matches · 1 a miss · 2 bad input (no project, no scenes export, no anchors read).
import { readFileSync, readdirSync, existsSync } from 'node:fs';
import { join, resolve, relative } from 'node:path';
import { pathToFileURL } from 'node:url';

const project = process.argv[2] && resolve(process.argv[2]);
if (!project || !existsSync(join(project, 'SCRIPT.md'))) {
  console.error('usage: node scripts/check-anchors.mjs video-projects/<slug>  (the folder holds SCRIPT.md)');
  process.exit(2);
}
process.chdir(project); // narrate.mjs reads SCRIPT.md from the working folder
const { scenes } = await import(pathToFileURL(join(project, 'tools/narrate.mjs')).href);
if (!Array.isArray(scenes)) {
  console.error('tools/narrate.mjs does not export `scenes`; write `export const scenes = []` there');
  process.exit(2);
}
const byId = new Map(scenes.map((s) => [s.id, s]));

const anchors = []; // { file, line, sid, li, phrase }
const lineOf = (src, k) => src.slice(0, k).split('\n').length;
const STR = `'([^'\\\\]*)'`;

function fromCode(file) {
  const src = readFileSync(file, 'utf8');
  for (const m of src.matchAll(new RegExp(`\\bW\\(${STR}, (\\d+), ${STR}`, 'g')))
    anchors.push({ file, line: lineOf(src, m.index), sid: m[1], li: +m[2], phrase: m[3] });
  for (const m of src.matchAll(new RegExp(`\\b[LW]\\(${STR}, (\\d+)\\)`, 'g')))
    anchors.push({ file, line: lineOf(src, m.index), sid: m[1], li: +m[2], phrase: null });
  // wrappers bind a scene id once; their calls carry only the line number and phrase
  for (const d of src.matchAll(new RegExp(`\\b(\\w+) = \\((\\w+)(?:, \\w+)?\\) => [LW]\\(${STR}, \\2`, 'g'))) {
    const [, name, , sid] = d;
    for (const m of src.matchAll(new RegExp(`(?<![\\w.])${name}\\((\\d+)(?:, ${STR})?\\)`, 'g')))
      anchors.push({ file, line: lineOf(src, m.index), sid, li: +m[1], phrase: m[2] ?? null });
  }
}

function fromJson(file) {
  const walk = (v, key) => {
    if (!v || typeof v !== 'object') return;
    const isAnchor = Array.isArray(v) && v.length === 4 && typeof v[0] === 'string' && Number.isInteger(v[1])
      && (v[2] === null || typeof v[2] === 'string') && typeof v[3] === 'number' && (byId.has(v[0]) || key === 'in' || key === 'out');
    if (isAnchor) return anchors.push({ file, line: null, sid: v[0], li: v[1], phrase: v[2] === 'end' ? null : v[2] });
    for (const [k, x] of Object.entries(v)) walk(x, k);
  };
  walk(JSON.parse(readFileSync(file, 'utf8')));
}

const list = (dir, ext) => (existsSync(dir) ? readdirSync(dir).filter((f) => f.endsWith(ext)).map((f) => join(dir, f)) : []);
const code = [...list('src', '.js'), ...list('tools', '.mjs').filter((f) => !f.endsWith('narrate.mjs'))];
const json = list('data', '.json');
code.forEach(fromCode);
json.forEach(fromJson);
if (!anchors.length) {
  console.error(`0 anchors read from ${code.length} code files and ${json.length} data files`);
  process.exit(2);
}

const misses = anchors.filter(({ sid, li, phrase }) => {
  const line = byId.get(sid)?.lines[li];
  return !line || (phrase != null && !line.text.includes(phrase));
});
for (const a of misses) {
  const where = `${relative(project, a.file)}${a.line ? `:${a.line}` : ''}`;
  const line = byId.get(a.sid)?.lines[a.li];
  const why = !byId.has(a.sid) ? 'no such scene' : !line ? `scene has ${byId.get(a.sid).lines.length} lines` : `"${a.phrase}" not in: ${line.text}`;
  console.log(`${where}  ${a.sid}.${a.li}  ${why}`);
}
console.log(`check-anchors: ${anchors.length} anchors from ${code.length} code and ${json.length} data files against ${scenes.length} scenes, ${misses.length} misses`);
process.exit(misses.length ? 1 : 0);
