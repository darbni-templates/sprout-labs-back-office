"""Customer complaints: the list, and one page per complaint."""

from flask import Blueprint, abort, render_template

from backoffice import db

bp = Blueprint("complaints", __name__)

QUERY = (
    "SELECT complaints.*, orders.number AS order_number, orders.email AS email "
    "FROM complaints JOIN orders ON orders.id = complaints.order_id"
)


def find_complaint(complaint_id):
    with db.connect() as conn:
        complaint = conn.execute(f"{QUERY} WHERE complaints.id = ?", (complaint_id,)).fetchone()
    if complaint is None:
        abort(404)
    return complaint


@bp.get("/complaints")
def complaint_list():
    with db.connect() as conn:
        complaints = conn.execute(f"{QUERY} ORDER BY complaints.created_at DESC").fetchall()
    return render_template("complaints.html", complaints=complaints)


@bp.get("/complaints/<int:complaint_id>")
def complaint_page(complaint_id):
    return render_template("complaint.html", complaint=find_complaint(complaint_id))
