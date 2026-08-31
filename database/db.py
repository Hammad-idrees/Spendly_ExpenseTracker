import calendar
import sqlite3
from datetime import date
from pathlib import Path

from werkzeug.security import generate_password_hash

DB_PATH = Path(__file__).resolve().parent.parent / "expense_tracker.db"

CATEGORIES = ["Food", "Transport", "Bills", "Health", "Entertainment", "Shopping", "Other"]


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TEXT DEFAULT (datetime('now'))
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            description TEXT,
            created_at TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)
    conn.commit()
    conn.close()


def _day_str(today, day_of_month):
    last_day = calendar.monthrange(today.year, today.month)[1]
    return date(today.year, today.month, min(day_of_month, last_day)).isoformat()


def seed_db():
    conn = get_db()

    if conn.execute("SELECT 1 FROM users LIMIT 1").fetchone() is not None:
        conn.close()
        return

    password_hash = generate_password_hash("demo123")
    cursor = conn.execute(
        "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
        ("Demo User", "demo@spendly.com", password_hash),
    )
    user_id = cursor.lastrowid

    today = date.today()
    sample_expenses = [
        (user_id, 45.50, "Food", _day_str(today, 1), "Groceries"),
        (user_id, 12.00, "Transport", _day_str(today, 3), "Bus pass"),
        (user_id, 89.99, "Bills", _day_str(today, 5), "Electricity bill"),
        (user_id, 25.00, "Health", _day_str(today, 8), "Pharmacy"),
        (user_id, 15.75, "Entertainment", _day_str(today, 11), "Movie ticket"),
        (user_id, 60.20, "Shopping", _day_str(today, 14), "New shoes"),
        (user_id, 9.30, "Other", _day_str(today, 17), "Miscellaneous"),
        (user_id, 32.10, "Food", _day_str(today, 20), "Restaurant dinner"),
    ]
    conn.executemany(
        """
        INSERT INTO expenses (user_id, amount, category, date, description)
        VALUES (?, ?, ?, ?, ?)
        """,
        sample_expenses,
    )
    conn.commit()
    conn.close()
