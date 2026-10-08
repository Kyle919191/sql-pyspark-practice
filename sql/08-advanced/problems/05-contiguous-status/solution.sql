-- TRY the starter first.
WITH marked AS (
    SELECT
        event_date,
        status,
        event_date - CAST(row_number() OVER (PARTITION BY status ORDER BY event_date) AS INTEGER) AS island
    FROM events
)
SELECT
    status,
    min(event_date) AS start_date,
    max(event_date) AS end_date
FROM marked
GROUP BY status, island
ORDER BY start_date;
