CREATE TABLE products (
    product_key INTEGER
);

INSERT INTO products VALUES (1), (2), (3);

CREATE TABLE purchases (
    customer_id INTEGER,
    product_key INTEGER
);

INSERT INTO purchases VALUES
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 2),
    (2, 1),
    (2, 2),
    (3, 1),
    (3, 2),
    (3, 3);
