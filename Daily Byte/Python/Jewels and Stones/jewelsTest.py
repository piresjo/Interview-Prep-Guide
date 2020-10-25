import unittest
from jewels import *

class Test(unittest.TestCase):

    def testGeneral(self):
        self.assertEqual(numJewels("abc", "ac"), 2)
        self.assertEqual(numJewels("Af", "AaaddfFf"), 3)
        self.assertEqual(numJewels("AYOPD", "ayopd"), 0)

if __name__ == '__main__':
   unittest.main()