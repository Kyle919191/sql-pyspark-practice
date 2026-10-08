# Orders with product names

**Pattern:** INNER JOIN lookup. **LeetCode cousin:** 1068.

## Tables

`orders(order_id, product_id, qty)` — one row per order  
`products(product_id, name)` — one row per product

## Task

Return `order_id`, `name`, and `qty` for every order that has a matching product.

Order does not matter.

## Example

Orders 10 (product 1) and 11 (product 3) exist. Product 2 has no order. Expected two rows: oats and chips, not kale.
