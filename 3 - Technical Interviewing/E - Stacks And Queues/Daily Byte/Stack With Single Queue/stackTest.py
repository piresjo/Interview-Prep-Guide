import pytest
from stack import *


class Test:

    def testGeneral(self):
        stackVal = Stack()

        stackVal.push(3)
        assert stackVal.peek(), 3)

        stackVal.push(4)
        assert stackVal.peek(), 4)

        stackVal.push(5)
        assert stackVal.peek(), 5)

        assert stackVal.pop(), 5)
        assert stackVal.peek(), 4)
