import unittest	
from convert import *	

class TestStringMethods(unittest.TestCase):		

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

        sortedList = convert(node4)	
        self.assertEqual(sortedList.data, 1)
        self.assertEqual(sortedList.next.data, 2)
        self.assertEqual(sortedList.next.next.data, 3)				


if __name__ == '__main__':	
   unittest.main()