import pytest
from listIntersection import *


class TestStringMethods:

    def testWithNoneObject(self):
        assert not isIntersection(None, None)

    def testSeparateLists(self):
        testNode = LinkedList(25, None)
        testNode2 = LinkedList(30, None)
        assert not isIntersection(testNode, testNode2)

    def testIntersectingLists(self):
        testNodeA = LinkedList(1, None)
        testNodeB = LinkedList(2, None)
        testNodeC = LinkedList(3, None)
        testNodeD = LinkedList(4, None)
        testNodeE = LinkedList(5, None)
        testNodeF = LinkedList(6, None)

        testNodeA.next = testNodeD
        testNodeB.next = testNodeC
        testNodeC.next = testNodeD
        testNodeD.next = testNodeE
        testNodeE.next = testNodeF

        assert testNodeF == getTail(testNodeA)
        assert testNodeF == getTail(testNodeB)
        assert 4 == getSize(testNodeA)
        assert 5 == getSize(testNodeB)
        assert 4 == isIntersection(testNodeA, testNodeB).data
