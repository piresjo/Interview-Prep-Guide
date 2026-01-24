import unittest
from searchInsertPosition import *

class Test(unittest.TestCase):

    def testGeneral(self):
        self.assertEqual(searchInsert([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(searchInsert([1, 2, 3, 4], 5), 4)
        


if __name__ == '__main__':
   unittest.main()