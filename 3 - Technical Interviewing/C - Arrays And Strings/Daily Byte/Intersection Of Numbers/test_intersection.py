import pytest
from intersection import *


class Test:
    def testGeneral(self):
        assert intersection([2, 4, 4, 2], [2, 4]) == [2, 4]
        assert intersection([1, 2, 3, 3], [3, 3]) == [3]
        assert intersection([2, 4, 6, 8], [1, 3, 5, 7]) == []
