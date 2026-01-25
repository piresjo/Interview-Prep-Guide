import pytest
from loopDetection import *


class TestStringMethods:

    def testWithNoneObject(self):
        assert not whereIsLoop(None)

    def testDouble(self):
        test = LinkedList(20, LinkedList(25, None))
        assert not whereIsLoop(test)

    def testSingle(self):
        testHead = LinkedList(20, None)
        assert not whereIsLoop(testHead)
