# SparkSession and DataFrames

## Start a session

```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (
    SparkSession.builder.appName("practice")
    .master("local[*]")
    .getOrCreate()
)
```

`getOrCreate()` reuses a session if one exists. The checker calls `spark.stop()` when it finishes.

## Read a CSV

```python
from pathlib import Path

products = (
    spark.read.option("header", True)
    .option("inferSchema", True)
    .csv(str(Path(__file__).parent / "products.csv"))
)
products.printSchema()
products.show()
```

`inferSchema` guesses types. Fine for practice. In jobs you pass an explicit schema so a bad file fails loudly.

## Look at a frame

```python
df.show(20, truncate=False)
df.printSchema()
df.columns
df.count()          # action — reads all data
df.limit(5).show()
```

## Create columns, keep columns, rename

```python
df.select("product_id", "name")
df.select(F.col("name").alias("product_name"))
df.withColumn("price_dollars", F.col("price_cents") / 100)
df.withColumnRenamed("name", "product_name")
```

`select` is SQL SELECT. `withColumn` adds or replaces one column and keeps the rest.

## Filter

```python
df.filter(F.col("organic") == "Y")
df.where((F.col("organic") == "Y") & (F.col("on_sale") == "Y"))
```

Python `and` / `or` do not work on Spark columns. Use `&`, `|`, `~`, and parentheses.

## NULL

```python
df.filter(F.col("referrer_id").isNull())
df.filter(F.col("referrer_id").isNotNull())
df.filter((F.col("referrer_id") != 2) | F.col("referrer_id").isNull())
```

Same trap as SQL.

## Distinct, sort, limit

```python
df.select("viewer_id").distinct()
df.orderBy(F.col("rating").desc())
df.limit(3)
```

## The contract for this repo

Your script must leave a DataFrame in a variable named `result`. The checker converts it to pandas and compares `expected.csv`.

## Run the playground

```bash
python pyspark/00-fundamentals/playground/hello_spark.py
python tools/check.py pyspark/00-fundamentals/playground
```

## You're ready when

You can read a CSV, `filter`, `select`, and `show` without copying. Then read the SQL ↔ PySpark map and start the Select twins.
