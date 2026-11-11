"""Orders: the list, one page per order, moving an order on, and archiving it."""

from flask import Blueprint, abort, redirect, render_template, request

from backoffice import db

bp = Blueprint("orders", __name__)

PAGE_SIZE = 10
STATUSES = ["Paid", "Shipped"]
# The one status an order may move to next.
NEXT_STATUS = {"Paid": "Shipped"}


def find_order(order_id):
    with db.connect() as conn:
        order = conn.execute("SELECT * FROM orders WHERE id = ?", (order_id,)).fetchone()
    if order is None:
        abort(404)
    return order


@bp.get("/orders")
def order_list():
    status = request.args.get("status", "")
    page = max(request.args.get("page", 1, type=int), 1)
    where, args = "archived = 0", []
    if status in STATUSES:
        where += " AND status = ?"
        args.append(status)
    with db.connect() as conn:
        count = conn.execute(f"SELECT COUNT(*) FROM orders WHERE {where}", args).fetchone()[0]
        orders = conn.execute(
            f"SELECT * FROM orders WHERE {where} ORDER BY created_at LIMIT ? OFFSET ?",
            [*args, PAGE_SIZE, (page - 1) * PAGE_SIZE],
        ).fetchall()
    pages = max((count + PAGE_SIZE - 1) // PAGE_SIZE, 1)
    return render_template(
        "orders.html", orders=orders, page=page, pages=pages, status=status, statuses=STATUSES
    )


@bp.get("/orders/<int:order_id>")
def order_page(order_id):
    order = find_order(order_id)
    return render_template("order.html", order=order, next_status=NEXT_STATUS.get(order["status"]))


@bp.post("/orders/<int:order_id>/status")
def change_status(order_id):
    order = find_order(order_id)
    new_status = request.form.get("status", "")
    if new_status != NEXT_STATUS.get(order["status"]):
        return f"An order that is {order['status']} can't move to {new_status}", 400
    with db.connect() as conn:
        conn.execute("UPDATE orders SET status = ? WHERE id = ?", (new_status, order_id))
    return redirect(f"/orders/{order_id}")


@bp.post("/orders/<int:order_id>/delete")
def archive(order_id):
    find_order(order_id)
    with db.connect() as conn:
        conn.execute("UPDATE orders SET archived = 1 WHERE id = ?", (order_id,))
    return redirect("/orders")
