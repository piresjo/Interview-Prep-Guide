import pytest
from valid import *


class Test:

    def testGeneral(self):
        assert isValid("()[]{}"))
        assert isValid(""))
        assert not isValid("}"))
