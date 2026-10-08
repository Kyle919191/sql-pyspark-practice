# What Spark is

SQL runs well on one database. Spark is for **distributed** tables: the data is split across machines (or, on your laptop, across CPU cores). You still write “table in, table out.” Spark decides how to split the work.

You will practice on `local[*]` — one machine, all cores. The API is the same one you will use on a cluster later.

## The objects

- **SparkSession** — the entry point. Create it once per script.
- **DataFrame** — a table with a schema. Not a pandas DataFrame, even though `.toPandas()` exists.
- **Column** — `F.col("name")`. You build expressions from columns.
- **Transformation** — `select`, `filter`, `join`, `groupBy`. These are lazy. Spark only records the plan.
- **Action** — `show()`, `count()`, `collect()`, `toPandas()`. These run the plan.

Until you call an action, nothing happens. That is why a typo in a column name often explodes at `.show()`, not at `.filter()`.

## Spark SQL vs DataFrame API

These two are the same engine:

```python
df.filter(F.col("organic") == "Y")
spark.sql("SELECT * FROM products WHERE organic = 'Y'")
```

If you can write the SQL, you can register a temp view and use `spark.sql`. This track still makes you write the DataFrame API. Interviews and production jobs use both. The API teaches you the physical operations (shuffle, partition) that SQL hides.

## When to use which in real life

- Quick exploration, messy joins you already have in SQL → `spark.sql`
- Pipelines you will test and compose → DataFrame API
- Same problem, two styles → you, this repo

## You're ready when

You can say: DataFrame ≈ table, filter ≈ WHERE, lazy until an action. Then read lesson 02 and run `hello_spark.py`.
