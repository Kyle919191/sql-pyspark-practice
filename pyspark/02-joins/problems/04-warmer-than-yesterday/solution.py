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

weather = (
    spark.read.option("header", True)
    .option("inferSchema", True)
    .csv(str(Path(__file__).parent / "weather.csv"))
)

today = weather.alias("today")
prev = weather.alias("prev")
result = (
    today.join(prev, F.col("today.record_date") == F.date_add(F.col("prev.record_date"), 1), "inner")
    .filter(F.col("today.temp") > F.col("prev.temp"))
    .select(F.col("today.id").alias("id"))
)
