-- TRY the starter first.
SELECT today.id
FROM weather AS today
INNER JOIN weather AS prev
    ON today.record_date = prev.record_date + INTERVAL 1 DAY
WHERE today.temp > prev.temp;
