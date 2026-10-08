-- Playground: this check only asks you to return all products.
-- After it passes, edit freely and rerun. No more expected file for experiments.
--
-- Ideas from the lessons:
--   SELECT name FROM products WHERE in_stock = true;
--   SELECT name, price_cents / 100.0 AS price_dollars FROM products;
--   SELECT id, name FROM customers WHERE referrer_id != 2 OR referrer_id IS NULL;

SELECT *
FROM products;
