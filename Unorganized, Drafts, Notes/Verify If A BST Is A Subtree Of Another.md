# Verify If A Binary Search Tree Is A Subtree Of Another

## Problem

Given two trees `t1` and `t2`, determine if `t2` is a subtree of `t1`.

## Things To Note

The `BinarySearchTreeNode` is as follows:

```python
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

## Solution Explained

The problem lends itself to a recursive solution. Generating the subtrees and comparing the trees are both recursive actions.

Let's start with the base cases. There is a base case before we generate or compare any subtrees: when `t2` is `None`.
`None` can be considered a subtree of any tree, so we'll return `True`.

Now to move onto the subtree generation. This will be done recursively, as mentioned above. There are two cases that break the recursion:

- If `t1` is `None` -> In that case, since no tree can be a subtree of `None`, we return `False`
- If `t1` and `t2` are equivalent -> Here, we'll return `True`

Otherwise, we need to run the function for the left and right subtrees until the above is met.

To determine whether or not the trees are equivalent, we'll need another recursive call to check that
the trees are equivalent in structure and content. There are three scenarios where we can break the recursion here:

- Both trees are `None` -> Return `True`
- One of the trees is `None` -> Return `False`
- The data in the nodes being compared don't match -> Return `False`

Otherwise, wee have to keep running this function for the left and right subtrees of each tree.

## Full Solution

```python
def containsTree(t1, t2):
    if t2 is None:
        return True
    return subtree(t1, t2)

def subtree(t1, t2):
    if t1 is None:
        return False
    if t1.data == t2.data and matchTree(t1, t2):
        return True
    
    return subtree(t1.left, t2) or subtree(t1.right, t2)

def matchTree(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 isNone or t2 is None:
        return False
    if t1.data != t2.data:
        return False
    
    return matchTree(t1.left, t2.left) and (t1.right, t2.right)
```

## Analysis

NEED TO ADD
