import unittest
from isSubtree import *

class Test(unittest.TestCase):

    def testWithNoneObject(self):
        self.assertFalse(isSubtree(None, None))

    def testHappyPath(self):
        node1 = Tree(1)
        node2 = Tree(2)
        node3 = Tree(3)
        node4 = Tree(4)
        node5 = Tree(5)

        node4.left = node2
        node2.left = node1
        node2.right = node3
        node4.right = node5

        self.assertTrue(isSubtree(node4, node2))

        
       
if __name__ == '__main__':
   unittest.main()