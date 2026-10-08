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

employees = (
    spark.read.option("header", True)
    .option("inferSchema", True)
    .csv(str(Path(__file__).parent / "employees.csv"))
)

bonuses = (
    spark.read.option("header", True)
    .option("inferSchema", True)
    .csv(str(Path(__file__).parent / "bonuses.csv"))
)

result = (
    employees.join(bonuses, employees.id == bonuses.emp_id, "left")
    .filter((F.col("bonus") < 500) | F.col("bonus").isNull())
    .select("name", "bonus")
)
