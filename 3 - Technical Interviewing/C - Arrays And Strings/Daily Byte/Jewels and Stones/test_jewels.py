import pytest
from jewels import *


class Test:

    def testGeneral(self):
        assert numJewels("abc", "ac") == 2
        assert numJewels("Af", "AaaddfFf") == 3
        assert numJewels("AYOPD", "ayopd") == 0
