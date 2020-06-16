def rotateMatrix(matrix):
    if matrix is None:
        return None

    if len(matrix) == 0:
        return None

    if len(matrix[0]) != len(matrix):
        return None

    lenVal = len(matrix)

    for layer in range(0, lenVal // 2):
        firstVal = layer
        lastVal = lenVal - 1 - layer

        for i in range (firstVal, lastVal):
            offset = i - firstVal
            top = matrix[firstVal][i]

            matrix[firstVal][i] = matrix[lastVal - offset][firstVal]
            matrix[lastVal - offset][firstVal] = matrix[lastVal][lastVal - offset]
            matrix[lastVal][lastVal - offset] = matrix[i][lastVal]
            matrix[i][lastVal] = top

    return matrix

