-- Back office tables. Runs on every start, so always use CREATE TABLE IF NOT EXISTS.
-- Money is stored in fils (1 BHD = 1000 fils) as an INTEGER, never as a float.
-- Dates are stored as text, Bahrain time: 2026-03-15 10:20:00.
CREATE TABLE IF NOT EXISTS staff (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    role TEXT NOT NULL,  -- 'manager' or 'viewer'
    password_hash TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number TEXT NOT NULL UNIQUE,  -- what customers see: LP-1001
    customer TEXT NOT NULL,
    email TEXT NOT NULL,
    total_fils INTEGER NOT NULL,
    status TEXT NOT NULL DEFAULT 'Paid',
    archived INTEGER NOT NULL DEFAULT 0,  -- 1 = hidden from the order list
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price_fils INTEGER NOT NULL,
    stock INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS suppliers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    fax TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS complaints (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL REFERENCES orders (id),
    customer TEXT NOT NULL,
    message TEXT NOT NULL,
    created_at TEXT NOT NULL
);
