import unittest
from decode import *

class Test(unittest.TestCase):
    
    def testWithEmpty(self):
        self.assertEqual(decodeString(""), "")
        
    def testGeneral(self):
        self.assertEqual(decodeString("asdf"), "asdf")
        self.assertEqual(decodeString("4[ab]"), "abababab")
        self.assertEqual(decodeString("3[a2[c]]"), "accaccacc")



if __name__ == '__main__':
   unittest.main()
