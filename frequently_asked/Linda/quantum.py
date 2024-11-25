l=[1,None,2,3,None,None,5,None]
a=[l[i] if l[i]!= None else l[i-1]  for i in range(len(l)) ]
b= [a[i] if a[i]!= None else a[i-2]  for i in range(len(a)) ]
print(b)

import pytest
@pytest.fixture(scope="function")
def get_numbers():
    print()
    first_number = (int(input("enter first number:")))
    second_number =(int(input("enter second number:")))
    return [first_number, second_number]

def test_addition(get_numbers):
    print(get_numbers[0], get_numbers[1])
    sum_of_number = sum(get_numbers)
    print(sum_of_number)
    assert sum_of_number == 5, "test failed"

import unittest

class Calculation:
    def __init__(self, a, b):
        self.a=a
        self.b=b

    def addition(self):
        return self.a+ self.b

class Test_Addition(unittest.TestCase):

    def test_number(self):
        obj = Calculation(2,3)
        self.assertEqual(obj.addition(), 5), "test failed"

if __name__=="__main__":
    unittest.main()