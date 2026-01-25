import pytest
from findMinRotatedSorted import *


class Test:
    def testBaseCases(self):
        assert findMin(None) == -1
        assert findMin([]) == -1
        assert findMin([1]) == 1

    def testGeneral(self):
        assert findMin([1, 2, 3, 4, 5]) == 1
        assert findMin([2, 3, 4, 5, 1]) == 1
        assert findMin([3, 4, 5, 1, 2]) == 1
        assert findMin([4, 5, 1, 2, 3]) == 1
