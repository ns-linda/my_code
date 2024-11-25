import pytest


# @pytest.fixture(scope ="class")
# def test_prepare_db(request):
#     request.cls.num = 5
#     request.cls.num2=6
#
# @pytest.mark.usefixtures("test_prepare_db")
# class Test_db_example:
#     def test_query(self):
#         assert add(self.num,self.num2) == 11, "failed"

@pytest.fixture(scope="class")
def test_prepare_db(request):
    request.cls.connect= "connected"

@pytest.mark.usefixtures("test_prepare_db")
class Test_db_example:
    def test_db_connect(self):
        # assert self.connect == "connected", "test failed"
        assert self.connect == "connected", "failed"


def add(num1,num2):
    return num1+num2


def test_method():
    x=1
    assert x ==1, "failed"

