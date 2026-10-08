"""Optional: print a plan that includes a shuffle.

    python pyspark/05-spark-specific/explain_demo.py
"""

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (
    SparkSession.builder.appName("explain")
    .master("local[*]")
    .config("spark.ui.showConsoleProgress", "false")
    .getOrCreate()
)
spark.sparkContext.setLogLevel("ERROR")

df = spark.createDataFrame(
    [(1, "a"), (1, "b"), (2, "c")],
    ["id", "label"],
)

print("filter + select (usually no shuffle):")
df.filter(F.col("id") == 1).select("label").explain()

print("groupBy (shuffle):")
df.groupBy("id").count().explain()

spark.stop()
