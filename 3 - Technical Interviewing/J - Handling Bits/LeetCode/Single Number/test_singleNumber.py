import pytest
from singleNumber import *


class Test:
    def test(self):
        assert singleNumber([1, 2, 2, 3, 4, 1, 3]) == 4
        assert singleNumber([1]) == 1
        assert singleNumber([1, 2, 2, 3, 4, 1, 3, 4]) == 0
