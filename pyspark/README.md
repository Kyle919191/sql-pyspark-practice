# PySpark track

Do this after SQL Select and Joins feel comfortable. A DataFrame is a table. `filter` is `WHERE`. `join` is `JOIN`. You already know the ideas.

## Why this format (not random Spark tutorials)

Each local SQL problem has a twin here. You solve the same business question with the DataFrame API. That is how data engineers actually switch between Spark SQL and PySpark.

There is also a short Spark-only lesson (`05-spark-specific/`) for lazy evaluation, partitions, and shuffle. Those do not show up on LeetCode. They show up when a job is slow.

## Order

1. `00-fundamentals/` — what Spark is, SparkSession, SQL ↔ PySpark map
2. `01-select-filter/` — the five Select twins
3. `02-joins/` — the five join twins
4. `03-aggregates/`
5. `04-windows/`
6. `05-spark-specific/`

## How to run

```bash
python tools/check.py pyspark/01-select-filter/problems/01-organic-onsale
```

Edit `starter.py`. Assign a DataFrame to `result`. First Spark start on a machine is slow (10–20s). Later checks reuse the JVM if one is still up; this checker stops the session after each run, so expect a cold start each time.

## Saving work

`pyspark/solutions/<module>_<problem>.py`
