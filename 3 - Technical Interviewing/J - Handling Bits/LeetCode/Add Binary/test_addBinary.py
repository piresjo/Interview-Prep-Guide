import pytest
from addBinary import *


class Test:
    def testGeneral(self):
        assert addBinary("1", "1") == "10"
        assert addBinary("0", "1") == "1"
        assert addBinary("0", "0") == "0"
