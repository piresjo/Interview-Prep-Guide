def remove(head, k):
    pointerToReturn = head
    pointerToEnd = head
    pointerBefore = None

    for i in range(0, k):
        if pointerToEnd is None:
            return None
        pointerToEnd = pointerToEnd.next

    while (pointerToEnd is not None):
        pointerToEnd = pointerToEnd.next
        pointerBefore = pointerToReturn
        pointerToReturn = pointerToReturn.next

    print("Q")
    print(pointerBefore.data)
    print(pointerToReturn.data)
    print(pointerToReturn.next.data)
    print("R")
        
    pointerBefore.next = pointerToReturn.next

    print("S")
    print(pointerBefore.data)
    print(pointerBefore.next.data)
    print("T")
    
    return head

class LinkedList:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next