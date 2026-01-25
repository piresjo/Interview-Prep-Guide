import pytest
from callCounter import *


class Test:

    def testGeneral(self):
        callCounter = CallCounter()
        assert callCounter.ping(1), 1)
        assert callCounter.ping(300), 2)
        assert callCounter.ping(3000), 3)
        assert callCounter.ping(3002), 3)
        assert callCounter.ping(7000), 1)
