from typing import no_type_check_decorator
import pytest
from identicalTree import *


class TestStringMethods:

    def testReturnTrue(self):
        assert isTreeIdentical(None, None)

        nodeA = Tree(1)
        nodeB = Tree(1)
        assert isTreeIdentical(nodeA, nodeB)

        nodeB = Tree(2)
        nodeC = Tree(3)
        nodeD = Tree(1)
        nodeE = Tree(2)
        nodeF = Tree(3)
        nodeA.right = nodeB
        nodeB.right = nodeC
        nodeD.right = nodeE
        nodeE.right = nodeF
        assert isTreeIdentical(nodeA, nodeD)

    def testReturnFalse(self):
        nodeA = Tree(1)
        assert not isTreeIdentical(nodeA, None)

        nodeB = Tree(2)
        nodeC = Tree(3)
        nodeD = Tree(1)
        nodeE = Tree(2)
        nodeF = Tree(3)
        nodeA.right = nodeB
        nodeB.right = nodeC
        nodeD.left = nodeE
        nodeE.left = nodeF
        assert not isTreeIdentical(nodeA, nodeD)
