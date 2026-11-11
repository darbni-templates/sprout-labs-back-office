"""Staff log in with a username and password. Every other page needs a logged-in staff member."""

from flask import Blueprint, g, redirect, render_template, request, session
from werkzeug.security import check_password_hash

from backoffice import db

bp = Blueprint("auth", __name__)

# Pages anyone may open, logged in or not.
OPEN_PAGES = {"auth.login_form", "auth.login", "static"}


def current_staff():
    """The logged-in staff member's row (username, name, role), or None."""
    if "staff" not in g:
        g.staff = None
        staff_id = session.get("staff_id")
        if staff_id is not None:
            with db.connect() as conn:
                g.staff = conn.execute("SELECT * FROM staff WHERE id = ?", (staff_id,)).fetchone()
    return g.staff


@bp.before_app_request
def require_login():
    """Runs before every request: visitors who aren't logged in go to the login page."""
    if request.endpoint in OPEN_PAGES:
        return None
    if current_staff() is None:
        return redirect("/login")
    return None


@bp.get("/login")
def login_form():
    return render_template("login.html")


@bp.post("/login")
def login():
    username = request.form.get("username", "").strip().lower()
    with db.connect() as conn:
        staff = conn.execute("SELECT * FROM staff WHERE username = ?", (username,)).fetchone()
    password = request.form.get("password", "")
    if staff is None or not check_password_hash(staff["password_hash"], password):
        return render_template("login.html", error="Wrong username or password"), 401
    session.clear()
    session["staff_id"] = staff["id"]
    return redirect("/")


@bp.post("/logout")
def logout():
    session.clear()
    return redirect("/login")
