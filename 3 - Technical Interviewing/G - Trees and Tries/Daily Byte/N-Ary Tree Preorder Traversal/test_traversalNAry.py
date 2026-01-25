import pytest
from traversalNAry import *
from traversalIterativeNAry import *


class Test:

    def testBasic(self):
        headNode = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node6 = Node(6)
        node3.children = [node5, node6]
        headNode.children = [node3, node2, node4]

        assert preorder(headNode) == [1, 3, 5, 6, 2, 4]
        assert preorderIterative(headNode) == [1, 3, 5, 6, 2, 4]
