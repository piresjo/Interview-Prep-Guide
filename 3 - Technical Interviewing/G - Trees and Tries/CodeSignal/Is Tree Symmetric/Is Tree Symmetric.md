# Is Tree Symmetric

## Problem

Given the head node of a binary tree `t`, determine if the tree is symmetric

## Things To Note

The tree node is defined as such

```python
class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None
```

Remember, we're dealing with a binary tree, not a BST.

By the way, here is a good example of a symmetric tree:

```python
                1
            /       \
        2               2
      /    \        /       \
    3       4       4       3
```

## Solution Explained

The nature of the question and the qualities of a binary tree gives us a good opportunity to use a recursive solution.

There are three cases that break the recursion:

- The left subtree and the right subtree are `None` -> Return `True`
- Either the left subtree or the right subtree is `None` -> Return `False`
- The values of the left node and the right node don't match -> return `False`

Otherwise, we recurse on the children of the node being looked at, being mindful of what to compare so that we keep symmetry.

## Solution

```python
def isTreeSymmetric(t):
    if not t:
        return True
    return symmetric(t.left, t.right)
    
def symmetric(l, r):
    if not l and not r:
        return True
    if not l or not r:
        return False
        
    if l.value == r.value:
        return symmetric(l.right, r.left) and symmetric(l.left, r.right)
        
    return False
```

## Analysis

In terms of time, in the worst case, we have to go through the entire tree. As a result, the time complexity is `O(n)`

As for space, again, we need to go through the entire tree in the worst case. Because we're doing this recursively, there is a stack cost. Because we have to add to the stack with each node accessed, the space complexity is `O(n)`, just like with time complexity.