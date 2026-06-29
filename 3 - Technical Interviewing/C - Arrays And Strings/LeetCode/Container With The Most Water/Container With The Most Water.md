# Container With The Most Water

## Problem

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.


## Solution Explained

At first glance, this looks like two-pointer can be applied. Because we're looking for max area, a good starting point for the pointers would be to:

- Have the left pointer at the first position of the list
- Have the right pointer at the last position of the list

Now we need to determine which pointer to move and where with each step. When going through the `height` list, It would make no sense for the taller of the two sides to move inward; you're more likely to have a smaller line and therefore a smaller area. So, when the left pointer has a smaller side, we move that one in (and vice versa if the right pointer is the smaller one).

We update the max area we find and return the highest area we can get.

## Solution

```python
def maxArea(height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        returnVal = 0

        while i < j:
            area = (min(height[i], height[j])) * (j - i)

            if area > returnVal:
                returnVal = area

            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1

        return returnVal
```


## Analysis

Everything here is being done in-place. Based off that, we can say that the space complexity is linear.

As for time complexity, in the worst case, all `n` elements in the array will be accessed once, indicating a linear time complexity.