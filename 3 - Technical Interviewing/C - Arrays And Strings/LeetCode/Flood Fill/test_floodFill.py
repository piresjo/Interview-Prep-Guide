import pytest
from floodFill import *


class Test:

    def testGeneral(self):
        assert floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == [
            [2, 2, 2],
            [2, 2, 0],
            [2, 0, 1],
        ]
        assert floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 0) == [[0, 0, 0], [0, 0, 0]]
