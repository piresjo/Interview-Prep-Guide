import pytest
from minNum import *


class Test:

    def testGeneral(self):
        assert findMinFibonacciNumbers(0) == 0
        assert findMinFibonacciNumbers(1) == 1
        assert findMinFibonacciNumbers(2) == 1
        assert findMinFibonacciNumbers(3) == 1
        assert findMinFibonacciNumbers(4) == 2
        assert findMinFibonacciNumbers(5) == 1
        assert findMinFibonacciNumbers(6) == 2
        assert findMinFibonacciNumbers(7) == 2
