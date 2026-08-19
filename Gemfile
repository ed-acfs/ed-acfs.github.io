source 'https://rubygems.org'

# ESPERIMENTO (branch explore/github-actions-jekyll4): al posto della gem
# "github-pages" (che pinnava tutto a Jekyll 3.9 + libSass 1.x per la
# pipeline legacy "Deploy from a branch"), Jekyll e i plugin sono dichiarati
# direttamente: la build/pubblicazione passerebbe a un workflow GitHub
# Actions, quindi le versioni le scegliamo noi qui. Stesso schema di
# skyflash.github.io e ipui2ipei.
gem "jekyll", "~> 4.3"

# markdown: kramdown, input: GFM (vedi _config.yml). Prima arrivava come
# dipendenza transitiva della gem github-pages; ora va dichiarata.
gem "kramdown-parser-gfm"

# Dart Sass al posto della libSass 1.x deprecata pinnata da github-pages.
gem "jekyll-sass-converter", "~> 3.0"

group :jekyll_plugins do
    gem "jekyll-sitemap"
    gem "jekyll-gist"
    gem 'jekyll-mentions'
    gem 'jekyll-feed'
    gem 'jekyll-paginate'
    gem 'jekyll-seo-tag'
    gem 'jekyll-redirect-from'
    gem 'jemoji'
end

# Non è un plugin Jekyll: gira in CI dopo la build per controllare link
# rotti, immagini senza alt, anchor interni non validi.
gem "html-proofer", group: :test

# Ruby 3.4+ stopped shipping these as default gems; Jekyll/Liquid still need them
gem 'logger'
gem 'bigdecimal'

# Windows does not include zoneinfo files, so bundle the tzinfo-data gem
gem "tzinfo-data"

# Performance-booster for watching directories on Windows. Deve usare
# `platforms:` (meccanismo nativo di Bundler) e non un `if Gem.win_platform?`:
# quest'ultimo viene valutato quando il Gemfile viene letto, quindi su CI
# Linux la gem sparirebbe dal Gemfile mentre resta nel lockfile, mandando in
# conflitto la modalità frozen usata in CI.
gem "wdm", ">= 0.1.0", platforms: [:windows]

gem "webrick", "~> 1.8"
gem "rack", ">= 2.1.4"
gem "addressable", ">= 2.8.0"
gem "nokogiri", ">= 1.13.2"
