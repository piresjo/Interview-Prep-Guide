import unittest	
from find import *	

class TestStringMethods(unittest.TestCase):	
	
    def testGeneral(self):	
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

        self.assertEqual(find(None, None), None)
        self.assertEqual(find(node1, None), None)
        self.assertEqual(find(node4, 7), node7)	
        self.assertEqual(find(node4, 1), node1)	
        self.assertEqual(find(node4, 4), node4)	
        self.assertEqual(find(node4, 17), None)	


if __name__ == '__main__':	
   unittest.main()