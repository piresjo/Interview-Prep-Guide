# 2 Sum

## Problem

Given an array of integers `nums` and an integer `target`, find if there are values in the array that hit that target.

## Things To Note

## Solution Explained

This solution allows us to iterate through the string once

Set a dict. We're looking for compliments to other numbers to get the target

## Solution

```python
def twoSum(nums, target):
    if not nums or not target:
        return []
    complimentDict = {}
    for i in range(0, len(nums)):
        if target - nums[i] in complimentDict:
            return [complimentDict[target - nums[i]], i]
        else:
            complimentDict[nums[i]] = i
    return []
```

## Analysis

For the time complexity, you are going through the array once. Therefore, we have a linear complexity.

As for space, the worst case involves a dictionary that is filled with all the values of the array. You end up with a linear space complexity as well.