def arrayMaxConsecutiveSum2(inputArray):
    currSum = 0
    minSum = 0
    result = inputArray[0]
    
    for i in range(0, len(inputArray)):
        currSum += inputArray[i]
        if currSum - minSum > result:
            result = currSum - minSum
        if currSum < minSum:
            minSum = currSum

    return result