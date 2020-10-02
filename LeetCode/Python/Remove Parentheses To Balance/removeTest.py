import unittest
from remove import *

class Test(unittest.TestCase):

    def testGeneral(self):
        self.assertEqual(minRemoveToMakeValid("()"), "()")
        self.assertEqual(minRemoveToMakeValid(")("), "")
        self.assertEqual(minRemoveToMakeValid("(()"), "()")
        self.assertEqual(minRemoveToMakeValid("lee(t(c)o)de)"), "lee(t(c)o)de")
        


if __name__ == '__main__':
   unittest.main()
