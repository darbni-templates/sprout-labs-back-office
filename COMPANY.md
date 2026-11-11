# Sprout Labs and Leaf & Pot

**Sprout Labs** is a five-person startup in Bahrain. We build and run **Leaf & Pot**, an online
plant shop that delivers indoor plants, pots and care kits across the island.

## The team
| Name | Role | Ask them about |
|---|---|---|
| Lina Haddad | Engineering manager, co-founder | priorities, deadlines, being stuck |
| Omar Khalil | Senior engineer | the code, Flask, how to approach a task |
| Sara Nasser | QA engineer | how something should behave, failing checks |
| Yousef Amin | Product manager | what customers and staff need and why |
| Rana Saleh | People and operations | how the internship works, your workload |

## The back office
The shop's staff use this dashboard all day. Khalid Mansoor manages the shop floor and the
stock; Huda Saeed answers customers and should only look, not change anything. Each staff
member has a role in the database (`manager` or `viewer`), but the code doesn't check it yet.

Orders are paid online, then shipped. Staff archive orders that were cancelled or are tests:
archived orders leave the order list but stay in the database. Customers' complaints come in
from the shop's contact form.

The dashboard grew one page at a time and nobody tidied it up. It works and the team relies on
it, so every change must keep the rest working. Small, careful changes win.

## House rules
- Money is stored in **fils** as integers (1 BHD = 1000 fils) and shown as BHD with 3
  decimals: `7.500 BHD`.
- Times are Bahrain time (`Asia/Bahrain`). The weekend is Friday and Saturday.
- All code lives in the `backoffice` package. Keep functions small and names clear.
- AI only through `backoffice/ai.py` (see README), always with a fallback.
- Don't break what works: run `pytest` and click through the dashboard before you submit.
