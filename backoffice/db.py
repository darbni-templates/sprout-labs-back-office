"""The SQLite database: tables from schema.sql, the shop's data from seed.sql."""

import sqlite3
from pathlib import Path

from flask import current_app

HERE = Path(__file__).parent


def init_db(path):
    with sqlite3.connect(path) as conn:
        conn.executescript((HERE / "schema.sql").read_text(encoding="utf-8"))
        if conn.execute("SELECT COUNT(*) FROM staff").fetchone()[0] == 0:
            conn.executescript((HERE / "seed.sql").read_text(encoding="utf-8"))


def connect():
    """A connection to the database. Use it as `with db.connect() as conn:`."""
    conn = sqlite3.connect(current_app.config["DATABASE"])
    conn.row_factory = sqlite3.Row  # rows work like dicts: row["name"]
    return conn
