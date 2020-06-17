import unittest
from checkBST import *

class TestStringMethods(unittest.TestCase):

    def testWithNoneObject(self):
    	self.assertTrue(isBST(None))

    def testWithSingleNode(self):
        head = BSTNode(25)
        self.assertTrue(isBST(head))

    def testHappyPath(self):
        node1 = BSTNode(1)
        node2 = BSTNode(2)
        node3 = BSTNode(3)
        node4 = BSTNode(4)
        node5 = BSTNode(5)
        node6 = BSTNode(6)
        node7 = BSTNode(7)

        node4.left = node2
        node4.right = node6
        node2.left = node1
        node2.right = node3
        node6.left = node5
        node6.right = node7

        self.assertTrue(isBST(node4))

    def testFalsePath(self):
        node1 = BSTNode(1)
        node2 = BSTNode(2)
        node3 = BSTNode(29)
        node4 = BSTNode(4)
        node5 = BSTNode(5)
        node6 = BSTNode(6)
        node7 = BSTNode(7)

        node4.left = node2
        node4.right = node6
        node2.left = node1
        node2.right = node3
        node6.left = node5
        node6.right = node7

        self.assertFalse(isBST(node4))
        
       
if __name__ == '__main__':
   unittest.main()