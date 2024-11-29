import unittest
from longest import *

class Test(unittest.TestCase):
    def testGeneral(self):
        self.assertEqual(findLongestSubarrayBySum(15, []), [-1])
        self.assertEqual(findLongestSubarrayBySum(15, [1, 2, 3, 4]), [-1])
        self.assertEqual(findLongestSubarrayBySum(15, [1, 2, 3, 4, 5]), [1, 5])
        self.assertEqual(findLongestSubarrayBySum(15, [5, 5, 5, 1, 2, 3, 4]), [3, 7])


if __name__ == '__main__':
   unittest.main()