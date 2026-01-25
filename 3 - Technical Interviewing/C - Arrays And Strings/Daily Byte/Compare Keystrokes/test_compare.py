import pytest
from compare import *


class Test:
    def testGeneral(self):
        assert backspaceCompare("ABC#", "CD##AB")
        assert backspaceCompare("como#pur#ter", "computer")
        assert not backspaceCompare("cof#dim#ng", "code")
