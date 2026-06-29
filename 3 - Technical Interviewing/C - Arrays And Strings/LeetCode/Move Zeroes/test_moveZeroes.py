import pytest
from moveZeroes import *


class Test:

    def testImplementation(self):
        assert moveZeroes([1,8,6,2,5,4,8,3,7]) == [1,8,6,2,5,4,8,3,7]
        assert moveZeroes([0, 0]) == [0, 0]
        assert moveZeroes([1, 0, 3, 0, 5]) == [1, 3, 5, 0, 0]