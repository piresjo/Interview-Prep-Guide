import unittest
from compare import *

class Test(unittest.TestCase):        
    def testGeneral(self):
        self.assertTrue(backspaceCompare("ABC#", "CD##AB"))
        self.assertTrue(backspaceCompare("como#pur#ter", "computer"))
        self.assertFalse(backspaceCompare("cof#dim#ng", "code"))

if __name__ == '__main__':
   unittest.main()