# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
bundle install

# Serve locally with live reload
bundle exec jekyll serve

# Build site
bundle exec jekyll build

# Manually trigger Notion sync (requires env vars)
NOTION_TOKEN=... NOTION_DATABASE_ID=... python3 scripts/notion_to_jekyll.py
```

## Architecture

This is a **bilingual Jekyll static site** (PT-BR + English) deployed to GitHub Pages via the `github-pages` gem.

### Multilingual System

Language support is custom (no plugin). Every page/post declares `lang: pt` or `lang: en` in frontmatter and uses a matching `permalink` that starts with `/pt/` or `/en/`. The `index.html` at root redirects to `/pt/` by default (`default_lang: "pt"` in `_config.yml`).

- `_data/translations.yml` — all UI strings keyed by component and language (`site.data.translations.home.hero.title.pt`)
- `_data/navigation.yml` — nav links per language
- `_includes/language-switcher.html` — renders the PT/EN toggle
- `pt/` and `en/` — language-specific page source files (index, portfolio, projects)

### Posts

Posts live in `_posts/` with filename `YYYY-MM-DD-{slug}-{lang}.md`. Required frontmatter:

```yaml
---
layout: post
title: "..."
info: "..."         # short description shown in blog listing
date: YYYY-MM-DD
lang: pt            # or en
permalink: /pt/YYYY-MM-DD/slug
type: post
tags: [Tag1, Tag2]
---
```

Blog listing pages (`pt/blog/`, `en/blog/`) filter `site.posts` by `post.lang`.

### Projects Carousel

The homepage carousel (`pt/index.md`, `en/index.md`) loads projects via a `fetch()` call at runtime against `/pt/projects.md` or `/en/projects.md`. Those files use a custom Markdown schema parsed by inline JS:

```markdown
### Project Name
Descrição: Short description
Imagem: /path/to/image.jpg
Link: https://...
```

### Notion → Jekyll Sync

`.github/workflows/notion-sync.yml` runs hourly. It uses a self-contained Node.js script (written inline in the workflow) that queries the Notion database for pages with `Published: true`, converts them to Jekyll posts using `notion-to-md`, and commits the result to `_posts/`. Required GitHub secrets: `NOTION_TOKEN`, `NOTION_DATABASE_ID`.

The Notion database must have these properties: `Title`, `Slug`, `Date`, `Published` (checkbox), `Language` (select: `pt` or `en`), `Info`, `Tech`, `Tags`, `Image`.

### Layouts

- `base.html` — wraps all pages with nav and footer; reads `page.lang` for language-aware nav
- `post.html` — blog post layout
- `portfolio.html` / `about.html` / `blog.html` / `certificates.html` — section-specific layouts

### Styles

Sass source is in `_sass/` (partials in `_sass/base/` and `_sass/layouts/`), compiled via `_sass/main.scss`. Assets (fonts, images, PDFs) live in `assets/`.
