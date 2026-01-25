import pytest
from matrixRotation import *


class TestStringMethods:

    def testWithNoneObject(self):
        assert not rotateMatrix(None)

    def testWithMisshapenList(self):
        misshapen = [[], [], []]
        rotateMatrix(misshapen)
        assert not rotateMatrix([[], [], []])

    def testWithEmptyList(self):
        assert not rotateMatrix([])

    def testOneByOne(self):
        testMatrix = [[1]]
        assert testMatrix == rotateMatrix(testMatrix)

    def testTwoByTwo(self):
        testMatrix0 = [[1, 2], [3, 4]]
        testMatrix90 = [[3, 1], [4, 2]]
        testMatrix180 = [[4, 3], [2, 1]]
        testMatrix270 = [[2, 4], [1, 3]]

        testMatrix = [[1, 2], [3, 4]]
        assert testMatrix90 == rotateMatrix(testMatrix)
        assert testMatrix180 == rotateMatrix(testMatrix)
        assert testMatrix270 == rotateMatrix(testMatrix)
        assert testMatrix0 == rotateMatrix(testMatrix)
