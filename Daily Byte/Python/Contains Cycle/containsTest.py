from typing import no_type_check
import unittest
from contains import *

class Test(unittest.TestCase):

    def testGeneral(self):
        nodeA = ListNode(1)
        nodeA.next = nodeA
        self.assertTrue(contains(nodeA))

        nodeB = ListNode(2)
        nodeC = ListNode(3)
        nodeA.next = nodeB
        nodeB.next = nodeC

        self.assertFalse(contains(nodeA))

        nodeC.next = nodeA
    
        self.assertTrue(nodeA)

if __name__ == '__main__':
   unittest.main()