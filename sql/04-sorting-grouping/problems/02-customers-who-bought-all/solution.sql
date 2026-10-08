-- TRY the starter first.
SELECT customer_id
FROM purchases
GROUP BY customer_id
HAVING count(DISTINCT product_key) = (SELECT count(*) FROM products);
