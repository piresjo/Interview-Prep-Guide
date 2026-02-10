import pytest
from majorityNumber import *


class Test:

    def testGeneral(self):
        assert majorityElement([3, 2, 3]) == 3
        assert majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
