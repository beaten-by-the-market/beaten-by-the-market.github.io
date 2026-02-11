# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Jekyll-based static blog ("Beaten by the Market") focused on Korean stock market analysis. Uses the **Minimal Mistakes** theme (v4.26.2) installed as a gem. Hosted on GitHub Pages. Content is primarily in Korean.

## Build & Development Commands

```bash
# Install dependencies
bundle install

# Serve the site locally (theme preview mode, uses test/ directory)
bundle exec rake preview
# This starts a dev server at http://localhost:4000/test/

# Build the actual blog site
bundle exec jekyll build

# Serve the blog locally
bundle exec jekyll serve

# Minify JavaScript (requires npm/uglify-js)
bundle exec rake js
```

Note: `_config.yml` is NOT hot-reloaded by `jekyll serve` — restart the server after config changes.

## Architecture

- **Theme**: Minimal Mistakes gem (`minimal-mistakes-jekyll`). Most layout/include/sass files come from the gem, not this repo. Only override files present in the repo are custom.
- **Skin**: `air`
- **Locale**: `ko-KR`, timezone `Asia/Seoul`
- **Permalink structure**: `/:categories/:title/`

### Key Directories

- `_posts/` — Blog posts in Markdown. Naming: `YYYY-MM-DD-slug.md`. Posts with `-code` suffix contain code companion content.
- `_pages/` — Static pages (category archive, tag archive, search)
- `_layouts/`, `_includes/`, `_sass/` — Theme overrides (only files that differ from the gem defaults)
- `_data/navigation.yml` — Site navigation menu
- `assets/images/` — Post images, organized by post date/topic

### Post Front Matter Convention

```yaml
---
layout: single
title: "Post title in Korean"
categories: 한국시장
tag: [Market]
toc: true
author_profile: false
---
```

Default values (set in `_config.yml`): `layout: single`, `toc: true`, `toc_sticky: true`, `toc_label: 목차`, `read_time: true`, `share: true`, `related: true`, `show_date: true`.

### Posts with Inline Styles

Many posts embed `<style>` blocks for `table.dataframe` styling (scrollable data tables). This is a recurring pattern for posts containing financial data tables.

## Configuration

- **`_config.yml`** — Main Jekyll config (332 lines). Controls theme, plugins, defaults, analytics, author info.
- **Plugins**: jekyll-paginate, jekyll-sitemap, jekyll-gist, jekyll-feed, jekyll-include-cache
- **Analytics**: Google gtag (`G-WT8C7EX0F3`)
- **Search**: Lunr (default, can switch to Algolia)

## Code Style

- 2-space indentation, UTF-8, LF line endings (see `.editorconfig`)
- Markdown files: trailing whitespace preserved
- Commit messages are typically in Korean
