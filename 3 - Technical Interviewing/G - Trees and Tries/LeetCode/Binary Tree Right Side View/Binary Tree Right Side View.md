# Binary Tree Right Side View

## Problem

Given the head of a binary tree `root`, going from top to bottom, return the right side view of the tree

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

Key words here are 'top to bottom'. This is likely a BFS solution. We need a modified BFS to return the right side view. We need a way to determine the rightmost element in a row. Given BFS, it would be the last element in the row.

## Solution

```python
def rightSideView(root):
    if root is None:
        return []
    visibleQueue = []
    visibleList = []
    visibleQueue.append(root)
        
    while len(visibleQueue) > 0:
        sizeVal = len(visibleQueue)
        for i in range(0, sizeVal):
            temp = visibleQueue.pop(0)
            if i == sizeVal - 1:
                visibleList.append(temp.val)
            if temp.left:
                visibleQueue.append(temp.left)
            if temp.right:
                visibleQueue.append(temp.right)
                
        
    return visibleList

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

## Analysis

With this solution, we are going through, at worst, all of the nodes in the tree. To keep track of what to return (and what to move through for the BST process), we'll need a list and queue that could potentially contain all nodes in the tree.

Based off this, we can say that both the time and space complexity are linear.