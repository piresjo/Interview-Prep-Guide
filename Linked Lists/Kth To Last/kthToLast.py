def kthToLast(head, k):
    pointerToReturn = head
    pointerToEnd = head

    for i in range(0, k):
        if pointerToEnd is None:
            return None
        pointerToEnd = pointerToEnd.next

    while (pointerToEnd is not None):
        pointerToEnd = pointerToEnd.next
        pointerToReturn = pointerToReturn.next
    
    return pointerToReturn