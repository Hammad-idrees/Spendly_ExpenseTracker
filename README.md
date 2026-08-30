# Expense Tracker

A Flask-based web app for tracking personal expenses, with user registration/login and expense management (add, edit, delete) built incrementally.

## Status

🚧 Work in progress. Currently implemented:

- Landing, register, and login pages (templates + routes)
- Project scaffolding for a SQLite-backed database layer

Not yet implemented (planned):

- Database setup (`database/db.py`)
- Logout and profile pages
- Add / edit / delete expense functionality

## Tech Stack

- [Flask](https://flask.palletsprojects.com/) 3.1
- SQLite
- pytest / pytest-flask for testing

## Getting Started

```bash
# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

The app runs at `http://localhost:5001`.

## Project Structure

```
expense-tracker/
├── app.py              # Flask app and routes
├── database/           # DB connection and setup (in progress)
├── templates/           # Jinja2 templates
├── static/              # CSS/JS/assets
└── requirements.txt
```
