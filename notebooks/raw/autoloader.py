from pyspark.sql import functions as F


# ============================================================
# 1. Widgets
# ============================================================

dbutils.widgets.text(
    "source", "s3://health-care-fraud-detection-dev/landing/claims", "Source Path"
)

dbutils.widgets.text(
    "checkpointLocation",
    "s3://health-care-fraud-detection-dev/checkpoints/claims_checkpoint",
    "Checkpoint Location",
)

dbutils.widgets.text(
    "schemaLocation",
    "s3://health-care-fraud-detection-dev/schemas/claims",
    "Schema Location",
)

dbutils.widgets.text("target", "healthcare.bronze.claims", "Target Table")


# ============================================================
# 2. Get widget values
# ============================================================

source_path = dbutils.widgets.get("source")
checkpoint_location = dbutils.widgets.get("checkpointLocation")
schema_location = dbutils.widgets.get("schemaLocation")
target_table = dbutils.widgets.get("target")


# ============================================================
# 3. Read using Auto Loader
# ============================================================

df = (
    spark.readStream.format("cloudFiles")
    .option("cloudFiles.format", "csv")
    .option("cloudFiles.schemaLocation", schema_location)
    .option("cloudFiles.schemaEvolutionMode", "rescue")
    .option("header", "true")
    .option("inferSchema", "true")
    .load(source_path)
)


# ============================================================
# 4. Add ingestion metadata
# ============================================================

df = df.select(
    "*",
    F.col("_metadata.file_path").alias("_source_file_path"),
    F.col("_metadata.file_modification_time").alias("_source_file_modified_time"),
    F.current_timestamp().alias("_load_timestamp"),
)


# ============================================================
# 5. Write to Bronze
# ============================================================

query = (
    df.writeStream.format("delta")
    .outputMode("append")
    .option("checkpointLocation", checkpoint_location)
    .trigger(availableNow=True)
    .toTable(target_table)
)
