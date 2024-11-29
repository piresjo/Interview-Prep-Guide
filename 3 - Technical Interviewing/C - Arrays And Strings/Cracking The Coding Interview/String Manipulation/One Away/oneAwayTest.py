import unittest
from oneAway import *

class TestStringMethods(unittest.TestCase):

    def testWithNoneString(self):
        self.assertFalse(oneAwayOrLess(None, None))

    def testTrueSameString(self):
        testString = "test"
        self.assertTrue(oneAwayOrLess(testString, testString))

    def testFalseLengthDifferenceTooGreat(self):
        testStringA = "asdfg"
        testStringB = "asd"
        self.assertFalse(oneAwayOrLess(testStringA, testStringB))

    def testTrueDifferingLengths(self):
        testStringA = "asdfg"
        testStringB = "asdf"
        self.assertTrue(oneAwayOrLess(testStringA, testStringB))
        self.assertTrue(oneAwayOrLess(testStringB, testStringA))

    def testTrueChangeLetter(self):
        testStringA = "asdf"
        testStringB = "awdf"
        self.assertTrue(oneAwayOrLess(testStringA, testStringB))
        self.assertTrue(oneAwayOrLess(testStringB, testStringA))

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