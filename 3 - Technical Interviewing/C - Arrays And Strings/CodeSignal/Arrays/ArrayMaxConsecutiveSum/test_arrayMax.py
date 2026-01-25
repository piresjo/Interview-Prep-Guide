import pytest
from arrayMax import *


class Test:
    def testGeneral(self):
        assert arrayMaxConsecutiveSum2([2, -1, 3, 5, -7]) == 9
        assert arrayMaxConsecutiveSum2([-2, 2, 5, -11, 6]) == 7
