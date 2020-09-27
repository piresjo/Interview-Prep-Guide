import unittest
from reverse import *

class Test(unittest.TestCase):

    def testGeneral(self):
        generalNodeA = ListNode(1)
        nodeB = ListNode(2)
        nodeC = ListNode(3)
        nodeD = ListNode(4)
        nodeE = ListNode(5)
        generalNodeA.next = nodeB
        nodeB.next = nodeC
        nodeC.next = nodeD
        nodeD.next = nodeE

        self.assertEqual(testHelper(reverseNodesInKGroups(generalNodeA, 1)), [1, 2, 3, 4, 5])
        self.assertEqual(testHelper(reverseNodesInKGroups(generalNodeA, 7)), [5, 4, 3, 2, 1])
        self.assertEqual(testHelper(reverseNodesInKGroups(generalNodeA, 2)), [2, 1, 4, 3, 5])


def testHelper(h):
    returnList = []
    curr = h
    while curr:
        returnList.append(curr.value)
        curr = curr.next
    return returnList


if __name__ == '__main__':
   unittest.main()
