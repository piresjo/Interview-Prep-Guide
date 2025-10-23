# Trapping Rainwater

## Problem

Given the array of height values `height`, determine how much rainwater would be trapped.

## Things To Note

## Solution Explained

You need to get the max left boundary for each section
and the max right boundary for each section. So, create two arrays to house
the left and right heights. `leftHeights[0] = heights[0]` and 
`rightHeights[len(heights)-1] = heights[len(heights)-1]`. For the left heights,
we'll see if the height of the section is bigger than the current max left
boundary, and update as appropriate. Similar thing happens to the right.

However, to correctly determine the trapped rainwater, we need to get
the min between the right and left max boundaries for each section 
(as a visualization, if a bucket has a left side that's two inches high and
a right side that's four inches, the water going past the two inches will
overflow). We also need to subtract the height of the region we're at, since
obviously rain can't be trapped there.

Here's an example:

```python
[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
```

First we want to get the max left boundary

```python
[0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
```

Then the max right boundary

```python
[3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1]
```

Then we want to find the mins of both (otherwise water will spill over)

```python
[0, 1, 1, 2, 2, 2, 2, 3, 2, 2, 2, 1]
```

Then we subtract the height of the rocks from the height of the boundary. This gives us the final array:

```python
[0, 0, 1, 0, 1, 2, 1, 0, 0, 1, 0, 0]
```

Summing this up, we get 6

## Solution

```python
def trap(height):
    if height is None:
        return 0
        
    if len(height) == 0:
        return 0
        
    leftHeights = [0] * len(height)
    rightHeights = [0] * len(height)
        
        
    leftHeights[0] = height[0]
    for i in range(1, len(height)):
        leftHeights[i] = max(leftHeights[i-1], height[i])
        
    rightHeights[len(height) - 1] = height[len(height) - 1]
    for i in range(len(height) - 2, -1, -1):
        rightHeights[i] = max(rightHeights[i+1], height[i])
            
    stored = 0
        
    for i in range(0, len(height)):
        stored += min(leftHeights[i], rightHeights[i]) - height[i]
            
    return stored
```

## Analysis

With respect to time, you have to go through the array(s) twice. This gives us a linear time complexity (`O(n)`)

As for space, you have to create two arrays of size `n` (`n` being the number of elements in the array). So, this gives us a linear space complexity.