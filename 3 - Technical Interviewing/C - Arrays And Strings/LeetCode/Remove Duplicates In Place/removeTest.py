import unittest
from remove import *

class Test(unittest.TestCase):

    def testGeneral(self):
        self.assertEqual(removeDuplicates([3, 2, 2, 3]), 2)
        self.assertEqual(removeDuplicates([1, 2, 3, 4]), 0)
        self.assertEqual(removeDuplicates([]), 0)
        self.assertEqual(removeDuplicates([1, 2, 2, 2, 2, 2, 3]), 5)
        


if __name__ == '__main__':
   unittest.main()