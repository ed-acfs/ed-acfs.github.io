# Changelog

All notable changes to this project will be documented in this file.

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