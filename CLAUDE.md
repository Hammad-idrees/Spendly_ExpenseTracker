# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A Flask-based expense tracker web app, built incrementally as a step-by-step student project (see the `# Step N` comments in `app.py` and `database/db.py`). Many features are intentionally unimplemented placeholders rather than bugs.

## Commands

```bash
# Activate the existing venv (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app (http://localhost:5001, debug=True)
python app.py

# Run tests (pytest / pytest-flask are installed; no tests/ directory exists yet)
pytest
pytest path/to/test_file.py::test_name   # single test
```

There is no build step, bundler, or linter configured — templates/CSS/JS are served as static files directly by Flask.

## Architecture

- **`app.py`** — the entire Flask app: one file, all routes. Routes call `render_template()` only; several (`/logout`, `/profile`, `/expenses/add`, `/expenses/<id>/edit`, `/expenses/<id>/delete`) are unimplemented placeholders that just return a plain string ("coming in Step N").
- **`database/db.py`** — stub for the SQLite layer, not yet implemented. Intended to expose `get_db()` (SQLite connection with `row_factory` and foreign keys enabled), `init_db()` (create tables with `CREATE TABLE IF NOT EXISTS`), and `seed_db()` (sample dev data). The runtime DB file (`expense_tracker.db`) is gitignored.
- **Templates use inheritance**: `templates/base.html` owns the shared chrome — navbar, footer, `<head>`/font/CSS links, and a `{% block content %}` — and every page template (`landing.html`, `login.html`, `register.html`, `terms.html`, `privacy.html`) extends it and fills `content` (and `title`). Shared elements like the footer links live only in `base.html`, not in the child templates — edit them there even if a request references a child template by name.
- **Auth forms are not wired up**: `login.html`/`register.html` POST to `/login` and `/register`, but `app.py` only defines `GET` handlers for those routes today — no session/auth logic exists yet.
- **Styling** (`static/css/style.css`) is a single hand-written stylesheet using CSS custom properties defined on `:root` (colors like `--ink`, `--paper`, `--accent`; fonts `--font-display`/`--font-body`; radii, `--max-width`). Fonts are DM Serif Display (headings) + DM Sans (body), loaded from Google Fonts in `base.html`. New sections follow the existing `-inner` max-width wrapper convention (e.g. `.hero-inner`, `.auth-container`, `.legal-inner`) and `-title`/`-body` naming rather than ad hoc classes.
- **`static/js/main.js`** is currently empty/unused (placeholder for future JS).
