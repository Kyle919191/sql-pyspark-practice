CREATE TABLE events (
    event_date DATE,
    status VARCHAR
);

INSERT INTO events VALUES
    (DATE '2024-01-01', 'ok'),
    (DATE '2024-01-02', 'ok'),
    (DATE '2024-01-03', 'fail'),
    (DATE '2024-01-04', 'fail'),
    (DATE '2024-01-05', 'fail'),
    (DATE '2024-01-06', 'ok');
