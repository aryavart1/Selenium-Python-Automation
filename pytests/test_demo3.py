""" Parameterizing test with multiple data sets using Fixtures """

# datadriven and parameterization can be done with return statements in tuple format
# when you define fixture scope to class only, it will run once before class is initiated and at the end


def test_crossBrowser(crossBrowser):
    print(crossBrowser)