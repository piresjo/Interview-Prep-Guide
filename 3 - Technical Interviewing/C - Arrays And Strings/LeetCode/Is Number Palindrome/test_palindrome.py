import pytest
from palindrome import *


class Test:

    def testGeneral(self):
        assert isPalindrome(10101)
        assert isPalindrome(1)
        assert not isPalindrome(1010)
        assert not isPalindrome(-10101)
