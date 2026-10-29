#!/usr/bin/env node
// Tiles many frames into one labelled image, so a review reads one picture instead of one per frame.
// Usage: node scripts/contact-sheet.mjs <out.png> <frame.png | folder>... [--cols N] [--width PX]
// Each tile is labelled with its time from a `hyperframes snapshot` name (frame-02-at-191s.png -> 191s),
// or the file name. Labels are drawn by the browser, since this Mac's ffmpeg has no drawtext.
// Default: 4 columns for tall frames, 2 for wide ones, 1600 px across. Exits 1 when no frames are read.
import { existsSync, readdirSync, statSync, writeFileSync, mkdirSync, rmSync } from 'node:fs';
import { basename, dirname, join, resolve } from 'node:path';
import { pathToFileURL } from 'node:url';
import { chromium } from 'playwright';

const args = process.argv.slice(2);
const opt = (k) => { const i = args.indexOf(k); return i < 0 ? null : +args.splice(i, 2)[1]; };
const colsArg = opt('--cols'), width = opt('--width') || 1600;
const [out, ...inputs] = args;
const frames = inputs.flatMap((p) => (existsSync(p) && statSync(p).isDirectory()
  ? readdirSync(p).filter((f) => /\.(png|jpe?g)$/i.test(f)).sort().map((f) => join(p, f))
  : [p])).filter((p) => existsSync(p)).map((p) => resolve(p))
  .filter((p) => p !== resolve(out || '') && !basename(p).startsWith('contact-sheet')); // never tile an earlier sheet
if (!out || !frames.length) {
  console.error('contact-sheet: no frames read. Usage: contact-sheet.mjs <out.png> <frame.png | folder>...');
  process.exit(1);
}

const label = (p) => (basename(p).match(/at-([\d.]+s)/) || [])[1] || basename(p).replace(/\.\w+$/, '');
const tiles = frames.map((p) => `<figure><img src="${pathToFileURL(p)}"><figcaption>${label(p)}</figcaption></figure>`).join('');
const html = `<!doctype html><meta charset=utf8><style>
body{margin:0;background:#111;color:#fff;font:600 22px system-ui;width:${width}px}
main{display:grid;grid-template-columns:repeat(var(--cols),1fr);gap:6px;padding:6px}
figure{margin:0}img{width:100%;display:block}figcaption{padding:4px 2px}</style><main>${tiles}</main>
<script>const i=document.images[0];const go=()=>{document.querySelector('main').style.setProperty('--cols',${colsArg || 0}||(i.naturalHeight>i.naturalWidth?4:2));document.title='ready'};i.complete?go():i.onload=go;</script>`;

const page = join(dirname(resolve(out)), '.contact-sheet.html');
mkdirSync(dirname(page), { recursive: true });
writeFileSync(page, html);
const b = await chromium.launch({ channel: 'chrome', headless: true, args: ['--disable-features=MacAppCodeSignClone', '--allow-file-access-from-files'] });
const p = await b.newPage({ viewport: { width, height: 800 } });
await p.goto(pathToFileURL(page).href);
await p.waitForFunction(() => document.title === 'ready' && [...document.images].every((im) => im.complete), null, { timeout: 30000 });
await p.screenshot({ path: out, fullPage: true });
await b.close();
rmSync(page);
console.log(`contact-sheet: ${frames.length} frames -> ${out}`);
