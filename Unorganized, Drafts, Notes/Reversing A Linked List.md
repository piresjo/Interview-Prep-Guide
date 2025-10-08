# Reversing A Linked List

## Problem

Given the `head` node of a single-linked list, reverse the order of the list

## Things To Note

The `LinkedListNode` object is defined as such:

```python
class LinkedListNode:
    def __init__(self, data):
        self.data = data # Whatever the data is
        self.next = None # Pointer to next node in list
```

You are given the `head` node of the linked list.
Since this solution is done in Python, the problem will look like this:

```python
def reverse(head):
    # Code
```

Like many other linked-list operations, this problem lends itself to a recursive solution as you go through the list flipping the directions of the list pointers.

There are two base cases: when the head is null or the only node in a list. There is nothing to remove, so we can return the `head`

## Solution Explained

TO BE ADDED

## Full Solution

```python
def reverse(head):
    if head is None or head.next is None:
        return head

    nextNode = head.next
    head.next = None
    newHead = reverse(nextNode)
    nextNode.next = head
    return newHead
```

## Analysis

TO BE ADDED