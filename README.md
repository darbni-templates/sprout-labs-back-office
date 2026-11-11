# Leaf & Pot back office

This is the staff dashboard the Leaf & Pot team uses every day: orders, customers, stock,
suppliers and customer complaints. It works, but the team keeps asking for changes. Read
`COMPANY.md` first: it has the team and the house rules.

## Your tasks
**Your exact task is in Darbni.** Open the task there and read its page: it has the rules and
the values (limits, messages, amounts) for YOUR version. Every intern gets their own version, so
a solution copied from someone else will fail the tests. Darbni also checks that what already
works keeps working.

## Run it
```
python -m venv .venv
.venv\Scripts\activate          # Windows (on macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
flask --app backoffice run --debug
```
Open http://127.0.0.1:5000. The database is `backoffice.sqlite`, created on start from
`backoffice/schema.sql`, with the shop's data from `backoffice/seed.sql`. Delete the file to
start over (do that after you change `schema.sql` or `seed.sql`).

Staff accounts:
| Username | Password | Role |
|---|---|---|
| `khalid` | `manager123` | manager |
| `huda` | `viewer123` | viewer |

## Test it
```
pytest
```
These tests are yours to run and extend. Darbni runs its own hidden tests on every submission.

## The AI rule
All AI calls go through `backoffice/ai.py`. Always call it like this:
```python
from backoffice import ai

reply = ai.ask_llm(prompt)
```
Not `from backoffice.ai import ask_llm`: Darbni's tests swap `ai.ask_llm` for a fake model, and
that import would keep the real one. `ask_llm` can fail, so always have a fallback text.

On your machine there is no real model: `ask_llm` returns a demo reply that starts with
`[Demo AI reply]`. To see what your page does when the AI is down, make it fail:
```
set BACKOFFICE_AI=fail          # Windows cmd (PowerShell: $env:BACKOFFICE_AI="fail")
export BACKOFFICE_AI=fail       # macOS/Linux
flask --app backoffice run --debug
```
Unset it (or open a new terminal) to get the demo reply back.

## Where things are
| File | What it does |
|---|---|
| `backoffice/__init__.py` | `create_app(config)`: builds the app |
| `backoffice/auth.py` | staff log in and out; every page needs a login |
| `backoffice/dashboard.py` | the home page with the shop's numbers |
| `backoffice/orders.py` | the order list (`/orders`), one page per order, status, archive |
| `backoffice/invoices.py` | a printable invoice per order |
| `backoffice/customers.py` | the customer list with what each one spent |
| `backoffice/export.py` | exporting orders (not built yet) |
| `backoffice/stock.py` | plants, prices, stock, and the low-stock alert |
| `backoffice/suppliers.py` | the supplier list and the new-supplier form |
| `backoffice/complaints.py` | customer complaints |
| `backoffice/dates.py` | how dates are shown (`\|date` in templates) |
| `backoffice/display.py` | how money is shown in templates (`\|bhd`) |
| `backoffice/db.py` | `db.connect()` for the SQLite database |
| `backoffice/schema.sql`, `seed.sql` | the tables, and the shop's data |
| `backoffice/ai.py` | `ask_llm(prompt)`, the only way to call AI |
| `backoffice/templates/` | `base.html` (header) and one template per page |
| `backoffice/static/style.css` | the styles |
| `tests/` | pytest tests |
