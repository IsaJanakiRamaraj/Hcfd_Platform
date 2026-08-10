from pyspark import SparkSession
from pyspark.sql import functions as F

dbutils.widgets.text("source", "s3://health-care-fraud-detection-dev/landing/claims")
dbutils.widgets.text("checkpointLocation", "s3://health-care-fraud-detection-dev/checkpoints/claims_check_point")
dbutils.widgets.text("target", " healthcare.bronze.claims")

source_path = dbutils.widgets.get("source", "")
checkpointLocation = dbutils.widgets.get("checkpointLocation", "")
target_path = dbutils.widgets.get("target", "")

df = (
    spark.readStream.format("cloudFiles.format", "csv")
    .option("header", "true")
    .option("inferschema", "true")
    .option("cloudFiles.schemaEvolutionMode", "rescue")
    .load(source_path)
    .select(
        "*",
        F.col("_metadata.file_path").alias("_source_file_path"),
        F.col("_metadata.file_modification_time").alias("_source_file_modified_time"),
        F.current_timestamp().alias("_load_timestamp"),
    )
)


query = (
    df.writeStream.format("delta")
    .outputMode("append")
    .option("checkpointLocation", checkpointLocation)
    .toTable(target_path)
)
