CREATE TABLE products (
    product_id INTEGER,
    name VARCHAR
);

INSERT INTO products VALUES
    (1, 'oats'),
    (2, 'kale'),
    (3, 'chips');

CREATE TABLE orders (
    order_id INTEGER,
    product_id INTEGER,
    qty INTEGER
);

INSERT INTO orders VALUES
    (10, 1, 2),
    (11, 3, 1),
    (12, 1, 4);
