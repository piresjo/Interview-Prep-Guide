import unittest
from middle import *

class Test(unittest.TestCase):

    def testEdgeCases(self):
        self.assertEqual(findMiddle(None), None)
        nodeA = ListNode(1)
        self.assertEqual(findMiddle(nodeA).value, nodeA.value)

    def testGeneral(self):
        nodeA = ListNode(1)
        nodeB = ListNode(2)
        nodeC = ListNode(3)
        nodeA.next = nodeB
        nodeB.next = nodeC
        self.assertEqual(findMiddle(nodeA).value, nodeB.value)

        nodeB.next = None
        self.assertEqual(findMiddle(nodeA).value, nodeA.value)


    


   

if __name__ == '__main__':
   unittest.main()
