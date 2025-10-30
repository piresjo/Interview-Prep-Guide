# Vertical Order Traversal

## Problem

## Things To Note

These are standard binary trees; no BST considerations are required.

Here is how the `TreeNode` is defined:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

## Solution Explained

We'll be using BFS, but we'll also need to account for both row and column in the tree. Both are needed; if you don't factor in the row, you might get things out of order. Once that's done, sort sections by column (keeping track of everything will necessitate a maxLevel and minLevel variable so we can iterate). Within the sections, sort by the row val.

We'll need a dictionary/map to keep the (node, row) tuples sorted by column.

## Solution

## Analysis