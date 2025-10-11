# Lowest Common Ancestor Of Nodes In A BST

## Problem

Given the `root` node of a binary search tree and two nodes `v1` and `v2`, find the lowest common ancestor (that is, the )

## Things To Note

The `BinarySearchTreeNode` is as follows:

```python
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

Since this solution is done in Python, the problem will look like this:

```python
def lca(root):
    # Code
```

## Solution Explained

FEED ME

## Full Solution

```python
def lca(root, v1, v2):
    if root.data < v1 and root.data < v2:
        return lca(root.right, v1, v2)
    if root.data > v1 and root.data > v2:
        return lca(root.left, v1, v2)
    
    return root
    
```

## Analysis

FEED ME