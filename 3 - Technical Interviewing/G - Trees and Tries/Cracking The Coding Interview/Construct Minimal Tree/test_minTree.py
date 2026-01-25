import pytest
from minTree import *


class TestStringMethods:

    def testWithNoneObject(self):
        assert not minTree(None)

    def testWithEmpty(self):
        assert not minTree([])

    def testWithSingle(self):
        headVal = BSTNode(25)
        assert headVal.data == minTree([25]).data

    def testWithDouble(self):
        headVal = BSTNode(25)
        rightVal = BSTNode(30)
        headVal.right = rightVal

        assert headVal.data == minTree([25, 30]).data
        assert rightVal.data == minTree([25, 30]).right.data
