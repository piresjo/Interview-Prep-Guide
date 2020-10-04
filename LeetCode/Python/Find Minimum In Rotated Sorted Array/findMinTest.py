import unittest
from findMin import *

class Test(unittest.TestCase):        
    def testBaseCases(self):
        self.assertEqual(findMin(None), -1)
        self.assertEqual(findMin([]), -1)
        self.assertEqual(findMin([1]), 1)

    def testGeneral(self):
        self.assertEqual(findMin([1, 2, 3, 4, 5]), 1)
        self.assertEqual(findMin([2, 3, 4, 5, 1]), 1)
        self.assertEqual(findMin([3, 4, 5, 1, 2]), 1)
        self.assertEqual(findMin([4, 5, 1, 2, 3]), 1)

if __name__ == '__main__':
   unittest.main()