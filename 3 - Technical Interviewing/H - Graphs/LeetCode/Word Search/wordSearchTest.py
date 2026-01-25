import pytest
from wordSearch import *


class Test:
    def testEdgeCases(self):
        threeByThree = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        assert not exist(None, None))
        assert not exist(None, "HELLO"))
        assert not exist(threeByThree, None))
        assert not exist(["A"], "HELLO"))

    def testSingle(self):
        singleGrid = [["A"]]
        assert exist(singleGrid, "A"))
        assert not exist(singleGrid, "F"))

    def testDouble(self):
        twoByTwo = [["A", "B"], ["C", "D"]]
        assert exist(twoByTwo, "ABDC"))
        assert not exist(twoByTwo, "AD"))
        assert not exist(twoByTwo, "AAAA"))

    def testTriple(self):
        threeByThree = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        assert exist(threeByThree, "ABCFEDGHI"))
        assert not exist(threeByThree, "ABFHD"))
        assert not exist(threeByThree, "AAAA"))
        assert exist(threeByThree, "GHEF"))
