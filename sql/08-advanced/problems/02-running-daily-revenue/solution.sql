-- TRY the starter first.
SELECT
    sale_date,
    amount,
    sum(amount) OVER (
        ORDER BY sale_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_revenue
FROM sales
ORDER BY sale_date;
