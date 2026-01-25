import pytest
from findProfession import *


class Test:

    def testWithBase(self):
        assert findProfession(1, 1), "Engineer")

    def testOnLevel2(self):
        assert findProfession(2, 2), "Doctor")

    def testOnLevel3(self):
        assert findProfession(3, 3), "Doctor")

    def testAdvanced(self):
        assert findProfession(25, 16777216), "Engineer")
