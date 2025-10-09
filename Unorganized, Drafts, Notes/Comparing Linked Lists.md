# Comparing Linked Lists

## Problem

Given the head nodes of two single-linked lists, can we determine if the lists are equivalent?

## Things To Note

By equivalent, we mean that:

- Both lists have the same number of elements
- The elements of both lists are equivalent

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
def compareLists(headA, headB):
    # Code
```

We can use a recursive algorithm to deal with both criteria. We can recursively traverse through both lists. If the values aren't equal or if one is null, that means that at least one of the criteria for equivalence can't be met.

## Solution Explained

As mentioned above, we'll be using a recursive algorithm. That way, we can check both the equal size and same elements criteria for equivalent lists in one pass.

We check the head nodes. If both are `None`, we can return `True`. If only one of them is `None`, we can return `False`. That will satisfy the length checks.

Then we'll be checking the data in the nodes. If the data matches, we can move onto the next element by calling the method and having the nodes after the head nodes as the parameters. Otherwise, we can return `False` since the data doesn't match.

## Full Solution

```python
def compareLists(headA, headB):
    if headA is None and headB is None:
        return True
    if headA is  None or headB is None:
        return False

    if (headA.data == headB.data):
        return compareLists(headA.next, headB.next)
    return False
```

## Analysis

In the worst case, both lists are the same size and have the same elements, since all of the elements in both lists have to be checked. So, the time complexity is `O(n)`, with `n` dependent on the size of the lists.

As for memory, in the worst case, we're only hitting each element of each list once. As a result, the size of the stack is dependent on the size of the lists and the complexity is `O(n)`.
