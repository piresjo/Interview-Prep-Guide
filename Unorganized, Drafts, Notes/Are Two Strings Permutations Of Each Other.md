# Determine If Two Strings Are Permutations Of Each Other

## Problem

Given two strings `str1` and `str2` determine if they are permutations of each other.

## Things To Note

In order for both strings to be permutations of each other, the character distribution has to be the same. In other words, both strings need to have the same characters being used at the same number of occurrences.

## Solution Explained

We'll need to see how many times each unique character in the strings is used. We'll have to use a map for each string. The solution is twofold:

- Populate the maps, with they keys being the unique characters and the values being the number of times they are used in the string.
- Check to see if both maps are equivalent.

## Full Solution

```python
def isPerm(str1, str2):
    if len(str1) != len(str2):
        return False
    
    str1Dict = {}
    str2Dict = {}

    for char in str1:
        if char not in str1Dict:
            str1Dict[char] = 1
        else:
            str1Dict[char] += 1

    for char in str2:
        if char not in str2Dict:
            str2Dict[char] = 1
        else:
            str2Dict[char] += 1

    return str1Dict == str2Dict
```

## Analysis

In terms of time complexity, it is `O(n)`. There are two passes being made through the string. As for memory, in the worst case, each character has to be added to the map. That means there is a `O(n)` memory complexity.
