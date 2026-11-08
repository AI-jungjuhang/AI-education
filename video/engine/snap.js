// 사용법: node snap.js <scene.html> <출력 접두사> <초1,초2,...>   (장면 파일을 시점별로 PNG로 저장)
const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const [html, out, ts] = process.argv.slice(2);
  const b = await chromium.launch(); const ctx = await b.newContext({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  const p = await ctx.newPage(); await p.goto('file://' + path.resolve(html), { waitUntil: 'networkidle' }).catch(() => {});
  for (const t of ts.split(',')) { await p.evaluate(x => window.seek(x), +t); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(250);
    await p.screenshot({ path: `${out}_${t}.png` }); }
  await b.close();
})();
