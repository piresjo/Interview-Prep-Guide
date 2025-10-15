# Path Through Tree With Given Sum

## Problem

Given the head `t` node of a tree and a sum `s`, is there a path in the tree where the sum of the nodes traverse equals `s`?

## Things To Note

The `BinaryTreeNode` is as follows:

```python
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

## Solution Explained

We can do this recursively, reducing the `s` value by the node's data until `s` is 0 (ideally).

We have two cases where we stop recursion:

- If `t` is `None` -> We return `False`
- If `t` doesn't have any children -> We check to see if `s` is 0. Otherwise there isn't a path that yields that sum.

## Solution

```python
def hasPathWithGivenSum(t, s):
    if t is None:
        return False
    
    s -= t.data

    if t.left is None and t.right is None:
        return (s == 0)
    
    return hasPathWithGivenSum(t.left, s) or hasPathWithGivenSum(t.right, s)
```

## Analysis

FEED ME