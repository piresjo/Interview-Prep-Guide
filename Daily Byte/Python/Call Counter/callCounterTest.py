import unittest
from callCounter import *

class Test(unittest.TestCase):

    def testGeneral(self):
        callCounter = CallCounter()
        self.assertEqual(callCounter.ping(1), 1)
        self.assertEqual(callCounter.ping(300), 2)
        self.assertEqual(callCounter.ping(3000), 3)
        self.assertEqual(callCounter.ping(3002), 3)
        self.assertEqual(callCounter.ping(7000), 1)

if __name__ == '__main__':
   unittest.main()
