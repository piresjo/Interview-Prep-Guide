import unittest
from url import *

class Test(unittest.TestCase):

    def testWithNone(self):
        self.assertEqual(replaceSpaces(None), None)   

    def testWithEmptyString(self):
        self.assertEqual(replaceSpaces(""), "")    

    def testWithSingletonString(self):
        self.assertEqual(replaceSpaces("a"), "a")  

    def testWithUncompressableString(self):
        self.assertEqual(replaceSpaces("Mr John Smith    "), "Mr%20John%20Smith")  

if __name__ == '__main__':
   unittest.main()
