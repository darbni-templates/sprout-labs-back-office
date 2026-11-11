"""Customers: everyone who has ordered, with how much they spent."""

from flask import Blueprint, render_template

from backoffice import db

bp = Blueprint("customers", __name__)


@bp.get("/customers")
def customer_list():
    with db.connect() as conn:
        rows = conn.execute(
            "SELECT customer, email, COUNT(*) AS orders, SUM(total_fils) AS spent "
            "FROM orders WHERE archived = 0 GROUP BY email ORDER BY customer"
        ).fetchall()
    customers = []
    for row in rows:
        spent = row["spent"]
        customers.append(
            {
                "name": row["customer"],
                "email": row["email"],
                "orders": row["orders"],
                "spent": str(spent // 1000) + "." + str(spent % 1000).zfill(3) + " BHD",
            }
        )
    return render_template("customers.html", customers=customers)
