def findMinFibonacciNumbers(k: int) -> int:
    fibCache = [0, 1]
    while fibCache[-1] < k:
        fibCache.append(fibCache[-1] + fibCache[-2])
        
    index = -1
    minCount = 0
        
    while k != 0:
        if k >= fibCache[index]: 
            minCount += 1
            k -= fibCache[index]
        index -= 1
            
    return minCount