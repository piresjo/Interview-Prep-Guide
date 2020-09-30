import unittest
from sortedSquared import *

class Test(unittest.TestCase):
    def testGeneral(self):
        self.assertEqual(sortedSquares([-5, -2, 0, 1, 3, 4]), [0, 1, 4, 9, 16, 25])

if __name__ == '__main__':
   unittest.main()
