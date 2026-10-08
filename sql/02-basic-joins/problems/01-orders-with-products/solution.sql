-- TRY the starter first.
SELECT o.order_id, p.name, o.qty
FROM orders AS o
INNER JOIN products AS p
    ON o.product_id = p.product_id;
