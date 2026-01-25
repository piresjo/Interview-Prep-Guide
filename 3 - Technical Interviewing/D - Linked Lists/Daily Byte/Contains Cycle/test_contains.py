from typing import no_type_check
import pytest
from contains import *


class Test:

    def testGeneral(self):
        nodeA = ListNode(1)
        nodeA.next = nodeA
        assert contains(nodeA)

        nodeB = ListNode(2)
        nodeC = ListNode(3)
        nodeA.next = nodeB
        nodeB.next = nodeC

        assert not contains(nodeA)

        nodeC.next = nodeA

        assert nodeA
