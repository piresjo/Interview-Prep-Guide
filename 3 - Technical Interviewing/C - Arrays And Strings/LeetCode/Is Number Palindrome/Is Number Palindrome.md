# Is Number Palindrome

## Problem

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

## Things To Note

An integer can be considered a palindrome if the digits in reverse order create the same number as the original. For example, `1001` is a palindrome.

Because of the negative sign, and that fact that it can only be in an integer at most once, no negative number is a palindrome.

## Solution Explained

Through the leveraging of remainders to get the digits, we can construct the number by performing some math on `x` and constructing the return value digit by digit in a loop.

## Solution

```python
def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    tempX = x
    reversedNum = 0

    while (tempX > 0):
        digit = tempX % 10
        reversedNum = (reversedNum * 10) + digit
        tempX = tempX // 10
        
    return x == reversedNum
```


## Analysis

When it comes to time complexity, we're looping through the number digit by digit. Similar to the characters in a string, going through the digits gives as a linear time algorithm.

As for space, the space used is constant.