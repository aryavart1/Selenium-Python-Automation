@pytest.mark.smoke
def test_FirstProgram():
    message = "Hello"
    assert message == "Hi", "Test Failed because strings do not match"

def test_SecondProgram():
    a = 2
    b = 6
    assert a+4 == b, "Addition doesn't match"
