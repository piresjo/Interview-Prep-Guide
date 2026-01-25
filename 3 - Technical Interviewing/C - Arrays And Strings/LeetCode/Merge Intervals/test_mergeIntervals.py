import pytest
from mergeIntervals import *


class Test:
    def testBaseCases(self):
        assert merge(None) == None
        assert merge([]) == []
        assert merge([[1, 3]]) == [[1, 3]]

    def testGeneral(self):
        assert merge([[1, 3], [4, 6], [8, 10]]) == [[1, 3], [4, 6], [8, 10]]
        assert merge([[8, 10], [4, 6], [1, 3]]) == [[1, 3], [4, 6], [8, 10]]
        assert merge([[1, 4], [4, 6], [5, 10]]) == [[1, 10]]
