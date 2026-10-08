-- TRY the starter first.
SELECT v.visit_id, v.customer_id
FROM visits AS v
LEFT JOIN purchases AS p
    ON v.visit_id = p.visit_id
WHERE p.purchase_id IS NULL;
