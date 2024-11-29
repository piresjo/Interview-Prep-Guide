import unittest
from vacuum import *

class Test(unittest.TestCase):        
    def testGeneral(self):
        self.assertTrue(vacuum(""))
        self.assertTrue(vacuum("LR"))
        self.assertTrue(vacuum("RUULLDRD"))
        self.assertFalse(vacuum("URURD"))

if __name__ == '__main__':
   unittest.main()