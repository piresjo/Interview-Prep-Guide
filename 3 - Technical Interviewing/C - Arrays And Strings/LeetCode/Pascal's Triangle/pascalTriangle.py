from typing import List


def generate(numRows: int) -> List[List[int]]:
    triangle = [[1]]

    for i in range(numRows - 1):
        modifiedRow = [0] + triangle[-1] + [0]
        newRow = []

        for j in range(len(modifiedRow) - 1):
            newRow.append(modifiedRow[j] + modifiedRow[j + 1])
        triangle.append(newRow)

    return triangle
