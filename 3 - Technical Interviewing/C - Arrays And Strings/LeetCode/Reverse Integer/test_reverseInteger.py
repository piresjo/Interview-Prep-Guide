import pytest
from reverseInteger import *


class Test:

    def testGeneral(self):
        assert reverse(0) == 0
        assert reverse(-123) == -321
        assert reverse(23) == 32
        assert reverseMethod2(0) == 0
        assert reverseMethod2(-123) == -321
        assert reverseMethod2(23) == 32
