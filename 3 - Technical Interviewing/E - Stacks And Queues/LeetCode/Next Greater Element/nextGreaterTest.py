import pytest
from nextGreater import *


class TestStringMethods:

    def testGeneral(self):
        assert nextGreaterElement([4, 1, 2], [1, 3, 4, 2]), [-1, 3, -1])
