import pytest
from numIslands import *


class Test:
    def testEdgeCases(self):
        assert numIslands(None), 0)
        # assert numIslands([1]), 0)
        assert numIslands([]), 0)

    def testIslands(self):
        island1 = [["1", "1", "0"], ["1", "0", "1"], ["0", "1", "1"]]
        island2 = [["1", "0", "1"], ["1", "0", "0"], ["0", "1", "1"]]

        assert numIslands(island1), 2)
        assert numIslands(island2), 3)
