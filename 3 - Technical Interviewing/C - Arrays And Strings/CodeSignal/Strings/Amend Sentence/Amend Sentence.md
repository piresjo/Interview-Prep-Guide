# Amending Sentences

## Problem

Given a string `s`, change any uppercase characters to lowercase.

## Solution

```python
def amendTheSentence(s):
    returnString = ""
    for i in range(0, len(s)):
        if s[i].lower() != s[i] and i == 0:
            returnString += s[i].lower()
            continue

        if s[i].lower() != s[i] and i != 0:
            returnString += " " + s[i].lower()
        else:
            returnString += s[i]
    return returnString
```

## Analysis

Since we have to check each character in the string, the time complexity for this solution is `O(n)`. As for space complexity, since we are returning a new string (rather than modifying the string in place and returning that), the space complexity is also `O(n)`
