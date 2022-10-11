import pytest
import myfunctions


def test_getTables():
    assert len(myfunctions.getTables()) is 1
    
def test_isEven():
    assert myfunctions.isEven(2) is True
    assert myfunctions.isEven(3) is False
