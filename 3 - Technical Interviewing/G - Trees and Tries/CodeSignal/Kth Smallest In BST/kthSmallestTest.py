import unittest
from kthSmallest import *

class Test(unittest.TestCase):
    
    def testWithNone(self):
        self.assertIsNone(kthSmallestInBST(None, 30))

    def testWithSingle(self):
        nodeVal = Tree(5)
        self.assertEqual(kthSmallestInBST(nodeVal, 1), 5)

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

        self.assertEqual(kthSmallestInBST(nodeA, 1), 1)
        self.assertEqual(kthSmallestInBST(nodeA, 2), 2)
        self.assertEqual(kthSmallestInBST(nodeA, 3), 3)
        self.assertEqual(kthSmallestInBST(nodeA, 4), 4)
        self.assertEqual(kthSmallestInBST(nodeA, 5), 5)

if __name__ == '__main__':
   unittest.main()
