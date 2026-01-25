import pytest
from threeStep import *


class Test:

    def testWithBaseCases(self):
        assert stairs(0), 1)
        assert stairs(1), 1)
        assert stairs(2), 2)

    def testGeneral(self):
        assert stairs(3), 4)
        assert stairs(4), 7)
        assert stairs(5), 13)
