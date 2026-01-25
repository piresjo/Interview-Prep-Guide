import pytest
from reorg import *


class Test:

    def testGeneral(self):
        assert reorganizeString("aab"), "aba")
