"""Back office: the staff dashboard of the Leaf & Pot plant shop."""

from flask import Flask

from backoffice import (
    auth,
    complaints,
    customers,
    dashboard,
    dates,
    db,
    display,
    export,
    invoices,
    orders,
    stock,
    suppliers,
)

BLUEPRINTS = (auth, dashboard, orders, invoices, customers, export, stock, suppliers, complaints)


def create_app(config=None):
    app = Flask(__name__)
    app.config.update(DATABASE="backoffice.sqlite", SECRET_KEY="dev-only-change-me")
    app.config.update(config or {})
    db.init_db(app.config["DATABASE"])
    app.add_template_filter(dates.format_date, "date")
    display.register(app)
    app.context_processor(lambda: {"staff": auth.current_staff()})
    for module in BLUEPRINTS:
        app.register_blueprint(module.bp)
    return app
