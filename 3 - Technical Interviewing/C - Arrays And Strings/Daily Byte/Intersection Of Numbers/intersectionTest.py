import unittest
from intersection import *

class Test(unittest.TestCase):        
    def testGeneral(self):
        self.assertEqual(intersection([2, 4, 4, 2], [2, 4]), [2, 4])
        self.assertEqual(intersection([1, 2, 3, 3], [3, 3]), [3])
        self.assertEqual(intersection([2, 4, 6, 8], [1, 3, 5, 7]), [])

if __name__ == '__main__':
   unittest.main()
