# Importing required libraries
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Creating a Spark session
# A SparkSession is used to programatically interact with Spark and start the underlying Spark functionality.
# The configuration of this builder is used to create a SparkSession which is required to create DataFrames or Dataset API.
spark = SparkSession.builder \
                    .appName('integrity-tests') \
                    .getOrCreate()

# Function that checks if a specified table exists in the specified database.
# This involves creating a Catalog so that the metadata about the tables and databases can be queried.
# Returns true when table exists, false otherwise.
def tableExists(tableName, dbName):
  return spark.catalog.tableExists(f"{dbName}.{tableName}")

# Function that checks if a specified column exists within a given DataFrame.
# Returns true when column exists within DataFrame, false otherwise.
def columnExists(dataFrame, columnName):
  if columnName in dataFrame.columns:
    return True
  else:
    return False

# Function that counts the number of rows present within a DataFrame for a specific column value.
# This method performs a filter operation to get a DataFrame with the specific column value,
# then counts the number of rows present in that DataFrame and returns the count.
def numRowsInColumnForValue(dataFrame, columnName, columnValue):
  df = dataFrame.filter(col(columnName) == columnValue)

  return df.count()

