# Remove Values From Array In Place

## Problem

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` in-place. The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.

## Things To Note

Consider the number of elements in `nums` which are not equal to `val` be `k`, to get accepted, you need to do the following things:

- Change the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to `val`. The remaining elements of `nums` are not important as well as the size of `nums`.
- Return `k`.


## Solution Explained

We can utilize two pointers. Since all of the non-target elements will be at the beginning of the array, one pointer can keep track of where the next non-target value will be. This pointer can also double as the number of target values in the array

The second pointer will go through all of the elements in the array in a single loop. If the element matches the value, we can just continue. However, we will need to swap array values based on the pointers. The element of position `count` will equal `nums[i]` and we increase `count` for the next non-target value. 

## Solution

```python
def removeElement(nums: List[int], val: int) -> int:
    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1
        
    return count
```

## Analysis

Starting with the space analysis, there are no new arrays being made (or any other data structure, for that matter). We can safely say that this solution is constant in terms of space complexity.

As for time analysis, we're looping through a string once. That alone indicates that this solution is in linear time.