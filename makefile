# Makefile for Jekyll commands

# Variables
JEKYLL_CMD = bundle exec jekyll serve
LIVERELOAD_FLAG = --livereload
FORCE_POLLING_FLAG = --force_polling

# Default target
all:
	$(JEKYLL_CMD)

# Helper for Juergen ;)
run:
	 $(MAKE) serve-livereload

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

# Generate calendar.ics from events data
calendar: setup-python
	@echo "Generating calendar.ics from events data..."
	@./.venv/bin/python generate_calendar.py
	@echo "Calendar generated successfully!"

# Setup Python environment for calendar generation
setup-python:
	@if [ ! -d ".venv" ]; then \
		echo "Setting up Python environment..."; \
		python3 -m venv .venv --upgrade-deps; \
		.venv/bin/pip install -r requirements.txt; \
		echo "Python environment ready!"; \
	fi

.PHONY: all serve serve-livereload serve-windows calendar setup-python run clean install

