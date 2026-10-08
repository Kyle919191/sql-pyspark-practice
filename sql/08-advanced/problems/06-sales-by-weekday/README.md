# Sales by weekday

**Pattern:** CASE pivot. **LeetCode cousins:** 1479-style, 1445-style.

## Table: `sales(product, weekday, amount)`

`weekday` is `'Mon'`, `'Tue'`, or `'Wed'`.

## Task

One row per product: `product`, `mon`, `tue`, `wed` — the sum of `amount` on that weekday. Missing weekdays are 0.

Order by `product`.
