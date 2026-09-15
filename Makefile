# Makefile for Jekyll commands

# Variables
JEKYLL_CMD = bundle exec jekyll serve --host 0.0.0.0
LIVERELOAD_FLAG = --livereload
FORCE_POLLING_FLAG = --force_polling
JEKYLL_ARGS =
VENV = .venv
PYTHON = $(VENV)/bin/python

# Default target
all:
	$(JEKYLL_CMD)

# Helper for Juergen ;)
run:
	 $(MAKE) serve-livereload

# Serve the site
serve:
	$(JEKYLL_CMD)

# Build the production site and reject invalid front matter
build:
	JEKYLL_ENV=production bundle exec jekyll build --strict_front_matter $(JEKYLL_ARGS)

# Check source files without generating the site
lint: setup-python
	@$(VENV)/bin/ruff check --ignore DTZ007 generate_calendar.py
	@$(VENV)/bin/yamllint _config.yml _data/events.yml .github
	@ruby -cw manage_redirects.rb
	@ruby -cw _plugins/datapage_redirect_generator.rb

# Exercise generated content and the complete production build
test: calendar build

# Run all validation used by CI
check: lint test

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
	@$(MAKE) setup-python
	@$(MAKE) build

# Generate calendar.ics from events data
calendar: setup-python
	@echo "Generating calendar.ics from events data..."
	@$(PYTHON) generate_calendar.py
	@echo "Calendar generated successfully!"

# Setup Python environment for calendar generation
setup-python: $(VENV)/.requirements-installed

$(VENV)/.requirements-installed: requirements.txt
	@if [ ! -d "$(VENV)" ]; then \
		echo "Setting up Python environment..."; \
		python3 -m venv $(VENV) --upgrade-deps; \
	fi
	@$(VENV)/bin/pip install -r requirements.txt
	@touch $@
	@echo "Python environment ready!"

.PHONY: all build lint test check serve serve-livereload serve-windows calendar setup-python run clean install

