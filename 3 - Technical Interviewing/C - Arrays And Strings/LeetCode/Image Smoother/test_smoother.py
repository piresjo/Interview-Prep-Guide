import pytest
from smoother import *


class Test:

    def testGeneral(self):
        assert imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        assert imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]]) == [
            [137, 141, 137],
            [141, 138, 141],
            [137, 141, 137],
        ]
        assert imageSmoother([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
        ]
