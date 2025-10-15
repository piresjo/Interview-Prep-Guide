# First Duplicate Value In Array

## Problem

Given an array `a`, return the first duplicate value in the array. Otherwise return -1.

## Solution Explained

We can use a set here, since sets only take in unique values. In Python, searching in a set is constant (and so is adding to a set). So, we could add each element to the set. If a new value in the array is in the set, we return that value.

Otherwise, we can only do this in `O(n^2)` time (although the space complexity is now constant).

## Solution

```python
def firstDuplicate(a):
    setVal = set()
    for x in a:
        if x in setVal:
            return x
        setVal.add(x)
    return -1
```

## Analysis

In terms of time complexity, searching in a set is `O(1)`. So, in the worst case, we'll have to search the list `n` number of times. So, the time complexity is `O(n)`.

As for space, in the worst case, we have to fill the set with all of the array's values. So, in the worse case, we're dealing with `O(n)` complexity.