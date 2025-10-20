# Reversing A Doubly Linked List

## Problem

Given the `head` node of a doubly-linked list, reverse the order of the list

## Things To Note

The `DoublyLinkedListNode` object is defined as such:

```python
class DoublyLinkedListNode:
    def __init__(self, data):
        self.data = data # Whatever the data is
        self.next = None # Pointer to next node in list
        self.prev = None # Pointer to prev node in list
```

You are given the `head` node of the linked list, as well as the data for the new node.
Since this solution is done in Python, the problem will look like this:

```python
def reverse(head):
    # Code
```

The bidirectional nature of doubly linked lists makes a recursive solution not as easy to fully understand. However, as with other problems involving doubly-linked lists, we can do an iterative solution

There are two edge cases: when the head is null or the only node in a list. There is nothing to remove, so we can return the `head`

## Full Solution

```python
def reverse(head):
    tempVal = None
    currVal =  head

    while currVal is not none:
        tempVal = currVal.prev
        currVal.prev = currVal.next
        currVal.next = tempVal
        currVal = currVal.prev
    
    if temVal is not None:
        head = tempVal.prev
    
    return head
```

## Analysis

TO BE ADDED