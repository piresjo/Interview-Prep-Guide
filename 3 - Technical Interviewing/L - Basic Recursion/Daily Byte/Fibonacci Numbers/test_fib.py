import pytest
from fibDP import *
from fibMemo import *


class Test:

    def testGeneral(self):
        assert fibDP(0) == 0
        assert fibMemo(0) == 0
        assert fibDP(1) == 1
        assert fibMemo(1) == 1
        assert fibDP(2) == 1
        assert fibMemo(2) == 1
        assert fibDP(3) == 2
        assert fibMemo(3) == 2
        assert fibDP(4) == 3
        assert fibMemo(4) == 3
        assert fibDP(5) == 5
        assert fibMemo(5) == 5
        assert fibDP(6) == 8
        assert fibMemo(6) == 8
        assert fibDP(7) == 13
        assert fibMemo(7) == 13
