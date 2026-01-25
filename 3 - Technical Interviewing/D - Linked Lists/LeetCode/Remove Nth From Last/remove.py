def removeNthFromEnd(head, n):
    dummy = ListNode()
    dummy.next = head
    pointerA = dummy
    pointerB = dummy
    for i in range(0, n + 1):
        if pointerA is None:
            return head
        pointerA = pointerA.next

    while pointerA is not None:
        pointerA = pointerA.next
        pointerB = pointerB.next

    pointerB.next = pointerB.next.next
    return dummy.next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
