import unittest
from add import *

class Test(unittest.TestCase):     
    def testGeneral(self):
        self.assertEqual(addBinary("1", "1"), "10")
        self.assertEqual(addBinary("0", "1"), "1")
        self.assertEqual(addBinary("0", "0"), "0")

if __name__ == '__main__':
   unittest.main()