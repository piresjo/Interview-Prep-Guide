import unittest
from arrayMax import *

class Test(unittest.TestCase):
    def testGeneral(self):
        self.assertEqual(arrayMaxConsecutiveSum2([2, -1, 3, 5, -7]), 9)
        self.assertEqual(arrayMaxConsecutiveSum2([-2, 2, 5, -11, 6]), 7)


if __name__ == '__main__':
   unittest.main()