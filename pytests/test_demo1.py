# Pytest naming convention -> any Pytest file should start with test_ or end with _test
# pytest method name should start with test
# Any code should be wrapped in methods only
# To run on command prompt -> py.test -v -s

def test_firstProgram():
    message = "Hello"
    assert message == "Hello", "Test Failed"
