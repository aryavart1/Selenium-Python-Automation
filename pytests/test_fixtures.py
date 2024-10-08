""" Data driven Fixtures to load data into tests """
# datadriven and parameterization can be done with return statements in tuple format
# when you define fixture scope to class only, it will run once before class is initiated and at the end

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