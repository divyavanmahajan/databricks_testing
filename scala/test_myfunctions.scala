// Databricks notebook source
// MAGIC %run ./myfunctions

// COMMAND ----------

import org.scalatest.funsuite.AsyncFunSuite
import org.scalatest._
import org.apache.spark.sql.types.{StructType, StructField, IntegerType, FloatType, StringType}
import scala.collection.JavaConverters._

class DataTests extends AsyncFunSuite {

  val tableName   = "diamonds"
  val dbName      = "default"
  val columnName  = "clarity"
  val columnValue = "SI2"

  // Create fake data for the unit tests to run against.
  // In general, it is a best practice to not run unit tests
  // against functions that work with data in production.
  val schema = StructType(Array(
                 StructField("_c0",     IntegerType),
                 StructField("carat",   FloatType),
                 StructField("cut",     StringType),
                 StructField("color",   StringType),
                 StructField("clarity", StringType),
                 StructField("depth",   FloatType),
                 StructField("table",   IntegerType),
                 StructField("price",   IntegerType),
                 StructField("x",       FloatType),
                 StructField("y",       FloatType),
                 StructField("z",       FloatType)
               ))

  val data = Seq(
                  Row(1, 0.23, "Ideal",   "E", "SI2", 61.5, 55, 326, 3.95, 3.98, 2.43),
                  Row(2, 0.21, "Premium", "E", "SI1", 59.8, 61, 326, 3.89, 3.84, 2.31)
                ).asJava

  val df = spark.createDataFrame(data, schema)

  // Does the table exist?
  test("The table exists") {
    assert(tableExists(tableName, dbName) == true)
  }

  // Does the column exist?
  test("The column exists") {
    assert(columnExists(df, columnName) == true)
  }

  // Is there at least one row for the value in the specified column?
  test("There is at least one matching row") {
    assert(numRowsInColumnForValue(df, columnName, columnValue) > 0)
  }
}

nocolor.nodurations.nostacks.stats.run(new DataTests)

// COMMAND ----------


