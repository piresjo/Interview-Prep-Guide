import pytest
from scoreParentheses import *


class Test:

    def testWithNone(self):
        assert scoreOfParentheses(None) == 0
        assert scoreOfParentheses("") == 0

    def testGeneral(self):
        assert scoreOfParentheses("()") == 1
        assert scoreOfParentheses("()()") == 2
        assert scoreOfParentheses("(())") == 2
        assert scoreOfParentheses("(()())") == 4
