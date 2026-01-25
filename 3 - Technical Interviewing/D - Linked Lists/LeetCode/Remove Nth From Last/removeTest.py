import pytest
from remove import *


class Test:

    def testEdgeCases(self):
        nodeA = ListNode(1)
        assert not removeNthFromEnd(None, 12))

        modNodeA = removeNthFromEnd(nodeA, 12)
        assert modNodeA.val, 1)
        assert not modNodeA.next)

    def testGeneral(self):
        nodeA = ListNode(1)
        nodeB = ListNode(2)
        nodeC = ListNode(3)
        nodeA.next = nodeB
        nodeB.next = nodeC

        modNodeA = removeNthFromEnd(nodeA, 12)
        assert modNodeA.val, 1)
        assert modNodeA.next.val, 2)
        assert modNodeA.next.next.val, 3)

        modNodeA = removeNthFromEnd(nodeA, 2)
        assert modNodeA.val, 1)
        assert modNodeA.next.val, 3)
        assert not modNodeA.next.next)
