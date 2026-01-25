import pytest
from simplify import *


class Test:
    def test(self):
        assert simplifyPath("/home/a/./x/../b//c/"), "/home/a/b/c")
        assert simplifyPath("/a/b/c/../.."), "/a")
        assert simplifyPath("/../"), "/")
        assert simplifyPath("/"), "/")
        assert simplifyPath("a/b/../c/d/../../e/../../"), "/")
        assert simplifyPath("/cHj/T//"), "/cHj/T")
