import pytest
import math


@pytest.mark.function
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5


@pytest.mark.regression
def  test_square():
    num = 7
    assert 7 * 7 == 49


@pytest.mark.xfail
def test_quality():
    assert 10 == 10
