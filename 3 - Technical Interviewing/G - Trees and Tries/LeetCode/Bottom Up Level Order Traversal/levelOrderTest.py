import unittest
from levelOrder import *

class Test(unittest.TestCase):
    
    def testWithNone(self):
        self.assertEqual(levelOrderBottom(None), [])

    def testSingle(self):
        nodeVal = TreeNode(5)
        self.assertEqual(levelOrderBottom(nodeVal), [[5]])

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

        self.assertEqual(levelOrderBottom(nodeA), [[1], [2, 4, 6, 8], [3, 7], [5]])


if __name__ == '__main__':
   unittest.main()
