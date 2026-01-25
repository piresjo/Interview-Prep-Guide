def remove(head, k):
    pointerToReturn = head
    pointerToEnd = head
    pointerBefore = None

    for i in range(0, k):
        if pointerToEnd is None:
            return None
        pointerToEnd = pointerToEnd.next

    while pointerToEnd is not None:
        pointerToEnd = pointerToEnd.next
        pointerBefore = pointerToReturn
        pointerToReturn = pointerToReturn.next

    pointerBefore.next = pointerToReturn.next

    return head


class LinkedList:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
