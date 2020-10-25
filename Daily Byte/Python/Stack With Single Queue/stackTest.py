import unittest
from stack import *

class Test(unittest.TestCase):

    def testGeneral(self):
        stackVal = Stack()

        stackVal.push(3)
        self.assertEqual(stackVal.peek(), 3)

        stackVal.push(4)
        self.assertEqual(stackVal.peek(), 4)

        stackVal.push(5)
        self.assertEqual(stackVal.peek(), 5)

        self.assertEqual(stackVal.pop(), 5)
        self.assertEqual(stackVal.peek(), 4)
        

if __name__ == '__main__':
   unittest.main()
