def reverseNodesInKGroups(l, k):
    curr = l
    countVal = 0
    while curr:
        countVal += 1
        curr = curr.next

    maxLen = countVal - (countVal % k)

    return reverseKAux(l, k, maxLen, 0)


def reverseKAux(head, k, lenVal, start):
    current = head
    nextVal = None
    prev = None
    count = 0

    while current is not None and count < k:
        nextVal = current.next
        current.next = prev
        prev = current
        current = nextVal
        count += 1
        start += 1

    if nextVal is not None and start < lenVal:
        head.next = reverseKAux(nextVal, k, lenVal, start)
    else:
        head.next = nextVal

    return prev


class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None
