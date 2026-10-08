# Customers who bought every product

**Pattern:** HAVING count(DISTINCT …) = (SELECT count(*) …). **LeetCode cousin:** 1045.

## Tables

`products(product_key)` — the catalog  
`purchases(customer_id, product_key)` — can contain duplicates

## Task

Return `customer_id` of customers who bought **every** product in the catalog at least once.

Order does not matter.
