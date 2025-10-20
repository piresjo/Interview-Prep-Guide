# Determining If A String Has All Unique Characters

## Problem

Given a string `strVal` of `char`s, determine if the `strVal` is comprised of all unique `char`s.

## Solution With Extra Memory

Using a map or a set, we can check to see if the character is there. If so, then the characters in the string is not unique.

For this solution, we'll be using a map.

```python
def allUniqueChars(strVal):
    charCount = {}
    for char in strVal:
        if char in charCount:
            return False
        else:
            charCount[char] = 1
    return True
```

## Solution Without Extra Memory

There is a way to do this without the extra `O(n)` memory used for the map. Since all the characters are supposed to be unique, if we perform a lexicographic sort of the characters, we can make one pass at the sorted string, checking to see if any two adjacent `chars` are the same or not. The time complexity will now be `O(nlg(n))` since we'll be using quicksort, but memory is now constant.

```python
def allUniqueChars(strVal):
    strVal = quickSort(strVal)
    for i in in range(0, len(strVal)-2):
        if strVal[i] == strVal[i+1]:
            return False
    return True
```
