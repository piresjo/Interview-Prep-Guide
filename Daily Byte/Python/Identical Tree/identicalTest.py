from typing import no_type_check_decorator
import unittest	
from identical import *	

class TestStringMethods(unittest.TestCase):	

    def testReturnTrue(self):
        self.assertTrue(isTreeIdentical(None, None))

        nodeA = Tree(1)
        nodeB = Tree(1)
        self.assertTrue(isTreeIdentical(nodeA, nodeB))	

        nodeB = Tree(2)
        nodeC = Tree(3)
        nodeD = Tree(1)
        nodeE = Tree(2)
        nodeF = Tree(3)
        nodeA.right = nodeB
        nodeB.right = nodeC
        nodeD.right = nodeE
        nodeE.right = nodeF
        self.assertTrue(isTreeIdentical(nodeA, nodeD))	

    def testReturnFalse(self):	
        nodeA = Tree(1)
        self.assertFalse(isTreeIdentical(nodeA, None))	

        nodeB = Tree(2)
        nodeC = Tree(3)
        nodeD = Tree(1)
        nodeE = Tree(2)
        nodeF = Tree(3)
        nodeA.right = nodeB
        nodeB.right = nodeC
        nodeD.left = nodeE
        nodeE.left = nodeF
        self.assertFalse(isTreeIdentical(nodeA, nodeD))				


if __name__ == '__main__':	
   unittest.main()