# Reverse Integer

## Problem

Given integer `x`, reverse it (ideally without converting to a string)

## Things To Note

`x` can be any integer. This could lead to the reversed integer breaking the limits of numbers in Python.

## Solution Explained

There are two different ways of handling this: keeping `x` as an integer, or converting `x` into a string.

### Non-String Solution

For the non-string solution, you just need to use integer division and the modulo to get the individual digits and place them in reverse order. Thios will have to be done in a loop.

There is a possibility that the reversed integer will be larger than the size limits for numbers in python. Therefore, you will need to check that. If it surpasses the limit, return 0. If the number is negative, make the reversed number negative. Then return the reversed number.

### String Solution

You will be looping through a stringified version of `x` backwards, created a string of the digits in reverse (and factoring in if the number is negative or not), converting the string to an integer, checking if the reversed integer is within the limits of numbers in Python, making the reversed number negative if `x` is negative, and returning the reversed number.

## Solution

```python
def reverse(x):
    valAsString = str(x)
    newNumber = ""
    makeNegative = False
    for i in range(len(valAsString)-1, -1, -1):
        if valAsString[i] == '-':
            makeNegative = True
        else:
            newNumber += valAsString[i]
        
    returnVal = int(newNumber)
    if makeNegative:
        returnVal *= -1
        
    if returnVal > ((2 ** 31) - 1) or returnVal < (-(2**31)):
        return 0
    
    return returnVal
```

```python
def reverseMethod2(x):
    negative = False
    if x < 0:
        negative = True
        x *= -1
        
    reversedVal = 0
        
    while x > 0:
        reversedVal = (reversedVal * 10) + (x % 10)
        x //= 10
        
        
    if reversedVal < (-2 ** 31) or reversedVal > ((2 ** 31) - 1):
        return 0
        
    if negative:
        return reversedVal * -1
        
    return reversedVal
```

## Analysis

We have to go through the integers of `x` in either solution. Therefore, in terms of time complexity, it is `O(n)`.

The space complexity depends on your solution. If you consider the string based solution, you have to create a string of size `n` (`n` being the number of digits in the number), so the space complexity is linear.

However, if you consider the non-string solution, you're not creating any data structures (in fact, you only create a boolean variable and an integer variable). We can consider the space complexity to be constant.