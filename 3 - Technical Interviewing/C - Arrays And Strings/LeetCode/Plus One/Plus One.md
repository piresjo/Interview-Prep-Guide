# Plus One

## Problem

You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the `i`th digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading `0`'s.

Increment the large integer by one and return the resulting array of digits.

## Solution Explained

You can go through `digits` backward, adding `1` to the last digit, and handling the carry-over process (adding 1 to the digit before `digit[i]`, continuing that until no more carry-overs are needed)

## Solution

```python
def plusOne(digits: List[int]) -> List[int]:
    end = len(digits) - 1
    digits[end] += 1

    while digits[end] == 10:
        digits[end] = 0
        if (end - 1) < 0:
            digits = [1] + digits
        else:
            digits[end - 1] += 1
            end -= 1

    return digits
```


## Analysis

When it comes to time complexity, we're looping through the number digit by digit, albeit backwards. This gives us a linear time complexity.

As for space, the space used is linear in the worst case (where the handling of 10s goes all the way to the beginning of `digits`). In terms of average case, the complexity is constant.