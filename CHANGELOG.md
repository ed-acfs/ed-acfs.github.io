# Changelog

All notable changes to this project will be documented in this file.

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