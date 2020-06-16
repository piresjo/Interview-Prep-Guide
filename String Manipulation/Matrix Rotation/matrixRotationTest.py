import unittest
from matrixRotation import *

class TestStringMethods(unittest.TestCase):

    def testWithNoneObject(self):
        self.assertIsNone(rotateMatrix(None))

    def testWithMisshapenList(self):
        misshapen = [ [],
                      [],
                      [] ]
        rotateMatrix(misshapen)
        self.assertIsNone(rotateMatrix([[], [], []]))

    def testWithEmptyList(self):
        self.assertIsNone(rotateMatrix([]))

    def testOneByOne(self):
        testMatrix = [ [1] ]
        self.assertEqual(testMatrix, rotateMatrix(testMatrix))

    def testTwoByTwo(self):
        testMatrix0 = [ [1, 2],
                       [3, 4] ]
        testMatrix90 = [ [3, 1],
                         [4, 2] ]
        testMatrix180 = [ [4, 3],
                          [2, 1] ]
        testMatrix270 = [ [2, 4],
                          [1, 3] ]

        testMatrix = [ [1, 2],
                       [3, 4] ] 
        self.assertEqual(testMatrix90, rotateMatrix(testMatrix))
        self.assertEqual(testMatrix180, rotateMatrix(testMatrix))
        self.assertEqual(testMatrix270, rotateMatrix(testMatrix))
        self.assertEqual(testMatrix0, rotateMatrix(testMatrix))
   
if __name__ == '__main__':
   unittest.main()