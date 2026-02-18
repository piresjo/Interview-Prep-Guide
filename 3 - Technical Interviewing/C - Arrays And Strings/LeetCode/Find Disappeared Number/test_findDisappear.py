import pytest
from findDisappear import *


class Test:

    def testArrayImplementation(self):
        assert findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
        assert findDisappearedNumbers([1, 1]) == [2]
        assert findDisappearedNumbers([1, 2, 3, 4, 5]) == []

    def testDictImplementation(self):
        assert findDisappearedNumbersAlt([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
        assert findDisappearedNumbersAlt([1, 1]) == [2]
        assert findDisappearedNumbersAlt([1, 2, 3, 4, 5]) == []
