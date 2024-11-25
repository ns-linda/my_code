from ast import In
import pytest

class Testfunc:

    @pytest.fixture(autouse=True)
    def call_first_test(self):
        print("Fixtures called first")

    def test_1(self):
        print("method1")


    def test_1(self):
        print("method2")

    @pytest.mark.parametrize("Input",[(1,2,3)])
    def test_add(self, Input):
        assert Input[0]+Input[1]==3, "failed"

    @pytest.mark.parametrize("Input",[1,2,3])
    def test_add(self, Input):
        print(Input)