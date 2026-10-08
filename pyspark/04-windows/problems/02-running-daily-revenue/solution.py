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

sales = (
    spark.read.option("header", True)
    .option("inferSchema", True)
    .csv(str(Path(__file__).parent / "sales.csv"))
)

w = Window.orderBy("sale_date").rowsBetween(Window.unboundedPreceding, Window.currentRow)
result = sales.withColumn("running_revenue", F.sum("amount").over(w)).orderBy("sale_date")
