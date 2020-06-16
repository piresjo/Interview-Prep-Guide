import unittest
from isPalindrome import *

class TestStringMethods(unittest.TestCase):

    def testWithNoneObject(self):
        self.assertFalse(isPalindrome(None))

    def testWithSingleton(self):
        single = LinkedList(25, None)
        self.assertTrue(isPalindrome(single))

    def testWithPalindromeDouble(self):
        testTail = LinkedList(67, None)
        testHead = LinkedList(67, testTail)
        self.assertTrue(isPalindrome(testHead))

    def testWithFalseDouble(self):
        testTail = LinkedList(67, None)
        testHead = LinkedList(25, testTail)
        self.assertFalse(isPalindrome(testHead))

    def testWithPalindromeMulti(self):
        testTail = LinkedList(67, None)
        testMiddleA = LinkedList(39, testTail)
        testMiddleB = LinkedList(39, testMiddleA)
        testHead = LinkedList(67, testMiddleB)
        self.assertTrue(isPalindrome(testHead))

    def testWithFalseMulti(self):
        testTail = LinkedList(67, None)
        testMiddleA = LinkedList(39, testTail)
        testMiddleB = LinkedList(19, testMiddleA)
        testHead = LinkedList(67, testMiddleB)
        self.assertFalse(isPalindrome(testHead))


        

       
if __name__ == '__main__':
   unittest.main()