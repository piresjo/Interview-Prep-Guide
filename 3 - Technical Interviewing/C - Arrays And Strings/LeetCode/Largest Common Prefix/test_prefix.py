import pytest
from prefix import *


class Test:
    def testWithNone(self):
        assert longestCommonPrefix(None) == ""
        assert longestCommonPrefix([]) == ""

    def testGeneral(self):
        assert longestCommonPrefix(["hello"]) == "hello"
        assert longestCommonPrefix(["hello", "hell", "helo"]) == "hel"
