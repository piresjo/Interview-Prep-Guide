import pytest
from valid import *


class Test:
    def testGeneral(self):
        assert validPalindrome("abcba")
        assert validPalindrome("foobof")
        assert not validPalindrome("abccab")
