# Isomorphic Strings

## Problem

Given two strings `s` and `t`, determine if they are isomorphic.

## Things To Note 

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

It might be worthwhile to look at an example:

We have the input values: `s = "egg"`, `t = "add"`

These two strings are isomorphic. The strings `s` and `t` can be made identical by:

- Mapping `'e'` to `'a'`.
- Mapping `'g'` to `'d'`.


Let's also be mindful of the constraints:

- `1 <= s.length <= 5 * 10^4`
- `t.length == s.length`
- `s` and `t` consist of any valid ascii character.


## Solution Explained

This solution will involve creating two dictionaries for `s` and `t`. The keys will be unique characters in `s` and `t`. The values will be the first instance those are found. This will allow us to determine which character in `s` will replace which character in `t`. So long as the first unique locations  for two characters are the same, we can replace it. If they differ, the character in `s` is replacing something else, and so we can return `False`. 

After going through the strings and populating the dictionaries, we can return True if the starting unique positions all match.


## Solution

```python
def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    sDict = {}
    tDict = {}

    for i in range(len(s)):
        if s[i] not in sDict:
            sDict[s[i]] = i
            
        if t[i] not in tDict:
            tDict[t[i]] = i

        if sDict[s[i]] != tDict[t[i]]:
            return False

    return True
```


## Analysis

For time complexity, we're passing through `s` and `t` once. Since both strings are the same size, the loop tells us that the time complexity is linear.

As for space complexity, we have to create two dictionaries and populate them. In the worst case, this could lead to two dictionaries of size `n`. Therefore, the space complexity is linear. 