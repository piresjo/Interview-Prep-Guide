import pytest
from listOfDepths import *


class Test:

    def testWithNone(self):
        assert listOfDepths(None), [])

    def testSingle(self):
        nodeVal = TreeNode(5)
        assert listOfDepths(nodeVal), [[5]])

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

        assert listOfDepths(nodeA), [[5], [3, 7], [2, 4, 6, 8], [1]])
