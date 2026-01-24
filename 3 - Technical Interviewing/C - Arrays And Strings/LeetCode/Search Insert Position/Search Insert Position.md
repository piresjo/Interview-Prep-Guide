# Search Insert Position

## Problem

Given a list of sorted and unique integers `nums` and an integer `target`, determine the location of `target` if it's in `nums`. If it's not in there, return the position it would need to go.

This needs to be done in `O(lg(n))` time.

## Things To Note

There are some things to keep in mind:

- `nums` is comprised of integers, those elements are unique, and the list is sorted 
- `nums` can't be empty
- We need to do this in logarithmic time

## Solution Explained

The logarithmic time and the fact that `nums` is sorted forces our hand into a binary search solution. We can take advantage of the binary search algorithm to get us the index to return.

First, let's focus on if `target` is within nums. When we eventually hit the `target`, the midpoint we're using in binary search can be returned.

Now let's focus on if `target` isn't. The list is sorted and the elements are unique. We also need to be mindful that lists start with element `0`. Therefore, we need to focus on the left pointer used in binary search. Because of the aspects of `nums`, we can just return the left pointer after the search loop is done.

## Solution

```python
def searchInsert(nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1

    while l <= r:
        midpoint = (l + r) // 2

        if nums[midpoint] == target:
            return midpoint
            
        if nums[midpoint] > target:
            r = midpoint - 1
        else:
            l = midpoint + 1
        
    return l
```


## Analysis

In terms of time, this is binary search with slight modification. In terms of time, it behaves exactly like a standard binary search implementation. Therefore, the time complexity is `O(lg(n))`

When it comes to the space complexity, no new data structures are being created, so the space complexity is linear.