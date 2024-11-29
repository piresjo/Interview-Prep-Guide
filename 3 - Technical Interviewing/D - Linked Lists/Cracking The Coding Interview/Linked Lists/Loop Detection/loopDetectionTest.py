import unittest
from loopDetection import *

class TestStringMethods(unittest.TestCase):

    def testWithNoneObject(self):
        self.assertIsNone(whereIsLoop(None))

    def testDouble(self):
        test = LinkedList(20, LinkedList(25, None))
        self.assertIsNone(whereIsLoop(test))

    def testSingle(self):
        testHead = LinkedList(20, None)
        self.assertIsNone(whereIsLoop(testHead))

    
if __name__ == '__main__':
   unittest.main()