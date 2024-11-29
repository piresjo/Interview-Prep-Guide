import unittest
from longest import *

class Test(unittest.TestCase):

    def testGeneral(self):
        self.assertEqual(lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(lengthOfLongestSubstring(""), 0)
    
if __name__ == '__main__':
   unittest.main()
