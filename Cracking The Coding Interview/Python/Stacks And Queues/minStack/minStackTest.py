import unittest
from minStack import *

class Test(unittest.TestCase):

    def testGeneral(self):
        stackVal = MinStack()
        
        stackVal.push(5)
        self.assertEqual(stackVal.stack, [5])
        self.assertEqual(stackVal.min(), 5)

        stackVal.push(6)
        self.assertEqual(stackVal.stack, [5, 6])
        self.assertEqual(stackVal.min(), 5)

        stackVal.push(3)
        self.assertEqual(stackVal.stack, [5, 6, 3])
        self.assertEqual(stackVal.min(), 3)

        stackVal.push(7)
        self.assertEqual(stackVal.stack, [5, 6, 3, 7])
        self.assertEqual(stackVal.min(), 3)

        stackVal.pop()
        self.assertEqual(stackVal.stack, [5, 6, 3])
        self.assertEqual(stackVal.min(), 3)

        stackVal.pop()
        self.assertEqual(stackVal.stack, [5, 6])
        self.assertEqual(stackVal.min(), 5)

    
if __name__ == '__main__':
   unittest.main()