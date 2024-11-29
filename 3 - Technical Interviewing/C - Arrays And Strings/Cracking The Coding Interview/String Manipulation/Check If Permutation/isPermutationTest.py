import unittest
from isPermutation import *

class TestStringMethods(unittest.TestCase):

    def testWithNoneString(self):
        testStringA = "testing"
        self.assertFalse(isPerm(None, testStringA))

    def testReturnTrue(self):
        testStringA = "testing"
        testStringB = "gnitset"
        self.assertTrue(isPerm(testStringA, testStringB))

    def testReturnFalseDiffLen(self):
        testStringA = "testing"
        testStringB = "moo"
        self.assertFalse(isPerm(testStringA, testStringB))

    def testReturnFalseIncorrectString(self):
        testStringA = "testing"
        testStringB = "kniters"
        self.assertFalse(isPerm(testStringA, testStringB))

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