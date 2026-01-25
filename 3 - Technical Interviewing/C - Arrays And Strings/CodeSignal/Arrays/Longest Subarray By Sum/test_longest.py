import pytest
from longest import *


class Test:
    def testGeneral(self):
        assert findLongestSubarrayBySum(15, []) == [-1]
        assert findLongestSubarrayBySum(15, [1, 2, 3, 4]) == [-1]
        assert findLongestSubarrayBySum(15, [1, 2, 3, 4, 5]) == [1, 5]
        assert findLongestSubarrayBySum(15, [5, 5, 5, 1, 2, 3, 4]) == [3, 7]
