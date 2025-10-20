# Determine The Height Of A Tree

## Problem

Given the `root` node of a tree, can we determine the height (from the root to the lowest reachable branch)

## Things To Note

For this problem, we're focusing on binary trees. This solution can be modified for trees with more than two potential branches per node

The `BinaryTreeNode` is as follows:

```python
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

Since this solution is done in Python, the problem will look like this:

```python
def height(root):
    # Code
```

## Solution Explained

Because of the qualities of a tree (especially binary trees), a recursive solution comes naturally.

We have to establish  some base cases:

- If `root` is None
  - Return 0
- If the `root` has no children
  - Return 0

Then we have to determine the height of both sides of the tree. This is where the recursive calls come in.

For situations where the left size is larger than the right side, we return the left side. Otherwise, we return the right side's height.

## Full Solution

```python
def height(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    
    leftVal = height(root.left)
    rightVal = height(root.right)

    if leftVal > rightVal:
        return leftVal + 1
    return rightVal + 1
```

## Analysis

In the worst case, all elements of the tree are accessed. Furthermore, we're using the stack since the algorithm is recursive. Based off this, we can say that both the time and space complexity is `O(n)`