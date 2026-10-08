# Pivot (rows to columns)

Pivoting is conditional aggregation:

```sql
SELECT
    product,
    sum(CASE WHEN weekday = 'Mon' THEN amount ELSE 0 END) AS mon,
    sum(CASE WHEN weekday = 'Tue' THEN amount ELSE 0 END) AS tue
FROM sales
GROUP BY product;
```

Each CASE keeps one weekday and zeros the rest. `GROUP BY product` collapses to one row per product.

## Unpivot (columns to rows)

The opposite: `UNION ALL` of one column per original measure, or DuckDB `UNPIVOT`. LeetCode 1795 (rearrange products table) is unpivot.

```sql
SELECT product_id, 'store1' AS store, store1 AS price FROM products WHERE store1 IS NOT NULL
UNION ALL
SELECT product_id, 'store2', store2 FROM products WHERE store2 IS NOT NULL;
```

## Empty categories

If a category might have zero rows, a plain `GROUP BY` will omit it. Build the category list first, then LEFT JOIN counts (salary categories, 1907).

## Pattern

- Known, small set of columns (weekdays, stores, genders) → CASE pivot
- Unknown set of columns → do not pivot in SQL; do it in PySpark / pandas
- Columns that should become rows → UNION ALL unpivot

## You're ready when

You can write a weekday pivot without thinking. Then the local sales-by-weekday problem.
