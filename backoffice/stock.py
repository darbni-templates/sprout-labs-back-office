"""Stock: every plant with its price and stock, and an alert for plants running low."""

from flask import Blueprint, redirect, render_template, request

from backoffice import db

bp = Blueprint("stock", __name__)

LOW_STOCK = 5


def low_stock_alert(products):
    """The line at the top of the stock page."""
    low = [p for p in products if p["stock"] < LOW_STOCK]
    if not low:
        return "No plants are low on stock."
    return "Low stock: " + ", ".join(f"{p['name']} ({p['stock']} left)" for p in low) + "."


@bp.get("/stock")
def stock_list():
    with db.connect() as conn:
        products = conn.execute("SELECT * FROM products ORDER BY name").fetchall()
    return render_template("stock.html", products=products, alert=low_stock_alert(products))


@bp.post("/stock/<int:product_id>")
def update(product_id):
    stock = request.form.get("stock", type=int)
    price = request.form.get("price_fils", type=int)
    if stock is None or price is None or stock < 0 or price < 0:
        return "Stock and price must be whole numbers from 0 up", 400
    with db.connect() as conn:
        found = conn.execute(
            "UPDATE products SET stock = ?, price_fils = ? WHERE id = ?",
            (stock, price, product_id),
        ).rowcount
    if not found:
        return "Unknown plant", 404
    return redirect("/stock")
