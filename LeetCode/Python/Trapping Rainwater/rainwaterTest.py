import unittest
from rainwater import *

class Test(unittest.TestCase):

    def testWithNone(self):
        self.assertEqual(trap(None), 0)

    def testWithEmptyList(self):
        self.assertEqual(trap([]), 0)

    def testWithSingleList(self):
        self.assertEqual(trap([2]), 0)

    def testWithDoubleList(self):
        self.assertEqual(trap([2, 1]), 0)

    def testNoWaterStored(self):
        self.assertEqual(trap([2, 2, 2, 2, 2, 2, 2, 2]), 0)

    def testWaterStored(self):
        self.assertEqual(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)


   

if __name__ == '__main__':
   unittest.main()