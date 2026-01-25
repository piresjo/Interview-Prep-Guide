import pytest
from reverse import *


class Test:
    def testGeneral(self):
        assert reverse(None) == ""
        assert reverse("") == ""
        assert reverse("Hello") == "olleH"
