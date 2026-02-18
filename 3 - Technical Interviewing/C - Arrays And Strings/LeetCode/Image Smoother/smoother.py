from typing import List


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
