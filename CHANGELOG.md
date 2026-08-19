# Changelog

All notable changes to this project will be documented in this file.

## [1.8.0] - 2026-08-19 — Migrazione a GitHub Actions (preparata, non ancora attiva)

Preparata, sul branch `explore/github-actions-jekyll4`, la migrazione dalla pipeline legacy di
GitHub Pages ("Deploy from a branch", che ignora il `Gemfile` del repo e builda sempre con la gem
`github-pages` pinnata dal team di GitHub) a un deploy tramite GitHub Actions, che builda con le
gemme scelte da questo repo. Stesso schema già validato su skyflash.github.io e ipui2ipei.
**La pubblicazione in produzione resta quella legacy finché non si cambia manualmente il source in
Settings → Pages → Build and deployment**: questo aggiornamento da solo non cambia nulla sul sito
live.

### Migrazione build e nuovi workflow

- `Gemfile`: `jekyll ~> 4.3` e `jekyll-sass-converter ~> 3.0` (Dart Sass) dichiarati direttamente,
  non più lasciati risolvere implicitamente dalle gemme dei plugin; aggiunta `kramdown-parser-gfm`
  (prima arrivava come dipendenza transitiva). In locale la build già usava Jekyll 4.4.1 da tempo
  (il `Gemfile` non lo pinnava), quindi qui non c'è un salto di versione da verificare come per gli
  altri due siti — solo la build in produzione, ancora su Jekyll 3.9.x via `github-pages`, resta
  indietro finché non si completa la migrazione.
- `Gemfile.lock`: generato solo su Windows (piattaforma `x64-mingw-ucrt`), mancava la piattaforma
  `x86_64-linux` necessaria ai runner Ubuntu di GitHub Actions — stesso problema già risolto su
  skyflash.github.io. Aggiunta con `bundle lock --add-platform x86_64-linux`.
- Due nuovi workflow GitHub Actions:
  - `.github/workflows/build-check.yml`: build + `html-proofer` (link interni, immagini) su ogni
    push/pull request di ogni branch — solo verifica, nessuna pubblicazione.
  - `.github/workflows/pages.yml`: build + deploy vero e proprio su GitHub Pages
    (`actions/upload-pages-artifact`, `actions/deploy-pages`), attivo su push a `master` e
    manualmente. Nessun trigger schedulato (a differenza di skyflash.github.io): questo sito non ha
    post con data futura da pubblicare da soli.

### Nuovi plugin

- `jekyll-target-blank`: link esterni con `target="_blank" rel="noopener noreferrer"` automatico,
  in tutto il sito — cosa che finora non veniva fatta in nessun modo.

### Verifica

- Confrontata riga per riga la build legacy (Gemfile precedente) con quella nuova: CSS compilato
  byte-identico, nessun file mancante o in più, unica differenza reale gli attributi
  `target="_blank"`/`rel="noopener"` aggiunti da `jekyll-target-blank`.
- `html-proofer` non è eseguibile in locale su Windows (la gem `ethon`/`typhoeus` richiede
  `libcurl.dll`, assente di serie) — la prima verifica reale sui link è avvenuta al primo push del
  branch, su `build-check.yml` sul runner Ubuntu di Actions.

### Bug scovato (e corretto) dal nuovo controllo

- `_posts/2020-11-13-pianeta-morte.md`: due link del lightbox (righe 44 e 137) puntavano a
  `/images/posts/pianet-morte/...` invece di `/images/posts/pianeta-morte/...` — refuso mai
  notato perché il tag `<img>` della miniatura usava il percorso corretto, solo il link
  "apri a piena risoluzione" era rotto. Tollerato in silenzio dalla pipeline legacy, segnalato
  subito da `html-proofer` al primo run su CI. Corretto.

## [1.7.3] - 2026-08-16 — Una 404 a tema

### Added

- **Pagina 404 a tema** (`404.html`), standalone (nessun nav/header/footer del sito, giusto lo
  stile via `main.css`): al posto del generico "codice errore" mostra a caso uno dei quattro
  errori di connessione più noti fra i piloti di Elite Dangerous — Orange Sidewinder, Mauve Adder,
  Yellow Adder, Blue Cobra — colorato col colore che richiama il nome.

## [1.7.2] - 2026-08-16 — Google Analytics non partiva mai dopo la migrazione a GA4

### Fixed

- Lo script GA4 in `_includes/tracking.html` restava bloccato con `type="text/plain"` in attesa
  che `cookieconsent.html` lo attivasse al consenso dell'utente, ma la libreria
  `vanilla-cookieconsent` 3.1.0 non implementa quel meccanismo: il tag non è mai partito, a
  prescindere dal consenso dato. Individuato tramite Tag Assistant (nessun tag trovato anche dopo
  aver accettato i cookie) e confermato ispezionando il sorgente della libreria, che non contiene
  alcun riferimento a `text/plain`. Ora `tracking.html` definisce `loadAnalytics()`, chiamata solo
  dopo consenso esplicito tramite gli hook reali della libreria (`onConsent`/`onChange` in
  `cookieconsent.html`), mantenendo separata la logica di consenso da quella del tool di tracking.

## [1.7.1] - 2026-08-16 — Un solo script per sincronizzare tabella e mappa

### Changed

- `spansh_sync.py` ora aggiorna in un'unica esecuzione sia la tabella sistemi di `about/index.md`
  sia `map/json_files/sistemi.json`, con un solo fetch da Spansh condiviso fra i due: prima erano
  due fonti alimentate a mano in momenti diversi, con il rischio concreto di lasciarne una indietro
  rispetto all'altra (è già successo con `sistemi.json`, sincronizzato per la prima volta solo
  ieri). La logica di risincronizzazione della mappa (aggiunta sistemi, stato
  Controllato/Non Controllato, categorie Material Trader/Technology Broker/Interstellar Factor),
  scritta ieri in script temporanei di appoggio, è ora integrata in modo permanente in
  `spansh_sync.py` come funzione `sync_map()`. Resta un comando manuale (`python spansh_sync.py`),
  nessuno scheduling automatico è stato ancora deciso.
- Aggiornati i dati sincronizzati da Spansh in `about/index.md` (popolazioni, in continua
  variazione nel gioco).

## [1.7.0] - 2026-08-16 — Mappa 3D risincronizzata, ricerca sistemi e via di uscita

### Added

- **Ricerca sistemi nell'HUD della mappa 3D** (`map/js/components/hud.class.js`): campo di testo
  che centra la camera sul sistema cercato premendo Invio (match esatto, poi per sottostringa),
  forzando la visibilità del punto anche se un filtro categoria l'aveva nascosto; se non trova
  nulla mostra "Nessun sistema trovato". Il campo esisteva come stub HTML commentato da circa
  quattro anni, mai attivato — riattivato e collegato alla logica di selezione già usata dai click
  diretti sui sistemi.
- **Pulsante "← Torna al sito"** in basso a destra su `/map/`: prima la pagina (senza header/nav
  del sito, `layout: null`) non offriva alcuna via di uscita visibile, solo il tasto "indietro" del
  browser. La voce "Mappa 3D" nel menu (`_data/navigation.yml`, `_includes/nav.html`) ora si apre
  anche in una nuova scheda (`target="_blank" rel="noopener"`, tramite un flag `newtab: true`
  generico riusabile per altri link), così chi arriva dal sito non perde la pagina di partenza.

### Changed

- **`map/json_files/sistemi.json` risincronizzato da zero con l'API pubblica di Spansh** (stessa
  fonte già usata da `spansh_sync.py` per `about/index.md`, dato che EDSM resta non disponibile):
  - Da ~95 a 373 sistemi con presenza di Flotta Stellare (tutti quelli già tracciati in
    `about/index.md`), con coordinate reali.
  - Stato Controllato/Non Controllato ricalcolato da `controlling_minor_faction`; corretti 6
    sistemi rimasti disallineati nella versione precedente (BD+14 831, G 98-44, HIP 28774, LFT 392,
    LHS 1743 → Controllato; Toog → Non Controllato).
  - Categorie Material Trader (Raw/Manufactured/Encoded) e Technology Broker (Human/Guardian)
    popolate per la prima volta in modo sistematico, leggendo i campi dedicati
    `material_trader`/`technology_broker` dell'endpoint `stations/search` di Spansh (l'endpoint
    sistemi generico non distingue i sottotipi). Criterio "qualsiasi stazione nel sistema",
    validato al 100% contro le 30 categorizzazioni già presenti a mano nel file prima della
    risincronizzazione.
  - Rimossa la categoria "SDE" (Star Divinity Expedition): stub mai completato, zero sistemi
    taggati e rotta con placeholder "Checkpoint 4/5/6" mai sostituiti, eredità della demo della
    libreria originale.
  - Confermato (non un bug): `BD+08 1303` e `Iansan` restano entrambi in mappa con le stesse
    coordinate — sono lo stesso sistema fisico, rinominato dalla Flotta dopo la colonizzazione,
    tenuto volutamente doppio.
- **Font "Euro Caps" applicato ai titoli dell'HUD** della mappa (`map/css/styles.css`), coerente
  con `family-heading` usato nel resto del sito — prima il preload del font era rotto (attributo
  `as="eurocaps"` non valido, mai realmente applicato) e i titoli usavano Helvetica generico. Colore
  hover dei filtri cambiato dall'arancio generico `#FF7207` all'arancio ufficiale ACFS `#FF9D00`
  (già usato per il colore dei sistemi sulla mappa).
- `map/index.html` carica ora i sorgenti JS non minificati (`js/ed3dmap.js`, che a sua volta carica
  dinamicamente i singoli `js/components/*.class.js`) invece del bundle precostruito
  `js/ed3dmap.min.js`. Quel bundle risaliva a diversi anni fa e il codice stesso lo bypassa
  completamente quando presente (`if(typeof isMinified !== 'undefined') return
  Ed3d.launchMap();`) senza più ricaricare i componenti: qualunque modifica ai singoli file
  `.class.js`, passata o futura, non arrivava mai in produzione. Non esiste più un build tool
  (Grunt) nel repository per rigenerare il bundle, quindi si è scelto di servire i sorgenti diretti.

### Fixed

- `Action.addCursorOnSelect` (`map/js/components/action.class.js`) scriveva
  `cursor.hover.scale.set(...)` invece di `cursor.selection.scale.set(...)` — copia-incolla da
  `addCursorOnHover`. Il bug era mascherato da sempre perché un click reale è sempre preceduto da
  un movimento del mouse (che inizializza `cursor.hover`); selezionare un sistema tramite la nuova
  ricerca da tastiera lo bypassa e mandava in eccezione la creazione del cursore di selezione.
  Scoperto testando la ricerca in Chromium headless (nessun hover simulato).

## [1.6.3] - 2026-08-15 — Service worker meno invasivo

### Fixed

- Il link "Gestisci preferenze cookie" tornava a non rispondere in browser normale (funzionava solo
  nella PWA installata). Causa: `serviceworker.js` (boilerplate PWABuilder) intercettava *ogni*
  richiesta GET della pagina, incluse quelle cross-origin verso jsDelivr per `cookieconsent.umd.js`,
  e non aveva `skipWaiting()`/`clients.claim()` — le tab già aperte restavano quindi pilotate dalla
  versione precedente del worker finché non si chiudeva l'intero browser, mentre l'app PWA partiva
  spesso con un'istanza fresca. Riscritto per limitarsi al suo scopo reale (fallback offline sulla
  sola navigazione della pagina, stesso dominio); tutte le richieste di terze parti (cookie consent,
  Google Analytics, Disqus, ecc.) non passano più dal service worker. Aggiunti `skipWaiting()` +
  `clients.claim()` e versioning della cache (`pwabuilder-offline-v2`, con pulizia delle versioni
  vecchie) così un futuro aggiornamento si propaga subito, senza richiedere la chiusura di tutte le
  tab.

## [1.6.2] - 2026-08-15 — Trailblazers, Vanguards e Operations nel menu Il Gioco

### Added

- Tre nuove pagine sotto `about/`, nello stesso stile delle esistenti Elite Dangerous/BGS/Odyssey
  (fonti ufficiali linkate in fondo a ciascuna):
  - **`/trailblazers/`** — System Colonisation, l'aggiornamento gratuito lanciato il 26 febbraio
    2025 (ancora in beta) che permette di reclamare e sviluppare i propri sistemi stellari.
  - **`/vanguards/`** — rework completo del sistema Squadrons, lanciato il 19 agosto 2025:
    creazione/personalizzazione dello squadrone, nuova Squadron Home, Squadron Carrier e Squadron
    Bank, classifiche stagionali.
  - **`/operations/`** — scenari cooperativi in squadra, lanciato il 30 giugno 2026, richiede
    Odyssey.
- Aggiunte le tre voci al menu "Il Gioco" in `_data/navigation.yml`, nell'ordine Odyssey →
  Trailblazers → Vanguards → Operations.

## [1.6.1] - 2026-08-15 — Rifiniture navbar e icone social

### Changed

- Rimossa la voce testuale "Cerca" dal menu di navigazione (`_data/navigation.yml`): era ridondante
  con l'icona a lente già presente, non a caso il testo era identico ("Cerca"). Verificato che la
  pagina di ricerca (SimpleJekyllSearch, completamente lato client) non dipenda in alcun modo da
  quella voce — resta raggiungibile tramite l'icona.
- Bottone `<pwa-install>` restylizzato usando gli Shadow Parts della libreria
  (`::part(openButton)`), per farlo somigliare ai bottoni outline già usati nel resto del sito
  invece dello stile generico di default.
- Le icone social (nav e footer) mostrano ora il **colore reale del brand** al passaggio del mouse
  (Facebook, Twitter, YouTube, Instagram, Discord, Telegram), non più un unico arancione generico.
- Icone social riordinate: Discord, Facebook, (Twitter — solo footer), YouTube, Instagram,
  Telegram.
- Ridotta la spaziatura fra le icone e il padding del bottone `pwa-install`, per correggere un
  problema di layout introdotto dalla maggiore larghezza del bottone (il menu a tendina "Il Gioco"
  andava a capo e si posizionava male).

### Fixed

- L'icona Telegram era visibilmente disallineata rispetto alle altre: causata dalla classe
  `fa-lg`, rimasta sul markup, che ingrandiva solo quel glifo del 33% rompendo la centratura nel
  badge circolare condiviso con le altre icone. Rimossa.
- I nuovi colori brand in hover non si applicavano nonostante `!important`: la regola arancione
  generica preesistente era radicata su selettori con ID (`#nav`, `#footer`), sempre più specifici
  di semplici selettori di classe. Le nuove regole sono ora annidate nello stesso punto (dentro
  `@mixin color-list`), con pari specificità e ordine successivo, quindi vincono correttamente.

## [1.6.0] - 2026-08-14 — Favicon configurabile e PWA davvero installabile

### Added

- `favicon_path` in `_config.yml`: singolo punto di controllo per l'intero set di
  favicon/apple-touch-icon/android-icon/ms-tile. `head.html`, `map/index.html` e `manifest.json`
  derivano tutti da questo valore — per sostituire il set basta cambiarlo, niente più modifiche
  sparse nei template.
- Nuovo set di icone generato dal logo "ACFS Logo 2025 Vanguards" (`assets/icon-vanguards/`): 13
  file favicon/apple-touch-icon/android-icon (trasparenza vera per favicon/android, sfondo scuro
  pieno per gli apple-touch-icon, come richiesto da iOS) più un'icona 512×512 "any" e una
  512×512 "maskable" con safe-zone corretta per l'installabilità PWA.
- Bottone `<pwa-install>` finalmente presente nell'header/nav — lo script
  `@pwabuilder/pwainstall` veniva caricato su ogni pagina da mesi, ma l'elemento custom non era
  mai stato inserito da nessuna parte nell'HTML: nessun visitatore, su nessun browser, aveva mai
  visto un bottone d'installazione. Temato via nuovo `_sass/components/_pwa-install.scss`.
  Attributo `showopen` per mostrarlo sempre, senza aspettare le euristiche di installabilità del
  browser.

### Fixed

- Script `@pwabuilder/pwainstall` fissato alla versione `1.6.7` (era `@latest`, non pinnata).
- Elenco icone di `manifest.json` ripulito: via i ~19 file legacy con nomi hash a dimensioni
  Windows-tile obsolete (620×300, 1240×600, ecc.), rimasti col logo vecchio; ora solo
  192/512/512-maskable dal logo nuovo.
- `start_url` nel manifest era il dominio di produzione hardcoded — rotto in locale e fragile a
  un eventuale cambio di dominio. Ora relativo (`/`).
- **Bug che impediva l'installabilità PWA**: `<link rel="manifest">` (in `head.html` e
  `map/index.html`) puntava a un URL assoluto costruito da `site.url`; Jekyll in `serve` scrive
  sempre `localhost` in `site.url` a prescindere dal flag `--host`, quindi navigando su
  `127.0.0.1` invece che `localhost` il fetch del manifest falliva per CORS (origini diverse) —
  né il browser né il bottone d'installazione potevano validare nulla. Ora l'URL è relativo,
  funziona con qualsiasi hostname.
- Registrazione del service worker (`serviceworker_pwa.js`) con URL assoluto cross-origin —
  funzionava per puro caso in produzione (stesso dominio) ma falliva silenziosamente ovunque
  altro, test locali inclusi. Ora path relativo, stesso dominio garantito.
- `theme-color` e `msapplication-TileColor` erano hardcoded bianchi, in contrasto con il colore
  di brand già corretto nel manifest. Allineati a `site.color` (arancione).

## [1.5.0] - 2026-08-14 — Cookie consent, GA4 e pulizia asset

### Added

- New cookie consent banner using [CookieConsent v3](https://cookieconsent.orestbida.com/) (orestbida),
  replacing the old `cookie-bar.eu` script (stuck on v1.10.3, unmaintained since July 2023). Same library
  already in use on skyflash.github.io.
  - Three consent categories: `necessary` (always on), `analytics` (Google Analytics), `thirdparty`
    (Disqus).
  - Real script blocking via `type="text/plain" data-category="..."` tags on the GA and Disqus embeds —
    the old banner was purely cosmetic and never actually gated anything.
  - New `_sass/components/_cookieconsent.scss`, theming the widget on the site's own palette
    (`_palette()`/`_font()` helpers) instead of the library's default look.
  - "Gestisci preferenze cookie" link added to the footer to reopen the preferences panel at any time.
  - Privacy policy stays hosted on iubenda as before; the banner links out to it.

### Fixed

- Cookie consent script was silently crashing (`TypeError: Cannot read properties of null (reading
  'appendChild')`) because it lived in `<head>` and tried to attach to `document.body` before the body
  existed. Moved the include to the end of `<body>` (`foot.html`), matching where it lives on skyflash.
- Two conflicting `<link rel="manifest">` tags, in `head.html` and `map/index.html` — the second one
  (`assets/icon/manifest.json`) pointed to icon paths at the site root (`/android-icon-*.png`) that don't
  exist, so every icon in it 404'd. Removed the dead one, kept the dynamic `/manifest.json`.
- `<link rel="preload">` tags for the EuroCaps CSS and the three webfonts had invalid/missing `as`
  attributes (`as="eurocaps"`, or no `as` at all on the fonts), so the browser ignored the preload hint
  entirely (and logged console warnings). Fixed to `as="style"` / `as="font"`.

### Changed

- Google Analytics migrated from Universal Analytics (`UA-147419241-1`, sunset by Google since July
  2023 — no longer collecting any data) to GA4 (`G-KKHDG21GJ4`). Confirmed Google Signals disabled and
  data retention set to 2 months in the GA4 console.
- DataTables (CSS + JS + init script) and Lightbox (JS + CSS) no longer load on every page — gated
  behind `page.datatable` / `page.lightbox` front matter flags in `head.html` / `scripts-main.html`.
  `about/index.md` (the systems table) already had `datatable: true` set but it was never actually
  wired up until now; every other page was paying for both libraries unconditionally.

## 2026-08-12

### Added

- New Python script `spansh_sync.py`, replacing `edsm_fetcher.py` as the default tool for keeping
  the systems table in `about/index.md` in sync (EDSM's API was unreachable; `edsm_fetcher.py` is
  kept in the repo as a fallback for when it comes back). Uses Spansh's public (unofficial) API,
  no API key required.
  - Adds missing systems to the table, alphabetically sorted, with Governo/Popolazione/Alleanza/Stato
    filled in from Spansh.
  - Updates those same fields on existing rows whenever the live BGS data differs from the file
    (government changes, control flips, population drift), and prints a per-field change log.
  - Leaves rows untouched when the system isn't found on Spansh (e.g. visited systems not yet in
    public dumps), instead of deleting them.
  - Updates `last_modified_at` in the front matter automatically on every run.
  - Recalculates and updates the "Governiamo su **N** abitanti" total from the sum of population of
    all "Controllato" rows.
- `README.md` updated with a new description of `spansh_sync.py` under "Aggiornare la tabella
  popolazione", replacing the old `edsm_fetcher.py` instructions.
- `__pycache__` added to `.gitignore`.

### Fixed

- Corrected a duplicated/misspelled system name in `about/index.md`
  ("V0502 V0502 Ophiuchii" → "V0502 Ophiuchii") that prevented it from being matched and updated.
- Removed a duplicate "Misir" row (two entries with different Governo values for the same system).
- Removed a stray compiled `__pycache__/edsm_fetcher.cpython-314.pyc` file that had been committed
  by mistake.

### Changed

- `about/index.md` systems table synced against live Spansh data: added 98 previously-missing
  systems and refreshed population/government/allegiance/status across the table.

## 2026-03-08

### Added

- New Python script `edsm_fetcher.py` (refactored existing fetch logic) to update
  population data in `about/index.md`.
  - Added `format_population()` helper to match EDSM number formatting (points
    for thousands, no suffixes).
  - Rewrote table processing to preserve original markdown spacing and pipe
    characters, update only the population field, and maintain blank lines
    around DataTable markers.
  - Implemented `max_updates` parameter for partial updates and prints
    progress messages.
  - Added robust handling of missing markers and carriage returns.

- README.md updated with a new section describing how to run
  `edsm_fetcher.py` and examples of usage.

### Fixed

- Ensured table regeneration does not break Markdown by inserting blank lines
  after `<div class="datatable-begin">` and before
  `<div class="datatable-end">`.

### Changed

- Existing `about/index.md` data regenerated with the new script; population
  values are now stored in numeric format consistent with EDSM.

### Added

- Table pagination feature integrated into the site earlier in the day;
  allows long tables (e.g. systems list) to be navigated with page controls.
  This enhancement improves usability on mobile and desktop alike.


*No other substantive code changes were made on this date.*