# Determine If A String Is A Permutation Of A Palindrome

## Problem

Given string `strVal`, determine if it is a permutation of a palindrome.

## Things To Note

If a string is a palindrome, the reverse order is the same as the forward order. This leads to a couple things regarding the character distribution of the string:

- If the string has an even number of characters, each unique character has to have an even number of occurrences.
- If the string has an odd number of characters, the above point applies, with the exception of one of the characters.

Furthermore, we only have to worry about if the string is a permutation of a palindrome. In other words, we don't have to worry about the order of the string.

## Solution Explained

We'll need to see how many times each unique character in the string is used. We'll have to use a map. The solution is twofold:

- Populate the map, with they keys being the unique characters and the values being the number of times they are used in the string.
- Go through the key-value pairs, making sure that the distribution rules we defined earlier are being followed.

## Full Solution

```python
def isPermOfPalindrome(strVal):
    isEvenLength = (len(strVal) % 2 == 0)
    oddCountMax = 0 if isEvenLength else 1
    oddCount = 0

    strDict = {}

    for char in strVal:
        if char not in strDict:
            strDict[char] = 1
        else:
            strDict[char] += 1

    for (k, v) in strDict:
        if v %  2 != 0:
            oddCount += 1
            if oddCount > oddCountMax:
                return False
    
    return True
```

## Analysis

In terms of time complexity, it is `O(n)`. There are two passes being made through the string. As for memory, in the worst case, each character has to be added to the map. That means there is a `O(n)` memory complexity.