import unittest

class cal:
    def __init__(self, a, b):
        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b

class test_num(unittest.TestCase):
    def test_check(self):
        obj=cal(5,4)
        self.assertEqual(obj.add(),10),"test failed"

if __name__=="__main__":
    unittest.main()