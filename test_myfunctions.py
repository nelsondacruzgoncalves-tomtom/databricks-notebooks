import pytest
import myfunctions


def test_getTables():
    assert len(myfunctions.getTables()) is 1
    
def test_isEven():
    assert myfunctions.isEven(2) is True
    assert myfunctions.isEven(3) is False

# Does the column exist?
#def test_columnExists():
#      assert myfunctions.columnExists(tableName, dbName, columnName) is True

# Is there at least one row for the value in the specified column?
#def test_numRowsInColumnForValue():
#      assert myfunctions.numRowsInColumnForValue(tableName, dbName, columnName, columnValue) > 0