import pytest
from middle import *


class Test:

    def testEdgeCases(self):
        assert findMiddle(None) == None
        nodeA = ListNode(1)
        assert findMiddle(nodeA).value == nodeA.value

    def testGeneral(self):
        nodeA = ListNode(1)
        nodeB = ListNode(2)
        nodeC = ListNode(3)
        nodeA.next = nodeB
        nodeB.next = nodeC
        assert findMiddle(nodeA).value == nodeB.value

        nodeB.next = None
        assert findMiddle(nodeA).value == nodeA.value
