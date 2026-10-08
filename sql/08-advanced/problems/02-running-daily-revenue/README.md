# Running daily revenue

**Pattern:** running SUM. **LeetCode cousin:** 1204 (same idea, different story).

## Table: `sales(sale_date, amount)`

One row per day, already unique.

## Task

Return `sale_date`, `amount`, and `running_revenue` = sum of `amount` from the first day through this day.

Order by `sale_date`.
