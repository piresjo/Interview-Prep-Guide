import pytest
from kthToLast import *


class TestStringMethods:

    def testWithNoneObject(self):
        assert not kthToLast(None, 5)

    def testKIsTooBig(self):
        testHead = LinkedList(20, None)
        assert not kthToLast(testHead, 3)

    def testHappyPath(self):
        testTail = LinkedList(20, None)
        testMiddleA = LinkedList(25, testTail)
        testMiddleB = LinkedList(30, testMiddleA)
        testHead = LinkedList(35, testMiddleB)
        assert 20 == kthToLast(testHead, 1).data
        assert 25 == kthToLast(testHead, 2).data
