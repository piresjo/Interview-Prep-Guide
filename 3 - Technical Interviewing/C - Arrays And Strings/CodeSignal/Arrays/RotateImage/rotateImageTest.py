import unittest
from rotateImage import *

class Test(unittest.TestCase):

    def testWithNone(self):
        self.assertIsNone(rotateImage(None))

    def testWithEmptyList(self):
        self.assertIsNone(rotateImage([]))

    def testWithMalformedImage(self):
        self.assertIsNone(rotateImage([1, 2, 4]))

    def testWith2By2Image(self):
        originalImage = [[1, 2], [3, 4]]
        finalImage = [[3, 1], [2, 4]]
        self.assertEqual(rotateImage(originalImage), finalImage)

    def testWith3By3Image(self):
        originalImage = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        finalImage = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        self.assertEqual(rotateImage(originalImage), finalImage)



   

if __name__ == '__main__':
   unittest.main()
