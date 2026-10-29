#!/usr/bin/env node
// Layout check: finds art that leaves the frame or crosses into the caption band.
// Usage: node scripts/check-layout.mjs <project> [--band Y] [--margin PX]
// Loads <project>/index.html in headless Chrome, seeks with window.__frame(t) to three moments in every
// voice line of timing.json, and measures the ink each element draws (its text runs and leaf shapes), not
// its box: full-width text boxes gave 101 false hits where ink gave the 9 real ones. Only scenes the camera
// has settled on are checked (a <section> centred on the frame); during a pan, neighbours show on purpose.
// --band Y: art must stay above frame y = Y (the caption band). --margin: side and top clearance, 10 px.
// --gap PX: also lists two pieces of art, the chapter bar among them, stacked closer than PX px (Christian,
// 14 Oct: "the spacing between different components is too small"); art that overlaps on purpose is not a gap.
// Full-bleed backgrounds carry data-bleed and are skipped. Prints what it read; exits 1 on any hit or no read.
import { existsSync, readFileSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { pathToFileURL } from 'node:url';
import { chromium } from 'playwright';

const args = process.argv.slice(2);
const opt = (k, d) => { const i = args.indexOf(k); return i < 0 ? d : +args.splice(i, 2)[1]; };
const band = opt('--band', null), margin = opt('--margin', 10), gap = opt('--gap', null);
const dir = resolve(args[0] || '.');
for (const f of ['index.html', 'timing.json']) {
  if (!existsSync(join(dir, f))) { console.error(`check-layout: no ${join(dir, f)}`); process.exit(1); }
}

const timing = JSON.parse(readFileSync(join(dir, 'timing.json'), 'utf8'));
const times = timing.scenes.flatMap((s) => s.lines.flatMap((l) => [l.start + 0.4, (l.start + l.end) / 2, l.end - 0.1]));
const b = await chromium.launch({ channel: 'chrome', headless: true, args: ['--disable-features=MacAppCodeSignClone'] });
const p = await b.newPage();
await p.goto(pathToFileURL(join(dir, 'index.html')).href);
await p.waitForFunction(() => typeof window.__frame === 'function', null, { timeout: 30000 });
const size = await p.evaluate(() => { const s = document.getElementById('stage'); return { w: +s.dataset.width, h: +s.dataset.height }; });
await p.setViewportSize({ width: size.w, height: size.h });

let read = 0;
const hits = [], gaps = new Map();
for (const t of times) {
  const r = await p.evaluate(({ t, band, margin, gap, W, H }) => {
    window.__frame(t);
    const vis = (el) => { let o = 1; for (let e = el; e && e.id !== 'stage'; e = e.parentElement) { const cs = getComputedStyle(e); if (cs.display === 'none' || cs.visibility === 'hidden') return 0; o *= +cs.opacity; } return o; };
    const ink = (el) => {
      const rs = [];
      const walk = (e) => {
        for (const c of e.childNodes) {
          if (c.nodeType === 3 && c.textContent.trim()) { const r = document.createRange(); r.selectNodeContents(c); rs.push(...r.getClientRects()); }
          // a child that clips its contents inks no further than its own box (a poster's rays end at its edge)
          else if (c.nodeType === 1 && vis(c) > 0.05) { if (getComputedStyle(c).overflow !== 'visible' && c.tagName !== 'svg') rs.push(c.getBoundingClientRect()); else if (c.children.length || (c.childNodes.length && c.textContent.trim())) walk(c); else rs.push(c.getBoundingClientRect()); }
        }
      };
      if ((!el.children.length && !el.textContent.trim()) || (getComputedStyle(el).overflow !== 'visible' && el.tagName !== 'svg')) rs.push(el.getBoundingClientRect()); else walk(el);
      const v = rs.filter((r) => r.width > 1 && r.height > 1);
      return v.length ? { l: Math.min(...v.map((r) => r.left)), t: Math.min(...v.map((r) => r.top)), r: Math.max(...v.map((r) => r.right)), b: Math.max(...v.map((r) => r.bottom)) } : null;
    };
    // settled: centred on the frame to 2 px and frame-sized, allowing the slow 2% push (scaled about the centre) some scenes run
    const settled = [...document.querySelectorAll('#world section')].filter((sec) => {
      if (getComputedStyle(sec).display === 'none') return false;
      const r = sec.getBoundingClientRect();
      return Math.abs(r.left + r.width / 2 - W / 2) < 2 && Math.abs(r.top + r.height / 2 - H / 2) < 2 && Math.abs(r.width / W - 1) < 0.05;
    });
    const out = [], near = [], boxes = []; let n = 0;
    const chap = document.getElementById('chap');
    if (settled.length && chap && vis(chap) > 0.15) { const bb = ink(chap); if (bb) boxes.push({ id: 'chapter bar', bb }); }
    for (const el of settled.flatMap((sec) => [...sec.children])) {
      n++;
      if (el.dataset.bleed !== undefined || vis(el) < 0.15) continue;
      const bb = ink(el);
      if (!bb) continue;
      boxes.push({ id: el.id || el.className || el.tagName, bb });
      if ((band !== null && bb.b > band) || bb.l < margin || bb.r > W - margin || bb.t < margin || bb.b > H - margin) {
        out.push(`${el.id || el.className || el.tagName} [${Math.round(bb.l)},${Math.round(bb.t)} → ${Math.round(bb.r)},${Math.round(bb.b)}]`);
      }
    }
    if (gap !== null) boxes.forEach((a, i) => boxes.slice(i + 1).forEach((b) => {
      const across = Math.min(a.bb.r, b.bb.r) - Math.max(a.bb.l, b.bb.l), v = Math.max(a.bb.t, b.bb.t) - Math.min(a.bb.b, b.bb.b);
      if (across > 0 && v >= 0 && v < gap) near.push([`${a.id} / ${b.id}`, Math.round(v)]);
    }));
    return { n, out, near };
  }, { t, band, margin, gap, W: size.w, H: size.h });
  read += r.n;
  r.out.forEach((o) => hits.push(`${t.toFixed(1)}s  ${o}`));
  // a pair is listed once, at its first frame and its tightest gap
  r.near.forEach(([k, v]) => { const g = gaps.get(k); if (!g || v < g.v) gaps.set(k, { t: g ? g.t : t, v }); });
}
await b.close();
console.log(`check-layout: ${size.w}x${size.h}, ${times.length} frames, ${read} element reads, ${hits.length} hits`);
if (!read) { console.error('check-layout: read nothing (no settled #world section at any frame)'); process.exit(1); }
hits.forEach((h) => console.log(h));
if (gap !== null) {
  console.log(`check-layout: ${gaps.size} pairs closer than ${gap} px`);
  [...gaps].sort((a, b) => a[1].t - b[1].t).forEach(([k, g]) => console.log(`${g.t.toFixed(1)}s  ${g.v} px  ${k}`));
}
process.exit(hits.length || gaps.size ? 1 : 0);
