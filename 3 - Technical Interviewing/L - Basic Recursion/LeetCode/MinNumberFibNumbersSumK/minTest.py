import unittest
from minNum import *

class Test(unittest.TestCase):

    def testGeneral(self):
        self.assertEqual(findMinFibonacciNumbers(0), 0)
        self.assertEqual(findMinFibonacciNumbers(1), 1)
        self.assertEqual(findMinFibonacciNumbers(2), 1)
        self.assertEqual(findMinFibonacciNumbers(3), 1)
        self.assertEqual(findMinFibonacciNumbers(4), 2)
        self.assertEqual(findMinFibonacciNumbers(5), 1)
        self.assertEqual(findMinFibonacciNumbers(6), 2)
        self.assertEqual(findMinFibonacciNumbers(7), 2)

if __name__ == '__main__':
   unittest.main()