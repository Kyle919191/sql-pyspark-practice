# Aggregates in PySpark

```python
df.groupBy("class").agg(F.countDistinct("student").alias("n")).filter(F.col("n") >= 3)

df.agg(
    F.count("*").alias("n"),
    F.avg("price").alias("avg_price"),
)

F.when(F.col("status") == "ok", 1.0).otherwise(0.0)
# then F.avg(that) for a rate
```

`HAVING` is just another `filter` after `agg`.

Twins: `01-not-boring-films`, `02-average-selling-price` — same as `sql/03-aggregates/problems/`.
