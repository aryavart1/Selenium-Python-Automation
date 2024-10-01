import pytest

class TestClass:

    @pytest.mark.sanity
    def test_LoginByEmail(self):
        print("This is login by email........")
        assert 1 == 1

    @pytest.mark.sanity
    def test_LoginByFacebook(self):
        print("This is login by facebook........")
        assert 1 == 1

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_LoginByTwitter(self):
        print("This is login by twitter........")
        assert 1 == 1

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_signupByEmail(self):
        print("This is signup by email test")
        assert True == True

    @pytest.mark.regression
    def test_signupByFacebook(self):
        print("This is signup by facebook test")
        assert True == True

    @pytest.mark.regression
    def test_signupbytwitter(self):
        print("This is signup by twitter test")
        assert True == True
