import unittest
from removeKFromList import *

class Test(unittest.TestCase):

    def testWithNone(self):
        self.assertEqual(removeKFromList(None, -1000), None)

    def testKNotFound(self):
        nodeA = ListNode(1)
        nodeB = ListNode(2)
        nodeC = ListNode(3)
        nodeA.next = nodeB
        nodeB.next = nodeC
        reducedList = removeKFromList(nodeA, -1000)
        self.assertEqual(removeKFromList(nodeA, -1000), nodeA)
        self.assertEqual(reducedList.value, 1)
        self.assertEqual(reducedList.next.value, 2)
        self.assertEqual(reducedList.next.next.value, 3)

    def testKFound(self):
        nodeA = ListNode(1)
        nodeB = ListNode(2)
        nodeC = ListNode(3)
        nodeA.next = nodeB
        nodeB.next = nodeC
        reducedList = removeKFromList(nodeA, 2)
        self.assertEqual(reducedList.value, 1)
        self.assertEqual(reducedList.next.value, 3)
        self.assertIsNone(reducedList.next.next)


   

if __name__ == '__main__':
   unittest.main()
