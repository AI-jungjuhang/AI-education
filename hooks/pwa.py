"""빌드가 끝나면 서비스 워커(sw.js)를 만든다 (2026-11-18, 앱 설치 지원).
- CORE_FILES: 앱 뼈대(홈, 설치 안내, 스타일, 스크립트, 아이콘, 감자 그림)
- ALL_PAGES: 모든 페이지. "책 전체 저장하기"를 누르면 받아 둔다
- VERSION: 뼈대 파일 내용으로 만든 해시. 바뀌면 새 서비스 워커가 옛 저장본을 지운다"""
import hashlib, json, os

SW = r'''/* AI 정주행 서비스 워커 (빌드할 때 hooks/pwa.py가 만든다. 직접 고치지 말 것)
   - 설치할 때: 앱 뼈대만 저장
   - 페이지: 인터넷이 되면 새로 받아 저장하고, 안 되면 저장해 둔 것을 보여 준다
   - "책 전체 저장하기" 요청이 오면 모든 페이지를 받아 둔다 */
const VERSION = "__VERSION__";
const CORE = "aj-core-" + VERSION;
const PAGES = "aj-pages-v1";
const ASSETS = "aj-assets-v1";
const CORE_FILES = __CORE__;
const ALL_PAGES = __PAGES__;

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
'''

def on_post_build(config, **kwargs):
    site = config["site_dir"]
    core, pages = [], []
    for root, _, files in os.walk(site):
        for f in files:
            rel = os.path.relpath(os.path.join(root, f), site).replace(os.sep, "/")
            if f == "index.html":
                d = rel[:-len("index.html")]
                if d.startswith("404") or d.startswith("search"):
                    continue
                pages.append(d or "./")
            elif rel.startswith(("assets/icons/", "javascripts/", "stylesheets/")) or (rel.startswith("assets/") and rel.endswith(".svg")) \
                    or (rel.startswith("assets/javascripts/") and rel.endswith(".min.js") and "/lunr/" not in rel) or (rel.startswith("assets/stylesheets/") and rel.endswith(".min.css")) \
                    or rel == "manifest.webmanifest":
                core.append(rel)
    core = sorted(set(core + ["./", "install/"]))
    pages = sorted(set(pages))
    h = hashlib.sha1()
    for rel in core:
        p = os.path.join(site, rel)
        if os.path.isfile(p):
            h.update(open(p, "rb").read())
    sw = SW.replace("__VERSION__", h.hexdigest()[:12]).replace("__CORE__", json.dumps(core, ensure_ascii=False)).replace("__PAGES__", json.dumps(pages, ensure_ascii=False))
    open(os.path.join(site, "sw.js"), "w", encoding="utf-8").write(sw)
