import unittest
from remove import *

class Test(unittest.TestCase):

    def testEdgeCases(self):
        nodeA = LinkedList(1)
        self.assertIsNone(remove(nodeA, 12))
        self.assertIsNone(remove(None, 12))
        

    def testGeneral(self):
        nodeA = LinkedList(1)
        nodeB = LinkedList(2)
        nodeC = LinkedList(3)
        nodeA.next = nodeB
        nodeB.next = nodeC
        # Method seems to run correctly, don't know why return pointer has
        # no next value
        self.assertEqual(remove(nodeA, 2).data, nodeA.data)
        self.assertEqual(remove(nodeA, 2).next.data, nodeC.data)


        


    


   

if __name__ == '__main__':
   unittest.main()
