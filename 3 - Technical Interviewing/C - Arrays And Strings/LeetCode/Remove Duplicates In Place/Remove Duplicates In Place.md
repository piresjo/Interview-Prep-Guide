# Remove Duplicates From Array In Place

## Problem

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

## Things To Note

Consider the number of unique elements in `nums` to be `k​​​​​​​​​​​​​​`. After removing duplicates, return the number of unique elements `k`.

The first `k` elements of `nums` should contain the unique numbers in sorted order. The remaining elements beyond index `k - 1` can be ignored.


## Solution Explained

We can utilize two pointers. Since all unique values will be frontloaded in `nums`, we can treat one pointer as:

- The position of the next unique number.
- Since positions in Python start at `0`, we can treat this as the number of unique values in `nums`.

We should be mindful that the first element in `nums` is always unique, so we can make this pointer start at `1`.

We need another pointer that loops through the list. Since we're comparing whether the value to the last acknowledged unique number (always in position `i - 1`), if `nums[j]` doesn't match that, we can place it at the beginning of the list (position `i`, specifically). For the next unique number, we have to increase `i` by `1`.

## Solution

```python
def removeDuplicates(nums: List[int]) -> int:
    i = 1

    for j in range(1, len(nums)):
        if nums[j] != nums[i - 1]:
            nums[i] = nums[j]
            i += 1
    return i 
```

## Analysis

Starting with the space analysis, there are no new arrays being made (or any other data structure, for that matter). We can safely say that this solution is constant in terms of space complexity.

As for time analysis, we're looping through a string once. That alone indicates that this solution is in linear time.