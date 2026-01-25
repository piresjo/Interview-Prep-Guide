import pytest
from permOfPalindrome import *


class TestStringMethods:

    def testWithNoneString(self):
        assert not permOfPalindrome(None)

    def testReturnTruePalindrome(self):
        testString = "asdfgfdsa"
        assert permOfPalindrome(testString)

    def testReturnTruePermutationOfPalindrome(self):
        testString = "abab"
        assert permOfPalindrome(testString)

    def testReturnFalse(self):
        testString = "testing"
        assert not permOfPalindrome(testString)

    def testPopulateDict(self):
        testString = "helloworld"
        testStringDict = populateDict(testString, {})
        assert testStringDict["h"] == 1
        assert testStringDict["e"] == 1
        assert testStringDict["l"] == 3
        assert testStringDict["o"] == 2
        assert testStringDict["r"] == 1
        assert testStringDict["d"] == 1
