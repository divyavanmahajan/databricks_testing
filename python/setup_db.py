# Databricks notebook source
# Importing required modules
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, FloatType, StringType

# Defining schema for dataset
schema = StructType([ \
  StructField("_c0",     IntegerType(), True), \
  StructField("carat",   FloatType(),   True), \
  StructField("cut",     StringType(),  True), \
  StructField("color",   StringType(),  True), \
  StructField("clarity", StringType(),  True), \
  StructField("depth",   FloatType(),   True), \
  StructField("table",   IntegerType(), True), \
  StructField("price",   IntegerType(), True), \
  StructField("x",       FloatType(),   True), \
  StructField("y",       FloatType(),   True), \
  StructField("z",       FloatType(),   True), \
])

# Creating sample dataset
data = [ (1, 0.23, "Ideal",   "E", "SI2", 61.5, 55, 326, 3.95, 3.98, 2.43 ), \
         (2, 0.21, "Premium", "E", "SI1", 59.8, 61, 326, 3.89, 3.84, 2.31 ),
         (3, 0.21, "Premium", "E", "VVS2", 59.8, 61, 326, 3.89, 3.84, 2.31 ) ]

# Creating DataFrame from sample dataset and schema defined
df = spark.createDataFrame(data, schema)

# Writing data to the hive table
df.write.mode(saveMode="overwrite").saveAsTable('hive_metastore.default.diamonds')


# COMMAND ----------


