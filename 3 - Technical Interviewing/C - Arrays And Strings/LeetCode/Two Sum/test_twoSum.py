import pytest
from twoSum import *


class Test:

    def testEdgeCases(self):
        assert twoSum(None, None) == []
        assert twoSum(None, 20) == []
        assert twoSum([2, 3, 4, 5, 6], None) == []
        assert twoSum([2], 2) == []

    def testGeneral(self):
        assert twoSum([1, 2, 3, 4, 5, 6], 10) == [3, 5]
        assert twoSum([1, 5, 6, 7, 8], 29) == []
