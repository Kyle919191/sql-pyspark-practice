"""Print a tiny DataFrame so you can see Spark start.

Run:
    python pyspark/00-fundamentals/playground/hello_spark.py
"""

from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (
    SparkSession.builder.appName("hello")
    .master("local[*]")
    .config("spark.ui.showConsoleProgress", "false")
    .getOrCreate()
)
spark.sparkContext.setLogLevel("ERROR")

products = (
    spark.read.option("header", True)
    .option("inferSchema", True)
    .csv(str(Path(__file__).parent / "products.csv"))
)

print("schema:")
products.printSchema()
print("all rows:")
products.show()
print("in stock, cheaper than 300 cents:")
products.filter((F.col("in_stock") == True) & (F.col("price_cents") < 300)).show()

spark.stop()
