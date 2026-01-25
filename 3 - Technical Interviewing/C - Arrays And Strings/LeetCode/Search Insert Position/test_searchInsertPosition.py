import pytest
from searchInsertPosition import *


class Test:

    def testGeneral(self):
        assert searchInsert([1, 2, 3, 4, 5], 3) == 2
        assert searchInsert([1, 2, 3, 4], 5) == 4
