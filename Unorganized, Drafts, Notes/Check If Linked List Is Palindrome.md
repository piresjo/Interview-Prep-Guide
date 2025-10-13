# Check If Linked List Is Palindrome

## Problem

Given the `head` of a single-linked list, see if the list is a palindrome.

## Things To Note

The `LinkedListNode` object is defined as such:

```python
class LinkedListNode:
    def __init__(self, data):
        self.data = data # Whatever the data is
        self.next = None # Pointer to next node in list
```

If a list is a palindrome, the reverse order is the same as the forward order.

Since this solution is done in Python, the problem will look like this:

```python
def isPalindrome,(head):
    # Code
```

## Solution Explained

We can do this in one pass with two pointers. One pointer will handle the first half of the list; the other will handle the second half. The LIFO nature of stacks will make the check relatively easy.

## Full Solution

```python
def isPalindrome(head):
    fast = head
    slow = head

    stack = []

    # Storing the first half of the list in a stack.
    # When we pop, it should match the contents of the second half of the list
    while fast is not None and fast.next is not None:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    # Handling cases where the list has an odd number of elements
    if fast is not None:
        slow = slow.next

    # Start comparing the first half with the second
    while slow is not None:
        dataToCheck = stack.pop()

        if top != slow.data:
            return False

        slow = slow.next
    return True
    
```

## Analysis

Linear time.
