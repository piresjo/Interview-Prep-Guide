import pytest
from areIsomorphic import *


class Test:

    def testGeneral(self):
        assert isIsomorphic("egg", "add")
        assert not isIsomorphic("foo", "bar")
        assert not isIsomorphic("a", "ab")
        assert isIsomorphic("paper", "title")
