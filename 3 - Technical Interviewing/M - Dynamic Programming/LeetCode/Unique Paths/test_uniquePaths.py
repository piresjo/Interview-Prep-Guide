import pytest
from uniquePaths import *


class Test:

    def testWithBaseCases(self):
        assert uniquePaths(0, 0) == 0
        assert uniquePaths(1, 1) == 1

    def testGeneral(self):
        assert uniquePaths(3, 2) == 3
        assert uniquePaths(7, 3) == 28
