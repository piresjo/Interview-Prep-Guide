# Majority Number In An Array

## Problem

Given an array nums of size `n`, return the majority element.

## Things To Note 

The majority element is the element that appears more than `n / 2` times. You may assume that the majority element always exists in the array.

Here are the constraints:

- `n == nums.length`
- `1 <= n <= 5 * 104`
- `-10^9 <= nums[i] <= 10^9`
- The input is generated such that a majority element will exist in the array.


## Solution Explained

There are multiple ways to determine the majority number. One easy way would be to use a dictionary to register the number of times we encounter an element. We know that the majority number will appear more than `len(nums) / 2` times, so traversing the populated dict will yield us our majority number.


There is another solution that allows us to not use any memory. [That Will Be Discussed At A Later Time]

## Solution

```python
def majorityElement(nums: List[int]) -> int:
    elementDict = {}

    for num in nums:
        if num not in elementDict:
            elementDict[num] = 1
        else:
            elementDict[num] += 1

    halfN = len(nums) / 2
    returnVal = None

    for k, v in elementDict.items():
        if v > halfN:
            returnVal = k

    return returnVal
```


## Analysis

We have to iterate through `nums` to determine what the majority number is. For our algorithm, we pass through `nums` once to populate the dict. After that, we have to iterate through the dict once. Since we're passing through each one without any nested loops, we can say that the time complexity is linear.

For the above solution, we have to create a dict that is at most size `len(nums)`. This means that in the worst case, we have linear space complexity.