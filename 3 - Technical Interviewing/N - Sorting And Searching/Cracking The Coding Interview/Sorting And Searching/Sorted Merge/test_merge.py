import pytest
from merge import *


class Test:

    def testWithBaseCases(self):
        assert merge(None, None, 0, 0) == None
        assert merge([2], None, 0, 0) == [2]

    def testGeneralCase(self):
        assert merge([1, 4, 5, 8, 10], [], 5, 0) == [1, 4, 5, 8, 10]
        assert merge([1, 4, 5, 8, 10, 0, 0], [3, 9], 5, 2) == [1, 3, 4, 5, 8, 9, 10]
