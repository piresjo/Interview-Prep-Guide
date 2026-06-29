import pytest
from mergeSorted import *


class Test:

    def testImplementation(self):
        assert mergeSorted([1,2,3,0,0,0], 3, [2,5,6], 3) == [1,2,2,3,5,6]
        assert mergeSorted([0, 0, 0, 0], 2, [0,0], 2) == [0, 0, 0, 0]
