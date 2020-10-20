import unittest
from rotation import *

class Test(unittest.TestCase):

    def testWithNone(self):
        self.assertFalse(rotation(None, None))  

    def testWithEmpty(self):
        self.assertFalse(rotation("", ""))  

    def testGeneral(self):
        self.assertTrue(rotation("waterbottle", "erbottlewat"))  
        self.assertFalse(rotation("waterbottle", "chungus")) 

    
if __name__ == '__main__':
   unittest.main()
