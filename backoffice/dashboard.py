"""The home page: the shop's numbers at a glance."""

from flask import Blueprint, render_template

from backoffice import db

bp = Blueprint("dashboard", __name__)


def _bhd(fils):
    return f"{fils // 1000}.{fils % 1000:03d} BHD"


@bp.get("/")
def home():
    with db.connect() as conn:
        orders = conn.execute(
            "SELECT COUNT(*) AS count, COALESCE(SUM(total_fils), 0) AS total "
            "FROM orders WHERE archived = 0"
        ).fetchone()
        to_ship = conn.execute(
            "SELECT COUNT(*) FROM orders WHERE archived = 0 AND status != 'Shipped'"
        ).fetchone()[0]
        complaints = conn.execute("SELECT COUNT(*) FROM complaints").fetchone()[0]
    average = orders["total"] // orders["count"] if orders["count"] else 0
    return render_template(
        "dashboard.html",
        order_count=orders["count"],
        total_sales=_bhd(orders["total"]),
        average_order=_bhd(average),
        to_ship=to_ship,
        complaint_count=complaints,
    )
