CREATE TABLE products (
    id INTEGER,
    name VARCHAR,
    price_cents INTEGER,
    in_stock BOOLEAN
);

INSERT INTO products VALUES
    (1, 'oats', 399, true),
    (2, 'kale', 249, true),
    (3, 'chips', 199, false),
    (4, 'apples', 350, true),
    (5, 'soda', 150, false);

CREATE TABLE customers (
    id INTEGER,
    name VARCHAR,
    referrer_id INTEGER
);

INSERT INTO customers VALUES
    (1, 'Amy', NULL),
    (2, 'Ben', 2),
    (3, 'Cai', 1),
    (4, 'Dee', 2),
    (5, 'Eve', NULL);
