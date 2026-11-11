"""Suppliers: the nurseries and shops we buy plants, pots and soil from."""

from flask import Blueprint, redirect, render_template, request

from backoffice import db

bp = Blueprint("suppliers", __name__)
FIELDS = ("name", "email", "phone", "fax")


@bp.get("/suppliers")
def supplier_list():
    with db.connect() as conn:
        suppliers = conn.execute("SELECT * FROM suppliers ORDER BY name").fetchall()
    return render_template("suppliers.html", suppliers=suppliers)


@bp.get("/suppliers/new")
def new_supplier():
    return render_template("supplier_form.html", form={})


@bp.post("/suppliers")
def add_supplier():
    form = {field: request.form.get(field, "").strip() for field in FIELDS}
    if not form["name"]:
        error = "Please enter the supplier name"
        return render_template("supplier_form.html", form=form, error=error), 400
    with db.connect() as conn:
        conn.execute(
            "INSERT INTO suppliers (name, email, phone, fax) VALUES (?, ?, ?, ?)",
            (form["name"], form["email"], form["phone"], form["fax"]),
        )
    return redirect("/suppliers")
