"""Exporting orders for the accountant."""

from flask import Blueprint, render_template

bp = Blueprint("export", __name__)


@bp.get("/orders/export")
def export_orders():
    return render_template("export.html")
