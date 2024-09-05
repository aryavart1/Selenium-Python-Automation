import pytest

@pytest.fixture()  # decorator
def setup():
    print("Launching browser...")  # Executes once before every test method
    yield
    print("closing browser..")  # Executes Once after every test method