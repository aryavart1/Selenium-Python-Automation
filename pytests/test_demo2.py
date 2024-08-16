# fixtures are used as setup and tear down methods for test cases- conftest file to generalize fixt
# fixture and make it available to all test cases (fixture name into parameters of method)
# datadriven and parameterization can be done with return statements in tuple format
# when you define fixture scope to class only, it will run once before class is initiated and at the end


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
