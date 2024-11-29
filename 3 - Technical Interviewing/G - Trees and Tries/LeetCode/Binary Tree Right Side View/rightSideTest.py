import unittest
from rightSide import *

class Test(unittest.TestCase):

    def testWithNone(self):
        self.assertEqual(rightSideView(None), [])

    def testBalancedTree(self):
        nodeA = TreeNode(1)
        nodeB = TreeNode(2)
        nodeC = TreeNode(3)
        nodeD = TreeNode(4)
        nodeE = TreeNode(5)
        nodeF = TreeNode(6)
        nodeG = TreeNode(7)

        nodeA.left = nodeB
        nodeA.right = nodeC
        nodeB.left = nodeD
        nodeB.right = nodeE
        nodeC.left = nodeF
        nodeC.right = nodeG

        self.assertEqual(rightSideView(nodeA), [1, 3, 7])

    def testRightTree(self):
        nodeA = TreeNode(1)
        nodeB = TreeNode(2)
        nodeC = TreeNode(3)
        nodeD = TreeNode(4)
        nodeE = TreeNode(5)
        nodeF = TreeNode(6)
        nodeG = TreeNode(7)

        nodeA.right = nodeC
        nodeB.right = nodeE
        nodeC.left = nodeF
        nodeC.right = nodeG
        self.assertEqual(rightSideView(nodeA), [1, 3, 7])

    def testLeftTree(self):
        nodeA = TreeNode(1)
        nodeB = TreeNode(2)
        nodeC = TreeNode(3)
        nodeD = TreeNode(4)
        nodeE = TreeNode(5)
        nodeF = TreeNode(6)
        nodeG = TreeNode(7)

        nodeA.left = nodeB
        nodeB.left = nodeD
        self.assertEqual(rightSideView(nodeA), [1, 2, 4])

    def testMixedTree(self):
        nodeA = TreeNode(1)
        nodeB = TreeNode(2)
        nodeC = TreeNode(3)
        nodeD = TreeNode(4)
        nodeE = TreeNode(5)
        nodeF = TreeNode(6)
        nodeG = TreeNode(7)

        nodeA.right = nodeC
        nodeC.left = nodeF

        self.assertEqual(rightSideView(nodeA), [1, 3, 6])


if __name__ == '__main__':
   unittest.main()
