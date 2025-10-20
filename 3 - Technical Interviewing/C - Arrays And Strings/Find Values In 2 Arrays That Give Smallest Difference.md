# Find Values In 2 Arrays That Give Smallest Difference

## Problem

FEED ME

## Things To Note

FEED ME

## Solution Explained

FEED ME

## Full Solution

```python
def findSmallestDifference(arr1, arr2):
    arr1.sort()
    arr2.sort()
    a = 0
    b = 0
    diff = Int.max

    while a < len(arr1) and b < len(arr2):
        if abs(arr1[a] - arr2[b]) < diff:
            diff = abs(arr[a] - arr2[b])
        
        if arr1[a] < arr2[b]:
            a += 1
        else
            b += 1
    
    return diff
```

## Analysis

FEED ME
