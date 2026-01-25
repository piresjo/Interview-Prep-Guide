import pytest
from deleteMid import *


class TestStringMethods:

    def testWithNoneObject(self):
        assert not deleteMid(None)

    def testWithSingleton(self):
        testNode = LinkedList(25, None)
        assert not deleteMid(testNode)

    def testWithSizeTwoList(self):
        testTail = LinkedList(25, None)
        testHead = LinkedList(12, testTail)
        assert 12 == deleteMid(testHead)

    def testWithMultiList(self):
        testTail = LinkedList(25, None)
        testMiddle = LinkedList(20, testTail)
        testHead = LinkedList(12, testMiddle)
        assert 20 == deleteMid(testMiddle)
