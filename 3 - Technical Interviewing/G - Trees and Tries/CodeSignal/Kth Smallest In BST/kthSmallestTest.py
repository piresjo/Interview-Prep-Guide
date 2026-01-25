import pytest
from kthSmallest import *


class Test:

    def testWithNone(self):
        assert not kthSmallestInBST(None, 30))

    def testWithSingle(self):
        nodeVal = Tree(5)
        assert kthSmallestInBST(nodeVal, 1), 5)

    def testGeneral(self):
        nodeA = Tree(5)
        nodeB = Tree(3)
        nodeC = Tree(7)
        nodeD = Tree(2)
        nodeE = Tree(4)
        nodeF = Tree(6)
        nodeG = Tree(8)
        nodeH = Tree(1)

        nodeA.left = nodeB
        nodeA.right = nodeC
        nodeB.left = nodeD
        nodeB.right = nodeE
        nodeC.left = nodeF
        nodeC.right = nodeG
        nodeD.left = nodeH

        assert kthSmallestInBST(nodeA, 1), 1)
        assert kthSmallestInBST(nodeA, 2), 2)
        assert kthSmallestInBST(nodeA, 3), 3)
        assert kthSmallestInBST(nodeA, 4), 4)
        assert kthSmallestInBST(nodeA, 5), 5)
