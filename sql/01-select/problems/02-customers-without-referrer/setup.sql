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
