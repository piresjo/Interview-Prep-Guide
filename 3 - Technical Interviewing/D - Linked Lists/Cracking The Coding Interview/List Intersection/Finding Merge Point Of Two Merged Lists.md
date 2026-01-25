# Comparing Linked Lists

## Problem

Given the head nodes of two single-linked lists, can we determine:

- If the lists merge?
- Where the merge point is?

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
def findMergeNode(headA, headB):
    # Code
```

## Solution Explained

FEED ME

## Full Solution

```python
def findMergeNode(headA, headB):
    currA = headA
    currB = headB

    while currA != currB:
        if currA.next is None:
            currA = headB
        else:
            currA = currA.next

        if currB.next is None:
            currB = headA
        else:
            currB = currB.next
    return currB.data
```

## Analysis

FEED ME
