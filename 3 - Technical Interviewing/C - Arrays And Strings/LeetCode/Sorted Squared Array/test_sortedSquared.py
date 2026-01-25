import pytest
from sortedSquared import *


class Test:
    def testGeneral(self):
        assert sortedSquares([-5, -2, 0, 1, 3, 4]) == [0, 1, 4, 9, 16, 25]
