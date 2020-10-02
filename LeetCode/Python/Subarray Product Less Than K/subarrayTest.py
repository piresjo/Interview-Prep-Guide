import unittest
from subarray import *

class Test(unittest.TestCase):
    def testGeneral(self):
        self.assertEqual(numSubarrayProductLessThanK([10,5,2,6], 100), 8)
        self.assertEqual(numSubarrayProductLessThanK([10,5,2,6], 1), 0)
        self.assertEqual(numSubarrayProductLessThanK([10,5,2,6], 0), 0)
        self.assertEqual(numSubarrayProductLessThanK([1, 2, 3, 4], 1), 0)
        self.assertEqual(numSubarrayProductLessThanK([1, 2, 3, 4], 2), 1)
        self.assertEqual(numSubarrayProductLessThanK([1, 2, 3, 4], 3), 3)
        

if __name__ == '__main__':
   unittest.main()
