import pytest
from product import *


class Test:
    def testGeneral(self):
        assert productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
