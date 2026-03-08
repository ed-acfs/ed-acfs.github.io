# Changelog

All notable changes to this project will be documented in this file.

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