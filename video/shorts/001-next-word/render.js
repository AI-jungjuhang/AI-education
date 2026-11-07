// 사용법: node render.js <프레임 폴더> [fps=30] [workers=4]
// scene.html의 seek(t)로 시간을 정해 프레임마다 JPEG를 저장한다. 같은 입력이면 같은 영상이 나온다.
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const out = process.argv[2], FPS = +(process.argv[3] || 30), W = +(process.argv[4] || 4);
const D = 58, N = D * FPS;
fs.mkdirSync(out, { recursive: true });
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  const url = 'file://' + path.resolve(__dirname, 'scene.html');
  const pages = [];
  for (let i = 0; i < W; i++) {
    const p = await ctx.newPage(); await p.goto(url, { waitUntil: 'networkidle' }).catch(() => {});
    // 글꼴 조각이 모두 내려받아지도록 모든 장면의 글자를 한 번씩 그려 본다
    for (const t of [1, 8, 15, 24, 34, 42, 50, 56]) { await p.evaluate(x => window.seek(x), t); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(250); }
    pages.push(p);
  }
  const check = await pages[0].evaluate(() => document.fonts.check('800 40px "Pretendard Variable"'));
  console.log('Pretendard 로드:', check);
  let done = 0;
  await Promise.all(pages.map(async (p, w) => {
    for (let i = w; i < N; i += W) {
      await p.evaluate(x => window.seek(x), i / FPS);
      await p.screenshot({ path: path.join(out, `f${String(i).padStart(5, '0')}.jpg`), type: 'jpeg', quality: 92 });
      if (++done % 300 === 0) console.log(`${done}/${N}`);
    }
  }));
  await b.close(); console.log('프레임 완료', N);
})();
