# Flood Fill

## Problem

You are given an image represented by an `m x n` grid of integers `image`, where `image[i][j]` represents the pixel value of the image. You are also given three integers `sr`, `sc`, and `color`. Your task is to perform a flood fill on the image starting from the pixel `image[sr][sc]`.

Return the modified image after performing the flood fill.

## Things To Note 

To perform a flood fill:
    - Begin with the starting pixel and change its color to `color`
    - Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
    - Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
    - The process stops when there are no more adjacent pixels of the original color to update.

Constraints:
    - `m == image.length`
    - `n == image[i].length`
    - `1 <= m, n <= 50`
    - `0 <= image[i][j], color < 216`
    - `0 <= sr < m`
    - `0 <= sc < n`




## Solution Explained

The process of the flood fill lends itself to using DFS to determine what pixels to change, as well as actually changing the pixel.

We can conceptualize `image` as a graph. `image[sr][sc]` would represent the head node of the graph, and we can traverse vertically and horizontally to find all other connected elements with the same original color as the head.

To better visualize the recursion stack, we'll be defining the stack explicitly. `image[sr][sc]` will be the first element in the stack. If the original color matches `color`, we don't have to do anything. However, if the colors differ, we need to keep track of what the original color of `image[sr][sc]` was and traverse to find all connected pixels of `image[sr][sc]` sharing the original color.

We pop the stack, determine if the original color is the same color as the popped pixel (if not, we pass), then add the pixel above, below, to the left of, and to the right of the popped pixel into the stack. Then we change the color of the popped pixel to `color`. We continue until the stack is empty, and we can return the modified `image`.


## Solution

```python
def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    stack = []
    stack.append((sr, sc))
    originalColor = image[sr][sc]
    if color == originalColor:
        return image

    while len(stack) != 0:
        coordinates = stack.pop()
        if image[coordinates[0]][coordinates[1]] != originalColor:
            pass
        else:
            image[coordinates[0]][coordinates[1]] = color

            if coordinates[0] > 0:
                stack.append((coordinates[0] - 1, coordinates[1]))
            if coordinates[0] < len(image) - 1:
                stack.append((coordinates[0] + 1, coordinates[1]))
            if coordinates[1] > 0:
                stack.append((coordinates[0], coordinates[1] - 1))
            if coordinates[1] < len(image[0]) - 1:
                stack.append((coordinates[0], coordinates[1] + 1))

    return image
```


## Analysis

Let's first look at the time complexity. We can consider the worst case scenario in terms of time: an `image` of a uniform color that needsa to be changed to a different `color`. This ends up with all the elements in `image` (think of them as pixels) being accessed. So, we have a time complexity of `O(n * m)`

As for space, in the worst case, all pixels will be in the recrsion stack, which yields us a space complexity of `O(n * m)`