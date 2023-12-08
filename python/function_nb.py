# Databricks notebook source
# Importing the required function from the myfunctions module
from myfunctions import *

# Specifying the table name, database name, column name and column value for checking existence
tableName   = "diamonds"
dbName      = "default"
columnName  = "clarity"
columnValue = "VVS2"

# Check if the table exists in the database
if tableExists(tableName, dbName):

  # Create a dataframe with all the columns of the table
  df = spark.sql(f"SELECT * FROM {dbName}.{tableName}")

  # Check if the specified column exists in the dataframe
  if columnExists(df, columnName):
    # If it exists, count the number of rows that have the specified value in the specified column
    numRows = numRowsInColumnForValue(df, columnName, columnValue)

    # Print the number of rows with the specified value in the specified column of the specified table in the specified schema
    print(f"There are {numRows} rows in '{tableName}' where '{columnName}' equals '{columnValue}'.")
  else:
    # If the specified column doesnot exist in the dataframe, print an error message
    print(f"Column '{columnName}' does not exist in table '{tableName}' in schema (database) '{dbName}'.")
else:
  # If the specified table doesnot exist in the specified schema, print an error message
  print(f"Table '{tableName}' does not exist in schema (database) '{dbName}'.")


# COMMAND ----------


