import unittest
from listIntersection import *

class TestStringMethods(unittest.TestCase):

    def testWithNoneObject(self):
        self.assertIsNone(isIntersection(None, None))

    def testSeparateLists(self):
        testNode = LinkedList(25, None)
        testNode2 = LinkedList(30, None)
        self.assertIsNone(isIntersection(testNode, testNode2))

    def testIntersectingLists(self):
        testNodeA = LinkedList(1, None)
        testNodeB = LinkedList(2, None)
        testNodeC = LinkedList(3, None)
        testNodeD = LinkedList(4, None)
        testNodeE = LinkedList(5, None)
        testNodeF = LinkedList(6, None)

        testNodeA.next = testNodeD
        testNodeB.next = testNodeC
        testNodeC.next = testNodeD
        testNodeD.next = testNodeE
        testNodeE.next = testNodeF

        self.assertEqual(testNodeF, getTail(testNodeA))
        self.assertEqual(testNodeF, getTail(testNodeB))
        self.assertEqual(4, getSize(testNodeA))
        self.assertEqual(5, getSize(testNodeB))
        self.assertEqual(4, isIntersection(testNodeA, testNodeB).data)
    
   
if __name__ == '__main__':
   unittest.main()