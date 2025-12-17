# AI Coding Agent Instructions for ed-acfs.github.io

## English Version

### Overview
This is a Jekyll-based static site for the Italian Elite Dangerous squadron "Alto Comando Flotta Stellare". It serves blog posts, guides, and community content about Elite Dangerous gameplay.

### Architecture
- **Content Structure**: Posts in `_posts/` (blog) and `_guide/` (guides), using Jekyll front matter with custom fields like `tags`, `author`, `image`
- **Tag System**: Custom Python script generates tag pages in `tag/` directory from post tags
- **Data-Driven**: Author profiles in `_data/authors.yml`, navigation in `_data/navigation.yml`
- **PWA Features**: Service worker, manifest.json for offline capabilities
- **Search**: JSON-based search using `search.json` generated from posts

### Build & Deploy Workflow
- **Local Development**: `bundle exec jekyll serve` (requires Ruby/Bundler)
- **Tag Generation**: Run `python tag_generator.py` before commits to generate tag pages (VS Code task: "Compilazione tags")
- **Dependencies**: Ruby gems in Gemfile, Jekyll plugins for SEO, sitemap, etc.
- **Exclude Pattern**: Files like README.md, Gemfile, package.json are excluded from build

### Key Conventions
- **Front Matter**: Use `tags:` array in posts (e.g., `tags: flotta-stellare esplorazione combat`)
- **Tag URLs**: Hyphen-separated for multi-word tags (e.g., `flotta-stellare`)
- **Author Attribution**: Reference authors by key in `_data/authors.yml` (e.g., `author: skyflash`)
- **Permalinks**: Blog posts use `/blog/:title/`, guides use `/guide/:title/`
- **SEO**: Use `sitemap` front matter for custom sitemap entries, `robots: noindex` for tag pages
- **Images**: Store in `images/`, reference with `/images/filename`

### Integration Points
- **External Links**: Inara.cz profiles, social media (Twitter, Facebook, Telegram)
- **Analytics**: Google Analytics with ID in `_config.yml`
- **Comments**: Disqus integration with shortname "flottastellare"

### Examples
- **New Post**: Add to `_posts/` with date prefix (e.g., `2019-04-08-entra-nello-squadrone.md`), include tags and author
- **Tag Page**: Auto-generated in `tag/tagname.md` with layout `tagpage`
- **Author Display**: Uses `_includes/author.html` and `_data/authors.yml` data

### Critical Files
- `_config.yml`: Site config, collections, plugins
- `tag_generator.py`: Tag page generator script
- `_layouts/post.html`: Main post layout with tag display
- `_data/authors.yml`: Author profiles with social links
- `search.json`: Search data source

## Versione Italiana

### Panoramica
Questo è un sito statico basato su Jekyll per lo squadrone italiano di Elite Dangerous "Alto Comando Flotta Stellare". Serve post di blog, guide e contenuti comunitari sul gameplay di Elite Dangerous.

### Architettura
- **Struttura dei Contenuti**: Post in `_posts/` (blog) e `_guide/` (guide), utilizzando front matter Jekyll con campi personalizzati come `tags`, `author`, `image`
- **Sistema di Tag**: Script Python personalizzato genera pagine tag nella directory `tag/` dai tag dei post
- **Data-Driven**: Profili autori in `_data/authors.yml`, navigazione in `_data/navigation.yml`
- **Funzionalità PWA**: Service worker, manifest.json per capacità offline
- **Ricerca**: Ricerca basata su JSON utilizzando `search.json` generato dai post

### Workflow di Build e Deploy
- **Sviluppo Locale**: `bundle exec jekyll serve` (richiede Ruby/Bundler)
- **Generazione Tag**: Eseguire `python tag_generator.py` prima dei commit per generare pagine tag (task VS Code: "Compilazione tags")
- **Dipendenze**: Gemme Ruby in Gemfile, plugin Jekyll per SEO, sitemap, ecc.
- **Pattern di Esclusione**: File come README.md, Gemfile, package.json sono esclusi dalla build

### Convenzioni Chiave
- **Front Matter**: Usare array `tags:` nei post (es., `tags: flotta-stellare esplorazione combat`)
- **URL Tag**: Separati da trattino per tag di più parole (es., `flotta-stellare`)
- **Attribuzione Autore**: Riferire autori per chiave in `_data/authors.yml` (es., `author: skyflash`)
- **Permalink**: Post blog usano `/blog/:title/`, guide usano `/guide/:title/`
- **SEO**: Usare front matter `sitemap` per voci sitemap personalizzate, `robots: noindex` per pagine tag
- **Immagini**: Memorizzare in `images/`, riferire con `/images/filename`

### Punti di Integrazione
- **Link Esterni**: Profili Inara.cz, social media (Twitter, Facebook, Telegram)
- **Analytics**: Google Analytics con ID in `_config.yml`
- **Commenti**: Integrazione Disqus con shortname "flottastellare"

### Esempi
- **Nuovo Post**: Aggiungere a `_posts/` con prefisso data (es., `2019-04-08-entra-nello-squadrone.md`), includere tag e autore
- **Pagina Tag**: Auto-generata in `tag/tagname.md` con layout `tagpage`
- **Display Autore**: Usa `_includes/author.html` e dati `_data/authors.yml`

### File Critici
- `_config.yml`: Config sito, collezioni, plugin
- `tag_generator.py`: Script generatore pagine tag
- `_layouts/post.html`: Layout post principale con display tag
- `_data/authors.yml`: Profili autori con link social
- `search.json`: Sorgente dati ricerca</content>
<parameter name="filePath">c:\Users\ccast\Progetti\ed-acfs.github.io\.github\copilot-instructions.md