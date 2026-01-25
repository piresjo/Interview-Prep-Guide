import pytest
from reverseVowelsStack import *


class Test:
    def testGeneral(self):
        assert reverseVowels("") == ""
        assert reverseVowels("hello") == "holle"
        assert reverseVowels("1.1.1.1") == "1.1.1.1"
