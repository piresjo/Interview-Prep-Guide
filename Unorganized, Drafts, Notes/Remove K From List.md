# Remove K From Linked List

## Problem

Given the head node of list `l` and value `k`, delete the node that contains `k`. Then return the modified list.

## Things To Note

The `LinkedListNode` object is defined as such:

```python
class LinkedListNode:
    def __init__(self, data):
        self.val = data # Whatever the data is
        self.next = None # Pointer to next node in list
```

## Solution Explained

To delete, all we need to do is move the pointer past the element with data `k`. If this were done in a language with manual memory management, you'll have to deal with freeing that data.

We can iterate through the list. If we hit the value `k`, we just repoint the `next` node in the node prior to the `k` node to the node after the `k` node (or `None`)

## Solution

```python
def removeKFromList(l, k):
    nullHead = LinkedListNode(Node)
    nullHead.next = l

    curr =  nullHead

    while curr:
        while curr.next and curr.next.val == k:
            curr.next = curr.next.next
        curr.next
    return nullHead.next
```

## Analysis

In terms of time, in the worst case, we have to go through each node in the list once. So, in terms of time complexity, we have `O(n)` complexity.

In terms of space, we are creating a single node, but that's it. In other words, the space complexity is constant.
