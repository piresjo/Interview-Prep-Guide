import pytest
from difference import *


class Test:

    def testGeneral(self):
        assert difference("foobar", "barfoot") == "t"
        assert difference("ide", "idea") == "a"
        assert difference("coding", "ingcod") == ""
