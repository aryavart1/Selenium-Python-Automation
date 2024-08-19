# Pytest naming convention -> any Pytest file should start with test_ or end with _test
# pytest method name should start with test
# Any code should be wrapped in methods only
# To run on command prompt -> py.test -v -s
# To run a specific test file -> py.test <file name> -v -s
# To run specific test methods -> py.test -k <method name or expression> -v -s
# -k stands for method names execution, -s logs in output, -v stands for more info metadata
# To run testcases that are marked (tagged) -> py.test -m <tag_name> -v -s
# you can skip tests with @pytest.mark.skip
# @pytest.mark.xfail -> to run TC without displaying output
# fixtures are used as setup and tear down methods for test cases- conftest file to generalize fixt
# fixture and make it available to all test cases (fixture name into parameters of method)
# datadriven and parameterization can be done with return statements in tuple format
# when you define fixture scope to class only, it will run once before class is initiated and at the end

import pytest
@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram(setup):
    print("PANAMA")

# @pytest.mark.xfail
def test_SecondGreetCreditCard():
    title = "Lizaaaa first demo session"
    assert title == "Amazon"

@pytest.fixture()
def setup():
    print("I will be executing first")
    yield
    print("last")

def test_fixtureDemo(setup):
    print("I will execute steps in fixture demo method")

"""
import pytest
@pytest.mark.smoke  # will run Testcases which are marked as Smoke
@pytest.mark.skip   # to skip particular test case
def test_firstProgram():
    message = "Hello"
    assert message == "Hello", "Test Failed"  # If the TC gets failed it will print a different message


@pytest.mark.xfail   # tc will run but will not be displayed in output
def test_SecondProgram():
    message = "Hello"
    assert message == "Hello", "Test Failed"
"""