from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window

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

w = Window.orderBy("record_date")
result = (
    weather.withColumn("prev_temp", F.lag("temp").over(w))
    .withColumn("delta", F.col("temp") - F.col("prev_temp"))
    .orderBy("record_date")
)
