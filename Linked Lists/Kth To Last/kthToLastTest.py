import unittest
from kthToLast import *

class TestStringMethods(unittest.TestCase):

    def testWithNoneObject(self):
        self.assertIsNone(kthToLast(None, 5))

    def testKIsTooBig(self):
        testHead = LinkedList(20, None)
        self.assertIsNone(kthToLast(testHead, 3))

    def testHappyPath(self):
        testTail = LinkedList(20, None)
        testMiddleA = LinkedList(25, testTail)
        testMiddleB = LinkedList(30, testMiddleA)
        testHead = LinkedList(35, testMiddleB)
        self.assertEqual(20, kthToLast(testHead, 1).data)
        self.assertEqual(25, kthToLast(testHead, 2).data)
    
   
if __name__ == '__main__':
   unittest.main()