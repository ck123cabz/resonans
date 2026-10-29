#!/usr/bin/env node
// Transcribe a video/audio file locally (whisper.cpp via `hyperframes transcribe`)
// -> the same word-level JSON shape transcribe-elevenlabs.mjs writes, so
// cut-silences and cut-mistakes take it unchanged. Free, no API key.
//
// Usage:
//   node scripts/transcribe-local.mjs <input> [--output path] [--model small.en]
//
// Writes <input-without-ext>.json next to the source:
//   { text, audio_duration_secs, words: [{ text, start, end, type: "word" }] }
//
// Whisper misspells local names ("Dumaguete" -> "Duma Gated"). Timing stays
// right; fix the word text during cut-mistakes review, never the timestamps.

import { readFileSync, writeFileSync, existsSync, mkdtempSync, rmSync } from "node:fs";
import { dirname, join, resolve, basename, extname } from "node:path";
import { tmpdir } from "node:os";
import { spawnSync } from "node:child_process";
import { argv, exit } from "node:process";

function die(msg) {
  console.error(msg);
  exit(1);
}

const args = argv.slice(2);
const opts = { input: null, output: null, model: "small.en" };
for (let i = 0; i < args.length; i++) {
  const a = args[i];
  if (a === "--output" || a === "-o") opts.output = args[++i];
  else if (a === "--model" || a === "-m") opts.model = args[++i];
  else if (a.startsWith("--")) die(`unknown option: ${a}`);
  else if (!opts.input) opts.input = a;
  else die(`unexpected argument: ${a}`);
}
if (!opts.input) die("usage: node scripts/transcribe-local.mjs <input> [--output path] [--model small.en]");

const inputPath = resolve(opts.input);
if (!existsSync(inputPath)) die(`input not found: ${inputPath}`);
const outputPath = resolve(
  opts.output ?? join(dirname(inputPath), `${basename(inputPath, extname(inputPath))}.json`),
);

const probe = spawnSync(
  "ffprobe",
  ["-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", inputPath],
  { encoding: "utf8" },
);
const duration = Number(probe.stdout.trim());
if (probe.status !== 0 || !Number.isFinite(duration)) die(`ffprobe failed on ${inputPath}: ${probe.stderr}`);

// hyperframes writes transcript.json into --dir; use a scratch dir so a
// project's own caption transcript is never overwritten.
const work = mkdtempSync(join(tmpdir(), "transcribe-local-"));
try {
  const run = spawnSync(
    "npx",
    ["hyperframes", "transcribe", inputPath, "--dir", work, "--model", opts.model, "--json"],
    { encoding: "utf8", stdio: ["ignore", "pipe", "inherit"] },
  );
  if (run.status !== 0) die(`hyperframes transcribe exited ${run.status}`);

  const words = JSON.parse(readFileSync(join(work, "transcript.json"), "utf8"));
  if (!Array.isArray(words) || words.length === 0) die("transcriber returned no words");

  const result = {
    text: words.map((w) => w.text).join(" "),
    audio_duration_secs: duration,
    words: words.map((w) => ({ text: w.text, start: w.start, end: w.end, type: "word" })),
  };
  writeFileSync(outputPath, JSON.stringify(result, null, 2) + "\n");
  console.log(`${words.length} words, ${duration.toFixed(2)}s -> ${outputPath}`);
} finally {
  rmSync(work, { recursive: true, force: true });
}
