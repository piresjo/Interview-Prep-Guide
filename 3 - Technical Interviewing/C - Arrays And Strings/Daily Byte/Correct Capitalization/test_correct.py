import pytest
from correct import *


class Test:
    def testGeneral(self):
        assert not correctCapitalization(None)
        assert not correctCapitalization("")
        assert correctCapitalization("A")
        assert correctCapitalization("a")
        assert correctCapitalization("USA")
        assert correctCapitalization("Calvin")
        assert correctCapitalization("computing")
        assert not correctCapitalization("hELLo")
