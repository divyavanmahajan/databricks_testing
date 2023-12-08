// Databricks notebook source
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.functions.col

// Does the specified table exist in the specified database?
def tableExists(tableName: String, dbName: String) : Boolean = {
  return spark.catalog.tableExists(dbName + "." + tableName)
}

// Does the specified column exist in the given DataFrame?
def columnExists(dataFrame: DataFrame, columnName: String) : Boolean = {
  val nameOfColumn = null

  for(nameOfColumn <- dataFrame.columns) {
    if (nameOfColumn == columnName) {
      return true
    }
  }

  return false
}

// How many rows are there for the specified value in the specified column
// in the given DataFrame?
def numRowsInColumnForValue(dataFrame: DataFrame, columnName: String, columnValue: String) : Long = {
  val df = dataFrame.filter(col(columnName) === columnValue)

  return df.count()
}
