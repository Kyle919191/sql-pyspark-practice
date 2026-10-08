CREATE TABLE employees (
    id INTEGER,
    name VARCHAR,
    supervisor_id INTEGER
);

INSERT INTO employees VALUES
    (1, 'Ada', NULL),
    (2, 'Bea', 1),
    (3, 'Cal', 1),
    (4, 'Dot', 2);

CREATE TABLE bonuses (
    emp_id INTEGER,
    bonus INTEGER
);

INSERT INTO bonuses VALUES
    (2, 800),
    (3, 200);
