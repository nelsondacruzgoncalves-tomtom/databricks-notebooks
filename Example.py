# Databricks notebook source
import myfunctions

tableName   = "diamonds"
dbName      = "default"
columnName  = "clarity"
columnValue = "VVS2"

# If the table exists in the specified database...
if tableExists(tableName, dbName):
  # And the specified column exists in that table...
  if columnExists(tableName, dbName, columnName):
    # Then report the number of rows for the specified value in that column.
    numRows = numRowsInColumnForValue(tableName, dbName, columnName, columnValue)

    print(f"There are {numRows} rows in '{tableName}' where '{columnName}' equals '{columnValue}'.")
  else:
    print(f"Column '{columnName}' does not exist in table '{tableName}' in database '{dbName}'.")
else:
  print(f"Table '{tableName}' does not exist in database '{dbName}'.")
