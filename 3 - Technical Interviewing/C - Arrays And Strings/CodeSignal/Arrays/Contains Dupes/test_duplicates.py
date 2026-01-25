import pytest
from duplicates import *


class Test:
    def test(self):
        assert containsDuplicates(None) == False
        assert containsDuplicates([]) == False
        assert containsDuplicates([1, 1, 2, 3, 4]) == True
        assert containsDuplicates([1, 2, 3, 4]) == False
