import pytest
from defang import *


class Test:
    def testGeneral(self):
        assert defangIPaddr("") == ""
        assert defangIPaddr("hello") == "hello"
        assert defangIPaddr("1.1.1.1") == "1[.]1[.]1[.]1"
        assert defangIPaddr("121.121.121.121") == "121[.]121[.]121[.]121"
