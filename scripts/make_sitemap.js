#!/usr/bin/env node
/* Generates sitemap.xml from shared/catalog.js (all product detail URLs). */
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const root = path.join(__dirname, '..');
const sandbox = { window: {} };
vm.createContext(sandbox);
vm.runInContext(fs.readFileSync(path.join(root, 'shared', 'offer-policy.js'), 'utf8'), sandbox);
vm.runInContext(fs.readFileSync(path.join(root, 'shared', 'catalog.js'), 'utf8'), sandbox);
const products = sandbox.window.PRIMARY_CATALOG;

const BASE = 'https://thedifference-za.pages.dev';
const urls = [
  { loc: `${BASE}/`, priority: '1.0', changefreq: 'daily' },
  ...products.map(p => ({
    loc: `${BASE}/?product=${p.id}`,
    priority: '0.8',
    changefreq: 'daily',
  })),
];

const today = new Date().toISOString().slice(0, 10);
const xml =
  '<?xml version="1.0" encoding="UTF-8"?>\n' +
  '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
  urls
    .map(
      u =>
        `  <url>\n    <loc>${u.loc}</loc>\n    <lastmod>${today}</lastmod>\n    <changefreq>${u.changefreq}</changefreq>\n    <priority>${u.priority}</priority>\n  </url>`
    )
    .join('\n') +
  '\n</urlset>\n';

fs.writeFileSync(path.join(root, 'sitemap.xml'), xml);
console.log(`sitemap.xml written with ${urls.length} URLs`);
