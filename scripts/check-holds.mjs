#!/usr/bin/env node
// Checks that every picture stays fully on screen long enough to be seen (Christian, 14 Oct: "some visuals don't
// stay on screen long enough to be noticed"). Usage: node scripts/check-holds.mjs <project> [--min 1.5]
// Loads <project>/index.html in headless Chrome, seeks with window.__frame every 0.1 s over the whole timeline,
// and times each run in which a scene element (a direct child of a #world section with an id) or a source card is
// fully shown: opacity above 0.85 all the way up its parents. A run shorter than --min seconds is a hit. It always
// reads the whole timeline, so its result covers the whole video (a slice once passed a 1.2 s stamp).
// Prints what it read; exits 1 on any hit or on nothing read.
import { existsSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { pathToFileURL } from 'node:url';
import { chromium } from 'playwright';

const args = process.argv.slice(2);
const i = args.indexOf('--min'), min = i < 0 ? 1.5 : +args.splice(i, 2)[1];
const dir = resolve(args[0] || '.');
if (!existsSync(join(dir, 'index.html'))) { console.error(`check-holds: no ${join(dir, 'index.html')}`); process.exit(1); }
const b = await chromium.launch({ channel: 'chrome', headless: true, args: ['--disable-features=MacAppCodeSignClone'] });
const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
await p.goto(pathToFileURL(join(dir, 'index.html')).href);
await p.waitForFunction(() => typeof window.__frame === 'function', null, { timeout: 30000 });
const r = await p.evaluate(() => {
  const end = +document.getElementById('stage').dataset.duration;
  const vis = (el) => { let o = 1; for (let e = el; e && e.id !== 'stage'; e = e.parentElement) { const cs = getComputedStyle(e); if (cs.display === 'none' || cs.visibility === 'hidden') return 0; o *= +cs.opacity; } return o; };
  const els = [...document.querySelectorAll('#world section > [id], #docs .dk')], on = new Map(), runs = [];
  let n = 0;
  for (let t = 0; t <= end; t += 0.1) {
    window.__frame(t); n++;
    els.forEach((el) => {
      const k = el.id || `card ${el.dataset.i}`, v = vis(el) > 0.85;
      if (v && !on.has(k)) on.set(k, t);
      if (!v && on.has(k)) { runs.push([k, on.get(k), t]); on.delete(k); }
    });
  }
  on.forEach((a, k) => runs.push([k, a, end]));
  return { n, end, els: els.length, runs };
});
await b.close();
const short = r.runs.filter(([, a, z]) => z - a < min);
console.log(`check-holds: ${r.n} frames over ${r.end.toFixed(1)} s, ${r.els} elements, ${r.runs.length} runs, ${short.length} under ${min} s`);
if (!r.runs.length) { console.error('check-holds: read nothing (no element was ever fully shown)'); process.exit(1); }
short.forEach(([k, a, z]) => console.log(`${a.toFixed(1)}s  ${(z - a).toFixed(1)} s  ${k}`));
process.exit(short.length ? 1 : 0);
