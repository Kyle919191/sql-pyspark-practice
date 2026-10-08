from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (
    SparkSession.builder.appName("practice")
    .master("local[*]")
    .config("spark.ui.showConsoleProgress", "false")
    .getOrCreate()
)
spark.sparkContext.setLogLevel("ERROR")

visits = (
    spark.read.option("header", True)
    .option("inferSchema", True)
    .csv(str(Path(__file__).parent / "visits.csv"))
)

purchases = (
    spark.read.option("header", True)
    .option("inferSchema", True)
    .csv(str(Path(__file__).parent / "purchases.csv"))
)

# Write your solution. Assign the final DataFrame to `result`.
result = None
