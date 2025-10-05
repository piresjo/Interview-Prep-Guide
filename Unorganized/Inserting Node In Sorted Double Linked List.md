# Inserting Node In Sorted Doubly-Linked List

## Problem

Given the `head` node of a doubly-linked list that is sorted and data for a new node,
create a new node with the data and add it to the linked list so the list is ordered.

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
def sortedInsert(head, data):
    # Code
    return head
```

There is a base case: when the head is null. As a result, the new node is automatically the head,
and since there is only one node in the list, the list is in order.

## Solution Explaned

The first thing we want to do is create the node based off the data we got.
If there is no `head` node, you can return the new node as is.
If the value of the new node is less than the value of the current head, make the new node the head.

```python
newNode = DoublyLinkedListNode(data)
if head is None:
    return newNode
if data < head.data:
    newNode.next = head
    head.pred = newNode
    return newNode
```

Create two new pointer variables. `pointerA` will refer to the node before `pointerB`.
Point `pointerA` to `None` and `pointerB` to `head`

```python
pointerA = None
pointerB = head
```

These pointer variables will be used for comparison. If the data of the new node is greater than
the data in `pointerA` and less then the data in `pointerB`, you need to put the new node in between
the pointers. This allows us to perform all this in linear time.

Once inserted, you can return the `head` of the list.

```python
# Find where to add the node
while(pointerB is not None and pointerB.data < data):
    pointerA = pointerB
    pointerB = pointerB.next

# Putting the node at the end
if pointerB is None:
    pointerA.next = newNode
    newNode.prev = pointerA
else: # Putting the node in the middle of the list
    pointerA.next = newNode
    pointerB.prev = newNode
    newNode.prev = pointerA
    newNode.next = pointerB

return head
```

## Full Solution

```python
def sortedInsert(head, data):
    newNode = DoublyLinkedListNode(data)

    if head is None:
        return newNode
    if data < head.data:
        newNode.next = head
        head.pred = newNode
        return newNode

    pointerA = None
    pointerB = head

    # Find where to add the node
    while(pointerB is not None and pointerB.data < data):
        pointerA = pointerB
        pointerB = pointerB.next

    # Putting the node at the end
    if pointerB is None:
        pointerA.next = newNode
        newNode.prev = pointerA
    else: # Putting the node in the middle of the list
        pointerA.next = newNode
        pointerB.prev = newNode
        newNode.prev = pointerA
        newNode.next = pointerB

    return head
```

## Analysis

In the worst case scenario, each node is used in a comparison twice (with the exception of the last node in the list, since that gets hit once).
This implies that the runtime is linear time (`O(n)`).
