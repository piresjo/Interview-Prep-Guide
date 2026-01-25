import pytest
from reverseVowels import *


class Test:

    def testGeneral(self):
        assert reverseVowels("Hello World") == "Hollo Werld"
        assert reverseVowels("asdf") == "asdf"
        assert reverseVowels("qwty") == "qwty"
        assert reverseVowels("AeIoU") == "UoIeA"
