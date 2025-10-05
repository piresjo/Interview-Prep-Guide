# Removing Duplicates From A Single-Linked List

## Problem

Given the `head` node of a single-linked list, determine if there are any duplicates in
the list and remove them, returning the `head` of a linked list of unique values.

## Things To Note

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
def removeDuplicates(head):
    # Code
```

There is a base case: when the head is null. There is nothing to remove, so we can return `None`

## Solution Explaned - Recursive

TO BE ADDED

## Full Solution - Recursive

```python
def removeDuplicates(head):
    if head is None:
        return None

    nextNode = head.next
    while nextNode is not None and head.data == nextNode.data:
        nextNode = nextNode.next
    head.next = removeDuplicates(nextNode)
    return head
```

## Solution Explaned - Recursive

TO BE ADDED

## Full Solution - Recursive

TO BE ADDED

## Analysis

TO BE ADDED
