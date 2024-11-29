import unittest
from uniqueStrings import *

# TODO - Run Tests To Show Memory And Time Differences

class TestStringMethods(unittest.TestCase):

    def testWithNoneString(self):
        self.assertFalse(allUniqueChars(None))
        self.assertFalse(allUniqueCharsNoMemory(None))

    def testAllUnique(self):
        testString = "asdfgh"
        self.assertTrue(allUniqueChars(testString))
        self.assertTrue(allUniqueCharsNoMemory(testString))

    def testNotAllUnique(self):
        testString = "aaaa"
        self.assertFalse(allUniqueChars(testString))
        self.assertFalse(allUniqueCharsNoMemory(testString))



if __name__ == '__main__':
   unittest.main()