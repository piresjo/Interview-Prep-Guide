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

class LinkedList:
  def __init__(self, data, next):
    self.data = data
    self.next = next