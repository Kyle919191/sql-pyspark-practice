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

customers = (
    spark.read.option("header", True)
    .option("inferSchema", True)
    .csv(str(Path(__file__).parent / "customers.csv"))
)

result = customers.filter(
    (F.col("referrer_id") != 2) | F.col("referrer_id").isNull()
).select("id", "name")
