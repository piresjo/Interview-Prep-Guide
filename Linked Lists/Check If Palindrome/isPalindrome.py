def isPalindrome(head):
    if head is None:
        return False
    if head.next is None:
        return True

    stack = []
    fast = head
    slow = head

    while fast is not None and fast.next is not None:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next


    if fast is not None:
        slow = slow.next

    while slow is not None:
        popValue = stack.pop() 
        if slow.data != popValue:
            return False
        slow = slow.next
    
    return True

class LinkedList:
  def __init__(self, data, next):
    self.data = data
    self.next = next