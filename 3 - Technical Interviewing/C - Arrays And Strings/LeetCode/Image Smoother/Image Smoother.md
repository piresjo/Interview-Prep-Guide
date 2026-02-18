# Image Smoother

## Problem

An image smoother is a filter of the size `3 x 3` that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).

Given an m x n integer matrix `img` representing the grayscale of an image, return the image after applying the smoother on each cell of it.

## Things To Note 

It seems like you can get away with returning a new matrix with the smoothed out pixels. This will allow us to reference the original image.

For the averaging, we're just focusing on the pixel and all the pixels adjacent to it (horizontally, vertically, and diagonally) if they exist.


## Solution Explained

The process is pretty straightforward. We need to smooth out every pixel in the image. That means that for each pixel, we need the average of the pixel and all adjacent pixels (based off the values of the original image).

To perform the smoothing for the pixel, we need to determine the upper, lower, left, and right boundary of the pixels we're getting the average of. This will allow us to handle the edge pixels (where not all adjacent pixels exist). Then we just need to calculate the integer average.

We repeat the process for each pixel in the original image.

For future reference, you'll sometimes encounter lines like these:

```
smoothImage = [[0 for c in range(cols)] for r in range(rows)]
```

These are list comprehensions, which provide a succinct way of generating collections.


## Solution

```python
def imageSmoother(img: List[List[int]]) -> List[List[int]]:
    rows = len(img)
    cols = len(img[0])
    smoothImage = [[0 for c in range(cols)] for r in range(rows)]
    for i in range(rows):
        for j in range(cols):
            smoothImage[i][j] = average(img, i, j)
    return smoothImage


def average(img, row, col):
    totalVal = 0
    count = 0

    topBoundary = max(0, row - 1)
    bottomBoundary = min(len(img), row + 2)
    leftBoundary = max(0, col - 1)
    rightBoundary = min(len(img[0]), col + 2)

    for i in range(topBoundary, bottomBoundary):
        for j in range(leftBoundary, rightBoundary):
            totalVal += img[i][j]
            count += 1

    return totalVal // count
```


## Analysis

This is a solution that requires us to access each element in the matrix multiple times over. Because of the nature of the image smoothing algorithm (with the smoothing being based off the adjacent elements to the element we're smoothing), we can consider those multiple instances to be based off a certain constant. Based off that, for worst case analysis, we can say that the time complexity is `O(n * m)`.

Our solution requires us to return a new matrix of size `n * m`. Based off this alone, for our implementation, the worst case space complexity is `O(n * m)`.