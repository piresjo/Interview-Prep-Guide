import pytest
from treeSums import *


class Test:
    def testWithNone(self):
        assert digitTreeSum(None) == 0

    def testWithSingle(self):
        assert digitTreeSum(Tree(5)) == 5

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

        assert digitTreeSum(nodeA) == 7009
