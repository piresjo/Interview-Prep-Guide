# Detecting A Cycle In A Linked List

## Problem

Given the `head` node of a single-linked list, can we determine if the list is cyclical.

## Things To Note

By `cyclical`, we mean that all the nodes point to another node in such a way to create a cycle.

The `LinkedListNode` object is defined as such:

```python
class LinkedListNode:
    __init__(self, data):
        self.data = data # Whatever the data is
        self.next = None # Pointer to next node in list
```

You are given the `head` node of the linked list.
Since this solution is done in Python, the problem will look like this:

```python
def hasCycle(head):
    # Code
```

There is a base case: when the head is null. The list is clearly not cyclical, so we can mark as `False`

All the values in the list are unique.

## Solution Explaned

If there is a cycle in the list, two pointers going through the list at different speeds will eventually intersect.

As for lists without a cycle, eventually one of the pointers will be `None` sooner or later. In the case of
the faster pointer, if it hits the end of the list, that'll suffice in stopping the loop.

As a starting point, the only place to start is `head`.

## Full Solution

```python
def hasCycle(head):
    if head is None:
        return False

    slow = head
    fast = head

    while (fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
```

## Analysis

NEED TO ADD
