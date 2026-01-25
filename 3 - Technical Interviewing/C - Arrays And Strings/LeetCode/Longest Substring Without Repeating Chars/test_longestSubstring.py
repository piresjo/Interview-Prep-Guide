import pytest
from longestSubstring import *


class Test:

    def testGeneral(self):
        assert lengthOfLongestSubstring("abcabcbb") == 3
        assert lengthOfLongestSubstring("bbbbb") == 1
        assert lengthOfLongestSubstring("pwwkew") == 3
        assert lengthOfLongestSubstring("") == 0
