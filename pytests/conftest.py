"""Conftest file & Scope of fixtures for building Generic fixtures"""

# fixtures are used as setup and tear down methods for test cases- conftest file to generalize fixt
# fixture and make it available to all test cases (fixture name into parameters of method)
# datadriven and parameterization can be done with return statements in tuple format
# when you define fixture scope to class only, it will run once before class is initiated and at the end

import pytest

@pytest.fixture(scope="class")  # the fixture will run once before and after Class
def setup():
    print("I will be executing first --p")
    yield
    print(" I will execute last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Mr", "Robot", "rahulshettyacademy.com"]

@pytest.fixture(params=[("chrome", "Mr", "Robot"), ("Firefox", "Robot"), ("IE", "Mr")])
def crossBrowser(request):  # need to pass 'request' as a parameter when passing values from fixture
    return request.param


