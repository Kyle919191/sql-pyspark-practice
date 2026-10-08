CREATE TABLE staff (
    id INTEGER,
    name VARCHAR,
    manager_id INTEGER
);

INSERT INTO staff VALUES
    (1, 'Ada', NULL),
    (2, 'Bea', 1),
    (3, 'Cal', 1),
    (4, 'Dot', 2);
