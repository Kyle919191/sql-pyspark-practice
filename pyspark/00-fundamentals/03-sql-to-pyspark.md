# SQL ↔ PySpark map

Keep this open while you remirror SQL problems.

| SQL | PySpark |
| --- | --- |
| `SELECT a, b` | `df.select("a", "b")` |
| `SELECT a AS x` | `df.select(F.col("a").alias("x"))` |
| `WHERE a = 1` | `df.filter(F.col("a") == 1)` |
| `AND` / `OR` / `NOT` | `&` / `\|` / `~` (parentheses required) |
| `IS NULL` | `F.col("a").isNull()` |
| `IN ('x','y')` | `F.col("a").isin("x", "y")` |
| `LIKE '%x%'` | `F.col("a").contains("x")` or `like("%x%")` |
| `ORDER BY a DESC` | `df.orderBy(F.col("a").desc())` |
| `LIMIT n` | `df.limit(n)` |
| `DISTINCT` | `df.select(...).distinct()` |
| `length(a)` | `F.length("a")` |
| `CASE WHEN …` | `F.when(cond, val).when(...).otherwise(val)` |
| `INNER JOIN … ON` | `a.join(b, a.id == b.a_id, "inner")` |
| `LEFT JOIN` | `a.join(b, on="id", how="left")` |
| `GROUP BY a` | `df.groupBy("a").agg(...)` |
| `count(*)` | `F.count(F.lit(1))` or `F.count("*")` |
| `count(DISTINCT a)` | `F.countDistinct("a")` |
| `HAVING` | `agg(...).filter(...)` |
| `sum() OVER (PARTITION BY …)` | `F.sum("x").over(Window.partitionBy("g").orderBy("t"))` |
| `LAG` | `F.lag("x").over(w)` |
| `COALESCE` | `F.coalesce(F.col("a"), F.lit(0))` |
| `round(x, 2)` | `F.round("x", 2)` |

Join with a shared column name:

```python
orders.join(products, on="product_id", how="inner")
```

Join with different names:

```python
visits.join(purchases, visits.visit_id == purchases.visit_id, "left")
```

After a join with two `visit_id` columns, qualify them or drop one. Duplicate names are a common Spark footgun.

## Spark SQL escape hatch

```python
products.createOrReplaceTempView("products")
result = spark.sql("""
    SELECT product_id, name
    FROM products
    WHERE organic = 'Y' AND on_sale = 'Y'
""")
```

Allowed as a way to check your logic. For this track, prefer the API so you learn it.

## You're ready when

You can look at a SQL solution you already wrote and rename each clause to a method without inventing new logic.
