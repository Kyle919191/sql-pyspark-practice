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

exams = (
    spark.read.option("header", True)
    .option("inferSchema", True)
    .csv(str(Path(__file__).parent / "exams.csv"))
)

w = Window.partitionBy("department").orderBy(F.col("score").desc())
result = (
    exams.withColumn("score_rank", F.dense_rank().over(w))
    .orderBy("department", "score_rank", "name")
    .select("department", "name", "score", "score_rank")
)
