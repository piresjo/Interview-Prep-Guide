# Merge Sorted Array

## Problem

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

## Things To Note

Bear in mind that we're making all the changes in `nums1` because `nums1` is the size of both `nums1` and `nums2` (this is why we have those `m` and `n` values). We also know that everything should be in increasing order.

## Solution Explained

The sorted nature of everything and the fact there are two lists make a two-pointer solution appealing. Our first pointer can be the last position of `nums1` and the second pointer can be the last position of `nums2`. We'll need a third pointer to represent the last position of the final `nums1`, but that will only be used for placement.

Depending on whether `nums1[i] > nums2[j]` or not, we'll either move `i` or `j`. We'll be looping until we reach the beginning of `nums2`.

## Solution

```python
def mergeSorted(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1

    while j >= 0:
        if i >= 0 and nums2[j] < nums1[i]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1 
```

## Analysis

Everything here is being done in-place. Based off that, we can say that the space complexity is linear.

As for time complexity, all elements will have to be accessed. Thankfully, this is only done once. Therefore, we can say that the time complexity is linear (`O(n+m)`).