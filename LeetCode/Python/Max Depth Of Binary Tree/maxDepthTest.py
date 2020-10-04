import unittest
from maxDepth import *

class Test(unittest.TestCase):
    
    def testWithNone(self):
        self.assertEqual(maxDepth(None), 0)

    def testSingle(self):
        nodeVal = TreeNode(5)
        self.assertEqual(maxDepth(nodeVal), 1)

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

        self.assertEqual(maxDepth(nodeA), 4)

        nodeD.left = None
        self.assertEqual(maxDepth(nodeA), 3)


      

if __name__ == '__main__':
   unittest.main()
