import pytest
from oneAway import *


class TestStringMethods:

    def testWithNoneString(self):
        assert not oneAwayOrLess(None, None)

    def testTrueSameString(self):
        testString = "test"
        assert oneAwayOrLess(testString, testString)

    def testFalseLengthDifferenceTooGreat(self):
        testStringA = "asdfg"
        testStringB = "asd"
        assert not oneAwayOrLess(testStringA, testStringB)

    def testTrueDifferingLengths(self):
        testStringA = "asdfg"
        testStringB = "asdf"
        assert oneAwayOrLess(testStringA, testStringB)
        assert oneAwayOrLess(testStringB, testStringA)

    def testTrueChangeLetter(self):
        testStringA = "asdf"
        testStringB = "awdf"
        assert oneAwayOrLess(testStringA, testStringB)
        assert oneAwayOrLess(testStringB, testStringA)

    def testPopulateDict(self):
        testString = "helloworld"
        testStringDict = populateDict(testString, {})
        assert testStringDict["h"] == 1
        assert testStringDict["e"] == 1
        assert testStringDict["l"] == 3
        assert testStringDict["o"] == 2
        assert testStringDict["r"] == 1
        assert testStringDict["d"] == 1
