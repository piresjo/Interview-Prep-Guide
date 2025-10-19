# Second Smallest Int In Array

## Problem

Given an array of integers `arr`, find the second smallest integer.

## Solution Explained

Using two variables referencing the smallest and second smallest values in the array, we can do this in one pass.

Set the variables to the maximum value for the data type you're using. Then go through the array, determining both the smallest and second smallest value.

When done, return the variable referencing the second smallest value

## Solution

```python
def secondSmallest(arr):
    if not arr:
        return None
    
    if len(arr) < 2:
        return None

    first = float("int")
    second = float("int")
    for x in arr:
        if x < first:
            second = first
            first = x
        elif x < second and x != first:
            second = x

    if second == float("int"):
        return None
    
    return second
```

## Analysis

This solution only goes through the array once. Based off that, the time complexity is `O(n)`.

As for space, the only space we're allocating is for `first` and `second`. Based off this, the space complexity is constant.
