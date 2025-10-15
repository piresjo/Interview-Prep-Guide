# Traverse A Tree Layer By Layer

## Problem

Given the head `t` of a binary tree, return a list of all the nodes of the tree, traversed level by level.

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

Based off the problem, we need to perform a level-order traversal. Essentially we're performing a Breadth-First Search on the tree.

Here's what the basic format of the level order traversal algorithm looks like:

```python
def levelOrder(head):
    queue = []
    temp = head

    while temp is not None:
        print str(temp.data) + ' '
        if temp.left is not None:
            queue.append(temp.left)
        if temp.right is not None:
            queue.append(temp.right)
        
        temp = queue.pop(0)
```

## Solution

```python
def traverseTree(t):
    if t is None:
        return []
    queue = []
    returnList = []
    queue.append(t)

    while len(queue) != 0:
        temp = queue.pop(0)
        returnList.append(temp.data)

        if temp.left is not None:
            queue.append(temp.right)
        if temp.right is not None:
```

## Analysis

When it comes to time complexity, we have to traverse through every node of the tree once. So, the time complexity is `O(n)`. As for memory, we need a `queue` and a `returnList` that will be filled with all elements of the tree at one point. Based off that, we can say that the space complexity is `O(n)`.
