import pytest
from maxDepthBinary import *


class Test:

    def testWithNone(self):
        assert maxDepth(None) == 0

    def testSingle(self):
        nodeVal = TreeNode(5)
        assert maxDepth(nodeVal) == 1

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

        assert maxDepth(nodeA) == 4

        nodeD.left = None
        assert maxDepth(nodeA) == 3
