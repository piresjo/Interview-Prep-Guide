# Climbing Stairs

## Problem

## Things To Note

## Solution Explained+

Based off the question, we can do a dynamic programming solution. There are two base cases:

- No steps
- One step

The values for both are `1`

For each subproblem, you just add the previous two, because you can go up one step or two.

## Solution

```python
def stairs(n):
    if n < 2:
        return 1

    answerArray = [-1] * (n+1)
    answerArray[0] = 1
    answerArray[1] = 1
    
    for i in range(2, n+1):
        answerArray[i] = answerArray[i-1] + answerArray[i-2]
    
    return answerArray[n]
```

## Analysis