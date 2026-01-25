import pytest
from removeKFromList import *


class Test:

    def testWithNone(self):
        assert removeKFromList(None, -1000), None)

    def testKNotFound(self):
        nodeA = ListNode(1)
        nodeB = ListNode(2)
        nodeC = ListNode(3)
        nodeA.next = nodeB
        nodeB.next = nodeC
        reducedList = removeKFromList(nodeA, -1000)
        assert removeKFromList(nodeA, -1000), nodeA)
        assert reducedList.value, 1)
        assert reducedList.next.value, 2)
        assert reducedList.next.next.value, 3)

    def testKFound(self):
        nodeA = ListNode(1)
        nodeB = ListNode(2)
        nodeC = ListNode(3)
        nodeA.next = nodeB
        nodeB.next = nodeC
        reducedList = removeKFromList(nodeA, 2)
        assert reducedList.value, 1)
        assert reducedList.next.value, 3)
        assert not reducedList.next.next)
