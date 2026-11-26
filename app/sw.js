// お祭りカレンダー：画面はキャッシュから素早く開き、お祭りデータはネットを優先（つながらないときは前回のデータ）
var CACHE = "omatsuri-app-v1";
var SHELL = ["/app/", "/app/index.html", "/app/manifest.webmanifest", "/app/icon-192.png", "/app/icon-512.png"];
self.addEventListener("install", function (e) {
  e.waitUntil(caches.open(CACHE).then(function (c) { return c.addAll(SHELL); }).then(function () { return self.skipWaiting(); }));
});
self.addEventListener("activate", function (e) {
  e.waitUntil(caches.keys().then(function (ks) {
    return Promise.all(ks.filter(function (k) { return k !== CACHE; }).map(function (k) { return caches.delete(k); }));
  }).then(function () { return self.clients.claim(); }));
});
self.addEventListener("fetch", function (e) {
  var u = new URL(e.request.url);
  if (u.origin !== location.origin || !u.pathname.startsWith("/app/")) return;
  if (u.pathname.endsWith("festivals.json")) {
    e.respondWith(fetch(e.request).then(function (r) {
      var cp = r.clone(); caches.open(CACHE).then(function (c) { c.put(e.request, cp); }); return r;
    }).catch(function () { return caches.match(e.request); }));
    return;
  }
  e.respondWith(caches.match(e.request).then(function (hit) {
    var net = fetch(e.request).then(function (r) {
      var cp = r.clone(); caches.open(CACHE).then(function (c) { c.put(e.request, cp); }); return r;
    }).catch(function () { return hit; });
    return hit || net;
  }));
});
