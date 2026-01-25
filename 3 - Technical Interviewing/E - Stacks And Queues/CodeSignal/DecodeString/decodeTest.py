import pytest
from decode import *


class Test:

    def testWithEmpty(self):
        assert decodeString(""), "")

    def testGeneral(self):
        assert decodeString("asdf"), "asdf")
        assert decodeString("4[ab]"), "abababab")
        assert decodeString("3[a2[c]]"), "accaccacc")
