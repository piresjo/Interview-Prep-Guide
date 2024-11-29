import unittest
from correct import *

class Test(unittest.TestCase):        
    def testGeneral(self):
        self.assertFalse(correctCapitalization(None))
        self.assertFalse(correctCapitalization(""))
        self.assertTrue(correctCapitalization("A"))
        self.assertTrue(correctCapitalization("a"))
        self.assertTrue(correctCapitalization("USA"))
        self.assertTrue(correctCapitalization("Calvin"))
        self.assertTrue(correctCapitalization("computing"))
        self.assertFalse(correctCapitalization("hELLo"))


if __name__ == '__main__':
   unittest.main()
