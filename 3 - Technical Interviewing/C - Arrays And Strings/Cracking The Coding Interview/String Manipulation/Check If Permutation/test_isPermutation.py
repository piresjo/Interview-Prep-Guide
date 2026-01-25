import pytest
from isPermutation import *


class TestStringMethods:

    def testWithNoneString(self):
        testStringA = "testing"
        assert not isPerm(None, testStringA)

    def testReturnTrue(self):
        testStringA = "testing"
        testStringB = "gnitset"
        assert isPerm(testStringA, testStringB)

    def testReturnFalseDiffLen(self):
        testStringA = "testing"
        testStringB = "moo"
        assert not isPerm(testStringA, testStringB)

    def testReturnFalseIncorrectString(self):
        testStringA = "testing"
        testStringB = "kniters"
        assert not isPerm(testStringA, testStringB)

    def testPopulateDict(self):
        testString = "helloworld"
        testStringDict = populateDict(testString, {})
        assert testStringDict["h"] == 1
        assert testStringDict["e"] == 1
        assert testStringDict["l"] == 3
        assert testStringDict["o"] == 2
        assert testStringDict["r"] == 1
        assert testStringDict["d"] == 1
