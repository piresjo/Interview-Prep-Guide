import unittest
from mergeString import *

class Test(unittest.TestCase):

    def testGeneral(self):
        self.assertEqual(mergeString("abc", "def"), "adbecf")
        self.assertEqual(mergeString("abcd", "ef"), "aebfcd")
        self.assertEqual(mergeString("", "abc"), "abc")
        self.assertEqual(mergeString("abc", ""), "abc")
        self.assertEqual(mergeString("", ""), "")

if __name__ == '__main__':
   unittest.main()