#!/usr/bin/env node
/**
 * Real-browser smoke test: loads index.html in headless Chromium, opens the
 * promo burner, asserts every packshot decodes and no uncaught page errors.
 * On failure, saves smoke-failure.png (CI uploads it as an artifact).
 */
import { chromium } from "playwright";
import { createServer } from "node:http";
import { join, extname, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { readFileSync, existsSync } from "node:fs";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const MIME = {
  ".html": "text/html", ".webp": "image/webp", ".png": "image/png",
  ".jpg": "image/jpeg", ".svg": "image/svg+xml", ".css": "text/css", ".js": "text/javascript"
};

const server = createServer((req, res) => {
  const path = req.url === "/" ? "index.html" : req.url.slice(1).split("?")[0];
  const file = join(root, path);
  if (!file.startsWith(root) || !existsSync(file)) {
    res.writeHead(404).end();
    return;
  }
  res.writeHead(200, { "Content-Type": MIME[extname(file)] || "application/octet-stream" });
  res.end(readFileSync(file));
});

await new Promise(resolve => server.listen(0, "127.0.0.1", resolve));
const port = server.address().port;

const browser = await chromium.launch({
  args: ["--no-sandbox", "--disable-gpu"],
  ...(process.env.PLAYWRIGHT_CHROMIUM_PATH ? { executablePath: process.env.PLAYWRIGHT_CHROMIUM_PATH } : {})
});

const page = await browser.newPage();
const pageErrors = [];
page.on("pageerror", e => pageErrors.push(e.message));

const fail = async msg => {
  console.error(`FAIL: ${msg}`);
  await page.screenshot({ path: "smoke-failure.png" }).catch(() => {});
  server.close();
  await browser.close();
  process.exit(1);
};

try {
  await page.goto(`http://127.0.0.1:${port}/index.html`, { waitUntil: "load", timeout: 30000 });
  await page.locator("#promoAnnouncementModal").evaluate(m => m.showModal());

  const packshots = await page.evaluate(async () => {
    const modal = document.getElementById("promoAnnouncementModal");
    const imgs = [...modal.querySelectorAll("img")];
    await Promise.all(imgs.map(i => i.complete ? null : new Promise(r => { i.onload = i.onerror = r; })));
    return imgs.map(i => ({
      src: i.src.split("/").pop(),
      ok: i.complete && i.naturalWidth > 0
    }));
  });

  if (packshots.length < 4) await fail(`expected 4 promo packshots, found ${packshots.length}`);
  const broken = packshots.filter(p => !p.ok);
  if (broken.length > 0) await fail(`broken packshots: ${broken.map(p => p.src).join(", ")}`);
  if (pageErrors.length > 0) await fail(`uncaught page errors: ${pageErrors.join(" | ")}`);
  console.log(`ok - all ${packshots.length} promo packshots loaded and decoded in real Chromium`);
  console.log("ok - zero uncaught page errors");
} catch (e) {
  await fail(`navigation failed: ${e.message.split("\n")[0]}`);
}

server.close();
await browser.close();
console.log("ok - zero uncaught page errors confirmed");
