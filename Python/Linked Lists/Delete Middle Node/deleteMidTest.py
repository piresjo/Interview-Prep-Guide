import unittest
from deleteMid import *

class TestStringMethods(unittest.TestCase):

    def testWithNoneObject(self):
        self.assertFalse(deleteMid(None))

    def testWithSingleton(self):
        testNode = LinkedList(25, None)
        self.assertFalse(deleteMid(testNode))

    def testWithSizeTwoList(self):
        testTail = LinkedList(25, None)
        testHead = LinkedList(12, testTail)
        self.assertEqual(12, deleteMid(testHead))

    def testWithMultiList(self):
        testTail = LinkedList(25, None)
        testMiddle = LinkedList(20, testTail)
        testHead = LinkedList(12, testMiddle)
        self.assertEqual(20, deleteMid(testMiddle))

    

        

       
if __name__ == '__main__':
   unittest.main()