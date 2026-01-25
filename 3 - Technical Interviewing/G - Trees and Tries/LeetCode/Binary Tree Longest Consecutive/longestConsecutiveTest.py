import pytest
from longestConsecutive import *


class Test:

    def testWithNone(self):
        assert longestConsecutive(None), 0)

    def testReturn1(self):
        nodeA = TreeNode(1)
        nodeB = TreeNode(3)
        nodeC = TreeNode(5)
        nodeD = TreeNode(6)

        nodeA.left = nodeB
        nodeA.right = nodeC
        nodeB.right = nodeD
        assert longestConsecutive(nodeA), 1)

    def testGeneral(self):
        nodeA = TreeNode(1)
        nodeB = TreeNode(2)
        nodeC = TreeNode(3)
        nodeD = TreeNode(4)
        nodeE = TreeNode(5)

        nodeA.left = nodeB
        nodeA.right = nodeC
        nodeC.left = nodeD
        nodeD.right = nodeE
        assert longestConsecutive(nodeA), 3)
