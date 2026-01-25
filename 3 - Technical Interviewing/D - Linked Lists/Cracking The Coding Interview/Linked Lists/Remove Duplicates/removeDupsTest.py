import pytest
from removeDups import *


class TestStringMethods:

    def testWithNoneObject(self):
        assert not deleteDups(None))

    def testNoDuplicates(self):
        test = LinkedList(20, LinkedList(25, LinkedList(30, None)))
        result = deleteDups(test)
        assert result.data, 20)
        assert result.next.data, 25)

    def testWithDuplicates(self):
        testA = LinkedList(20, None)
        testB = LinkedList(15, None)
        testC = LinkedList(20, None)
        testD = LinkedList(30, None)
        testE = LinkedList(15, None)
        testA.next = testB
        testB.next = testC
        testC.next = testD
        testD.next = testE
        result = deleteDups(testA)
        assert result.data, 20)
        assert result.next.data, 15)
