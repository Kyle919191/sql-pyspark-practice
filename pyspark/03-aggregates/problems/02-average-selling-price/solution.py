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

prices = (
    spark.read.option("header", True)
    .option("inferSchema", True)
    .csv(str(Path(__file__).parent / "prices.csv"))
)

sales = (
    spark.read.option("header", True)
    .option("inferSchema", True)
    .csv(str(Path(__file__).parent / "sales.csv"))
)

joined = prices.join(
    sales,
    (prices.product_id == sales.product_id)
    & (sales.sale_date >= prices.start_date)
    & (sales.sale_date <= prices.end_date),
    "left",
)
result = joined.groupBy(prices.product_id.alias("product_id")).agg(
    F.round(
        F.coalesce(F.sum(F.col("price") * F.col("units")) / F.nullif(F.sum("units"), F.lit(0)), F.lit(0)),
        2,
    ).alias("average_price")
)
