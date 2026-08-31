from flask import Flask, render_template, session, redirect, url_for

from database.db import get_db, init_db, seed_db

app = Flask(__name__)
app.secret_key = "dev-only-secret-key"

with app.app_context():
    init_db()
    seed_db()


# ------------------------------------------------------------------ #
# Routes                                                              #
# ------------------------------------------------------------------ #

@app.route("/")
def landing():
    return render_template("landing.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/terms")
def terms():
    return render_template("terms.html")


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


# ------------------------------------------------------------------ #
# Placeholder routes — students will implement these                  #
# ------------------------------------------------------------------ #

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("landing"))


# TEMP: no real login exists yet (Step 3), so this is the only way to get a
# session in a browser to view /profile. Remove once /login sets the session.
@app.route("/dev/login-as-demo")
def dev_login_as_demo():
    if not app.debug:
        return redirect(url_for("login"))
    session["user_id"] = 1
    session["user_name"] = "Demo User"
    return redirect(url_for("profile"))


@app.route("/profile")
def profile():
    if not session.get("user_id"):
        return redirect(url_for("login"))

    user = {
        "name": "Demo User",
        "email": "demo@spendly.com",
        "member_since": "January 2026",
        "initials": "DU",
    }

    summary_stats = [
        {"label": "Total Spent", "value": "$289.84"},
        {"label": "Transactions", "value": "8"},
        {"label": "Top Category", "value": "Food"},
    ]

    transactions = [
        {"date": "2026-08-20", "description": "Restaurant dinner", "category": "Food", "amount": "$32.10"},
        {"date": "2026-08-17", "description": "Miscellaneous", "category": "Other", "amount": "$9.30"},
        {"date": "2026-08-14", "description": "New shoes", "category": "Shopping", "amount": "$60.20"},
        {"date": "2026-08-11", "description": "Movie ticket", "category": "Entertainment", "amount": "$15.75"},
        {"date": "2026-08-08", "description": "Pharmacy", "category": "Health", "amount": "$25.00"},
    ]

    category_breakdown = [
        {"category": "Food", "amount": "$77.60", "percent": 27},
        {"category": "Bills", "amount": "$89.99", "percent": 31},
        {"category": "Shopping", "amount": "$60.20", "percent": 21},
        {"category": "Health", "amount": "$25.00", "percent": 9},
        {"category": "Entertainment", "amount": "$15.75", "percent": 5},
        {"category": "Transport", "amount": "$12.00", "percent": 4},
        {"category": "Other", "amount": "$9.30", "percent": 3},
    ]

    return render_template(
        "profile.html",
        user=user,
        summary_stats=summary_stats,
        transactions=transactions,
        category_breakdown=category_breakdown,
    )


@app.route("/expenses/add")
def add_expense():
    return "Add expense — coming in Step 7"


@app.route("/expenses/<int:id>/edit")
def edit_expense(id):
    return "Edit expense — coming in Step 8"


@app.route("/expenses/<int:id>/delete")
def delete_expense(id):
    return "Delete expense — coming in Step 9"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
