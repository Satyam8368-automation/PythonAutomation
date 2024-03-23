import pytest

@pytest.mark.xfail
def test_name():
    print("SATYAM")
@pytest.mark.skip
def test_res():
    print("SATYAM")
@pytest.mark.FT
def test_cal():
    assert 2+2==4
