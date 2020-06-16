import unittest
from permOfPalindrome import *

class TestStringMethods(unittest.TestCase):

    def testWithNoneString(self):
        self.assertFalse(permOfPalindrome(None))

    def testReturnTruePalindrome(self):
        testString = "asdfgfdsa"
        self.assertTrue(permOfPalindrome(testString))

    def testReturnTruePermutationOfPalindrome(self):
        testString = "abab"
        self.assertTrue(permOfPalindrome(testString))

    def testReturnFalse(self):
        testString = "testing"
        self.assertFalse(permOfPalindrome(testString))

    def testPopulateDict(self):
        testString = "helloworld"
        testStringDict = populateDict(testString, {})
        self.assertEqual(testStringDict['h'], 1)
        self.assertEqual(testStringDict['e'], 1)
        self.assertEqual(testStringDict['l'], 3)
        self.assertEqual(testStringDict['o'], 2)
        self.assertEqual(testStringDict['r'], 1)
        self.assertEqual(testStringDict['d'], 1)

if __name__ == '__main__':
   unittest.main()