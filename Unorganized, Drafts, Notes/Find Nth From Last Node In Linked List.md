# Find Nth From Last Node In A Linked List

## Problem

Given the `head` of a single-linked list and an integer `n` to represent the `n`th from last position, find the value of that node, if possible.

## Things To Note

The `LinkedListNode` object is defined as such:

```python
class LinkedListNode:
    def __init__(self, data):
        self.data = data # Whatever the data is
        self.next = None # Pointer to next node in list
```

Since this solution is done in Python, the problem will look like this:

```python
def nthFromLast(head, n):
    # Code
```

## Solution Explained

We two pointers, we can do all this in one pass.
Let's create two pointer variables pointing to the head.

We'll use the first pointer to act as an offset for the second pointer. We'll move the first pointer `n` times through the list.

With that, all we need to do is move both pointers forward until the first pointer leaves the list. Whatever node that the second pointer hits will be the node that needs to be returned.

## Full Solution

```python
def nthFromLast(head, n):
    pA = head
    pB = head

    for i in range(0, n):
        if not pA:
            return None
        
        while pA:
            pA = pA.next
            pB = pB.next

    return pB
```

## Analysis

Linear time
