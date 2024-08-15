import pytest


@pytest.mark.smoke
# @pytest.mark.skip
def test_firstProgram():
    msg = "Hello"  # operations
    assert msg == "Hi", "Test failed because strings do not match"


def test_SecondCreditCard():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition do not match"


"""@pytest.mark.smoke
def test_FirstProgram():
    message = "Hello"
    assert message == "Hi", "Test Failed because strings do not match"

def test_SecondProgram():
    a = 2
    b = 6
    assert a+4 == b, "Addition doesn't match"
"""
