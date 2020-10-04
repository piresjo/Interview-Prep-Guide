import unittest
from maxDepth import *

class Test(unittest.TestCase):
    
    def testWithNone(self):
        self.assertEqual(maxDepth(None), 0)

    def testSingle(self):
        nodeVal = Node(5)
        self.assertEqual(maxDepth(nodeVal), 1)

    def testGeneral(self):
        nodeA = Node(5)
        nodeB = Node(3)
        nodeC = Node(7)
        nodeD = Node(2)
        nodeE = Node(4)
        nodeF = Node(6)
        nodeG = Node(8)
        nodeH = Node(1)
        nodeA.children = [nodeB, nodeC, nodeD, nodeE]
        nodeB.children = [nodeF, nodeG]
        nodeF.children = [nodeH]

        self.assertEqual(maxDepth(nodeA), 4)

        nodeF.children = []
        self.assertEqual(maxDepth(nodeA), 3)


      

if __name__ == '__main__':
   unittest.main()
