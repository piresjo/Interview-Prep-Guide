import pytest
from subarrayProduct import *


class Test:
    def testGeneral(self):
        assert numSubarrayProductLessThanK([10, 5, 2, 6], 100) == 8
        assert numSubarrayProductLessThanK([10, 5, 2, 6], 1) == 0
        assert numSubarrayProductLessThanK([10, 5, 2, 6], 0) == 0
        assert numSubarrayProductLessThanK([1, 2, 3, 4], 1) == 0
        assert numSubarrayProductLessThanK([1, 2, 3, 4], 2) == 1
        assert numSubarrayProductLessThanK([1, 2, 3, 4], 3) == 3
