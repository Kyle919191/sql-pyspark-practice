CREATE TABLE events (
    event_date DATE,
    tag VARCHAR
);

INSERT INTO events VALUES
    (DATE '2024-03-01', 'sql'),
    (DATE '2024-03-01', 'spark'),
    (DATE '2024-03-01', 'sql'),
    (DATE '2024-03-02', 'pandas'),
    (DATE '2024-03-03', 'sql'),
    (DATE '2024-03-03', 'ml');
