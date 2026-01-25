import pytest
from uncommon import *


class Test:

    def testGeneral(self):
        assert uncommon("the quick", "brown fox") == ["the", "quick", "brown", "fox"]
        assert uncommon(
            "the tortoise beat the haire", "the tortoise lost to the haire"
        ) == ["beat", "lost", "to"]
        assert uncommon("copper coffee pot", "hot coffee pot"), ["copper", "hot"]
