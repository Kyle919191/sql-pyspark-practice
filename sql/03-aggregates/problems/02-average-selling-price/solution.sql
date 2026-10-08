-- TRY the starter first.
SELECT
    p.product_id,
    round(coalesce(sum(p.price * s.units) * 1.0 / nullif(sum(s.units), 0), 0), 2) AS average_price
FROM prices AS p
LEFT JOIN sales AS s
    ON p.product_id = s.product_id
   AND s.sale_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;
