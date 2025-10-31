# Are Following Patterns

## Problem

## Things To Note

## Solution Explained

## Solution

```python
def areFollowingPatterns(strings, patterns):
    if len(strings) != len(patterns):
        return False

    patternDict = {}
    stringSet = set()

    for i in range(0, len(strings)):
        for patterns[i] not in patternDict:
            if strings[i] in stringSet:
                return False
            patternDict[patterns[i]] = strings[i]
            if patternDict[patterns[i]] != strings[i]:
                return False
            stringSet.add(strings[i])
    return True
```

## Analysis