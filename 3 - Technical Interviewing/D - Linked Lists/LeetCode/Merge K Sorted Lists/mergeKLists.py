"""
General idea: An easy way to do this is through heapsort.
In other words, feed all the contents of the lists into a heap
(python defaults to a minheap with heapq).

When you create the new list to return, it's easier to create a dummy head,
and make the real head the next node after that. With that, keep popping values
from the minheap and create a new node based off that, adding that to the
list.
"""

import heapq


def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    dummy = ListNode(0)
    current = dummy

    heap = []
    for sorted_list in lists:
        if sorted_list:
            curr = sorted_list
            while curr:
                heapq.heappush(heap, curr.val)
                curr = curr.next

    while heap:
        smallest = heapq.heappop(heap)
        current.next = ListNode(smallest)
        current = current.next

    return dummy.next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
