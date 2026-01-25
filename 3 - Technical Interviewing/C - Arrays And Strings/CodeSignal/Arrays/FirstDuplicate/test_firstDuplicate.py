import pytest
from firstDuplicate import *


class Test:

    def testWithNone(self):
        assert firstDuplicate(None) == -1

    def testWithEmptyList(self):
        assert firstDuplicate([]) == -1

    def testWithSingleList(self):
        assert firstDuplicate([1]) == -1

    def testWithDoubleListNoDuplicate(self):
        assert firstDuplicate([1, 2]) == -1

    def testWithDoubleListDuplicate(self):
        assert firstDuplicate([1, 1]) == 1

    def testWithLongListNoDuplicate(self):
        listVal = [1, 2, 3, 4, 5, 6, 7]
        assert firstDuplicate(listVal) == -1

    def testWithLongListDuplicate(self):
        listVal = [1, 2, 3, 4, 2, 3, 4]
        assert firstDuplicate(listVal) == 2
