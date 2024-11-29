import unittest
from longestConsecutive import *

class Test(unittest.TestCase):

    def testWithNone(self):
        self.assertEqual(longestConsecutive(None), 0)

    def testReturn1(self):
        nodeA = TreeNode(1)
        nodeB = TreeNode(3)
        nodeC = TreeNode(5)
        nodeD = TreeNode(6)

        nodeA.left = nodeB
        nodeA.right = nodeC
        nodeB.right = nodeD
        self.assertEqual(longestConsecutive(nodeA), 1)

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
        self.assertEqual(longestConsecutive(nodeA), 3)


if __name__ == '__main__':
   unittest.main()
