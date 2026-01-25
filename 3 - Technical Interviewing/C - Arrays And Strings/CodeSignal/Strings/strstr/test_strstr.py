import pytest
from strstr import *


class Test:
    def testGeneral(self):
        assert strStr("CodefightsIsAwesome", "IA") == -1
        assert strStr("CodefightsIsAwesome", "IsA") == 10
        assert strStr("a", "a") == 0
        assert strStr("a", "A") == -1
