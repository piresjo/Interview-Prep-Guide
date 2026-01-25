import pytest
from traversals import *


class Test:

    def testLevelOrderWithNoneObject(self):
        assert not levelOrder(None))

    def testLevelOrderSingle(self):
        node = BSTNode(1)
        assert "1", levelOrder(node))

    def testLevelOrderGeneralCase(self):
        node1 = BSTNode(1)
        node2 = BSTNode(2)
        node3 = BSTNode(3)
        node4 = BSTNode(4)
        node5 = BSTNode(5)

        node4.left = node2
        node2.left = node1
        node2.right = node3
        node4.right = node5
        assert "4 2 5 1 3", levelOrder(node4))

    def testInOrderWithNoneObject(self):
        assert "", inOrder(None))

    def testInOrderSingle(self):
        node = BSTNode(1)
        assert "1", inOrder(node))

    def testInOrderGeneralCase(self):
        node1 = BSTNode(1)
        node2 = BSTNode(2)
        node3 = BSTNode(3)
        node4 = BSTNode(4)
        node5 = BSTNode(5)

        node4.left = node2
        node2.left = node1
        node2.right = node3
        node4.right = node5
        assert "1 2 3 4 5", inOrder(node4))

    def testPreOrderWithNoneObject(self):
        assert "", preOrder(None))

    def testPreOrderSingle(self):
        node = BSTNode(1)
        assert "1", preOrder(node))

    def testPreOrderGeneralCase(self):
        node1 = BSTNode(1)
        node2 = BSTNode(2)
        node3 = BSTNode(3)
        node4 = BSTNode(4)
        node5 = BSTNode(5)

        node4.left = node2
        node2.left = node1
        node2.right = node3
        node4.right = node5
        assert "1 2 3 5 4", preOrder(node4))

    def testPostOrderWithNoneObject(self):
        assert "", postOrder(None))

    def testPostOrderSingle(self):
        node = BSTNode(1)
        assert "1", postOrder(node))

    def testPostOrderGeneralCase(self):
        node1 = BSTNode(1)
        node2 = BSTNode(2)
        node3 = BSTNode(3)
        node4 = BSTNode(4)
        node5 = BSTNode(5)

        node4.left = node2
        node2.left = node1
        node2.right = node3
        node4.right = node5
        assert "4 1 2 3 5", postOrder(node4))
