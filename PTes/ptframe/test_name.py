import pytest

def get_Data():
    return [
        ("Satyam.agnihotri","TEST"),
        ("TEST@131","TEST&&")
    ]
@pytest.mark.parametrize("username,password", get_Data())
def test_dis(username, password):
    print(username,password)
