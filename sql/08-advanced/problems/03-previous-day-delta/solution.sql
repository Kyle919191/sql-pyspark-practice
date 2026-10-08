-- TRY the starter first.
SELECT
    record_date,
    temp,
    lag(temp) OVER (ORDER BY record_date) AS prev_temp,
    temp - lag(temp) OVER (ORDER BY record_date) AS delta
FROM weather
ORDER BY record_date;
