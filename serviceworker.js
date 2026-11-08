const CACHE = "pwabuilder-offline-v3";

const offlineFallbackPage = "index.html";

// Install stage sets up the index page (home page) in the cache and opens a new cache
self.addEventListener("install", function (event) {
  self.skipWaiting();

  event.waitUntil(
    caches.open(CACHE).then(function (cache) {
      return cache.add(offlineFallbackPage);
    })
  );
});

// Drop old cache versions and take control of already-open tabs immediately,
// instead of waiting for every tab to be closed before the update applies.
self.addEventListener("activate", function (event) {
  event.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(
        keys.filter(function (key) {
          return key !== CACHE;
        }).map(function (key) {
          return caches.delete(key);
        })
      );
    }).then(function () {
      return self.clients.claim();
    })
  );
});

// Only handle same-origin GET navigations: fetch from the network, and fall
// back to the cached offline page if the network is unavailable. Everything
// else (assets, and especially cross-origin third-party scripts like the
// cookie consent library, Google Analytics, Disqus) is left completely
// untouched so the service worker can never interfere with them.
self.addEventListener("fetch", function (event) {
  if (event.request.method !== "GET") return;
  if (event.request.mode !== "navigate") return;
  if (new URL(event.request.url).origin !== self.location.origin) return;
  // Il ACFS BGS Tool (/acfs-bgs-tool/) è una PWA a sé, con un proprio service worker:
  // se questo la intercettasse, in caso di rete assente le servirebbe la home del sito.
  if (new URL(event.request.url).pathname.indexOf("/acfs-bgs-tool/") === 0) return;

  event.respondWith(
    fetch(event.request).catch(function () {
      return caches.open(CACHE).then(function (cache) {
        return cache.match(offlineFallbackPage);
      });
    })
  );
});
