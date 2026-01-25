import pytest
from rotation import *


class Test:

    def testWithNone(self):
        assert not rotation(None, None)

    def testWithEmpty(self):
        assert not rotation("", "")

    def testGeneral(self):
        assert rotation("waterbottle", "erbottlewat")
        assert not rotation("waterbottle", "chungus")
