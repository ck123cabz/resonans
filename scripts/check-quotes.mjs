#!/usr/bin/env node
// Checks that every quote on a paper card is the source's own words.
// Usage: node scripts/check-quotes.mjs <project>
// Reads <project>/data/docs.json: each card with a `body` shows the body with {0}, {1} filled from
// `hl`, and "…" marks a cut. Every piece between cuts must appear word for word in
// <project>/sources/<src>.txt, a plain-text copy of the source saved when the card was written.
// Exits 1 on a missing quote, a missing source file, or no cards read.
import { existsSync, readFileSync } from 'node:fs';
import { join, resolve } from 'node:path';

const dir = resolve(process.argv[2] || '.');
const file = join(dir, 'data/docs.json');
if (!existsSync(file)) {
  console.error(`check-quotes: no ${file}`);
  process.exit(1);
}

// Typography, quotation marks and line wrapping may differ between a card and its source; the words may not.
const norm = (s) => s
  .replace(/­/g, '')
  .replace(/(\w)-\s*\n\s*(\w)/g, '$1$2')
  .replace(/[‘’ʼ]/g, "'")
  .replace(/[“”"]/g, '')
  .replace(/[–—]/g, '-')
  .replace(/\s+/g, ' ')
  .toLowerCase();

const docs = JSON.parse(readFileSync(file, 'utf8'));
const cards = (docs.cards || []).filter((c) => c.body);
const texts = {};
let pieces = 0;
const fails = [];

for (const [i, c] of cards.entries()) {
  const path = join(dir, 'sources', `${c.src}.txt`);
  if (!existsSync(path)) {
    fails.push(`card ${i}: no source file sources/${c.src}.txt`);
    continue;
  }
  texts[c.src] ??= norm(readFileSync(path, 'utf8'));
  const shown = c.body.replace(/\{(\d+)\}/g, (_, n) => c.hl[+n][0]);
  for (const piece of shown.split('…').map((p) => p.trim().replace(/^[\s,.;:]+|[\s,.;:]+$/g, ''))) {
    if (!piece) continue;
    pieces++;
    if (!texts[c.src].includes(norm(piece))) fails.push(`card ${i} (${c.src}): "${piece}" is not in the source`);
  }
}

const chars = Object.values(texts).reduce((a, t) => a + t.length, 0);
console.log(`check-quotes: ${cards.length} cards, ${pieces} quoted pieces, ${Object.keys(texts).length} sources (${chars} chars)`);
if (!cards.length || !pieces) {
  console.error('check-quotes: no quotes read');
  process.exit(1);
}
for (const f of fails) console.error(`  FAIL ${f}`);
process.exit(fails.length ? 1 : 0);
