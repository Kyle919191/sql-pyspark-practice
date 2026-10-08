# Windows in PySpark

```python
from pyspark.sql import Window

dept = Window.partitionBy("department").orderBy(F.col("score").desc())
df.withColumn("score_rank", F.dense_rank().over(dept))

by_date = Window.orderBy("sale_date").rowsBetween(Window.unboundedPreceding, Window.currentRow)
df.withColumn("running_revenue", F.sum("amount").over(by_date))

df.withColumn("prev_temp", F.lag("temp").over(Window.orderBy("record_date")))
```

Twins of `sql/08-advanced/problems/01-exam-ranks`, `02-running-daily-revenue`, `03-previous-day-delta`.
