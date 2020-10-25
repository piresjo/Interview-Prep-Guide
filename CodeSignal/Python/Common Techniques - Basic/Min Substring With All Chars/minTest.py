import unittest
from min import *

class Test(unittest.TestCase):

    def testGeneral(self):
        self.assertEqual(minSubstringWithAllChars("adobecodebanc", "abc"), 'banc')
        self.assertEqual(minSubstringWithAllChars("", ""), '')
        self.assertEqual(minSubstringWithAllChars("abc", "abc"), 'abc')
        self.assertEqual(minSubstringWithAllChars("zqyvbfeiee", "ze"), "zqyvbfe")
        

if __name__ == '__main__':
   unittest.main()
