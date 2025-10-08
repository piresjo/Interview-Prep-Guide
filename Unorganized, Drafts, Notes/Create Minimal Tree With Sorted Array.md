# Create A Minimal Tree With A Sorted Array

## Problem

Given a sorted array `arr`, create a minimal binary search tree. In other words, the tree should be
as short as possible.

## Things To Note

The array is sorted.

The `BinarySearchTreeNode` is as follows:

```python
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

## Solution Explained

The problem lends itself to a recursive solution. Since the array is sorted, you can use the middle element as a good starting point.
Since this is sorted and you're trying to create a binary search tree, you'll then have to deal with the left and right halves.

If we're doing this recursively, we need a base case. Here, it's when the array is empty.

We also want to be mindful of where the array being analyzed begins and where it ends. We can stop the recursion if you can't split in half anymore
without the start and end points not behaving correctly. This will also help us determine when the array gets empty. We'll also need it to determine
midpoints in the recursion steps.

## Full Solution

```python
def createMinBST(arr):
    return createMinBSTHelper(arr, 0, len(arr)-1)

def createMinBSTHelper(arrm, start, end):
    if end < start:
        return None
    
    midPoint = (start + end) / 2
    n = Node(arr[midPoint])
    n.left = createMinBSTHelper(arr, start, mid-1)
    n.right = createMinBSTHelper(arr, mid+1, end)
    return n
```

## Analysis

NEED TO ADD

I think it's linear, though.

Memory is a different story, since recursion is being used and that tends to be more expensive for the stack.
