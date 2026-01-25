import pytest
from vacuum import *


class Test:
    def testGeneral(self):
        assert vacuum("")
        assert vacuum("LR")
        assert vacuum("RUULLDRD")
        assert not vacuum("URURD")
