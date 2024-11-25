import pytest

# @pytest.mark.t1
# def test_1():
#     x=1
#     y=2
#     assert x+y == 3, "test failed"
#     assert x != y, "test failed"
#
# def test_method_2():
#     x=1
#     y=4
#     assert x+y == 5, "test failed"
#     assert x != y, "test failed"



# class person():
#     def __init__(self, name):
#         self.name = name
#
#     def show(self):
#         print("name", self.name)
#
# obj=person("danita")
# obj2=person("latha")
# obj.show()
# obj2.show()

@pytest.fixture()
def supply_value():
    a= 5
    b=6
    c=7
    return[a,b,c]

def test_a_b(supply_value):
    z=7
    assert z==supply_value[1], "test failed"

@pytest.mark.parametrize("input1, input2, outpt", [(5,5,10), (5,6,10)])
def test_input_output(input1, input2, outpt):
    assert input1 + input2 == outpt, "test failed"


