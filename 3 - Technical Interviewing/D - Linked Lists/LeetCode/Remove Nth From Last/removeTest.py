import unittest
from remove import *

class Test(unittest.TestCase):

    def testEdgeCases(self):
        nodeA = ListNode(1)
        self.assertIsNone(removeNthFromEnd(None, 12))

        modNodeA = removeNthFromEnd(nodeA, 12)
        self.assertEqual(modNodeA.val, 1)
        self.assertIsNone(modNodeA.next)
        

    def testGeneral(self):
        nodeA = ListNode(1)
        nodeB = ListNode(2)
        nodeC = ListNode(3)
        nodeA.next = nodeB
        nodeB.next = nodeC

        modNodeA = removeNthFromEnd(nodeA, 12)
        self.assertEqual(modNodeA.val, 1)
        self.assertEqual(modNodeA.next.val, 2)
        self.assertEqual(modNodeA.next.next.val, 3)

        modNodeA = removeNthFromEnd(nodeA, 2)
        self.assertEqual(modNodeA.val, 1)
        self.assertEqual(modNodeA.next.val, 3)
        self.assertIsNone(modNodeA.next.next)


    


   

if __name__ == '__main__':
   unittest.main()
