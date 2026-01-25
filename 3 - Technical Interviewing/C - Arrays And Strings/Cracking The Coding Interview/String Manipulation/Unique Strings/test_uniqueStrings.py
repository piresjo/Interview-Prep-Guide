import pytest
from uniqueStrings import *

# TODO - Run Tests To Show Memory And Time Differences


class TestStringMethods:

    def testWithNoneString(self):
        assert not allUniqueChars(None)
        assert not allUniqueCharsNoMemory(None)

    def testAllUnique(self):
        testString = "asdfgh"
        assert allUniqueChars(testString)
        assert allUniqueCharsNoMemory(testString)

    def testNotAllUnique(self):
        testString = "aaaa"
        assert not allUniqueChars(testString)
        assert not allUniqueCharsNoMemory(testString)
