# Changelog

All notable changes to this project will be documented in this file.

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