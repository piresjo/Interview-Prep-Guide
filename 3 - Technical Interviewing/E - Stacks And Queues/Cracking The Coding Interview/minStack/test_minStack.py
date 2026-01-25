import pytest
from minStack import *


class Test:

    def testGeneral(self):
        stackVal = MinStack()

        stackVal.push(5)
        assert stackVal.stack == [5]
        assert stackVal.min() == 5

        stackVal.push(6)
        assert stackVal.stack == [5, 6]
        assert stackVal.min() == 5

        stackVal.push(3)
        assert stackVal.stack == [5, 6, 3]
        assert stackVal.min() == 3

        stackVal.push(7)
        assert stackVal.stack == [5, 6, 3, 7]
        assert stackVal.min() == 3

        stackVal.pop()
        assert stackVal.stack == [5, 6, 3]
        assert stackVal.min() == 3

        stackVal.pop()
        assert stackVal.stack == [5, 6]
        assert stackVal.min() == 5
