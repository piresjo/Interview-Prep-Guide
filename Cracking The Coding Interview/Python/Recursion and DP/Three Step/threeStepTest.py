import unittest
from threeStep import *

class Test(unittest.TestCase):
    
    def testWithBaseCases(self):
       self.assertEqual(stairs(0), 1)
       self.assertEqual(stairs(1), 1)
       self.assertEqual(stairs(2), 2)

    def testGeneral(self):
        self.assertEqual(stairs(3), 4)
        self.assertEqual(stairs(4), 7)
        self.assertEqual(stairs(5), 13)

      

if __name__ == '__main__':
   unittest.main()