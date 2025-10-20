# Check If Binary Search Tree Is Balanced

## Problem

Given the `head` node of a binary search tree, determine if the tree is a balanced.

## Things To Note

The `BinarySearchTreeNode` is as follows:

```python
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

Recall the properties of a BST:

- Binary tree
- Left children elements less than parent
- Right children elements greater than parent

Here, we want to determine if the tree is balanced. In other words, we want to make sure that the height of the left subtree and the height of the right subtree are equal for all nodes.

## Solution Explained

FEED ME

## Full Solution

```python
def balanced(head):
    return checkHeight(head) != MIN

def checkHeight(head):
    if head is None:
        return MIN

    leftHeight = checkHeight(head.left)
    if not leftHeight:
        return MIN

    rightHeight = checkHeight(head.right)
    if not rightHeight:
        return MIN

    diff = Math.abs(leftHeight-rightHeight)

    if diff > 1:
        return MIN
    else:
        return Math.max(leftHeight, rightHeight) + 1

```

## Analysis

NEED TO ADD
