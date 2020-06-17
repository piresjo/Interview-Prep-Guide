import unittest
from minTree import *

class TestStringMethods(unittest.TestCase):

    def testWithNoneObject(self):
    	self.assertIsNone(minTree(None))

    def testWithEmpty(self):
    	self.assertIsNone(minTree([]))

    def testWithSingle(self):
        headVal = BSTNode(25)
        self.assertEqual(headVal.data, minTree([25]).data)

    def testWithDouble(self):
        headVal = BSTNode(25)
        rightVal = BSTNode(30)
        headVal.right = rightVal

        self.assertEqual(headVal.data, minTree([25, 30]).data)
        self.assertEqual(rightVal.data, minTree([25, 30]).right.data)
        
       
if __name__ == '__main__':
   unittest.main()