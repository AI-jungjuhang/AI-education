// 사용법: node render.js <scene.html 경로> <프레임 폴더> <timeline.json 경로> [fps=30] [workers=4]
// scene.html의 seek(t)로 시간을 정해 프레임마다 JPEG를 저장하고, 효과음 위치(timeline.json)를 장면 파일에서 뽑아 저장한다.
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const SCENE = process.argv[2], out = process.argv[3], TL = process.argv[4], FPS = +(process.argv[5] || 30), W = +(process.argv[6] || 4);
fs.mkdirSync(out, { recursive: true });
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  const url = 'file://' + path.resolve(SCENE);
  const pages = [];
  for (let i = 0; i < W; i++) {
    const p = await ctx.newPage(); await p.goto(url, { waitUntil: 'networkidle' }).catch(() => {});
    // 글꼴 조각이 모두 내려받아지도록 모든 장면의 글자를 한 번씩 그려 본다
    const total = await p.evaluate(() => window.collectSfx().total * 60 / 128);
    for (let t = 1; t < total; t += 2.5) { await p.evaluate(x => window.seek(x), t); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(200); }
    pages.push(p);
  }
  console.log('Pretendard 로드:', await pages[0].evaluate(() => document.fonts.check('900 40px "Pretendard Variable"')));
  const tl = await pages[0].evaluate(() => window.collectSfx());
  fs.writeFileSync(TL, JSON.stringify(tl, null, 1));
  const D = tl.total * 60 / tl.bpm, N = Math.round(D * FPS);
  console.log(`길이 ${D.toFixed(2)}초, 프레임 ${N}, 효과음 ${tl.sfx.length}개`);
  let done = 0;
  await Promise.all(pages.map(async (p, w) => {
    for (let i = w; i < N; i += W) {
      await p.evaluate(x => window.seek(x), Math.min(i / FPS, D - 0.001));
      await p.screenshot({ path: path.join(out, `f${String(i).padStart(5, '0')}.jpg`), type: 'jpeg', quality: 92 });
      if (++done % 300 === 0) console.log(`${done}/${N}`);
    }
  }));
  await b.close(); console.log('프레임 완료', N);
})();
