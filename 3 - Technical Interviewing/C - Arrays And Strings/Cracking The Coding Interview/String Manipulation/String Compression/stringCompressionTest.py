import unittest
from stringCompression import *

class Test(unittest.TestCase):

    def testWithNone(self):
        self.assertEqual(compress(None), None)   

    def testWithEmptyString(self):
        self.assertEqual(compress(""), "")  

    def testWithSingletonString(self):
        self.assertEqual(compress("a"), "a") 

    def testWithUncompressableString(self):
        self.assertEqual(compress("asdfghjkl"), "asdfghjkl") 

    def testCompress(self):
        self.assertEqual(compress("aaasssddddff"), "a3s3d4f2") 

if __name__ == '__main__':
   unittest.main()
