import pytest
from crypt import *


class Test:
    def test(self):
        crypt1 = ["SEND", "MORE", "MONEY"]
        solution1 = [
            ["O", "0"],
            ["M", "1"],
            ["Y", "2"],
            ["E", "5"],
            ["N", "6"],
            ["D", "7"],
            ["R", "8"],
            ["S", "9"],
        ]
        crypt2 = ["ONE", "ONE", "TWO"]
        solution2 = [["O", "0"], ["T", "1"], ["W", "2"], ["E", "5"], ["N", "6"]]
        crypt3 = ["A", "B", "C"]
        solution3 = [["A", "5"], ["B", "6"], ["C", "1"]]

        assert isCryptSolution(crypt1, solution1)
        assert not isCryptSolution(crypt2, solution2)
        assert not isCryptSolution(crypt3, solution3)
