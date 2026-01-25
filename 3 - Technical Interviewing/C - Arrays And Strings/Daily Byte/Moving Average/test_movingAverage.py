import pytest
from movingAverage import *


class Test:

    def testGeneral(self):
        moving3 = MovingAverage(3)
        assert moving3.next(3) == 3
        assert moving3.next(5) == 4
        assert moving3.next(7) == 5
        assert moving3.next(6) == 6
