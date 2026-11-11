"""A printable invoice for each order. Prices include 10% VAT."""

from datetime import datetime

from flask import Blueprint, abort, render_template

from backoffice import db

bp = Blueprint("invoices", __name__)

VAT_PERCENT = 10


def money(fils):
    return "%d.%03d BHD" % (fils // 1000, fils % 1000)


@bp.get("/orders/<int:order_id>/invoice")
def invoice(order_id):
    with db.connect() as conn:
        order = conn.execute("SELECT * FROM orders WHERE id = ?", (order_id,)).fetchone()
    if order is None:
        abort(404)
    total = order["total_fils"]
    vat = total * VAT_PERCENT // (100 + VAT_PERCENT)
    issued = datetime.strptime(order["created_at"], "%Y-%m-%d %H:%M:%S").strftime("%m/%d/%Y")
    return render_template(
        "invoice.html",
        order=order,
        issued=issued,
        net=money(total - vat),
        vat=money(vat),
        total=money(total),
    )
