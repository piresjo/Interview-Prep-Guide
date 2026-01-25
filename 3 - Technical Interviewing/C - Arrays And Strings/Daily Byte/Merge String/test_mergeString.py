import pytest
from mergeString import *


class Test:

    def testGeneral(self):
        assert mergeString("abc", "def") == "adbecf"
        assert mergeString("abcd", "ef") == "aebfcd"
        assert mergeString("", "abc") == "abc"
        assert mergeString("abc", "") == "abc"
        assert mergeString("", "") == ""
