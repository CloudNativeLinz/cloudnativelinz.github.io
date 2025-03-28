# Makefile for Jekyll commands

# Variables
JEKYLL_CMD = jekyll serve
LIVERELOAD_FLAG = --livereload
FORCE_POLLING_FLAG = --force_polling

# Default target
all: serve

# Helper for Juergen ;)
run: serve-livereload

# Serve the site
serve:
	$(JEKYLL_CMD)

clean:
	@echo "Cleaning up..."
	@rm -rf _site
	@rm -rf .jekyll-cache
	@rm -rf .sass-cache
	@rm -rf vendor/bundle

# Serve the site with live reload
serve-livereload:
	$(JEKYLL_CMD) $(LIVERELOAD_FLAG)

# Serve the site with live reload and force polling (for Windows)
serve-windows:
	$(JEKYLL_CMD) $(LIVERELOAD_FLAG) $(FORCE_POLLING_FLAG)

install:
	@echo "Installing dependencies..."
	@bundle install
	@bundle exec jekyll build

.PHONY: all serve serve-livereload serve-windows
