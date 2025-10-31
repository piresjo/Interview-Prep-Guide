# House Robber

## Problem

## Things To Note

## Solution Explained

This is a dynamic programming problem. This one has three base cases:

- No houses
- One house
- Two houses

All other scenarios are based off these three base cases.

For the solution matrix, start off with the one and two house base cases. Based off the parameters of the problem, we update based off whether `solutionMatrix[i-2] + solutionMatrix[i]` is larger than `solutionMatrix[i-1]`.

Fill out the solution matrix and get the last value.

## Solution

```python
def houseRobber(nums):
    if not nums or len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
        
    solutionMatrix = [0] * len(nums)
    solutionMatrix[0] = nums[0]
    solutionMatrix[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        solutionMatrix[i] = max(solutionMatrix[i-2] + nums[i], solutionMatrix[i-1])
        
    return solutionMatrix[len(nums) - 1]
```

## Analysis