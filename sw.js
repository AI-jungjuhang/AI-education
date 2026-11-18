/* AI 정주행 서비스 워커 (빌드할 때 hooks/pwa.py가 만든다. 직접 고치지 말 것)
   - 설치할 때: 앱 뼈대만 저장
   - 페이지: 인터넷이 되면 새로 받아 저장하고, 안 되면 저장해 둔 것을 보여 준다
   - "책 전체 저장하기" 요청이 오면 모든 페이지를 받아 둔다 */
const VERSION = "ba626b03f511";
const CORE = "aj-core-" + VERSION;
const PAGES = "aj-pages-v1";
const ASSETS = "aj-assets-v1";
const CORE_FILES = ["./", "assets/icons/apple-touch-icon.png", "assets/icons/icon-192.png", "assets/icons/icon-512.png", "assets/icons/maskable-192.png", "assets/icons/maskable-512.png", "assets/javascripts/bundle.60a45f97.min.js", "assets/javascripts/workers/search.f8cc74c7.min.js", "assets/potato-grin.svg", "assets/potato-logo.svg", "assets/potato-smile.svg", "assets/potato-wow.svg", "assets/potato.svg", "assets/stylesheets/main.a40c8224.min.css", "assets/stylesheets/palette.06af60db.min.css", "install/", "javascripts/app.js", "javascripts/potato.js", "javascripts/reveal.js", "manifest.webmanifest", "stylesheets/extra.css"];
const ALL_PAGES = ["./", "appendix/", "appendix/glossary/", "appendix/prompt-bank/", "appendix/reading-order/", "appendix/references/", "appendix/review-log/", "install/", "part1/", "part1/ch01/", "part1/ch01/hallucination/", "part1/ch01/next-word/", "part1/ch01/tokens/", "part1/ch02/", "part1/ch02/context/", "part1/ch02/fresh-start/", "part1/ch02/iterate/", "part1/ch02/role-format/", "part1/ch02/specific/", "part1/ch02/templates/", "part1/ch03/", "part1/ch03/bias/", "part1/ch03/check-numbers/", "part1/ch03/check-sources/", "part1/ch03/copyright/", "part1/ch03/privacy/", "part1/ch03/second-opinion/", "part1/ch04/", "part1/ch04/choose/", "part1/ch04/free-paid/", "part1/ch04/kinds/", "part2/", "part2/ch05/", "part2/ch05/first-draft/", "part2/ch05/rewrite/", "part2/ch05/summarize/", "part2/ch06/", "part2/ch06/long-docs/", "part2/ch06/quick-intro/", "part2/ch06/tutor/", "part2/ch07/", "part2/ch07/math-caution/", "part2/ch07/meeting-notes/", "part2/ch07/tables/", "part2/ch08/", "part2/ch08/prompt-library/", "part2/ch08/rollout-check/", "part2/ch08/team-rules/", "part3/", "part3/ch09/", "part3/ch09/pretraining/", "part3/ch09/scale/", "part3/ch09/tuning/", "part3/ch10/", "part3/ch10/closeness/", "part3/ch10/context-meaning/", "part3/ch10/tokens-to-vectors/", "part3/ch11/", "part3/ch11/attention-idea/", "part3/ch11/context-window/", "part3/ch11/transformer-layer/", "part3/ch12/", "part3/ch12/long-answer/", "part3/ch12/sampling/", "part3/ch12/temperature/", "part4/", "part4/ch13/", "part4/ch13/connectors/", "part4/ch13/files-code/", "part4/ch13/search-rag/", "part4/ch14/", "part4/ch14/failures/", "part4/ch14/loop/", "part4/ch14/what-agent/", "part4/ch15/", "part4/ch15/evaluate/", "part4/ch15/instructions/", "part4/ch15/tool-design/", "part5/", "part5/ch16/", "part5/ch16/checkpoint-rewind/", "part5/ch16/checkpoint-vs-git/", "part5/ch16/claudemd-intro/", "part5/ch16/claudemd-write/", "part5/ch16/cli-modes/", "part5/ch16/cli-pipe/", "part5/ch16/slash-basics/", "part5/ch16/slash-custom/", "part5/ch17/", "part5/ch17/hook-basics/", "part5/ch17/hook-checker/", "part5/ch17/hook-safety/", "part5/ch17/mcp-connect/", "part5/ch17/mcp-intro/", "part5/ch17/mcp-token-safety/", "part5/ch17/skill-anatomy/", "part5/ch17/skill-safety/", "part5/ch17/skill-video/", "part5/ch17/subagent-intro/", "part5/ch17/subagent-team/", "part5/ch17/subagent-vs-mcp/", "part5/ch18/", "part5/ch18/agent-teams/", "part5/ch18/background-tasks/", "part5/ch18/cli-automation/", "part5/ch18/permissions/", "part5/ch18/plan-mode/", "part5/ch18/plugin-bundle/", "part5/ch18/super-skill/", "part6/", "part6/ch19/", "part6/ch19/circuits/", "part6/ch19/features/", "part6/ch19/interp-intro/", "part6/ch20/", "part6/ch20/alignment/", "part6/ch20/rl-reasoning/", "part6/ch20/scaling/", "part6/ch21/", "part6/ch21/benchmarks/", "part6/ch21/eval-hallu/", "part6/ch21/risks/", "part6/ch22/", "part6/ch22/altman/", "part6/ch22/amodei/", "part6/ch22/hassabis/", "part6/ch22/hinton/", "part6/ch22/karpathy/", "part6/ch22/views-compare/", "part6/ch23/", "part6/ch23/context-fill/", "part6/ch23/context-habits/", "part6/ch23/model-choice/", "part6/ch23/model-effort/", "part6/ch23/prompt-agent/", "part6/ch23/prompt-why/", "part6/ch23/verify-build/", "part6/ch23/verify-loop/"];

self.addEventListener("install", (e) => {
  e.waitUntil(caches.open(CORE).then((c) => c.addAll(CORE_FILES)).then(() => self.skipWaiting()));
});
self.addEventListener("activate", (e) => {
  e.waitUntil(caches.keys().then((keys) => Promise.all(keys.filter((k) => k.startsWith("aj-core-") && k !== CORE).map((k) => caches.delete(k)))).then(() => self.clients.claim()));
});
function isPage(req) { return req.mode === "navigate" || (req.headers.get("accept") || "").includes("text/html"); }
async function pageFirstNetwork(req) {
  const cache = await caches.open(PAGES);
  const key = req.url.split("#")[0].split("?")[0];
  try {
    const res = await fetch(req);
    if (res.ok) cache.put(key, res.clone());
    return res;
  } catch (err) {
    return (await cache.match(key)) || (await caches.match(key)) ||
      (await caches.match(new URL("./", self.registration.scope).href)) ||
      new Response("<h1>오프라인이에요</h1><p>이 페이지는 아직 저장되지 않았어요. 인터넷에 연결되면 다시 열어 주세요.</p>", {headers: {"Content-Type": "text/html; charset=utf-8"}});
  }
}
async function assetCacheFirst(req) {
  const hit = await caches.match(req);
  if (hit) return hit;
  try {
    const res = await fetch(req);
    if (res.ok || res.type === "opaque") (await caches.open(ASSETS)).put(req, res.clone());
    return res;
  } catch (err) { return new Response("", {status: 504}); }
}
self.addEventListener("fetch", (e) => {
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  const sameOrigin = url.origin === self.location.origin;
  if (sameOrigin && !url.pathname.startsWith(new URL(self.registration.scope).pathname)) return;
  if (sameOrigin && isPage(req)) { e.respondWith(pageFirstNetwork(req)); return; }
  if (url.pathname.endsWith("search_index.json")) {
    e.respondWith(fetch(req).then((res) => { caches.open(ASSETS).then((c) => c.put(req, res.clone())); return res; }).catch(() => caches.match(req)));
    return;
  }
  e.respondWith(assetCacheFirst(req));
});
self.addEventListener("message", (e) => {
  if (!e.data || e.data.type !== "save-all") return;
  const port = e.ports[0];
  e.waitUntil((async () => {
    const cache = await caches.open(PAGES);
    let done = 0, failed = 0;
    for (const p of ALL_PAGES) {
      const url = new URL(p, self.registration.scope).href;
      try {
        if (!(await cache.match(url))) { const res = await fetch(url); if (res.ok) await cache.put(url, res); else failed++; }
      } catch (err) { failed++; }
      done++;
      if (port && (done % 5 === 0 || done === ALL_PAGES.length)) port.postMessage({done, total: ALL_PAGES.length, failed});
    }
    try { const idx = new URL("search/search_index.json", self.registration.scope).href; const r = await fetch(idx); if (r.ok) await (await caches.open(ASSETS)).put(idx, r); } catch (err) {}
    if (port) port.postMessage({done, total: ALL_PAGES.length, failed, finished: true});
  })());
});
