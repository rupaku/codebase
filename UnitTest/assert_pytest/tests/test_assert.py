import pytest

#@pytest.mark.skip("WIP")
#@pytest.mark.skipif(sys.version_info < (3,6))
@pytest.mark.demo_test
class Demo:
    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_variable_exist(self):
        ls=["a","b"]
        assert "a" in ls
        

    