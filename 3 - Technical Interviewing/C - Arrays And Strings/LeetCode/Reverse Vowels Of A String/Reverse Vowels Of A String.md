# Reverse Vowels In A String

## Problem

Given a string `s`, reverse only all the vowels in the string and return it.

## Things To Note

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in both lower and upper cases, more than once.


## Solution Explained

We can utilize two pointers. The first pointer will be placed at the beginning of the string; the second will be placed at the end. Then have both make their way to the middle.

There are three things to consider:

- String immutability (this depends on the language, but I'll showcase it in the below solution)
- Moving the pointer properly
- Handling swaps properly

Depending on your language, the string might be immutable and you'll need to create another string to return.

As for the next two points, one way to handle pointer movement is to have the first pointer keep going forward until it hits a vowel (or it goes past the second pointer) and move the second pointer backward until one of those conditions are met. Once both pointers are pointing to a vowel, you can swap the characters, move the first pointer forward, and move the second pointer backward to continue the 'traverse-and-swap' process.

The return the modified string.
## Solution

```python
def reverseVowels(s: str) -> str:
    stringList = list(s)
    start = 0
    end = len(s) - 1
    vowels = ['a', 'e', 'i', 'o', 'u']

    while start < end:
        if stringList[start].lower() in vowels and stringList[end].lower() in vowels:
            stringList[start], stringList[end] = stringList[end], stringList[start]
            start += 1
            end -= 1
        else:
            if stringList[start].lower() not in vowels:
                start += 1
            if stringList[end].lower() not in vowels:
                end -= 1
    return "".join(stringList)
```

## Analysis

For this solution, we're returning a new string that's the same size of `s`. This means that the algorithm has linear space complexity.

As for time analysis, We're only making a pass through the string once. This also means that the time complexity is also linear.