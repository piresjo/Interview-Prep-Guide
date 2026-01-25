import pytest
from url import *


class Test:

    def testWithNone(self):
        assert replaceSpaces(None) == None

    def testWithEmptyString(self):
        assert replaceSpaces("") == ""

    def testWithSingletonString(self):
        assert replaceSpaces("a") == "a"

    def testWithUncompressableString(self):
        assert replaceSpaces("Mr John Smith    ") == "Mr%20John%20Smith"
