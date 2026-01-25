import pytest
from restore import *


class Test:

    def testWithNone(self):
        assert not restoreBinaryTree([], []))

    def testWithSingle(self):
        nodeVal = Tree(5)
        assert identicalTrees(nodeVal, restoreBinaryTree([5], [5])))

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

        preOrder = [5, 3, 2, 1, 4, 7, 6, 8]
        inOrder = [1, 2, 3, 4, 5, 6, 7, 8]
        assert identicalTrees(nodeA, restoreBinaryTree(inOrder, preOrder)))


def identicalTrees(a, b):

    # 1. Both empty
    if a is None and b is None:
        return True

    # 2. Both non-empty -> Compare them
    if a is not None and b is not None:
        return (
            (a.value == b.value)
            and identicalTrees(a.left, b.left)
            and identicalTrees(a.right, b.right)
        )

    # 3. one empty, one not -- false
    return False
