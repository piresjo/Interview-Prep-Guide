import unittest
from loopDetection import *

class TestStringMethods(unittest.TestCase):

    def testWithNoneObject(self):
        self.assertIsNone(whereIsLoop(None))

    def testDouble(self):
        test = LinkedList(20, LinkedList(25, None))
        self.assertIsNone(whereIsLoop(test))

    # For some reason, the last test in this file always sends a noneType, 
    # despite the code declaring otherwise. Will take a look later (TODO)
    def testSingle(self):
        testHead = LinkedList(20, None)
        self.assertIsNone(whereIsLoop(testHead))

    
if __name__ == '__main__':
   unittest.main()