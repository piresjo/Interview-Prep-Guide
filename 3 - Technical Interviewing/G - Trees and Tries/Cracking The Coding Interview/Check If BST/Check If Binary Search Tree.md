# Check If Tree Is Binary Search Tree

## Problem

Given the `head` node of a tree, determine if the tree is a BST.

## Things To Note

The `BinaryTreeNode` is as follows:

```python
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

Recall the properties of a BST:

- Binary tree
- Left children elements less than parent
- Right children elements greater than parent

## Solution Explained

The problem lends itself to a recursive solution due to the qualities of a BST.

Our base case will be when the `head` is `None`. We'll consider `None` trees BSTs. Otherwise, we'll need to see if:

- The root data is less than or equal to the minimum value found in the tree
- The root data is greater than the maximum value already found in the tree
- The left subtree is a BST
- The right subtree is a BST

If the first two are false and the last two are true, then the tree is a BST

## Full Solution

```python
def isBST(head):
    return isBST(head, None, None)

def isBST(head, min, max):
    if head is None:
        return True

    if ((min is not None and head.data <= min) or (max is not None and head.data > max)):
        return False

    if not isBST(head.left, min, head.data) or not isBST(head.right, head,data, max):
        return False

    return True
```

## Analysis

NEED TO ADD
