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

# Serve the site with live reload
serve-livereload:
	$(JEKYLL_CMD) $(LIVERELOAD_FLAG)

# Serve the site with live reload and force polling (for Windows)
serve-windows:
	$(JEKYLL_CMD) $(LIVERELOAD_FLAG) $(FORCE_POLLING_FLAG)

.PHONY: all serve serve-livereload serve-windows
