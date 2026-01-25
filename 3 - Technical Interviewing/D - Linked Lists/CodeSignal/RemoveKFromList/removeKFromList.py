def removeKFromList(l, k):
    # Generation of the nullhead helps us avoid
    # Dealing with the case where we have to remove the
    # first value in the list. Now removing the first value in
    # the list can be done the same as any of the internal nodes
    nullHead = ListNode(None)
    nullHead.next = l

    curr = nullHead

    while curr:
        # By checking curr.next, we can easily deal with the
        # last node in the list
        while curr.next and curr.next.value == k:
            curr.next = curr.next.next
        curr = curr.next
    return nullHead.next


class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None
