/**
 * Dati aggiornati per la mappa: sistemi, stato Controllato / Non Controllato, Material Trader,
 * Technology Broker e Interstellar Factor arrivano dal server dello Squadrone (/v1/site: Spansh più
 * EDDN), oppure, se non risponde, dal bgs.json dell'ACFS BGS Tool. sistemi.json resta la base per
 * quello che si scrive a mano (categorie, Capitale, note "infos", Spedizione Verso il Niente) e la
 * copia di riserva se nessuna delle due fonti risponde.
 *
 * Prima (fino a ottobre 2026) questi dati li scriveva in sistemi.json spansh_sync.py, lanciato a mano.
 */
(function () {
  var SITE_API = 'https://api.flottastellare.it/v1/site';
  var TOOL_DATA = 'https://flottastellare.it/acfs-bgs-tool/data/bgs.json';
  var FACTION = 'Flotta Stellare';
  var TIMEOUT_MS = 8000;
  var CAPITALE = 0, CONTROLLATO = 1, NON_CONTROLLATO = 2, INTERSTELLAR_FACTOR = 6;
  var MATERIAL_TRADER = { Raw: 3, Manufactured: 4, Encoded: 5 };
  var TECH_BROKER = { Human: 7, Guardian: 8 };
  // Un elenco con molti meno sistemi della mappa è più probabilmente una risposta sbagliata che una ritirata in massa.
  var MIN_SHARE = 0.8;

  /** Per provare in locale con l'API sul proprio PC: /map/?api=http://localhost:8081/v1/site (solo su localhost). */
  if (location.hostname === 'localhost') {
    var override = new URLSearchParams(location.search).get('api');
    if (override) SITE_API = override;
  }

  function getJson(url) {
    var controller = new AbortController();
    var timer = setTimeout(function () { controller.abort(); }, TIMEOUT_MS);
    return fetch(url, { signal: controller.signal })
      .then(function (r) {
        if (!r.ok) throw new Error(url + ': HTTP ' + r.status);
        return r.json();
      })
      .finally(function () { clearTimeout(timer); });
  }

  /** Da /v1/site: i sistemi in cui siamo presenti e con le coordinate. */
  function fromSite(data) {
    return {
      label: 'server ACFS (Spansh ed EDDN)',
      at: data.spansh_fetched_at,
      systems: data.systems.filter(function (s) { return s.present && s.x !== null; }).map(function (s) {
        return { name: s.name, x: s.x, y: s.y, z: s.z, controlled: s.controlled, services: s.services };
      }),
    };
  }

  /** Dal bgs.json del tool: gli stessi dati, con i servizi da riassumere stazione per stazione. */
  function fromTool(data) {
    return {
      label: 'ACFS BGS Tool (Spansh)',
      at: data.generated_at,
      systems: data.results.map(function (s) {
        var assets = s.assets || [];
        var kinds = function (field) {
          return assets.map(function (a) { return a[field]; }).filter(function (v) { return typeof v === 'string'; });
        };
        return {
          name: s.name, x: s.x, y: s.y, z: s.z,
          controlled: s.controlling_minor_faction === FACTION,
          services: {
            material_trader: kinds('material_trader'),
            technology_broker: kinds('technology_broker'),
            interstellar_factors: assets.some(function (a) { return a.interstellar_factors === true; }),
          },
        };
      }),
    };
  }

  function serviceCats(services) {
    var cats = [];
    services.material_trader.forEach(function (k) { if (MATERIAL_TRADER[k] !== undefined) cats.push(MATERIAL_TRADER[k]); });
    if (services.interstellar_factors) cats.push(INTERSTELLAR_FACTOR);
    services.technology_broker.forEach(function (k) { if (TECH_BROKER[k] !== undefined) cats.push(TECH_BROKER[k]); });
    return cats.filter(function (c, i) { return cats.indexOf(c) === i; }).sort(function (a, b) { return a - b; });
  }

  /**
   * sistemi.json con i dati aggiornati: per i sistemi della Flotta (cat numerica) coordinate e categorie
   * vengono dalla fonte, note "infos" restano; la Capitale tiene la categoria 0; i sistemi nuovi si
   * aggiungono, quelli in cui non siamo più si tolgono. Le voci della Spedizione restano come sono.
   */
  function merge(base, live) {
    var byName = {};
    live.systems.forEach(function (s) { byName[s.name.toLowerCase()] = s; });
    var used = {};
    var fleet = [], others = [];
    base.systems.forEach(function (entry) {
      if (typeof entry.cat[0] !== 'number') { others.push(entry); return; }
      var key = entry.name.toLowerCase();
      var s = byName[key];
      if (!s) {
        if (entry.cat[0] === CAPITALE) fleet.push(entry);
        return;
      }
      used[key] = true;
      var status = [s.controlled ? CONTROLLATO : NON_CONTROLLATO];
      if (entry.cat[0] === CAPITALE) status.unshift(CAPITALE);
      fleet.push($.extend({}, entry, { coords: { x: s.x, y: s.y, z: s.z }, cat: status.concat(serviceCats(s.services)) }));
    });
    live.systems.forEach(function (s) {
      if (used[s.name.toLowerCase()]) return;
      fleet.push({ name: s.name, coords: { x: s.x, y: s.y, z: s.z }, cat: [s.controlled ? CONTROLLATO : NON_CONTROLLATO].concat(serviceCats(s.services)) });
    });
    return $.extend({}, base, { systems: fleet.concat(others) });
  }

  function fleetCount(base) {
    return base.systems.filter(function (s) { return typeof s.cat[0] === 'number'; }).length;
  }

  /**
   * Carica sistemi.json e i dati aggiornati, poi chiama done(json, info): info dice da dove vengono i
   * dati (label) e di quando (at, ISO), oppure stale: true se si usa solo sistemi.json.
   */
  window.acfsMapData = function (basePath, done) {
    getJson(basePath).then(function (base) {
      var tryLive = function (url, convert) {
        return getJson(url).then(function (data) {
          var live = convert(data);
          if (live.systems.length < fleetCount(base) * MIN_SHARE) throw new Error(url + ': solo ' + live.systems.length + ' sistemi');
          return live;
        });
      };
      tryLive(SITE_API, fromSite)
        .catch(function (err) {
          console.warn('Mappa: server non disponibile, uso il bgs.json del tool', err);
          return tryLive(TOOL_DATA, fromTool);
        })
        .then(function (live) {
          done(merge(base, live), { label: live.label, at: live.at });
        })
        .catch(function (err) {
          console.warn('Mappa: dati aggiornati non disponibili, uso sistemi.json', err);
          done(base, { stale: true });
        });
    });
  };
})();
