def whereIsLoop(head):
    if head is None:
        return None

    pointer1 = head
    pointer2 = head

    while (True):
        
        if pointer2.next is None:
            return None
        if pointer2.next.next is None:
            return None
        if pointer1 == pointer2:
            return pointer1
        pointer1 = pointer1.next
        pointer2 = pointer2.next.next

class LinkedList:
  def __init__(self, data, next):
    self.data = data
    self.next = next
