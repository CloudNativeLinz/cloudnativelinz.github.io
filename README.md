# Cloud Native Linz Website

[![Last Commit](https://img.shields.io/github/last-commit/cloudnativelinz/cloudnativelinz.github.io?label=updated)](https://github.com/cloudnativelinz/cloudnativelinz.github.io/commits/main)
[![Website](https://img.shields.io/website?url=https%3A%2F%2Fcloudnativelinz.github.io)](https://cloudnativelinz.github.io)
[![Contributors](https://img.shields.io/github/contributors/cloudnativelinz/cloudnativelinz.github.io)](https://github.com/cloudnativelinz/cloudnativelinz.github.io/graphs/contributors)

Official website for the Cloud Native Linz community.

🌐 Website: https://cloudnativelinz.at

📅 Meetup page: https://www.meetup.com/Cloud-Native-Linz/

💬 Community page: https://community.cncf.io/linz/


## Quick Start

This site is built with Jekyll.

### Recommended: Dev Container or Codespaces

The easiest setup is GitHub Codespaces or VS Code Dev Containers, where tooling is preconfigured.

Run locally:

```bash
bundle install
bundle exec jekyll serve --livereload
```

Open preview at: http://127.0.0.1:4000

If file watching is unreliable on your machine (commonly Windows), use:

```bash
bundle exec jekyll serve --livereload --force_polling
```

## Makefile Commands

This repository includes common shortcuts in [`makefile`](makefile):

- `install`: Install Ruby dependencies and run a build
- `serve`: Run Jekyll server on all interfaces
- `serve-livereload`: Run server with live reload
- `serve-windows`: Live reload with force polling
- `clean`: Remove build and cache artifacts
- `calendar`: Generate `calendar.ics` from event data

Examples:

```bash
make install
make serve-livereload
make calendar
```

## Content and Data

Key locations:

- Pages: [`_pages`](./_pages)
- Layouts: [`_layouts`](./_layouts)
- Includes: [`_includes`](./_includes)
- Styles: [`assets/style.scss`](assets/style.scss)
- Event data: [`_data/events.yml`](_data/events.yml)

## Event URL Redirects

Event pages use stable slugs to avoid broken links when titles change.

- Guide: [`REDIRECT_MANAGEMENT.md`](REDIRECT_MANAGEMENT.md)
- Helper script: [`manage_redirects.rb`](manage_redirects.rb)
- Redirect generator plugin: [`_plugins/datapage_redirect_generator.rb`](_plugins/datapage_redirect_generator.rb)

Typical workflow:

```bash
ruby manage_redirects.rb
bundle exec jekyll build
```

## Calendar Generation

The repository can generate `calendar.ics` from event data.

- Script: [`generate_calendar.py`](generate_calendar.py)
- Python deps: [`requirements.txt`](requirements.txt)

Run via Makefile:

```bash
make calendar
```

## Build and Deploy

GitHub Pages builds and serves this site from this repository.

To validate locally before pushing:

```bash
bundle exec jekyll build
```

## Contributing

Contributions are welcome.

1. Create a branch
2. Make your changes
3. Build locally and verify
4. Open a pull request

