import unittest

class person(unittest.TestCase):

    def test_name(self):
        aname='some'
        bname='some'
        self.assertEqual(aname, bname)

    def test(self):
        self.assertTrue(True)
if __name__ == '__main__':
    unittest.main()

import unittest


class SimpleTest(unittest.TestCase):

    # Returns True or False.
    def test(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()


