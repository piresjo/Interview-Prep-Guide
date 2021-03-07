import unittest
from reverse import *

class Test(unittest.TestCase):

    def testGeneral(self):
        self.assertEqual(reverse(0), 0)
        self.assertEqual(reverse(-123), -321)
        self.assertEqual(reverse(23), 32)
        self.assertEqual(reverseMethod2(0), 0)
        self.assertEqual(reverseMethod2(-123), -321)
        self.assertEqual(reverseMethod2(23), 32)
        


if __name__ == '__main__':
   unittest.main()
