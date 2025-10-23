# Find Profession

## Problem

## Things To Note

## Solution Explained

## Solution

```python
def findProfession(level, pos):
    # The base case is always engineer
    if level == 1:
        return 'Engineer'
        
    # If parent is doctor
    if (findProfession(level - 1, (pos + 1) // 2) == 'Doctor'): 
        if (pos % 2 == 1): 
            return 'Doctor'
        else: 
            return 'Engineer'
            
    # If Parent Is Engineer
    if (pos % 2 == 1): 
        return 'Engineer'
    else: 
        return 'Doctor'
```

## Analysis