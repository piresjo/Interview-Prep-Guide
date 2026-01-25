import pytest
from rainwater import *


class Test:

    def testWithNone(self):
        assert trap(None) == 0

    def testWithEmptyList(self):
        assert trap([]) == 0

    def testWithSingleList(self):
        assert trap([2]) == 0

    def testWithDoubleList(self):
        assert trap([2, 1]) == 0

    def testNoWaterStored(self):
        assert trap([2, 2, 2, 2, 2, 2, 2, 2]) == 0

    def testWaterStored(self):
        assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
