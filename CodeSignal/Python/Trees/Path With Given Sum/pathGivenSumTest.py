import unittest
from pathGivenSum import *

class Test(unittest.TestCase):

    def testWithNoneObject(self):
        self.assertFalse(hasPathWithGivenSum(None, 0))

    def testGeneralCase(self):
        node1 = Tree(1)
        node2 = Tree(2)
        node3 = Tree(3)
        node4 = Tree(4)
        node5 = Tree(5)

        node4.left = node2
        node2.left = node1
        node2.right = node3
        node4.right = node5

        self.assertFalse(hasPathWithGivenSum(node4, 20))
        self.assertFalse(hasPathWithGivenSum(node4, 10))
        self.assertTrue(hasPathWithGivenSum(node4, 9))
        self.assertTrue(hasPathWithGivenSum(node4, 7))

        
       
if __name__ == '__main__':
   unittest.main()