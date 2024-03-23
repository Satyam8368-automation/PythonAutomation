import math
import pytest

@pytest.mark.skip
def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

def testsquare():
   num = 7
   assert 7*7 == 49

def test_quality():
   assert 10 == 10
