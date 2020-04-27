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
        if slow.data != stack.pop:
            return False
    
    return True