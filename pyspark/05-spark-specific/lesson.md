# Spark-specific ideas (no LeetCode)

You do not need these to pass SQL 50. You need them so Spark is not a mystery box.

## Lazy evaluation

```python
df2 = df.filter(F.col("x") > 0).select("id")   # plan only
df2.count()                                    # runs
```

Spark fuses those steps. Calling `.count()` then `.show()` can scan twice. Reuse one action, or `cache()` if you really iterate (practice data is tiny — do not cache by habit).

## Partitions

A DataFrame is split into partitions. `local[*]` ≈ one partition per core. `df.rdd.getNumPartitions()` shows the number.

- **Narrow** transform (filter, select): each partition stays put.
- **Wide** transform (join, groupBy, window with partitionBy): **shuffle** — rows move so matching keys share a machine.

Shuffles are the usual reason a “simple” group-by is slow.

## Explain

```python
df.groupBy("id").count().explain(True)
```

You will see `Exchange` (shuffle) and `HashAggregate`. You do not need to memorize plans. Notice whether a shuffle appeared.

## Spark SQL is still Spark

```python
df.createOrReplaceTempView("t")
spark.sql("SELECT id, count(*) FROM t GROUP BY id").show()
```

Same optimizer as the API.

## What to do with this

After you finish the window twins, pick one SQL 50 medium you already solved and rewrite it in PySpark two ways: DataFrame API and `spark.sql`. Compare `.explain()`. That is enough Spark theory until you have a real cluster job.
