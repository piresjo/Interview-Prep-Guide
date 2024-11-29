import unittest
from fibDP import *
from fibMemo import *

class Test(unittest.TestCase):

    def testGeneral(self):
        self.assertEqual(fibDP(0), 0)
        self.assertEqual(fibMemo(0), 0)
        self.assertEqual(fibDP(1), 1)
        self.assertEqual(fibMemo(1), 1)
        self.assertEqual(fibDP(2), 1)
        self.assertEqual(fibMemo(2), 1)
        self.assertEqual(fibDP(3), 2)
        self.assertEqual(fibMemo(3), 2)
        self.assertEqual(fibDP(4), 3)
        self.assertEqual(fibMemo(4), 3)
        self.assertEqual(fibDP(5), 5)
        self.assertEqual(fibMemo(5), 5)
        self.assertEqual(fibDP(6), 8)
        self.assertEqual(fibMemo(6), 8)
        self.assertEqual(fibDP(7), 13)
        self.assertEqual(fibMemo(7), 13)

if __name__ == '__main__':
   unittest.main()