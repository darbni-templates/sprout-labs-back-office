"""How dates are shown. The database stores them as text, Bahrain time: 2026-03-15 10:20:00."""

from datetime import datetime

STORED = "%Y-%m-%d %H:%M:%S"


def format_date(stored):
    """2026-03-15 10:20:00 -> 03/15/2026. Used in templates as {{ order["created_at"]|date }}."""
    return datetime.strptime(stored, STORED).strftime("%m/%d/%Y")
