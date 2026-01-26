import pytest
from plusOne import *


class Test:

    def testGeneral(self):
        assert plusOne([0]) == [1]
        assert plusOne([9]) == [1, 0]
        assert plusOne([2, 0]) == [2, 1]
        assert plusOne([2, 9]) == [3, 0]
        assert plusOne([9, 9]) == [1, 0, 0]
