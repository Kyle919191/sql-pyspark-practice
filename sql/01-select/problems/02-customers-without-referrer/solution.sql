-- TRY the starter first.
SELECT id, name
FROM customers
WHERE referrer_id != 2 OR referrer_id IS NULL;
