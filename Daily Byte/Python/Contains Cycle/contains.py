def contains(head):
    valueSet = set()
    pointer = head
    while pointer:
        if pointer.value in valueSet:
            return True
        valueSet.add(pointer.value)
        pointer = pointer.next
    return False

class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None