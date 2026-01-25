import pytest
from maxDepthNAry import *


class Test:

    def testWithNone(self):
        assert maxDepth(None) == 0

    def testSingle(self):
        nodeVal = Node(5)
        assert maxDepth(nodeVal) == 1

    def testGeneral(self):
        nodeA = Node(5)
        nodeB = Node(3)
        nodeC = Node(7)
        nodeD = Node(2)
        nodeE = Node(4)
        nodeF = Node(6)
        nodeG = Node(8)
        nodeH = Node(1)
        nodeA.children = [nodeB, nodeC, nodeD, nodeE]
        nodeB.children = [nodeF, nodeG]
        nodeF.children = [nodeH]

        assert maxDepth(nodeA) == 4

        nodeF.children = []
        assert maxDepth(nodeA) == 3
