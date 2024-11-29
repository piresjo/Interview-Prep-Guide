import unittest
from valid import *

class Test(unittest.TestCase):       
    def testGeneral(self):
        self.assertTrue(validPalindrome("abcba"))
        self.assertTrue(validPalindrome("foobof"))
        self.assertFalse(validPalindrome("abccab"))

if __name__ == '__main__':
   unittest.main()