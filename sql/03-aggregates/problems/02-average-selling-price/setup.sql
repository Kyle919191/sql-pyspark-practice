CREATE TABLE prices (
    product_id INTEGER,
    start_date DATE,
    end_date DATE,
    price INTEGER
);

INSERT INTO prices VALUES
    (1, DATE '2024-01-01', DATE '2024-01-10', 10),
    (1, DATE '2024-01-11', DATE '2024-01-20', 20),
    (2, DATE '2024-01-01', DATE '2024-01-31', 5),
    (3, DATE '2024-01-01', DATE '2024-01-31', 8);

CREATE TABLE sales (
    product_id INTEGER,
    sale_date DATE,
    units INTEGER
);

INSERT INTO sales VALUES
    (1, DATE '2024-01-05', 4),
    (1, DATE '2024-01-15', 2),
    (2, DATE '2024-01-09', 3);
