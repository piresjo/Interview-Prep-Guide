import pytest
from twoSum import *


class Test:

    def testWithNone(self):
        assert not findTarget(None, 7))

    def testSingle(self):
        nodeVal = TreeNode(5)
        assert not findTarget(nodeVal, 5))

    def testGeneral(self):
        nodeA = TreeNode(5)
        nodeB = TreeNode(3)
        nodeC = TreeNode(7)
        nodeD = TreeNode(2)
        nodeE = TreeNode(4)
        nodeF = TreeNode(6)
        nodeG = TreeNode(8)
        nodeH = TreeNode(1)

        nodeA.left = nodeB
        nodeA.right = nodeC
        nodeB.left = nodeD
        nodeB.right = nodeE
        nodeC.left = nodeF
        nodeC.right = nodeG
        nodeD.left = nodeH

        assert not findTarget(nodeA, 500))
        assert findTarget(nodeA, 10))
