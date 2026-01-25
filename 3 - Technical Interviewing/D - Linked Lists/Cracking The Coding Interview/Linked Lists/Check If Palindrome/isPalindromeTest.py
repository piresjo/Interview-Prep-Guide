import pytest
from isPalindrome import *


class TestStringMethods:

    def testWithNoneObject(self):
        assert not isPalindrome(None))

    def testWithSingleton(self):
        single = LinkedList(25, None)
        assert isPalindrome(single))

    def testWithPalindromeDouble(self):
        testTail = LinkedList(67, None)
        testHead = LinkedList(67, testTail)
        assert isPalindrome(testHead))

    def testWithFalseDouble(self):
        testTail = LinkedList(67, None)
        testHead = LinkedList(25, testTail)
        assert not isPalindrome(testHead))

    def testWithPalindromeMulti(self):
        testTail = LinkedList(67, None)
        testMiddleA = LinkedList(39, testTail)
        testMiddleB = LinkedList(39, testMiddleA)
        testHead = LinkedList(67, testMiddleB)
        assert isPalindrome(testHead))

    def testWithFalseMulti(self):
        testTail = LinkedList(67, None)
        testMiddleA = LinkedList(39, testTail)
        testMiddleB = LinkedList(19, testMiddleA)
        testHead = LinkedList(67, testMiddleB)
        assert not isPalindrome(testHead))
