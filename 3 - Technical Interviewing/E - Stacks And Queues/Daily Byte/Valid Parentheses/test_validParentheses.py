import pytest
from validParentheses import *


class Test:

    def testGeneral(self):
        assert isValid("()[]{}")
        assert isValid("")
        assert not isValid("}")
