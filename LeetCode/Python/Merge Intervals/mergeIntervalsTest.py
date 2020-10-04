import unittest
from mergeIntervals import *

class Test(unittest.TestCase):        
    def testBaseCases(self):
        self.assertEqual(merge(None), None)
        self.assertEqual(merge([]), [])
        self.assertEqual(merge([[1, 3]]), [[1, 3]])

    def testGeneral(self):
        self.assertEqual(merge([[1, 3], [4, 6], [8, 10]]), [[1, 3], [4, 6], [8, 10]])
        self.assertEqual(merge([[8, 10], [4, 6], [1, 3]]), [[1, 3], [4, 6], [8, 10]])
        self.assertEqual(merge([[1, 4], [4, 6], [5, 10]]), [[1, 10]])

if __name__ == '__main__':
   unittest.main()