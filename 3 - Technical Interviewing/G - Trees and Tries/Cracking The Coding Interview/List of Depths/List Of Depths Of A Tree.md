# List Of Depths Of A Tree

## Problem

Return a list of list of values in each row of a binary tree, given the head `TreeNode` `node`.

## Things To Note

This is how the `TreeNode` is defined:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

## Solution Explained

We can  use a slightly modified version of BFS. We'll need to track each level, as well as when we reach the end of a level.

## Solution

```python
def listOfDepths(node):
    if node is None:
        return []
    visibleQueue = []
    visibleList = []
    visibleQueue.append(node)
        
    while len(visibleQueue) > 0:
        sizeVal = len(visibleQueue)
        levelList = []
        for i in range(0, sizeVal):
            temp = visibleQueue.pop(0)
            levelList.append(temp.val)
            if temp.left:
                visibleQueue.append(temp.left)
            if temp.right:
                visibleQueue.append(temp.right)
        visibleList.append(levelList)
                
        
    return visibleList
```

## Analysis

You have to traverse through all nodes in the tree.  On top off that, each node  will have to be added to a queue of some sort for the BST to work. Therefore, both time and space complexity is linear.