import pyspark
from pyspark.sql import SparkSession


# Because this file is not a Databricks notebook, you
# must create a Spark session. Databricks notebooks
# create a Spark session for you by default.
spark = SparkSession.builder \
                    .appName('integrity-tests') \
                    .getOrCreate()


def getTables():
    return spark.catalog.listTables()

def isEven(num):
    return (num % 2) == 0
