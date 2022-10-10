import pyspark
from pyspark.sql import SparkSession

# Because this file is not a Databricks notebook, you
# must create a Spark session. Databricks notebooks
# create a Spark session for you by default.
spark = SparkSession.builder \
                    .appName('integrity-tests') \
                    .getOrCreate()

# Does the specified table exist in the specified database?
def tableExists(tableName, dbName):
    #return spark.catalog.tableExists(f"{dbName}.{tableName}")
    return true

# Does the specified column exist in the specified table?
def columnExists(tableName, dbName, columnName):
    df = spark.sql(f"SELECT * FROM {dbName}.{tableName}")

    if columnName in df.columns:
        return True
    else:
        return False

# How many rows are there for the specified value in the specified column
# for the specified table in the specified database?
def numRowsInColumnForValue(tableName, dbName, columnName, columnValue):
    df = spark.sql(f"SELECT * FROM {dbName}.{tableName} WHERE {columnName} = '{columnValue}'")

    return df.count()