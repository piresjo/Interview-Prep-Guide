import unittest
from singleNumber import *

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(singleNumber([1, 2, 2, 3, 4, 1, 3]), 4)
        self.assertEqual(singleNumber([1]), 1)
        self.assertEqual(singleNumber([1, 2, 2, 3, 4, 1, 3, 4]), 0)


if __name__ == '__main__':
   unittest.main()