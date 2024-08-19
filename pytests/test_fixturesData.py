"""Data driven Fixtures to load data into tests"""

# In case of returning data from the fixture it's mandatory to pass the fixture name as a parameter to the TC although
# its declared globally

import pytest

from pytests.BaseClass import BaseClass


# from pytestsDemo.BaseClass import BaseClass
@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_editProfile(self, dataLoad):
        print(dataLoad[0])
        print(dataLoad[2])
        log = self.getLogger()
        log.info(dataLoad[0])
        log.info(dataLoad[2])
        print(dataLoad[2])

