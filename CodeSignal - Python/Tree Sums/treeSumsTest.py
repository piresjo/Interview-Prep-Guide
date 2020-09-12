import unittest
from treeSums import *

class Test(unittest.TestCase):
    def testWithNone(self):
        self.assertEqual(digitTreeSum(None), 0)

    def testWithSingle(self):
        self.assertEqual(digitTreeSum(Tree(5)), 5)

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

        self.assertEqual(digitTreeSum(nodeA), 7009)
        

if __name__ == '__main__':
   unittest.main()