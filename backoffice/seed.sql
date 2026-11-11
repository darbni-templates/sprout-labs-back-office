-- The shop's data: orders, plants, suppliers, complaints and two staff members.
-- Staff: khalid (manager, password manager123) and huda (viewer, password viewer123).
INSERT INTO staff (username, name, role, password_hash) VALUES
    ('khalid', 'Khalid Mansoor', 'manager', 'scrypt:32768:8:1$Jle59oZZaFAjfQH3$4785cebedddbad0b6046f5a884192d760ae5ae12c64762dd85985097d3b4a51ddc22aaee37069f09caf85abdb0f73a713247f1a957bc6d38ec9a03aaa9e5bb7a'),
    ('huda', 'Huda Saeed', 'viewer', 'scrypt:32768:8:1$sVeiTuXLfi8uyNV5$53368eca248e1ff92114922739cbce756b081204e4703d88eb7509f8f26d36609fddabdf2fdf85e7b7a0a7a39c7618af251fefb0db1187af53a7b23211656f81');

INSERT INTO orders (id, number, created_at, customer, email, total_fils, status) VALUES
    (1, 'LP-1001', '2026-02-03 09:15:00', 'Mariam Ali', 'mariam@example.com', 12900, 'Shipped'),
    (2, 'LP-1002', '2026-02-14 11:40:00', 'Hassan Saleh', 'hassan@example.com', 7450, 'Shipped'),
    (3, 'LP-1003', '2026-02-21 16:05:00', 'Noor Hasan', 'noor@example.com', 18150, 'Shipped'),
    (4, 'LP-1004', '2026-03-02 10:30:00', 'Fatima Isa', 'fatima@example.com', 4500, 'Shipped'),
    (5, 'LP-1005', '2026-03-09 13:20:00', 'Ali Jaffar', 'ali@example.com', 25150, 'Shipped'),
    (6, 'LP-1006', '2026-03-13 18:45:00', 'Mariam Ali', 'mariam@example.com', 9250, 'Shipped'),
    (7, 'LP-1007', '2026-03-17 08:55:00', 'Yusuf Khalil', 'yusuf@example.com', 16250, 'Shipped'),
    (8, 'LP-1008', '2026-03-22 12:10:00', 'Noor Hasan', 'noor@example.com', 21300, 'Shipped'),
    (9, 'LP-1009', '2026-03-28 17:30:00', 'Palm Cafe, Riffa', 'hello@palmcafe.bh', 9650, 'Shipped'),
    (10, 'LP-1010', '2026-04-04 09:05:00', 'Fatima Isa', 'fatima@example.com', 14400, 'Paid'),
    (11, 'LP-1011', '2026-04-11 14:50:00', 'Ali Jaffar', 'ali@example.com', 5050, 'Paid'),
    (12, 'LP-1012', '2026-04-15 10:25:00', 'Mariam Ali', 'mariam@example.com', 19500, 'Paid'),
    (13, 'LP-1013', '2026-04-19 19:40:00', 'Yusuf Khalil', 'yusuf@example.com', 9750, 'Paid'),
    (14, 'LP-1014', '2026-04-23 11:15:00', 'Noor Hasan', 'noor@example.com', 31050, 'Paid'),
    (15, 'LP-1015', '2026-04-27 16:35:00', 'Hassan Saleh', 'hassan@example.com', 11500, 'Paid');

INSERT INTO products (id, name, price_fils, stock) VALUES
    (1, 'Aloe Vera', 2700, 25),
    (2, 'Spider Plant', 2950, 4),
    (3, 'Pothos', 4500, 9),
    (4, 'Snake Plant', 9250, 6),
    (5, 'Peace Lily', 9650, 3),
    (6, 'ZZ Plant', 9750, 12),
    (7, 'Calathea', 11500, 0),
    (8, 'Monstera', 12900, 7),
    (9, 'Rubber Plant', 15650, 5),
    (10, 'Fiddle Leaf Fig', 16250, 8);

INSERT INTO suppliers (id, name, email, phone, fax) VALUES
    (1, 'Green Valley Nursery', 'sales@greenvalley.bh', '1745 2210', '1745 2211'),
    (2, 'Desert Bloom Farms', 'orders@desertbloom.bh', '1772 8800', '1772 8801'),
    (3, 'Riffa Pottery', 'hello@riffapottery.bh', '1766 3140', '1766 3141'),
    (4, 'Gulf Soil Supplies', 'info@gulfsoil.bh', '1733 9025', '1733 9026'),
    (5, 'Island Seeds', 'team@islandseeds.bh', '1790 4410', '1790 4411');

INSERT INTO complaints (id, order_id, customer, message, created_at) VALUES
    (1, 3, 'Noor Hasan', 'My Monstera arrived with two broken leaves.', '2026-02-24 09:30:00'),
    (2, 7, 'Yusuf Khalil', 'The Fiddle Leaf Fig came two days late.', '2026-03-20 15:10:00'),
    (3, 12, 'Mariam Ali', 'I was charged twice for the same order.', '2026-04-16 11:45:00'),
    (4, 14, 'Noor Hasan', 'The pot was cracked when it arrived.', '2026-04-25 13:05:00');
