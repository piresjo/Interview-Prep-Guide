# Move Zeroes

## Problem

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.


## Solution Explained

While this isn't a typical two-pointer scenario, we will be using two pointers here. The first pointer will go through all elements in `nums`. The second pointer will point to where the next nonzero value to go. A good starting point for that second pointer would be `0`, since we want all the nonzero values on the left of the array.

Bear in mind we need to keep relative order.

So, we traverse through the array with our first pointer. When we hit a non-zero value, we'll swap `nums[i]` with `nums[nextNonZero]` and then update `nextNonZero` by one. This ensures that if the first element is non-zero, it gets swapped with itself (i.e. nothing changes). This also ensures that relative order is kept and the zero is moved rightward.

As the first pointer goes through the array, the zeroes will percolate to the right.

## Solution

```python
def moveZeroes(nums: List[int]) -> None:
    nextNonZero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[nextNonZero], nums[i] = nums[i], nums[nextNonZero]
            nextNonZero += 1
```

## Analysis

Everything here is being done in-place. Based off that, we can say that the space complexity is linear.

As for time complexity, in the worst case, all `n` elements in the array will be accessed once, indicating a linear time complexity.