# Intersection Of Numbers In Array

## Problem

Given two integer arrays `nums1` and `nums2`, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

## Things To Note 

An intersection of two arrays entails values that are in both `nums1` and `nums2`

For instance:

```python
[1, 2, 3, 4]
[3, 4, 5, 6]
```

Yields an intersection of:

```python
[3, 4]
```

Here are some constraints to be mindful of:
    - `1 <= nums1.length, nums2.length <= 1000`
    - `0 <= nums1[i], nums2[i] <= 1000`



## Solution Explained

Generally, a simple solution would entail getting all the unique elements in both arrays, and then finding which elements are in both sets of unique elements.

Speaking of sets, we'll be using a couple to get the unique elements in `nums1` and `nums2`. Then we can just check to see if any unique elements in `nums1` are in `nums2` (list access is Python is constant time, if I'm not mistaken).


## Solution

```python
def intersection(nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)

    returnList = []
    for x in nums1:
        if x in nums2:
            returnList.append(x)
    return returnList
```


## Analysis

Because list access is constant in Python, we just need to consider the passing over the unique elements in one of the arrays. The worse case of that would be an array of unique numbers. That yields us a linear time complexity.

Between the creation of the sets and the populating of the `returnList`, in the worst case, there are no intersecting elements. This yields us a linear space complexity.