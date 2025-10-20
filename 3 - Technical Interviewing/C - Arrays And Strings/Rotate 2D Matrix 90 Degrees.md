# Rotate 2D Matrix 90 Degrees

## Problem

Given a 2D `matrix` rotate the values 90 degrees.

## Things To Note

Recall how 2D arrays work.

Here's a visual example.

Let's say we have a 2D array:

```python
[[1, 2, 3, 4],
 [5, 6, 7, 8],
 [9, 10, 11, 12],
 [13, 14, 15, 16]]
```

Rotating, we get:

```python
[[13, 9, 5, 1],
 [14, 10, 6, 2],
 [15, 11, 7, 3],
 [16, 12, 8, 4]]
```

## Solution Explained

FEED ME

## Full Solution

```python
def rotate(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return
    n = len(matrix)
    for layer in range(0, n):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            topVal = matrix[first][i]
            matrix[first][i] = matrix[last-offset][first]
            matrix[last-offset][first] = matrix[last][last-offset]
            matrix[last][last-offset] = matrix[i][last]
            matrix[i][last] = topVal
```

## Analysis

FEED ME
