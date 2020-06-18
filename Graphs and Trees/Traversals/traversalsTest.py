import unittest
from traversals import *

class Test(unittest.TestCase):

    def testLevelOrderWithNoneObject(self):
        self.assertIsNone(levelOrder(None))
    
    def testLevelOrderSingle(self):
        node = BSTNode(1)
        self.assertEqual("1", levelOrder(node))
        

    def testLevelOrderGeneralCase(self):
        node1 = BSTNode(1)
        node2 = BSTNode(2)
        node3 = BSTNode(3)
        node4 = BSTNode(4)
        node5 = BSTNode(5)

        node4.left = node2
        node2.left = node1
        node2.right = node3
        node4.right = node5
        self.assertEqual("4 2 5 1 3", levelOrder(node4))

        
       
if __name__ == '__main__':
   unittest.main()