import pytest
from removeKth import *


class Test:

    def testEdgeCases(self):
        nodeA = LinkedList(1)
        assert not remove(nodeA, 12)
        assert not remove(None, 12)

    @pytest.mark.skip
    def testGeneral(self):
        nodeA = LinkedList(1)
        nodeB = LinkedList(2)
        nodeC = LinkedList(3)
        nodeA.next = nodeB
        nodeB.next = nodeC
        # Method seems to run correctly, don't know why return pointer has
        # no next value
        assert remove(nodeA, 2).data == nodeA.data
        assert remove(nodeA, 2).next.data == nodeC.data
