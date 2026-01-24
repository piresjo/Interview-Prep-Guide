import unittest
from palindrome import *

class Test(unittest.TestCase):

    def testGeneral(self):
        self.assertTrue(isPalindrome(10101))
        self.assertTrue(isPalindrome(1))
        self.assertFalse(isPalindrome(1010))
        self.assertFalse(isPalindrome(-10101))
        


if __name__ == '__main__':
   unittest.main()