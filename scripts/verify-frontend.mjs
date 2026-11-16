#!/usr/bin/env node
/**
 * Frontend integrity verification: extracts every inline <script> block
 * from index.html and syntax-checks it, then validates HTML tag balance.
 * Exit 1 on any failure; exit 0 when clean.
 */
import { readFileSync } from "node:fs";
import { spawnSync } from "node:child_process";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const html = readFileSync(join(root, "index.html"), "utf8");

let failures = 0;

// 1. Inline script syntax checks
const scripts = [...html.matchAll(/<script(?![^>]*type="application\/ld\+json")[^>]*>([\s\S]*?)<\/script>/g)];
scripts.forEach((m, i) => {
  const code = m[1];
  if (!code.trim()) return;
  const res = spawnSync("node", ["--check"], { input: code, encoding: "utf8" });
  if (res.status !== 0) {
    failures++;
    console.error(`FAIL: script block #${i} has a syntax error:\n${res.stderr}`);
  } else {
    console.log(`ok ${i} - script block syntax valid`);
  }
});

// 2. Tag balance check.
// Strip script/style block contents first: HTML-like strings inside JS
// template literals are string data, not DOM, and must not be matched.
const htmlForBalance = html
  .replace(/<script[^>]*>[\s\S]*?<\/script>/gi, "<script></script>")
  .replace(/<style[^>]*>[\s\S]*?<\/style>/gi, "<style></style>");

const VOID = new Set(["area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"]);
const stack = [];
const tagRe = /<\/?([a-zA-Z][a-zA-Z0-9-]*)\b[^>]*?(\/?)>/g;
let m;
while ((m = tagRe.exec(htmlForBalance)) !== null) {
  const [full, tag, selfClose] = m;
  const t = tag.toLowerCase();
  if (VOID.has(t) || selfClose === "/") continue;
  if (full.startsWith("</")) {
    const top = stack[stack.length - 1];
    if (top === t) {
      stack.pop();
    } else {
      failures++;
      console.error(`FAIL: mismatched </${t}> at offset ${m.index}, expected </${top || "nothing"}>`);
      break;
    }
  } else {
    stack.push(t);
  }
}
if (stack.length > 0) {
  failures++;
  console.error(`FAIL: ${stack.length} unclosed tag(s): ${stack.join(", ")}`);
} else {
  console.log("ok - HTML tag balance valid");
}

// 3. Promo burner packshots: every referenced packshot must exist and carry
// valid WebP magic bytes. shortcut: validates headers, not a full browser
// decode; upgrade when CI runs a real browser.
const packshots = [...new Set([...html.matchAll(/images\/products\/(prod-[a-z0-9-]+\.webp)/g)].map(m => m[1]))];
for (const name of packshots) {
  try {
    const buf = readFileSync(join(root, "images", "products", name));
    const isWebp = buf.length > 12 &&
      buf.subarray(0, 4).toString("latin1") === "RIFF" &&
      buf.subarray(8, 12).toString("latin1") === "WEBP";
    if (!isWebp) {
      failures++;
      console.error(`FAIL: promo packshot ${name} is not a valid WebP file`);
    } else {
      console.log(`ok - promo packshot ${name} present and valid (${buf.length} bytes)`);
    }
  } catch {
    failures++;
    console.error(`FAIL: promo packshot ${name} referenced in index.html but missing from images/products/`);
  }
}

if (failures > 0) {
  console.error(`\n${failures} integrity check(s) failed`);
  process.exit(1);
}
console.log("\nAll frontend integrity checks passed");
