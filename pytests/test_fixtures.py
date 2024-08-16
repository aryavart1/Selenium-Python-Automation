import pytest


@pytest.mark.usefixtures("setup")  # passed the fixture name mentioned in conftest file as parameter
class TestExample:

    def test_fixtureDemo(self):
        print("i will execute steps in fixtureDemo method")
        yield
        print("END of execution")

    def test_fixtureDemo1(self):
        print("i will execute steps in fixtureDemo1 method")

    def test_fixtureDemo2(self):
        print("i will execute steps in fixtureDemo2 method")

    def test_fixtureDemo3(self):
        print("i will execute steps in fixtureDemo3 method")