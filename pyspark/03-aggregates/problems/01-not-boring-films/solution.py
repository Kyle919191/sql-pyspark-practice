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

films = (
    spark.read.option("header", True)
    .option("inferSchema", True)
    .csv(str(Path(__file__).parent / "films.csv"))
)

result = (
    films.filter((F.col("id") % 2 == 1) & (F.col("description") != "boring"))
    .orderBy(F.col("rating").desc())
    .select("id", "title", "description", "rating")
)
