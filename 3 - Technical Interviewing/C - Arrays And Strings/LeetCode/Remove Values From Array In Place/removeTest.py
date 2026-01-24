import unittest
from remove import *

class Test(unittest.TestCase):

    def testGeneral(self):
        self.assertEqual(removeElement([3, 2, 2, 3], 3), 2)
        self.assertEqual(removeElement([1, 2, 3, 4], 5), 0)
        self.assertEqual(removeElement([], 0), 0)
        self.assertEqual(removeElement([1, 2, 2, 2, 2, 2, 3], 2), 5)
        


if __name__ == '__main__':
   unittest.main()