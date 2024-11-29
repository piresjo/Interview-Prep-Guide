import unittest
from twoSum import *

class Test(unittest.TestCase):

    def testEdgeCases(self):
        self.assertEqual(twoSum(None, None), [])
        self.assertEqual(twoSum(None, 20), [])
        self.assertEqual(twoSum([2, 3, 4, 5, 6], None), [])
        self.assertEqual(twoSum([2], 2), [])

    def testGeneral(self):
        self.assertEqual(twoSum([1, 2, 3, 4, 5, 6], 10), [3, 5])
        self.assertEqual(twoSum([1, 5, 6, 7, 8], 29), [])


   

if __name__ == '__main__':
   unittest.main()