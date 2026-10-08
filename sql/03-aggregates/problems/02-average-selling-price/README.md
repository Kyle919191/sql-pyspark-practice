# Average selling price

**Pattern:** weighted average after a date-range join. **LeetCode cousin:** 1251.

## Tables

`prices(product_id, start_date, end_date, price)` — one row per price window  
`sales(product_id, sale_date, units)` — one row per sale day

A sale matches a price when `sale_date` is between `start_date` and `end_date` inclusive.

## Task

For every product that appears in `prices`, return `product_id` and `average_price`.

`average_price = round(sum(price * units) / sum(units), 2)`.

If a product never sold, the average is `0`.

Order does not matter.
