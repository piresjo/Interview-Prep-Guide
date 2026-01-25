import pytest
from pathGivenSum import *


class Test:

    def testWithNoneObject(self):
        assert not hasPathWithGivenSum(None, 0)

    def testGeneralCase(self):
        node1 = Tree(1)
        node2 = Tree(2)
        node3 = Tree(3)
        node4 = Tree(4)
        node5 = Tree(5)

        node4.left = node2
        node2.left = node1
        node2.right = node3
        node4.right = node5

        assert not hasPathWithGivenSum(node4, 20)
        assert not hasPathWithGivenSum(node4, 10)
        assert hasPathWithGivenSum(node4, 9)
        assert hasPathWithGivenSum(node4, 7)
