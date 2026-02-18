# Find Disappeared Numbers In An Array

## Problem

Given an array nums of `n` integers where `nums[i]` is in the range `[1, n]`, return an array of all the integers in the range `[1, n]` that do not appear in nums.

Could you do it without extra space and in `O(n)` runtime? You may assume the returned list does not count as extra space.


## Things To Note 

If there are no disappeared number, each integer will appear once. If there are, there will be multiples of the same digit somewhere.

To illustrate what we're trying to solve, let's look at an example:

```python
[1, 2, 3, 4, 4]
```

In an array without a disappeared number, we should be seeing:

```python
[1, 2, 3, 4, 5]
```

So `5` is the disappeared number.

Here are some constraints to keep in mind:
    - `n == nums.length`
    - `1 <= n <= 105`
    - `1 <= nums[i] <= n`


## Solution Explained

The more trivial solution would involve getting a count of each element in `nums`, then going through the dict to see what vaules we're missing.

The dict-free solution is a bit trickier. 


## Solution

### Solution With Dict

```python
def findDisappearedNumbersAlt(nums: List[int]) -> List[int]:
    numDict = {}
    for i in range(len(nums)):
        numDict[i + 1] = 0

    for num in nums:
        numDict[num] += 1

    res = []

    for key, val in numDict.items():
        if val == 0:
            res.append(key)

    return res
```


### Solution Without Extra Space

```python
def findDisappearedNumbers(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        flipIndex = abs(nums[i]) - 1

        if nums[flipIndex] > 0:
            nums[flipIndex] *= -1

    res = []

    for i in range(len(nums)):
        if nums[i] > 0:
            res.append(i + 1)

    return res
```


## Analysis

In both solutions, we're making a constant number of passes through the elements in `nums`. Therefore, we the time complexity is dependent on the number of elements in `nums`. Therefore, the time complexity is linear.

The implementations have slightly different space complexities. For the solution with a dict, the dict is the same size as `nums`. That indicates to us on its own a linear space complexity. However, in both solutions, we're returning a list of disappeared elements. The worse case would be an array populated with a bunch of the same integer. That ensures that the space of `res` will always be `n - 1`. Therefore, we can say that the dict-free solution has linear space complexity as well. That said, the dict-free solution doesn't use any unnecessary space.