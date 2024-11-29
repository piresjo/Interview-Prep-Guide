import unittest
from valid import *

class Test(unittest.TestCase):

    def testGeneral(self):
        self.assertTrue(isValid("()[]{}"))
        self.assertTrue(isValid(""))
        self.assertFalse(isValid("}"))

if __name__ == '__main__':
   unittest.main()
