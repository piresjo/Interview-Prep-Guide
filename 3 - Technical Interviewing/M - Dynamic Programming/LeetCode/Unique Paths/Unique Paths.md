# Unique Paths

## Problem

## Things To Note

## Solution Explained

This is a DP problem using a 2D array. We have two base cases, if either m or n is 0 (return 0, since there's nowhere to go) or if either m or n is 1 (return 1, since you can only go down/right)

For the solution matrix, create the m * n matrix, and fill in for the base cases. We don't have to worry about the 0 base case, but we need to factor in the 1 base case. Once we do that, than for all the other sections in the matrix, we add the number of paths to get to the space above you and the number of paths to get to the space to the left of you; the sum of those gets you the number of paths for that section of the matrix.

## Solution

```python
def uniquePaths(self, m: int, n: int) -> int:
    if m == 0 or n == 0:
        return 0
    if m == 1 or n == 1:
        return 1
        
    solutionMatrix = [[0] * n] * m
        
    for i in range(0, m):
        solutionMatrix[i][0] = 1
            
    for i in range(0, n):
        solutionMatrix[0][i] = 1
            
    for i in range(1, m):
        for j in range(1, n):
            solutionMatrix[i][j] = solutionMatrix[i-1][j] + solutionMatrix[i][j-1]
                
    return solutionMatrix[m-1][n-1]
```

## Analysis

