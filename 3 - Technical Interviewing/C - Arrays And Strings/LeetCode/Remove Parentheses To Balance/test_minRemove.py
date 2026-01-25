import pytest
from minRemove import *


class Test:

    def testGeneral(self):
        assert minRemoveToMakeValid("()") == "()"
        assert minRemoveToMakeValid(")(") == ""
        assert minRemoveToMakeValid("(()") == "()"
        assert minRemoveToMakeValid("lee(t(c)o)de)") == "lee(t(c)o)de"
