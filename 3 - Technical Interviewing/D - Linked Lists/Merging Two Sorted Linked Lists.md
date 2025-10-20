# Merge Two Sorted Linked Lists

## Problem

Given the head nodes of two sorted single-linked lists, merge them so that the final list is sorted.

## Things To Note

The `LinkedListNode` object is defined as such:

```python
class LinkedListNode:
    def __init__(self, data):
        self.data = data # Whatever the data is
        self.next = None # Pointer to next node in list
```

You are given the head nodes of the linked lists.
Since this solution is done in Python, the problem will look like this:

```python
def merge(headA, headB):
    # Code
```

## Solution Explained

FEED ME

## Full Solution

```python
def merge(headA, headB):
    if headB is None and headA is None:
        return None
    if headA is not None and headB is  None:
        return headA
    if headB is not None and headA is None:
        return headB
    
    if headA.data < headB.data: 
        headA.next = merge(headA.next, headB)
    else:
        temp = headB
        headB = headB.next
        temp.next = headA
        headA = temp
        headA.next = merge(headA.next, headB)

    return headA
```

## Analysis

FEED ME
