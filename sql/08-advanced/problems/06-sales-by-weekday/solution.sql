-- TRY the starter first.
SELECT
    product,
    sum(CASE WHEN weekday = 'Mon' THEN amount ELSE 0 END) AS mon,
    sum(CASE WHEN weekday = 'Tue' THEN amount ELSE 0 END) AS tue,
    sum(CASE WHEN weekday = 'Wed' THEN amount ELSE 0 END) AS wed
FROM sales
GROUP BY product
ORDER BY product;
