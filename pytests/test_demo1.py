# Pytest naming convention -> any Pytest file should start with test_ or end with _test
# pytest method name should start with test
# Any code should be wrapped in methods only
# To run on command prompt -> py.test -v -s
# To run a specific test file -> py.test <file name> -v -s
# To run specific test methods -> py.test -k <method name or expression> -v -s
# -k stands for method names execution, -s logs in output, -v stands for more info metadata

import pytest


@pytest.mark.smoke
def test_firstProgram():
    message = "Hello"
    assert message == "Hello", "Test Failed" # If the TC gets failed it will print a different message
