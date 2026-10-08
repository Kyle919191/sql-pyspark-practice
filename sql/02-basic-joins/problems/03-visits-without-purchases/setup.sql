CREATE TABLE visits (
    visit_id INTEGER,
    customer_id INTEGER
);

INSERT INTO visits VALUES
    (1, 10),
    (2, 10),
    (3, 20),
    (4, 30),
    (5, 40);

CREATE TABLE purchases (
    purchase_id INTEGER,
    visit_id INTEGER
);

INSERT INTO purchases VALUES
    (100, 1),
    (101, 1),
    (102, 5);
