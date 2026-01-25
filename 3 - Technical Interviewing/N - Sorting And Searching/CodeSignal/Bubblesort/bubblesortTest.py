import pytest
from bubblesort import *


class Test:

    def testWithNone(self):
        assert bubbleSort(None), None)

    def testWithEmpty(self):
        assert bubbleSort([]), [])

    def testWithOne(self):
        assert bubbleSort([1]), [1])

    def testGeneralCase(self):
        assert bubbleSort([9, 6, 8, 3, 1]), [1, 3, 6, 8, 9])
