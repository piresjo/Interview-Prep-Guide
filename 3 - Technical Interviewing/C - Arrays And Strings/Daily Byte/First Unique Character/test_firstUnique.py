import pytest
from firstUnique import *


class Test:
    def testGeneral(self):
        assert firstUniqChar("abcabd") == 2
        assert firstUniqChar("thedailybyte") == 1
        assert firstUniqChar("developer") == 0
        assert firstUniqChar("aassddff") == -1
