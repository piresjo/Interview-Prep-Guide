import unittest
from movingAverage import *

class Test(unittest.TestCase):

    def testGeneral(self):
        moving3 = MovingAverage(3)
        self.assertEqual(moving3.next(3), 3)
        self.assertEqual(moving3.next(5), 4)
        self.assertEqual(moving3.next(7), 5)
        self.assertEqual(moving3.next(6), 6)

if __name__ == '__main__':
   unittest.main()
