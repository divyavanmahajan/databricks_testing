// Databricks notebook source
// MAGIC %run ./myfunctions

// COMMAND ----------

val tableName   = "diamonds"
val dbName      = "default"
val columnName  = "clarity"
val columnValue = "VVS2"

// If the table exists in the specified database...
if (tableExists(tableName, dbName)) {

  val df = spark.sql("SELECT * FROM " + dbName + "." + tableName)

  // And the specified column exists in that table...
  if (columnExists(df, columnName)) {
    // Then report the number of rows for the specified value in that column.
    val numRows = numRowsInColumnForValue(df, columnName, columnValue)

    println("There are " + numRows + " rows in '" + tableName + "' where '" + columnName + "' equals '" + columnValue + "'.")
  } else {
    println("Column '" + columnName + "' does not exist in table '" + tableName + "' in database '" + dbName + "'.")
  }

} else {
  println("Table '" + tableName + "' does not exist in database '" + dbName + "'.")
}

// COMMAND ----------


