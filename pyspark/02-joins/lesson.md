# Joins in PySpark

Same four shapes as SQL.

```python
# inner lookup
orders.join(products, on="product_id", how="inner")

# left keep-all
employees.join(employee_ids, on="id", how="left")

# anti-join
visits.join(purchases, on="visit_id", how="left_anti")

# self-join
today = weather.alias("today")
prev = weather.alias("prev")
today.join(prev, F.col("today.record_date") == F.date_add(F.col("prev.record_date"), 1), "inner")
```

`how="left_anti"` is the unmatched-left rows. It is cleaner than LEFT + `isNull`. SQL people write the `IS NULL` form; Spark people often use `left_anti`. Both are correct.

## Twins

| PySpark | SQL folder |
| --- | --- |
| `01-orders-with-products` | `sql/02-basic-joins/problems/01-orders-with-products` |
| `02-employee-unique-id` | `sql/02-basic-joins/problems/02-employee-unique-id` |
| `03-visits-without-purchases` | `sql/02-basic-joins/problems/03-visits-without-purchases` |
| `04-warmer-than-yesterday` | `sql/02-basic-joins/problems/04-warmer-than-yesterday` |
| `05-employees-below-bonus` | `sql/02-basic-joins/problems/05-employees-below-bonus` |

After a join, `.select(...)` the columns you need so you do not leak `id` twice.
