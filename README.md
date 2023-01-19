# Cloud Native Meetup Linz Website - cloudnativelinz.github.io

![GitHub last commit](https://img.shields.io/github/last-commit/cloudnativelinz/cloudnativelinz.github.io?label=updated)

## Development using Codespaces

It is easiest to use [codespaces](https://github.com/features/codespaces) since all tooling is already installed in the dev-container.

Open via the Github UI and once you have launched the codespaces, run a development session via:

```
jekyll serve
```
or via auto reload in the browser
```
jekyll serve --livereload
```
on windows the following option might be needed for auto reload
```
 jekyll serve --livereload --force_polling
```

The preview is now available via http://127.0.0.1:4000/

The setup of codespaces was inspired by this [blog post](https://garethbrown.net/2022/07/01/maintaining-a-blog-with-jekyll-github-pages-codespaces) - kudos!

## Local development with Dev Container

- Docker Desktop
- VS Code + Extension: Name: [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)


## Local development without Dev Container

Probably there are some dependencies that you'd need to check to run the static web generator Jekyll locally. If you want to contribute to this readme to fill in the blanks here, you are most welcome!

## Source

The website source has been created by using the template from 
https://github.com/amitmerchant1990/reverie

