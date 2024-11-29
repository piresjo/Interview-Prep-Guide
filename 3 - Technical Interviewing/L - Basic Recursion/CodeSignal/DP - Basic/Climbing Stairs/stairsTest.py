import unittest
from stairs import *

class Test(unittest.TestCase):
    
    def testWithBaseCases(self):
       self.assertEqual(stairs(0), 1)
       self.assertEqual(stairs(1), 1)

    def testGeneral(self):
        self.assertEqual(stairs(2), 2)
        self.assertEqual(stairs(3), 3)
        self.assertEqual(stairs(38), 63245986)

      

if __name__ == '__main__':
   unittest.main()
