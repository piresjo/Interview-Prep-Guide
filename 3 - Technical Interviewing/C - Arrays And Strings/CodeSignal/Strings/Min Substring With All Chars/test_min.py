import pytest
from min import *


class Test:

    def testGeneral(self):
        assert minSubstringWithAllChars("adobecodebanc", "abc") == "banc"
        assert minSubstringWithAllChars("", "") == ""
        assert minSubstringWithAllChars("abc", "abc") == "abc"
        assert minSubstringWithAllChars("zqyvbfeiee", "ze") == "zqyvbfe"
