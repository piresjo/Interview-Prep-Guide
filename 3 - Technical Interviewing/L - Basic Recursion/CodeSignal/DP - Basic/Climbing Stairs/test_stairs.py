import pytest
from stairs import *


class Test:

    def testWithBaseCases(self):
        assert stairs(0) == 1
        assert stairs(1) == 1

    def testGeneral(self):
        assert stairs(2) == 2
        assert stairs(3) == 3
        assert stairs(38) == 63245986
