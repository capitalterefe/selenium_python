import pytest
@pytest.mark.usefixtures("oneTimeSetUp")
class TestClassDemo():
    
    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetUp):
        self.field_value=self.browserType

    def test_pp(self):
        print("Running test_pp")
        print(self.field_value)
    
    def test_dd(self):
        print("Running test_pp")