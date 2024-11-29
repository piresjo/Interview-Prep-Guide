import unittest
from prefix import *

class Test(unittest.TestCase):    
    def testWithNone(self):
        self.assertEqual(longestCommonPrefix(None), "")    
        self.assertEqual(longestCommonPrefix([]), "") 

    def testGeneral(self):
        self.assertEqual(longestCommonPrefix(["hello"]), "hello") 
        self.assertEqual(longestCommonPrefix(["hello", "hell", "helo"]), "hel") 

if __name__ == '__main__':
   unittest.main()