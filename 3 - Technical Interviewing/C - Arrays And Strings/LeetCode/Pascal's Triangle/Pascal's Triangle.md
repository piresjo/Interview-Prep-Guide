# Pascal's Triangle

## Problem

Given an integer `numRows`, return the first `numRows` of Pascal's triangle.

## Things To Note 

In Pascal's triangle, each number is the sum of the two numbers directly above it (if the left and right above values exist). Because of the nature of Pascal's triangle, we have to explicity set up the top row.

## Solution Explained

We need to explicitly set the first row (which is `[1]`)

Then, for `numRows - 1` steps (if we have `numRows = 1`, this will allow us to skip the generation process and just return what we already have):
- Generate a row used for the addition by appending a trailing and leading `0` to a copy of the previous row in the triangle. This way, we can handle the cases for the numbers at the ends of the row more seamlessly. We'll call this `modifiedRow`
- Generate an empty row. This will get filled out by the addition actions and will then be added to the triangle we're returning
- Going through the elements of `modifiedRow`, add together adjacent elements and append them to the row for the triangle
- Append new row to the triangle

Then we return the triangle

## Solution

```python
def generate(numRows: int) -> List[List[int]]:
    triangle = [[1]]

    for i in range(numRows - 1):
        modifiedRow = [0] + triangle[-1] + [0]
        newRow = []

        for j in range(len(modifiedRow) - 1):
            newRow.append(modifiedRow[j] + modifiedRow[j + 1])
        triangle.append(newRow)

    return triangle
```


## Analysis

When it comes to time complexity, we're doing a loop within a loop. In the outer loop, we're generating the rows. In the inner rows, we are performing the additions to make the rows acceptable for Pascal's triangle. This goes through the elements of our rows (which include the leading and trailing `0` we added). This means we have a quadratic (i.e. `O(n^2)`) time complexity

Because of the generation of the rows for the triangle, we also have a quadratic space complexity