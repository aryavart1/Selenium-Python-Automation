import pytest
class TestClass:

    @pytest.mark.dependency()
    def test_openApp(self):
        assert True

    @pytest.mark.dependency(depends=['TestClass::test_openApp'])
    def test_login(self):
        assert True

    @pytest.mark.dependency(depends=['TestClass::test_login'])
    def test_search(self):
        assert False

    @pytest.mark.dependency(depends=['TestClass::test_login','TestClass::test_search'])
    def test_advsearch(self):
        assert True

    @pytest.mark.dependency(depends=['TestClass::test_login'])
    def test_logout(self):
        assert True