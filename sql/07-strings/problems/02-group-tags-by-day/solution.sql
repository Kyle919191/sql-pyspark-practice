-- TRY the starter first.
SELECT
    event_date,
    count(DISTINCT tag) AS n_tags,
    string_agg(DISTINCT tag, ',' ORDER BY tag) AS tags
FROM events
GROUP BY event_date
ORDER BY event_date;
